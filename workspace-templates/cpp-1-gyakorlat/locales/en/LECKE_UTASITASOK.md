# C++ Basics – internal session script

This file is for the assistant and the teacher. The student receives the tasks
in conversation; do not refer to this file or to the internal step
identifiers. Read the whole current lesson and the actual source before you
start.

## Using the steps

**Demonstration:** explanation and observation; the expected result may be
shown in advance. **Checking question:** after giving the code, the input and a
question, wait for the answer. Do not quote the "After the answer" part
before that, not even as a comment or a hint. These explanations are available
to the teacher in advance; they should reach the student only at the right
moment.

After a checking question, evaluate the answer, clarify the expected
behaviour, then give the trial. Mark an execution done only after observation
or student confirmation. Every modification is followed by a save and a
recompilation; after a failed compilation do not run an old binary to check
the new code. After demonstrating the initial behaviour, do not ask the just-
shown result back as a prediction. Use the next change or the reasoning
instead.

The output blocks show the standard output; the answers typed by the student
and the separately marked error output are not part of them. The details are
marked separately. The sources follow the classroom examples of CPP_01.html.

## 1. Core exercise – The first program

**Source:** `L01_elso_program.cpp`. Related classroom chapters: 1–2 and 9.

### A1 – Checking question: the first output

Show the body of the main function without a comment that explains the result.
Question: "What text do you expect the program to print when it runs?" Wait
for the answer.

**After the answer:** cout is the standard output stream; we write into it
with the << operator. The '\n' is a newline character. The return 0; signals
successful termination; it does not print zero. The std:: prefix denotes the
std namespace. The #include belongs to preprocessing, and main is the entry
point; explain their roles briefly if needed.

Lead the trial in two steps: first compilation, and only after its result,
running.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01 L01_elso_program.cpp
```

```bash
./L01
```

Expected output:

```text
Hello, world!
```

A silent compilation is usual, but the basis of success is a successful
command execution. The -o L01 gives the name of the resulting executable. Do
not ask this again if the student has already stated it precisely.

### A2 – Checking question: saving and recompiling

Original line:

```cpp
std::cout << "Hello, world!" << '\n';
```

New line:

```cpp
std::cout << "Hi, world!" << '\n';
```

Question: "Which text appears if you save the modification but start the
earlier L01 program without recompiling?" Wait for the answer.

**After the answer:** The earlier program prints the Hello, world! text.
Saving modifies the source file; a new compilation produces the executable.

**Trial:** perform the line change, save, and run the earlier ./L01 program.
After the experience, recompile with the A1 command, then run: now the Hi,
world! text appears. There should be feedback about both runs. This step is
not done just because it was explained.

### A3 – Checking question: a missing semicolon

Remove the semicolon from the end of the working output line:

```cpp
std::cout << "Hi, world!" << '\n'
```

Question: "Does the problem show up at compilation or while the program is
running?" Wait for the answer.

**After the answer:** We expect a compilation error, because the closing of
the statement is missing. The student should remove only the semicolon marked
here; they should not choose another place.

**Trial:** save and compile. Ask for the first error message. The message may
also point at the following return line; the exact text depends on the
context. No new, successfully compiled program was produced; the old
executable may remain all the same.

**Restoration:** semicolon back, text back to Hello, world!, save, compile and
run. A1–A3 are done when both changes and the restoration are confirmed, or
the student explicitly skipped one of the steps.

## 2. Core exercise – Variables and values

**Source:** `L01b_valtozok_es_ertekek.cpp`. Related chapters: 3–4.

### B1 – Demonstration: initialization and assignment

Based on the source, explain: at initialization the variable receives an
initial value; at assignment we modify the value of an existing variable. The
constexpr here denotes a constant that has a type and can be evaluated at
compile time.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01b L01b_valtozok_es_ertekek.cpp
./L01b
```

The complete initial output:

```text
Count: 4
Previously computed total: 750
Recomputed total: 1000
Integer division result: 2
Floating-point division result: 2.5
The count is at least 4.
```

The total first stores the value of 3 * 250. The count = 4; does not modify
it; only the later total = count * unit_price; gives it a new value.
The if chooses a branch based on the truth value of the bool variable. Leave
the explanation of division to step B3 if there is no question about it now.
Do not overload the demonstration with many parallel questions.

### B2 – Checking question: changing the count

Original line: `count = 4;`. New line: `count = 2;`.
Question: "What will the recomputed total be?" Wait for the answer.

**After the answer:** The recomputed total is 500. If needed, examine the
previously computed total afterwards as a separate question: it stays 750.
Do not mark the answer "500" as wrong when you asked about the recomputed
total.

**Trial:** line change, save, compile and run as in B1. Count: 2; previous
total: 750; new total: 500; the division lines are unchanged; the last line:
The count is less than 4. After the trial, restore the count = 4; line.
Confirm the restoration before the next change.

### B3 – Demonstration, then checking question: the type of division

First explain the initial example: with 5 / 2 both operands are int, so the
result is the int 2. From this comes the double variable's value 2.0.
The std::cout prints 2 here by default, not necessarily 2.0.
The 5.0 / 2 is a floating-point division; its result is 2.5.

Then ask for reasoning, not for the already-shown numbers:
"Why is the result of 5 / 2 not 2.5 just because we put it into a double
variable?" Wait for the answer.

**After the answer:** The division happens according to the operands' types;
the result is converted to double only afterwards. If the student stated this
independently, no further long explanation is needed.

**Guided trial:** replace the original line

```cpp
double int_division = 5 / 2;
```

with this:

```cpp
double int_division = 5.0 / 2;
```

After saving, compiling and running, this output shows 2.5 as well. The label
of the output refers to the initial example, so after the trial restore the
original line, then compile and run the program. The B2 and B3 changes are
both parts of the lesson; do not close the lesson after B1.

## 3. Core exercise – Reading input and strings

**Source:** `L04_io_string_hibakes.cpp`. Related chapters: 4–9.

