# C++ basics – internal lesson guide

This file is for the assistant and the instructor. Give students their tasks in
the conversation; do not refer to this file or internal step identifiers.
Read the entire current lesson and its actual source before starting.

## Using the steps

**Demonstration:** explanation and observation; you may show the expected result
in advance. **Check question:** present the code, input and one question, then
wait for the answer. Do not quote the “After the answer” section beforehand,
even as a comment or hint. These explanations are available to the instructor in
advance, but should reach the student only at the appropriate moment.

After a check question, assess the answer, clarify the expected behavior, then
assign the experiment. Mark execution as complete only after observing it or
receiving student confirmation. Every edit should be followed by saving and
recompilation, except the explicit no-recompilation experiment in A2. After a
failed compilation, do not run an old binary as a test of the new code.
After demonstrating the initial behavior, do not ask the student to “predict”
the result you just showed. Use the next change or ask for reasoning.

Output blocks show standard output. Answers typed by the student and separately
labelled standard error are not part of those blocks. Excerpts are identified
separately. The sources follow the classroom examples in CPP_01.html, adapted to
English names and text. That classroom HTML is a separate resource, not included
in this package. Teach new concepts before requesting independent application,
as described in the tutor guide; the first run may be a shared demonstration.

## 1. Core exercise – The first program

**Source:** `L01_first_program.cpp`. Related classroom chapters: 1–2 and 9.

### A1 – Check question: the first output

Show the body of main without comments explaining the result.
Question: “What text do you expect when the program runs?” Wait for the answer.

**After the answer:** cout is the standard output stream; we write to it with
`<<`. `'\n'` is a newline character. `return 0;` indicates successful completion;
it does not print zero. The `std::` prefix refers to the std namespace.
`#include` belongs to preprocessing; main is the entry point. Briefly explain
these roles as needed.

Guide the experiment in two steps: first compilation, then execution after
checking the compilation result.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01 L01_first_program.cpp
```

```bash
./L01
```

Expected output:

```text
Hello, world!
```

Silent compilation is normal, but success depends on the command completing
successfully. `-o L01` names the executable being created. Do not ask about this
again if the student has already explained it accurately.

### A2 – Check question: saving and recompiling

Original line:

```cpp
std::cout << "Hello, world!" << '\n';
```

New line:

```cpp
std::cout << "Hi, world!" << '\n';
```

Question: “Which text appears if you save the change but run the previous L01
program without recompiling?” Wait for the answer.

**After the answer:** The previous program prints Hello, world! Saving changes
the source file; a new compilation creates the updated executable.

**Experiment:** Ask the student to replace the line, save and run the previous
`./L01` program. After discussing the observation, recompile with the A1 command
and run again: now Hi, world! appears. Obtain feedback about both runs.
Explaining the step alone does not mean it has been performed.

### A3 – Check question: a missing semicolon

Remove the semicolon from the end of the working output statement:

```cpp
std::cout << "Hi, world!" << '\n'
```

Question: “Does the problem appear during compilation or while the program is
running?” Wait for the answer.

**After the answer:** We expect a compilation error because the statement's
terminator is missing. Ask the student to remove only the indicated semicolon,
not one elsewhere.

**Experiment:** Save and compile. Request the first error message. It may point
to the following return statement; the exact wording depends on the environment.
No new successfully compiled program was produced, although the previous
executable may still exist.

**Restore:** Put the semicolon back, restore Hello, world!, save, compile and run.
A1–A3 can be closed when both changes and the restoration have been confirmed,
or the student has explicitly skipped a step. Record any skipped step as skipped.

## 2. Core exercise – Variables and values

**Source:** `L01b_variables_and_values.cpp`. Related chapters: 3–4.

### B1 – Demonstration: initialization and assignment

Explain using the source: initialization gives a variable its initial value;
assignment changes the value of an existing variable. Here constexpr declares
a typed constant whose value can be evaluated at compile time.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01b L01b_variables_and_values.cpp
./L01b
```

