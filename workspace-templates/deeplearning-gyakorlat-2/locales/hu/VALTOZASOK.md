# Deep Learning 2026 – 2. gyakorlat: változások

Módszertani változat 2, a kipróbálásról kapott beszélgetés alapján.

- Minden új program kötelező bevezetése: konkrét cél, egy minta jelentése,
  bemenet, célérték, várt eredmény, tanítás vagy előreterjesztés.
- Új PROGRAM_BEMUTATOK: a hét program adatfolyamata és fontos kódblokkjai.
  A magyarázat mindig megelőzi a kérdést és az első futtatást.
- Offline szemléltető: egy súly lépése, feliratozott és léptethető 3–2–1
  hálózat, szerkeszthető bemenetek/súlyok/biasok; boradatok és osztályindexek.
- A kézi hálózatszámítás választható. Több közös bemutató, kevesebb ismételt
  kikérdezés. A 2 × 45 percet a választható kísérletek elhagyása védi.
- A programok rövid szöveges célbemutatással indulnak. A boros fájlok egy
  valódi sor bemeneteit és célját is megmutatják.
- A tanítóprogramok a napló végén kiírják a tényleges konfigurációt,
  paraméterszámot és a fontos eredményeket. A JSON is menti a paraméterszámot.
- A tutor nem fogad el igazolt módosításként pusztán egy új eredménymappát;
  ellenőrzi az aktuális konfigurációt. A változatlan metrika önmagában nem dönt.
- Hibás válaszra nincs hamis helyeslés. A segítséggel feldolgozott részt a
  zárásban megkülönböztetjük az önálló megértéstől.
- Javított fogalmi sorrend: bemeneti jellemzők → predict → softmax-vektor →
  argmax → nullától indexelt osztálycímke.
- Első naplózott futás előtt mkdir -p naplok; rövid összefoglalóhoz tail -n 18.
- A végső modellválasztást a validációs MAE indokolja. A korábbi jobb
  beállítás visszaírható; a próbák eredményei megmaradnak. Kísérleti jegyzet is készült.

A számítási és tanítási alapbeállítások változatlanok. Nincs dropout,
batch normalizáció vagy Colab. A helyi CPU-futtatás maradt az alap.
