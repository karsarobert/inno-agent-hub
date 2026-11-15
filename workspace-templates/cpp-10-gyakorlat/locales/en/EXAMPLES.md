# Analogous examples – before the tasks

These complete programs solve different problems. Run them individually in separate scratch sources; do not treat them as completed target solutions.

## M1 – Writing text to a file

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ofstream file("status_demo.txt");
    if (!file) return 1;
    file << "READY\n";
    file.close();
    cout << static_cast<bool>(file) << '\n';
}
```

Expected output:

```text
1
```

iostream supplies cout; fstream supplies ofstream. The ofstream constructor opens the file; !file checks failed state. << writes characters. close completes buffered output; Boolean conversion afterwards reports errors, not whether the file remains open. static_cast<bool> explicitly requests that conversion.

G10_01 requires two two-number records and their separators rather than a single status word.

## M2 – Appending and line-by-line reading

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    { ofstream file("events_demo.txt"); if (!file) return 1;
      file << "OPEN\n"; file.close(); if (!file) return 1; }
    { ofstream file("events_demo.txt", ios::app); if (!file) return 1;
      file << "CLOSE\n"; file.close(); if (!file) return 1; }
    ifstream input("events_demo.txt"); if (!input) return 1;
    string line;
    while (getline(input,line)) cout << line << '\n';
    if (input.bad() || !input.eof()) return 1;
}
```

Expected output:

```text
OPEN
CLOSE
```

The first block creates the baseline; the second appends with ios::app. Both check closing. string and getline come from string: getline extracts a complete line of characters. The while condition checks extraction success, so the body has a usable line.

G10_02 contains numbers; you must accumulate their count and sum while reading.

## M3 – The final number and EOF

```cpp
#include <iostream>
#include <fstream>
using namespace std;

int main() {
    { ofstream file("number_demo.txt"); if (!file) return 1;
      file << "8"; file.close(); if (!file) return 1; }
    ifstream input("number_demo.txt"); if (!input) return 1;
    int number = 0;
    input >> number;
    cout << number << ' ' << input.eof() << ' ' << input.fail() << '\n';
    input >> number;
    cout << input.eof() << ' ' << input.fail() << '\n';
}
```

Expected output:

```text
8 1 0
1 1
```

ofstream writes a number without a newline. The first extraction succeeds while detecting EOF: eof true, fail false. The second request has no new number: both flags become true. We do not print the number after that failed extraction.

G10_03 requests two fields and explores invalid text and a missing field. These flags are not mutually exclusive.

## M4 – Tokens and full-number validation

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    const string line = "MODE 2x";
    istringstream fields(line);
    string keyword, text, extra;
    if (!(fields >> keyword >> text) || (fields >> extra)) return 1;
    istringstream data(text);
    int number = 0; char leftover;
    bool success = static_cast<bool>(data >> number);
    bool complete = success && !(data >> leftover);
    cout << (keyword == "MODE") << ' ' << complete << '\n';
}
```

Expected output:

```text
1 0
```

string holds the line; sstream supplies istringstream. fields reads two strings and probes for a third: if present, the format is invalid. data inspects only the second token. It can read 2, but x remains, so complete is false. && short-circuits: after failed numeric extraction the character probe is skipped.

Both target tokens are numbers and need range checks; the project must reuse existing addition rules. Checking the MODE keyword does not solve those tasks.

## M5 – Temporary state

```cpp
#include <iostream>
using namespace std;

class Level {
private:
    int value;
public:
    Level() : value(5) {}
    int get() const { return value; }
    bool set(int number) {
        if (number < 0 || number > 10) return false;
        value = number; return true;
    }
};
int main() {
    Level original, candidate;
    bool first = candidate.set(8);
    bool second = candidate.set(12);
    if (first && second) original = candidate;
    cout << original.get() << '\n';
}
```

Expected output:

```text
5
```

There are two independent Level objects. Setting 8 on the temporary succeeds; setting 12 fails. The original is assigned only after both succeed, so it stays 5. Returning false does not undo mutations: preserving the original depends on not modifying it yet.

The project has an unknown number of file lines rather than two known requests. Any invalid record must prevent the final object replacement.

## M6 – Output string stream

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    ostringstream text;
    int value = 9;
    text << "LEVEL=" << value << ";READY=" << (value >= 5);
    string result = text.str();
    cout << result << '\n';
}
```

Expected output:

```text
LEVEL=9;READY=1
```

ostringstream is an in-memory output stream from sstream. << converts values into characters; str() returns a string. Only the cout statement prints. Constructing the text does not open a file.

P5 builds its report from two queries on the current office and returns the text from a method.

## M7 – Checking the header separately

```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    { ofstream file("header_demo.txt"); if (!file) return 1;
      file << "COLORS 2\nblue\n"; file.close(); if (!file) return 1; }
    ifstream input("header_demo.txt"); if (!input) return 1;
    string header;
    if (!getline(input,header) || header != "COLORS 2") return 1;
    string line;
    while (getline(input,line)) cout << line << '\n';
    if (input.bad() || !input.eof()) return 1;
}
```

Expected output:

```text
blue
```

The first getline reads the header, not a record. || short-circuits, so a failed read immediately causes rejection. Equality compares the entire text: a different version or extra space is a mismatch. The next getline reads the first data line.

The project expects TICKETS 1 rather than COLORS 2, and subsequent lines represent two integer seat coordinates rather than colour names.