Complete initial output:

```text
Quantity: 4
Previously calculated total: 750
Recalculated total: 1000
Integer division result: 2
Floating-point division result: 2.5
The quantity is at least 4.
```

Initially, total stores `3 * 250`. `quantity = 4;` does not change total; only
the later `total = quantity * unit_price;` gives it a new value.
The if statement selects a branch based on the bool variable's truth value.
Leave the division explanation until B3 unless the student asks about it now.
Do not overload the demonstration with several simultaneous questions.

### B2 – Check question: changing the quantity

Original line: `quantity = 4;`. New line: `quantity = 2;`.
Question: “What will the recalculated total be?” Wait for the answer.

**After the answer:** The recalculated total is 500. If needed, then ask a separate
question about the previously calculated total: that stays at 750. Do not mark
500 as wrong when you asked about the recalculated total.

**Experiment:** Replace the line, save, compile and run as in B1. Quantity: 2;
previous total: 750; new total: 500; the division lines are unchanged; the final
line is: The quantity is less than 4. After the experiment, restore
`quantity = 4;`. Confirm restoration before the next change.

### B3 – Demonstration, then check question: the type of division

First explain the initial example: in `5 / 2`, both operands are int, so the
result is the int value 2. This becomes the value 2.0 in the double variable.
By default, std::cout prints 2 here, not necessarily 2.0. `5.0 / 2` performs
floating-point division and gives 2.5.

Next, ask for reasoning instead of asking for numbers you have already shown:
“Why doesn't storing the result of 5 / 2 in a double variable make it 2.5?”
Wait for the answer.

**After the answer:** Division follows the operand types; the result is converted
to double afterwards. If the student explains this independently, another long
explanation is unnecessary.

**Guided experiment:** Replace the original line

```cpp
double integer_division = 5 / 2;
```

with:

```cpp
double integer_division = 5.0 / 2;
```

After saving, compiling and running, this output line also shows 2.5. Its label
refers to the initial example, so restore the original line after the experiment,
then compile and run. The B2 and B3 changes are part of the lesson; do not finish
after B1 alone.

## 3. Core exercise – Input and strings

**Source:** `L04_input_strings_validation.cpp`. Related chapters: 4–9.

