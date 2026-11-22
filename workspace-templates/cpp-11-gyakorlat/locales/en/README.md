# C++ 07–10 – short InnoAgent practice

24 independent coding tasks, each followed by 1–2 theory questions about your code. Four blocks of six tasks. The 47 theory questions are discussed after coding.

## Getting started

1. Extract the complete English package into its own working directory, keeping the `data` directory.
2. Open that directory in InnoAgent. Tutor instructions are in `agent.md`. If the interface does not load them automatically, provide that file as the tutor instructions and make the package files available.
3. Open `g07_01.cpp`. Compile and run one `.cpp` at a time: each has its own `main`.
4. The tutor guides you in small steps. Read `TASKS.md` for task details and use `WORKSHEET.md` for notes.

## Running the code

C++17 and the standard library, with no additional C++ packages. Example terminal command:

```bash
g++ -std=c++17 -Wall -Wextra -pedantic g07_01.cpp -o g07_01 && ./g07_01
```
The `&&` prevents an old program from running after a compilation failure. In InnoAgent use RUN for the selected file. Run from the package root so `data/...` paths resolve correctly. Supply the exact task input on each run; handling console input outside the stated ranges is outside the task contracts.

G07_05, G08_02, G08_04 and G09_03 intentionally start with compilation errors. Other starters may compile but remain incomplete or incorrect. G09_04 refactors working code. Starter code is not a model solution.

File tasks write `out01.txt` and `out02.txt`; keep the `data` fixtures unchanged. Initially `out02.txt` contains `2`. Do not reset it between the two linked G10_02 runs. Refresh the file view if a newly created file does not appear.

## Blocks

| Block | Topics | Estimated time |
|---|---|---|
| 07 | Structures, copying, pointers, scope, unions | 45–60 min |
| 08 | Classes, private members, getters, const, object arrays | 45–60 min |
| 09 | Constructors, initialization, composition, supplied virtual example | 45–60 min |
| 10 | Writing, appending, reading, validation, safe replacement | 60–75 min |

Times are estimates; split the work across sessions as needed. There is no final project, separate exit quiz or submission task. After checking the code, the tutor asks the corresponding theory questions one at a time. Progress can be resumed from saved state.
