#include <iostream>
using namespace std;

// Source data only; you will create the Book objects and loops.
int main() {
    const int size = 6;
    const int ids[size] = {501, 502, 503, 504, 505, 506};
    const int totals[size] = {5, 3, 0, 7, 4, 2};
    const int loans[size] = {3, 3, 0, 2, 0, 1};
    cout << "Source books: " << size << '\n';
    cout << "First source: " << ids[0] << ' ' << totals[0] << ' ' << loans[0] << '\n';
    return 0;
}
