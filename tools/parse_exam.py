#!/usr/bin/env python3
"""
parse_exam.py - convert the exam Markdown into questions.json.

    python3 -I tools/parse_exam.py source/software-engineering-fundamentals-exam.md questions.json

Reads the exam body and the answer key at the end of the same file, joins
them by question id, and writes a single JSON file. Prints a report of
anything that did not parse cleanly. Standard library only. The output is
deterministic (no timestamps), so re-running gives an identical file.
"""
import hashlib
import json
import re
import sys
import textwrap
from pathlib import Path

PART_HEAD = re.compile(r'^## Part ([A-J]): (.+?) \((.+)\)\s*$')
SEC_HEAD = re.compile(r'^### ([A-J]-[A-Z])\. (.+?) \((.+)\)\s*$')
Q_HEAD = re.compile(r'^\*\*(?P<id>[A-J]?\d+)\.(?P<title>[^*]*)\*\*(?P<rest>.*)$')
BULLET = re.compile(r'^- \*\*(.+?)\*\*:?\s*(.*)$')
OPT = re.compile(r'(?:^|\s{2})([A-D])\. ')

TYPE_BY_PART = {
    'A': 'multiple_choice', 'B': 'short_answer', 'C': 'code_trace',
    'D': 'coding', 'E': 'system_design', 'I': 'coding', 'J': 'judgment',
}
TYPE_BY_SECTION = {
    'F-A': 'multiple_choice', 'F-B': 'code_trace', 'F-C': 'coding',
    'G-A': 'multiple_choice', 'G-B': 'coding', 'G-C': 'coding',
    'H-A': 'multiple_choice', 'H-B': 'short_answer',
}
# Type choices that are judgment calls (reported so a human can overrule them).
TYPE_REVIEW = {
    'G9': "code review plus a rewrite, typed 'coding'",
    'G10': "refactor plus tests plus a short judgment, typed 'coding'",
}

# Options that only make sense in a fixed position ("All of the above"...).
POSITIONAL = re.compile(
    r'\b(?:all|none|neither|both)\s+of\s+the\s+(?:above|following)\b|\b(?:all|none)\s+of\s+these\b',
    re.I)
# Text that refers to other options by letter ("Both A and B", "option C").
LETTER_REF = re.compile(
    r'\b(?:[Bb]oth|[Ee]ither|[Nn]either)\s+[A-D]\b|\b[A-D]\s+(?:and|or)\s+[A-D]\b'
    r'|\b(?:[Oo]ption|[Cc]hoice|[Aa]nswer)s?\s+[A-D]\b')
# Text that points at another question or an earlier snippet.
CROSS_REF = re.compile(
    r'\b(?:question|exercise|problem)s?\s+[A-J]?\d+\b'
    r'|\b(?:code|snippet|example|function|table|trace|error)\s+above\b'
    r'|\bprevious\s+(?:question|code|snippet|part)\b|\bthe above\b', re.I)


