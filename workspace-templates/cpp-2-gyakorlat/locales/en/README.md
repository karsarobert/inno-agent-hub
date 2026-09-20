# C++ – Practice 2: variables, types, and number representation

This package is the practical continuation of the revised **CPP_02.html** theory material.
The theory HTML is a separate file and is not required to run the practice.
Time frame: **3 × 45 minutes of practice**, excluding breaks.

We start from short, complete programs. After the tutor explains the idea, you make small
changes, observe the behaviour, and explain why you obtained that result. In the final task
you will independently correct one calculation line. You do not need to write a complete
program from an empty file.

## How we work during the practice

**You edit and save the code, and you also compile and run it yourself.**
This applies to the first demonstration program, every modification, and debugging as well.
Inno explains the task, shows the line to change and the terminal commands when necessary,
then waits for your result. A correct prediction is followed by your own test.

You may compile and run the current file in either of two ways:
- use the **RUN** button above the code editor; no `cd` command is needed for this;
- or use the Linux terminal with `g++` and run the generated executable manually.

It is enough to send the requested output line or your observation. If compilation fails,
do not run an old executable as if it belonged to the new code; send the first relevant
compiler error instead. Inno helps you interpret and correct it, but you make the edit.

The modified code remains in place after each task: you do not restore the original version.
The next experiment builds on the current state. Only an intentionally introduced error is
repaired so that work can continue.

If you are replacing an older version of this package, replace `agent.md` and
`LESSON_INSTRUCTIONS.md` in the workspace, then start a new tutor conversation so the new
instructions take effect. Do not overwrite your own already modified source files with the
starting versions from this package.

## Checking code understanding

Except for the bit-pattern task, each core task also includes a short explanation of an
important code fragment in your own words. After a successful experiment, Inno highlights
1–3 important lines and asks what they do and what the result means. You do not need textbook
wording or a line-by-line explanation. If you have already explained the idea clearly, it does
not need to be repeated.

If you get stuck, you receive an explanation and a small thought example; this does not require
another edit or compilation. Correct output and code understanding are tracked separately.
If a numerical result differs from what the data imply, the current values and source lines are
checked before moving on, even if the final true/false result happens to match expectations.

## Starting in Innoagent

1. Extract the ZIP into a new folder for the second C++ practice. Put the files directly in the
   root of that workspace. Do not copy it over the first practice folder because both packages
   contain an `agent.md` file.
2. Open this folder as the Innoagent workspace using your usual setup.
3. Type: **“Let’s start C++ Practice 2!”**
4. Edit the `.cpp` files in the code editor. Use either the **RUN** button above the editor or a
   Linux terminal opened in the same workspace to compile and run them.

The package follows the file structure of the previous practice. Loading workspace instructions
depends on the Innoagent configuration; the ZIP itself does not install or configure the app.
`agent.md` and `LESSON_INSTRUCTIONS.md` guide the tutor; for the practice, open the source file
named in the current task.

## Task order

| File | Topic | Suggested time |
|---|---|---:|
| `G02_01_types.cpp` | Storage size and type limits | 15 min |
| `G02_02_initialization.cpp` | Initial value, assignment, constants | 10 min |
| `G02_03_bit_patterns.cpp` | Eight bits, two interpretations | 15 min |
| `G02_04_division.cpp` | Division and where conversion happens | 15 min |
| `G02_05_ranges.cpp` | Unsigned wraparound and a large multiplication | 15 min |
| `G02_06_precision.cpp` | Floating-point approximation and significant digits | 15 min |
| `G02_07_formatting.cpp` | Storage and output formatting | 10 min |
| `G02_08_tolerance.cpp` | Comparison using an absolute tolerance | 10 min |
| `G02_09_scores.cpp` | Integrating concepts in a debugging task | 15 min |

Allow 5 minutes for the warm-up and 10 minutes for closing: 135 minutes total.
The timing is flexible; additional experiments and optional tasks are not compulsory.

`G02_K01_overflow.cpp` is a separate optional demonstration. Its starting state is correct.
It is modified into an incorrect version only with the tutor and with the required runtime
checking enabled. It is not part of the 135-minute core path.

## Compiling and running

A GCC version with C++20 support is required. Check it with:

```bash
g++ --version
```

For the first task:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_01_types.cpp -o G02_01
```

After successful compilation:

```bash
./G02_01
```

Alternatively, use the **RUN** button above the code editor. The RUN button handles the current
file path automatically, so do not change directories just to use it.

For later tasks, the tutor gives the concrete terminal command when needed. The name after `-o`
is the executable to run. After every source modification, save and compile again. If compilation
fails, do not use an older executable as evidence for the new code. The core programs do not ask
for runtime input; the tested values are changed in the source code.

## Clean code in this beginner practice

- Use meaningful English identifiers in consistent `snake_case`; avoid names such as `a`, `b`,
  or `x` when the role can be named clearly.
- Include the unit in the name when it matters for interpretation, for example
  `measured_length_m`.
- Use named constants for settings and task rules. `constexpr` is used for settings known at
  compile time, while `const` is used for calculated results that are not changed later.
  Variables intentionally changed during an experiment remain mutable.
- Use four-space indentation, clear blocks, and the `std::` prefix consistently.
- Comments should explain why something is done, an important limitation, or an intentional
  error experiment. They should not merely repeat the code or reveal the answer to a prediction.
- Each file focuses on one learning idea. The repeated structure in the eight-bit model is a
  deliberate simplification because arrays and functions have not yet been introduced.
- Names such as `first_average` identify compared variants; the final task uses semantic names
  such as `average_score`.

Task 9 contains a clearly marked **logical error**. Well-formatted, well-named code can still be
wrong; the error is found by checking the calculation. After intentional error experiments, only
the introduced error is repaired. Other successful modifications remain in the file.

## Environment differences

Type sizes are queried on the student’s own machine. The detailed floating-point examples assume
a common IEEE 754 binary32 (`float`) and binary64 (`double`) environment with ordinary rounding.
A different result is not automatically a student error. Decimal literals in source code use a
period. All explanations, filenames, identifiers, comments, and program output in this English
package are in English.
