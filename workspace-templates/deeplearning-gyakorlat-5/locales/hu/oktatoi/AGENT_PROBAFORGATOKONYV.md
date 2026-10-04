# Rövid élő Innoagent-próba az óra előtt

Ezek elvárt viselkedések, nem már elvégzett élő teszt jegyzőkönyvei.
A Python-futtatások ellenőrzése külön: ELLENORZES.md.

1. **Új kezdés.** „Kezdjük a gyakorlatot!” Elvárt: bemutatkozás egyszer,
   autoencoder/ECG cél, környezetellenőrzés, várakozás. Nincs CNN vagy teljes feladatsor.
2. **Sikeres ellenőrzés.** Add meg a KÖRNYEZET RENDBEN sort. Elvárt: G01 célja,
   bemenete, 140 pont és indexelés, kulcskód, egy alapfuttatás kérése.
3. **Csak kész.** Válasz: „kész”. Elvárt: egy konkrét hiányzó kimenet bekérése;
   nincs új bevezető vagy automatikus teljesítés.
4. **Ismételt kimenet.** Ugyanazt a már elfogadott eredményt másold be kétszer.
   Elvárt: nem számít új futásnak, nem ismétli a teljes következő feladatot.
5. **Hiányzó kódmagyarázat.** Jelezd: „A fit-et nem értem.” Elvárt: bemenet=cél,
   adatcsomag és súlyfrissítés rövid tisztázása; nem indul újra a lecke.
6. **G03 előtt.** Elvárt: kimondja, hogy előre mentett valódi referencia, nem
   a hallgató legutóbbi modellje. Magyarázza abs, mean, axis=1 jelentését még a Run előtt.
7. **Indexváltás után változatlan hisztogram.** Elvárt: ez helyes működés,
   mert a teljes csoport ugyanaz; nem kér hibajavítást.
8. **Küszöb 0.025.** TP nem nő a 0.04-es eredményhez képest. Elvárt: elfogadja,
   mert már minden rendellenest jelzett az alapfutás; az FP-változást értelmezi.
9. **Hibás válasz.** „A recall azt jelenti, hány riasztás volt jogos.” Elvárt:
   udvarias javítás: ez a precision; recall a tényleges rendellenesekből indul.
10. **Záróteszt.** Egy kérdés egyszerre; helyes válasz csak a hallgató válasza
    után. „B vagy D” esetén tisztázás. A tizedik után pontszám, összegzés,
    egyértelmű lezárás; nincs házi, 11. kérdés vagy CNN-feladat.

Ha nincs elegendő időadat, az agent nem állíthatja, hogy „még 12 perced van”.
A pontozás és memória csak az alkalmazásban valóban rendelkezésre álló módon történjen.

## Az 1.1 változat külön ellenőrzései

- Minden sikeres futásra adott első válaszban önálló Nézet-frissítési emlékeztető
  van akkor is, ha csak két számot kapott vissza az agent. Képmegnyitáskor a
  megfelelő fájlt nevezi meg; nem talál ki ismeretlen futásmappát.
- A fájl megnyitásakor előbb a számozott blokkok rövid térképét magyarázza el.
  A teljes autoencoder-modellt mutatja, nem két távoli réteget szomszédként.
- Mindkét indexváltás előtt elmagyarázza: 0 az első, 3 a negyedik példa, amelyet
  most külön megvizsgálunk. Az eredeti jelértékek nem változnak.
- A 30 epochás saját futás után az osszehasonlitas.png képet használja; a két
  futás neve az ábrán szerepel. Hiányzó korábbi futást nem helyettesít észrevétlenül referenciával.
- Az axis_1.png megtekintése után megvárja, miért két külön szám a két jel átlaga.
- Precision: a 127 riasztásból indul; megértési kérdés és válasz után recall:
  a 128 valódi rendellenességből indul. A tesztet csak a két külön válasz után kezdi.
- Nem mondja, hogy G04-ben nincs hibaszámítás: a rögzített rekonstrukciókból
  ugyanazokat a hibákat újraszámítjuk. Nem mond látatlanban új részletet a görbékről.
