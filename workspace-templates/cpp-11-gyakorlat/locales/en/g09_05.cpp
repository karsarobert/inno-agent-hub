#include <iostream>
using namespace std;

struct Book { int id; };
class Shelf {
    Book items[2]{};
    int size = 0;
public:
    bool add(Book item) {
        if (size == 2) return false;
        items[size++] = item;
        return true;
    }
    bool removeLast() {
        // TODO
        return false;
    }
    int get() const { return size; }
};

int main() {
    int n, k;
    cin >> n >> k;
    Shelf shelf;
    for (int i = 0; i < n; i++) shelf.add(Book{10 + i});
    for (int i = 0; i < k; i++) {
        cout << shelf.removeLast() << " " << shelf.get() << "\n";
    }
    return 0;
}
