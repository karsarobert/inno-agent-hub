# CPP_05 – Lesson Instructions

## Overview

Time frame: **3 × 45 minutes**.

- Block 1: function fundamentals – `G05_01`…`G05_04`
- Block 2: project – `P05_measurement_data.cpp`, P1…P7
- Block 3: midterm preparation – 20 pre-written questions

The student writes the code. Before every new project section, the tutor shows and explains
a short sample, but does not automatically write the project solution.

---

# Block 1 – Function fundamentals

## G05_01 – First custom function

**File:** `G05_01_first_function.cpp`

### Task A

The student creates a function named `square` that receives one integer and returns its
square. In `main()`, call it with the existing `value` variable and print the result.

**Expected result:** 36.

Do not immediately give the complete `int square(int number)` header. If needed, recall the
parts separately: return type, name, parameter, `return`.

### Task B

Create a function named `doubleValue` that returns twice an integer. Call it using the same
`value` argument.

**Expected result:** 12.

Short understanding check: which name is the parameter, and which variable is the argument
in the call?

---

## G05_02 – Multiple parameters

**File:** `G05_02_parameters.cpp`

### Task A

Create a `double` function named `rectangleArea` that calculates a rectangle's area from
two `double` parameters.

**Expected result:** 13.5.

### Task B

Create a `rectanglePerimeter` function with the same two parameters.

**Expected result:** 15.

After running, emphasize that the same arguments can be passed to two different functions
that solve two different subproblems.

---

## G05_03 – `void` procedure

**File:** `G05_03_void.cpp`

### Task A

Create a parameterless `void` function named `printHeader` that prints, for example:

```text
=== MEASUREMENT RESULTS ===
```

### Task B

Create a `void` function named `printMeasurement` that receives one integer parameter and
prints it in the form `Measurement: <value>`.

Ask once during the block: why can the `printHeader()` call not be used on the right side of
an assignment such as `int result = ...`? Expected idea: `void` does not return a value.

---

## G05_04 – Prototype

**File:** `G05_04_prototype.cpp`

The definition of `add` is intentionally placed after `main()`.

### Task A

1. The student adds a call in `main()` that prints the result of `add(a, b)`.
2. Compile it. At the call site, the compiler does not yet know the `add` function.
3. Keep the definition after `main()` and solve the problem using a function prototype.

**Expected result after the fix:** 11.

### Task B

The student defines a `difference` function after `main()`, adds its prototype before
`main()`, then prints the result of `a - b`.

**Expected result:** 5.

### Required explanation

A prototype is useful when:

- we want to keep the function definition after `main()`;
- we want a quick overview near the beginning of the program of what operations can be called;
- later we split the program into multiple source and header files;
- the compiler can already check return and parameter types at the call site.

A prototype does not execute the function and does not replace its definition.

---

# Block 2 – Project: Measurement Data Analyzer

**File:** `P05_measurement_data.cpp`

Before each step, show the indicated sample from `SAMPLE_CODE.md`. Explain the sample in
2–5 sentences, then ask the student to create the project version.

For every project function, the student creates a prototype before `main()` and keeps the
definition after `main()`. This immediately applies the structure learned in G05_04.

## P1 – `printData`

**Sample:** M2.

Show the M2 `printScores` example. Explain:

- `void`: no return value;
- `const int*`: the function reads the array elements but does not modify them;
- size is a separate parameter;
- the loop accesses elements through an index.

Then the student creates a `printData` function for the project and calls it from `main()`.

**Expected data sequence:** 18 24 11 29 21 17.

## P2 – `sum`

**Sample:** M3.

Show the M3 summing pattern, emphasizing the accumulator's initial value of 0, the loop,
and the role of `return`.

The student creates a `sum` function for the project.

**Expected result:** 120.

## P3 – `average`

**Sample:** M4, and if necessary recall M3.

The `average` function should **not write another summing loop**. It should call the project's
own `sum` function and use its result to calculate the average. The result must be `double`.

If needed, show an analogous `static_cast<double>` example to preserve the fractional part,
but do not immediately write the project's full `return` statement.

**Expected result:** 20.

