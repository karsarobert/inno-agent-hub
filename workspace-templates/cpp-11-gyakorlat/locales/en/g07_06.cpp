#include <iostream>
using namespace std;

struct TwoNumbers { int integer; double real; };
union Number { int integer; double real; };

int main() {
    char kind;
    cin >> kind;
    Number item{};
    if (kind == 'I') cin >> item.integer;
    else cin >> item.real;
    // TODO: print only the active member
    cout << sizeof(TwoNumbers) << " " << sizeof(Number) << " " << sizeof(int) << " " << sizeof(double) << "\n";
    return 0;
}
