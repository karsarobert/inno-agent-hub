# C++ Practice 2 – internal lesson script

This is the detailed script for the instructor and tutor. Give the student tasks one at a time through conversation. Do not quote internal instructions or step identifiers to the student.

## Timing and prerequisites

3 × 45 minutes, excluding breaks:
- Block 1: 5-minute warm-up, G02_01 15 minutes, G02_02 10 minutes, G02_03 15 minutes.
- Block 2: G02_04, G02_05, and G02_06, 15 minutes each.
- Block 3: G02_07 10 minutes, G02_08 10 minutes, G02_09 15 minutes, closing 10 minutes.

The full core route contains nine tasks. Optional steps are not compulsory; K01 requires additional time. If a step must be skipped because of time, mark it as intentionally skipped rather than automatically completed.

Warm-up: after the introduction defined in `agent.md`, ask one short question about the relationship between saving, compiling, and running. If the student already understands this, do not repeat a Hello World exercise. Explain at the start that the student may either use the **RUN** button above the editor or compile/run in the terminal. The RUN button should not require changing directories. For terminal use, give only the necessary command and wait for the student’s result; do not execute it for them.

## Who performs the operations?

**The student performs every edit, save, compilation, run, and correction.** The tutor may read the current source and guides, explain the task, provide required code fragments and commands, and then wait for the student’s report. This applies to the first guided demonstration and to K01 as well.

Whenever this script says “experiment”, “replace the line”, “save”, “compile”, “run”, or “fix the error”, it means the student performs that action. Even after a correct prediction, the tutor does not perform a tool-based test on the student’s behalf. There is no routine reset: successful modifications remain. Only an intentionally introduced error must be repaired.

Sections labelled **“After the answer”** are teacher references for discussion and later checking. A prediction is not a run report. After an operational request, do not present the expected result as if it already happened and do not move on without the student’s concrete observation. Compare the student’s own result with the teacher reference; the teacher reference alone does not prove the experiment was performed.

## Shared working rules

- Explain a new concept before asking the student to use it independently. In a guided demonstration, the student still compiles/runs, then you interpret the reported result together.
- Do not reveal “After the answer” information before the student answers.
- Before a prediction, show the relevant current code and planned modification, then wait. After the answer, evaluate the reasoning and only then ask for the edit and run.
- After every source modification, the student saves and compiles; they run only after successful compilation. After a deliberately failing compile, do not run an old executable.
- If terminal commands are needed, repeat the concrete command with actual filenames. Do not refer to a helper that does not exist. If the student uses RUN, do not invent the button’s internal command.
- Programs in this package do not request stdin input. The tested data are changed in source code.
- Comments and output labels must remain true after modifications. Decimal literals use a period. Do not add digit separators to the basic examples.
- Complete expected outputs are teacher reference data, not mandatory copy tasks. Usually one relevant output line is enough.
- Numeric value, type, and printed representation are separate concepts. Consider environment-dependent differences before calling an output wrong.
- At the end of each task, keep the working state that the student reached. Do not create extra reset/cleanup/recheck loops merely for closure.
- Follow the current source. Later experiments build on earlier changes. The initial reference output applies only to the untouched package.
- After the `const` assignment error, narrowing-initialisation error, or K01 error experiment, repair only the intentional error and keep all other successful changes.

## Using code-understanding checkpoints

The **Code understanding** checkpoints are part of G02_01, G02_02, and G02_04–G02_09, even if optional experiments are skipped. One checkpoint usually takes 1–2 minutes within the task’s time. G02_03 has no separate code-explanation checkpoint; focus there on interpreting the bit pattern and place-value calculation. If K01 is completed, the explanation of the repair serves as its checkpoint.

After teaching the new concept and completing the student experiment, highlight a short fragment from the student’s current code and ask for an explanation in their own words. Wait for the answer before using the **teacher reference**. Follow-up questions should target only missing parts. If the student already demonstrated the idea independently, do not ask again.

Do not count repeating a freshly given solution, a single numeric value, a yes/no answer, a variable name, or a copied line as independent code understanding. Accept simple but conceptually correct English. If the student gets stuck, explain the idea and then use a slightly different thought example; do not require another edit just to check understanding.

Keep execution success and conceptual understanding separate.

## 1. Storage size and type limits

**Source:** `G02_01_types.cpp`. **Goal:** distinguish byte, bit, storage size, and the value range of a type.

### 1.1 – Guided interpretation, student compile and run

