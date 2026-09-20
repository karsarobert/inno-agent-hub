// Optional demonstration. The starting program is correct; modify it only with the tutor.
#include <iostream>

int main() {
    int quantity = 50000;
    int unit_price = 50000;
    const long long total_price = static_cast<long long>(quantity) * unit_price;

    std::cout << "Total price: " << total_price << '\n';
    return 0;
}
