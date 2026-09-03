/*
 * 4. LECKE – C++ I/O, std::string, konverzió és hibakeresés
 *
 * A program beolvas adatokat a felhasználótól, string-műveleteket végez,
 * és egy fontos feltételt asserttel ellenőriz.
 * JÓSOLD MEG a kimenetet, mielőtt lefuttatnád!
 */

#include <iostream>
#include <string>
#include <cassert>
using namespace std;

int main() {
  string nev;
  int kor;

  cout << "Add meg a neved és az életkorod (szóközzel elválasztva): ";
  cin >> nev >> kor;

  // string műveletek
  string udvozles = "Szia, " + nev + "!";
  cout << udvozles << endl;
  cout << "A neved hossza: " << nev.size() << " betű." << endl;

  // konverzió
  string kor_szoveg = to_string(kor);
  cout << "Korod szövegesen: " + kor_szoveg << endl;

  // assert: az életkor ésszerű tartományban van
  assert(kor > 0);
  assert(kor < 150);

  return 0;
}