Connect to the first practice: previously we stored values; now we inspect the size of the storage and the limits of the type. Explain that `sizeof` reports a size in bytes, while `CHAR_BIT` reports the number of bits in one byte. `sizeof(char) == 1` means one byte, not one bit.

Explain the purpose of `<climits>` and `<limits>`. Break down `std::numeric_limits<int>::max()`: `std` namespace; `numeric_limits<int>` provides characteristics of `int`; `max()` returns the upper limit. Here `lowest()` gives the lower limit for `int`.

Do not ask the student to memorise type sizes before observing them. The reference below assumes an 8-bit byte, 32-bit `int`, and common IEEE 754 floating types. If the student’s correct local result differs, use the local result.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_01_types.cpp -o G02_01
./G02_01
```

The student may instead use RUN. Wait for the result before interpreting it.

**Teacher reference – initial output in a common environment, not a completed experiment:**

```text
Bits in one byte: 8
Size of int in bytes: 4
Size of float in bytes: 4
Size of double in bytes: 8
Lowest int value: -2147483648
Highest int value: 2147483647
Score: 12
Score storage size in bytes: 4
```

### 1.2 – Core experiment: larger value, same type

Current line:

```cpp
int score = 12;
```

Planned line:

```cpp
int score = 1200;
```

Ask: **“Will changing the value from 12 to 1200 change the result of `sizeof(score)`? Why?”** Wait and evaluate the reasoning.

Then ask the student to replace the line, save, compile/run, and report the last two output lines.

**After the answer:** the value becomes 1200, while the storage size associated with the type does not change; in a common environment it remains 4 bytes. Do not ask for byte-to-bit multiplication again if the student already explained it.

### 1.3 – Short type change

Replace this entire output line:

```cpp
std::cout << "Size of int in bytes: " << sizeof(int) << '\n';
```

with:

```cpp
std::cout << "Size of long long in bytes: " << sizeof(long long) << '\n';
```

First ask: **“Why must the label change as well?”** After discussing the answer, the student makes the replacement, saves, compiles/runs, and reports the `long long` size line. The label must match the type actually being queried. A common size is 8 bytes, but do not require that on every environment.

**State to keep:** `score` remains 1200 and the type-size line now queries and labels `long long`.

### Code understanding – storage size versus value limit

Highlight:

```cpp
sizeof(score)
std::numeric_limits<int>::max()
```

Ask: **“What does each expression tell us, and how are their meanings different?”** Wait.

**Teacher reference:** the first reports storage size in bytes; the second reports the largest representable `int` value. Neither reports the current score. Emphasise the type and the local environment rather than memorising one number.

If needed: **“Does `max()` examine the current value of `score`?”**

Thought example after help: suppose `score` were 25; ask which query would change. Keep 1200 in the actual source.

## 2. Initialisation, assignment, and constants

**Source:** `G02_02_initialization.cpp`. **Goal:** understand initial value, later assignment, copying a value, and mutability.

### 2.1 – Guided interpretation, student compile and run

Show `score{}` as value initialisation, then `score = 72;` as later assignment. `fixed_score` receives a copy of the current value and is `const`; `max_score` is `constexpr`, a compile-time-known setting. Every data object in the file has an initial value.

Teach the role these keywords have in this example rather than giving a full language-theory lecture.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_02_initialization.cpp -o G02_02
./G02_02
```

**Teacher reference – initial output:**

```text
Initial score: 0
Current score: 72
Fixed score: 72
Maximum score: 100
```

### 2.2 – Core experiment: trying to modify a constant

Immediately after:

```cpp
const int fixed_score = score;
```

temporarily insert:

```cpp
fixed_score = 80;
```

Ask: **“Will we discover that this is invalid during compilation or only while the program is running?”** Wait.

Clarify that this experiment is compiled only. After a failed compile, do not run an old executable. The student repairs the error by deleting only the invalid assignment.

**After the answer:** compilation fails because an assignment attempts to modify a `const` object. Exact diagnostic wording is compiler-version dependent. Ask for only the first relevant diagnostic.

### 2.3 – Optional: modifying the variable after creating the copy

After the compile error has been repaired, insert after the creation of `fixed_score`:

```cpp
score = 80;
```

First ask which later printed value changes. After the answer, the student tests it.

**After the answer:** current score becomes 80, while the fixed copy remains 72. Keep the working `score = 80;` assignment if this optional experiment is completed.

### 2.4 – Optional: narrowing initialisation

Original:

```cpp
int score{};
```

Temporary version:

```cpp
int score{3.7};
```

Explain the role of braces, then ask what kind of result to expect from compilation. This is ill-formed because list initialisation would narrow `double` to `int`. Do not promise a runtime value of 3 or 4.

