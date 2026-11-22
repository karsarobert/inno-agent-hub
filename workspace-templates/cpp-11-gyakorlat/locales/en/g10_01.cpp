#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool save(const string& filename, const int items[], int n) {
    ofstream output(filename);
    if (!output) return false;
    // TODO
    output.close();
    return !output.fail();
}

int main() {
    int n;
    cin >> n;
    int items[4]{};
    for (int i = 0; i < n; i++) cin >> items[i];
    if (!save("out01.txt", items, n)) { cout << "ERROR\n"; return 0; }
    cout << "OK\n";
    ifstream input("out01.txt");
    int number;
    while (input >> number) cout << number << "\n";
    return 0;
}
