# CPP_09 – InnoAgent student package

**3 × 45 minutes.** Constructors, valid initial state, cooperating classes and composition.

## Getting started

1. Extract into a new, empty working folder. Do not overwrite a previous lesson or the other language version.
2. Open the folder as your InnoAgent workspace using your existing setup.
3. Type: **“Let's start C++ practice 9!”**
4. Write and save the code yourself. Run one `.cpp` file at a time with RUN.

| File | Content |
|---|---|
| G09_01_competitor.cpp | Competitor: three constructor overloads |
| G09_02_brightness.cpp | Brightness: `?:`, initial state and updates |
| G09_03_parcel.cpp | Parcel and rate calculator |
| G09_04_result_sheet.cpp | Result sheet: object arrays and composition |
| P09_box_office.cpp | Theatre seat booking in six steps |

Starters compile on their own but do not solve the tasks. You write the requested classes, constructors, conditions and loops. Inno first explains a complete analogous program solving a different problem.

## Three blocks

1. Four foundation tasks: 45 minutes including the introduction.
2. Box office: 45 minutes in a single source file developed progressively.
3. 20 questions: 10 multiple choice, 5 output questions and 5 debugging questions; 45 minutes including feedback.

Breaks are additional. The lesson consists of these tasks; there is no extra task sequence. There is no homework or automatically announced upcoming test.

## Supporting materials

- `LESSON_INSTRUCTIONS.md`: precise foundation-task requirements.
- `EXAMPLES.md`: complete analogous programs with explanations.
- `PROJECT.md`: box-office steps and checking cases.
- `STUDENT_WORKSHEET.md`: short reference; no separate editing is required.
- `FINAL_QUIZ.md`: fixed questions without an answer key.
- `PROGRESS.json`: continuation state maintained by the tutor.
- `agent.md`: tutor instructions.

Keep the teacher solution package separate. Do not copy it into the student workspace. The ZIP itself does not install or configure InnoAgent; workspace-instruction loading depends on the application setup.

If RUN fails, or on request, use a terminal opened in the working folder:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G09_01_competitor.cpp -o G09_01 && ./G09_01
```

With `&&`, execution starts only after successful compilation. Do not compile all five sources together: each has its own `main` function.
