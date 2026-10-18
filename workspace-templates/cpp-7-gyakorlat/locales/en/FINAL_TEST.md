# CPP_07 – Fixed final assessment

The tutor asks questions individually, in order. The first meaningful answer counts. Do not run the first five T2 programs before answering. Debugging code is for analysis; do not run the faulty union or out-of-bounds program before correcting it.

# T1 – 10 multiple-choice questions

## T1/1

Which is a characteristic of a structure?

A) It can contain only elements of the same type.

B) It groups named members whose types may differ.

C) It is always indexed numerically.

D) It can store only one member value at a time.

## T1/2

What does the declaration struct Measurement { int id; double value; }; create by itself?

A) One measurement with value 0.

B) Two separate global variables.

C) A type named Measurement, without a particular measurement object.

D) A function call.

## T1/3

What happens in Measurement copy = original; when copy is declared here for the first time?

A) A new object is created by copy-initialization.

B) The original object is destroyed.

C) Copy becomes another name for the original object.

D) Only the type name changes.

## T1/4

Which accesses the value member of the object pointed to by the structure pointer named pointer?

A) pointer.value

B) pointer[value]

C) &pointer.value

D) pointer->value

## T1/5

What does the parameter const Measurement* data mean?

A) The function cannot read any data.

B) The function cannot modify measurements through this pointer.

C) The element count is known automatically.

D) All measurements are guaranteed to be valid.

## T1/6

Which member do we read in the safe examples of a simple int/double union?

A) The currently active member.

B) Both members, in any order.

C) Always the first member, regardless of assignments.

D) Only the larger member.

## T1/7

What keeps a separate flag consistent with the active union member?

A) Cout fixes it automatically.

B) The union itself stores the correct flag value.

C) The program must set both consistently.

D) The include directive.

## T1/8

Where can an index declared in a for-loop header be used?

A) Throughout the program.

B) In every other function.

C) Only in the first statement after the loop.

D) In the loop condition, increment and body, but not after the loop.

## T1/9

Does a called function automatically access a local variable of its caller?

A) Yes, if the variable has the same name.

B) No; the value can be passed as a parameter, for example.

C) Yes, if both functions are void.

D) Only when the caller is main.

## T1/10

What happens to an outer object when an inner block declares a local variable with the same name?

A) It is destroyed immediately.

B) Its value automatically becomes 0.

C) It remains alive; the inner declaration hides its name from ordinary lookup.

D) It always becomes a pointer to the inner object.

# T2 – 5 output questions and 5 debugging questions

## T2/1 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;
struct Measurement { double value; };
int main() {
    Measurement original{8.0};
    Measurement copy = original;
    copy.value = 11.0;
    cout << original.value << " " << copy.value << '\n';
    return 0;
}
```

## T2/2 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;
struct Measurement { double value; };
Measurement increased(Measurement data) {
    data.value += 4.0;
    return data;
}
int main() {
    Measurement original{10.0};
    Measurement updated = increased(original);
    Measurement* pointer = &original;
    pointer->value += 3.0;
    cout << original.value << " " << updated.value << '\n';
    return 0;
}
```

## T2/3 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;
struct Measurement { double value; bool valid; };
int main() {
    Measurement data[3] = {{8.0, true}, {100.0, false}, {12.0, true}};
    double sum = 0.0;
    int count = 0;
    for (int i = 0; i < 3; ++i) {
        if (data[i].valid) {
            sum += data[i].value;
            ++count;
        }
    }
    cout << sum / count << '\n';
    return 0;
}
```

## T2/4 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;
union NumberValue { int integer; double real; };
int main() {
    NumberValue data{};
    data.integer = 4;
    cout << data.integer << " ";
    data.real = 1.5;
    cout << data.real << '\n';
    return 0;
}
```

## T2/5 – output

What is the exact output?

```cpp
#include <iostream>
using namespace std;
int number = 5;
void printValue() { cout << number << " "; }
int main() {
    int number = 10;
    {
        int number = 20;
        cout << number << " ";
        printValue();
    }
    cout << number << '\n';
    return 0;
}
```

## T2/6 – debugging

What is the main error, and what is the smallest correct fix? Do not assume successful compilation proves correctness.

```cpp
#include <iostream>
using namespace std;
struct Measurement {
    double value;
}
int main() {
    Measurement data{2.5};
    cout << data.value << '\n';
    return 0;
}
```

## T2/7 – debugging

What is the main error, and what is the smallest correct fix? Do not assume successful compilation proves correctness.

```cpp
#include <iostream>
using namespace std;
struct Measurement { double value; };
int main() {
    Measurement data{2.5};
    Measurement* pointer = &data;
    cout << pointer.value << '\n';
    return 0;
}
```

## T2/8 – debugging

What is the main error, and what is the smallest correct fix? Do not assume successful compilation proves correctness.

```cpp
#include <iostream>
using namespace std;
union NumberValue { int integer; double real; };
int main() {
    NumberValue data{};
    data.real = 2.5;
    cout << data.integer << '\n';
    return 0;
}
```

## T2/9 – debugging

What is the main error, and what is the smallest correct fix? Do not assume successful compilation proves correctness.

```cpp
#include <iostream>
using namespace std;
int main() {
    {
        int count = 3;
    }
    cout << count << '\n';
    return 0;
}
```

## T2/10 – debugging

What is the main error, and what is the smallest correct fix? Do not assume successful compilation proves correctness.

```cpp
#include <iostream>
using namespace std;
struct Measurement { double value; };
int main() {
    const int size = 2;
    Measurement data[size] = {{3.0}, {5.0}};
    double sum = 0.0;
    for (int i = 0; i <= size; ++i) {
        sum += data[i].value;
    }
    cout << sum << '\n';
    return 0;
}
```
