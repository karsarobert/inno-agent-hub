/*
 * KIEGÉSZÍTŐ GYAKORLAT – Feltételes fordítás és paraméteres makrók
 *
 * A programot kétféle fordítási beállítással vizsgáljuk.
 * A SQUARE makrót csak a megadott kifejezésekkel használd;
 * a SQUARE(i++) nem megfelelő használat. A programozói feltételt az assert ellenőrzi.
 */

#include <iostream>
#include <cassert>

#define SQUARE(x) ((x) * (x))

int main() {
#ifdef DEBUG
    std::cout << "A diagnosztikai uzenet be van kapcsolva." << '\n';
#else
    std::cout << "A diagnosztikai uzenet ki van kapcsolva." << '\n';
#endif

    std::cout << "SQUARE(3) = " << SQUARE(3) << '\n';
    std::cout << "SQUARE(1 + 2) = " << SQUARE(1 + 2) << '\n';

    // Az assert programozói feltételt ellenőriz; itt nem felhasználói bemenetet.
    // Ha a NDEBUG makró definiálva van, ez az ellenőrzés kimarad.
    // A hívásnak nincs olyan mellékhatása, amelyre a program működése épülne.
    assert(SQUARE(1 + 2) == 9);
    return 0;
}
