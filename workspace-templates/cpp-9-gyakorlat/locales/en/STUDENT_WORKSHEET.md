# CPP_09 – Short worksheet

This is a reference, not another form to fill in. Inno maintains progress.

| Part | Main idea | Check |
|---|---|---|
| G09_01 | Three constructors | 0/0, 17/0, 23/12 |
| G09_02 | Conditional initial value and preserved state | -1 and 101 → 50; failed 120 keeps 70 |
| G09_03 | Separate data and pricing classes | 1100, 1100, 2000; another tariff gives 1800 |
| G09_04 | Objects in an object array | 20, inner sheet 5, outer sheet still 20 |
| P1–P3 | Ticket, box office, duplicate rejection | Four distinct seats; fifth rejected |
| P4–P5 | Cancellation, active prefix and total | Cancelling a middle entry gives 3/11000 |
| P6 | Returning text by value | Current and empty box-office summaries |

Exact interfaces and the checking sequence are in PROJECT.md. Rows 1–3, seats 1–4. Theatre: 12 seats; storage: 4 tickets. Both row and seat must match to identify one place. count is the number of active entries, not the last index. Rejected operations preserve state. Read only the active prefix after cancellation. Revenue and ticket prices are computed.

When reading a program, identify the type, object construction, selected constructor, initialized members and read-only queries. A constructor cannot have a return type. An initializer list is not an ordinary sequence of free-function calls. Member objects are constructed before the enclosing constructor body.

Save, then RUN. On compilation errors inspect the first relevant diagnostic; do not substitute an old binary for a successful new build. Check other objects and boundary values. The first substantive quiz answer counts. No new task sequence or homework follows completion.
