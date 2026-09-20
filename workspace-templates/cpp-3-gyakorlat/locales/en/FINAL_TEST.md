# CPP_03 – Final Test

The tutor leads this test one question at a time. Do not read ahead for solutions; the goal is to answer independently after the practice work.

## T1 – Multiple-choice questions

### 1.
When is the body of an `if` block executed?

A) Always once.  
B) When the condition is true.  
C) When the condition is false.  
D) Only when there is an `else` branch.

### 2.
What does a valid `if–else` structure guarantee during one execution?

A) Both branches run.  
B) Neither branch can run.  
C) Exactly one branch runs.  
D) The `else` branch always runs first.

### 3.
What happens in an `if / else if / else` chain when one condition becomes true?

A) Its branch runs and the later branches in the chain are skipped.  
B) Every later condition must still be evaluated.  
C) The `else` branch also runs.  
D) The program automatically ends.

### 4.
What is the typical role of `break` inside a `switch` `case` branch?

A) It restarts the `switch`.  
B) It stops the whole program.  
C) It prevents execution from continuing into following `case` branches.  
D) It makes the `switch` condition false.

### 5.
Which statement is true about a `do–while` loop?

A) Its body never runs if the condition is initially false.  
B) Its body runs at least once.  
C) It can only have an even number of iterations.  
D) It has no condition.

### 6.
Why is a `for` loop often convenient for counting tasks?

A) Because it cannot contain a selection statement.  
B) Because it always runs exactly ten times.  
C) Because it does not need a loop variable.  
D) Because initialization, condition, and update are visible in one place.

## T2 – Output prediction

### 1.
What is the exact output?

```cpp
#include <iostream>

int main() {
    const int number = 5;

    if (number > 3) {
        std::cout << "A\n";
    }

    std::cout << "C\n";
}
```

### 2.
What is the exact output?

```cpp
#include <iostream>

int main() {
    const int score = 60;

    if (score >= 80) {
        std::cout << "Excellent\n";
    } else if (score >= 60) {
        std::cout << "Satisfactory\n";
    } else {
        std::cout << "Needs improvement\n";
    }
}
```

### 3.
What is the exact output?

```cpp
#include <iostream>

int main() {
    const int value = 2;

    switch (value) {
        case 1:
            std::cout << "One\n";
            break;
        case 2:
            std::cout << "Two\n";
            break;
        default:
            std::cout << "Other\n";
            break;
    }
}
```

### 4.
What is the exact output?

```cpp
#include <iostream>

int main() {
    int number = 1;
    int sum = 0;

    while (number <= 3) {
        sum += number;
        ++number;
    }

    std::cout << sum << '\n';
}
```

### 5.
What is the exact output?

```cpp
#include <iostream>

int main() {
    int number = 4;
    const int last_number = 3;

    do {
        std::cout << number << '\n';
        ++number;
    } while (number <= last_number);
}
```

### 6.
What is the exact output?

```cpp
#include <iostream>

int main() {
    for (int number = 1; number <= 6; ++number) {
        if (number % 2 == 0) {
            std::cout << number << ' ';
        }
    }
    std::cout << '\n';
}
```
