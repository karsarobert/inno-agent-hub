# C++ Basics — Student Practice Workspace

This workspace is an independent practice space for the **"C++ Basics"**
course material (4 × 45-minute lesson). Here **you yourself** type in, compile
and run the code.

## ⚠️ The most important things to know

- **Work at the root:** create every `.cpp` file at the **root of this
  workspace** (not in subfolders). This way you can run it right away and the
  paths stay simple.
- **Use the terminal below the workspace:** work in the **Terminal** window at
  the bottom (or on the right) — that is where we run `g++`. For every lesson I
  will give the exact commands to compile and run.
- **Save the file before compiling** (Ctrl+S), otherwise you compile the old
  version.

## The lessons

| File | Lesson | What we practise |
|------|-------|-----------------|
| `L01_elso_program.cpp` | Lesson 1 | First program: **observing** compilation–running (code given) |
| `L02_preprocesszor_makro.cpp` | Lesson 2 | `#include`, `#define` macros, the `-E` switch |
| `L03_felteteles_makro.cpp` | Lesson 3 | `#ifdef/#else/#endif`, `-D`, include guards, parameterized macros |
| `L04_io_string_hibakes.cpp` | Lesson 4 | `cin`/`cout`, `std::string`, conversion, `assert` |

## The general way of running (g++)

```
g++ -Wall -o program your_file.cpp
./program
```

> If you are in the terminal below the workspace and the file is at the root,
> this works as is — no path needed.

Preparation for the lessons is based on the lesson plan: `01..04_*.md` in the
teacher's material.
