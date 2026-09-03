# The lessons, step by step

> Type every command into the **terminal below the workspace**.
> Every `.cpp` file is at the **root** of the workspace — so no path is needed.

---

## Lesson 1 — first program (observation)

The code is **given** in `L01_elso_program.cpp`. You do not have to write it,
only **observe**.

**1. Compile it:**
```
g++ -Wall -o L01 L01_elso_program.cpp
```

**2. Run it:**
```
./L01
```

**3. What to observe?**
- What appears on the screen?
- Why did we have to **compile first**? (How is this different from Python?)
- What is the role of the `#include <iostream>` line? Of `using namespace std;`? Of `return 0;`?
- Remove the `using namespace std;` line and change `cout` to `std::cout`. Does it still compile? What do you notice?

---

## Lesson 2 — the preprocessor and macros

`L02_preprocesszor_makro.cpp` already exists. **First PREDICT the output**, then run it.

**1. Compile and run:**
```
g++ -Wall -o L02 L02_preprocesszor_makro.cpp
./L02
```

**2. Look at the preprocessed output:**
The `-E` switch shows what the code becomes before compilation.
```
g++ -E L02_preprocesszor_makro.cpp
```

**3. What to observe?**
- What do the `PRINT_MY_NAME` and `MY_FAV_NUM` macros become in the preprocessed output?
- How much extra code got added before your short program (from `iostream`)?
- Change `MY_FAV_NUM` to 7, compile again — what happens?

---

## Lesson 3 — conditional compilation

**1. First predict what depends on the `DEBUG` macro.**

**2. Compile without DEBUG:**
```
g++ -Wall -o L03 L03_felteteles_makro.cpp
./L03
```

**3. Compile with DEBUG:**
```
g++ -Wall -DDEBUG -o L03 L03_felteteles_makro.cpp
./L03
```

**4. What do you observe?**
- Which message appears in the two cases? Why?
- The `DEBUG` macro decides at **compile time** — not at run time. Can you see the difference between `#ifdef` and a plain `if`?
- **SQUARE trap:** here the macro is `((x)*(x))` — parenthesized, so `SQUARE(1+2)=9`. Try it without the parentheses (`x * x` instead of `(x) * (x)`). What is the result? Why?

---

## Lesson 4 — I/O, strings, debugging

**1. Predict what output you will get for your input.**

**2. Compile and run:**
```
g++ -Wall -o L04 L04_io_string_hibakes.cpp
./L04
```

**3. What do you observe?**
- What is the direction of the operator for `cout <<` and `cin >>`? Why are they opposite?
- What does `nev.size()` give? What is the role of `to_string()`?
- What does `assert` do? Try entering an age of 0 or 200 — what happens? Why does the program stop?

---

## Useful revision

The general compile-run pattern (for any `.cpp`):
```
g++ -Wall -o <output_name> <file>.cpp
./<output_name>
```
> Always compile with **-Wall**! That way you see the warnings that help you
> avoid errors.
