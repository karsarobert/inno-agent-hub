#include <iostream>

int main() {
    constexpr int max_score = 100;
    int score{};
    std::cout << "Initial score: " << score << '\n';

    score = 72;
    const int fixed_score = score;

    std::cout << "Current score: " << score << '\n';
    std::cout << "Fixed score: " << fixed_score << '\n';
    std::cout << "Maximum score: " << max_score << '\n';
    return 0;
}
