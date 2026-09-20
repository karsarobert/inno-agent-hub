# C++ Practice 03 – Internal Lesson Instructions

## Time frame

Total time: 3 × 45 minutes. The practice is strongly hands-on. Explanations should be short; most of the time should go to student code writing, compiling, running, and interpretation.

Suggested timing:

- Block 1: E0 5 min, G03_01 9, G03_02 9, G03_03 11, G03_04 9, S1 2.
- Block 2: G03_05 12, G03_06 10, G03_07 15, summary 8.
- Block 3: G03_08 12, G03_09 12, T1 8, T2 10, closing 3.

These minute values are estimates. Do not invent elapsed time.

## E0 – start and workflow

The agent must introduce itself according to `agent.md`. Tell the student that from this practice onward they will write more short code fragments themselves, but they do not need to build complete programs from an empty file. The files already contain the program frame and some necessary variables.

At the beginning, explain the two ways to run a program once:

1. the **RUN** button above the code editor: after saving, the student can use it to compile and run the current file;
2. from the terminal, for example:
   `g++ -std=c++20 -Wall -Wextra -Wpedantic G03_01_if.cpp -o G03_01_if`
   followed by `./G03_01_if`.

State clearly that either method is acceptable. Do not ask for `cd` when the student uses the RUN button. Repeat the full `g++` command later only when needed.

Before every task, check the actual task description and the related `.cpp` file. For example, G03_01 is the **freezing-risk task**; do not replace it with a different `if` exercise.

Only check `g++ --version` if necessary. Do not spend practice time on compulsory environment diagnostics when compilation already works. Some starter TODO files may produce an `unused variable` warning before the TODO is completed; this is expected because provided variables are not yet used. Do not treat it as a compilation error.

## G03_01 – simple if

**File:** `G03_01_if.cpp`

**Goal:** when the temperature is below the freezing point, print `Freezing risk.`, then always print `Check complete.`

**New concept:** the body of an `if` runs only when the condition is true. Execution continues after the selection.

**Analogous micro-example if needed:**

```cpp
if (age >= 18) {
    std::cout << "Adult.\n";
}
```

Do not immediately provide the complete ready-made `if` block for the student’s own task.

**Student task:** write the `if` block at the TODO using the existing `temperature` and `freezing_point` variables.

**Test 1:** `temperature = -3` → two lines: `Freezing risk.` and `Check complete.`

**Test 2:** change `temperature` to `2` → only `Check complete.`

**Code understanding:** briefly ask why the second line appears in both runs.

## G03_02 – if–else

**File:** `G03_02_if_else.cpp`

**Goal:** decide whether an integer is even or odd.

**Prior knowledge:** `%` is remainder. If needed, briefly recall that `17 % 2` is 1 and `18 % 2` is 0.

**Student task:** write an `if–else` at the TODO. The condition should use `number % 2 == 0` or an equivalent expression.

**Tests:** 17 → `The number is odd.`; 18 → `The number is even.`; 0 → `The number is even.`

After the first two tests, explicitly ask about zero because it is a useful boundary case.

**Code understanding:** why does exactly one branch run?

## G03_03 – else if chain

**File:** `G03_03_score.cpp`

**Goal:** classify a score between 0 and 100 into three categories:

- 80 or more: `Excellent`
- 60–79: `Satisfactory`
- 0–59: `Needs improvement`
- below 0 or above 100: `Invalid score`

The file already contains the thresholds and the `score` variable. The student writes the complete selection chain.

**Teaching:** first discuss checking the invalid range. Then discuss the first-true-branch rule. There is no need for two-sided conditions for every middle range when earlier branches have already excluded larger values.

**Tests:** -1, 0, 59, 60, 79, 80, 100, 101. They do not all need to be run in one sequence; at least one value from each boundary pair should be tested.

**Common error:** with independent `if` statements, more than one category may be printed. Do not immediately give the fix; first ask why several conditions could be true at the same time.

## G03_04 – switch

**File:** `G03_04_switch.cpp`

**Goal:** for 1, 2, or 3 print `First`, `Second`, or `Third`; for any other value print `Unknown`.

**New concept:** `switch` selects among `case` branches based on one integer/enum-like expression. `break` closes the current branch.

The student writes the `switch` structure. If they get stuck, first show only one `case` example using different data.

**Tests:** 2 → `Second`; 5 → `Unknown`.

**Short demonstration, only after the working solution:** ask the student to temporarily remove the `break` from a middle branch, compile/run, observe fall-through, and then **have the student restore the `break`**. This is a deliberate behavior experiment, not a final source state.

## S1 – close block 1

Briefly summarize: simple `if`; two-way `if–else`; first true branch in an `else if` chain; `switch` and `break`. Record the actual state in learner memory. No homework.

## G03_05 – while

**File:** `G03_05_while.cpp`

**Goal:** print the numbers from 1 to 5, one per line.

The file already contains `const int last_number = 5;` and `int current_number = 1;`. The student writes the complete `while` loop.

**Teaching:** organize the explanation around three questions:

1. What is the starting value?
2. When may the loop continue?
3. What changes the state so that the loop can eventually terminate?

