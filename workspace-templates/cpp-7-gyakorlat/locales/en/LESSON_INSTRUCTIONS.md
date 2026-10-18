# CPP_07 – Lesson instructions

## Schedule

| Block | Parts | Suggested time |
|---|---|---|
| 1 | G07_01: 12, G07_02: 12, G07_03: 10, G07_04: 11 minutes | 45 minutes |
| 2 | PROJECT steps P1–P6 | 45 minutes |
| 3 | T1: 15, T2: 25, feedback: 5 minutes | 45 minutes |

Times are planning guides, not automatic completion criteria. For every new part:
big picture → analogous example → explain key lines → one action → RUN → interpretation.

## G07_01 – A custom structure and an independent copy

**File:** G07_01_structure.cpp. **Example:** M1.

### A – One measurement

Big picture: combine three related pieces of data into one compound value.
Before main, the student defines `Measurement` with an integer `id`, a
`double value`, and a Boolean `valid` member. In main, create an object named
`original` from the starter values and print all three members.

Do not immediately supply the complete type definition using the task's own names.
Check: 101, 23.5, true; printing the Boolean as `1` is also correct.
Ask one short understanding question: which part defines the type, and which creates the object?

### B – Copying and assignment

Create a new object named `copy` from the original and change its value to 30.
Print the original and copy values. As a separate operation, assign the original
to the existing copy, then print both again.

Check: first `23.5 30`, then `23.5 23.5`.
Name the two operations: copy-initialization, then copy assignment.
Explain the difference between an uninitialized local object and this simple
structure initialized with empty braces. Do not read an uninitialized member.

## G07_02 – A structure passed by value and a pointer

**File:** G07_02_copying.cpp. **Examples:** M2, then M3.
The type and an original measurement are provided so the student can focus on the new operations.

### A – Returning a modified copy

After M2, implement `increasedCopy`. It takes a measurement by value and a
double increment, increases its own parameter's measured value, and returns the
whole modified structure. Other members stay unchanged. Call it with the original
and 2.0; store the result in a new variable.

Check: original 10.5, new object 12.5; both IDs are 201 and both flags are true.
Explain the return type, the independent parameter object and the role of return.

### B – Accessing the original through a pointer

After M3, create a pointer to the original and use it to increase the original's
value by 1.5. No additional function is required yet. Print the original and the copy from A.

Check: original 12, copy 12.5. The pointer stores an address and accesses the
original; it does not create another copy. Explain the equivalence of arrow access
and parenthesized dereferencing, without typing the student's assignment statement for them.

## G07_03 – A union and tracking its selected alternative

**File:** G07_03_union.cpp. **Example:** M4.
Big picture: a result is an integer count OR a real value. The alternatives are
not stored simultaneously, so we track which one can be read.

### A – Integer result

Define `NumberData` as a union with `integer` (int) and `real` (double).
Define `Result` as a structure containing a Boolean `isInteger` flag and a
`NumberData` member named `data`. Create an object, set the initial integer
and matching flag, then use if to print only the member selected by the flag.

Check: 7, integer active, flag true.

### B – Switching to a real value

Set the same object's real member to 2.5, update the flag, and print the real result
according to the flag. Factoring the output into a void function is allowed but optional.

Check: 2.5. Do not read the old integer member now.
Brief question: who keeps the flag and union consistent? The program, not automatically the compiler.
If sizeof is explored, do not require a specific size; alignment matters too.

## G07_04 – Blocks, shadowing and a loop variable

**File:** G07_04_scope.cpp. **Example:** M5.

### A – Three separate objects with the same name

A global `number` is provided with value 5. In main, create a local variable
with the same name and value 10, then another with value 20 in a separate inner
block. Print the inner value, the local main value after the block, then the
global value using a qualified name.

Check: 20, 10, 5. Two such local definitions in the same block are not allowed.
The outer object still exists inside the nested block, but its name is hidden.

### B – A function does not see its caller's local variable

Call the starter's `printGlobal()` from main.
Check: 5. The local value 10 in main remains unchanged. Interpret name lookup
from where the function's code is written, not the block from which it was called.

### C – A variable declared in a loop header

Use a for loop to sum 1, 2, 3 into a variable declared outside the loop.
Declare the index in the loop header. Print the sum after the loop.
Check: 6. Then try printing the loop index after the loop once: this use of the
name causes a compilation error. Remove the invalid output statement and
compile/run again. Never run an old executable after a failed compilation.

Conclude by distinguishing a name's scope from an object's lifetime. The inner
automatic variable in this example reaches the end of its lifetime when its block is exited.

## The next two blocks

Follow PROJECT steps P1–P6 with their specified analogous examples. Check values
are in TUTOR_KEY. Then ask the twenty questions from FINAL_TEST individually,
in their fixed order. Do not replace them with improvised questions.
