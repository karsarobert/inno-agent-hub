#include <iostream>
using namespace std;

struct Product { int count; double unitPrice; };

int main() {
    int n, next;
    cin >> n >> next;
    Product original{n, 4.5};
    Product copy{}; // TODO 1: copy initialization
    // TODO 2
    cout << original.count << " " << copy.count << "\n";
    return 0;
}
