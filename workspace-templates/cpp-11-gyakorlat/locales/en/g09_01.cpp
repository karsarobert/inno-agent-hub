#include <iostream>
using namespace std;

class Rectangle {
    int width;
    int height;
public:
    Rectangle() : width(0), height(0) /* TODO 1 */ {}
    Rectangle(int a, int b) : width(0), height(0) /* TODO 2 */ {}
    int area() const { return width * height; }
};

int main() {
    int a, b;
    cin >> a >> b;
    Rectangle first;
    Rectangle second(a, b);
    cout << first.area() << " " << second.area() << "\n";
    return 0;
}
