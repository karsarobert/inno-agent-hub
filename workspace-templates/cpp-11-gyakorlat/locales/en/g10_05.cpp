#include <iostream>
#include <sstream>
#include <string>
using namespace std;

bool integerToken(const string& text, int* result) {
    istringstream probe(text);
    int temporary;
    if (!(probe >> temporary)) return false;
    probe >> ws;
    if (!probe.eof()) return false;
    *result = temporary;
    return true;
}

bool validateLine(const string& line, int* code, int* count) {
    istringstream parts(line);
    string codeText, countText, extra;
    int k, d;
    // TODO 1: require exactly two tokens
    if (!integerToken(codeText, &k) || !integerToken(countText, &d)) return false;
    // TODO 2: check range
    *code = k;
    *count = d;
    return true;
}

int main() {
    string line;
    getline(cin, line);
    int code = 77, count = 88;
    bool success = validateLine(line, &code, &count);
    cout << success << " " << code << " " << count << "\n";
    return 0;
}
