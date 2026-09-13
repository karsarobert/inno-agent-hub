# C++ basics – English student practice package

This package accompanies the revised **CPP_01.html – C++ basics** classroom material.
The complete programs are provided. First read and interpret them, then compile,
run, and make the small, precisely specified changes.
No previous programming knowledge or independent program writing is required.
The classroom HTML file is a separate resource and is not included in this ZIP.

## Recommended order

The lesson identifiers have been retained, so the numbers in the filenames do not
indicate the recommended study order. The macro examples are optional exercises.

| Order | File | Related classroom topics |
|---|---|---|
| 1. Core exercise | `L01_first_program.cpp` | First program; saving, compiling and running; compilation errors |
| 2. Core exercise | `L01b_variables_and_values.cpp` | Initialization, assignment, integer and floating-point division, simple branching |
| 3. Core exercise | `L04_input_strings_validation.cpp` | Input, input validation, strings, indexing and conversion |
| 4. Optional exercise | `L02_preprocessor_macros.cpp` | Preprocessing, `#include`, `#define`, `-E`, `constexpr` |
| 5. Optional exercise | `L03_conditional_macros.cpp` | Conditional compilation, `-D`, function-like macros, `assert` |

Your learning assistant provides the steps. First you receive a question or an
observation task, then you try the example and discuss what happened. You do not
need to retype the programs. You do not need to read the instructor Markdown files
in advance; open the source files listed above for practice.

If four 45-minute blocks are available, core exercises 1–2 can be covered in the
first block and core exercise 3 in the second. The remaining blocks can be used
to revisit the basics or cover the two optional exercises, depending on progress.
You do not need to understand macros to complete the core exercises.

## Setup and execution

1. Extract the ZIP. Keep the source files in the root of the extracted workspace;
   do not create a separate subfolder for them.
2. Open a terminal in that directory. What matters is the terminal's current
   working directory, not the position of its window on the screen.
3. The commands assume Linux and a command-line GCC compiler supporting C++20.
   Use `g++ --version` to check that the compiler is available.
4. After changing the source, save it and compile again. Run the resulting program
   only after successful compilation.

Commands for the first program:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01 L01_first_program.cpp
./L01
```

`-std=c++20` selects the language standard. `-Wall` and `-Wextra` enable many useful
warnings, but not all warnings. `-pedantic` reports certain departures from the
selected ISO language standard. `-o L01` names the executable file. `./L01` runs it.

Compiling alone does not display the program's messages. If compilation fails,
an older executable may still exist: running it does not test the new code.

## Language and characters

The explanations, comments, program messages and identifiers are in English.
The `DEBUG`, `NDEBUG` and `SQUARE` macro names are retained for comparison with the
classroom examples. Sample names and strings have been adapted, and the expected
outputs in the instructions match these English source files.

The length of a `std::string` is not generally a letter count. `size()` returns
the number of stored `char` elements; in UTF-8, an accented letter may occupy
several bytes. Start with ASCII examples when examining individual characters.
An accented name is used deliberately in the UTF-8 exercise.

## Viewing long files

Preprocessor output can be long because it contains the included headers.
In the optional exercise, our own program is at the end of the file, so after
creating it, it is enough to inspect its last twenty lines:

```bash
g++ -std=c++20 -E L02_preprocessor_macros.cpp -o L02_preprocessed.ii
tail -n 20 L02_preprocessed.ii
```

Run the second command after the first one succeeds. `tail` only displays the
end of the file; it does not change it. You do not need to open the entire file
or paste it into the conversation.

## Instructor files

`agent.md` contains the English tutor role and teaching rules. Its existing name
is retained for compatibility with the original workspace setup.
`LESSON_INSTRUCTIONS.md` contains the complete English lesson sequence, questions,
expected outputs and restoration steps. All references to renamed files have
been updated. The lesson identifiers and the core/optional distinction are unchanged.