The student repairs it to:

```cpp
int score{3};
```

then saves and compiles. If run successfully, the first output line now shows 3; later lines follow any earlier retained modifications. Do not introduce an uninitialised-read experiment.

### Code understanding – value copying and mutability

Highlight:

```cpp
const int fixed_score = score;
```

Ask: **“Explain in your own words what happens in this line.”** Wait.

**Teacher reference:** a new `int` object receives a copy of the value `score` has at that moment; because it is `const`, it cannot later be assigned a new value. This does not create a live link between the variables.

If needed: **“If only `score` changes later, what happens to the copy?”**

Discuss `constexpr int max_score = 100;` separately only if needed. A `const` initializer can in general be determined at runtime; here a `constexpr` variable requires a constant expression. Do not claim that `const` always means runtime.

Thought example after help: `score` is 65 when copied, then later 90. Ask what value the copy keeps.

**End state:** keep the compilable version reached by the student. Do not mark skipped optional experiments as completed.

## 3. Eight bits, two interpretations

**Source:** `G02_03_bit_patterns.cpp`. **Goal:** distinguish `-1` from `-127` in an 8-bit two’s-complement model.

### 3.1 – Guided interpretation, student compile and run

The eight ordinary `int` variables containing 0 or 1 **illustrate** eight bits. Their real storage size is not one bit, and the program is not inspecting raw memory bytes. Without a sign, the top bit has place value +128; in an 8-bit two’s-complement interpretation, it contributes -128. The lower seven bits are calculated once and stored under a meaningful name.

The values 64, 32, ..., 1 are binary place values, not arbitrary task parameters. Do not introduce arrays, loops, or bitwise operators here. The initial bit pattern is `01111111`, positive under both interpretations.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_03_bit_patterns.cpp -o G02_03
./G02_03
```

**Teacher reference – initial output:**

```text
Bit pattern: 01111111
Unsigned interpretation: 127
Two's complement interpretation: 127
```

### 3.2 – Core experiment: change only the leftmost bit

Original:

```cpp
int bit7 = 0;
```

New:

```cpp
int bit7 = 1;
```

Ask: **“What signed value will this pattern represent in two’s complement?”** Wait, then ask the student to edit and run.

**After the answer:** pattern `11111111`; unsigned interpretation `128 + 127 = 255`; signed interpretation `-128 + 127 = -1`. If the student says -127, correct the sign-and-magnitude misconception: two’s complement does not simply place a minus sign in front of the remaining 127.

### 3.3 – Core experiment: the pattern for -127

Replace the eight-bit setup block with:

```cpp
int bit7 = 1;
int bit6 = 0;
int bit5 = 0;
int bit4 = 0;
int bit3 = 0;
int bit2 = 0;
int bit1 = 0;
int bit0 = 1;
```

Ask: **“What is the two’s-complement sum now?”** Wait, then test.

**After the answer:** pattern `10000001`; unsigned 129; signed `-128 + 1 = -127`. Treat replacing the eight-line block as one coherent bit-pattern change rather than eight separate compile cycles.

**State to keep:** `10000001`. Optional thought question: interpret `10000000` (unsigned 128, signed -128). Never ask the student to place anything other than 0 or 1 in the bit variables.

## 4. Division and where conversion happens

**Source:** `G02_04_division.cpp`. **Goal:** distinguish conversion before an operation from conversion after the operation.

### 4.1 – Guided interpretation, student compile and run

Walk through all three formulas. Two `int` operands perform integer division; the result is only converted to `double` afterwards. `static_cast<double>(total_points)` creates a `double` value before division without changing the original variable. A cast around the already completed integer division only converts the truncated result.

The names `first_average`, `second_average`, and `third_average` identify the three variants being compared. `std::cout` uses its default floating formatting here, so a `double` value such as 3.0 is printed as `3`.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_04_division.cpp -o G02_04
./G02_04
```

**Teacher reference – initial output:**

```text
First calculation: 3
Second calculation: 3.5
Third calculation: 3
```

### 4.2 – Core experiment: new data

Original:

```cpp
int total_points = 7;
```

New:

```cpp
int total_points = 9;
```

Ask: **“Which calculation keeps the fractional part, and what value will it produce?”** Wait, then ask the student to test it.

**After the answer:** the second calculation gives 4.5. The first and third are `double` values equal to 4.0, printed as `4` with the default format. The reason is the type of the operation, not the variable name.

### 4.3 – Core experiment: repair one line

