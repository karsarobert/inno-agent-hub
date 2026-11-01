# CPP_08 v2 – Introductory tasks

| Block | Content | Suggested time |
|---|---|---:|
| 1 | G08_01: 11, G08_02: 11, G08_03: 11, G08_04: 12 minutes | 45 min |
| 2 | Library project, P1–P6 | 45 min |
| 3 | T1: 15, T2: 25, feedback: 5 minutes | 45 min |

Breaks are additional. Times are guides, not evidence of completion.
Each part: big picture → complete analogy → key lines → explain the difference → one student action → save/RUN → checks.
Sources contain starting data only. Do not fill requested classes, function headers, conditions or loops for the student.

## G08_01 – Duration: stored state and computed queries

**File:** G08_01_duration.cpp. **Example:** M1.

### A – store total minutes

Define Duration with int minutes = 0;.
Implement void add(int amount), which increases this object’s minutes.
Inputs are small nonnegative integers; validation is not required here.
Add int hours() and int remainderMinutes().
Use integer division for complete hours and remainder modulo 60 for minutes left over. For integer operands, / gives the integer quotient and % gives the remainder.
In main, add the initial 90 minutes through the member function and print using both queries.
Check: 1 hour 30 minutes. Do not print precomputed constants as the result.

### B – another call on the same object

Add 45 minutes and let the queries calculate the new display.
Check: 2 hours 15 minutes.
Transfer check: another 45 minutes gives 3 hours 0 minutes.
Briefly discuss why subtracting 60 just once is insufficient.
The next task investigates trailing const in detail.

## G08_02 – Rectangle and const snapshot

**File:** G08_02_rectangle.cpp. **Example:** M2.

### A – two different formulas

Define Rectangle with double width = 1.0; and double height = 1.0;.
Implement void resize(double newWidth, double newHeight), double area() const, and double perimeter() const.
Supplied sides are positive finite numbers; validation is not required here.
Create a 3×2 rectangle and const Rectangle baseline = shape;.
Resize the modifiable shape to 4×3. Print both objects’ areas and perimeters.
Checks: baseline 6 and 10; modified 12 and 14; baseline still 6 and 10.

### B – intentional compile error

Try calling resize on baseline once. Explain the first relevant diagnostic.
Remove the invalid call, then build and run again; the final program must be correct.
Do not remove const to bypass the intended constraint.
Transfer check: queries on a new const 2×2 rectangle give 4 and 8.

## G08_03 – Lamps: private state and copying

**File:** G08_03_lamp.cpp. **Example:** M3.

### A – one query uses two members

Define Lamp with private bool on = false; and int brightness = 0;.
Public operations: void turnOn(), void turnOff(), void setBrightness(int newBrightness), bool isLit() const.
isLit is true only when the lamp is on AND brightness is positive.
Supplied brightness values are 0–100; no validating setter is required here.
Set both objects’ brightness to 50 but turn on only the first.
Checks: true/false; after turning the first off, false/false.
Try directly assigning first.brightness once; fix the compile error by using a public operation.

### B – an independent copy

Turn the first back on and copy-initialize copy from it.
Set the copy’s brightness to zero. The original remains lit; the copy does not.
Then assign first to the existing copy; it becomes lit again.
Transfer check: being on with brightness zero still gives false.
private does not prevent ordinary copying of the whole simple object.

## G08_04 – Fill and drain a tank

**File:** G08_04_tank.cpp. **Example:** M4.

### A – filling depends on free space

Define Tank with private int capacity = 10; and int contents = 0;.
The capacity constant in main is only source data; define the class’s own member separately.
bool fill(int amount) accepts a positive amount no greater than current free space.
Increase contents on success; return false and preserve state on failure.
int current() const returns stored contents; int freeSpace() const computes remaining capacity.
Filling 6 succeeds: contents 6, free 4. Another fill of 5 fails, retaining 6.

### B – draining needs a different condition

bool drain(int amount) accepts a positive amount no greater than contents.
main must use every Boolean result, for example printing it together with stored state.
Draining 2 leaves contents 4, free 6. Draining 5 fails, retaining 4.
Both operations reject zero.
Transfer checks: exactly 6 more units fit, making the tank full; all 10 can then be drained, making it empty.
Check after performing the operations, rather than routinely predicting output first.

## Continue

Guide the six PROJECT steps. The student must formulate the borrowing/return conditions; do not provide a renamed tank program as a completed library solution.
