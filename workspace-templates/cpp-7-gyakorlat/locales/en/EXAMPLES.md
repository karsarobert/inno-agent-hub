# CPP_07 – Analogous example programs

These examples are not completed measurement-task solutions. They use different names and data. Each can be compiled as a separate program. Inno should show and explain only the current example, not the entire collection at once.

## M1 – Types, objects and copying

```cpp
#include <iostream>
using namespace std;

struct Product {
    int code;
    double price;
    bool available;
};

int main() {
    Product first{12, 450.0, true};
    Product second = first; // Initialize a new object.
    second.price = 500.0;
    cout << first.price << " " << second.price << '\n';
    second = first;        // Assignment to an existing object.
    cout << first.price << " " << second.price << '\n';
    return 0;
}
```

Expected output:

```text
450 500
450 450
```

The type describes three members. Two separate objects are created; changing the second price does not change the first. The later assignment copies the first object's member values back.

## M2 – Structure parameters and returning a structure

```cpp
#include <iostream>
using namespace std;
struct Point {
    int x;
    int y;
};

Point shifted(Point position, int step) {
    position.x += step; // Modify our own parameter object.
    return position;    // Return a complete structure value.
}

int main() {
    Point original{1, 2};
    Point updated = shifted(original, 5);
    cout << original.x << " " << updated.x << '\n';
    return 0;
}
```

Expected output:

```text
1 6
```

The return type is Point. The position parameter is a separate object that the function modifies. The original point stays unchanged, while the returned value initializes the new point.

## M3 – Modifying an original through a pointer

```cpp
#include <iostream>
using namespace std;
struct Item {
    double price;
};

void applyDiscount(Item* item, double sum) {
    item->price -= sum; // The pointed-to object changes.
}

int main() {
    Item product{100.0};
    applyDiscount(&product, 10.0);
    cout << product.price << '\n';
    return 0;
}
```

Expected output:

```text
90
```

The function receives the product's address. The arrow selects a member of the pointed-to object. The original price changes, rather than the value of an independent copy.

## M4 – Tracking a union alternative with a flag

```cpp
#include <iostream>
using namespace std;
union SettingData {
    int level;
    double ratio;
};
struct Setting {
    bool usesLevel;
    SettingData data;
};

void displaySetting(Setting setting) {
    if (setting.usesLevel) {
        cout << setting.data.level << '\n';
    } else {
        cout << setting.data.ratio << '\n';
    }
}

int main() {
    Setting setting{};
    setting.data.level = 3;
    setting.usesLevel = true;
    displaySetting(setting);
    setting.data.ratio = 0.75;
    setting.usesLevel = false;
    displaySetting(setting);
    return 0;
}
```

Expected output:

```text
3
0.75
```

The union alternatives share storage. A separate structure flag records the selected alternative. Update the flag when switching members; output reads only the matching member.

## M5 – Name lookup and an inner block

```cpp
#include <iostream>
using namespace std;
int score = 3;
void display() { cout << score << '\n'; }

int main() {
    int score = 8;
    {
        int score = 12; // A separate object with the same name.
        cout << score << '\n';
    }
    cout << score << '\n';
    cout << ::score << '\n'; // Qualify the global name.
    display();
    return 0;
}
```

Expected output:

```text
12
8
3
3
```

The inner name denotes 12; after that block, main's local 8 is accessible again. The expression ::score accesses the global 3 directly. The display function also sees the global 3: calling it does not make main's local variable visible inside it.

## M6 – Nested data and printing by value

```cpp
#include <iostream>
using namespace std;
struct Position {
    int row;
    int column;
};
struct Package {
    int code;
    Position position;
};

void display(Package package) {
    cout << package.code << ": " << package.position.row << ", "
         << package.position.column << '\n';
}

int main() {
    Package box{7, {2, 4}};
    display(box);
    return 0;
}
```

Expected output:

```text
7: 2, 4
```

The position member is itself a structure. The expression package.position.row first selects a position and then its row. The void function takes a package by value and prints its data.

## M7 – Traversing structures with an existing function

```cpp
#include <iostream>
using namespace std;
struct StockItem {
    int code;
    int stock;
};

void printItem(StockItem entry) {
    cout << entry.code << ": " << entry.stock << '\n';
}

void listItems(const StockItem* items, int count) {
    for (int i = 0; i < count; ++i) {
        printItem(items[i]);
    }
}

int main() {
    StockItem items[2] = {{11, 3}, {12, 8}};
    listItems(items, 2);
    return 0;
}
```

Expected output:

```text
11: 3
12: 8
```

The function receives a pointer and a separate count. The loop selects a complete element and passes it to the existing printing function. The const qualifier prevents changing array elements through this pointer.

## M8 – Conditional counting

```cpp
#include <iostream>
using namespace std;
struct Exam {
    int score;
    bool attended;
};

int countPassing(const Exam* exams, int count, int minimum) {
    int result = 0;
    for (int i = 0; i < count; ++i) {
        if (exams[i].attended && exams[i].score >= minimum) {
            ++result;
        }
    }
    return result;
}

int main() {
    Exam exams[3] = {{60, true}, {90, false}, {80, true}};
    cout << countPassing(exams, 3, 60) << '\n';
    return 0;
}
```

Expected output:

```text
2
```

The counter starts at zero and && combines two conditions. Project P3 needs only the validity condition. P5 needs two conditions but requires strictly greater, unlike this example's greater-than-or-equal comparison.

## M9 – Averages and zero elements

```cpp
#include <iostream>
using namespace std;

double averagePrices(const double* prices, int count) {
    double sum = 0.0;
    for (int i = 0; i < count; ++i) {
        sum += prices[i];
    }
    return sum / count; // Precondition: count is positive.
}

int main() {
    const int count = 2;
    double prices[count] = {10.0, 15.0};
    if (count > 0) {
        cout << averagePrices(prices, count) << '\n';
    } else {
        cout << "No data." << '\n';
    }
    return 0;
}
```

Expected output:

```text
12.5
```

A double sum preserves the fractional part. The caller checks that the count is positive. In the project, invalid records must also be filtered out: divide by the valid count, not by the entire array size.
