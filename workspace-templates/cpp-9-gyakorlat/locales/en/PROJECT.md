# CPP_09 – Theatre box office

**Single source:** `P09_box_office.cpp`. **Time:** 45 minutes. Develop the same program through six stages. The tutor explains the current stage; you do not need to implement the entire list at once.

## Situation and model

The theatre has 3 rows with 4 seats each. A ticket identifies a specific row–seat pair. Row 1 costs 4000 units; rows 2 and 3 cost 3000. The practice box office stores at most 4 tickets at once. This storage capacity differs from the theatre's 12 physical seats.

Ticket represents one seat and its price. BoxOffice adds, searches, cancels, lists and totals multiple tickets. Tickets are its own data members: the box office contains them. Two box offices have separate stored tickets and counts.

Use small, explicitly supplied integer inputs. No menu, keyboard input, customer name, date, payment or file saving is required. Revenue means the total price of currently stored tickets, not historical accounting.

Source order: includes and namespace → required constant → Ticket → BoxOffice → free-function prototype when needed → main → free-function definition. Define member functions inside their classes. Use the specified class names and interface for continuity; equivalent internal solutions are accepted.

## P1 – Constructing tickets, 7 minutes

**Example:** M5; recall the initialization principles from M1–M2.

Create Ticket with private int row and int seat members.

- Ticket() → 0/0, not yet a usable booking.
- Ticket(int newRow, int newSeat) → keep a valid pair; choose 0/0 for an invalid pair.
- int getRow() const, int getSeat() const.
- bool isValid() const → row 1–3 AND seat 1–4.
- int price() const → 0 for an invalid ticket, 4000 in row 1, 3000 in rows 2–3.

Compute the price instead of storing another member. Initialize both members in the parameterized constructor's initializer list. A readable approach initializes 0/0 and then assigns both in the body if the complete pair is valid. The list performs initialization; statements in the body perform later assignment. The requirement is a complete, consistent state when construction finishes. There is no need to force another ?: expression here.

Check using queried values:

| Construction | Stored row/seat | Valid? | Price |
|---|---|---|---:|
| No arguments | 0/0 | false | 0 |
| 1, 2 | 1/2 | true | 4000 |
| 3, 4 | 3/4 | true | 3000 |
| 4, 1 | 0/0 | false | 0 |
| 2, 0 | 0/0 | false | 0 |

Include at least one const ticket and query its state too.

## P2 – Empty box office and adding, 8 minutes

**Example:** M6. Unlike the indicator panel's fixed two entries, only a prefix is active within this storage capacity.

Create BoxOffice using constant `const int CAPACITY = 4;`. Private members: `Ticket tickets[CAPACITY]` and `int count`. The no-argument constructor initializes count to 0 in its initializer list. All four tickets' default constructors run independently of this count.

`int getCount() const` returns the used count. `bool add(int row, int seat)` first checks pair validity and remaining storage. Reject invalid input or full storage with false and unchanged state. Otherwise assign the new ticket to the next active position, increment count once and return true.

Checks: initially 0; adding 1/2 gives true and 1; adding 0/2 gives false and still 1. Use the returned success value. Check capacity before writing to the array.

Duplicate rejection is added in P3; until then use different seats only. This is an intermediate development stage, not the final add behavior.

## P3 – Preventing duplicate bookings, 7 minutes

**Example:** M7 searches for one number. Here two values must match together.

Write `bool isBooked(int row, int seat) const`. Search only `[0, count)`. Return true if both row and seat match an active ticket, otherwise false.

Extend add to reject duplicates as well as invalid input and full storage. Another seat in the same row is permitted. Do not compare only rows or use OR for matching identity.

Build the following state, printing each success value and current count:

1. Add 1/2: true, 1.
2. Add 1/2 again: false, 1.
3. Add 2/3: true, 2.
4. Add 3/1: true, 3.
5. Add 1/4: true, 4. It is another seat in row 1, so it is allowed.
6. Add 2/2: false, 4, because storage is full.

