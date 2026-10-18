# CPP_07 project – Analyzing valid measurements

Develop a single file: **P07_measurements.cpp**. The starter provides Date and
Measurement types and six records. You implement the processing functions,
their prototypes, and the calls.

| ID | Value | Valid? | Date |
|---|---:|---|---|
| 101 | 18.5 | yes | 2026-10-17 |
| 102 | 26.0 | no | 2026-10-17 |
| 103 | 21.0 | yes | 2026-10-17 |
| 104 | -2.0 | yes | 2026-10-17 |
| 105 | 30.5 | yes | 2026-10-17 |
| 106 | 21.0 | yes | 2026-10-17 |

A negative value can be a valid temperature. Read validity from its separate
flag; do not infer it from the sign or threshold.

## Workflow and organization

Before each step, Inno explains a short, complete analogous example. Then you
apply the idea. Work on only the current part at a time.
File order: types → prototypes → main → function definitions.
Main coordinates the program; separate functions perform individual operations.
Keep the threshold and array size local to main and pass them where needed.

## P1 – Print one measurement with its nested date

**Example:** M6. Suggested time: 7 minutes.

The `recorded` member contains a complete Date value. Two consecutive dots
select members at two levels. Write a void function named `printMeasurement`.
It takes one measurement by value and prints its ID, value, validity and all
three date parts. Call it with a selected array element. No input reading is needed.

Check for the first record: 101, 18.5, true, 2026-10-17.
Formatting is flexible; Boolean `1` and textual “yes” are both acceptable.

## P2 – Print all records

**Example:** M7. Suggested time: 6 minutes.

Implement `printMeasurements`, taking a pointer to readable measurements and
an element count. Loop over the array and call P1's printing function for each
element. Main calls this function to display the full dataset.

Check: six records in their original order, including the invalid one.
The const-qualified pointer prevents changing elements through it. A pointer
does not supply the array size; pass the size separately.

## P3 – Count valid measurements

**Example:** M8, but only the validity condition is needed here.
Suggested time: 6 minutes.

Implement `countValid`, taking readable measurements and an element count.
Return the number of valid records. Exclude ID 102, but include the valid record with value -2.0.

Check: 5.

## P4 – Average the valid values

**Example:** M9; reuse P3 as well. Suggested time: 9 minutes.

Implement `averageValid` returning double. Sum only valid values and divide
by the valid count. Obtain that count by calling `countValid`; do not duplicate
its counting logic.

Precondition: at least one measurement is valid. Main must check this before
calling the average function. If no measurements are valid, do not call it;
print a clear message instead. Avoid division by zero and invented average values.

Check: valid values sum to 89 and average to 17.8.
As a test, make all validity flags false and check the no-valid-data branch.
Compile again. Restore the original flags before continuing with the original dataset.

## P5 – Valid AND strictly above a threshold

**Example:** M8; explain only the newly relevant difference again.
Suggested time: 7 minutes.

Implement `countAboveThreshold`, taking measurements, an element count and a
double threshold. A record counts only if it is valid AND its value is
**strictly greater** than the threshold. Call the same function with both 20 and 21.

Check: 3 above 20, 1 above 21. Values equal to the threshold do not count.
The invalid 26.0 record counts in neither case.

## P6 – Modify an original record through a pointer

**Example:** M3. Suggested time: 10 minutes.

Implement the void function `increaseValue`, taking a pointer to a modifiable
measurement and a double increment. Increase only that measurement's value.
Its ID, validity and date must not change.

Precondition: the pointer points to a live measurement. Main passes the first
array element's address and an increment of 2.0. Do not create a second array:
observe a change in the original record. Call the existing printing, averaging
and counting functions again.

Check: first value 20.5; valid count 5; average 18.2;
valid count above 20 is 4; valid count above 21 remains 1.
The first record's ID and date are unchanged.

## Project wrap-up

Briefly explain which function receives a copy, which reads the array, and
which modifies an original record. Why is validity separate data?
This is an explanation of behavior, not another program or output-prediction exercise.
