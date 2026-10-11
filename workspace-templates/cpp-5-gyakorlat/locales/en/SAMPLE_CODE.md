# CPP_05 – Sample Code for the Project

These examples are **not ready-made solutions to the measurement project**. They show the
same programming patterns using different names and different data. Inno should show and
explain only the sample needed for the current project step; students should not be asked
to read this entire file in advance.

## M1 – Function returning a value

```cpp
int triple(int value) {
    return value * 3;
}
```

The function receives one `int` parameter and returns one `int` result.

## M2 – `void` function that traverses an array

```cpp
void printScores(const int* scores, int count) {
    for (int i = 0; i < count; ++i) {
        cout << scores[i] << ' ';
    }
    cout << '\n';
}
```

`const int*` indicates that this function only reads the data through the pointer. `count`
is a separate parameter because the pointer alone does not tell us how many elements are in
the array.

## M3 – Summing function

```cpp
int sumScores(const int* scores, int count) {
    int sum = 0;

    for (int i = 0; i < count; ++i) {
        sum += scores[i];
    }

    return sum;
}
```

This places the summing pattern learned earlier into a reusable function.

## M4 – One custom function calls another

```cpp
int sumTwo(int a, int b) {
    return a + b;
}

double averageTwo(int a, int b) {
    return static_cast<double>(sumTwo(a, b)) / 2;
}
```

The second function does not repeat the addition; it reuses the first function.

## M5 – Finding the maximum

```cpp
int largestScore(const int* scores, int count) {
    int largest = scores[0];

    for (int i = 1; i < count; ++i) {
        if (scores[i] > largest) {
            largest = scores[i];
        }
    }

    return largest;
}
```

This example assumes the array contains at least one element.

## M6 – Conditional counting with a parameterized limit

```cpp
int countPassing(const int* scores, int count, int minimum) {
    int result = 0;

    for (int i = 0; i < count; ++i) {
        if (scores[i] >= minimum) {
            ++result;
        }
    }

    return result;
}
```

The third parameter makes the same function reusable with several different limits.

## M7 – Modify the original variable through a pointer

```cpp
void incrementOne(int* value) {
    *value += 1;
}
```

A call could be `incrementOne(&number);`. This does not modify a copy: the function receives
the address of the original variable.

## M8 – Using the standard mathematical library

```cpp
double hypotenuse(double a, double b) {
    return sqrt(a * a + b * b);
}
```

This requires the `<cmath>` header. `sqrt` belongs to the standard library's `std` namespace;
because this course uses `using namespace std;`, we can write the shorter `sqrt(...)` form.