Required short explanation: one custom function may call another custom function; this can
reduce code repetition.

## P4 – `maximum`

**Sample:** M5.

The student creates a `maximum` function. You may assume `size > 0`. The initial maximum
should be the first element; traversal may begin with the next element.

**Expected result:** 29.

## P5 – `countAboveThreshold`

**Sample:** M6.

Project function parameters:

- data;
- number of elements;
- threshold.

Count values that are strictly greater than the threshold.

**Expected result with threshold 20:** 3.

The sample uses `>=`, but the project requires **`>`**. Point this out, but let the student
write the concrete `if` line.

## P6 – `increment`

**Sample:** M7.

The student creates a `void` function named `increment` with one `int*` parameter. It
increases the pointed-to integer by 1.

Before the call, ask one short prediction: will the original `alertThreshold` variable
change? Then call the function with the address of `alertThreshold`.

**Expected new threshold:** 21.  
**Expected count above 21:** 2.

Connect this to the previous lesson: with a by-value `int` parameter we would receive a copy;
by passing the address, the function can access the original variable.

## P7 – `distance`

**Sample:** M8.

The student creates `distance(double x, double y)` using `sqrt` from `<cmath>`. Because the
course uses `using namespace std;`, `sqrt(...)` can be written without qualification; its
full name is `std::sqrt`.

**Expected result for `3.0`, `4.0`:** 5.

At the end, briefly summarize the project structure: prototypes → `main()` → function
definitions; `main()` organizes the program, while named functions solve the subproblems.

---

# Block 3 – Midterm preparation test

Ask the questions from `FINAL_TEST.md` one at a time, without changing them.

## T1 answer key

1. B – functions can reduce code repetition and separate subproblems.
2. A – a parameter is the input variable written in the definition.
3. C – an argument is the concrete value/expression passed during the call.
4. B – `return` gives a value back and ends that function call.
5. A – `void` means there is no return value.
6. C – with a simple value type, the parameter receives a copy.
7. A – a prototype tells the compiler the function interface in advance.
8. B – a local variable is visible only within its own scope.
9. B – `#include` and `using` perform different jobs.
10. C – `<cmath>` provides declarations for mathematical functions.

## T2 answer key

### T2/1
`14`

Reason: `doubleValue(4)=8`, `doubleValue(3)=6`, total 14.

### T2/2
`10`

Reason: `modify` receives `number` by value, so it changes a copy; the original `value`
does not change.

### T2/3
`25`

Reason: `3*3 + 4*4 = 9 + 16 = 25`.

### T2/4
`20`

Reason: `2 + 5 + 3 + 10 = 20`.

### T2/5
`6`

Reason: the function receives the address of `x` and increases the original pointed-to value.

### T2/6
Main problem: `add` has no known declaration at the call site. Smallest fix: place
`int add(int a, int b);` before `main()`, or move the complete definition before `main()`.
The primary expected answer is the prototype.

### T2/7
The function is `void`, so it cannot return the value `a + b`. A natural fix is to change
the return type to `int`; if it really should remain `void`, then it must not return a value
and the result must be handled differently. For this question, changing to `int` is the most
direct expected fix.

### T2/8
`area` expects two parameters, but the call supplies only one argument. The call must provide
two suitable arguments.

### T2/9
Because of `i <= size`, when `i == size` the program accesses `data[size]`, which is outside
the array. The safe condition here is `i < size`.

### T2/10
`cout` is in the `std` namespace. Fix it by writing `std::cout`, or by adding an appropriate
`using namespace std;` / `using std::cout;`. This course uses the `using namespace std;`
pattern.

## Test scoring

- T1: 10 points.
- T2: 10 points.
- Each question is worth 1 point; the first substantive answer counts.
- For debugging tasks, accept technically equivalent correct fixes.
- At the end, name review topics only from questions the student actually missed.

Suggested topic labels:

- function structure / parameter and argument;
- `return` and `void`;
- pass by value;
- prototypes and declaration order;
- local scope;
- namespaces and headers;
- loop bounds and arrays;
- modification through pointers;
- custom functions calling other custom functions.
