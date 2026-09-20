# CPP_03 – Practice Tasks

The tasks use short programs. The basic program structure is already prepared in each file; you write the marked parts yourself. Save after each change, then compile and run the program.

You have two options:

1. **RUN button:** use the RUN button above the code editor to compile and run the current file. You do not need to change directories.
2. **Terminal:** for example, for the first file:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G03_01_if.cpp -o G03_01_if
./G03_01_if
```

Always adapt the filename and executable name to the current task. You may use either method throughout the practice. In the starter TODO files, the compiler may show an `unused variable` warning because a provided variable is not used yet. This usually disappears after you complete the task.

## G03_01 – simple if

**File:** `G03_01_if.cpp`

Write an `if` statement that prints `Freezing risk.` when the temperature is below the freezing point. The line `Check complete.` must always be printed.

Test at least with temperatures `-3` and `2`.

## G03_02 – if–else

**File:** `G03_02_if_else.cpp`

Decide whether the value of `number` is even or odd. Exactly one of these messages should be printed:

- `The number is even.`
- `The number is odd.`

Test with 17, 18, and 0.

## G03_03 – several possibilities

**File:** `G03_03_score.cpp`

Classify the score:

- 80–100: `Excellent`
- 60–79: `Satisfactory`
- 0–59: `Needs improvement`
- below 0 or above 100: `Invalid score`

Use an `if / else if / else` chain. Test boundary values too.

## G03_04 – switch

**File:** `G03_04_switch.cpp`

Print according to `position`:

- 1 → `First`
- 2 → `Second`
- 3 → `Third`
- any other value → `Unknown`

Use `switch`, `case`, `break`, and `default`.

## G03_05 – while

**File:** `G03_05_while.cpp`

Use a `while` loop to print the numbers from 1 to 5, one per line. Make sure the loop variable moves toward the exit condition in every iteration.

Then test with a starting value of 6 as well.

## G03_06 – do–while

**File:** `G03_06_do_while.cpp`

Use a `do–while` loop to print the numbers from 1 to 3. Then change the starting value to 4 and observe how the behavior differs from the `while` task.

## G03_07 – for

**File:** `G03_07_for.cpp`

Use a `for` loop to print the numbers from 1 to 5. Then modify it so the output becomes:

```text
2
4
6
8
10
```

## G03_08 – number of even values

**File:** `G03_08_even_count.cpp`

Traverse the range 1..10 with a `for` loop and use `if` to count the even numbers. At the end, print the result in this form:

```text
Number of even numbers: <result>
```

Then test the range 3..9 as well. Determine the second result from your program run rather than from the task description.

## G03_09 – sum of numbers divisible by 3

**File:** `G03_09_divisible_sum.cpp`

Traverse the range 1..15. Add only numbers divisible by 3 to the `sum` variable. At the end, print the result in this form:

```text
Sum: <result>
```

Then test the range 1..10 as well. Check the numerical result with the program rather than reading it from the task description.

## Final test

After the coding tasks, the tutor leads two short tests:

1. multiple-choice questions;
2. prediction of the output of short C++ code fragments.

For output prediction, answer first and only then check the execution if needed.

**There is no homework.** The required practice ends with the final tests and the tutor’s closing summary. After the practice has clearly ended, the tutor may offer **one short optional extra task**. It is not part of the required CPP_03 practice.

## Optional extra practice

After the required CPP_03 practice has ended, if you want one more short exercise, the tutor may offer `G03_EXTRA_practice.cpp`. This is **not homework**, is not required, and does not affect the final-test result.
