# Software Engineering Fundamentals Exam

A self-contained, closed-book exam web app for the 101-question Software Engineering Fundamentals Exam. It uses plain HTML, CSS, and JavaScript; there is no framework, backend, build step, or third-party dependency.

## Run it

- Open `index.html` directly in a browser, or
- Publish the project directory with GitHub Pages.

The app loads `questions.js` as a script so question data also works when the page is opened with `file://`. Attempts and graded history are stored in that browser's local storage. If the browser blocks local storage, the app will warn that progress cannot be persisted.

## Regenerate the exam data

Edit the Markdown source, then run this from the project directory:

```sh
python3 -I tools/parse_exam.py source/software-engineering-fundamentals-exam.md questions.json
```

The parser deterministically writes both `questions.json` and `questions.js`. Do not edit either generated data file by hand.

## Grading, results, and privacy

Multiple-choice questions are graded automatically. All other answers are self-graded against the model answers, rubrics, and any grading notes in the exam. Results and history remain in the browser unless you explicitly download or export them; nothing is uploaded.

The result downloads are named `results-YYYY-MM-DD-HHMM.json` and `results-YYYY-MM-DD-HHMM.md`. Your browser chooses the download location. If you want to keep them in the project, move them into a local `results/` folder; that folder is ignored by Git. **Never commit or upload result files or history exports.** Browser local storage can be lost when browser data is cleared, so export history for a private backup.

## Limitations

- The exam is self-graded except for multiple-choice questions; scores depend on honest, consistent use of the rubrics.
- Attempts and history are local to one browser profile and device. There is no account, server backup, or synchronization.
- The question bank and answer key are included in `questions.js` and are readable in the page source. GitHub Pages is public hosting, not a way to secure the answers.
- The app cannot save downloads directly into the project directory; use the browser's download flow and move files yourself if needed.
# exam-app (swe)
