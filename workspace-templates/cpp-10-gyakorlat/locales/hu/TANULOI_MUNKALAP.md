# CPP_10 – Gyors emlékeztető

Ez referencia; külön kitölteni nem kell. A haladást Inno vezeti.

| Fogalom | Mire figyelj? |
|---|---|
| ofstream | Sikeres alapértelmezett megnyitáskor a korábbi tartalom törlődik. |
| ios::app | A végére ír; teljes pillanatkép mentésére most nem ezt használjuk. |
| ifstream >> | Számokat olvas, az újsort is átugorja. |
| getline | Egy sort választ le; nem ellenőrzi a sor számainak érvényességét. |
| istringstream | A leválasztott string karaktereit dolgozza fel saját állapottal. |
| ostringstream | Értékekből karaktereket épít memóriában; str() ad stringet. |
| eof / fail / bad | Fájlvég / sikertelen művelet vagy bad / súlyos I/O-hiba; nem kizáró állapotok. |
| bool-konverzió | !fail(); nem azonos az is_open() lekérdezéssel. |
| fejléc | TICKETS 1, mindkét nyelven; a verzió nem darabszám. |
| ideiglenes objektum | Teljes siker után csere; hibánál az eredeti nem változik. |

Fejlécek: iostream – cout, cerr, cin; fstream – fájlfolyamok; string – string és getline; sstream – szövegfolyamok. A static_cast és a return nyelvi elemek. A projekt két int mezője miatt nincs szükség iomanip/limits vagy double-pontossági beállításra.

Nézőtér: 3×4; tároló: 4 jegy; első sor 4000, másik sor 3000. Dupla sor–szék pár tiltott, ugyanabban a sorban másik szék megengedett. Csak a [0,darab) rész aktív. Hiányzó fejléc hiba, csak fejléc helyes üres állapot.

A sikertelen művelet után a tényleges adatokat is kérdezd le. Mentés után ellenőrizd a fájlt, szükség esetén frissítsd a nézetet. Új programfutásban a memória újra üres; csak a betöltés állíthatja vissza az adatokat.
