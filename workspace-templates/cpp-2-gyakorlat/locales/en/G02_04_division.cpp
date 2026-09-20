#include <iostream>

int main() {
    int total_points = 7;
    constexpr int student_count = 2;

    const double first_average = total_points / student_count;
    const double second_average = static_cast<double>(total_points) / student_count;
    const double third_average = static_cast<double>(total_points / student_count);

    std::cout << "First calculation: " << first_average << '\n';
    std::cout << "Second calculation: " << second_average << '\n';
    std::cout << "Third calculation: " << third_average << '\n';
    return 0;
}