Keep `total_points = 9`. Ask the student to make the first calculation compute a real average too. If necessary, show the current line:

```cpp
const double first_average = total_points / student_count;
```

Only after the student has tried to reason it out, offer this replacement:

```cpp
const double first_average = static_cast<double>(total_points) / student_count;
```

After saving and running, the first and second calculations should both be 4.5; the third remains 4.

**State to keep:** `total_points` is 9 and `first_average` uses conversion before the division.

### 4.4 – Optional: truncation with a negative value

Before `return`, the student may insert:

```cpp
const double measurement_value = -3.9;
std::cout << "Converted to int: " << static_cast<int>(measurement_value) << '\n';
```

First explain truncation toward zero using a different number, then ask for a prediction. The result here is -3, not -4. Keep the two extra lines if this optional experiment is completed. Never set `student_count` to zero as an error experiment.

### Code understanding – order of operations in the division

Highlight the current corrected formula:

```cpp
const double first_average = static_cast<double>(total_points) / student_count;
```

Ask: **“Walk me through how the program evaluates this expression.”** Wait.

**Teacher reference:** `total_points` is converted to a `double` value; the other operand is converted as needed for the division; floating-point division is performed; the result initialises the `const double`. The type of the original `total_points` variable itself is unchanged. A numeric answer such as 4.5 is not enough by itself.

If needed: **“What would change if the cast surrounded the entire division instead?”**

Thought example after help: 11 points and 2 students; ask the student to explain the evaluation order and result without editing the file.

## 5. Range limits and larger calculations

**Source:** `G02_05_ranges.cpp`. **Goal:** understand unsigned wraparound and choosing a sufficiently wide type for an operation.

### 5.1 – Guided interpretation, student compile and run

First explain only the counter part. `std::numeric_limits<unsigned int>` selects the type being examined; `max()` gives its maximum value. That value initialises `counter`. The named constant `increment` identifies the step used in the addition. `1u` has the same numeric value as 1 but is an `unsigned int` literal; `u` is a type suffix, not a unit.

Unsigned wraparound is defined by the language. The first printed maximum may differ with the implementation.

Then explain the multiplication. Mathematically 50000 × 50000 = 2,500,000,000. Because one operand is converted to `long long` **before** multiplication, the multiplication is carried out in a sufficiently wide type. `total_price` is `const` because the calculated result is not changed later.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_05_ranges.cpp -o G02_05
./G02_05
```

**Teacher reference – common initial output:**

```text
Counter before: 4294967295
Counter after: 0
Highest int value: 2147483647
Total price: 2500000000
```

### 5.2 – Core experiment: a different increment

Original:

```cpp
constexpr unsigned int increment = 1u;
```

New:

```cpp
constexpr unsigned int increment = 2u;
```

Ask: **“What will the counter contain after the addition?”** Wait, then test.

**After the answer:** 1. Starting from the maximum, the next value is 0 and then 1. The result 1 does not depend on the width of `unsigned int`. Keep `increment = 2u`.

### 5.3 – Core experiment: type of the multiplication

Original:

```cpp
int quantity = 50000;
```

New:

```cpp
int quantity = 60000;
```

Ask: **“Does the mathematical result fit in the machine’s `int`, and why can this program still calculate it correctly?”** Use the upper limit actually observed on the student’s machine.

**After the answer:** the mathematical result is 3,000,000,000; it does not fit in a 32-bit `int`, but the multiplication takes place as `long long` because conversion happens before the operation. Do not remove the correct cast in the core task.

**State to keep:** `quantity = 60000`, `increment = 2u`, and the pre-operation cast remains.

### Code understanding – counter and large multiplication

Use two short questions because the task contains two independent ideas.

First highlight:

```cpp
unsigned int counter = std::numeric_limits<unsigned int>::max();
counter = counter + increment;
```

Ask: **“Where does `counter` get its starting value, and how does the next line change it?”** Wait.

**Teacher reference:** `numeric_limits<unsigned int>::max()` provides the upper limit for that type. The second line adds the increment to the old value and stores the result back. Unsigned wraparound is defined. With the current `2u`, the result is 1.

If needed: **“What does the `u` mean in `2u`?”** It makes the integer literal unsigned.

Then, after the multiplication experiment, highlight:

```cpp
const long long total_price = static_cast<long long>(quantity) * unit_price;
```

Ask: **“Why can this line calculate the current large product correctly?”** Wait.

**Teacher reference:** conversion occurs before multiplication, so the other operand is converted as part of the usual arithmetic conversions and the multiplication is performed as `long long`. The destination type alone would not protect an already-overflowed `int` multiplication.

If needed: **“In what type would the multiplication occur without the cast?”**

Do not write or run the incorrect version here; that belongs only to optional K01.

## 6. Floating-point precision

**Source:** `G02_06_precision.cpp`. **Goal:** understand approximate storage and significant digits.

### 6.1 – Guided interpretation, student compile and run

Work in two parts. First observe storage of `0.1f` and `0.1`: the `f` suffix makes a `float` literal, while an unsuffixed floating literal is `double`. `setprecision(17)` here requests significant digits in the default floating format; it does not create more stored precision.

In the usual binary formats, decimal 0.1 has a repeating binary expansion, so it is stored as a rounded approximation. The student does not need to calculate or memorise the long decimal output in advance.

The reference values assume common IEEE 754 binary32/binary64 formats. If the student gets a different valid result, first check the literal, type, formatting state, and environment.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_06_precision.cpp -o G02_06
./G02_06
```