def die(msg):
    print('FATAL: ' + msg, file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------- helpers

def unesc_line(s):
    return re.sub(r'\\([\[\]])', r'\1', s)


def unescape_outside_fences(text):
    out, in_fence = [], False
    for line in text.split('\n'):
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            out.append(line)
        else:
            out.append(line if in_fence else unesc_line(line))
    return '\n'.join(out)


def clean_bold(s):
    return s.replace('**', '').strip()


def cap_first(s):
    s = s.strip()
    return s[:1].upper() + s[1:]


def parse_spec(spec):
    d = {}
    m = re.search(r'(\d+) points', spec)
    d['points'] = int(m.group(1)) if m else None
    m = re.search(r'(\d+) each', spec)
    d['each'] = int(m.group(1)) if m else None
    m = re.search(r'(\d+) minutes', spec)
    d['minutes'] = int(m.group(1)) if m else None
    return d


def parse_table(lines):
    rows = []
    for ln in lines:
        if ln.startswith('|'):
            rows.append([c.strip() for c in ln.strip().strip('|').split('|')])
    return rows[2:]  # drop header and separator


def entry_text(lines):
    if lines and not lines[0].strip():
        return textwrap.dedent('\n'.join(lines[1:])).strip('\n').strip()
    return '\n'.join(lines).strip()


def collect_entries(lines):
    """Split '- **Label:** text' bullets (with their indented/fenced
    continuation lines) from loose paragraphs."""
    entries, extras = [], []
    cur, in_fence = None, False
    for ln in lines:
        s = ln.strip()
        if in_fence:
            (cur['lines'] if cur else extras).append(ln)
            if s.startswith('```'):
                in_fence = False
            continue
        if s.startswith('```'):
            in_fence = True
            (cur['lines'] if cur else extras).append(ln)
            continue
        m = BULLET.match(ln)
        if m:
            cur = {'label': m.group(1).rstrip(':').strip(), 'lines': [m.group(2)]}
            entries.append(cur)
            continue
        if cur is not None and (s == '' or ln.startswith(' ')):
            cur['lines'].append(ln)
            continue
        cur = None
        if s:
            extras.append(ln)
    return entries, extras


# ------------------------------------------------------------ exam body

def split_options(line):
    ms = list(OPT.finditer(line))
    letters = [m.group(1) for m in ms]
    if letters != ['A', 'B', 'C', 'D']:
        return None
    texts = []
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(line)
        texts.append(unesc_line(line[m.end():end].strip()))
    return texts


def parse_part(pid, name, spec, lines):
    part = {'id': pid, 'name': name, **parse_spec(spec)}
    part['points_each'] = part.pop('each')
    part.update({'intro': '', 'rubric_each': None, 'stretch': None,
                 'grading_scheme': None, 'grading_notes': [], 'sections': []})
    questions, intro = [], []
    section, cur, in_fence = None, None, False

    def sink():
        return cur['lines'] if cur else intro

    for ln in lines:
        s = ln.strip()
        if in_fence:
            sink().append(ln)
            if s.startswith('```'):
                in_fence = False
            continue
        if s.startswith('```'):
            in_fence = True
            sink().append(ln)
            continue
        if s == '---':
            continue
        m = SEC_HEAD.match(ln)
        if m:
            sp = parse_spec(m.group(3))
            section = {'id': m.group(1), 'name': m.group(2), 'points': sp['points'],
                       'points_each': sp['each'], 'minutes': sp['minutes'],
                       'question_ids': []}
            part['sections'].append(section)
            cur = None
            continue
        m = Q_HEAD.match(ln)
        is_e = pid == 'E' and ln.startswith('**Design a URL shortener**')
        if m or is_e:
            pts = mins = None
            if m:
                qid, title, first = m.group('id'), m.group('title').strip(), m.group('rest').strip()
                tm = re.search(r'\((\d+) points, (\d+) minutes\)', title)
                if tm:
                    pts, mins = int(tm.group(1)), int(tm.group(2))
                    title = (title[:tm.start()] + title[tm.end():]).strip()
                title = title.strip().rstrip('.').strip()
                if qid.isdigit():
                    qid = pid + qid
            else:
                qid, title, first = 'E1', 'Design a URL shortener', s
            cur = {'id': qid, 'part': pid, 'section': section['id'] if section else None,
                   'title': title or None, '_points': pts, 'suggested_minutes': mins,
                   'rubric': None, 'lines': [first]}
            questions.append(cur)
            continue
        if ln.startswith('**Rubric per'):
            part['rubric_each'] = re.sub(r'^\*\*[^*]+\*\*\s*', '', ln).strip()
            cur = None
            continue
        if ln.startswith('**Rubric:**'):
            if cur is None:
                part['grading_notes'].append('Unattached rubric line: ' + clean_bold(ln))
            else:
                cur['rubric'] = ln[len('**Rubric:**'):].strip()
            continue
        if ln.startswith('**Stretch'):
            part['stretch'] = clean_bold(ln)
            cur = None
            continue
        sink().append(ln)

    part['intro'] = unescape_outside_fences('\n'.join(intro).strip())
    return part, questions


def finish_question(q, part, issues):
    sec = next((x for x in part['sections'] if x['id'] == q['section']), None)
    q['type'] = TYPE_BY_SECTION[q['section']] if q['section'] else TYPE_BY_PART[q['part']]
    body = q.pop('lines')
    q['options'] = None
    if q['type'] == 'multiple_choice':
        nonblank = [l for l in body if l.strip()]
        if len(nonblank) != 2:
            issues['errors'].append(f"{q['id']}: expected a prompt line and an options line, found {len(nonblank)} lines")
            q['prompt'] = unescape_outside_fences('\n'.join(nonblank[:-1]).strip())
            texts = None
        else:
            q['prompt'] = unescape_outside_fences(nonblank[0].strip())
            texts = split_options(nonblank[1])
        if texts is None:
            issues['errors'].append(f"{q['id']}: could not split options A-D")
            texts = []
        if len(set(texts)) != len(texts):
            issues['errors'].append(f"{q['id']}: duplicate option text (answer mapping by text would be ambiguous)")
        q['options'] = [{'text': t, 'pinned': False} for t in texts]
    else:
        q['prompt'] = unescape_outside_fences('\n'.join(body).strip())

    # points: own header > section "each" > part "each" > section points / count > part points / count
    pts = q.pop('_points')
    if pts is None:
        for src in (sec, part):
            if src and src.get('points_each') is not None:
                pts = src['points_each']
                break
    if pts is None:
        for src in (sec, part):
            if src and src.get('points') and src['_count'] and src['points'] % src['_count'] == 0:
                pts = src['points'] // src['_count']
                break
    if pts is None:
        issues['errors'].append(f"{q['id']}: could not work out points")
        pts = 0
    q['points'] = pts
    if q['rubric'] is None and part['rubric_each']:
        q['rubric'] = part['rubric_each']


# ----------------------------------------------------------- answer key

def apply_mc_line(text, pid, qmap, issues):
    head, _, missed = text.partition('Commonly missed:')
    for n, letter in re.findall(rf'\b{pid}(\d+) ([A-D])\b', head):
        q = qmap.get(f'{pid}{n}')
        if q is None:
            issues['warnings'].append(f'key mentions unknown question {pid}{n}')
        else:
            q['_key_letter'] = letter
    for n, letter, expl in re.findall(rf'\b{pid}(\d+) ([A-D]) \(([^)]*)\)', head):
        if f'{pid}{n}' in qmap:
            qmap[f'{pid}{n}']['explanation'] = cap_first(expl)
    for sentence, qid in re.findall(rf'([^.]*\(({pid}\d+)\)[^.]*\.)', head):
        if qid in qmap:
            qmap[qid]['explanation'] = sentence.strip()
    for n, expl in re.findall(rf'\b{pid}(\d+) \(([^)]*)\)', missed):
        if f'{pid}{n}' in qmap:
            qmap[f'{pid}{n}']['explanation'] = 'Commonly missed: ' + expl


def apply_key(pid, heading, key_lines, qmap, part, issues):
    note = re.search(r'\(([^()]*)\)\s*$', heading)
    if note:
        part['grading_scheme'] = note.group(1)

    if pid == 'E':  # one big question: the whole section is the model answer
        qmap['E1']['model_answer'] = unescape_outside_fences('\n'.join(key_lines).strip())
        return

    entries, extras = collect_entries(key_lines)
    for ln in extras:
        s = ln.strip()
        if re.fullmatch(r'\d+ [A-D](?:, \d+ [A-D])*\.?', s):
            for n, letter in re.findall(r'(\d+) ([A-D])', s):
                q = qmap.get(f'{pid}{n}')
                if q is None:
                    issues['warnings'].append(f'key mentions unknown question {pid}{n}')
                else:
                    q['_key_letter'] = letter
        elif s.startswith('**'):
            part['grading_notes'].append(clean_bold(s))

    last_q = None
    for e in entries:
        label, text = e['label'], entry_text(e['lines'])
        if re.fullmatch(r'[A-J]-[A-Z]', label):
            apply_mc_line(text, pid, qmap, issues)
            last_q = None
            continue
        m = re.match(r'^([A-J]\d+)', label)
        qid = m.group(1) if m else ('A' + label if pid == 'A' and label.isdigit() else None)
        if qid:
            q = qmap.get(qid)
            if q is None:
                issues['warnings'].append(f'key entry {label!r} has no matching question')
                continue
            text = unescape_outside_fences(text)
            if pid == 'A':
                q['explanation'] = text
            else:
                rest = label[len(qid):].strip(' :') if m else ''
                if rest and not rest.startswith('(') and not re.fullmatch(r'[a-z]', rest):
                    text = f'**{cap_first(rest)}:**\n{text}'
                q['model_answer'] = (q['model_answer'] + '\n\n' + text) if q['model_answer'] else text
            last_q = q
        elif last_q is not None and pid != 'A':
            last_q['model_answer'] += f'\n\n**{label}:** ' + unescape_outside_fences(text)
        else:
            issues['warnings'].append(f'Part {pid}: key entry {label!r} was not attached to a question')


# ------------------------------------------------------------------ main

def main():
    if len(sys.argv) != 3:
        die('usage: parse_exam.py <exam.md> <questions.json>')
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    raw = src.read_text(encoding='utf-8')
    exam_text, sep, key_text = raw.partition('\n# Answer key and grading guide')
    if not sep:
        die('answer key heading not found')
    lines = exam_text.split('\n')
    issues = {'errors': [], 'warnings': [], 'notes': []}

    # --- header, rules, parts table
    first_part = next(i for i, l in enumerate(lines) if PART_HEAD.match(l))
    head = lines[:first_part]
    title = next(l[2:].strip() for l in head if l.startswith('# '))
    rules_at = next(i for i, l in enumerate(head) if l.startswith('## Rules'))
    description = ' '.join(l.strip() for l in head[1:rules_at] if l.strip())
    rule_entries, _ = collect_entries([l for l in head[rules_at + 1:] if not l.startswith('|')])
    rules = [{'label': e['label'], 'text': entry_text(e['lines'])} for e in rule_entries]
    table = {}
    for cells in parse_table(head):
        if cells[0] in 'ABCDEFGHIJ' and cells[0]:
            table[cells[0]] = {'tests': cells[1], 'questions': int(cells[2]),
                               'points': int(cells[3]), 'minutes': int(re.search(r'\d+', cells[4]).group())}
    total_points = sum(t['points'] for t in table.values())
    total_minutes = sum(t['minutes'] for t in table.values())

    # --- split into parts
    idx = [i for i, l in enumerate(lines) if PART_HEAD.match(l)] + [len(lines)]
    parts, questions = [], []
    for a, b in zip(idx, idx[1:]):
        m = PART_HEAD.match(lines[a])
        part, qs = parse_part(m.group(1), m.group(2), m.group(3), lines[a + 1:b])
        t = table.get(part['id'])
        if not t:
            issues['errors'].append(f"Part {part['id']} missing from the summary table")
            continue
        part['tests'] = t['tests']
        part['question_count'] = len(qs)
        part['_count'] = len(qs)
        for s in part['sections']:
            s['question_ids'] = [q['id'] for q in qs if q['section'] == s['id']]
            s['_count'] = len(s['question_ids'])
        for what in ('points', 'minutes'):
            if part[what] != t[what]:
                issues['errors'].append(f"Part {part['id']}: heading says {part[what]} {what}, table says {t[what]}")
        if len(qs) != t['questions']:
            issues['errors'].append(f"Part {part['id']}: parsed {len(qs)} questions, table says {t['questions']}")
        for q in qs:
            q['model_answer'] = None
            q['explanation'] = None
            q['correct'] = None
            q['correct_original_letter'] = None
            q['group'] = None
            q['flags'] = []
            finish_question(q, part, issues)
        parts.append(part)
        questions.extend(qs)
    qmap = {q['id']: q for q in questions}
    if len(qmap) != len(questions):
        issues['errors'].append('duplicate question ids')

    # --- answer key
    klines = key_text.split('\n')
    kidx = [i for i, l in enumerate(klines) if l.startswith('## ')] + [len(klines)]
    closing, bands = '', []
    pmap = {p['id']: p for p in parts}
    for a, b in zip(kidx, kidx[1:]):
        h = klines[a][3:].strip()
        body = klines[a + 1:b]
        pm = re.match(r'Part ([A-J])\b', h)
        if pm:
            apply_key(pm.group(1), h, body, qmap, pmap[pm.group(1)], issues)
        elif h.startswith('Final scoring'):
            for cells in parse_table(body):
                r = re.match(r'(\d+) to (\d+)', cells[0])
                lo, hi = (int(r.group(1)), int(r.group(2))) if r else (0, int(re.search(r'\d+', cells[0]).group()) - 1)
                bands.append({'min': lo, 'max': hi, 'label': cells[0], 'message': cells[1]})
            closing = ' '.join(l.strip() for l in body if l.strip() and not l.startswith('|'))

    # --- join key letters to option TEXT, detect position-dependent options
    for q in questions:
        for fld in ('prompt',):
            if CROSS_REF.search(q[fld]):
                issues['warnings'].append(f"{q['id']}: prompt may refer to another question/snippet: {CROSS_REF.search(q[fld]).group(0)!r}")
        if q['type'] == 'multiple_choice':
            letter = q.pop('_key_letter', None)
            if letter is None:
                issues['errors'].append(f"{q['id']}: no answer in the key")
            elif len(q['options']) == 4:
                i = 'ABCD'.index(letter)
                q['correct'] = q['options'][i]['text']
                q['correct_original_letter'] = letter
            for o in q['options']:
                if POSITIONAL.search(o['text']):
                    o['pinned'] = True
                    q['flags'].append('positional_option_pinned')
                if LETTER_REF.search(o['text']) or LETTER_REF.search(q['prompt']):
                    q['flags'].append('refers_to_options_by_letter')
        else:
            if not q['model_answer']:
                issues['errors'].append(f"{q['id']}: no model answer / grading hints found in the key")
        if q['id'] == 'E1':
            q['flags'].append('synthetic_id')
        if q['id'] in TYPE_REVIEW:
            q['flags'].append('type_is_a_judgment_call')
            issues['notes'].append(f"{q['id']}: {TYPE_REVIEW[q['id']]}")
        q['flags'] = sorted(set(q['flags']))

    # --- totals
    for p in parts:
        got = sum(q['points'] for q in questions if q['part'] == p['id'])
        if got != p['points']:
            issues['errors'].append(f"Part {p['id']}: question points add to {got}, heading says {p['points']}")
        for s in p['sections']:
            g = sum(q['points'] for q in questions if q['section'] == s['id'])
            if s['points'] is not None and g != s['points']:
                issues['errors'].append(f"Section {s['id']}: question points add to {g}, heading says {s['points']}")
    got_total = sum(q['points'] for q in questions)
    if got_total != total_points:
        issues['errors'].append(f'total points {got_total} != table total {total_points}')

    # --- output
    order = ['id', 'part', 'section', 'type', 'points', 'title', 'prompt', 'options', 'correct',
             'correct_original_letter', 'model_answer', 'explanation', 'rubric',
             'suggested_minutes', 'group', 'flags']
    out_questions = [{k: q[k] for k in order} for q in questions]
    out_parts = []
    for p in parts:
        p = {k: v for k, v in p.items() if not k.startswith('_')}
        p['sections'] = [{k: v for k, v in s.items() if not k.startswith('_')} for s in p['sections']]
        out_parts.append(p)
    result = {
        'meta': {
            'title': title,
            'description': description,
            'source_file': src.name,
            'source_sha256': hashlib.sha256(raw.encode('utf-8')).hexdigest(),
            'total_points': total_points,
            'total_minutes': total_minutes,
            'rules': rules,
        },
        'parts': out_parts,
        'score_bands': bands,
        'closing_note': closing,
        'questions': out_questions,
    }
    dst.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    # Same data as a script file: browsers block fetch() of local files on
    # file://, but a <script src> works everywhere (file://, GitHub Pages).
    js = dst.with_suffix('.js')
    js.write_text('// Generated by tools/parse_exam.py from questions.json. Do not edit.\n'
                  'window.EXAM_DATA = ' + json.dumps(result, ensure_ascii=False) + ';\n',
                  encoding='utf-8')

    # --- report
    print(f'{"Part":<5}{"Name":<42}{"Qs":>4}{"Pts":>5}{"Min":>5}  types')
    for p in parts:
        qs = [q for q in questions if q['part'] == p['id']]
        types = {}
        for q in qs:
            types[q['type']] = types.get(q['type'], 0) + 1
        print(f'{p["id"]:<5}{p["name"][:40]:<42}{len(qs):>4}{p["points"]:>5}{p["minutes"]:>5}  '
              + ', '.join(f'{v} {k}' for k, v in types.items()))
    print(f'TOTAL {len(questions)} questions, {got_total} points, {total_minutes} minutes '
          f'({total_minutes // 60} h {total_minutes % 60} min); table says {total_points} points')
    flagged = [q for q in questions if q['flags']]
    print('\nFLAGGED QUESTIONS:')
    for q in flagged:
        print(f"  {q['id']}: {', '.join(q['flags'])}")
    if not flagged:
        print('  (none)')
    print('\nNOTES:')
    for n in issues['notes']:
        print('  ' + n)
    print('\nWARNINGS:')
    for w in issues['warnings']:
        print('  ' + w)
    if not issues['warnings']:
        print('  (none)')
    print('\nERRORS:')
    for e in issues['errors']:
        print('  ' + e)
    if not issues['errors']:
        print('  (none)')
    sys.exit(1 if issues['errors'] else 0)


if __name__ == '__main__':
    main()
