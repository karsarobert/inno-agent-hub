#include <iostream>
#include <fstream>
using namespace std;

int main() {
    int number;
    cin >> number;
    ofstream output("out02.txt"); // TODO
    if (!output) { cout << "ERROR\n"; return 0; }
    output << number << "\n";
    output.close();
    if (output.fail()) { cout << "ERROR\n"; return 0; }
    ifstream input("out02.txt");
    while (input >> number) cout << number << "\n";
    return 0;
}