**Teacher reference – common initial output:**

```text
float: 0.10000000149011612
double: 0.10000000000000001
Short output: 1.23457
Medium output: 1.234568
Long output: 1.23456788
```

### 6.2 – Core experiment: an exactly representable fraction

Original:

```cpp
float float_measurement = 0.1f;
double double_measurement = 0.1;
```

New:

```cpp
float float_measurement = 0.5f;
double double_measurement = 0.5;
```

Using the relationship `0.5 = 1/2 = 0.1₂`, ask: **“How would you justify whether 0.5 can be stored exactly in these types?”** Wait. Do not state the answer before the prediction. If needed, teach the binary-fraction connection and mark that as assisted learning.

After the edit and run, the first two lines print `0.5`. The final three lines are unchanged because they use a different variable. Requesting 17 significant digits does not force trailing zeros in the default format.

Keep `0.5f` and `0.5` in the source.

### 6.3 – Code understanding: storage versus printed digits

Highlight:

```cpp
float float_measurement = 0.5f;
double double_measurement = 0.5;
std::cout << std::setprecision(detailed_digits);
```

Ask: **“Which lines determine the storage type, and which line changes how values are printed? Explain the difference.”** Wait.

**Teacher reference:** the declarations create `float` and `double` variables. The `f` suffix makes the literal itself a `float`; without it, the literal is `double`. `setprecision` changes the output stream. Without `fixed`, it requests significant digits. Setting `detailed_digits` to 17 does not give a `float` 17 significant decimal digits of stored precision.

If needed: **“If we only increase `setprecision`, what happens to data already stored in the variable?”**

Thought example: `double double_measurement = 0.5f;` — ask for the type of the variable and distinguish it from the type of the literal.

Then connect the final three outputs to the same idea. `detailed_measurement` is initialised from `1.23456789f`; in common binary32, printing 9 significant digits gives about `1.23456788`, reflecting the stored approximation. Leading zeros are not significant digits. `digits10` for binary32 is commonly 6, meaning six decimal digits can be preserved reliably through decimal→binary→decimal conversion; a seventh digit is not guaranteed for every value.

### 6.4 – Optional: adding one to a large float may be lost

Before `return`, the student may insert:

```cpp
const float large_value = 16777216.0f;
constexpr float increment = 1.0f;
const float increased_value = large_value + increment;
std::cout << "Large value increased: " << std::setprecision(detailed_digits)
          << increased_value << '\n';
```

First explain that spacing between adjacent representable floating values grows with magnitude, then ask for an observation. With common binary32 and round-to-nearest, the printed result remains 16777216. This is a **precision** limitation, not a finite-range limit.

Ask: **“Why is it not enough that the number is still inside the finite range of `float`?”** Keep the working optional block if completed.

## 7. Output formatting

**Source:** `G02_07_formatting.cpp`. **Goal:** separate stored value from output formatting.

### 7.1 – Guided interpretation, student compile and run

In the previous task, `setprecision` in the default floating format controlled significant digits. Here, because `fixed` is active, `setprecision` controls the number of digits after the decimal point.

