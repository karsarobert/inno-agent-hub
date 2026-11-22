#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool countNegative(const string& filename, int* result) {
    ifstream input(filename);
    if (!input) return false;
    int temporary = 0;
    int number;
    while (input >> number) {
        // TODO 1
    }
    if (!input.eof() || input.bad()) return false;
    // TODO 2
    return true;
}

int main() {
    string filename;
    cin >> filename;
    int result = 99;
    bool success = countNegative(filename, &result);
    cout << success << " " << result << "\n";
    return 0;
}
