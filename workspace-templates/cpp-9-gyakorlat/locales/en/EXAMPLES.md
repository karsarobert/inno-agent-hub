# CPP_09 – Explained analogous examples

Every program runs independently. Inno also shows the relevant example in chat, explains it and identifies the difference from your task. These are not a target solution split into pieces. An already understood example need not be re-examined at every later step.

## M1 – Three ways to construct a segment

```cpp
#include <iostream>
using namespace std;


class Segment {
private:
    int start;
    int end;
public:
    Segment() : start(0), end(0) {}
    Segment(int length) : start(0), end(length) {}
    Segment(int newStart, int newEnd) : start(newStart), end(newEnd) {}
    int length() const { return end - start; }
};
int main() {
    const Segment initial;
    const Segment single(6);
    const Segment full(3, 11);
    cout << initial.length() << ' ' << single.length() << ' ' << full.length() << '\n';
    return 0;
}
```

Output:

```text
0 6 8
```

A no-argument segment starts at 0/0, the one-argument form starts at 0 and ends at the supplied length, and the two-argument form uses both endpoints. Length is a computed query rather than another stored member. The three calls select three parameter lists. The competitor task queries two stored values instead of computing an endpoint difference.

## M2 – Selecting direction with a conditional expression

```cpp
#include <iostream>
using namespace std;


class Direction {
private:
    int sign;
public:
    Direction(int input) : sign(input < 0 ? -1 : 1) {}
    int getSign() const { return sign; }
};
int main() {
    const Direction left(-4);
    const Direction right(7);
    const Direction initial(0);
    cout << left.getSign() << ' ' << right.getSign() << ' ' << initial.getSign() << '\n';
    return 0;
}
```

Output:

```text
-1 1 1
```

The input < 0 condition selects the initial sign: -1 when true and 1 otherwise. Zero deliberately chooses 1 here. Only the selected branch is evaluated. Its value feeds sign(...) before the constructor body. Brightness makes a different decision: check an entire valid range and choose 50 for invalid input. The student writes that range condition.

## M3 – Document and printer cooperation

```cpp
#include <iostream>
using namespace std;


class Document {
private:
    int pages;
    bool color;
public:
    Document(int newPages, bool newColor) : pages(newPages), color(newColor) {}
    int getPages() const { return pages; }
    bool isColor() const { return color; }
};
class Printer {
private:
    int perPage;
    int colorExtra;
public:
    Printer(int value, int surcharge) : perPage(value), colorExtra(surcharge) {}
    int cost(Document document) const {
        int unitPrice = perPage;
        if (document.isColor()) { unitPrice += colorExtra; }
        return document.getPages() * unitPrice;
    }
};
int main() {
    const Document document(3, true);
    const Printer printer(10, 30);
    cout << printer.cost(document) << '\n';
    return 0;
}
```

Output:

```text
120
```

Document stores page count and color status. Printer stores the per-page charge and per-color-page surcharge, and cost uses document queries. The value parameter is a separate copy. Three color pages cost 3 × (10 + 30) = 120. Postal pricing differs: base charge, started 500-gram units and a per-parcel express surcharge. Renaming alone cannot solve that task.

## M4 – Direct initialization of member objects

```cpp
#include <iostream>
using namespace std;


class Point {
private:
    int x;
    int y;
public:
    Point(int newX, int newY) : x(newX), y(newY) {}
    int getX() const { return x; }
    int getY() const { return y; }
};
class Span {
private:
    Point left;
    Point right;
public:
    Span(int start, int end) : left(start, 0), right(end, 0) {}
    int sumX() const { return left.getX() + right.getX(); }
};
int main() {
    const Span span(2, 8);
    cout << span.sumX() << '\n';
    return 0;
}
```

Output:

```text
10
```

Span contains two Point objects. The left(start, 0) and right(end, 0) initializers call Point constructors. This matters because Point has no no-argument constructor: assignment in the body would be too late for initial construction. Competitor does have a default constructor, so its array can be constructed first and filled later. sumX is simply the two x coordinates added, not a geometric area.

## M5 – Validity of a die roll

```cpp
#include <iostream>
using namespace std;


class Roll {
private:
    int face;
public:
    Roll() : face(0) {}
    Roll(int newFace) : face(0) {
        if (newFace >= 1 && newFace <= 6) { face = newFace; }
    }
    bool isValid() const { return face >= 1 && face <= 6; }
    bool isEven() const { return isValid() && face % 2 == 0; }
};
int main() {
    const Roll first(4);
    const Roll second(9);
    cout << first.isValid() << ' ' << first.isEven() << '\n';
    cout << second.isValid() << ' ' << second.isEven() << '\n';
    return 0;
}
```

