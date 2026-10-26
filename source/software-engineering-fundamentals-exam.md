# The Software Engineering Fundamentals Exam

Prepared for Aisosaibi. A closed-book, self-graded exam covering the fundamentals that separate engineers who understand their craft from engineers who only copy patterns.

## Rules and time budget

- **Total score:** 400 points
- **Total time:** about 8 hours 50 minutes of working time, plus breaks. Do it in four sittings, ideally on separate days: Parts A to C (about 2 hours), Parts D and E (about 2.5 hours), Parts F to H (about 2.5 hours), then Parts I and J (about 2 hours).
- **Closed book:** no AI, no search, no notes. An IDE is allowed for Parts D and I only if you turn off autocomplete. Better still, write on paper or a plain editor first, then run it.
- **Language:** use Java, Python or JavaScript for Part D. Pick the one you would defend in an interview.
- **Grade honestly.** Use the answer key at the end only after you finish every part.

| Part | What it tests | Questions | Points | Time |
| --- | --- | --- | --- | --- |
| A | Multiple choice across the core of computing | 30 | 60 | 40 min |
| B | Short answers (explain it in your own words) | 10 | 30 | 40 min |
| C | Code tracing and prediction | 5 | 30 | 35 min |
| D | Coding exercises | 5 | 60 | 120 min |
| E | System design | 1 | 20 | 35 min |
| F | Frontend and the browser | 15 | 40 | 45 min |
| G | Design, code quality and code review | 10 | 40 | 45 min |
| H | Systems, infrastructure and security | 16 | 40 | 50 min |
| I | Advanced algorithms | 4 | 40 | 75 min |
| J | Engineering judgment and communication | 5 | 40 | 45 min |
|  | **Total** |  | **400** | **about 8 h 50 min** |

---

## Part A: Multiple choice (60 points, 2 each, 40 minutes)

Pick one answer per question.

**1.** Worst-case time to binary search a sorted array of n items:

A. O(n)  B. O(n log n)  C. O(log n)  D. O(1)

**2.** Which statement about a hash map is correct?

A. Lookup is always O(1)  B. Lookup is always O(log n)  C. Lookup is O(1) on average but degrades with many collisions  D. Lookup is always O(n)

**3.** Which combination gives an LRU cache with O(1) get and put?

A. Sorted array  B. Hash map plus doubly linked list  C. Binary search tree  D. Stack

**4.** Breadth-first search on a graph is naturally implemented with:

A. A stack  B. Recursion only  C. A priority queue  D. A queue

**5.** A sorting algorithm is *stable* when:

A. It runs in O(n log n)  B. It sorts in place  C. Equal elements keep their original relative order  D. It uses no extra memory

**6.** Appending to a dynamic array (ArrayList, Python list, JS array) is:

A. O(1) amortized  B. O(n) every time  C. O(log n)  D. O(n²)

**7.** Threads within the same process share:

A. Their stacks  B. Their registers  C. The heap and global data  D. Their program counters

**8.** Which is NOT a necessary condition for deadlock?

A. Mutual exclusion  B. Hold and wait  C. Circular wait  D. Preemption of resources

**9.** A race condition is best described as:

A. The program slowing down under load  B. A result that depends on the interleaving of unsynchronized access to shared state  C. Two threads running at the same time  D. A null pointer crash

**10.** Which is true about TCP?

A. It does not guarantee ordering  B. It is connectionless  C. It provides a reliable, ordered byte stream  D. It is the protocol DNS always uses

**11.** Which HTTP methods are defined as idempotent?

A. POST, PATCH  B. GET only  C. POST, PUT  D. GET, PUT, DELETE

**12.** What is the difference between 401 and 403?

A. 401 means not authenticated; 403 means authenticated but not permitted  B. 401 means forbidden; 403 means not logged in  C. They are interchangeable  D. 401 is a server error

**13.** The correct way to store user passwords:

A. SHA-256 with no salt  B. AES-encrypt them and keep the key beside the data  C. bcrypt or Argon2 with a per-user salt  D. Base64 encode them

**14.** CORS restrictions are enforced by:

A. The browser  B. The server firewall  C. DNS  D. TLS

**15.** A LEFT JOIN returns:

A. Only rows that match in both tables  B. All rows from the left table, with NULLs where the right has no match  C. The Cartesian product  D. Only unmatched rows

**16.** The 'I' in ACID (isolation) means:

A. Data survives a crash  B. Concurrent transactions do not see each other's partial work, to the degree the isolation level promises  C. A transaction is all-or-nothing  D. Constraints are always valid

**17.** Adding a database index:

A. Is a free speedup  B. Speeds up both reads and writes  C. Only helps unique columns  D. Speeds up reads at the cost of slower writes and extra storage

**18.** The primary defense against SQL injection:

A. Manually escaping quotes  B. Hiding error messages  C. Parameterized queries  D. Client-side validation

**19.** The 'N+1 query problem' is:

A. A query returning N+1 columns  B. One query to fetch a list, then one more query per item in the list  C. An index on N columns  D. A join of N tables

**20.** Third normal form (3NF) is often summarized as:

A. Every column is indexed  B. No NULLs allowed  C. Non-key attributes depend on the key, the whole key, and nothing but the key  D. No table has more than three columns

**21.** Why is rebasing and force-pushing a shared branch dangerous?

A. It rewrites history that other people have already based work on  B. It deletes the remote repository  C. Rebase never produces conflicts  D. Force-push is always safe

**22.** The Liskov Substitution Principle says:

A. A subclass must add methods  B. Subtypes must be usable wherever the base type is expected without breaking correctness  C. A class should have one reason to change  D. Depend on abstractions, not concretions

**23.** The main benefit of dependency injection:

A. Faster execution  B. Lower memory use  C. Dependencies are passed in rather than created inside, so code is easier to test and swap  D. It removes the need for interfaces

**24.** A common reason to favor composition over inheritance:

A. It couples classes less and lets behavior be swapped  B. It is always faster  C. Java requires it  D. Inheritance is banned in OOP

**25.** A good unit test is:

A. Hitting the real network  B. Dependent on running order  C. Reading the wall clock  D. Fast, isolated and deterministic

**26.** Time complexity of: `for i in range(n): for j in range(i): work()`

A. O(n)  B. O(n log n)  C. O(n²)  D. O(2^n)

**27.** In most languages, `0.1 + 0.2 == 0.3` evaluates to:

A. true  B. false, because of binary floating point representation  C. a runtime error  D. depends on the OS

**28.** In Python, `def f(x, items=[]): items.append(x); return items`. Calling `f(1)` then `f(2)`:

A. Returns \[1\] then \[2\]  B. Raises an error  C. Returns \[1\] then \[1, 2\], because the default list is created once  D. Returns \[\] both times

**29.** In Java, if you override `equals`, you must also override:

A. hashCode  B. toString  C. clone  D. compareTo

**30.** In JavaScript, `typeof null` returns:

A. 'null'  B. 'undefined'  C. 'object'  D. 'number'

---

## Part B: Short answers (30 points, 3 each, 40 minutes)

Answer in 4 to 8 sentences each. Precision beats length.

**B1.** Walk through what happens from the moment you type a URL and press Enter until the page is rendered. Cover at least DNS, TCP, TLS, HTTP and rendering.

**B2.** Distinguish a process from a thread, and concurrency from parallelism. Give one example where concurrency helps even on a single core.

**B3.** Define dirty read, non-repeatable read and phantom read. Which isolation level prevents which?

**B4.** Why should money never be stored as a floating-point number? What should you use instead?

**B5.** Java and Python are both 'pass by object reference' in practice. Explain the difference between *mutating* an argument and *reassigning* the parameter, and what the caller sees in each case.

**B6.** What is a pure function, and why does purity make code easier to test and reason about?

**B7.** Distinguish authentication from authorization. Compare server-side sessions with stateless JWTs: one strength and one weakness of each.

**B8.** State the CAP theorem in plain language. Give one example of a system that chooses availability and one that chooses consistency during a partition.

**B9.** Describe your Git workflow for a feature from branch to merge. What do you do when you hit a merge conflict, and how do you decide which side is right?

**B10.** The naive recursive Fibonacci is `fib(n) = fib(n-1) + fib(n-2)`. State its time and space complexity, explain why it is slow, and give two ways to fix it.

---

## Part C: Trace and predict (30 points, 6 each, 35 minutes)

Predict the exact output. Do not run the code first. Then explain *why* in one or two sentences, because the explanation is worth half the points.

**C1. Python**

```python
def add(x, bucket=[]):
    bucket.append(x)
    return bucket

print(add(1))
print(add(2))
print(add(3, []))
print(add(4))
```

**C2. JavaScript**

```javascript
console.log('A');
setTimeout(() => console.log('B'), 0);
Promise.resolve().then(() => console.log('C'));
(async () => {
  console.log('D');
  await null;
  console.log('E');
})();
console.log('F');
```

**C3. Java**

```java
Integer a = 127, b = 127;
Integer c = 128, d = 128;
String s1 = new String("hi");
String s2 = "hi";
System.out.println(a == b);
System.out.println(c == d);
System.out.println(s1 == s2);
System.out.println(s1.equals(s2));
```

**C4. Python**

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])

funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])
```

**C5. SQL**

Table `orders(id, customer, amount)` has these rows: (1, A, 50), (2, A, 70), (3, B, 20), (4, C, 90), (5, C, 10), (6, C, 30).

```sql
SELECT customer, SUM(amount) AS total
FROM orders
GROUP BY customer
HAVING SUM(amount) > 60
ORDER BY total DESC;
```

What rows come back, in what order? What would change if `HAVING` were replaced with `WHERE`?

---

## Part D: Coding exercises (60 points, 12 each, 120 minutes, about 24 minutes each)

Use one language throughout. Write clean, readable code with sensible names. **Write at least three test cases per exercise**, including an edge case. State the time and space complexity of your solution in a comment.

**Rubric per exercise (12 points):** correctness 5, complexity appropriate 3, edge cases and tests 2, readability 2.

**D1. Two Sum, indices.** Given an array of integers and a target, return the indices of the two numbers that add to the target, or an empty result if none exist. Target: O(n) time.

**D2. Balanced brackets.** Given a string containing `()[]{}` and other characters, return true if every bracket is correctly matched and nested. Ignore non-bracket characters. Example: `{[a(b)c]}` is valid; `([)]` is not.

**D3. LRU Cache.** Implement a class with `get(key)` and `put(key, value)`, both O(1), with a fixed capacity. `get` of a missing key returns -1. When full, `put` evicts the least recently used key. Do not use a built-in ordered-dictionary shortcut (such as `OrderedDict` or `LinkedHashMap`). Build the linked list yourself.

**D4. Merge intervals.** Given a list of intervals like `[[1,3],[2,6],[8,10],[15,18]]`, merge all overlapping ones and return the result. Your input may be unsorted. Decide, and document, whether touching intervals like `[1,2]` and `[2,3]` merge.

**D5. Rate limiter.** Implement `allow(user_id, timestamp)` that returns true if the user has made fewer than N requests in the trailing window of W seconds, and records the request when allowed. Memory must not grow forever for inactive users. Write tests that prove the window slides (not resets) correctly.

**Stretch (no points, for self-assessment):** explain how D5 would change if the service ran on ten servers.

---

## Part E: System design (20 points, 35 minutes)

**Design a URL shortener** (like bit.ly) that handles 100 million new URLs per month and 10 times as many redirects.

Deliver a written design in your own words, containing:

1. Functional and non-functional requirements (state your assumptions).
2. The API (endpoints, methods, status codes).
3. The data model.
4. How you generate short IDs, and how you avoid collisions.
5. A **plain-text architecture diagram** (boxes and arrows in ASCII).
6. Where you cache, what you cache, and how you invalidate.
7. What breaks first at 10 times the load, and what you would do about it.
8. Two things you deliberately chose *not* to build, and why.

**Rubric:** requirements and estimation 4, API and data model 4, ID generation 4, scaling and caching 4, trade-offs and failure thinking 4.

---

## Part F: Frontend and the browser (40 points, 45 minutes)

Every engineer ships to a browser sooner or later. Part F tests the web platform, JavaScript's sharp edges, React fundamentals and web security.

### F-A. Multiple choice (24 points, 2 each, 15 minutes)

**F1.** An element has `width: 200px; padding: 20px; border: 5px solid;` with the default `box-sizing: content-box`. Its total rendered width is:

A. 200px  B. 240px  C. 250px  D. 225px

**F2.** Which selector has the highest specificity?

A. `.card p`  B. `#nav a`  C. `div.card.active`  D. `p:first-child`