**Test:** 1..5.

**Modification:** set `current_number = 6` → print no number. This demonstrates that a `while` body may run zero times.

Do not intentionally run an infinite loop.

## G03_06 – do–while

**File:** `G03_06_do_while.cpp`

**Goal:** print 1 to 3 using a `do–while` loop.

The student writes the structure using the provided start value and limit.

**Test 1:** starting value 1 → 1, 2, 3.

**Test 2:** starting value 4 → the program prints 4 once. Ask why the body ran once even though the continuation condition was already false initially.

At the end, the student may restore the teaching example to a start value of 1 or leave the second test; there is no need to force a reset if the source state is clear.

## G03_07 – for

**File:** `G03_07_for.cpp`

**Goal:** print 1 to 5 using a `for` loop.

Only `last_number` is provided. The student writes the complete `for` loop. Before that, explain the three parts: initialization, condition, update.

**Test 1:** 1..5.

**Test 2:** modify the start value and update so the output becomes 2, 4, 6, 8, 10. Do not provide the complete loop header immediately. A new `const int` may be used for the final value.

**Code understanding:** what happens to the loop variable at the end of an iteration, and when does the loop stop?

## S2 – close block 2

Using the student’s own runs, summarize:

- `while` checks before the body;
- `do–while` checks after the body;
- `for` keeps the three control elements together for counting tasks.

Write a continuation checkpoint to memory. No homework.

## G03_08 – small combination: count even numbers

**File:** `G03_08_even_count.cpp`

**Goal:** examine the numbers from 1 to 10, count how many are even, and print the count as `Number of even numbers: ...`.

The file already contains:

- `const int first_number = 1;`
- `const int last_number = 10;`
- `int even_count{};`

The student must:

1. write a `for` loop to traverse the range;
2. use `if` inside the loop to test evenness;
3. increase the counter when the condition is true;
4. print the final result after the loop.

This is already a combination task. At first, give only the goal and the existing variables. Do not provide the loop header, the exact evenness condition, or the concrete counter-increment line. Do not state the expected count in advance. If the student gets stuck, first ask a guiding question: how did we earlier decide whether a number was even?

**Test 1:** 1..10. For the agent’s internal check, the correct count is 5, but say this only after the student’s own run or prediction.

**Test 2 – independent modification:** use the range 3..9. Again, do not reveal the numerical answer in advance; the internal correct count is 3.

## G03_09 – small combination: sum numbers divisible by 3

**File:** `G03_09_divisible_sum.cpp`

**Goal:** from 1 to 15, add the numbers divisible by 3 and print the result as `Sum: ...`.

The file already contains the range and the `sum{}` variable. The student writes the `for` + `if` solution and the accumulation.

At first, do not provide the finished divisibility condition or the `sum += current_number` line. The student should recall remainder and the role of an accumulator. If they get stuck, help progressively: question → short pseudocode → only then a concrete code line.

**Test 1:** 1..15. The correct internal check is 45, but do not reveal it before the student’s own attempt and do not list the divisible numbers in advance.

**Test 2:** 1..10. The correct internal check is 18; again use it only after the student produces their own result.

If the student hard-codes 45 by manually adding the concrete numbers, the task is not complete. The source must contain a loop, a condition, and an accumulator.

## T1 – final multiple-choice test

Ask the questions from `FINAL_TEST.md` one at a time. Correct answers:

1. B
2. C
3. A
4. C
5. B
6. D

Score: 0–6 correct. Do not convert this into an artificial percentage-based “knowledge level”.

Short explanations:

1. The `if` body runs only when the condition is true.
2. `if–else` selects exactly one branch.
3. In an `else if` chain, later branches are skipped after the first true branch.
4. `break` ends the current `case` branch.
5. A `do–while` body executes at least once.
6. In a counting `for`, initialization, condition, and update are visible together.

## T2 – final output-prediction test

Show the code one question at a time and wait for the student’s exact prediction.

Solutions:

1. `A` then `C` on separate lines – checks whether the student notices the independent statement after the `if`.
2. `Satisfactory` – exact-boundary `else if` tracing.
3. `Two` – `switch` and `break`.
4. `6` – tracing a `while` loop and accumulator.
5. `4` – initially false `do–while` that still executes once.
6. `2 4 6` – `for` + `if` together.

Score: 0–6 correct. Do not count minor formatting differences as errors if the execution path and printed values are correct.

## CLOSING

After the tests, do not start another required task. After a short factual summary, record the final learning event. State that there is no homework.

The required closing must visibly include:

**The required CPP_03 practice ends here.**

Only after that, offer the single optional `G03_EXTRA_practice.cpp` task. Do not start it automatically; wait for the student to ask for it. The optional task does not change the required practice or final-test result.

## EXTRA – optional one-task practice

**File:** `G03_EXTRA_practice.cpp`

**Goal:** traverse the range 1..12, print the numbers divisible by 3, and at the end print how many such numbers there were. This briefly combines `for`, `if`, divisibility, and counting.

At first, state only the goal. Do not provide the selected numbers, final count, ready-made condition, or counter-increment line. Use the same progressive support ladder as in G03_08–G03_09.
