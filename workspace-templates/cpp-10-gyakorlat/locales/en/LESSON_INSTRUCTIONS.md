# CPP_10 – Foundations, 45 minutes

Introduction: 3 minutes; G10_01: 8, G10_02: 9, G10_03: 10, G10_04: 15. The tutor assigns one substep at a time. Actual file contents, as well as console output, are evidence of completion.

## G10_01 – Stock snapshot

**Source:** G10_01_save.cpp. **Analogy:** M1 writes a status word rather than records.

**G10_01_A:** Create stock.txt using ofstream. Write two records on separate lines: `215 7` and `309 12`. The first field is a product code, the second its quantity. Check opening, close the file, then check stream state too. Print success only afterwards. Inspect the actual file: a space separates fields and a newline separates records.

**G10_01_B:** In the source, change the second quantity from 12 to 5, compile and run again. The file must still have two lines, the second now `309 5`. Also edit the generated file manually and observe how another run restores the source-defined contents. This tests overwriting; use only your practice files.

Explain the separate opening and writing checks. After close(), the file is no longer open, but successful stream state can still convert to true.

## G10_02 – Appending and summing visitors

**Source:** G10_02_visitors.cpp. **Analogy:** M2 uses text events; you must process numbers.

**G10_02_A:** In one block, create visits.txt with 4 and 6 on separate lines, then close and check. In another block, use ios::app to append 3 on its own line; close and check that write too. The file order is 4, 6, 3.

**G10_02_B:** Use ifstream and a loop such as `while (input >> value)` to count and sum the numbers. Expect count 3 and sum 13. After the loop, reject bad() and termination without EOF. This exercise handles one-number records with valid input; it is not the project's strict two-number parser.

Second test: append 8 rather than 3 in the source. On the next run, expect 3 values and sum 18. The first block recreates the file on every run, so repeating the complete program does not keep appending extra lines. Compute 3/13 and 3/18 from variables rather than printing hard-coded answers.

## G10_03 – Invalid file and stream state

**Source:** G10_03_invalid_data.cpp. **Analogy:** M3; first discuss the successful final-number extraction.

**G10_03_A:** Write `215 bad` and a newline to invalid.txt, then close, check and reopen it for reading. Expect two integers. Convert the chained extraction result to bool and print success, eof() and fail(). Expected: `0 0 1`. Do not process the second number after failed extraction. This is an intentional diagnostic demonstration and may terminate normally with code 0.

**G10_03_B:** Change the generated contents in the source; compile and run separately for each:

| Entire contents | Success | eof | fail |
|---|---:|---:|---:|
| 215 bad followed by newline | 0 | 0 | 1 |
| 215 7, no final newline | 1 | 1 | 0 |
| only 215, no final newline | 0 | 1 | 1 |

Print actual state-query results. The last two cases show why EOF is not equivalent to a valid record. A !eof() check alone can miss the missing second field. Check state after reading, rather than predicting a future read.

## G10_04 – Strict validation of one line

**Source:** G10_04_line.cpp. **Analogy:** M4 checks a MODE keyword and one number; your task needs two integer fields and two ranges.

**G10_04_A:** Implement `bool validLine(string line)`. Require exactly two whitespace-separated tokens. The first must be an entire integer in 100–999; the second an entire integer in 0–20. A missing or third token, characters left after the number, or an out-of-range int must be rejected. Extract two text tokens, then parse and validate each using its own istringstream. Do not simply extract two numbers: the invalid single token `215.7` could split into two numbers.

A token is a whitespace-separated piece of text. After numeric extraction, probing for another char checks whether any characters remain. A successful char probe means rejection. Failure at the token's end is the expected outcome here.

**G10_04_B:** Read supplied g04_cases.txt using getline. Call your function for each line and print the bool result. Eight output lines: `1, 0, 0, 0, 0, 0, 0, 0`. Also check `100 0` and `999 20`: both true. Preserve the original eight-line fixture; boundary cases can be separate function calls.

This exercise evaluates each line separately. The project will add the requirement that the whole object collection is replaced only after a completely successful load.
