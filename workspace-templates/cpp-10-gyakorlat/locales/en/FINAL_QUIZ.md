# CPP_10 – Fixed final assessment

20 questions. T1: 10 multiple choice; T2: 5 exact outputs and 5 repairs. The first substantive answer counts. Programs are independent and assume successful file access except where a missing file is specified. Do not execute question code before answering. For repairs, give both cause and the smallest correct change.

## T1/1

Why use a TICKETS 1 header?

A. 1 means only one ticket is allowed.
B. It identifies the file format and its version.
C. It automatically opens the file.
D. It gives the price of the first ticket.

## T1/2

After successful writing and close(), which is true?

A. Boolean conversion is always false.
B. eof() must be true.
C. is_open() is false, but Boolean conversion can be true.
D. The object immediately ceases to exist.

## T1/3

What can eof=true and fail=false mean after numeric extraction?

A. The last number was successfully extracted at EOF.
B. The number must be invalid.
C. Another number is definitely available.
D. The file never opened.

## T1/4

Which statement about empty state is correct for this project?

A. Both empty-file variants are invalid.
B. An empty file is valid, but a header is invalid.
C. An empty file appends a zero to the old log.
D. A header-only file is valid; a completely empty file is invalid.

## T1/5

Which pair of records is a duplicate booking?

A. 1 2 and 1 3
B. 2 4 and 2 4
C. 1 2 and 2 2
D. 2 1 and 3 1

## T1/6

Why use getline before istringstream?

A. It isolates a record for validation without crossing into the next line.
B. It eliminates all error handling.
C. It makes every file valid automatically.
D. ifstream cannot read numbers at all.

## T1/7

What does ostringstream::str() return?

A. The opened filename.
B. A pointer to the stream.
C. The constructed text as a string value.
D. A Boolean saving result.

## T1/8

Why is repeated ios::app saving wrong for a full snapshot?

A. app is only for reading.
B. It cannot write int values.
C. close() cannot be used.
D. It can append another header and duplicate records.

## T1/9

Which header supplies both string-stream types?

A. <cmath>
B. <sstream>
C. <iomanip>
D. <limits>

## T1/10

ok.txt is visible in the workspace but RUN cannot open it. What should be checked first?

A. Remove header validation.
B. Always return true.
C. The running program’s working directory.
D. Change the seat price.

## T2/1

What is the exact output?

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    { ofstream file("q01.txt"); if (!file) return 1;
      file << "3\n5\n"; file.close(); if (!file) return 1; }
    ifstream input("q01.txt"); if (!input) return 1;
    int value, count = 0, sum = 0;
    while (input >> value) { ++count; sum += value; }
    cout << count << ' ' << sum << '\n';
}
```

## T2/2

What is the exact output?

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ostringstream text;
    text << "N=" << 7;
    string result = text.str();
    result += "!";
    cout << text.str() << '\n' << result << '\n';
}
```

## T2/3

What is the exact output?

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream data("16");
    int number = 0;
    data >> number;
    cout << data.eof() << ' ' << data.fail() << ' '
         << static_cast<bool>(data) << '\n';
}
```

## T2/4

What is the exact output?

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream data("4x");
    int number = 0; char leftover = '?';
    bool success = static_cast<bool>(data >> number);
    bool hasLeftover = static_cast<bool>(data >> leftover);
    cout << success << ' ' << hasLeftover << '\n';
}
```

## T2/5

What is the exact output?

```cpp
#include <iostream>
using namespace std;

class Level {
private:
    int value;
public:
    Level(int number) : value(number) {}
    bool set(int number) {
        if (number < 0 || number > 10) return false;
        value = number; return true;
    }
    int get() const { return value; }
};
int main() {
    Level original(8), candidate(1);
    candidate.set(6);
    bool success = candidate.set(-1);
    if (success) original = candidate;
    cout << original.get() << ' ' << candidate.get() << '\n';
}
```

## T2/6

Why does this fail compilation? Repair the return so it reports saving success.

```cpp
#include <iostream>
#include <fstream>
using namespace std;

bool save() {
    ofstream file("q06.txt");
    if (!file) return false;
    file << "READY\n";
    file.close();
    return file;
}
int main() { cout << save() << '\n'; }
```

## T2/7

Why is the number printed twice? Process only successful extractions.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream input("6\n");
    int value = 0;
    while (!input.eof()) {
        input >> value;
        cout << value << '\n';
    }
}
```

## T2/8

Why does this print ERROR although 25 was read successfully? Repair the success check.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    istringstream data("25");
    int value = 0;
    data >> value;
    if (data.good()) cout << "OK\n";
    else cout << "ERROR\n";
}
```

## T2/9

absent_q09.txt does not exist. The old value 9 should be preserved. Where is that violated, and what is the smallest repair?

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int original = 9;
    original = 0;
    ifstream file("absent_q09.txt");
    if (!file) {
        cout << original << '\n';
        return 0;
    }
}
```

## T2/10

We save the same full snapshot twice but get six lines. How should only three remain?

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    { ofstream file("q10.txt"); if (!file) return 1;
      file.close(); if (!file) return 1; }
    for (int i = 0; i < 2; ++i) {
        ofstream file("q10.txt", ios::app);
        if (!file) return 1;
        file << "TICKETS 1\n1 2\n2 3\n";
        file.close(); if (!file) return 1;
    }
    ifstream input("q10.txt"); if (!input) return 1;
    string line; int count = 0;
    while (getline(input,line)) ++count;
    cout << count << '\n';
}
```
