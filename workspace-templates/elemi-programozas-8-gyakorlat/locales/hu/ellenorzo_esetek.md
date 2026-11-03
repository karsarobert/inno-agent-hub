# EP_08 – Normatív ellenőrző esetek

Ezek elvárt eredmények, nem elvégzett tanulói futások. A próba mindig az akkori kódhoz és bemenethez tartozik. Az ismert próbát csak érintő módosítás vagy ellentmondás esetén ismételjük. A szótár kulcssorrendje és a tételsor jelentését nem változtató szóköz nem önálló értékelési szempont; a rekordelválasztó és a sortörés funkciója viszont számít.

## A1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A1.1 | `rendelesek.txt` | `["kávé", "szendvics", "kávé", "üdítő"]`, darab 4. A forrás 5 fizikai sora közül az üres kimarad. |
| A1.2 | `rendeles_valtott.txt` | `["tea", "víz", "tea"]`, darab 3. Csak a fájlnév változik. |
| A1.3 | `ures.txt` | `[]`, darab 0; nincs hiba. |

## A2

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A2.1 | `velemenyek.txt`; `{ "finom", "gyors", "olcsó" }` | `{"finom": 2, "gyors": 2, "olcsó": 0}`. Más szó nem kulcs. A szótár sorrendje közömbös. |
| A2.2 | `velemeny_rovid.txt`; ugyanaz a kulcsszóhalmaz | `{"finom": 1, "gyors": 2, "olcsó": 1}`. A csak írásjelből álló darabok nem számítanak. |
| A2.3 | `ures.txt`; ugyanaz a kulcsszóhalmaz | `{"finom": 0, "gyors": 0, "olcsó": 0}`; nem üres szótár. |
| A2.4 | `velemenyek.txt`; `{"kávé", "drága", "hiányzik"}` | `{"kávé": 2, "drága": 1, "hiányzik": 0}`. A kulcsszavak paraméterből származnak. |

## A3.a

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.a.1 | Az A1 saját függvénye; `rendelesek.txt`; alapárak | Négy tételsor, ebben a sorrendben: `kávé: 450 Ft`, `szendvics: 890 Ft`, `kávé: 450 Ft`, `üdítő: 390 Ft`. Mindegyik külön sor; végső összesítő még nem követelmény. |

## A3.b

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| A3.b.1 | Az alapadatok teljes blokkja | A négy tételsor után `Összesen: 2180 Ft`. Összesen 5, sortöréssel lezárt sor. |
| A3.b.2 | Ugyanazt a blokkot készítsd el még egyszer | Továbbra is ugyanaz az 5 sor; nincs duplázódás. |
| A3.b.3 | A kosár forrása `ures.txt` | A cél egyetlen sora `Összesen: 0 Ft`. Az előző tételek eltűnnek. |
| A3.b.4 | A kosár forrása `rendeles_valtott.txt`; az árjegyzékben a tea árát előbb állítsd 400-ra | Tételárak 400, 0, 400 Ft; utolsó sor `Összesen: 800 Ft`. Nem változik a feldolgozó kód. |

## B1.a

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.a.1 | Új munkatérben eladasok.txt még nincs. Alapárak, kosár `["kávé", "tea"]`; mentes_bekapcsolva=True; egy futás | A fájl két sora: `kávé;450` és `tea;350`. Mindkettő sortöréssel lezárt. A B1.b kiírása most még helykitöltő. |
| B1.a.2 | Ugyanazzal a kóddal/adattal még egy futás, a fájl megtartásával | A fájl négy sora a két előző sor kétszeri ismétlése. A korábbi sorok megmaradnak. A `naplo_proba.txt` ennek változatlan ellenőrző mása. |

## B1.b

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| B1.b.1 | Előbb mentes_bekapcsolva=False; naplo_fajl="naplo_proba.txt"; alapárak | Visszatérés `(4, 1600)`; a fájl tartalma változatlan. |
| B1.b.2 | False marad; naplo_fajl="naplo_regi_arak.txt"; a kávé jelenlegi árát állítsd 999-re | `(3, 1150)`; a régi, fájlban tárolt 400, 450, 300 Ft számít. Az aktuális árjegyzék nem adatforrás. |
| B1.b.3 | False marad; naplo_fajl="ures.txt" | `(0, 0)`; a bemeneti fájl továbbra is 0 bájtos. |

## Z1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| Z1.1 | `eladas_minta.txt`; keresett="kávé" | Tuple `(2, 850)`; jelentés: Termék: kávé / Eladott darab: 2 / Bevétel: 850 Ft, három külön sorban. |
| Z1.2 | Ugyanaz a fájl; keresett="víz" | `(1, 0)`; a nulla árú eladás is egy darab. A jelentés az új adatot tartalmazza. |
| Z1.3 | Ugyanaz a fájl; keresett="kakaó" | `(0, 0)`; a jelentés a keresett kakaó nevét és a két nullát tartalmazza. |
| Z1.4 | `ures.txt`; keresett="kávé" | `(0, 0)`, nincs hiba; háromsoros friss jelentés készül. |
| Z1.5 | `eladas_valtott.txt`; keresett="kávé" | `(3, 1050)`; a jelentésben 3 és 1050 Ft. Csak a bemenet és a keresett paraméter változik. |

## C1

| Próba | Adat / végrehajtás | Elvárt viselkedés |
| --- | --- | --- |
| C1.1 | `eladas_minta.txt` | Az adatszótár: kávé → (2,850), tea → (1,350), víz → (1,0), szendvics → (1,890). A riport első sora `termek;darab;bevetel`, majd a kulcsok `sorted` sorrendjében kávé, szendvics, tea, víz. |
| C1.2 | `ures.txt` | Üres szótár; a riport csak a sortöréssel lezárt fejlécet tartalmazza. |
| C1.3 | `eladas_valtott.txt` | kávé → (3,1050), tea → (2,670); két adatsor a fejléc után. Korábbi riportsor nem marad meg. |