Consolidate earlier main calls into this sequence: do not accidentally pre-add the first ticket before starting the new sequence. Start from one freshly constructed box office.

## P4 – Cancellation and shifting left, 10 minutes

**Example:** M8 has a known removal index; your project must find the matching pair first.

Implement `bool cancel(int row, int seat)`:

1. Find the complete pair in the active tickets. Use an unambiguous not-found index value.
2. If absent, return false without modifying anything.
3. If found, move subsequent tickets one position left.
4. Decrement count once and return true.

Reading the following entry is allowed only while it remains in the active range. The tutor explains why shifting stops at the second-to-last active index and why count decreases after the loop.

From the preceding four-ticket state, cancel 2/3: true, count 3. Bookings 3/1 and 1/4 must still be found. Cancel 2/4: false, count 3. Adding 2/2 then succeeds and count becomes 4.

P5's listing will also check order. The old entry beyond count is inactive, so later searches, listings and totals must ignore it. Clearing it separately is unnecessary.

## P5 – Listing and current revenue, 7 minutes

**Example:** M9; use Ticket's public queries in place of directly stored primitive inputs.

Implement `void list() const` and `int revenue() const`. List each active ticket's row, seat and price. Revenue is the sum of price() for active tickets. Empty revenue is 0 and an empty listing prints no ticket rows.

Do not store a separate revenue member or traverse the full capacity. Shifting after cancellation need not erase the last physical slot; the correct used count excludes it.

Consolidate main into the following sequential checking run. Each result describes the state AFTER that operation.

| Operation | Success? | Count | Revenue |
|---|---|---:|---:|
| Empty box office | – | 0 | 0 |
| Add 1/2 | true | 1 | 4000 |
| Add 0/2 | false | 1 | 4000 |
| Add 1/2 again | false | 1 | 4000 |
| Add 2/3 | true | 2 | 7000 |
| Add 3/1 | true | 3 | 10000 |
| Add 1/4 | true | 4 | 14000 |
| Add 2/2 into full storage | false | 4 | 14000 |
| Cancel 2/3 | true | 3 | 11000 |
| Cancel absent 2/4 | false | 3 | 11000 |
| Add 2/2 | true | 4 | 14000 |

After cancelling the middle ticket, list rows are 1/2/4000, 3/1/3000, 1/4/4000. Adding 2/2 appends a fourth row 2/2/3000. A separate const empty box office must still report count 0 and revenue 0.

Keep this four-ticket state for P6's summary check. Afterwards, run a short boundary check: cancel first entry 1/2, last entry 2/2, then remaining 3/1 and 1/4. Count/revenue values are 3/10000, 2/7000, 1/4000, 0/0. Another cancellation of 1/4 returns false and preserves 0/0. Adding 3/4 then succeeds, yielding 1/3000. These are boundary checks of existing operations, not another task sequence.

## P6 – Returning text and cooperating library classes, 6 minutes

**Example:** M10. New includes: sstream and string. Instead of the business-card example, summarize box-office data.

Write free function `string summary(const BoxOffice* office)`. Build text in a local ostringstream using public queries and return its str() result. main prints the returned string with cout. The function itself must not print directly to cout.

Expected content is `BOOKINGS=4;VALUE=14000` for P5's final four-ticket state, and `BOOKINGS=0;VALUE=0` for the separate empty office. Labels may differ, but count and revenue must always come from current object queries.

**Pointer role:** &office passes an existing local object's address. The parameter is const BoxOffice*, so suitable const queries can be called through it. The arrow calls a member through a pointer; it does not expose private data. There is no separate box-office copy, no new/delete and no retained pointer to an expired object.

**Library cooperation:** ostringstream builds text in memory; str() produces a string value; main writes that string to cout, the standard output stream. The summary format can change independently of booking rules. These are standard-library classes/objects, not built-in primitive types.

## Final understanding check

In one short explanation, connect what Ticket construction guarantees, what additional constraints BoxOffice.add checks, and why revenue can be computed from stored tickets. Continue to the fixed quiz, without starting another project.
