# CPP_05 – Midterm Preparation Final Test

The tutor asks the questions **one at a time**, in the exact order shown here. The questions
are pre-written; do not replace them with different tasks.

# T1 – 10 multiple-choice questions from today's theory

## T1/1
What is one of the most important advantages of splitting a program into functions?

A) Every variable automatically becomes global.  
B) Code repetition can be reduced, and subproblems can be handled separately.  
C) A program can have several `main()` functions.  
D) The program always becomes automatically faster.

## T1/2
What do we call a **parameter**?

A) An input variable written in the function definition.  
B) A concrete value passed during a function call.  
C) The value returned by `return`.  
D) The function's local result.

## T1/3
What do we call an **argument**?

A) The function's return type.  
B) The parameter name written in the function definition.  
C) A concrete value or expression passed during a function call.  
D) Only an integer can be an argument.

## T1/4
What is the role of `return` in a function that returns a value?

A) It prints the result on the screen.  
B) It returns a value to the calling code and ends that function call.  
C) It restarts the function.  
D) It can only be used in `main()`.

## T1/5
What does the `void` return type mean?

A) The function does not return a value.  
B) The function cannot have parameters.  
C) The function cannot contain an `if` statement or a loop.  
D) The function cannot be called from `main()`.

## T1/6
What happens when a simple `int` variable is passed by value?

A) The parameter becomes the same object as the original variable.  
B) The function automatically receives the variable's address.  
C) The parameter receives a copy of the argument's value.  
D) The argument becomes `const`.

## T1/7
What is a function prototype used for?

A) It tells the compiler the function's name, return type, and parameter types in advance.  
B) It runs the function before `main()`.  
C) It always replaces the function definition.  
D) It allocates memory for the function result.

## T1/8
Which statement is true about a local variable in a function?

A) It can be accessed directly from every function in the program.  
B) It is only accessible within the scope where it was created.  
C) It is always `static`.  
D) It can only be an array.

## T1/9
Which statement correctly describes the relationship between `#include <iostream>` and `using namespace std;`?

A) They do exactly the same thing.  
B) `#include <iostream>` makes the I/O declarations available; `using namespace std;` allows name lookup to find names from `std`, so we may write `cout` instead of `std::cout`.  
C) `using namespace std;` loads the `<iostream>` header.  
D) `<iostream>` is the name of a namespace.

## T1/10
Why might a program contain `#include <cmath>`?

A) It is required for every `for` loop.  
B) It defines the `main()` function.  
C) It makes declarations for standard mathematical functions such as `sqrt` available.  
D) It is used instead of `using namespace std;`.

# T2 – 10 code-understanding and debugging tasks

## T2/1 – Output prediction
What is the exact output?

```cpp
#include <iostream>
using namespace std;

int doubleValue(int number) {
    return number * 2;
}

int main() {
    cout << doubleValue(4) + doubleValue(3) << '\n';
    return 0;
}
```

## T2/2 – Output prediction
What is the exact output?

```cpp
#include <iostream>
using namespace std;

void modify(int number) {
    number = 100;
}

int main() {
    int value = 10;
    modify(value);
    cout << value << '\n';
    return 0;
}
```

## T2/3 – Output prediction
What is the exact output?

```cpp
#include <iostream>
using namespace std;

int square(int x) {
    return x * x;
}

int sumOfSquares(int a, int b) {
    return square(a) + square(b);
}

int main() {
    cout << sumOfSquares(3, 4) << '\n';
    return 0;
}
```

## T2/4 – Output prediction
What is the exact output?

```cpp
#include <iostream>
using namespace std;

int sum(const int* data, int size) {
    int result = 0;
    for (int i = 0; i < size; ++i) {
        result += data[i];
    }
    return result;
}

int main() {
    int numbers[4] = {2, 5, 3, 10};
    cout << sum(numbers, 4) << '\n';
    return 0;
}
```

## T2/5 – Output prediction
What is the exact output?

```cpp
#include <iostream>
using namespace std;

void increment(int* value) {
    *value += 1;
}

int main() {
    int x = 5;
    increment(&x);
    cout << x << '\n';
    return 0;
}
```

## T2/6 – Debugging
The program does not compile in this form. What is the main problem, and what is the smallest fix?

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << add(2, 3) << '\n';
    return 0;
}

int add(int a, int b) {
    return a + b;
}
```

## T2/7 – Debugging
What is wrong with this function?

```cpp
void add(int a, int b) {
    return a + b;
}
```

## T2/8 – Debugging
The program does not compile. Why?

```cpp
#include <iostream>
using namespace std;

int area(int a, int b) {
    return a * b;
}

int main() {
    cout << area(4) << '\n';
    return 0;
}
```

## T2/9 – Debugging
The program may compile, but the loop is incorrect and unsafe. What is the problem?

```cpp
#include <iostream>
using namespace std;

int sum(const int* data, int size) {
    int result = 0;

    for (int i = 0; i <= size; ++i) {
        result += data[i];
    }

    return result;
}
```

## T2/10 – Debugging
The code includes `<iostream>`, but `cout` still cannot be used like this. What is missing, or what must be changed?

```cpp
#include <iostream>

int main() {
    cout << "Hello!" << '\n';
    return 0;
}
```
