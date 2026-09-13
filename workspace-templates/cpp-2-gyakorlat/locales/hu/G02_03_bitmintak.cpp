#include <iostream>

int main() {
    // Szemléltető modell: minden bitváltozó megengedett értéke 0 vagy 1.
    int bit7 = 0;
    int bit6 = 1;
    int bit5 = 1;
    int bit4 = 1;
    int bit3 = 1;
    int bit2 = 1;
    int bit1 = 1;
    int bit0 = 1;

    // A 128, 64, ..., 1 a kettes számrendszer nyolc helyiértéke.
    const int also_het_bit_erteke = bit6 * 64 + bit5 * 32 + bit4 * 16
        + bit3 * 8 + bit2 * 4 + bit1 * 2 + bit0;
    constexpr int legfelso_bit_helyierteke = 128;
    const int elojel_nelkuli_ertek = bit7 * legfelso_bit_helyierteke
        + also_het_bit_erteke;
    const int elojeles_ertek = -bit7 * legfelso_bit_helyierteke
        + also_het_bit_erteke;

    std::cout << "Bitminta: " << bit7 << bit6 << bit5 << bit4
              << bit3 << bit2 << bit1 << bit0 << '\n';
    std::cout << "Elojel nelkul: " << elojel_nelkuli_ertek << '\n';
    std::cout << "Kettes komplemens: " << elojeles_ertek << '\n';
    return 0;
}
