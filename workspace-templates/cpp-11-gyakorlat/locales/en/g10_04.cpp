#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string filename;
    cin >> filename;
    ifstream input(filename);
    if (!input) { cout << "ERROR\n"; return 0; }
    int number = 0;
    int count = 0;
    while (!input.eof()) {
        input >> number;
        if (number % 2 == 0) count++;
    }
    cout << count << "\n";
    return 0;
}
