# C++ Basics – Student practice pack (English)

This pack belongs to the revised **CPP_01.html – C++ Basics** classroom
material. All programs are provided complete. First read and interpret them,
then compile, run, and carry out the small, precisely specified changes.
No prior programming knowledge or independent program writing is required.

## Recommended order

We kept the original file names, so the numbers in their names do not indicate
the recommended order of working through them. The macro examples are
supplementary exercises.

| Order | File | Related class topics |
|---|---|---|
| 1. Core exercise | `L01_elso_program.cpp` | First program; saving, compilation and running; compilation errors |
| 2. Core exercise | `L01b_valtozok_es_ertekek.cpp` | Initialization, assignment, integer and floating-point division, simple branching |
| 3. Core exercise | `L04_io_string_hibakes.cpp` | Reading input, input validation, strings, indexing and conversion |
| 4. Supplementary | `L02_preprocesszor_makro.cpp` | Preprocessing, `#include`, `#define`, `-E`, `constexpr` |
| 5. Supplementary | `L03_felteteles_makro.cpp` | Conditional compilation, `-D`, parameterized macros, `assert` |

The steps of the exercise are given by the assistant that guides your
learning. First you get a question or an observation task, then you try out
the example, and you discuss what you experienced. You do not need to retype
the programs. You do not need to read the teacher-facing Markdown files in
this pack in advance; for the practice, open the source files listed above.

If four 45-minute blocks are available, exercises 1–2 can be worked through
in the first block and core exercise 3 in the second. In the further blocks,
repetition of the core material or the two supplementary exercises may follow,
depending on progress. Knowing the macros is not a prerequisite for
understanding the core exercises.

## Preparation and running

1. Unpack the ZIP file. Keep the source files in the root directory of the
   unpacked workspace; do not create subfolders for them.
2. Open a terminal in this directory. What matters is where the terminal's
   current directory is; where the terminal window sits on the screen does not.
3. The commands are written for Linux and for a GCC reachable from the command
   line that supports C++20. You can check the compiler with `g++ --version`.
4. After a modification, save the source, then compile again. Run the
   resulting program only after a successful compilation.

The concrete commands for the first program:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -o L01 L01_elso_program.cpp
./L01
```

`-std=c++20` selects the language standard; `-Wall` and `-Wextra` enable many
useful warnings, but not all of them. `-pedantic` flags certain deviations
from the selected ISO language standard. `-o L01` gives the name of the
resulting executable. `./L01` runs it.

Compilation alone does not print the program's messages. If the compilation
fails, an older executable may remain: running it does not test the new code.

## Language and characters

The explanations and comments are in English. The programs' printed messages
and identifiers use English words, typically without special characters,
matching the classroom code examples. The macro names `DEBUG`, `NDEBUG` and
`SQUARE` are kept so they can be compared with the classroom examples.

We do not generally call the length of a `std::string` a letter count. The
`size()` gives the number of stored `char` elements; for UTF-8 text one
accented letter can consist of several bytes. For character-by-character
observations, use samples without accents first.

## Viewing long files

The result of preprocessing can be long because of the included headers. In
the supplementary exercise our own program is at the end of the file, so after
creating it, it is enough to look at the last twenty lines:

```bash
g++ -std=c++20 -E L02_preprocesszor_makro.cpp -o L02_preprocessed.ii
tail -n 20 L02_preprocessed.ii
```

Use the second command after the first one has executed successfully. The
`tail` only displays the end of the file; it does not modify it. You do not
need to open the whole file or paste it into the conversation.
