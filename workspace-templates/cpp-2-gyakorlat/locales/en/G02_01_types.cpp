#include <climits>
#include <iostream>
#include <limits>

int main() {
    std::cout << "Bits in one byte: " << CHAR_BIT << '\n';
    std::cout << "Size of int in bytes: " << sizeof(int) << '\n';
    std::cout << "Size of float in bytes: " << sizeof(float) << '\n';
    std::cout << "Size of double in bytes: " << sizeof(double) << '\n';
    std::cout << "Lowest int value: " << std::numeric_limits<int>::lowest() << '\n';
    std::cout << "Highest int value: " << std::numeric_limits<int>::max() << '\n';

    int score = 12;
    std::cout << "Score: " << score << '\n';
    std::cout << "Score storage size in bytes: " << sizeof(score) << '\n';
    return 0;
}
