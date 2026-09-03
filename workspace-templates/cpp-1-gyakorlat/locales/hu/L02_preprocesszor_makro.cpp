/*
 * 2. LECKE – preprocesszor alapjai: #include, #define, -E
 *
 * A makrók FORDÍTÁSIDŐBEN helyettesítődnek be (nem futásidőben!).
 * A te feladatod: JÓSOLD MEG a kimenetet, majd futtasd és ellenőrizd.
 */

#include <iostream>
using namespace std;

// Makró definiálása (értékes makró)
#define PRINT_MY_NAME cout << "My name is John Doe" << endl;
#define MY_FAV_NUM 42

int main() {
  // PREDICTION (jósold meg futtatás előtt!):
  // Kérdés: mi lesz a kimenet? Ha nem biztos, mondd el a tippet,
  // azután futtasd le, és hasonlítsd össze.

  PRINT_MY_NAME
  cout << "My fav number is: " << MY_FAV_NUM << endl;

  return 0;
}
