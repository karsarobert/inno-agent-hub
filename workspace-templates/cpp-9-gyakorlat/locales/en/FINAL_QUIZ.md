# CPP_09 – Fixed final quiz

20 questions, presented one at a time. The first substantive answer counts. Answer A/B/C/D in T1. Do not run T2/1–5 before answering. T2/6–10 require the cause and the smallest fix preserving the stated goal. No answer key is included in the student package.

## T1/1

Which declaration is a constructor in class Window?

A) void Window(int width);

B) Window(int width);

C) int Window(int width);

D) bool window(int width);

## T1/2

There is a no-argument constructor and a constructor with two int parameters. Which is selected by Machine machine(4, 7);?

A) Always the no-argument one.

B) First the no-argument one, then separately the two-parameter one.

C) Either, depending on a choice made inside main.

D) The constructor taking two int parameters.

## T1/3

What does number(7) mean in the constructor Option() : number(7) {}?

A) Initializing the number member before executing the body.

B) Calling a free function named number.

C) Assignment at the end of the constructor.

D) Creating seven separate objects.

## T1/4

Members are declared as Member first; followed by Member second;. Which is initialized first if the initializer list says second(...), first(...)?

A) second, because it appears first in the list.

B) Whichever receives more arguments.

C) first, because member declaration order controls initialization.

D) The compiler randomly changes this on each run.

## T1/5

Which statement about condition ? leftValue : rightValue is correct?

A) After the condition, only the selected branch is evaluated.

B) Both branches are always evaluated.

C) Its result is always bool.

D) It can only be used with cout.

## T1/6

Why may a constructor choose a fallback for invalid input while a later setter rejects it and preserves the previous value?

A) C++ automatically zeroes all invalid constructor input.

B) A setter cannot read private data.

C) A bool result automatically undoes modifications.

D) They are different application policies for establishing initial state and updating existing state.

## T1/7

A rate calculator calls the parcel getGrams() query. What is the benefit?

A) This eliminates every object copy.

B) The calculation uses the public interface without accessing storage details.

C) The private member automatically becomes public.

D) Both classes must store the same data members.

## T1/8

Which case is composition?

A) A local int variable in a function adds two numbers.

B) Two class names start with the same letter.

C) ResultSheet contains Competitor objects as data members.

D) A free function prints a received number.

## T1/9

A storage array has capacity four and count = 2. Which indices belong to the current listing and total?

A) 0, 1, 2, 3, because all array elements were constructed.

B) 0 and 1.

C) 1 and 2.

D) Only index 2.

## T1/10

What does access through const BoxOffice* allow?

A) Calling suitable const queries on the existing object.

B) Directly modifying the private count.

C) Calling all modifying operations.

D) Automatically copying the object at every arrow operator.

## T2/1 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Job {
private:
    int duration;
public:
    Job() : duration(2) {}
    Job(int newDuration) : duration(newDuration) {}
    int getDuration() const { return duration; }
};
int main() {
    const Job first;
    const Job second(7);
    cout << first.getDuration() << ' ' << second.getDuration() << '\n';
    return 0;
}
```

## T2/2 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Window {
private:
    int number;
public:
    Window(int input) : number(input > 0 ? input : 3) {}
    int getNumber() const { return number; }
};
int main() {
    const Window first(0);
    const Window second(5);
    cout << first.getNumber() << ' ' << second.getNumber() << '\n';
    return 0;
}
```

## T2/3 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Job {
private:
    int duration;
public:
    Job(int newDuration) : duration(newDuration) {}
    int getDuration() const { return duration; }
};
class Machine {
private:
    int quantity;
public:
    Machine(int newNumber) : quantity(newNumber) {}
    int total(Job job) const { return job.getDuration() * quantity; }
};
int main() {
    const Job job(6);
    const Machine machine(3);
    cout << machine.total(job) << '\n';
    return 0;
}
```

## T2/4 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Entry {
private:
    int number;
public:
    Entry() : number(2) {}
    Entry(int newNumber) : number(newNumber) {}
    int getNumber() const { return number; }
};
class Container {
private:
    Entry values[3];
    int active;
public:
    Container() : active(1) { values[0] = Entry(9); }
    int total() const {
        int result = 0;
        for (int i = 0; i < active; ++i) { result += values[i].getNumber(); }
        return result;
    }
};
int main() {
    const Container container;
    cout << container.total() << '\n';
    return 0;
}
```

## T2/5 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Option {
private:
    int number;
public:
    Option(int input) : number(input) {}
    void setValue(int newNumber) { number = newNumber; }
    int getNumber() const { return number; }
};
Option extend(Option option) {
    option.setValue(option.getNumber() + 2);
    return option;
}
int main() {
    Option original(4);
    const Option copy = extend(original);
    cout << original.getNumber() << ' ' << copy.getNumber() << '\n';
    Option* target = &original;
    target->setValue(9);
    cout << original.getNumber() << ' ' << copy.getNumber() << '\n';
    return 0;
}
```

## T2/6 – debugging

The goal is to query 7 after constructing a Window. What is the main error and the smallest fix?

```cpp
#include <iostream>
using namespace std;

class Window {
private:
    int number = 2;
public:
    void Window() { number = 7; }
    int getNumber() const { return number; }
};
int main() {
    const Window window;
    cout << window.getNumber() << '\n';
    return 0;
}
```

## T2/7 – debugging

Both array entries should initially have duration 0; parameterized construction must remain available. Why is the program invalid and how would you fix it?

```cpp
#include <iostream>
using namespace std;

class Job {
private:
    int duration;
public:
    Job(int newDuration) : duration(newDuration) {}
    int getDuration() const { return duration; }
};
int main() {
    Job jobs[2];
    cout << jobs[0].getDuration() << ' ' << jobs[1].getDuration() << '\n';
    return 0;
}
```

## T2/8 – debugging

Construct the Member directly with the received value. Do not add a default constructor to Member. Why is assignment inside the body insufficient?

```cpp
#include <iostream>
using namespace std;

class Member {
private:
    int number;
public:
    Member(int input) : number(input) {}
    int getNumber() const { return number; }
};
class Container {
private:
    Member member;
public:
    Container(int input) { member = Member(input); }
    int getNumber() const { return member.getNumber(); }
};
int main() {
    const Container container(6);
    cout << container.getNumber() << '\n';
    return 0;
}
```

## T2/9 – debugging

The goal is the total of active entries only. Every array element is initialized; this is not a compilation-error question. What is wrong and what is the smallest fix?

```cpp
#include <iostream>
using namespace std;

class Container {
private:
    int values[3] = {10, 2, 2};
    int active = 1;
public:
    int total() const {
        int result = 0;
        for (int i = 0; i < 3; ++i) { result += values[i]; }
        return result;
    }
};
int main() {
    const Container container;
    cout << container.total() << '\n';
    return 0;
}
```

## T2/10 – debugging

Only nonnegative values are allowed. Rejection must preserve the previous value. What is the main error and the smallest fix?

```cpp
#include <iostream>
using namespace std;

class Option {
private:
    int number;
public:
    Option(int input) : number(input) {}
    bool setValue(int newNumber) {
        number = newNumber;
        if (newNumber < 0) { return false; }
        return true;
    }
    int getNumber() const { return number; }
};
int main() {
    Option option(5);
    cout << option.setValue(-1) << ' ' << option.getNumber() << '\n';
    return 0;
}
```