### C1 – Demonstration: initial behaviour

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L04 L04_io_string_hibakes.cpp
./L04
```

For the name question the input is Anna, for the age question 19; press Enter
after both. The complete standard output:

```text
Enter your full name:
Enter your age as a whole number:
Hi, Anna!
Number of char elements stored in the name: 4
Next year you will be 20.
Value of the age variable: 19
Age as text: 19
Character read earlier: m
Modified text: aleafa
Length of the modified text: 6
```

The questions appear before the input belonging to them. The age + 1 does not
modify the value of age. The to_string makes a text from a number. Instead of
the whole output, show only the lines needed for a given question, marked as
an excerpt.

### C2 – Checking question: the full name

Unchanged code, name: Kiss Anna, age: 19.
Question: "How many char elements does this name store?" Wait for the answer.

**After the answer:** Nine; the space counts too. The getline reads the whole
line; it reads the newline character but does not store it in the name.

**Trial:** a new run, without a code modification. Greeting: Hi, Kiss Anna!;
the number of stored char elements is 9. Confirming these two lines is enough.

### C3 – Checking question: changing the way of reading

Original line:

```cpp
std::getline(std::cin, name);
```

New line:

```cpp
std::cin >> name;
```

Question: "What happens when reading the age if we enter the line Kiss Anna
as the name?" Wait for the answer; do not say beforehand what stays in the
input.

**After the answer:** The compilation succeeds. The name becomes only Kiss;
Anna remains in the input. The message asking for the age still appears, but
the next read tries to interpret the text Anna as a whole number; it does not
wait for a newly typed age.

**Trial:** line change, save, compile, run. Only the name Kiss Anna has to be
typed. After the age question this error output is expected:

```text
Error: could not read the age as a whole number.
```

The >> skips leading whitespace characters by default, and when reading text
it stops at the next whitespace character. Whitespace is for example the
space, the tabulator and the newline character.

**Restoration:** getline line back, save, compile, trial with the Kiss Anna
and 19 input. In the current order there is no need to use std::ws.

**Extend only on request:** if a getline came after reading a number, the
leftover newline character could make it read an empty line. The
std::getline(std::cin >> std::ws, name) skips the leading whitespace
characters, so it is not appropriate when the empty line or the leading space
is data to be preserved. The current program's order is different.

### C4 – Checking questions: read and range errors

Each trial is a new run, with Anna as the name. The code is unchanged.
First ask only this: "Which check rejects the age -1?"
After the answer and the trial, a separate question follows for the apple
input. Do not show the evaluation table below in advance.

**After the answer, reference data for the teacher:**

| Input | Expected behaviour | Reason |
|---|---|---|
| -1 or 200 | Range error; no greeting. | The number can be read, but it is outside the 0–120 range. |
| apple | Read error; no greeting. | Cannot be read as a whole number. |
| 0 | Runs to the end; next year 1. | The lower bound is accepted too. |
| 120 | Runs to the end; next year 121. | The upper bound is accepted too; the check applies to the read age. |
| 19abc or 19.5 | Runs to the end with the value 19. | The >> reads the leading whole number; it does not process the rest. |

Work through the -1 and apple trials; from the remaining edge cases choose one
or more according to progress. Do not treat the skipped inputs as tried.
The ! is logical negation; the || is logical "or". The first if checks the
read, the second the allowed range. The cerr is the standard error stream; the
return 1; here signals erroneous termination. The if is a general branch; it
can be used for several purposes.

An empty name line gives an error; a name containing only spaces is not an
empty string, so the sample accepts it. The program does not perform full
name or whole-line numeric validation. Explain this if needed; do not open a
new task while the previous question is being answered.

### C5 – Demonstration, then checking question: copying and modifying

In the initial sample, the indices of alma are: 0: a, 1: l, 2: m, 3: a. The
letter receives a copy of the value of s[2]; modifying s does not modify the
value of letter. Then we would replace the original `s[2] = 'e';` line with
the `s[2] = 'o';` line.

Question: "What text will the value of s be after the modification and the
appending of fa?" Wait for the answer.

**After the answer:** aloafa, and its length is 6. The value of the letter
read earlier stays m. If you get only the answer aloa, acknowledge that this
is the state right after the character swap; ask specifically for the result
of the appending.

**Trial:** line change, save, compile, run with the Anna and 19 input.
**Restoration:** the original 'e' back, save and recompile.
Do not ask for the use of an invalid [] index; for an index check that throws
an exception, the ready-made classroom at() example can be used. Introduce
references only on explicit request.

### C6 – Checking question: the length with UTF-8

Prior knowledge: the size() gives the number of stored char elements, not a
general letter counter. Question: "Will the size() result for the text Ági
certainly be three?" Wait for the answer; in case of uncertainty it can also
be continued as an observation.

**After the answer:** With UTF-8, Á is two bytes, g and i are one byte each,
so the result is 4. The number of visible letters is three. The actual input
encoding depends on the terminal.

**Trial:** unchanged code, name Ági, age 19. Observing the length is enough.
The terminating null character does not count into the size() result. When
indexing ASCII texts, one char element corresponds to one visible character.

### C7 – Interpretation question: conversion and concatenation

This is a thinking task, not writing a new program. Show it without a comment:

```cpp
std::string("19") + "1"
```

Question: "What text does this expression give?" Wait for the answer.

**After the answer:** The text "191". The + concatenates here. Then briefly
put next to it: the result of std::stoi("19") + 1 is the whole number 20; the
result of std::to_string(19) is the text "19". On request, cover the errors of
stoi: with "19abc" it gives 19, with "apple" it throws an invalid_argument
exception. Full-text validation and exception handling are explained by the
ready-made classroom example.

After C1–C7 the core exercises can be closed. Briefly name the parts actually
done; ask once about the supplementary exercises.

## 4. Supplementary exercise – Preprocessing and macros

**Source:** `L02_preprocesszor_makro.cpp`. Related chapter: 10.

### D1 – Demonstration: macro and preprocessing

The #define FAVOURITE_NUMBER 42 gives a substitution rule. The preprocessor
substitutes the appropriate occurrences of the macro name with the 42 token.
A token is an element of the source code, for example a name, a numeric
literal or an operator. The macro is not a variable; it has no type of its own
like a variable and no runtime storage. The 42 is nevertheless an int integer
literal in the C++ expression.

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L02 L02_preprocesszor_makro.cpp
./L02
```

