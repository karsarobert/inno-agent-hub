# CPP_08 v2 – Fixed final test

20 questions, one at a time. The first meaningful response counts. Do not run the first five T2 programs before answering. Debugging requires the cause and smallest intent-preserving fix. No student answer key is included.

# T1 – 10 multiple-choice questions

## T1/1

Which library quantity should be computed from the other two members?

A) ID from the copy count.

B) Borrowed count from the ID.

C) Available count from total minus borrowed.

D) A random new count for every query.

## T1/2

Which state satisfies 0 <= borrowed <= total?

A) Total 4, borrowed 4.

B) Total 2, borrowed 3.

C) Total -1, borrowed 0.

D) Total 5, borrowed -1.

## T1/3

Why should the caller handle initialization/update success?

A) A bool exists only after printing.

B) false automatically stops main.

C) cout corrects all failures.

D) After rejection, the caller must not assume the requested change happened.

## T1/4

When should a rejecting operation return false to preserve state?

A) Always after modifying.

B) Before assigning the data members.

C) Only after printing.

D) Only at the end of main.

## T1/5

Why can an area-calculating const member be called on a const shape?

A) const permits calculation without changing ordinary members.

B) const applies only to int.

C) All double fields are freely writable.

D) const removes data members.

## T1/6

Which statement is correct about a private data member?

A) Even the class’s own members cannot read it.

B) The object must be uncopyable.

C) main cannot access it directly, but a public member function may use it.

D) Its value is always zero.

## T1/7

What is a non-const object copied by value from a const object?

A) Another name for the same object.

B) An independent object that can be modified.

C) Always a compile error.

D) An automatically allocated dynamic pointer.

## T1/8

Which statement about class and struct access is correct?

A) struct can never contain member functions.

B) class cannot contain data members.

C) Both default to private.

D) class defaults to private, struct to public; both allow explicit labels.

## T1/9

What is also needed beside a const Book* parameter reading an array?

A) The full class text in every call.

B) The element count; the pointer does not store it.

C) Always a constructor name.

D) Only the first record’s count; that determines everything.

## T1/10

What does modifying an object parameter passed by value change by itself?

A) The function’s own parameter object.

B) Every object in the caller.

C) All future instances of the type.

D) Always the original array’s first element.

# T2 – 5 output and 5 debugging questions

## T2/1 – output

What is the exact output?

~~~cpp
#include <iostream>
using namespace std;

struct Route {
    int outward = 4;
    int inward = 6;
    int total() const {
        return outward + inward;
    }
};
int main() {
    Route first;
    const Route snapshot = first;
    first.inward = 9;
    cout << first.total() << ' ' << snapshot.total() << '\n';
    return 0;
}
~~~

## T2/2 – output

What is the exact output?

~~~cpp
#include <iostream>
using namespace std;

struct Switch {
    bool enabled = false;
    void toggle() {
        enabled = !enabled;
    }
    bool state() const {
        return enabled;
    }
};
int main() {
    Switch switcher;
    const Switch baseline = switcher;
    switcher.toggle();
    cout << switcher.state() << ' ' << baseline.state() << '\n';
    return 0;
}
~~~

## T2/3 – output

What is the exact output?

~~~cpp
#include <iostream>
using namespace std;

class StepCounter {
private:
    int value = 2;
public:
    bool advance(int amount) {
        if (amount <= 0 || amount > 3) {
            return false;
        }
        value += amount;
        return true;
    }
    int get() const {
        return value;
    }
};
int main() {
    StepCounter current;
    cout << current.advance(3) << ' ' << current.advance(4) << ' ' << current.get() << '\n';
    return 0;
}
~~~

## T2/4 – output

What is the exact output?

~~~cpp
#include <iostream>
using namespace std;

class Result {
private:
    int price = 0;
    bool active = false;
public:
    void set(int newPrice, bool newActive) {
        price = newPrice;
        active = newActive;
    }
    int effective() const {
        if (!active) {
            return 0;
        }
        return price;
    }
};
int main() {
    Result results[3];
    results[0].set(7, true);
    results[1].set(20, false);
    results[2].set(3, true);
    int sum = 0;
    for (int i = 0; i < 3; ++i) {
        sum += results[i].effective();
    }
    cout << sum << '\n';
    return 0;
}
~~~

## T2/5 – output

What is the exact output?

~~~cpp
#include <iostream>
using namespace std;

class Direction {
private:
    bool negative = false;
public:
    void reverse() {
        negative = !negative;
    }
    int sign() const {
        if (negative) {
            return -1;
        }
        return 1;
    }
};
Direction reversedCopy(Direction direction) {
    direction.reverse();
    return direction;
}
int main() {
    Direction original;
    Direction copy = reversedCopy(original);
    cout << original.sign() << ' ' << copy.sign() << '\n';
    Direction* pointer = &original;
    pointer->reverse();
    cout << original.sign() << ' ' << copy.sign() << '\n';
    return 0;
}
~~~

## T2/6 – debugging

Raise volume from 1 to 2 using a public operation while retaining data hiding. What is the main error and smallest correct fix?

~~~cpp
#include <iostream>
using namespace std;

class Volume {
private:
    int level = 1;
public:
    bool raiseOne() {
        if (level >= 3) {
            return false;
        }
        ++level;
        return true;
    }
    int get() const {
        return level;
    }
};
int main() {
    Volume volume;
    volume.level = 2;
    cout << volume.get() << '\n';
    return 0;
}
~~~

## T2/7 – debugging

Query whether the number in a const check object is even. What is the main error and smallest correct fix?

~~~cpp
#include <iostream>
using namespace std;

struct Check {
    int number = 2;
    bool isEven() {
        return number % 2 == 0;
    }
};
int main() {
    const Check check;
    cout << check.isEven() << '\n';
    return 0;
}
~~~

## T2/8 – debugging

Restart is intentionally a modifying operation that resets ticks to zero. What is the main error and smallest correct fix?

~~~cpp
#include <iostream>
using namespace std;

struct Wait {
    int ticks = 3;
    void restart() const {
        ticks = 0;
    }
};
int main() {
    Wait wait;
    wait.restart();
    cout << wait.ticks << '\n';
    return 0;
}
~~~

## T2/9 – debugging

Accept only positive reductions no greater than the current percentage. Rejection must preserve state. What is the main error and smallest correct fix?

~~~cpp
#include <iostream>
using namespace std;

class Percentage {
private:
    int percent = 100;
public:
    bool reduce(int reduction) {
        percent -= reduction;
        if (reduction <= 0 || percent < 0) {
            return false;
        }
        return true;
    }
    int get() const {
        return percent;
    }
};
int main() {
    Percentage percentage;
    cout << percentage.reduce(120) << ' ' << percentage.get() << '\n';
    return 0;
}
~~~

## T2/10 – debugging

Print the actual current number waiting at the stop, rather than the initial source input. What is the main error and smallest correct fix?

~~~cpp
#include <iostream>
using namespace std;

class Stop {
private:
    int waiting = 0;
public:
    void arrive(int amount) {
        waiting += amount;
    }
    int get() const {
        return waiting;
    }
};
int main() {
    const int sourceCount = 2;
    Stop stop;
    stop.arrive(sourceCount);
    stop.arrive(3);
    cout << sourceCount << '\n';
    return 0;
}
~~~