Output:

```text
1 1
0 0
```

Zero means no roll yet; only 1–6 are valid. The constructor initializes the member to 0, then assigns valid input in the body. isEven checks validity as well as remainder, so zero is not treated as a valid even roll. Ticket must instead handle two related members and a row-dependent price; this die example does not solve that target.

## M6 – Object array inside an indicator panel

```cpp
#include <iostream>
using namespace std;


class Indicator {
private:
    bool enabled;
public:
    Indicator() : enabled(false) {}
    void enable() { enabled = true; }
    bool isEnabled() const { return enabled; }
};
class IndicatorPanel {
private:
    Indicator lamps[2];
public:
    bool enable(int index) {
        if (index < 0 || index >= 2) { return false; }
        lamps[index].enable();
        return true;
    }
    void list() const {
        for (int i = 0; i < 2; ++i) { cout << lamps[i].isEnabled() << ' '; }
        cout << '\n';
    }
};
int main() {
    IndicatorPanel panel;
    panel.list();
    cout << panel.enable(1) << '\n';
    panel.list();
    cout << panel.enable(2) << '\n';
    return 0;
}
```

Output:

```text
0 0 
1
0 1 
0
```

Constructing the panel default-constructs both Indicator objects, initially off. Check the index before accessing the array. This panel always uses two lamps, so its listing visits both. The box office instead starts with used count 0 and traverses only its active prefix. The panel contains no ticket-adding or seat-search solution.

## M7 – Searching and the matching index

```cpp
#include <iostream>
using namespace std;


int main() {
    const int values[4] = {4, 8, 12, 16};
    const int selected = 12;
    int found = -1;
    for (int i = 0; i < 4; ++i) {
        if (values[i] == selected) { found = i; break; }
    }
    // An index is different from the stored value.
    cout << found << '\n';
    return 0;
}
```

Output:

```text
2
```

Minus one denotes no match. On success the loop stores the position, not the matching value 12, and break exits the loop. The index here is 2. Booking search compares two members together and visits only actual tickets instead of full capacity. Cancellation may use the index only after a successful search.

## M8 – Removing a known position from an array

```cpp
#include <iostream>
using namespace std;


int main() {
    int values[5] = {10, 20, 30, 40, 50};
    int size = 5;
    const int removedPosition = 2;
    // Move the entries after the match one position left.
    for (int i = removedPosition; i < size - 1; ++i) { values[i] = values[i + 1]; }
    --size;
    for (int i = 0; i < size; ++i) { cout << values[i] << ' '; }
    cout << '\n';
    return 0;
}
```

Output:

```text
10 20 40 50 
```

Index 2 holds 30. The loop moves 40 and then 50 one position left; i + 1 must still be active, hence i < size - 1. The used size decreases afterwards. The old 50 in the last physical slot falls outside the active range. In the project, you must first find a row–seat pair, handle absence and shift whole Ticket objects.

## M9 – Computing a total from source data

```cpp
#include <iostream>
using namespace std;


int main() {
    const int quantity[3] = {2, 1, 4};
    const int unitPrice[3] = {100, 250, 50};
    int amount = 0;
    for (int i = 0; i < 3; ++i) { amount += quantity[i] * unitPrice[i]; }
    cout << amount << '\n';
    return 0;
}
```

Output:

```text
650
```

The total starts at 0 and adds quantity × unit price for each item: 200 + 250 + 200 = 650. The final result is not hard-coded. In the box office, a member query supplies each ticket price and only count active tickets contribute. Three is the actually used item count in this example; do not replace it mechanically with the box-office capacity.

## M10 – Returning text from a business card

```cpp
#include <sstream>
#include <string>
#include <iostream>
using namespace std;


class Card {
private:
    string name;
    int postalCode;
public:
    Card(string newName, int newPostalCode) : name(newName), postalCode(newPostalCode) {}
    string getName() const { return name; }
    int getPostalCode() const { return postalCode; }
};
string label(const Card* card) {
    // The stream builds text; str() returns a string value.
    ostringstream text;
    text << card->getName() << " (" << card->getPostalCode() << ")";
    return text.str();
}
int main() {
    const Card card("Anna", 7624);
    cout << label(&card) << '\n';
    return 0;
}
```

Output:

```text
Anna (7624)
```

label receives an existing Card address through a const pointer and calls public queries with the arrow. A local ostringstream builds text in memory. Its str() result is returned as a string value, so destruction of the local stream does not invalidate the returned text. main prints it to cout. The box-office summary uses a different type, different queries and count/value content.