### C1 – Demonstration: initial behavior

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L04 L04_input_strings_validation.cpp
./L04
```

Enter Anna at the name prompt and 19 at the age prompt; press Enter after each.
Complete standard output:

```text
Enter your full name:
Enter your age as an integer:
Hi, Anna!
Number of char elements stored in the name: 4
Next year you will be 20 years old.
Value of the age variable: 19
Age as text: 19
Previously read character: o
Modified text: boakcase
Length of the modified text: 8
```

Each prompt appears before its corresponding input. `age + 1` does not change
age. `to_string` converts a number to text. For a particular question, show only
the relevant lines, labelled as an excerpt, rather than the full output.
The deliberately modified text need not be a real word; trace the code to find it.

### C2 – Check question: a full name

Code unchanged; name: Anna Hill; age: 19.
Question: “How many char elements does this name store?” Wait for the answer.

**After the answer:** Nine; the space counts too. getline reads the whole line;
it consumes the newline but does not store it in name.

**Experiment:** Run again without changing the code. Greeting: Hi, Anna Hill!;
number of stored char elements: 9. Confirmation of these two lines is enough.

### C3 – Check question: replacing the input operation

Original line:

```cpp
std::getline(std::cin, name);
```

New line:

```cpp
std::cin >> name;
```

Question: “What happens when the program reads the age if we enter Anna Hill as
the name?” Wait for the answer; do not first reveal what remains in the input.

**After the answer:** Compilation succeeds. name contains only Anna; Hill remains
in the input. The age prompt still appears, but the next input operation tries to
interpret Hill as an integer; it does not wait for a newly typed age.

**Experiment:** Replace the line, save, compile and run. Type only Anna Hill.
After the age prompt, the expected standard error is:

```text
Error: could not read the age as an integer.
```

By default, `>>` skips leading whitespace and, when reading a string, stops at
the next whitespace character. Whitespace includes spaces, tabs and newlines.

**Restore:** Restore the getline line, save, compile and try Anna Hill and 19.
With the current input order, std::ws is not needed.

**Extend only on request:** If getline followed numeric input, it could read an
empty line because of a remaining newline. `std::getline(std::cin >> std::ws, name)`
skips leading whitespace, so it is unsuitable if empty lines or leading spaces
must be preserved as data. The current program uses a different order.

### C4 – Check questions: input failure and range errors

Start a new run for each experiment, using Anna as the name. Keep the code unchanged.
First ask only: “Which check rejects an age of -1?” After the answer and experiment,
ask separately about the input apple. Do not show the following assessment table
in advance.

**After the answer, instructor reference data:**

| Input | Expected behavior | Reason |
|---|---|---|
| -1 or 200 | Range error; no greeting. | The number can be read, but is outside 0–120. |
| apple | Input failure; no greeting. | It cannot be read as an integer. |
| 0 | Runs to completion; next year's age is 1. | The lower boundary is accepted. |
| 120 | Runs to completion; next year's age is 121. | The upper boundary is accepted; validation concerns the age entered. |
| 19abc or 19.5 | Runs to completion with the value 19. | `>>` reads the initial integer; the rest is not processed. |

Work through -1 and apple; choose one or more other boundary cases according to
progress. Do not record skipped inputs as tested. `!` is logical negation;
`||` is logical OR. Of the two age-related if statements, the first checks input
success and the second checks the permitted range. cerr is the standard error
stream; `return 1;` indicates unsuccessful completion here. if is a general
branching statement with many uses.

An empty name line causes an error. A name consisting only of spaces is not an
empty string, so this example accepts it. The program does not fully validate
names or require the whole age-input line to contain only an integer. Explain
this if needed; do not start a new task while addressing the previous question.

### C5 – Demonstration, then check question: copying and modifying

In the initial example, the indices of book are: 0: b, 1: o, 2: o, 3: k.
letter receives a copy of the value of `s[2]`; changing s does not change letter.
Next, consider replacing the original `s[2] = 'a';` with `s[2] = 'o';`.

Question: “What text will s contain after the change and after appending case?”
Wait for the answer.

**After the answer:** bookcase, with length 8. The previously read letter stays o.
If the student answers only book, acknowledge that this is the state after the
character assignment; ask only about the result of appending the suffix.

**Experiment:** Replace the line, save, compile and run with Anna and 19.
**Restore:** Restore the original 'a', save and recompile.
Do not request an invalid `[]` index. For bounds checking that throws an exception,
use the ready-made at() example in the classroom material. Introduce references
only when explicitly requested.

### C6 – Check question: length in UTF-8

Prerequisite: size() returns the number of stored char elements, not a general
letter count. Question: “Will size() definitely return three for the text Éva?”
Wait for the answer; if the student is unsure, continue as an observation exercise.

**After the answer:** In UTF-8, É uses two bytes, while v and a use one each, so
the result is 4. There are three visible letters. The actual input encoding
depends on the terminal.

**Experiment:** Keep the code unchanged; enter Éva and 19. Observing the length
is enough. The terminating null character is not included in size(). When
indexing these ASCII word examples, one char element corresponds to one visible
character.

### C7 – Interpretation question: conversion and concatenation

This is a reasoning task, not a request to write a new program. Show without comments:

```cpp
std::string("19") + "1"
```

Question: “What text does this expression produce?” Wait for the answer.

**After the answer:** The text "191". Here, + concatenates strings. Then briefly
compare: `std::stoi("19") + 1` gives the integer 20; `std::to_string(19)` gives
the text "19". On request, discuss stoi failures: "19abc" gives 19; "apple"
throws invalid_argument. The ready-made classroom example explains checking the
whole string and handling exceptions.

After C1–C7, the core exercises can be closed. Briefly name the parts actually
completed; ask once whether to continue with the optional exercises.

## 4. Optional exercise – Preprocessing and macros

**Source:** `L02_preprocessor_macros.cpp`. Related chapter: 10.

### D1 – Demonstration: macros and preprocessing

`#define FAVORITE_NUMBER 42` specifies a replacement rule. The preprocessor replaces
appropriate occurrences of the macro name with the token 42. A token is an element
of source code, such as a name, numeric literal or operator. A macro is not a
variable: it has no variable-like type or runtime storage of its own. However,
42 is an integer literal of type int when used in a C++ expression.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L02 L02_preprocessor_macros.cpp
./L02
```

Expected output:

```text
My name is Anna Hill.
My favorite number: 42
```

### D2 – Guided observation: inspecting a relevant part of a large file

Before giving the commands, say: “The headers make the resulting file long.
In this example, our own program is at the end; we will look at the last twenty
lines.” Do not first ask the student to open the whole file in the editor.
Give the creation and viewing commands together; the student should use the
second after the first succeeds.

```bash
g++ -std=c++20 -E L02_preprocessor_macros.cpp -o L02_preprocessed.ii
tail -n 20 L02_preprocessed.ii
```

`-E` stops after preprocessing; it does not create an executable program. tail
only reads the end of the file; it does not change its contents. Ask the student
for only the line containing My favorite number, not the whole file.
If the relevant line is missing from the excerpt, search specifically for it:

```bash
rg -n -F 'My favorite number' L02_preprocessed.ii
```

If rg is unavailable:

```bash
grep -n -F 'My favorite number' L02_preprocessed.ii
```

**After the observation:** 42 appears in place of the macro name. The processed
header contents account for the file's length. Later stages produce assembly
code, object code and, through linking, an executable. Do not say that a macro
simply replaces every textual occurrence: substitution works on tokens.

### D3 – Check question: a new replacement token

Original line: `#define FAVORITE_NUMBER 42`. New line: `#define FAVORITE_NUMBER 7`.
Question: “What will the program display as the favorite number after recompilation?”
Wait for the answer.

