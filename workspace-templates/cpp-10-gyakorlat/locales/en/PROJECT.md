# CPP_10 – Persistent box-office data

**Source:** P10_box_office.cpp. **45 minutes, P1–P6.** Existing domain classes are supplied; you write the new file handling. No inheritance, override, polymorphism, dynamic memory or reference parameters. Your methods take strings by value. numeric_limits is unnecessary here because all stored data is integer.

## Model and shared file format

Three rows with four seats each; row 1 costs 4000 and rows 2–3 cost 3000. Storage capacity is four tickets. A seat may appear only once. Revenue is the sum of current ticket prices. The provided add() checks ranges, capacity and duplicates before modifying state.

The first file line is **exactly** `TICKETS 1`, followed by two integers per line: row and seat. This header is identical in both language packages. The 1 is a format version, not a ticket count. Price and count are not stored; they are derived from records.

```text
TICKETS 1
1 2
2 3
```

This represents two tickets and revenue 7000. Data fields are separated by at least one space/tab; leading/trailing whitespace on data lines is allowed. The header has no extra whitespace, BOM or fields. Fixtures use LF line endings. The final newline is optional. Blank data lines are invalid. A completely empty file is invalid because its header is missing. A **header-only** file is valid and represents an empty office. This differs from the HTML measurement log.

## P1 – Understand the baseline and format, 4 minutes

Run the baseline: the first two additions succeed, the duplicate does not; count 2, revenue 7000. Locate the active count, validation and const getters. Make your own second test: adding 3/4 succeeds and revenue becomes 10000. Return to the original two-ticket setup for the next stage. P1 requires this independent second test and understanding the rules; merely running the starter is insufficient.

The supplied baseline is not the whole lesson-9 project: unused refund functionality is omitted. If using your own previous classes, align the required names/interface without automatically overwriting your working implementation.

## P2 – Saving with a header, 8 minutes

**Examples:** M1 and M7's header concept. Implement `bool save(string filename) const`. Default ofstream: check opening → write header → write active tickets using row/seat getters → close → return success from stream state. Keep members private.

Saving two tickets must produce the three lines shown above in tickets.txt. Save the same office again: still three lines, not two headers or four tickets. Saving a const empty office to a separate file produces only the header. No floating-point precision setting is needed because both fields are int.

Stream Boolean conversion reports errors, not whether a file remains open. Both return static_cast<bool>(file) and equivalent return !file.fail() are acceptable. Direct overwrite saving does not restore the old file after a write failure; preserving in-memory state is a separate loading requirement.

## P3 – Processing one booking line, 10 minutes

**Example:** M4 and your G10_04. Implement public `bool addLine(string line)`. Require exactly two separate tokens, each entirely a valid int. Only then call the existing add(row, seat). Return its result; do not duplicate the capacity, range and duplicate checks.

Starting with a fresh office, test in order: `1 2` true; another `1 2` false; `2.3` false; `2 4x` false; `2 4` true. Final count 2, revenue 7000. Also reject a missing seat, third token, `4 1`, `1 0` and an oversized integer. Failure must leave the office unchanged.

This operation is deliberately public: it offers a validated addition, without exposing the array. During a full file load, the same operation will be called on a temporary office.

## P4 – Complete load or unchanged original, 12 minutes

**Examples:** M5's temporary state and M7's header. Your P3 already handles a line. Implement `bool load(string filename)`:

1. Open with ifstream; failed opening returns false without changing the original.
2. Read the header with the first getline. Missing or different header: false, original preserved.
3. Create an empty temporary BoxOffice.
4. For each subsequent getline, call its addLine. Any rejection makes the whole load fail.
5. After the loop, check bad() and EOF termination. Only after complete success assign the temporary state to the current object and return true.

The this pointer identifies the current object; *this accesses that object. Whole-object assignment copies both the fixed array and count here. Do not clear the original first or update it inside the reading loop.

Tests: begin with 1/4 in the original (count 1, revenue 4000). Loading ok.txt produces 2 tickets and 7000: replacement, not append. Loading duplicate.txt and then missing.txt must both fail; count/revenue stay 2/7000 and the same two seats remain. P6 lists the remaining mandatory edge cases.

## P5 – Returning a text report, 6 minutes

**Example:** M6. Implement `string report() const` using ostringstream. Return `TICKETS=2;REVENUE=7000` for the two-ticket office and `TICKETS=0;REVENUE=0` for a const empty office. Query both numbers from current state. The method neither prints directly to cout nor modifies tickets.txt; main prints the returned string.

Explain: ostringstream builds characters in memory and str() returns the resulting string. Report labels are identical in HU/EN, while source identifiers follow the package language.

## P6 – New execution and invalid files, 5 minutes

Have main read a single character: `S` or `L`. S adds tickets 1/2 and 2/3 and saves to tickets.txt; L loads that file into a freshly created empty office. Then print the operation's success and your report. Invalid mode/input may exit with code 1; a full menu is not required.

RUN → S → program ends; new RUN → L. Both produce success and TICKETS=2;REVENUE=7000. The loading branch must neither recreate the file nor manually add the two tickets: data must actually come from the previous execution.

The tutor checks the completed operation against the supplied files through short test calls, without introducing another parser:

| File | Outcome |
|---|---|
| full.txt | success, 4 tickets, 14000 |
| no_newline.txt | success, 1 ticket (3/4), 3000 |
| header_only.txt | success, empty office |
| empty.txt, wrong_header.txt | failure; original preserved |
| duplicate.txt, overflow.txt | failure; original preserved |
| missing.txt, extra.txt, joined.txt, suffix.txt, range.txt, blank.txt | failure; original preserved |
| nonexistent absent.txt | failure; original preserved |

Before each failure test, establish a known nonempty original. Afterwards inspect count, revenue and actual seats, not just a false return. Do not change the save target tickets.txt to an invalid fixture that S could overwrite; pass the fixture to load in a separate test call.