**F3.** What is the difference between `display: none` and `visibility: hidden`?

A. Both remove the element from layout  B. `display: none` removes it from layout; `visibility: hidden` keeps its space  C. `visibility: hidden` removes it from layout; `display: none` keeps its space  D. They are identical

**F4.** A closure in JavaScript is:

A. A function with no parameters  B. A function together with the variables from the scope where it was defined  C. A function defined inside a class  D. A function that runs immediately

**F5.** Inside an arrow function, the value of `this` is:

A. Decided by how the function is called  B. Always the global object  C. Inherited lexically from the enclosing scope  D. Always the object before the dot

**F6.** Event delegation means:

A. Calling `preventDefault` on every event  B. Using `setTimeout` to delay handlers  C. Attaching one listener to an ancestor and relying on bubbling to handle events from many children  D. Removing all listeners after use

**F7.** Why does React need a stable `key` on list items?

A. For styling  B. For SEO  C. To wire up click handlers  D. So React can match items across renders and keep state and DOM nodes with the right item

**F8.** In React, `useEffect(() => {...}, [])` runs:

A. After every render  B. Once after the first mount (and twice in development StrictMode)  C. Before the first render  D. Whenever any prop changes

**F9.** The correct defense against cross-site scripting (XSS) is:

A. Relying on HTTPS  B. Validating input only in the browser  C. Escaping output according to its context, avoiding `innerHTML` with untrusted data, and setting a Content Security Policy  D. Hashing passwords

**F10.** A solid defense against cross-site request forgery (CSRF):

A. SameSite cookies plus anti-CSRF tokens  B. Relying on CORS alone  C. Relying on HTTPS alone  D. Hashing passwords

**F11.** Which Core Web Vital measures visual stability (content jumping around while loading)?

A. LCP  B. CLS  C. INP  D. TTFB

**F12.** Server-side rendering mainly improves:

A. Time to first meaningful content and crawlability for content pages, at the cost of server work  B. Bundle size, always  C. It removes the need for hydration  D. Database speed

### F-B. Trace and predict (8 points, 4 each, 10 minutes)

**F13. React.** What does the page show after 5 seconds, and why? Then fix it.

```jsx
function Counter() {
  const [n, setN] = useState(0);
  useEffect(() => {
    const id = setInterval(() => setN(n + 1), 1000);
    return () => clearInterval(id);
  }, []);
  return <p>{n}</p>;
}
```

**F14. JavaScript.** Assume strict mode (an ES module). Predict the result of each `console.log`, and explain.

```javascript
const obj = {
  n: 1,
  regular() { return this.n; },
};
const { regular } = obj;
console.log(obj.regular());
console.log(regular());
```

### F-C. Coding (8 points, 20 minutes)

**F15. Debounced search with stale-response protection.** In plain JavaScript (or a React hook if you prefer), write `createSearch({ delay, fetchResults, onState })` that returns a `search(query)` function.

1. Calls to `search` are debounced: only the last call within `delay` milliseconds triggers `fetchResults(query, signal)`.
2. When a newer search starts, the older request is aborted through its `AbortController` signal, and its late response must never overwrite the newer one.
3. `onState` receives `{ status, data, error }` where status is `idle`, `loading`, `success` or `error`. An empty or whitespace-only query resets to `idle` without touching the network.
4. Aborted requests are not reported as errors.

In two sentences, explain why a plain debounce alone is not enough.

**Rubric:** debounce 2, abort and stale-response protection 3, states and empty query 2, clarity 1.

---

## Part G: Design, code quality and code review (40 points, 45 minutes)

World-class engineers are distinguished less by what they can write than by what they notice in code someone else wrote, and by how easy their own code is to change.

### G-A. Multiple choice (16 points, 2 each, 10 minutes)

**G1.** Which class most clearly violates the Single Responsibility Principle?

A. `Invoice`, which computes its totals  B. `UserService`, which validates input, writes to the database and sends emails  C. `Money`, a value object  D. `EmailSender`, which sends email

**G2.** The Open/Closed Principle says:

A. Every class must be abstract  B. New behavior should be added by extending the system, not by editing tested code  C. Classes may never change  D. Interfaces must be public

**G3.** The Strategy pattern is best described as:

A. A way to guarantee a single instance  B. A way to build objects step by step  C. Putting interchangeable algorithms behind a common interface so they can be chosen at runtime  D. A way to notify observers of changes

**G4.** The same `if (type == A) ... else if (type == B)` chain appears in five places in the codebase. This most likely signals:

A. Excellent explicitness  B. A missing index  C. A performance problem  D. A missing abstraction that polymorphism could provide

**G5.** Best REST endpoint to fetch order 42 belonging to customer 7:

A. `GET /getOrder?id=42`  B. `POST /orders/get`  C. `GET /customers/7/orders/42`  D. `GET /customers/7/getOrders/42`

**G6.** For a large, constantly changing list, which pagination approach is more stable and faster at depth?

A. Offset pagination (`LIMIT 20 OFFSET 100000`)  B. Cursor (keyset) pagination  C. Return everything  D. Random sampling

**G7.** Under semantic versioning, a backward-incompatible API change should bump:

A. The major version  B. The minor version  C. The patch version  D. Nothing

**G8.** Refactoring means:

A. Changing behavior to add features  B. Rewriting from scratch  C. Restructuring code without changing its external behavior, ideally protected by tests  D. Renaming files only

### G-B. Code review (14 points, 20 minutes)

**G9.** You are reviewing this pull request. List **at least ten distinct problems** (bugs, security, concurrency, performance, design, readability). Then rank the **top three** you would block the merge on, and rewrite the most dangerous function safely.

```python
import sqlite3, hashlib

DB = sqlite3.connect('app.db')

def register(u, p, e):
    c = DB.cursor()
    c.execute("SELECT * FROM users WHERE name='" + u + "'")
    if c.fetchall():
        return 'exists'
    h = hashlib.md5(p.encode()).hexdigest()
    c.execute("INSERT INTO users VALUES ('" + u + "','" + h + "','" + e + "')")
    DB.commit()
    print('registered ' + u + ' with password ' + p)
    return 'ok'

def get_orders(uid, page):
    out = []
    for o in DB.execute('SELECT * FROM orders').fetchall():
        if o[1] == uid:
            out.append(o)
    return out[page*10:(page+1)*10]
```

**Rubric:** issues found (10 or more = 8 points, scaled below that), ranking and reasoning 3, quality of the safe rewrite 3.

### G-C. Refactoring (10 points, 15 minutes)

**G10.** Refactor this code so that adding a new customer type requires **no edits to existing code**. Write the **characterization tests first** (they must pass before and after). Then, in three sentences, say when this refactoring would be over-engineering and you would leave the `if` chain alone.

```java
double price(String type, double base) {
    if (type.equals("STUDENT")) return base * 0.5;
    else if (type.equals("SENIOR")) return base * 0.7;
    else if (type.equals("VIP")) return base * 0.8 - 5;
    else return base;
}
```

**Rubric:** design (interface plus implementations or a map of strategies, with a safe default) 4, tests that lock in behavior including the unknown type 3, honest judgment about over-engineering 3.

---

## Part H: Systems, infrastructure and security (40 points, 50 minutes)

Code that works on your laptop is the beginning. This part tests how software behaves when it is deployed, scaled, attacked and broken.

### H-A. Multiple choice (24 points, 2 each, 15 minutes)

**H1.** `chmod 640 notes.txt` gives:

A. Owner read and write, group read, others nothing  B. Owner read, write and execute, group read, others nothing  C. Everyone read and write  D. Owner read, group write, others nothing

**H2.** What is the difference between a Docker image and a container?

A. A container is a stored template; an image is a running process  B. An image is a read-only template; a container is a running instance of it  C. They are the same thing  D. A container is a virtual machine with its own kernel

**H3.** Continuous delivery versus continuous deployment:

A. They mean the same thing  B. Delivery ships every commit automatically; deployment requires approval  C. In delivery every change is releasable and shipping is a human decision; in deployment every change that passes the pipeline ships automatically  D. Deployment applies only to mobile apps

**H4.** A cache stampede is:

A. A cache with too little memory  B. A cache returning stale data  C. Two keys colliding  D. Many requests missing on an expired hot key at once and all hitting the database; mitigated by locking, request coalescing or jittered expiry

**H5.** A message queue promises *at-least-once* delivery. Consumers must therefore be:

A. Fast  B. Idempotent, so processing a message twice has the same effect as once  C. Single-threaded  D. Stateless

**H6.** The purpose of an idempotency key on a payment request:

A. To encrypt the request  B. To authenticate the caller  C. To let the server recognize a retry and avoid repeating the charge  D. To speed up processing

**H7.** The best retry strategy for a failing network call:

A. Retry immediately in a tight loop  B. Exponential backoff with jitter and a retry cap  C. Retry once an hour  D. Never retry

**H8.** A circuit breaker:

A. Encrypts traffic  B. Balances load  C. Caches responses  D. Stops calls to a failing dependency for a while so callers fail fast and the dependency can recover

**H9.** The three pillars of observability are:

A. Logs, metrics and traces  B. Tests, builds and deploys  C. CPU, memory and disk  D. Alerts, pages and dashboards

**H10.** An endpoint has p99 latency of 800 ms. This means:

A. The average request takes 800 ms  B. The slowest request ever took 800 ms  C. 99 percent of requests complete in 800 ms or less  D. 99 percent of requests take exactly 800 ms

**H11.** A canary deployment:

A. Deploys to all servers at once  B. Runs two full environments and switches all traffic instantly  C. Restarts servers one at a time  D. Sends a small share of traffic to the new version first and widens it while metrics stay healthy

**H12.** A user changes `/orders/124` to `/orders/125` in the address bar and sees another customer's order. This is:

A. XSS  B. Broken access control (an insecure direct object reference)  C. CSRF  D. SQL injection

