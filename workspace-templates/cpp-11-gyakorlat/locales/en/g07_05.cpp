#include <iostream>
using namespace std;

int main() {
    int number;
    cin >> number;
    {
        int result = number * 3;
    }
    cout << result << "\n";
    {
        int number = 9;
        cout << number << "\n";
    }
    cout << number << "\n";
    return 0;
}
