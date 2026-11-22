#include <iostream>
#include <fstream>
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

struct List { int values[2]{}; int size = 0; };
bool validNumber(const string& line, int* number) {
    istringstream parts(line);
    string text, extra;
    if (!(parts >> text) || (parts >> extra)) return false;
    return integerToken(text, number) && *number >= 0 && *number <= 50;
}
bool load(const string& filename, List* target) {
    ifstream input(filename);
    if (!input) return false;
    List temporary; // TODO: use this temporary
    target->size = 0;
    string line;
    while (getline(input, line)) {
        int number;
        if (!validNumber(line, &number)) return false;
        if (target->size == 2) return false;
        target->values[target->size++] = number;
    }
    if (!input.eof() || input.bad()) return false;
    // TODO: commit only on success
    return true;
}

int main() {
    string filename;
    cin >> filename;
    List item;
    item.values[0] = 40;
    item.values[1] = 41;
    item.size = 2;
    bool success = load(filename, &item);
    cout << success << " " << item.size;
    for (int i = 0; i < item.size; i++) cout << " " << item.values[i];
    cout << "\n";
    return 0;
}
