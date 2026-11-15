# CPP_10 – InnoAgent student package

**3 × 45 minutes, excluding breaks.** File I/O and persistent storage for the box office.

1. Extract into a new, empty folder. Keep HU and EN packages separate.
2. Open it as an InnoAgent workspace using your established configuration.
3. Say: **“Let's start C++ practice 10!”**
4. You write and save the new code. Run one `.cpp` file at a time using RUN.

Block 1 has four foundation exercises, block 2 has six connected project stages, and block 3 has 20 fixed questions. There is no homework or separate extra task set. Timings are guidance: unfinished work must not be marked complete.

The four G10 sources are compilable starters only. P10 provides the previously learned ticket and box-office operations so you do not have to rewrite lesson 9. **It provides no saving, loading or report implementation.** You write those. The HTML measurement-log code is not a ready solution: this project adds a header, row/seat ranges, duplicate bookings and different empty-file rules.

| File | Purpose |
|---|---|
| agent.md | Tutor instructions |
| LESSON_INSTRUCTIONS.md | G10_01–04 requirements and checks |
| EXAMPLES.md | Complete analogous programs, not target solutions |
| PROJECT.md | P1–P6 requirements |
| STUDENT_WORKSHEET.md | Quick concept and format reference |
| FINAL_QUIZ.md | 20 questions without an answer key |
| PROGRESS.json | Tutor-maintained resume state |
| *.txt | Parsing/project fixtures, not C++ source files |

The ZIP neither installs nor configures InnoAgent. Loading workspace instructions depends on the application configuration. Do **not** place the instructor package in this workspace.

Relative filenames refer to the program's working directory. If the supplied ok.txt cannot be found, establish RUN's working directory first; do not change the loader to hide an environment problem. Refresh the file view if a newly created file is not visible. Examples are checked with Linux/GCC, C++20 and LF line endings.

For a RUN problem, from a terminal opened in this package folder:
`g++ -std=c++20 -Wall -Wextra -Wpedantic G10_01_save.cpp -o g01 && ./g01`

Run only after a successful compilation. Do not compile all five sources into a single program: each has its own main.