**After the answer:** 7. The macro name is now replaced by the token 7; this is
not a general replacement of every number 42 in the program.

**Experiment:** Replace the line, save, compile and run with the D1 commands.
The second line is: My favorite number: 7. Regenerating the .ii file is optional;
if you do so, provide the complete D2 command pair, including tail.

**Restore:** Restore 42, save, compile and run. If you regenerated the .ii file
for the version with 7, regenerate it from the restored source too, so that it
does not show a misleading intermediate state. For a fixed numerical value,
we generally use a constexpr constant; the macro here illustrates preprocessing.

## 5. Optional exercise – Conditional compilation and assert

**Source:** `L03_conditional_macros.cpp`. Related chapters: 9–10.

### E1 – Demonstration: two compilation variants

First variant:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L03 L03_conditional_macros.cpp
./L03
```

Expected output:

```text
The diagnostic message is disabled.
SQUARE(3) = 9
SQUARE(1 + 2) = 9
```

Second variant:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -DDEBUG -o L03_debug L03_conditional_macros.cpp
./L03_debug
```

The first line is now: The diagnostic message is enabled. The other lines are
unchanged. `-DDEBUG` defines the macro; `#ifdef` checks whether it is defined.
`#else` introduces the other branch, and `#endif` closes the conditional section.
Selection takes place during preprocessing; by contrast, a C++ if statement is
part of the program's behavior.

The filenames help distinguish the variants in these command pairs. If the
student's output differs, request their actual last compile and run commands;
do not infer the history from the filename. An earlier DEBUG-enabled binary does
not update automatically when only L03 is rebuilt later.

### E2 – Check question: parentheses

The correct macro is `#define SQUARE(x) ((x) * (x))`.
Show the version to be examined without its solution:

