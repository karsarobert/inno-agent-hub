# CPP_09 – Foundation tasks

Introduction: 3 minutes; G09_01: 8, G09_02: 12, G09_03: 12, G09_04: 10 minutes. The tutor assigns one part at a time. You write the code; examples solve different problems. Query the actual objects in every check rather than printing the expected numbers as constants.

## G09_01 – Constructing a competitor

**Source:** `G09_01_competitor.cpp`. **Example:** M1.

### G09_01_A

Create class `Competitor` with private `int bib` and `int points` members. A data member stores data belonging to each object. Write a no-argument constructor for initial state 0/0, and a constructor taking a bib number with points initially 0. Both use initializer lists.

Write `int getBib() const` and `int getPoints() const` queries. Create a no-argument object and another with bib 17. Check: 0/0 and 17/0. Bib 0 means not identified yet; validation is not part of this task.

### G09_01_B

Add a two-int constructor initializing both bib and points. An object with bib 23 and 12 points must report 23/12. Both previous construction forms must still work. Include at least one const object whose queries can be called.

A constructor has its class name and no return type. Its initializer list supplies member initial values before the body. Follow member declaration order. No setters, custom copy constructor or additional topic is required.

## G09_02 – Brightness and the conditional expression

**Source:** `G09_02_brightness.cpp`. **Example:** M2.

### G09_02_A

Create `Brightness` with private `int level`. Its range is 0–100, including both endpoints. A no-argument constructor chooses 50. A one-value constructor keeps valid input and selects 50 otherwise. Provide `int get() const`.

Use a `?:` expression within the parameterized constructor's initializer list. Inno first explains M2 in detail; you then formulate the brightness condition. The starter contains no target condition.

**Reading order:** evaluate the condition before `?`. If true, the expression between `?` and `:` provides the result; otherwise the expression after `:` does. Only the selected branch is evaluated. Its result becomes the member's initial value. The colon following the constructor parameter list starts the initializer list; the inner colon separates the two alternatives.

Checks: -1 → 50, 0 → 0, 40 → 40, 100 → 100, 101 → 50. No-argument construction gives 50. Do not build complicated nested conditional expressions.

### G09_02_B

Implement `bool set(int newLevel)`. Valid values update state and return true. Invalid input returns false and preserves the previous state. main prints both success and the current queried value.

For an object starting at 40: set 70 → true/70; then 120 → false/70; 0 → true/0; 100 → true/100. Validate before assignment. The constructor fallback and setter rejection deliberately use different application policies; neither is automatic C++ repair.

## G09_03 – Parcel and rate calculator

**Source:** `G09_03_parcel.cpp`. **Example:** M3.

### G09_03_A

Create `Parcel` with private `int grams` and `bool express`, a two-parameter constructor and queries `int getGrams() const`, `bool isExpress() const`. Input is known to be valid, from 1 to 5000 whole grams.

`RateCalculator` has private `int base`, `int step`, `int surcharge`, initialized from its three constructor arguments. `int fee(Parcel shipment) const` uses the parcel's public queries instead of accessing its private members.

Fee: base charge + charge per started 500 grams + express surcharge if applicable. For positive whole grams, `(grams + 499) / 500` counts started units. Why? Values 1–500 give integer quotient 1, and 501–1000 give 2. This formula is explicitly explained processing, not a new mathematical discovery expected of the student.

For base 800, unit charge 300 and express surcharge 600: 450 g normal → 1100; 500 g normal → 1100; 501 g express → 2000.

### G09_03_B

Process the same 501 g express parcel with another calculator configured as 1000/200/400: the result is 1800. The parcel needs no modification. The calculator stores its own settings, giving this separate class a concrete purpose. Another processor could later use the same parcel to produce a shipping label.

The parcel parameter is passed by value, so the function receives a separate parameter object and only reads it. The calculator does not store the parcel as a data member; this is temporary cooperation rather than composition.

## G09_04 – Result sheet and composition

**Source:** `G09_04_result_sheet.cpp`. **Examples:** M4 and the array-element-construction part of M6. There is no need to re-examine M1.

### G09_04_A

Copy your own completed Competitor class from G09_01 into this separate source. Do not copy a second main function with it. Create `ResultSheet` with a private array of two Competitor objects.

Its constructor takes four ints: first bib and points, second bib and points. In the constructor body, assign parameterized Competitor objects to the array elements. Both array elements are already constructed by their default constructors before the body starts. Filling them in the body is subsequent assignment. This is why the no-argument Competitor constructor is needed too.

### G09_04_B

`int totalPoints() const` uses both objects' getPoints() queries. With 17/8 and 23/12, the total is 20. Inside an inner block, construct another sheet with 31/0 and 32/5: total 5. After the block, the first sheet still reports 20.

The second sheet's lifetime ends at the inner block's end. The outer sheet stays alive; do not access the expired sheet. No custom destructor or retained pointer is introduced.

The sheet contains competitors: composition. The next project contains an object array of tickets with a variable used count.