Walk through the actual output chain: `std::cout` is the output stream; `std::fixed` sets fixed-point formatting; `std::setprecision(short_decimal_places)` requests two digits after the decimal point; `quotient` is the data; `\n` starts a new line. The manipulators do not print their own names or the number 2. The `<<` operations can be chained because they keep returning the stream. `fixed` remains active for the following output. The stored value of `quotient` does not change between lines.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_07_formatting.cpp -o G02_07
./G02_07
```

**Teacher reference – initial output:**

```text
Short output: 0.33
Detailed output: 0.3333333333
Storage size in bytes: 8
```

### 7.2 – Core experiment: more displayed decimal places

Original:

```cpp
constexpr int short_decimal_places = 2;
```

New:

```cpp
constexpr int short_decimal_places = 6;
```

Ask: **“Does the stored value or storage size of `quotient` change, or only its representation on output?”** Wait, then test.

**After the answer:** only the representation changes. The first line becomes `0.333333`, the second remains `0.3333333333`, and the storage size remains whatever was observed on the local environment.

### 7.3 – Optional: same formatting with a larger value

Keep six decimal places. Change only:

```cpp
constexpr double numerator = 1.0;
```

to:

```cpp
constexpr double numerator = 22.0;
```

Before editing, ask whether “six” under `fixed` means six significant digits total or six digits after the decimal point. Wait for the answer, then test.

**Teacher reference:** first line `7.333333`; in common binary64, second line `7.3333333333`. Here the stored quotient changes because the numerator changes; this is different from the previous experiment, which changed only formatting.

### Code understanding – the output chain

Highlight the current output line:

```cpp
std::cout << "Short output: " << std::fixed
          << std::setprecision(short_decimal_places) << quotient << '\n';
```

Ask: **“Explain from left to right what each part does.”** Wait.

**Teacher reference:** `cout` is the stream; the string is the label; `fixed` sets the formatting mode; `setprecision` sets decimal places in that mode; `quotient` is the value being displayed; `\n` adds a newline. The manipulators do not change the stored quotient. The stream settings persist into later output.

If needed: **“Why does `fixed` affect the next output line too?”**

Thought example after help: imagine three decimal places; ask which setting changes and whether the stored quotient changes.

**State to keep:** `short_decimal_places = 6`; `numerator` remains 1.0 after the core path, or 22.0 if the optional experiment was completed.

## 8. Comparison using an absolute tolerance

**Source:** `G02_08_tolerance.cpp`. **Goal:** approximate comparison tied to the problem and unit.

### 8.1 – Guided interpretation, student compile and run

The variable names explicitly include metres because the meaning of `0.001` depends on the unit. In this example, 0.001 metres is one millimetre. `measured_length_m` is mutable because it is changed during experiments; `expected_length_m` and `allowed_deviation_m` are named task rules.

Explain the sequence: subtraction → `std::abs` → comparison. `<cmath>` provides the floating-point absolute-value overload. `within_tolerance` is a `bool`; `std::boolalpha` prints `true`/`false` instead of `1`/`0`. The chosen tolerance is a domain rule for this example, not a universal machine epsilon.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_08_tolerance.cpp -o G02_08
./G02_08
```

**Teacher reference – initial output:**

```text
Absolute deviation in metres: 0.0005
Within tolerance: true
```

### 8.2 – Core experiment: larger deviation

Original:

```cpp
double measured_length_m = 1.2345;
```

New:

```cpp
double measured_length_m = 1.2360;
```

Ask: **“Will this measurement be accepted by the rule in the program?”** Wait, then test.

**After the answer:** no. The printed absolute deviation is `0.0020` metres and `within_tolerance` is `false`. Do not change the threshold or formatting during this experiment.

**If the output differs, stop here.** With expected value 1.2340 and measured value 1.2360, the mathematical absolute deviation is 0.0020, not 0.0015. A final `false` value does not validate an incorrect intermediate calculation. Do not explain a wrong difference as ordinary rounding. Check the current expected value, measured value, tolerance, and formula, or ask the student to paste those lines. If the source is correct, ask them to verify saving and the most recent successful compile/run. The student performs any correction and repeats the test.

Do not continue to the opposite-direction deviation until this is resolved.

### 8.3 – Core experiment: direction of the deviation

Now change the measurement to:

```cpp
double measured_length_m = 1.2320;
```

Ask: **“Does acceptance change just because the measurement is now smaller by the same amount?”** Wait, then test.

**After the answer:** no. The printed absolute deviation is again `0.0020` and the result is `false`. The raw difference is negative, but the absolute value is positive.

**State to keep:** `measured_length_m = 1.2320`; threshold and formatting unchanged. The strict `<` condition would reject a mathematical deviation exactly equal to the threshold. Avoid boundary-valued core examples and do not introduce NaN or infinity here. Relative tolerance for very different scales is a later topic.

### Code understanding – from deviation to a Boolean result

After source and output are consistent, highlight:

```cpp
const double absolute_deviation_m = std::abs(measured_length_m - expected_length_m);
const bool within_tolerance = absolute_deviation_m < allowed_deviation_m;
```

