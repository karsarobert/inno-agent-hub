# CPP_04 – Lesson Instructions

## Overview

Time frame: **3 × 45 minutes**.

- Block 1: arrays – `G04_01`…`G04_05`
- Block 2: pointer basics – `G04_06`…`G04_08`
- Block 3: relationship between arrays and pointers – `G04_09`…`G04_10`, final test

Every file contains a **basic Task A** and a **more applied Task B**. The starters provide only the necessary data and a minimal program skeleton. The student must write the indexing expression, `for` loop, `if` condition, or pointer expression that is part of the learning target.

### Important tutor rule

Give the task first in **natural language**. The exact syntax below is for your checking purposes; **do not give it away immediately**. When the student gets stuck, use the help ladder: conceptual hint → analogous one-line example → partial structure → full solution only as a last resort.

---

## G04_01 – First array: index and value

**File:** `G04_01_array_basics.cpp`

### Task A – say it like this

“Print the first and the third element of the array on separate lines. Write the complete output statements yourself.”

Do not give the indices immediately. If the student gets stuck, first ask: “What index does a C++ array start with?”

### Task B – say it like this

“Print the last element of the array so that your solution calculates the last valid index from the `arraySize` variable. Do not write a specific final index directly.”

### Tutor check – do not give this away immediately

- first element: `numbers[0]`
- third element: `numbers[2]`
- last element: `numbers[arraySize - 1]`
- expected values: 12, 18, 9

Do not ask for an output prediction before running. Do not intentionally run out-of-bounds access.

---

## G04_02 – Modifying an array element

**File:** `G04_02_array_modification.cpp`

### Task A

“Print the current value of the second element, change it to 20, then print it again.”

The student chooses the correct index and writes the assignment.

### Task B

“Print the value of the third element, then increase it by 5 using its previous value. Print it again afterwards.”

### Tutor check

- second element: index 1, final value 20
- third element: index 2, 18 → 23

Understanding question: “What changed: the index, or the value stored at that index?”

---

## G04_03 – Traversing an array with a `for` loop

**File:** `G04_03_array_traversal.cpp`

### Task A

“Write a complete `for` loop that moves from the beginning of the array to the end and prints every element.”

**Do not dictate the loop header immediately.** If the student gets stuck, ask in this order:

1. What is the first valid index?
2. What is the last valid index?
3. What condition keeps us safely inside the array?
4. How do we move to the next index?

### Task B

“Write a second loop. This time, print the index and its corresponding value on every line, for example `2 -> 18`.”

### Tutor check

The correct loop logic starts at 0, continues while the index is smaller than the size, and increases the index by one. Do not provide the full `for (...)` line unless help is genuinely needed.

Short check: why is it dangerous if the loop goes one step beyond the last valid index?

---

## G04_04 – Summation and average

**File:** `G04_04_summation.cpp`

### Task A

“The `sum` variable already starts at 0. Write a **complete `for` loop** that traverses the array and adds every element to the sum. After the loop, print the result.”

The starter intentionally contains neither a loop header nor a ready-made summation statement.

### Task B

“Using the completed sum and the array size, calculate the average in a way that can preserve a fractional result. Print the average.”

### Tutor check

- expected sum: 50
- expected average: 10.0
- if needed, remind the student about floating-point division; do not give the exact `static_cast` line immediately

Do not ask for a preliminary arithmetic prediction.

---

## G04_05 – Conditional counting with two conditions

**File:** `G04_05_conditional_counting.cpp`

### Task A

“Write a complete array traversal loop. Inside the loop, use a condition to count how many elements are greater than 10. Print the count at the end.”

Do not provide a ready-made loop or `if` condition at first.

### Task B

“During the same traversal, maintain a second count as well: how many elements are even? Print this count at the end too.”

### Tutor check

- elements greater than 10: 2
- even elements: 3 (`12`, `18`, `4`)

At the end of Block 1, briefly summarize: index, traversal, summation, conditional counting.

---

## G04_06 – Value, address, and the first pointer

**File:** `G04_06_address_and_pointer.cpp`

### Required explanation

Use these four questions:

1. what is the value;
2. where is the value;
3. what does the pointer store;
4. what do we get when we dereference it.

### Task A – say it like this

“Print the value of `number` and its memory address. Then create a pointer to an `int` that stores this address, and print the address stored in the pointer as well.”

Do not immediately provide the complete line using `&` or `int*`. Help with a conceptual question first.

### Task B

“Redirect the existing pointer to `otherNumber`. Print the address of `otherNumber` and the new value stored in the pointer.”

### Tutor check – do not give this away immediately

Conceptually, the address-of operator gives us an address, and an `int*` pointer can store it. The pointer can later be redirected to the address of another `int` object.

Do not ask the student to predict a specific hexadecimal address.

---

## G04_07 – Dereferencing and modification

**File:** `G04_07_dereferencing.cpp`

### Task A

“Create a pointer that points to `number`. Read the value through the pointer, then change it to 99 through the pointer. Finally, print the `number` variable to verify the modification.”

Ask exactly one short prediction immediately before the first modification through the pointer: “Which value do you think will change?”

Only name the operation **dereferencing** after the concrete example.

### Task B

“Increase the current value by another 10 through the pointer. Do not modify `number` directly.”

### Tutor check

Expected final value of `number`: 109.

If the student describes the pointer instead of dereferencing, clarify that dereferencing means accessing the object at the stored address.

