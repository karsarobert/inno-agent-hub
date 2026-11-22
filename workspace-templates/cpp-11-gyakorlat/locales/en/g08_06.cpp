#include <iostream>
using namespace std;

class Result {
    int score = 0;
public:
    void set(int next) { score = next; }
    int get() const { return score; }
};
int countReached(const Result items[], int n, int threshold) {
    int count = 0;
    // TODO
    return count;
}

int main() {
    int n, threshold;
    cin >> n >> threshold;
    Result items[5];
    for (int i = 0; i < n; i++) {
        int score;
        cin >> score;
        items[i].set(score);
    }
    cout << countReached(items, n, threshold) << "\n";
    return 0;
}