### H-B. Short answers (16 points, 4 each, 35 minutes)

**H13.** Your API's p99 latency tripled right after a deploy. Walk through your investigation in order: what you look at, what you rule out, and when you roll back instead of debugging.

**H14.** A client retries a payment request after a network timeout. Explain how you guarantee the customer is charged exactly once. Cover the idempotency key, where it is stored, and what happens on a race between two identical requests.

**H15.** Compare rolling, blue-green and canary deployments. When would you choose each, and why are database schema migrations the hardest part of any rollback?

**H16.** Explain horizontal versus vertical scaling. Name three things that make a service hard to scale horizontally, and how you would fix each.

---

## Part I: Advanced algorithms (40 points, 75 minutes)

These are the problems that separate engineers who recognize patterns from engineers who only memorized one example. Use one language, state the complexity of each solution, and write at least three tests per problem. If you use JavaScript, you must write your own heap, which is itself part of the test.

**Rubric per problem (10 points):** correctness 5, complexity 2, edge cases and tests 2, explanation 1.

**I1. Shortest paths (Dijkstra).** Given `n` nodes labeled `0..n-1`, a list of directed weighted edges `[u, v, w]` with non-negative weights, and a source `s`, return the shortest distance from `s` to every node (infinity if unreachable). Use a min-heap. Example: `n = 5`, edges `[[0,1,4],[0,2,1],[2,1,2],[1,3,1],[2,3,5]]`, `s = 0` gives `[0, 3, 1, 4, inf]`.

Then answer: what is the complexity, why do negative edge weights break the algorithm, and what do you use instead?

**I2. Coin change.** (a) Given coin denominations and a target amount, return the *minimum* number of coins needed, or -1 if impossible. Use dynamic programming and write the recurrence in a comment. Example: coins `[1, 5, 6, 9]`, amount 11 gives 2 (5 + 6). Explain why the greedy approach fails on this example. (b) Return the *number of distinct combinations* that make the amount. Example: coins `[1, 2, 5]`, amount 5 gives 4.

**I3. Course schedule.** There are `n` courses. Each pair `[a, b]` means course `b` must be taken before course `a`. Return one valid order to take all courses, or an empty list if a cycle makes it impossible. Example: `n = 4`, prerequisites `[[1,0],[2,0],[3,1],[3,2]]` gives `[0, 1, 2, 3]` (or `[0, 2, 1, 3]`). With `[[0,1],[1,0]]` the answer is empty. Required: O(V + E).

**I4. Kth largest in a stream.** Implement a class constructed with `k` and an initial list of numbers, with `add(val)` returning the current kth largest element after inserting `val`. Each `add` must run in O(log k). Example: `k = 3`, initial `[4, 5, 8, 2]`; then `add(3)` gives 4, `add(5)` gives 5, `add(10)` gives 5, `add(9)` gives 8, `add(4)` gives 8.

Explain why a sorted array would be too slow, and what you would do if the stream were too large for one machine.

---

## Part J: Engineering judgment and communication (40 points, 45 minutes)

The best engineers debug fast, estimate sanely, write clearly and make good decisions when information is missing. No code is run in this part. Write in full sentences.

**J1. Read the stack trace (10 points, 12 minutes).** Here is the code and the error it produced.

```python
def average(scores):
    return sum(scores) / len(scores)

def class_report(classes):
    return {name: average(s) for name, s in classes.items()}

print(class_report({'A': [80, 90], 'B': []}))
```

```
Traceback (most recent call last):
  File "report.py", line 7, in <module>
    print(class_report({'A': [80, 90], 'B': []}))
  File "report.py", line 5, in class_report
    return {name: average(s) for name, s in classes.items()}
  File "report.py", line 2, in average
    return sum(scores) / len(scores)
ZeroDivisionError: division by zero
```

Explain how you read a trace (which end you start from and why), name the root cause, then give **three different fixes** (for example returning a sentinel, raising a domain-specific error, skipping the entry). Pick one, defend the choice, and say which test you would add.

**J2. Estimation (6 points, 8 minutes).** A photo-sharing app has 2 million daily active users. Each uploads 1.5 photos a day, averaging 3 MB each. Estimate the storage added per day and per year, and the average and peak upload bandwidth (assume peak is 5 times the average). Show your arithmetic. Name two things you would do to cut storage cost.

**J3. Explain it to a founder (8 points, 8 minutes).** Your non-technical founder says: 'Login with Google is just a button. Why can't it ship today?' Write a reply of at most 150 words that is honest, free of jargon, explains what the real work is, and offers two options with their trade-offs.

**J4. Commit message and pull request (6 points, 7 minutes).** You fixed a bug where the cart total ignored discount codes whenever an item's quantity was above 1. You added tests and also renamed one confusing helper function. Write the commit message (a short subject line plus a body) and a pull request description a reviewer can act on.

**J5. Decision under pressure (10 points, 10 minutes).** It is two days before a release. You find a bug that corrupts roughly 0.1 percent of user records. The fix touches core code with no automated tests. Product wants to ship on time. State your decision, what you do first, whom you tell and what you tell them, what you refuse to do, and how you would reduce the risk of the fix.

---

# Answer key and grading guide

**Do not read this until you have finished every part.**

## Part A answers

1 C, 2 C, 3 B, 4 D, 5 C, 6 A, 7 C, 8 D, 9 B, 10 C, 11 D, 12 A, 13 C, 14 A, 15 B, 16 B, 17 D, 18 C, 19 B, 20 C, 21 A, 22 B, 23 C, 24 A, 25 D, 26 C, 27 B, 28 C, 29 A, 30 C.

Notes on the commonly missed ones:

- **2:** Java 8 and later convert long collision chains into balanced trees, giving O(log n) worst case, but 'always O(1)' is still wrong.
- **8:** Deadlock needs *no* preemption. If resources could be forcibly taken, the cycle could be broken.
- **11:** PUT and DELETE repeated give the same final state. POST creates a new thing each time. PATCH may or may not be idempotent depending on the operation.
- **14:** The server sends CORS headers, but the browser enforces them. curl and Postman ignore CORS.
- **16:** Durability is the 'D' and atomicity is the 'A'. Mixing them up is the usual mistake.
- **28:** The default is evaluated once, when the function is defined. Use `None` as the default and create the list inside.
- **29:** Equal objects must produce equal hash codes, or hash-based collections break.

**Scoring:** 2 points each. Below 24/30 correct means you have core vocabulary gaps worth fixing before anything else.

## Part B key points (3 points: 1 for each of three core ideas, partial credit allowed)

- **B1:** DNS resolves the name to an IP (cache, then resolver chain). TCP three-way handshake. TLS handshake negotiates keys and verifies the certificate. HTTP request, server response. Browser parses HTML, builds the DOM and CSSOM, fetches sub-resources, then lays out and paints. Bonus: CDN, HTTP caching, keep-alive.
- **B2:** A process has its own address space; threads share their process's memory. Concurrency is structuring work to make progress on several tasks in overlapping time; parallelism is literally executing at the same instant on multiple cores. Single-core example: a server switching tasks while one waits on disk or network I/O.
- **B3:** Dirty read: reading uncommitted data. Non-repeatable read: the same row read twice gives different values because another transaction committed in between. Phantom: the same query returns a different set of rows. Read Committed blocks dirty reads; Repeatable Read also blocks non-repeatable reads; Serializable blocks phantoms too. Note that real databases vary (PostgreSQL's Repeatable Read also prevents phantoms).
- **B4:** Binary floats cannot represent most decimal fractions exactly, so errors accumulate. Use integer minor units (kobo or cents) or a decimal type such as `BigDecimal` or `Decimal`, and store the currency.
- **B5:** The reference is copied. Mutating the object through the parameter is visible to the caller. Reassigning the parameter only changes the local copy of the reference; the caller's variable is unchanged.
- **B6:** Same inputs always give the same output, with no side effects. It needs no setup or mocks to test, can be cached, is safe to run in parallel, and is easy to reason about in isolation.
- **B7:** Authentication proves who you are; authorization decides what you may do. Sessions: easy to revoke, but need shared server state. JWTs: stateless and scale easily, but are hard to revoke before expiry and dangerous if stored carelessly.
- **B8:** During a network partition you must choose between consistency (refuse some requests) and availability (answer, possibly with stale data). Examples vary: a bank ledger prefers consistency; a social feed or shopping cart prefers availability.
- **B9:** Branch from an up-to-date main, small commits with clear messages, push, open a pull request, review, run CI, merge. For a conflict, understand *both* changes' intent (read the history or ask the author), combine them deliberately, rerun tests. Never accept 'ours' or 'theirs' blindly.
- **B10:** Time O(2^n) (more precisely about O(1.6^n)), space O(n) for the call stack. It recomputes the same subproblems repeatedly. Fixes: memoization (O(n) time) and bottom-up iteration (O(n) time, O(1) space). Bonus: matrix exponentiation for O(log n).

## Part C answers (3 points for the output, 3 for the explanation)

- **C1:** `[1]`, `[1, 2]`, `[3]`, `[1, 2, 4]`. The default list is shared across calls that do not pass their own list.
- **C2:** `A D F C E B`. Synchronous code runs first (A, D, then F; the async function runs synchronously until its first `await`). Then the microtask queue drains (C, then E). The timer callback is a macrotask and runs last (B).
- **C3:** `true`, `false`, `false`, `true`. Small Integer values (-128 to 127) are cached, so `==` compares the same object. 128 is boxed as separate objects. `new String` creates a distinct object; `equals` compares content.
- **C4:** `[2, 2, 2]` then `[0, 1, 2]`. Lambdas capture the *variable* `i`, not its value at creation time. The default argument freezes the value.
- **C5:** Rows: `C, 130` then `A, 120`. B totals 20 and is filtered out. Replacing `HAVING` with `WHERE SUM(...)` is an error, because `WHERE` runs before grouping and cannot use aggregates.

## Part D grading hints

- **D1:** Single pass with a hash map from value to index. Check for the complement *before* inserting the current value (this handles duplicates such as `[3,3]` with target 6). O(n) time, O(n) space.
- **D2:** A stack and a map of closing to opening brackets. Edge cases: empty string, a closing bracket first, leftover openers at the end. O(n).
- **D3:** Hash map from key to node, plus a doubly linked list with sentinel head and tail nodes. Every `get` and `put` moves the node to the front. Eviction removes the node before the tail and its map entry. Edge cases: capacity 1, updating an existing key, a missing key.
- **D4:** Sort by start, then sweep, merging when the next start is at most the current end (or strictly less, if you decided touching intervals stay separate). O(n log n) from the sort. Edge cases: empty input, a single interval, fully nested intervals such as `[1,10]` and `[2,3]`.
- **D5:** Per-user queue of timestamps. On each call, drop timestamps older than `timestamp - W`, then allow only if the size is below N. Cleanup for inactive users needs a periodic sweep or lazy eviction. Edge cases: exactly on the window boundary, out-of-order timestamps, N = 0. Stretch: use a shared store such as Redis with atomic operations, and accept either a small inconsistency or the cost of coordination.

**Red flags that cost points:** O(n²) where O(n) was possible, no edge-case tests, mutating inputs without saying so, single-letter variable names everywhere, and code that only works for the example given.

## Part E: what a strong answer contains

- **Estimation:** 100M writes per month is about 40 writes per second on average; 1 billion reads per month is about 400 reads per second on average, with peaks perhaps 10 times higher. This is a read-heavy system and the numbers are small enough that one well-designed database is plausible at first.
- **API:** `POST /urls` returns 201 with the short code; `GET /{code}` returns a 301 or 302 redirect (and you should be able to explain the trade-off: 301 is cacheable and cuts load, 302 keeps analytics accurate); 404 for unknown codes, 410 for expired ones.
- **Data model:** code (primary key), long URL, created at, expiry, optional owner.
- **ID generation:** options include a base62-encoded counter or database sequence (no collisions, but predictable), random codes with a collision check, or pre-generated key ranges handed to each server. The answer should say how many characters are needed: 7 characters in base62 gives about 3.5 trillion codes.
- **Cache:** an in-memory cache such as Redis in front of the database for hot codes; entries are effectively immutable, so invalidation mostly means expiry and deletion.
- **What breaks first:** the cache hit ratio and database read capacity. Fix with read replicas, a CDN, and sharding by code.
- **Deliberate omissions:** for example, custom analytics dashboards, or user accounts at launch. Good engineers name what they cut.

Example of the text diagram style that earns full marks for item 5:

```
Client --> Load Balancer --> App Servers --> Cache (Redis)
                                  |                |
                                  v                v (miss)
                            ID Generator      Database (primary)
                                                   |
                                              Read Replicas
```

## Part F answers

- **F-A:** F1 C (200 + 40 + 10 = 250), F2 B (an id selector outranks any number of classes), F3 B, F4 B, F5 C, F6 C, F7 D, F8 B, F9 C, F10 A, F11 B, F12 A. Commonly missed: F5 (arrow functions have no `this` of their own) and F8 (the empty dependency array means once per mount, not once per page).
- **F13:** It shows 1 and stays at 1. The effect runs once, and its closure captured `n = 0`, so every tick calls `setN(0 + 1)`. Fix: `setN(c => c + 1)` (a functional update). Re-creating the interval on every change of `n` also works but is wasteful.
- **F14:** `1`, then a `TypeError` (cannot read properties of undefined, reading `n`). `this` depends on how a function is called; destructuring detaches the method from its object, and in strict mode `this` is `undefined`. Fix: call it through the object, use `bind`, or define it as an arrow function in a class field.
- **F15:** Full marks need: one timer cleared on each call; one `AbortController` per request, with the previous one aborted when a new search starts; ignoring `AbortError` instead of reporting it; an empty query that clears the timer, aborts anything in flight and emits `idle`. The two-sentence answer: debounce reduces how many requests are sent, but it does nothing about *responses* arriving out of order. A slow older response can land after a faster newer one and overwrite it, so stale responses must be cancelled or ignored.

## Part G answers

- **G-A:** G1 B, G2 B, G3 C, G4 D, G5 C, G6 B, G7 A, G8 C. Offset pagination (G6) gets slower the deeper you go and skips or repeats rows when data changes underneath it.
- **G9 problems to find:**
  - **Security:** SQL injection in both queries; unsalted MD5 for passwords; the password is printed to the log; the 'exists' reply allows username enumeration; no input validation; `get_orders` performs no authorization check, so any `uid` is accepted.
  - **Correctness and concurrency:** the check-then-insert race (use a UNIQUE constraint and handle the `IntegrityError`); one shared global connection opened at import time; no transaction handling or error handling; `INSERT` and `SELECT *` rely on column order and positional indexes like `o[1]`.
  - **Performance:** `get_orders` loads the whole table and filters and paginates in Python; it needs `WHERE user_id = ?` with `LIMIT`, and an index on that column.
  - **Readability and design:** one-letter names, the magic number 10, magic return strings instead of exceptions, mixed concerns in one function, no tests.
- **Top three to block on:** SQL injection, password handling (weak hash plus logging it), missing authorization. A strong rewrite looks like this:

```python
def register(conn, username, password, email):
    validate(username, password, email)
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        with conn:
            conn.execute(
                'INSERT INTO users (name, password_hash, email) VALUES (?, ?, ?)',
                (username, pw_hash, email),
            )
    except sqlite3.IntegrityError:
        raise UsernameTaken(username)
```

- **G10:** A `DiscountStrategy` interface (or a map from type to strategy) with a default that returns the base price, so a new type is a new class or entry, not an edit. Characterization tests: STUDENT 100 gives 50, SENIOR 100 gives 70, VIP 100 gives 75, an unknown type 100 gives 100. A sharp candidate also notices that VIP at a base of 5 gives -1, and decides explicitly whether to preserve or fix that. Over-engineering: three stable cases, in one place, rarely changing, with one team owning it. A `switch` is clearer. Refactor when cases multiply, change often, are owned by different teams or need runtime configuration.

## Part H answers

- **H-A:** H1 A, H2 B, H3 C, H4 D, H5 B, H6 C, H7 B, H8 D, H9 A, H10 C, H11 D, H12 B.
- **H13 (4 points):** Check what changed (deploy markers, feature flags, config). Use traces to find which span got slower (database, a downstream service, garbage collection, CPU saturation). Compare traffic, error rate and saturation. Check slow-query logs and locks. If users are hurting now and the deploy is the leading suspect, roll back first and debug after. Then reproduce, fix, and add an alert or test so it cannot recur. Communicate throughout.
- **H14:** The client sends a unique idempotency key per logical payment. The server stores the key, a fingerprint of the request and the result under a UNIQUE constraint, in the same transaction as the charge record. Two racing identical requests: one insert wins; the other returns the stored result or a 409 while the first is in progress. The same key with a different payload is rejected. Pass a derived key to the payment provider too, and expire stored keys after a defined window.
- **H15:** Rolling replaces instances gradually (cheap, but old and new versions run side by side, so they must be compatible). Blue-green keeps two full environments and switches traffic at once (instant rollback, double the cost). Canary sends a small slice of traffic first (best for risky changes where you have good metrics). Migrations are hard because switching code back does not undo changed data. The safe pattern is expand then contract: add backward-compatible schema, deploy code that handles both, backfill, then remove the old shape later.
- **H16:** Vertical scaling makes one machine bigger (simple, but capped and a single point of failure). Horizontal scaling adds machines (needs stateless services). Blockers and fixes: in-memory session state (use a shared store or stateless tokens); files on local disk (use object storage); a single-writer database or hot rows (replicas, sharding, queues); scheduled jobs running on every instance (leader election or a dedicated scheduler).

## Part I grading hints

- **I1:** Distances start at infinity; a heap holds (distance, node); when a popped entry is staler than the recorded distance, skip it; otherwise relax each outgoing edge. O((V + E) log V). Negative edges break the guarantee that a popped node's distance is final. Use Bellman-Ford (O(VE), also detects negative cycles). Edge cases: unreachable nodes, zero-weight edges, parallel edges, `n = 1`.
- **I2a:** `dp[0] = 0; dp[a] = min(dp[a - c] + 1)` over coins `c <= a`; unreachable stays infinity and becomes -1. O(amount × coins) time, O(amount) space. Greedy picks 9 + 1 + 1 (three coins) where the optimum is 5 + 6 (two). **I2b:** `ways[0] = 1`, coin loop on the *outside*, amount loop inside: `ways[a] += ways[a - coin]`. Swapping the loops counts ordered sequences instead of combinations, which is the classic mistake. Expected result: 4.
- **I3:** Kahn's algorithm: compute in-degrees, queue the zeros, pop and decrement neighbors. If fewer than `n` courses are output, there is a cycle, so return an empty list. A DFS with three colors is equally valid. O(V + E). Edge cases: no prerequisites, duplicate pairs, a self-dependency like `[0, 0]` (a cycle), a disconnected graph.
- **I4:** A min-heap holding the k largest values; the root is the answer. Constructor: push everything and pop until the size is k. `add`: push, pop if the size exceeds k, return the root. O(log k). A sorted array costs O(n) per insert. For a stream too big for one machine, each shard keeps its own top k and a coordinator merges them; for an approximate answer, use a quantile sketch. Edge cases: fewer than k items so far, duplicates, negatives, `k = 1`.

## Part J grading hints

- **J1:** Read from the bottom: the last line says *what* happened, the frame above it says *where*, and walking upward finds the first caller you control that supplied the bad input. Root cause: `average` assumes a non-empty list and class B is empty. Three fixes: return a sentinel (hides the problem, and 0 is misleading), raise a domain error (loud and correct, but the caller must handle it), skip or mark the empty class in `class_report` (usually best when 'no data' differs from zero). Any defended choice earns marks. Tests: an empty list, mixed classes, and `average([])`.
- **J2:** 2M × 1.5 = 3M photos per day; × 3 MB = 9 TB per day; × 365 is about 3.3 PB per year (before replication, which multiplies it). Average upload is 9,000,000 MB / 86,400 s, about 104 MB/s or 0.83 Gbit/s; at 5 times that, about 520 MB/s or 4.2 Gbit/s. Cost cuts: resize and compress on upload, generate thumbnails rather than storing copies, tier old photos to cold storage, deduplicate by hash. Full marks need the arithmetic shown and units kept correct (bytes versus bits is the common slip).
- **J3:** A strong reply: the button is the visible tip; the work is the Google project and consent screen, a security review of how accounts get linked, what happens to existing email-and-password users, and testing the failure cases. It gives an honest estimate with its uncertainty, offers two options with trade-offs (for example a minimal version sooner with known limits, versus a complete version later), asks for a decision, and does not blame anyone or use jargon. Under 150 words.
- **J4:** A subject of about 50 characters in the imperative (for example 'Apply discount codes when quantity is above 1'). The body gives the cause (for instance, the discount was applied to the unit price rather than the line total), what changed, and what the tests cover. The PR description has problem, cause, fix, how to verify, risk, and a note that the rename is a separate refactor, ideally its own commit.
- **J5:** The decision is stated, not hedged. Do not ship silently: tell the product owner and your lead today, with numbers (which records, how badly, whether it is repairable). First, snapshot data and quantify the damage; write characterization tests around the core code before touching it; make the smallest possible fix; get a second reviewer; release behind a flag or as a canary with a rollback plan; plan repair for records already corrupted. Refuse: hiding the bug, a large rewrite two days out, pushing an untested change straight to production. Compare the risk of delaying against the risk of shipping, and let the stakeholders see both.

## Final scoring

| Score | What it means |
| --- | --- |
| 360 to 400 | Excellent fundamentals. You can hold your own in interviews at strong companies. Focus on depth and shipping real systems. |
| 300 to 359 | Strong. A few gaps. Study the parts where you lost the most points. |
| 240 to 299 | Solid foundation, clearly employable, with specific topics to close. |
| Below 240 | Real gaps in fundamentals. Fix the lowest-scoring part first, then retake in four weeks. |

Two honest cautions. First, scoring well on this exam shows strong fundamentals, not that you are one of the best in the world; that standard is built by shipping and maintaining real software, reading other people's code, and getting reviewed by people better than you. Second, your lowest-scoring part is your most valuable discovery. Spend your next two weeks on it, then retake only that part.
