#include <iomanip>
#include <iostream>

int main() {
    constexpr int student_count = 2;
    constexpr int max_score = 100;
    constexpr double percentage_multiplier = 100.0;
    constexpr int displayed_decimal_places = 1;
    int first_score = 71;
    int second_score = 84;

    const int total_points = first_score + second_score;
    // Assigned debugging task: compare this calculation with the manual average.
    const double average_score = total_points / student_count;
    const double average_percentage = average_score / max_score * percentage_multiplier;

    std::cout << std::fixed << std::setprecision(displayed_decimal_places);
    std::cout << "Average score: " << average_score << '\n';
    std::cout << "Average percentage: " << average_percentage << "%\n";
    return 0;
}
