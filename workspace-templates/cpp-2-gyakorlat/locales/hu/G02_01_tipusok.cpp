#include <climits>
#include <iostream>
#include <limits>

int main() {
    std::cout << "Egy bajt bitjei: " << CHAR_BIT << '\n';
    std::cout << "int merete bajtban: " << sizeof(int) << '\n';
    std::cout << "float merete bajtban: " << sizeof(float) << '\n';
    std::cout << "double merete bajtban: " << sizeof(double) << '\n';
    std::cout << "int also hatara: " << std::numeric_limits<int>::lowest() << '\n';
    std::cout << "int felso hatara: " << std::numeric_limits<int>::max() << '\n';

    int pontszam = 12;
    std::cout << "Pontszam: " << pontszam << '\n';
    std::cout << "Pontszam tarmerete bajtban: " << sizeof(pontszam) << '\n';
    return 0;
}
