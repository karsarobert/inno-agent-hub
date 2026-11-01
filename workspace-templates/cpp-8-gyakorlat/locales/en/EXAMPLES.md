# CPP_08 v2 – Analogous examples

Show and explain only the current example. These are not solutions to the student tasks. Always identify how the application differs. Each program compiles independently.

## M1 – Member function and persistent state

~~~cpp
#include <iostream>
using namespace std;

struct Signal {
    int value = 2;
    int step = 3;

    void advance() {
        // Only this object changes.
        value += step;
    }

    int nextValue() {
        return value + step;
    }
};

int main() {
    Signal signal;
    cout << signal.nextValue() << '\n';
    signal.advance();
    cout << signal.nextValue() << '\n';
    return 0;
}
~~~

Expected output:

~~~text
5
8
~~~

The query computes a next value, while advance stores a new state. The duration task requires different calculations: division and remainder.

## M2 – Const calculation and independent copy

~~~cpp
#include <iostream>
using namespace std;

struct Shipment {
    int goods = 4;
    int packaging = 1;

    void setGoods(int newGoods) {
        goods = newGoods;
    }

    int grossWeight() const {
        // Read the members; leave both unchanged.
        return goods + packaging;
    }
};

int main() {
    Shipment shipment;
    const Shipment baseline = shipment;
    shipment.setGoods(8);
    cout << baseline.grossWeight() << ' ' << shipment.grossWeight() << '\n';
    return 0;
}
~~~

Expected output:

~~~text
5 9
~~~

The fixed copy keeps its total while the original changes. The rectangle requires two different formulas, rather than adding weights.

## M3 – Private coordinates and object copying

~~~cpp
#include <iostream>
using namespace std;

class Position {
private:
    int x = 0;
    int y = 0;

public:
    void place(int newX, int newY) {
        x = newX;
        y = newY;
    }

    bool atOrigin() const {
        return x == 0 && y == 0;
    }
};

int main() {
    Position first;
    Position second;
    second.place(2, 3);
    Position copy = first;
    copy.place(1, 0);
    cout << first.atOrigin() << ' ' << second.atOrigin() << ' ' << copy.atOrigin() << '\n';
    copy = first;
    cout << copy.atOrigin() << '\n';
    return 0;
}
~~~

Expected output:

~~~text
1 0 0
1
~~~

main uses operations instead of writing coordinate fields. The lamp requires different state and a different Boolean condition.

## M4 – Reject before changing state

~~~cpp
#include <iostream>
using namespace std;

class BoardPosition {
private:
    int x = 1;
    int y = 2;

public:
    bool move(int dx, int dy) {
        const int newX = x + dx;
        const int newY = y + dy;
        // Check before changing either member.
        if (newX < 0 || newY < 0) {
            return false;
        }
        x = newX;
        y = newY;
        return true;
    }

    void print() const {
        cout << x << ' ' << y << '\n';
    }
};

int main() {
    BoardPosition position;
    cout << position.move(-2, 0) << '\n';
    position.print();
    cout << position.move(2, 1) << '\n';
    position.print();
    return 0;
}
~~~

Expected output:

~~~text
0
1 2
1
3 3
~~~

Computing candidate coordinates does not yet alter the object. The tank needs conditions based on capacity and current contents; borrowing depends on available copies.

## M5 – Validating two related values

~~~cpp
#include <iostream>
using namespace std;

class Interval {
private:
    int start = 0;
    int end = 0;

public:
    bool record(int newStart, int newEnd) {
        if (newStart < 0 || newEnd < newStart) {
            return false;
        }
        start = newStart;
        end = newEnd;
        return true;
    }

    int length() const {
        return end - start;
    }
};

int main() {
    Interval interval;
    cout << interval.record(3, 8) << ' ' << interval.length() << '\n';
    cout << interval.record(9, 4) << ' ' << interval.length() << '\n';
    return 0;
}
~~~

Expected output:

~~~text
1 5
0 5
~~~

The rule checks the relationship between values, not just their signs. Book stock has a different relationship: borrowed copies cannot exceed the total.

## M6 – Reading an object array

~~~cpp
#include <iostream>
using namespace std;

class Beacon {
private:
    int frequency = 0;
    bool enabled = false;

public:
    void configure(int newFrequency, bool newEnabled) {
        frequency = newFrequency;
        enabled = newEnabled;
    }

    int getFrequency() const {
        return frequency;
    }

    bool isEnabled() const {
        return enabled;
    }
};

void printAll(const Beacon* beacons, int size) {
    // Size is supplied separately from the pointer.
    for (int i = 0; i < size; ++i) {
        if (beacons[i].isEnabled()) {
            cout << beacons[i].getFrequency() << '\n';
        }
    }
}

int main() {
    Beacon beacons[3];
    beacons[0].configure(10, true);
    beacons[1].configure(20, false);
    beacons[2].configure(30, true);
    printAll(beacons, 3);
    return 0;
}
~~~

Expected output:

~~~text
10
30
~~~

The const pointer gives read-only access and size is separate. The library must print every record and initialize through validated operations.

## M7 – A free processing function

~~~cpp
#include <iostream>
using namespace std;

class Task {
private:
    int points = 0;
    bool done = false;

public:
    void set(int newPoints, bool newDone) {
        points = newPoints;
        done = newDone;
    }

    int getPoints() const {
        return points;
    }

    bool isDone() const {
        return done;
    }
};

int largestDone(const Task* tasks, int size) {
    int best = 0;
    for (int i = 0; i < size; ++i) {
        if (tasks[i].isDone() && tasks[i].getPoints() > best) {
            best = tasks[i].getPoints();
        }
    }
    return best;
}

int main() {
    Task tasks[3];
    tasks[0].set(4, true);
    tasks[1].set(20, false);
    tasks[2].set(7, true);
    cout << largestDone(tasks, 3) << '\n';
    return 0;
}
~~~

Expected output:

~~~text
7
~~~

The example assumes nonnegative points and finds a maximum among completed tasks. Library processing instead needs addition and conditional counting.

## M8 – By-value parameter and original object

~~~cpp
#include <iostream>
using namespace std;

class Marker {
private:
    int position = 0;

public:
    void offset(int distance) {
        position += distance;
    }

    int getPosition() const {
        return position;
    }
};

Marker shiftedCopy(Marker current, int distance) {
    // This parameter is an independent copy.
    current.offset(distance);
    return current;
}

void shiftOriginal(Marker* current, int distance) {
    // Call a public member through the pointer.
    current->offset(distance);
}

int main() {
    Marker original;
    Marker copy = shiftedCopy(original, 4);
    shiftOriginal(&original, -2);
    cout << original.getPosition() << ' ' << copy.getPosition() << '\n';
    return 0;
}
~~~

Expected output:

~~~text
-2 4
~~~

The value parameter is a copy; the pointer accesses an existing object. Book borrowing additionally requires handling a Boolean result and rejected requests.

## M9 – Searching with a returned index

~~~cpp
#include <iostream>
using namespace std;

class Parcel {
private:
    int code = 0;

public:
    void setCode(int newCode) {
        code = newCode;
    }

    bool matches(int requested) const {
        return code == requested;
    }
};

int indexOf(const Parcel* parcels, int size, int requested) {
    for (int i = 0; i < size; ++i) {
        if (parcels[i].matches(requested)) {
            return i;
        }
    }
    return -1;
}

int main() {
    Parcel parcels[2];
    parcels[0].setCode(41);
    parcels[1].setCode(72);
    cout << indexOf(parcels, 2, 72) << ' ' << indexOf(parcels, 2, 99) << '\n';
    return 0;
}
~~~

Expected output:

~~~text
1 -1
~~~

An index is a position, not an ID. -1 means no matching element; never use it to access the array. This example is needed only for optional X1.
