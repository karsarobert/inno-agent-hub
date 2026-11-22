#include <iostream>
using namespace std;

struct Book { int pages; bool available; };
int countAvailable(const Book items[], int n) {
    int count = 0;
    // TODO: count only the matching records
    return count;
}

int main() {
    int n;
    cin >> n;
    Book items[5]{};
    for (int i = 0; i < n; i++) cin >> items[i].pages >> items[i].available;
    cout << countAvailable(items, n) << "\n";
    return 0;
}
