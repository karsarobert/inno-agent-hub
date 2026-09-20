#include <iostream>
#include <limits>

int main() {
    constexpr unsigned int increment = 1u;
    unsigned int counter = std::numeric_limits<unsigned int>::max();
    std::cout << "Counter before: " << counter << '\n';

    counter = counter + increment;
    std::cout << "Counter after: " << counter << '\n';

    int quantity = 50000;
    int unit_price = 50000;
    const long long total_price = static_cast<long long>(quantity) * unit_price;

    std::cout << "Highest int value: " << std::numeric_limits<int>::max() << '\n';
    std::cout << "Total price: " << total_price << '\n';
    return 0;
}
