#include <iostream>

using namespace std;

int main() {
    const int a = 8;
    const int b = 3;

    cout << "a = " << a << ", b = " << b << '\n';

    // Elso lepesben probald itt meghivni az osszead fuggvenyt.
    // Figyeld meg, mit mond a fordito, majd oldd meg prototipussal.

    return 0;
}

int osszead(int a, int b) {
    return a + b;
}
