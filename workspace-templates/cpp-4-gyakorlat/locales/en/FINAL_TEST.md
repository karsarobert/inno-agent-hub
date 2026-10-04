# CPP_04 – Final Test

The tutor presents this test one question at a time. Do not read it in advance as a solution sheet; the goal is to answer from your own understanding after the coding practice.

## T1 – Multiple-choice questions

### 1.
An array with five elements is declared as follows:

```cpp
int numbers[5] = {10, 20, 30, 40, 50};
```

What is the last valid index?

A) `5`  
B) `1`  
C) `4`  
D) `0`

### 2.
What does the expression `&number` produce?

```cpp
int number = 42;
```

A) The value of `number`.  
B) The address of the memory location of `number`.  
C) The type of `number`.  
D) A copy of the value of `number`.

### 3.
What does the variable `pointer` store?

```cpp
int number = 42;
int* pointer = &number;
```

A) The value `42` directly.  
B) The name of the `number` variable as text.  
C) The type of `number`.  
D) The address of the memory location of `number`.

### 4.
What does the expression `*pointer` mean in this example?

```cpp
int number = 42;
int* pointer = &number;
```

A) We access the `int` object stored at the address held by the pointer.  
B) We create a new pointer.  
C) We get the address of the memory location of `pointer`.  
D) We automatically set the pointer to `nullptr`.

### 5.
Which solution uses `pointer` safely if it may be `nullptr`?

A)
```cpp
std::cout << *pointer << '\n';
```

B)
```cpp
if (pointer == nullptr) {
    std::cout << *pointer << '\n';
}
```

C)
```cpp
if (pointer != nullptr) {
    std::cout << *pointer << '\n';
}
```

D)
```cpp
if (*pointer != 0) {
    std::cout << pointer << '\n';
}
```

### 6.
Which statement is correct?

```cpp
int numbers[3] = {10, 20, 30};
int* pointer = numbers;
```

A) The `numbers` array and the `pointer` variable are the same object.  
B) `pointer` points to the first element of the array; the array itself does not become a pointer.  
C) `pointer` automatically points to the last element of the array.  
D) `pointer` stores the number of elements in the array.

## T2 – Output prediction

### 1.
What is the exact output?

```cpp
#include <iostream>

int main() {
    int a = 5;
    int b = 9;
    int* pointer = &a;

    *pointer = 7;
    pointer = &b;
    *pointer += 3;

    std::cout << a << ' ' << b << '\n';
}
```

### 2.
What is the exact output?

```cpp
#include <iostream>

int main() {
    int numbers[4] = {10, 20, 30, 40};
    int* pointer = numbers;

    std::cout << *(pointer + 2) << '\n';
}
```

### 3.
What is the exact output?

```cpp
#include <iostream>

int main() {
    int numbers[4] = {5, 10, 15, 20};
    int* pointer = numbers;

    *(pointer + 1) = 42;

    std::cout << numbers[1] << '\n';
}
```

### 4.
What is the exact output?

```cpp
#include <iostream>

int main() {
    const int arraySize = 4;
    int numbers[arraySize] = {2, 4, 6, 8};
    int* pointer = numbers;
    int sum = 0;

    for (int i = 0; i < arraySize; ++i) {
        sum += *(pointer + i);
    }

    std::cout << sum << '\n';
}
```

### 5.
What is the exact output?

```cpp
#include <iostream>

int main() {
    int number = 8;
    int* pointer = nullptr;

    if (pointer != nullptr) {
        std::cout << *pointer << '\n';
    } else {
        std::cout << "empty\n";
    }

    pointer = &number;

    if (pointer != nullptr) {
        std::cout << *pointer << '\n';
    }
}
```

### 6.
What is the exact output?

```cpp
#include <iostream>

int main() {
    const int arraySize = 4;
    int numbers[arraySize] = {1, 2, 3, 4};
    int* pointer = numbers;

    for (int i = 0; i < arraySize; ++i) {
        if (*(pointer + i) % 2 == 0) {
            *(pointer + i) *= 10;
        }
    }

    for (int i = 0; i < arraySize; ++i) {
        std::cout << numbers[i] << ' ';
    }
    std::cout << '\n';
}
```
