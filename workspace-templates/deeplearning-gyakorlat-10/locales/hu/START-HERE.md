# Indítás · 10. gyakorlat

1. Csomagold ki a ZIP-et. Nyisd meg a `PTE_DL10_MAGYARAZHATOSAG.ipynb` fájlt Colabban a notebook megnyitása/feltöltése lehetőséggel, vagy helyi Jupyterben. A kódot ott futtatod, az Innoagenttel megbeszéled.
2. Colabban válassz GPU-t: Futtatókörnyezet → Futtatókörnyezet típusának módosítása → GPU → Mentés. E01 ténylegesen ellenőrzi; üres GPU-listánál megáll. Helyi CPU működhet, de a teljes képi kinyerés lényegesen lassabb.
3. Kezdés az oktató magyar tutorjával: „Megnyitottam a 10. gyakorlat notebookját, kezdjük E01-gyel.” Ha már lefutott, a környezet/TF/GPU sorokat küldd el.
4. Egyszerre csak az aktuális cella. Minden kód teljes; nem kell visszaküldeni változatlanul. Küldd a kért rövid kimenetet és értelmezést. K01, C08, Z01 beszélgetés.
5. C01 automatikusan letölti a két mintaképet és a JSON-t, ha az assets nincs a notebook mellett. A csomagban helyi másolat is van. A01 a forrás CSV-jét és 239 MB-os képarchívumát tölti le; kicsomagolva további hely kell.

Az assets, dl10_data, dl10_results mappák a notebook aktuális munkakönyvtárába kerülnek. A F02 gyorsítótára a dl10_results/feature_cache; a kód a valódi kinyerést és cache-találatot külön jelzi. Futtatókörnyezet-váltás Colabban fájlokat és változókat törölhet.

Letöltési kvóta/hálózati hibánál az oktató a forrásnotebookból ismert labels.csv és final_files.zip pontos fájljait előre a dl10_data mappába helyezheti. Ez induláskori technikai előkészítés; a végén nincs fájlbeadás. Az A01 ellenőrzőösszege helyi fájlokra is érvényes. Eltérő archívumot ne nevezz ugyanannak az adatváltozatnak.

Újraindításkor: FOLYTATAS.md. Saját célú mentés opcionális; nincs beadás, megosztási link vagy mentési igazolás.

Helyi környezethez az oktató használhatja a requirements.txt-t; terminálhasználat nem tanulói feladat. Az élő Innoagent- és Colab GPU-felületet órakezdés előtt külön próbáld ki. A csomag nem hoz létre távoli agentet.
