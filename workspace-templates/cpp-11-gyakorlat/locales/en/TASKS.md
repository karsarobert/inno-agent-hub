# C++ 07–10 – short InnoAgent practice

24 independent coding tasks, each followed by 1–2 theory questions about your code. Four blocks of six tasks. The 47 theory questions are discussed after coding.

## Contents

- [G07_01 – Product data](#g07_01)
- [G07_02 – Changing a copy](#g07_02)
- [G07_03 – Deactivation through a pointer](#g07_03)
- [G07_04 – Available books](#g07_04)
- [G07_05 – Scope error](#g07_05)
- [G07_06 – The active union member](#g07_06)
- [G08_01 – Are the two stocks empty?](#g08_01)
- [G08_02 – Fixing an access error](#g08_02)
- [G08_03 – Valid reservations](#g08_03)
- [G08_04 – Querying a const object](#g08_04)
- [G08_05 – Further deposits into two money boxes](#g08_05)
- [G08_06 – Results reaching a threshold](#g08_06)
- [G09_01 – Two ways to construct a rectangle](#g09_01)
- [G09_02 – Clamping a charge level](#g09_02)
- [G09_03 – Initializing an object array](#g09_03)
- [G09_04 – Refactoring to an initializer list](#g09_04)
- [G09_05 – Removing the last book](#g09_05)
- [G09_06 – Calling through the supplied pointer](#g09_06)
- [G10_01 – Saving a short integer list](#g10_01)
- [G10_02 – Appending across two runs](#g10_02)
- [G10_03 – Counting negative values](#g10_03)
- [G10_04 – Fixing an extra count at end of file](#g10_04)
- [G10_05 – Strict validation of two integer fields](#g10_05)
- [G10_06 – Loading while preserving old data on failure](#g10_06)

<a id="g07_01"></a>

## G07_01 – Product data

**File:** `g07_01.cpp` · Incomplete code

**Goal:** Read structure members and use them in a calculation.

At the two TODO markers, read the quantity and unit price into the Product members, then print their product. Quantity is an integer from 0 to 20; unit price is a finite real number from 0 to 100. Output one number with two decimal places and no label. Keep the supplied formatting.

### Checks

**1. Typical purchase**


Input:

```text
3 2.50
```

Expected output:

```text
7.50
```

**2. Zero quantity**


Input:

```text
0 8.25
```

Expected output:

```text
0.00
```

**3. Upper bounds**


Input:

```text
20 100
```

Expected output:

```text
2000.00
```

### Theory questions – after checking the code

1. Why can these two structure members have different types?
2. Which expression in your program accesses the object’s unit price?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g07_02"></a>

## G07_02 – Changing a copy

**File:** `g07_02.cpp` · Incomplete code

**Goal:** Trace copy-initialization and independent object state.

Change the first TODO line to copy-initialize copy from original. At the second TODO, set only copy.count to the input next value. Input consists of two integers from 0 to 20. Keep the supplied output statement.

### Checks

**1. Different new value**


Input:

```text
5 2
```

Expected output:

```text
5 2
```

**2. Zero in the copy**


Input:

```text
9 0
```

Expected output:

```text
9 0
```

### Theory questions – after checking the code

1. Why was the original quantity preserved?
2. How does creating the copy differ from assigning a member later?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g07_03"></a>

## G07_03 – Deactivation through a pointer

**File:** `g07_03.cpp` · Incomplete code

**Goal:** Modify one member through a valid pointer.

Implement deactivate. For a valid pointer, set active to false and preserve id; for nullptr, do nothing. The function prints nothing. Input is an identifier from 0 to 99 and a 0/1 flag. main also tries a null-pointer call.

### Checks

**1. Active device**


Input:

```text
12 1
```

Expected output:

```text
12 0
```

**2. Already inactive**


Input:

```text
3 0
```

Expected output:

```text
3 0
```

### Theory questions – after checking the code

1. What expression is p->active shorthand for?
2. Why must a null pointer be excluded before member access?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g07_04"></a>

## G07_04 – Available books

**File:** `g07_04.cpp` · Incomplete code

**Goal:** Count matching records in an array of structures.

Complete countAvailable: how many of the first n books are available? Do not sum page counts. 0 ≤ n ≤ 5, followed by n pairs of page count and flag (pages: 1…1000; flag: 0 or 1). Do not modify the array. An empty range yields 0.

### Checks

**1. Mixed list**


Input:

```text
3
120 1
80 0
250 1
```

Expected output:

```text
2
```

**2. Empty list**


Input:

```text
0
```

Expected output:

```text
0
```

**3. None available**


Input:

```text
2
20 0
30 0
```

Expected output:

```text
0
```

**4. All available**


Input:

```text
2
20 1
30 1
```

Expected output:

```text
2
```

### Theory questions – after checking the code

1. Why iterate to n rather than always through all five slots?
2. What input would expose counting every book without the condition?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g07_05"></a>

## G07_05 – Scope error

**File:** `g07_05.cpp` · Intentional compilation error

**Goal:** Fix local-name visibility and trace shadowing.

The starter intentionally fails to compile. Keep the multiplication inside its inner block and the output outside. Place the result declaration and assignment so the program prints three times the input, then 9, then the original input. Input is an integer from −20 to 20. Preserve the second inner block.

### Checks

**1. Positive input**


Input:

```text
4
```

Expected output:

```text
12
9
4
```

**2. Negative input**


Input:

```text
-2
```

Expected output:

```text
-6
9
-2
```

### Theory questions – after checking the code

1. Why was result not visible at the original output statement?
2. What would change if the second block used number = 9; instead of int number = 9;?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g07_06"></a>

## G07_06 – The active union member

**File:** `g07_06.cpp` · Incomplete code

**Goal:** Use a tag to access the active member and observe memory layout.

Input is I and an integer, or D and a finite real value. The supplied code reads the appropriate union member. At TODO, print only that active member on one line. Keep the sizeof output. Choose the correct member before running; do not read an inactive member. Sizes depend on the environment; no specific byte sizes are required.

### Checks

**1. Integer member**


Input:

```text
I 7
```

First output line: `7`.

The second line contains four byte sizes: `sizeof(TwoNumbers) sizeof(Number) sizeof(int) sizeof(double)`. No fixed numbers are required. The structure occupies at least the sum of its two members’ sizes; the union occupies at least the larger member’s size. Padding may increase these sizes.

**2. Real member**


Input:

```text
D 2.5
```

First output line: `2.5`.

The second line contains four byte sizes: `sizeof(TwoNumbers) sizeof(Number) sizeof(int) sizeof(double)`. No fixed numbers are required. The structure occupies at least the sum of its two members’ sizes; the union occupies at least the larger member’s size. Padding may increase these sizes.

### Theory questions – after checking the code

1. Why do we read the member indicated by kind?
2. Why might the structure be larger than the sum of its member sizes?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g08_01"></a>

## G08_01 – Are the two stocks empty?

**File:** `g08_01.cpp` · Incomplete code

**Goal:** Public Boolean queries and per-instance state.

Make isEmpty return true when its own object has quantity 0, and false otherwise. Change only the TODO return expression. Input consists of two integers from 0 to 100; output the two empty-state flags (0/1), separated by a space.

### Checks

**1. Two non-empty stocks**


Input:

```text
4 9
```

Expected output:

```text
0 0
```

**2. The first is empty**


Input:

```text
0 100
```

Expected output:

```text
1 0
```

**3. The second is empty**


Input:

```text
100 0
```

Expected output:

```text
0 1
```

### Theory questions – after checking the code

1. What is the class, and which two objects are created in this main?
2. Why does setting the second object not overwrite the first object’s state?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g08_02"></a>

## G08_02 – Fixing an access error

**File:** `g08_02.cpp` · Intentional compilation error

**Goal:** Recognize a compilation error and use the public interface.

The starter intentionally fails to compile. Fix the output statement in main using the existing getter. Keep the data member private. Input is one integer from −10 to 10; print that value.

**Source review:** The member remains private; main uses the public getter.

### Checks

**1. Positive**


Input:

```text
6
```

Expected output:

```text
6
```

**2. Negative**


Input:

```text
-3
```

Expected output:

```text
-3
```

### Theory questions – after checking the code

1. Why was direct member access from main invalid?
2. What is the default access in a class and in a struct?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g08_03"></a>

## G08_03 – Valid reservations

**File:** `g08_03.cpp` · Incomplete code

**Goal:** Conditional state changes and preserving state on rejection.

Implement reserve. For a positive request no greater than the remaining stock, subtract it and return true; otherwise return false without changing the stock. Initial stock is 20. Input contains two successive requests from −5 to 25. Each output line contains the success flag (0/1) and remaining quantity.

### Checks

**1. Two successes**


Input:

```text
3 5
```

Expected output:

```text
1 17
1 12
```

**2. Zero then success**


Input:

```text
0 1
```

Expected output:

```text
0 20
1 19
```

**3. Two rejections**


Input:

```text
-2 21
```

Expected output:

```text
0 20
0 20
```

**4. Entire stock**


Input:

```text
20 1
```

Expected output:

```text
1 0
0 0
```

### Theory questions – after checking the code

1. Why must the second request be compared with the current stock?
2. Which test demonstrates that a rejected request did not change the state?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g08_04"></a>

## G08_04 – Querying a const object

**File:** `g08_04.cpp` · Intentional compilation error

**Goal:** Const-correctness in a computed getter.

The starter intentionally fails to compile. Complete the freeSpaces member function declaration so it can be called on a const object. Keep const in main. Input: capacity and occupancy, with 0 ≤ occupancy ≤ capacity ≤ 100. Output: the number of free spaces.

**Source review:** The getter is const and main retains its const object.

### Checks

**1. Partly occupied**


Input:

```text
12 5
```

Expected output:

```text
7
```

**2. Zero capacity**


Input:

```text
0 0
```

Expected output:

```text
0
```

**3. Full**


Input:

```text
10 10
```

Expected output:

```text
0
```

### Theory questions – after checking the code

1. What does const after the member function parameter list promise?
2. May a const getter perform subtraction? Why?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g08_05"></a>

## G08_05 – Further deposits into two money boxes

**File:** `g08_05.cpp` · Incomplete code

**Goal:** Modify independent copies through member functions.

After the copy is created, deposit y into first and z into second. Keep the copy operation and output statement in place. Input x, y, z consists of three integers from 0 to 100. Output the first and second balances.

### Checks

**1. Different deposits**


Input:

```text
10 2 7
```

Expected output:

```text
12 17
```

**2. Zero initial balance**


Input:

```text
0 5 0
```

Expected output:

```text
5 0
```

**3. Boundary values**


Input:

```text
100 100 100
```

Expected output:

```text
200 200
```

### Theory questions – after checking the code

1. Which object is modified by first.deposit(y)?
2. Why does the second money box also contain the initial x amount?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g08_06"></a>

## G08_06 – Results reaching a threshold

**File:** `g08_06.cpp` · Incomplete code

**Goal:** Traverse an object array using public getters.

Implement countReached to count objects among the first n whose score is at least threshold. An empty array gives 0. Use the getter and preserve private access. Input: n (0…5), threshold, then n scores; all scores and the threshold are integers from −100 to 100.

### Checks

**1. Mixed**


Input:

```text
4 10
9 10 15 -2
```

Expected output:

```text
2
```

**2. Empty**


Input:

```text
0 5
```

Expected output:

```text
0
```

**3. Exactly at the threshold**


Input:

```text
1 10
10
```

Expected output:

```text
1
```

**4. None**


Input:

```text
2 10
1 9
```

Expected output:

```text
0
```

### Theory questions – after checking the code

1. Why can the getter be called on elements of the const array?
2. Which test distinguishes > from >=?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g09_01"></a>

## G09_01 – Two ways to construct a rectangle

**File:** `g09_01.cpp` · Incomplete code

**Goal:** Default and parameterized constructors.

Fix the initializer lists of both constructors. With no arguments, create a 1×1 rectangle; with two arguments, create an a×b rectangle. Input: two integers from 1 to 20. Output the areas of the default and parameterized rectangles.

### Checks

**1. Different sides**


Input:

```text
3 7
```

Expected output:

```text
1 21
```

**2. Unit square**


Input:

```text
1 1
```

Expected output:

```text
1 1
```

**3. Upper bound**


Input:

```text
20 20
```

Expected output:

```text
1 400
```

### Theory questions – after checking the code

1. Why is there no return type before either constructor name?
2. How is one of the two constructors selected?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g09_02"></a>

## G09_02 – Clamping a charge level

**File:** `g09_02.cpp` · Incomplete code

**Goal:** Valid initial state and handling both bounds.

Make the constructor clamp the input integer charge to 0…100: negative values become 0, values above 100 become 100, and valid values stay unchanged. Input: one integer from −200 to 200. Output the stored value.

### Checks

**1. Below lower bound**


Input:

```text
-1
```

Expected output:

```text
0
```

**2. Lower bound**


Input:

```text
0
```

Expected output:

```text
0
```

**3. Interior value**


Input:

```text
38
```

Expected output:

```text
38
```

**4. Upper bound**


Input:

```text
100
```

Expected output:

```text
100
```

**5. Above upper bound**


Input:

```text
102
```

Expected output:

```text
100
```

### Theory questions – after checking the code

1. How does clamping differ from rejecting a request?
2. Why are 0 and −1 separate tests?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g09_03"></a>

## G09_03 – Initializing an object array

**File:** `g09_03.cpp` · Intentional compilation error

**Goal:** Construct array elements with a parameterized constructor.

The starter intentionally fails to compile. Initialize both elements of rooms in its declaration using a and b. Keep the class unchanged. Input: two integers from 1 to 4. Output the bed counts of the two rooms.

**Source review:** Both array elements are initialized with arguments in the declaration; the class is unchanged.

### Checks

**1. Different rooms**


Input:

```text
1 4
```

Expected output:

```text
1 4
```

**2. Identical rooms**


Input:

```text
2 2
```

Expected output:

```text
2 2
```

### Theory questions – after checking the code

1. Why did the array declaration without arguments fail to compile?
2. What constructor would the original declaration need?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g09_04"></a>

## G09_04 – Refactoring to an initializer list

**File:** `g09_04.cpp` · Required refactoring of working code

**Goal:** Distinguish initialization from later assignment.

The starter already produces correct output. Rewrite the constructor to initialize both members in an initializer list, in their declaration order, and leave the constructor body empty. Keep the remaining code. Input: row and seat, two integers from 1 to 20. Completion also requires source inspection.

**Source review:** Both members appear in an initializer list in declaration order; the constructor body is empty. The starter output is already correct, so execution alone is insufficient.

### Checks

**1. Typical seat**


Input:

```text
4 12
```

Expected output:

```text
4 12
```

**2. First seat**


Input:

```text
1 1
```

Expected output:

```text
1 1
```

### Theory questions – after checking the code

1. What determines the order of member initialization?
2. When does the constructor body run relative to member initialization?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g09_05"></a>

## G09_05 – Removing the last book

**File:** `g09_05.cpp` · Incomplete code

**Goal:** Composition and managing logical size.

Implement removeLast: on an empty shelf return false without changes; otherwise decrease the size by one and return true. Do not resize or clear the array. Input: initial size n (0…2) and removal attempts k (1…3). For each attempt output success and the new size.

### Checks

**1. Empty shelf**


Input:

```text
0 1
```

Expected output:

```text
0 0
```

**2. One book**


Input:

```text
1 2
```

Expected output:

```text
1 0
0 0
```

**3. Two books**


Input:

```text
2 3
```

Expected output:

```text
1 1
1 0
0 0
```

### Theory questions – after checking the code

1. How does capacity differ from the current size?
2. Why is the relationship between the shelf and its books composition?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g09_06"></a>

## G09_06 – Calling through the supplied pointer

**File:** `g09_06.cpp` · Incomplete code

**Goal:** Observe virtual dispatch in a supplied short example.

The class definitions are supplied; keep them unchanged. At both TODO markers call signal through pointer and print its result. Input is 0 or 1. A 0 keeps the base object; a 1 selects the bell for the second call. Use the supplied pointer rather than hard-coding output.

**Source review:** Both output statements call the virtual function through the supplied base pointer. Classes are unchanged; no answers are hard-coded.

### Checks

**1. Keep the base object**


Input:

```text
0
```

Expected output:

```text
BASE
BASE
```

**2. Switch to the bell**


Input:

```text
1
```

Expected output:

```text
BASE
DING
```

### Theory questions – after checking the code

1. Why can the second result be DING even though the pointer type is Device*?
2. What does override help check here?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g10_01"></a>

## G10_01 – Saving a short integer list

**File:** `g10_01.cpp` · Incomplete code

**Goal:** File output, replacement and checked closing.

In save, write the first n integers on separate lines. Opening and error checking are supplied. Saving replaces the previous out01.txt contents; n=0 produces an empty file. Input: n (0…4), followed by n integers from −99 to 99. main prints OK and then reads back the file.

### Checks

**1. Three numbers**


Input:

```text
3
4 -2 9
```

Expected output:

```text
OK
4
-2
9
```

Expected file contents: `out01.txt`

```text
4
-2
9
```

**2. Replacement**

Before starting, `out01.txt` contains:

```text
99
88
```

Input:

```text
1
7
```

Expected output:

```text
OK
7
```

Expected file contents: `out01.txt`

```text
7
```

**3. Empty save**

Before starting, `out01.txt` contains:

```text
99
```

Input:

```text
0
```

Expected output:

```text
OK
```

Expected file contents: `out01.txt`

*Empty file (0 bytes).*

### Theory questions – after checking the code

1. Why does the save function use ofstream?
2. Why check the stream state after close as well?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g10_02"></a>

## G10_02 – Appending across two runs

**File:** `g10_02.cpp` · Behavior to fix

**Goal:** Append mode and persistent file contents.

The starter incorrectly overwrites. Change only the opening mode to append the input integer to out02.txt. Before the first shared test, the file should contain one line with 2 (supplied in the package). Run with 5 and then −1 in the same directory; do not reset the file between runs. Also try a separate case with no existing file. Input is one integer from −99 to 99.

### Checks

**1. Two successive runs**

Before starting: `out02.txt` contains one line, `2`. Do not reset between these steps.

Run 1:

Input:

```text
5
```

Expected output:

```text
2
5
```

Expected file contents: `out02.txt`

```text
2
5
```

Run 2:

Input:

```text
-1
```

Expected output:

```text
2
5
-1
```

Expected file contents: `out02.txt`

```text
2
5
-1
```

**2. Creating a missing file**

For this separate test, `out02.txt` must not exist; preserve the previous test file first.

Input:

```text
7
```

Expected output:

```text
7
```

Expected file contents: `out02.txt`

```text
7
```

### Theory questions – after checking the code

1. How does ios::app differ from the original opening mode used here?
2. Relative to which directory is out02.txt resolved?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g10_03"></a>

## G10_03 – Counting negative values

**File:** `g10_03.cpp` · Incomplete code

**Goal:** Extraction-controlled loops and committing a result only on success.

At TODO 1 count negative numbers in the temporary variable; at TODO 2 commit the result through the supplied pointer only after reading has passed its checks. Standard input supplies a filename. Files contain only integer tokens from −99 to 99, whitespace, or the invalid token X; there are no overflows or partially numeric tokens. Missing/invalid files must preserve the result 99. An empty file succeeds with count 0.

### Checks

**1. Mixed numbers**


Input:

```text
data/neg_ok.txt
```

Expected output:

```text
1 2
```

**2. Empty**


Input:

```text
data/neg_empty.txt
```

Expected output:

```text
1 0
```

**3. No final newline**


Input:

```text
data/neg_no_newline.txt
```

Expected output:

```text
1 1
```

**4. Invalid token**


Input:

```text
data/neg_bad.txt
```

Expected output:

```text
0 99
```

**5. Missing file**


Input:

```text
data/missing.txt
```

Expected output:

```text
0 99
```

### Theory questions – after checking the code

1. Why count in a temporary variable?
2. When is the caller’s result variable modified?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g10_04"></a>

## G10_04 – Fixing an extra count at end of file

**File:** `g10_04.cpp` · Behavior to fix

**Goal:** Fix the while (!eof()) pattern.

For some files the starter processes a value again. Make successful extraction control the loop and remove the separate extraction inside the body. Standard input supplies a filename; files contain only valid integers from −99 to 99, or are empty. Output the count of even numbers. Zero is even.

### Checks

**1. With a final newline**


Input:

```text
data/even_newline.txt
```

Expected output:

```text
1
```

**2. Without a final newline**


Input:

```text
data/even_no_newline.txt
```

Expected output:

```text
2
```

**3. Empty**


Input:

```text
data/even_empty.txt
```

Expected output:

```text
0
```

### Theory questions – after checking the code

1. Why must extraction success be checked before processing a value?
2. Why does eof() not predict whether the next read will succeed?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g10_05"></a>

## G10_05 – Strict validation of two integer fields

**File:** `g10_05.cpp` · Incomplete code

**Goal:** Validate field count and range using a supplied token validator.

Make validateLine accept exactly two integer tokens: a code and a quantity from 0 to 20. Keep the supplied integerToken helper unchanged. At the first TODO require both fields and reject a third; at the second check the quantity range. The code may be any int value. On failure preserve both output variables (77, 88). The data to validate is one entire line of standard input.

### Checks

**1. Valid**


Input:

```text
12 7
```

Expected output:

```text
1 12 7
```

**2. Missing field**


Input:

```text
12
```

Expected output:

```text
0 77 88
```

**3. Extra field**


Input:

```text
12 7 extra
```

Expected output:

```text
0 77 88
```

**4. Invalid token**


Input:

```text
12x 7
```

Expected output:

```text
0 77 88
```

**5. Lower bound**


Input:

```text
0 0
```

Expected output:

```text
1 0 0
```

**6. Upper bound**


Input:

```text
-4 20
```

Expected output:

```text
1 -4 20
```

**7. Too large**


Input:

```text
12 21
```

Expected output:

```text
0 77 88
```

**8. Negative quantity**


Input:

```text
12 -1
```

Expected output:

```text
0 77 88
```

**9. Empty line**


Input:

```text

```

Expected output:

```text
0 77 88
```

**10. Partially numeric quantity**


Input:

```text
12 7x
```

Expected output:

```text
0 77 88
```

### Theory questions – after checking the code

1. Why are field count and each token being a complete integer checked separately?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.

<a id="g10_06"></a>

## G10_06 – Loading while preserving old data on failure

**File:** `g10_06.cpp` · Behavior to fix

**Goal:** Temporary storage and a single final commit.

Keep the supplied helpers and main unchanged. load currently clears and changes its target too early. Make capacity checks and all new values use the temporary list, then replace the target only after complete success. File format: exactly one integer from 0 to 50 per line, at most two lines. An empty file is a valid empty list; a blank line is invalid. On failure preserve the original list containing 40, 41. Input is the filename; output success, size, then the elements.

### Checks

**1. Successful replacement**


Input:

```text
data/load_ok.txt
```

Expected output:

```text
1 2 5 7
```

**2. Empty file**


Input:

```text
data/load_empty.txt
```

Expected output:

```text
1 0
```

**3. Invalid second line**


Input:

```text
data/load_bad.txt
```

Expected output:

```text
0 2 40 41
```

**4. Capacity overflow**


Input:

```text
data/load_full.txt
```

Expected output:

```text
0 2 40 41
```

**5. Blank line**


Input:

```text
data/load_blank.txt
```

Expected output:

```text
0 2 40 41
```

**6. Negative value**


Input:

```text
data/load_negative.txt
```

Expected output:

```text
0 2 40 41
```

**7. Extra field**


Input:

```text
data/load_extra.txt
```

Expected output:

```text
0 2 40 41
```

**8. Missing file**


Input:

```text
data/missing.txt
```

Expected output:

```text
0 2 40 41
```

### Theory questions – after checking the code

1. Why may the target be replaced only after the entire read succeeds?
2. How does an empty file differ from a file containing one blank line in this task?

**Complete when:** the code meets the requirements, all checks pass, and you have answered each question in your own words.