---

## G04_08 – `nullptr` and redirecting a pointer

**File:** `G04_08_nullptr.cpp`

The starter intentionally shows the new `nullptr` initial value, but the student writes the safe check.

### Task A

“Check whether the pointer points to a valid object, and read the pointed-to value only when it is safe. Then make the pointer point to `number` and perform the check again.”

Before the first check, ask one brief prediction: which branch will execute?

### Task B

“Redirect the same pointer to `otherNumber`, then use the same safe pattern to read the value.”

### Tutor check

- first state: `nullptr`, do not dereference
- second state: 25
- third state: 40

Never ask the student to dereference `nullptr`.

---

## G04_09 – Relationship between an array and a pointer

**File:** `G04_09_array_and_pointer.cpp`

### Task A – say it like this

“First print the address of the first element of the array. In a second output statement, put only the array name on the right-hand side of `std::cout`. Then create a pointer that points to the first element and print the address stored in it. Compare the three results.”

Make the phrase “only the array name” explicit; this wording previously caused confusion.

### Task B

“Now print the address of the second element in two ways: once directly from the element, and once by moving one element forward from the pointer to the first element.”

### Tutor check – do not give this away immediately

- the two forms for the first element's address ultimately refer to the same location
- in this expression, the array name converts to a pointer value referring to the first element
- moving one element forward from the pointer gives the address of the next `int` element

Explain clearly: the array is not a pointer.

---

## G04_10 – Indexing, pointer traversal, and summation

**File:** `G04_10_pointer_traversal.cpp`

### Task A

“Create a pointer to the first element of the array. Print the element at index 2 (the third element) in two ways: once using array indexing and once starting from the pointer. Then write a complete `for` loop that traverses and prints the array through the pointer. Finally, use the pointer to change the element at index 2 to 100, and verify it with array indexing.”

Before comparing the two access methods, ask one brief prediction: should they produce the same value?

**Do not provide immediately** either the pointer-arithmetic expression or the `for` header.

### Task B

“Write another complete loop that accesses the already modified array through the pointer and calculates the sum of its elements.”

### Tutor check

- element at index 2 was originally 30
- after modification: 100
- expected sum: 220

For simple array traversal, indexing is often more readable; the goal is not to write everything with pointers.

---

# Required final test

After Task B of the 10th file, say:

**“You have completed the required programming tasks for CPP_04. Now we will do the short final test.”**

Ask the questions from `FINAL_TEST.md` **unchanged, one at a time**. Do not generate replacement questions.

## T1 – Multiple-choice final test

Correct answers:

1. C
2. B
3. D
4. A
5. C
6. B

Scoring: 0–6 correct. Do not convert this to a percentage-based knowledge level.

Short explanations:

1. Five elements have indices `0, 1, 2, 3, 4`, so the last valid index is `4`.
2. `&number` gives the address of the memory location of `number`.
3. In this example, the `int*` pointer stores the address of `number`.
4. `*pointer` dereferences the pointer and accesses the `int` object at the stored address.
5. We dereference only a valid, non-`nullptr` pointer.
6. `pointer = numbers` makes the pointer point to the first element, but the array and the pointer remain different concepts.

## T2 – Output-prediction final test

For each question, show the corresponding complete program from `FINAL_TEST.md` and wait for the student's answer.

Solutions:

1. `7 12`
   - The pointer first points to `a`, so `a` becomes 7.
   - Then the pointer is redirected to `b`, and `b` is increased by 3.

2. `30`
   - `pointer + 2` points to the element at index 2, the third element.
   - Dereferencing produces its value.

3. `42`
   - `*(pointer + 1) = 42` modifies the array element at index 1.
   - This is the same element as `numbers[1]`.

4. `20`
   - The loop adds the values through the pointer: `2 + 4 + 6 + 8`.

5. Two lines:
   - `empty`
   - `8`
   In the first check, the pointer is `nullptr`, so the `else` branch runs. Then the pointer is set to the address of `number`, so the second check safely prints 8.

6. `1 20 3 40`
   - The loop modifies only the even elements through the pointer.
   - 2 becomes 20 and 4 becomes 40; the odd elements remain unchanged.

Scoring: 0–6 correct. Do not count minor formatting differences as errors if the values, order, and execution logic are correct.

After T2 question 6, report:

- T1 result: `x/6`
- T2 result: `y/6`

Then say:

**“The required CPP_04 practice is now complete.”**

---

# Adaptive complex extra task – K04_01

**File:** `K04_01_extra.cpp`

Use the `practice_start_time` recorded at the beginning of the practice and the completion time of the 12th final-test question to calculate total elapsed time.

- **< 90 minutes:** offer the complex extra task;
- **>= 90 minutes:** do not offer or mention it;
- if the start time cannot be determined reliably: do not estimate and do not offer it automatically.

## Complex task

The starter provides only the array. The student must independently:

1. create a pointer for traversing the array;
2. write a complete loop;
3. increase the even elements by 2 through the pointer;
4. calculate the sum after the modification;
5. count how many elements are greater than 10;
6. print index–value pairs;
7. print the sum and the count.

### Tutor check

Expected modified array: `3 10 14 5 22 7`.

Expected sum: **61**.

Number of elements greater than 10: **2**.

For the extra task, follow the help ladder especially carefully; do not provide a ready-made loop or complete solution at first.

There is no homework.
