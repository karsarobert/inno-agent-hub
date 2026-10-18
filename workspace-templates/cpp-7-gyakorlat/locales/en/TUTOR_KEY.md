# CPP_07 – Tutor and instructor checking guide

This is not a student lesson to read aloud. Check actual code against the
requirements; do not reveal the entire key before the tasks.

## Introductory exercise checks

| Part | Required result or behavior |
|---|---|
| G07_01 A | A particular object as well as a type: 101, 23.5, true. |
| G07_01 B | After changing the copy: 23.5 and 30; after separate assignment: 23.5 and 23.5. |
| G07_02 A | A by-value parameter and a returned structure: original 10.5, new 12.5. |
| G07_02 B | The original's address and arrow access: original 12, copy 12.5. |
| G07_03 A/B | Integer 7, then real 2.5; the flag is updated; only active members are read. |
| G07_04 A/B | Inner 20, outer local 10, global 5; the function also sees global 5. |
| G07_04 C | Sum 6; loop index unavailable after the loop; final code compiles again. |

## Project checks

| Check | Original data | After P6 |
|---|---:|---:|
| First record's value | 18.5 | 20.5 |
| Valid count | 5 | 5 |
| Valid sum for checking the average | 89 | 91 |
| Valid average | 17.8 | 18.2 |
| Valid and above 20 | 3 | 4 |
| Valid and above 21 | 1 | 1 |

P2 prints all six records. P4 excludes the invalid 26.0 and includes the valid
-2.0. Call the average function only with a positive valid count. When all flags
are false, there must be no average call or division by zero. Restore the original flags afterwards.

P6 changes the first record directly. Its ID, date and Boolean member, and the
other records, stay unchanged. Existing functions should remain reusable.
Both 1/0 and yes/no, and both 17.8 and 17.80, are acceptable. An average truncated
to 17 is incorrect. Labels and spacing can differ.

## T1 answer key

### T1/1 – B

Members have names and may have different types.
Topic: structures and arrays.

### T1/2 – C

The type definition describes the data structure; an object is created separately.
Topic: types and objects.

### T1/3 – A

The copy is a separate object initialized from the original's member values.
Topic: copying and initialization.

### T1/4 – D

The arrow selects a member of the pointed-to structure.
Topic: pointers and member access.

### T1/5 – B

Const prevents changes through this access path; the element count is separate.
Topic: const and array parameters.

### T1/6 – A

Reading an inactive member in the demonstrated case would be undefined behavior.
Topic: active union members.

### T1/7 – C

The flag is a manual convention; the language does not check consistency automatically.
Topic: tracking a union with a flag.

### T1/8 – D

The variable declared in the header belongs to the loop's scope.
Topic: loop-variable scope.

### T1/9 – B

Calling a function does not extend the visibility of the caller's local names.
Topic: functions and name lookup.

### T1/10 – C

Shadowing changes name lookup; it does not destroy the outer object.
Topic: shadowing and lifetime.

## T2 answer key

### T2/1

```text
8 11
```

The objects are separate, so changing the copy does not affect the original.
Topic: copying structures.

### T2/2

```text
13 14
```

The increased function returns an independent copy. The pointer later changes the original.
Topic: pass by value and pointers.

### T2/3

```text
10
```

The invalid 100 is excluded; the average is (8+12)/2.
Topic: filtering valid data.

### T2/4

```text
4 1.5
```

Each read uses the member active at that point; the previous member is not read after switching.
Topic: active union members.

### T2/5

```text
20 5 10
```

The inner name denotes 20, printValue sees global 5, and after the block main's local value is 10.
Topic: shadowing and name lookup.

### T2/6

A semicolon is missing after the structure definition's closing brace.
This is a compilation error; adding the semicolon is the smallest correction.
Topic: structure-definition syntax.

### T2/7

Pointer is a pointer, so `pointer.value` is invalid.
Correct it to `pointer->value` or `(*pointer).value`.
Topic: pointers and member access.

### T2/8

The real member is active, but the code reads integer.
This is undefined behavior even if compilation succeeds. To print the assigned
value, the smallest correction is to read `data.real`. If an integer value is
intended, assign that member appropriately before reading it. Do not expect a numeric output from the faulty code.
Topic: reading an inactive union member.

### T2/9

The name count is not visible outside the inner block.
Moving the output into that block is an acceptable fix. If the value must be
used outside, declare the variable in the outer block and assign it inside,
rather than declaring another inner variable.
Topic: local scope.

### T2/10

At `i == size`, the loop accesses beyond the array.
Use `i < size`. There is no element `data[size]`; do not run the faulty code
before correcting it. Successful compilation alone does not prove correctness.
Topic: loop bounds and arrays.

## Scoring and completion

Each question is worth 1 point. T1: 10; T2: 10; total: 20.
For debugging, award the point when the main cause and a working minimal fix
are both given. Accept technically equivalent fixes. For output, check meaningful
order; do not deduct a point just for omitting the final newline.

The first meaningful answer counts, followed by teaching feedback. Choose review
topics only from actual errors. Do not assign grades, percentage ratings,
homework, or automatically announce an exam for the next class.
