# CPP_10 – InnoAgent hallgatói csomag

**3 × 45 perc, szünetek nélkül.** Fájlkezelés és a jegypénztár tartós tárolása.

1. Csomagold ki új, üres munkamappába. A HU és EN csomagot külön tartsd.
2. Nyisd meg a mappát InnoAgent-munkaterületként a korábban használt beállítással.
3. Írd: **„Kezdjük a 10. C++-gyakorlatot!”**
4. A hallgató írja és menti az új kódot; egyszerre egy `.cpp` fájlt futtat a RUN gombbal.

Az első blokkban négy alapozó feladat, a másodikban hat összefüggő projektrész, a harmadikban 20 rögzített kérdés következik. Nincs házi feladat és külön pluszfeladatsor. Az időkeret támpont: a befejezetlen feladatot nem jelöljük késznek.

A négy G10-forrás csak leforduló kezdőfájl. A P10-forrás tartalmazza a korábbról ismert jegy- és pénztárosztály alapműveleteit, így a teljes 9. leckét nem kell újra megírni. **Fájlmentést, betöltést és jelentést nem tartalmaz:** ezeket te készíted el. A HTML mérési naplója nem helyettesíti ezt a feladatot: itt fejléc, sor–szék tartomány, ismétlődő helyfoglalás és eltérő üresfájl-szabály is van.

| Fájl | Szerep |
|---|---|
| agent.md | A tutor működésének útmutatója |
| LECKE_UTASITASOK.md | G10_01–04 feladatok és próbák |
| MINTAKODOK.md | Teljes analóg példák; nem célmegoldások |
| PROJEKT.md | P1–P6 követelményei |
| TANULOI_MUNKALAP.md | Gyors fogalmi és fájlformátum-áttekintő |
| ZARO_TESZT.md | 20 kérdés, kulcs nélkül |
| HALADAS.json | A tutor által vezetett folytatási állapot |
| *.txt | Projekt- és feldolgozási próbaadatok; nem C++ források |

A ZIP nem telepíti és nem konfigurálja az InnoAgentet. A munkaterületi utasítások betöltése az alkalmazás beállításától függ. Az oktatói csomagot **ne** másold ebbe a munkamappába.

A relatív fájlút a program munkakönyvtárához tartozik. Ha a mellékelt ok.txt nem található, előbb a RUN munkakönyvtárát tisztázzátok; ne a betöltőt írjátok át az adathiba elfedésére. Új fájl létrehozása után szükség lehet a fájlnézet frissítésére. A próbák Linux/GCC, C++20 és LF sorvégek mellett ellenőrzöttek.

RUN-hiba esetén, a csomag mappájában megnyitott terminálban például:
`g++ -std=c++20 -Wall -Wextra -Wpedantic G10_01_mentes.cpp -o g01 && ./g01`

Csak sikeres fordítás után futtass. Az öt forrást ne fordítsd egyetlen programba: mindegyiknek saját main-je van.