Ask: **“How do these two lines get from the two length values to a true or false result?”** Wait.

**Teacher reference:** subtract to get a signed difference, use absolute value to get its magnitude regardless of direction, then compare that magnitude with the allowed deviation. The deviation is still measured in metres; `within_tolerance` is a Boolean. `<` is strict. A bare answer of `false` does not explain the two lines.

If needed: **“Why do we need the absolute value when the measurement is smaller than expected?”**

Thought example after help: expected 2.0 m, measured 1.5 m, tolerance 0.25 m; ask the student to walk through both lines. These values are chosen to check reasoning rather than floating-point rounding.

## 9. Integrating the ideas: scores

**Source:** `G02_09_scores.cpp`. **Goal:** combine type choice, calculation repair, and output formatting.

### 9.1 – Guided interpretation, student compile and run

This is a complete, compilable program, but the marked calculation contains a deliberate logical error. Readable formatting and meaningful names do not by themselves guarantee correctness.

The program works with two integer scores between 0 and 100. First ask the student to describe the role of the two inputs in their own words, then ask why their average may be fractional. In a separate question, ask which type is suitable for individual scores and which type is suitable for the average. Evaluate these separately; do not immediately give the correction.

The initial output is only a run reference. Compare it with the manually calculated average and use the discrepancy to continue.

