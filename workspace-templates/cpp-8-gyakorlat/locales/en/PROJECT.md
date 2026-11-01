# CPP_08 v2 – Library borrowing project

**One working file:** P08_library.cpp. This is not a rewrite of the HTML measurement project.
A Book object represents multiple copies of one title. IDs are small positive integers and quantities are small integers.
Private members: int id = 0; int total = 0; int borrowed = 0;.
Always preserve 0 <= borrowed <= total.
Do not store available copies as a fourth member; calculate it from the two quantities.

Order: class → free-function prototypes → main → free-function definitions.
Define members inside the class. No custom constructors, reference parameters or dynamic allocation.
The tutor guides small steps; the student writes the code.

## P1 – Title identity and total stock

**Example:** M5; reuse M3’s access principle if needed. **Time:** 7 minutes.

Create Book with the members above.
Public operations:

- void identify(int newId): store the ID. The exercise supplies correct positive IDs.
- bool setTotal(int newTotal): reject negative totals and totals below already borrowed copies. Never reset borrowed to zero as a shortcut.
- int getId() const and int getTotal() const.

Initialize one new object as ID 501 with total 5; main checks setter success.
Try total -1: reject it and retain 5.
Print queried object state rather than source constants.

## P2 – Computed query and const snapshot

**Example:** M2’s copying/const principle. **Time:** 6 minutes.

Add int getBorrowed() const, int available() const and void print() const.
available computes total minus borrowed; it is not a separately stored value.
print displays ID, total, borrowed and available on one line.
Check: 501 5 0 5.
Create const Book snapshot = book; call print and available on it.
Try setTotal on the snapshot once; remove the invalid call and build again.

## P3 – Borrow: are enough copies available?

**Example:** M4’s check-before-change principle. **Time:** 7 minutes.

Implement bool borrow(int amount).
Only positive requests no greater than available copies may succeed.
Increase borrowed on success; never change total.
On rejection, leave every member unchanged. main uses the result and displays actual state.

Borrowing 3 from total 5 succeeds: 501 5 3 2.
Then borrowing 4 fails, retaining 501 5 3 2.
Requests 0 and -1 also fail. Continue with 3 borrowed and 2 available.

## P4 – Returns and relationships between members

**Example:** M5’s relationship constraint; explain only the difference. **Time:** 7 minutes.

Implement bool giveBack(int amount).
Accept only positive returns no greater than currently borrowed copies.
Decrease borrowed on success; keep total unchanged.
Returning 1 from the 3 borrowed copies leaves 501 5 2 3.
Another return of 3 fails because only 2 remain borrowed. Zero and -1 fail too.
Now try reducing total to 1: setTotal must reject it while 2 are borrowed.
Boundary check: returning both remaining copies succeeds, giving 0 borrowed and 5 available. Borrow 2 again for further single-object checks.

## P5 – Six titles and summaries

**Examples:** M6 traversal and M7 processing function. **Time:** 10 minutes.

Replace the P1–P4 single-object tests in main with an array loaded from the supplied source data, rather than maintaining a parallel project.

| ID | Total | Initial borrowing |
|---|---:|---:|
| 501 | 5 | 3 |
| 502 | 3 | 3 |
| 503 | 0 | 0 |
| 504 | 7 | 2 |
| 505 | 4 | 0 |
| 506 | 2 | 1 |

Create an array of 6 Book objects in main. Initialize its elements in a loop: identify, validate total, then perform positive initial borrowing.
Zero initial borrowing means no borrowing operation: do not call borrow(0), which expects positive requests.
If any source operation fails, report an error and do not treat that record as successfully initialized.
Implement free functions taking const Book* and a separate size:

- void printAll(...): call print for every record.
- int totalAvailable(...): sum computed available counts.
- int unavailableTitles(...): count titles with zero available copies.

Checks: 12 available copies and 2 unavailable titles. Zero-stock ID 503 counts as one of those two.
Free functions cannot directly access private state.
An additional check within this task: size zero returns zero sum/count without reading through the pointer.

## P6 – Trial borrowing on a copy and on the original

**Example:** M8. **Time:** 8 minutes.

### P6_A – independent parameter object

Implement Book borrowedCopy(Book book, int amount).
Try borrowing on the parameter object, display the Boolean result, then return the complete object.
Create a separate copy from the first array element, borrowing 2 copies.
Checks: original 501 5 3 2, copy 501 5 5 0; array summaries still 12 and 2.

### P6_B – change the original

Implement bool borrowOriginal(Book* book, int amount).
Call a public member through the pointer and return operation success.
Borrowing 1 on the first original element succeeds: 501 5 4 1.
Updated summaries: 11 available copies and still 2 unavailable titles.
Another request for 2 fails; retain the record and 11/2 summaries.

Finish with a brief explanation: why are borrowing and returning different operations, and why is available stock computed instead of stored separately?
