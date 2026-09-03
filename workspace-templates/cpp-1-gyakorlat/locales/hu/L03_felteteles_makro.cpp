/*
 * 3. LECKE – feltételes direktívák és paraméteres makrók
 *
 * A program viselkedése attól függ, definiáltuk-e a DEBUG makrót
 * fordításkor. A fordítási parancsok a lecke alatti leírásban vannak.
 */

#include <iostream>
#include <cassert>
using namespace std;

#ifndef CXX_ALAPOK_HEADER
#define CXX_ALAPOK_HEADER
// Include guard: ez a blokk egy fordítási egységben csak egyszer kerülhet be.
#endif

#define SQUARE(x) ((x) * (x))

int main() {
#ifdef DEBUG
  cout << "DEBUG mód: diagnosztikai üzenet bekapcsolva" << endl;
#else
  cout << "Normál mód: nincs debug üzenet" << endl;
#endif

  cout << "SQUARE(3) = " << SQUARE(3) << endl;
  cout << "SQUARE(1 + 2) = " << SQUARE(1 + 2) << endl;

  // A zárójelezett makró helyes eredményt ad.
  assert(SQUARE(1 + 2) == 9);
  return 0;
}