Terminal option:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic G02_09_scores.cpp -o G02_09
./G02_09
```

**Teacher reference – initial output:**

```text
Average score: 77.0
Average percentage: 77.0%
```

### 9.2 – Core task: independently repair the calculation

After observing the discrepancy, ask: **“How would you repair the average calculation, and why would your change prevent the fractional part from being lost?”** Wait.

Do not first point to the exact faulty line and ask which line is wrong. If you have already highlighted it, ask the student to explain its behaviour and the correction. The student should not rewrite the whole program; first they propose a change.

Give help gradually, only when needed:
1. Point to the `average_score` formula and ask for the operand types.
2. Remind them that the conversion must happen **before** the division.
3. Finally, show the replacement and mark it as an assisted solution.

Original:

```cpp
const double average_score = total_points / student_count;
```

Corrected:

```cpp
const double average_score = static_cast<double>(total_points) / student_count;
```

Converting the denominator before division is also acceptable. Merely renaming the integer variables or declaring the destination as `double` again is not a repair. Accept another correct solution if the student can explain it.

After saving and running, the output should be:

```text
Average score: 77.5
Average percentage: 77.5%
```

After the successful repair, the student should remove the comment that labels the calculation as an assigned debugging error, because it would now be misleading. Keep the corrected formula.

### 9.3 – Core task: display two decimal places

Ask: **“How would you change the program so the average is displayed with two digits after the decimal point?”** Do not point to the setting before the student answers.

If needed, show this replacement:

```cpp
constexpr int displayed_decimal_places = 1;
```

to:

```cpp
constexpr int displayed_decimal_places = 2;
```

After saving and running, `77.50` and `77.50%` appear. The stored average has not become more precise merely because more digits are printed. Keep the new setting.

### 9.4 – Core experiment: new, unsolved data

In the corrected program, set:

```cpp
int first_score = 73;
int second_score = 88;
```

First ask for the expected average and a short explanation. If the student answers only “80.5%”, clarify whether they mean the score average or percentage. Only then ask them to edit, save, and compile/run.

**After the answer:** with a maximum score of 100, both displayed values are `80.50` and `80.50%`.

If the tutor accidentally gave this prediction away, use a different new pair or mark the attempt as assisted; for example 90 and 95 gives 92.50 and 92.50%.

### 9.5 – Code understanding: average score and percentage

Highlight the corrected calculations:

```cpp
const double average_score = static_cast<double>(total_points) / student_count;
const double average_percentage = average_score / max_score * percentage_multiplier;
```

Ask: **“Explain what these two lines calculate and what the two results mean.”** Wait.

**Teacher reference:** the first computes an average score from the total, with conversion before division. The second relates the average score to the maximum and multiplies by 100. Score and percentage are different meanings; the numbers happen to be equal while the maximum is 100. `max_score` and `percentage_multiplier` have different roles. `const` prevents later reassignment of the calculated results.

If the student used another correct average formula, ask them to explain their actual line.

If needed: **“Which result would change if the same assessment allowed a different maximum number of points?”**

Thought example after help: 60 points with a maximum of 120; ask the student to explain the second formula without giving 50% in advance.

Optional actual experiment with the corrected 73/88 scores: change `max_score` to 120. Ask for prediction and reasoning first, then let the student edit and run. Teacher reference: average score remains `80.50`; percentage becomes about `67.08%` in the common environment. Keep the modification if this optional experiment is completed.

**Final state to preserve:** corrected average formula, `displayed_decimal_places = 2`, `first_score = 73`, `second_score = 88`, and no misleading debugging comment. `max_score` remains 100 on the core route or 120 after the optional experiment.

The repaired source is the student’s finished result; do not request extra edits merely to close the lesson.

## K01 – Optional controlled overflow demonstration

**Source:** `G02_K01_overflow.cpp`. This is not part of the core route. Ask the student once whether they want the optional demonstration. If not, mark it skipped and close the practice.

The provided source is correct and compilable. Initial output:

```text
Total price: 2500000000
```

The only intentional incorrect change in this demonstration is removing the pre-operation cast.

### K01.1 – Preconditions and correct baseline run

Use Task 1 to verify that the environment’s upper `int` limit is 2147483647. If it is different, do not run this exact demonstration under unchanged assumptions.

Explain in advance: for the incorrect version, we do **not** predict a specific numeric stdout value. We observe runtime detection of undefined signed overflow.

Ask the student to compile the correct program with runtime checking:

```bash
g++ -std=c++20 -Wall -Wextra -pedantic -O0 -fsanitize=undefined -fno-sanitize-recover=undefined G02_K01_overflow.cpp -o G02_K01_checked
```

Then, only after successful compilation:

```bash
./G02_K01_checked
```

`-fsanitize=undefined` adds runtime checks for undefined behaviour; `-fno-sanitize-recover=undefined` stops on a detected issue. `-O0` disables normal optimisation but does not make invalid code valid.

If the sanitizer option or required runtime library is unavailable, stop the optional demonstration. Do not run the incorrect version without checking and do not turn the lesson into an environment-installation detour.

### K01.2 – Recognising the incorrect multiplication

Correct line:

```cpp
const long long total_price = static_cast<long long>(quantity) * unit_price;
```

Temporary, intentionally incorrect line:

```cpp
const long long total_price = quantity * unit_price;
```

Ask: **“Why does the `long long` destination variable not protect this calculation by itself?”** Wait.

**After the answer:** the two `int` operands are multiplied as `int`; signed overflow can occur before the result is assigned to `long long`. This is undefined behaviour, so do not promise wraparound or a specific numeric result.

The student makes the change, saves, recompiles using the **same full checked command**, and runs only after successful compilation. Ask for the relevant sanitizer message and wait. A diagnostic typically mentions signed integer overflow and the process terminates with an error. Exact wording, path, and line number are environment-dependent. The sanitizer message is not normal `std::cout` output.

Fix the overflow in the operation rather than disabling the warning.

### K01.3 – Repairing the overflow error

Ask the student to restore the pre-operation `static_cast`, save, compile with the same checked command, and run if compilation succeeds. Wait for the report: expected normal result again is `2500000000`, without the sanitizer error.

Only then consider the demonstration complete. Keep the final source correct.

### Code understanding – explaining the K01 repair

After the successful repair, show the actual correct multiplication line and ask: **“Explain how this repair prevents the previous overflow.”** Wait.

The key idea is conversion before the operation and therefore the type in which multiplication occurs, not suppressing a diagnostic. If the student already explained this independently in K01.2, count that and do not repeat it. After help, use a thought example where the other operand is converted before multiplication; do not request another incorrect run.

## Closing – 10 minutes

Start with a short connected review, then ask only a few questions targeted at actual uncertainty. Do not present the entire list at once or turn it into a new compulsory exam. Understanding already demonstrated in the tasks does not need to be proved again.

Possible questions:
- What does `sizeof` measure, and how can we derive a number of bits from it?
- Why is `11111111` equal to -1 and `10000001` equal to -127 in the 8-bit two’s-complement model?
- Why does the location of a conversion matter in division or multiplication?
- What is the difference between a range limit and a precision limit?
- Why does printing more decimal places not make the stored variable more precise?
- What role do absolute value and the unit play in a tolerance comparison?
- In the student’s repaired program, which name or constant makes the code easier to understand?

The closing should state which core tasks were actually completed, which ideas were applied independently, which required help, and where to continue next time. Treat technical obstacles separately from conceptual uncertainty. The repaired Task 9 source is the student’s completed result.

The next theory topics are compound conditions and control structures. Do not start an unplanned new task here.

Clearly state: **“The required C++ Practice 2 is complete.”** There is no homework.