Expected output:

```text
My name is Kiss Anna.
My favourite number: 42
```

### D2 – Guided observation: viewing the large file in a targeted way

Even before the commands, say: "Because of the headers a long file is
produced. In this example our own program is at the end; we look at the last
twenty lines." Do not first ask for the whole file to be opened in the editor.
Give the creation and viewing commands together; the student uses the second
after the first has executed successfully.

```bash
g++ -std=c++20 -E L02_preprocesszor_makro.cpp -o L02_preprocessed.ii
tail -n 20 L02_preprocessed.ii
```

The -E stops after preprocessing; it does not make an executable. The tail
only reads the end of the file; it does not modify its content. Ask the
student only for the line containing the Favourite number text, not for the
whole file. If the searched line is not in the excerpt, search in a targeted
way:

```bash
rg -n -F 'Favourite number' L02_preprocessed.ii
```

If rg is not available:

```bash
grep -n -F 'Favourite number' L02_preprocessed.ii
```

**After the observation:** in the place of the macro name, 42 is visible. The
length of the file comes from the processed content of the headers. Later
assembly code, object code and, with linking, an executable program are
produced. Do not say that the macro simply replaces every textual occurrence:
the substitution happens on tokens.

### D3 – Checking question: a new replacement text

Original line: `#define FAVOURITE_NUMBER 42`. New line:
`#define FAVOURITE_NUMBER 7`.
Question: "What does the program print in the place of the favourite number
after recompiling?" Wait for the answer.

**After the answer:** 7. Now the 7 token goes into the place of the macro
name; we are not generally replacing every 42 in the program.

**Trial:** line change, save, compile and run with the D1 commands.
The second line: My favourite number: 7. Regenerating the .ii file is
optional; if you repeat it, give the complete D2 command pair, together with
the tail.

**Restoration:** 42 back, save, compile and run. If you also regenerated the
.ii file for the 7 version, refresh it from the original source as well, so
that no misleading intermediate state remains. For a fixed numeric value we
usually use a constexpr constant; here the macro serves to demonstrate
preprocessing.

## 5. Supplementary exercise – Conditional compilation and assert

**Source:** `L03_felteteles_makro.cpp`. Related chapters: 9–10.

### E1 – Demonstration: two compilation variants

First variant:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L03 L03_felteteles_makro.cpp
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
g++ -std=c++20 -Wall -Wextra -pedantic -DDEBUG -o L03_debug L03_felteteles_makro.cpp
./L03_debug
```

Here the first line is: The diagnostic message is enabled. The other lines are
identical. The -DDEBUG defines the macro; the #ifdef checks whether it is
defined. The #else marks the other branch, the #endif closes it. The selection
happens at preprocessing; the C++ if, in contrast, is part of the program's
operation.

The file names help distinguish the given command pairs. If the student's
output differs, ask for the actual last compilation and run commands; do not
infer the history from the file name. An earlier DEBUG binary does not update
automatically just because later only the L03 file is compiled again.

### E2 – Checking question: parenthesization

The correct macro: `#define SQUARE(x) ((x) * (x))`.
Show the variant to be examined, without the solution:

```cpp
#define SQUARE(x) x * x
```

