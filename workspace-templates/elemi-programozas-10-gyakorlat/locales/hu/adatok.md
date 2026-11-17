# Próbaadatok

Minden adat UTF-8. Nincs fejléc. Sorforma: termek;darab.
A mezők körüli szóközöket a beolvasó levágja.
A beolvasó ellenőrzi a két mezőt, a nem üres nevet és az egészre
alakítható darabszámot. A pozitivitás és a termék létezése a Bufe dolga.
Az eredeti fizikai sorszámot őrizzük meg.
A hibaüzenet pontos szövege nem kötött, de legyen érthető az ok.

| Bemenet | Értékesítés | Darab | Bevétel | Hiba | Üres sor |
|---|---:|---:|---:|---:|---:|
| eladasok_jo.txt | 3 | 6 | 1300 Ft | 0 | 0 |
| eladasok_vegyes.txt | 3 | 6 | 1300 Ft | 4 | 1 |
| eladasok_hibas.txt | 0 | 0 | 0 Ft | 5 | 0 |
| ures.txt | 0 | 0 | 0 Ft | 0 | 0 |

A vegyes fájl hibás sorai: 2, 5, 7, 8; a 3. sor üres.
Az utolsó sor végén nincs sortörés. Az ures.txt valóban 0 bájtos.
Az ep10_hianyzo.txt nincs mellékelve; ezt a próba előtt ne hozd létre.

A cél külön fájl: jelentes.txt. Rekordforma: termek;darab;osszeg.
A „Teljes” állapot azt jelenti, hogy nincs elutasított sor.
Az üres sor önmagában nem hiba. Az üres létező fájl feldolgozható;
a hiányzó fájl nem sikeres üres bemenet.
Sérült karakterkódolás kezelése nem része a feladatnak.