```cpp
#define SQUARE(x) x * x
```

Question: “What would SQUARE(1 + 2) evaluate to with this definition?” Wait for the
answer. If help is needed, first show only the expanded expression; allow another
attempt before providing the numerical result.

**After the answer:** `1 + 2 * 1 + 2`, which evaluates to 5. Multiplication has
higher precedence. SQUARE(3) still evaluates to 9. Missing parentheses cause a
logic error.

**Preparing the experiment:** Two related lines must be changed for this observation.
First explain assert: when its check is active, a false condition produces a
diagnostic message and abnormal termination. To observe the numbers without
interruption, temporarily disable this one call.

1. Replace the macro definition with the version above that has no parentheses.
2. Comment out `assert(SQUARE(1 + 2) == 9);`:

```cpp
// assert(SQUARE(1 + 2) == 9);
```

Save, then compile and run with this exact command pair:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L03 L03_conditional_macros.cpp
./L03
```

Complete output:

```text
The diagnostic message is disabled.
SQUARE(3) = 9
SQUARE(1 + 2) = 5
```

After the experiment, restore both original lines: the parenthesized macro
and the active assert call. Compile and run with the same command pair; the
output matches the first E1 variant. Close the experiment only after confirmation.
Do not request SQUARE(i++): substituting the argument twice can cause problems.
We generally implement calculations like this with a function.

### E3 – Demonstration and concept check: DEBUG and NDEBUG

First explain the separate roles of the two macros:

| Setting | Message in this example | assert check |
|---|---|---|
| Neither -DDEBUG nor -DNDEBUG | Disabled. | Active. |
| Only -DDEBUG | Enabled. | Active. |
| Only -DNDEBUG | Disabled. | Omitted. |
| Both -DDEBUG and -DNDEBUG | Enabled. | Omitted. |

The table applies to the supplied source when no other settings override these
macros. NDEBUG must be defined before cassert is included. The terms debug/release
do not replace knowing the actual settings.

Then ask for reasoning: “Why shouldn't we rely only on assert to validate the age?”
Wait for the answer. “assert does not run without DEBUG” is partly incorrect:
acknowledge the recognition that checks can be disabled, but correct the macro
name and condition.

**After the answer:** With NDEBUG, the check is omitted. The if statements in L04
validate input. Do not put a side effect required for the program to work inside
an assert condition. Omitting a check does not itself guarantee a crash; the
consequence depends on the program.

Execution of output statements before assert and actual appearance of the text
are different: buffered output may be incomplete after abnormal termination.
Do not promise that particular lines will appear, and do not request a separate
termination experiment.

### E4 – Optional demonstration: include guards

An include guard prevents repeated processing of a header in the same translation
unit. In the classroom favorites-header example, `#ifndef` checks that the guard
macro is absent, the header defines the macro, and `#endif` closes the section.
On a second inclusion, the contents are skipped. An empty guard block in a single
.cpp file would not demonstrate this; do not ask the student to create one.
The header example belongs to the separate classroom material, not this ZIP.

## Closing and review

First check the actual status of the steps internally. Do not mark a skipped
experiment as completed. Briefly summarize the topics covered. If the student
asks for revision, give one question at a time, targeted at an earlier uncertainty.
Do not automatically repeat every question when understanding is already clear.

Possible questions, without revealing solutions in advance:

- What changes when you save, and what changes when you compile?
- Why doesn't total update automatically when quantity changes?
- Why do 5 / 2 and 5.0 / 2 give different results?
- Why does Anna Hill cause a problem for numeric input when the name was read with `>>`?
- Why can the number of visible letters differ from the number of stored char elements?
- Why does letter stay unchanged after s is modified?
- How does an input failure differ from a value outside the permitted range?
- What controls whether assert is disabled in the macro example?

Assess answers accurately. After an assisted solution, “we discussed this” is
accurate; “you solved it perfectly on your own” is not. Promise continuation in
a later session only when the necessary state is actually available.