Question: "What would SQUARE(1 + 2) be with this?" Wait for the answer.
If help is needed, first show only the substituted expression; do not give
the numeric result before another attempt.

**After the answer:** 1 + 2 * 1 + 2, the result is 5. The multiplication binds
more strongly. The value of SQUARE(3) is still 9. The missing
parenthesization causes a logic error.

**Preparing the trial:** here two related lines must be modified for the same
observation. First explain the role of assert: with the check active, a false
condition causes a diagnostic message and an abnormal termination. To observe
the numbers undisturbed, we temporarily switch off this one call.

1. Replace the macro definition with the unparenthesized variant above.
2. Comment out the `assert(SQUARE(1 + 2) == 9);` line:

```cpp
// assert(SQUARE(1 + 2) == 9);
```

Save, then compile and run with this concrete command pair:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L03 L03_felteteles_makro.cpp
./L03
```

The complete output:

```text
The diagnostic message is disabled.
SQUARE(3) = 9
SQUARE(1 + 2) = 5
```

After the trial, restore both original lines: the parenthesized macro
definition and the active assert call. Compile and run with the same command
pair; the result is the output of the first variant of E1. Close the trial
only after confirmation. Do not ask for the use of SQUARE(i++): substituting
the parameter twice can cause a problem. Such calculations are generally
implemented with a function.

### E3 – Demonstration and conceptual check: DEBUG and NDEBUG

First explain the separate roles of the two macros:

| Setting | The message in the example | The assert check |
|---|---|---|
| No -DDEBUG and no -DNDEBUG | Disabled. | Active. |
| Only -DDEBUG | Enabled. | Active. |
| Only -DNDEBUG | Disabled. | Skipped. |
| -DDEBUG and -DNDEBUG together | Enabled. | Skipped. |

The table applies to the given source and to macros not overridden by another
setting. NDEBUG must be defined before the insertion of cassert. A
debug/release naming does not replace knowing the actual settings.

Then ask for reasoning: "Why do we not rely only on assert for checking the
age?" Wait for the answer. The "assert does not run if there is no DEBUG"
explanation is partly wrong; acknowledge the recognition that it can be
switched off, but correct the macro name and the condition.

**After the answer:** Under NDEBUG the check is skipped. The validation of the
input is done by the if statements of L04. We should not put a side effect
needed for the program's operation into the assert condition. The skipping of
the check alone does not mean a guaranteed crash; the consequence depends on
the program.

The execution of the output statements before the assert and the actual
appearance of the text differ: at an abnormal termination the buffered output
may stay incomplete. Do not promise lines that certainly appear, and do not
ask for a separate termination trial.

### E4 – Optional demonstration: include guard

Protection against multiple inclusion prevents a header from being processed
again in the same translation unit. In the classroom favourites.h example the
#ifndef checks the absence of the guard macro, the header defines the macro,
and the #endif closes the part. At a second inclusion the inner content is
skipped. An empty guard block in a single .cpp would not demonstrate this; do
not have the student make one.

## Closing and repetition

First check internally the actual state of the steps. Do not write a skipped
trial as done. Briefly summarize the topics covered. If the student asks for
repetition, give one question at a time, aimed at an earlier uncertainty.
Do not automatically repeat all the questions if the understanding is already
clear.

Possible questions, without giving the solution in advance:

- What changes when saving, and what changes when compiling?
- Why does the total not update automatically when count changes?
- Why do the results of 5 / 2 and 5.0 / 2 differ?
- Why does reading the number after Kiss Anna cause a problem if >> read the
  name?
- Why can the number of visible letters and the number of stored char
  elements differ?
- Why does letter stay unchanged after s is modified?
- How do a read error and a violation of the allowed range differ?
- What controls switching assert off in the macro example?

Evaluate the answer precisely. After an assisted solution, the statement "we
discussed it" is right; "you solved it independently and flawlessly" is not.
For the next session, promise only a continuation for which the necessary
state is actually available.
