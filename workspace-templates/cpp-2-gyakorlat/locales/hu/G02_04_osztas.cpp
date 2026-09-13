#include <iostream>

int main() {
    int osszes_pont = 7;
    constexpr int hallgatok_szama = 2;

    const double elso_atlag = osszes_pont / hallgatok_szama;
    const double masodik_atlag = static_cast<double>(osszes_pont) / hallgatok_szama;
    const double harmadik_atlag = static_cast<double>(osszes_pont / hallgatok_szama);

    std::cout << "Elso szamitas: " << elso_atlag << '\n';
    std::cout << "Masodik szamitas: " << masodik_atlag << '\n';
    std::cout << "Harmadik szamitas: " << harmadik_atlag << '\n';
    return 0;
}
