#include <iostream>

int main() {
    // Teaching model: each bit variable may only contain 0 or 1.
    int bit7 = 0;
    int bit6 = 1;
    int bit5 = 1;
    int bit4 = 1;
    int bit3 = 1;
    int bit2 = 1;
    int bit1 = 1;
    int bit0 = 1;

    // 128, 64, ..., 1 are the eight place values in binary.
    const int lower_seven_bits_value = bit6 * 64 + bit5 * 32 + bit4 * 16
        + bit3 * 8 + bit2 * 4 + bit1 * 2 + bit0;
    constexpr int top_bit_place_value = 128;
    const int unsigned_value = bit7 * top_bit_place_value
        + lower_seven_bits_value;
    const int signed_value = -bit7 * top_bit_place_value
        + lower_seven_bits_value;

    std::cout << "Bit pattern: " << bit7 << bit6 << bit5 << bit4
              << bit3 << bit2 << bit1 << bit0 << '\n';
    std::cout << "Unsigned interpretation: " << unsigned_value << '\n';
    std::cout << "Two's complement interpretation: " << signed_value << '\n';
    return 0;
}
