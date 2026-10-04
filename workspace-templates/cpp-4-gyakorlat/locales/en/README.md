# C++ – Practice 4: Arrays and Pointers

This package is the practical continuation of the **CPP_04 – Arrays and Pointers** theory material.
Time frame: **3 × 45 minutes** of practice, not including breaks.

## Learning goals

By the end of the practice, the student:

- understands array indexing and the role of zero-based indices;
- can traverse an array with a `for` loop;
- can implement simple summation, average calculation, and conditional counting;
- can distinguish between the value of a variable and its memory address;
- understands what a pointer stores and what `&` and `*` mean;
- understands dereferencing through a concrete example;
- knows the basic role of `nullptr`;
- recognizes the relationship between `array[i]` and `*(pointer + i)`;
- can safely traverse and modify a simple array using a pointer.

## Division of work

**The student edits, saves, and runs the code.** Inno explains, asks questions, gives small examples, and helps with debugging, but does not write the complete solution for the student.

The easiest way to run a program is the **RUN** button above the editor. You can also compile and run from the terminal, for example:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic G04_01_array_basics.cpp -o G04_01
./G04_01
```

The RUN button handles the file path, so you do not need to change directories with `cd` before using it.

## Structure

Every required `.cpp` file contains two steps. The starter files provide only the necessary data and a minimal program skeleton; the student writes the key indexing expression, loop, condition, and pointer expression:

- **Task A:** basic application of the new concept;
- **Task B:** a more independent, modified application of the same concept.

This way, the student does not simply fill in a prewritten solution pattern, but recalls the learned syntax and applies it immediately.

| File | Topic |
|---|---|
| `G04_01_array_basics.cpp` | Index, value, last element |
| `G04_02_array_modification.cpp` | Direct and relative modification |
| `G04_03_array_traversal.cpp` | Traversal, index + value |
| `G04_04_summation.cpp` | Sum and average |
| `G04_05_conditional_counting.cpp` | Two conditional counts |
| `G04_06_address_and_pointer.cpp` | Value, address, redirecting a pointer |
| `G04_07_dereferencing.cpp` | Dereferencing and two modifications |
| `G04_08_nullptr.cpp` | `nullptr`, checking, another object |
| `G04_09_array_and_pointer.cpp` | Address of first and second array elements |
| `G04_10_pointer_traversal.cpp` | Pointer traversal, modification, summation |

The programming tasks are followed by a **prewritten final test**: 6 multiple-choice conceptual questions and 6 output-prediction tasks using complete C++ programs. The questions are stored in `FINAL_TEST.md`; Inno presents them one at a time and does not generate replacement questions.

## Adaptive additional challenge

The package also contains a more complex `K04_01_extra.cpp` task. Inno offers it only if the student completes the required programming tasks and the final test substantially faster than planned. It is not part of the required work and is not homework.

## Important

- We do not intentionally test out-of-bounds array indexing.
- We do not dereference a pointer whose value is `nullptr`.
- During this practice we do not use `new`, `delete`, `malloc`, `free`, `int**`, user-defined functions, or dynamic arrays.
- An array and a pointer are not the same thing. In many expressions, the array name converts to a pointer to its first element.
- Output prediction is not required before every task; it is used only where it helps verify a new mental model.
