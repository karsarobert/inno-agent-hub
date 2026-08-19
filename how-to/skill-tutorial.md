# Saját tanulási Agent létrehozása az Inno Agenttel

**Verzió:** v0.2.3 · 2026. június 7. · A Kelet-kínai Tanárképző Egyetem Sanghaji Intelligens Oktatási Kutatóintézete

Ez az útmutató egy „angol nyelvvizsgára felkészítő munkaterület” példáján mutatja be, hogyan határozható meg a munkaterület kontextusa az `agent.md` fájllal, hogyan adhatók hozzá speciális képességek a `.skills/` könyvtárban, és hogyan hozható létre egyedi viselkedésű tanulási Agent egy konkrét munkaterületen.

---

## 1. Tervezési alapelvek

A rendszerüzenet két szakaszban áll össze, amelyek eltérő időpontban kerülnek be a kontextusba:

```
━━ A beszélgetés létrehozásakor rögzítve (Pi SDK) ━━━━━━━━━━━━━━━

  INNO alap-rendszerüzenet
    ↓
  Globális Skillek           ← A Készségek panelen telepíthetők,
    ↓                            minden munkaterület közösen használja őket
  Aktuális dátum + munkakönyvtár

━━ Dinamikus beillesztés minden körben (before_agent_start hook) ━━

  L1 kontextuscsomag (tanulási célok / tudásszint / tévképzetek / preferenciák)
    ↓
  Munkaterület-kontextus      ← A munkaterülethez tartozik,
    ├── agent.md                 minden körben újra beolvasódik
    │                            a munkaterület gyökerében, közvetlenül írható,
    │                            nem kell feltölteni
    └── .skills/              ← A munkaterület eszköztárának ✦ gombjával
    ↓                            feltöltött Skill-csomagok
  L3 beszélgetések közötti felidézés
    ↓
  A legutóbbi kódfuttatás adatai
```

**Két fájl, két külön belépési pont — nem cserélhetők fel:**

| Fájl | Helye | Létrehozása | Mit határoz meg? |
|---|---|---|---|
| `agent.md` | A munkaterület gyökérkönyvtára | Létrehozhatja az Agent, vagy közvetlenül megírható a beszélgetésben | A munkaterület személyisége: tanulási háttér, preferenciák, fájlok leírása |
| `.skills/<név>/SKILL.md` | A munkaterület `.skills/` alkönyvtára | `.md` vagy `.zip` feltöltése az eszköztár ✦ gombjával | Speciális képesség: aktiválási feltételek, formátumszabályok, munkafolyamatok |

---

## 2. Új munkaterület létrehozása

1. Kattints a bal oldali beszélgetéssáv **alján** az „**+ Új beszélgetés**” gombra.
2. Válaszd az „**Új munkaterület**” lehetőséget, és add meg az `ielts-prep` nevet.
3. Kattints a „Létrehozás” gombra.

![Új munkaterület párbeszédablaka: az ielts-prep név megadása, majd a Létrehozás gomb](./assets/01_new_workspace.png)

---

## 3. Az agent.md létrehozása

Az `agent.md` fájl a munkaterület **gyökérkönyvtárába** kerül, és nem a Skill-feltöltési folyamaton keresztül kell hozzáadni. Kétféleképpen hozható létre:

**A módszer: létrehozás az Agenttel (ajánlott)**

Másold be az alábbi sablont egy új beszélgetés beviteli mezőjébe, majd küldd el:

```
Hozd létre az agent.md fájlt az aktuális munkaterület gyökérkönyvtárában
az alábbi tartalommal:

## Angol nyelvvizsgára felkészítő munkaterület

A tanuló háttere: középfokú angol nyelvtudás, a cél IELTS 7-es eredmény,
a felkészülési idő körülbelül 3 hónap.
Fő tanulási területek: tudományos szókincs, összetett mondatok megértése,
hosszabb esszék írása.

### Tanítási preferenciák
- Új szavak: először a magyar jelentés és a szófaj, majd egy példamondat
  az eredeti szövegből
- Összetett mondatok: először a mondatszerkezet jelölése
  (alany/állítmány/tárgy/határozó), majd a teljes mondat fordítása
- Gyakorlás: főként hibajavítás és mondatalkotás, kevés feleletválasztós feladat

### A munkaterület fájljai
- cards/   Szókincsismétlő kártyák (Anki CSV-formátum)
- notes/   Részletes szövegfeldolgozási jegyzetek
```

Az Agent meghívja a fájlíró eszközt, az `agent.md` pedig megjelenik a jobb oldali munkaterületi fájlfában, a gyökérkönyvtárban.

**B módszer: kézi létrehozás szövegszerkesztővel**

Mentsd el a fenti sablont `agent.md` néven egy tetszőleges szövegszerkesztővel — például a VS Code-dal vagy a Jegyzettömbbel —, majd húzd a fájlt a jobb oldali munkaterületi fájlfa üres területére. Ügyelj arra, hogy ne legyen kijelölve alkönyvtár: így a fájl a munkaterület gyökérkönyvtárába kerül. Ha a `.skills/` könyvtár van kijelölve, a rendszer Skill-csomagként dolgozza fel.

![Az Agent létrehozta az agent.md fájlt; a jobb oldali fájlfa és a beszélgetés a fájl összefoglalóját mutatja](./assets/02_agent_create.png)

> **Megjegyzés:** Az `agent.md` egyszerű Markdown-fájl, nincs szüksége frontmatterre. Beillesztéskor a rendszer automatikusan hozzáadja a `# Munkaterület-kontextus (agent.md)` címet.

---

## 4. Szókártyakészítő Skill feltöltése

A kártyagenerátor egy speciális képesség. A munkaterület eszköztárának **✦ gombjával** tölthető fel, és a `.skills/` könyvtárba települ.

### 4.1. A Skill-fájl előkészítése

Hozz létre egy `card-maker.md` nevű fájlt egy szövegszerkesztőben, és írd meg a saját igényeid szerint. Az alábbi példa közvetlenül kimásolható és használható. Az egyetlen kötelező követelmény, hogy a fájl elején szerepeljen egy `---` jelek közé zárt frontmatter. Enélkül a rendszer feltöltéskor általános leírást hoz létre, ezért az Agent nem tudja pontosan felismerni a képességet.

````markdown
---
name: card-maker
description: Az angol tananyag új szavait Anki-kompatibilis szókártyákká alakítja
---

## Szókártyakészítő

### Aktiválási feltételek

Amikor a felhasználó azt kéri, hogy „készíts belőle kártyákat”,
„gyűjtsd ki az új szavakat”, „készíts szókártyákat” vagy „Anki-kártyákat kérek”,
kapcsolj kártyakészítő módba.

### Kártyaformátum

Minden kártya formátuma: `szó vagy kifejezés;szófaj magyar jelentés | eredeti példamondat;címkék`

Példasor:

```
ubiquitous;adj. mindenütt jelen lévő | Smartphones have become ubiquitous in daily life.;ielts academic
```

Szabályok:
- A példamondat lehetőleg a felhasználó által megadott eredeti szövegből származzon.
  Ha nincs eredeti szöveg, alkoss az IELTS témavilágához illő mondatot.
- A címkék mindig tartalmazzák az `ielts` címkét és egy tartalmi címkét,
  például `technology` vagy `environment`.
- Egyszerre legfeljebb 20 kártya készülhet. Kifejezés esetén a teljes kifejezés
  kerüljön a kártya előoldalára; ne bontsd részekre.

### Fájlműveletek

Írd az eredményt a `cards/<forrás-témája>.csv` fájlba. A fájl fejléce mindig:

```
#separator:Semicolon
#html:false
Szó vagy kifejezés;Jelentés és példamondat;Címkék
```

Elkészítés után közöld a fájl elérési útját és a kártyák számát, valamint írd le
az Anki-importálás módját: File → Import, elválasztójel: „;”.

### Kapcsolódás a memóriához

- Archiváld a forrásszöveget az `l2_archive` meghívásával,
  `[IELTS-olvasás] A szöveg témája` címformátumban.
- Hívd meg a `record_learning_event` eszközt `concept_explained` eseménnyel,
  a `mastery_delta` értéke legyen 0.01.
````

### 4.2. Feltöltés a munkaterületre

1. Válts a jobb oldali „**Előnézet**” lapra, és nyisd meg a munkaterületi fájlfát.
2. Kattints a fájlfa eszköztárának jobb felső **✦** (Sparkles) gombjára. Az elemleírás szövege: „Skill-csomag (.zip/.md) feltöltése a .skills könyvtárba”.
3. Válaszd ki a `card-maker.md` fájlt.
4. A feltöltés után megjelenik a fájlfában a `.skills/card-maker/SKILL.md` fájl.

![Feltöltés után a fájlfa a .skills/card-maker/SKILL.md fájlt, az előnézeti panel pedig a Skill tartalmát mutatja](./assets/03_skill_uploaded.png)

A feltöltés utáni könyvtárszerkezet:

```
workspace/
└── ielts-prep/
    ├── agent.md              ← Munkaterület-kontextus (a 3. lépésben létrehozva)
    └── .skills/
        └── card-maker/
            └── SKILL.md      ← Szókártyakészítő képesség (a 4. lépésben feltöltve)
```

### 4.3. Ellenőrzés

Hozz létre **új beszélgetést**, rendeld hozzá az `ielts-prep` munkaterülethez, majd küldd el ezt az üzenetet:

```
Milyen speciális képességeid vannak ezen a munkaterületen?
```

Az Agent válaszának egyaránt ismertetnie kell az angol nyelvvizsgára felkészítő munkaterület hátterét — az `agent.md` alapján — és a `.skills/card-maker/` könyvtárból származó szókártyakészítő képességet.

---

## 5. Teljes folyamat bemutatása

### 5.1. Egy szövegrészlet részletes feldolgozása

Küldd el ezt az üzenetet:

```
Dolgozd fel részletesen az alábbi szöveget, különös figyelmet fordítva
az új szavak magyarázatára:

The proliferation of renewable energy sources has been one of the most
significant developments in addressing climate change. Solar and wind power,
once considered too intermittent and costly to be viable alternatives to
fossil fuels, have become increasingly competitive due to technological
advancements and economies of scale.
```

Az Agent az `agent.md` fájlban megadott preferenciák szerint válaszol: a `proliferation`, `intermittent`, `viable` és más új szavaknál először megadja a magyar jelentést és a szófajt, majd példaként idézi az eredeti mondatot.

![Az Agent szavanként magyarázza el az új kifejezéseket az agent.md fájlban beállított „magyar jelentés + eredeti példamondat” formátumban](./assets/04_vocab_explain.png)

### 5.2. Szókártyák létrehozása

A részletes feldolgozás után küldd el ezt az üzenetet:

```
Készíts szókártyákat a szöveg új szavaiból.
```

Az Agent aktiválja a `card-maker` képességet, és például a következő eredményt adja:

```
Elkészült 6 szókártya. Fájl: cards/climate-change.csv

Előnézet:
1. proliferation
   → n. gyors elterjedés; megsokszorozódás | The proliferation of renewable energy sources has been significant.
   Címkék: ielts environment

2. intermittent
   → adj. időszakos; szakaszos | Solar power was once considered too intermittent to be viable.
   Címkék: ielts environment
… (összesen 6 kártya)

A forrás archiválva: [IELTS-olvasás] Climate Change and Renewable Energy
Anki-importálás: File → Import → cards/climate-change.csv, elválasztójel: „;”
```

![A kártyagenerálás összefoglaló táblázata; a jobb oldali fájlfában megjelent a cards/climate-change.csv](./assets/05_cards_result.png)

---

## 6. Továbbfejlesztés és karbantartás

| Módosítási igény | Teendő |
|---|---|
| Tanulási háttér vagy tanítási preferenciák módosítása | Szerkeszd közvetlenül az `agent.md` fájlt; a változás új beszélgetésben lép életbe. |
| A kártyaformátum vagy az aktiválási feltételek módosítása | Kattints a munkaterületi fájlfában a `.skills/card-maker/SKILL.md` fájlra, módosítsd a jobb oldali szerkesztőben, majd mentsd. A változás új beszélgetésben lép életbe. |
| Új speciális képesség hozzáadása | Készíts egy új, frontmattert tartalmazó `<név>.md` fájlt, majd töltsd fel a ✦ gombbal. |
| Egy képesség letiltása | Töröld a `.skills/<név>/` könyvtárat. |

A rendszer mindkét fájlt valós időben, minden `before_agent_start` eseménynél újra beolvassa, ezért a módosítások után nem kell újraindítani a szolgáltatást.

---

## 7. Globális Skill: minden munkaterületen használható képesség

A munkaterület `agent.md` fájlja és `.skills/` könyvtára csak az adott munkaterülethez kapcsolt beszélgetésekre érvényes. Ha egy képességre **minden munkaterületen szükség van**, globális Skillként kell telepíteni.

### 7.1. Mikor érdemes globális Skillt használni?

| Felhasználási helyzet | Leírás |
|---|---|
| Általános eszközök | Webes keresés, dokumentumformátumok átalakítása, kódfuttatás támogatása stb. |
| Projektek közötti tanulási szabályok | Például: „Az Agent minden munkaterületen adjon automatikusan egy gyakorlófeladatot a fogalom elmagyarázása után.” |
| Szervezeti vagy csapatszintű szabályok | Több felhasználó közös Inno-példánya esetén egységes válaszstílus vagy munkafolyamat. |

Nem érdemes globális Skillként kezelni a projektspecifikus formátumszabályokat vagy egy adott munkaterület tanulási hátterét. Ezekhez az `agent.md` vagy a munkaterület `.skills/` könyvtára a megfelelő hely.

### 7.2. Létrehozás és feltöltés

A globális Skill fájlformátuma teljesen megegyezik a munkaterületi Skillével, és ugyanúgy kötelező a frontmatter:

```markdown
---
name: grammar-checker
description: Ellenőrzi az angol szöveg nyelvtani hibáit, és javítási javaslatokat ad
---

## Nyelvtani ellenőrző

Ha a felhasználó angol mondatot vagy bekezdést küld, sorold fel külön-külön
a nyelvtani hibákat, nevezd meg a hibatípust, és add meg a javított mondatot.
```

A feltöltés lépései:

1. Kattints a jobb oldali panel tetején a „**Készségek**” lapra.
2. Kattints a jobb felső „**Feltöltés**” gombra.
3. Válaszd ki a `.md` vagy `.zip` fájlt.
4. A Skill megjelenik a listában, „Engedélyezve” állapottal.

![Készségek panel: a grammar-checker telepítve van; a jobb felső Feltöltés és Újratöltés gomb jól látható](./assets/06_skills_panel.png)

### 7.3. Beillesztési időpont és eltérés a munkaterületi Skilltől

| | Globális Skill | Munkaterületi `.skills/` |
|---|---|---|
| Telepítési hely | `~/.inno-agent/skills/` | `workspace/<név>/.skills/` |
| Feltöltési hely | A jobb oldali Készségek lap Feltöltés gombja | A munkaterületi fájlfa ✦ gombja |
| Beillesztés időpontja | **A beszélgetés létrehozásakor rögzül**, utána nem változik | Minden `before_agent_start` eseménynél dinamikusan beolvasódik |
| Hatókör | Minden munkaterület minden beszélgetése | Csak az adott munkaterülethez kapcsolt beszélgetések |
| Módosítás érvényesítése | Újra fel kell tölteni, majd **új beszélgetést** kell létrehozni | A fájl közvetlenül szerkeszthető, majd új beszélgetést kell létrehozni |

> **Megjegyzés:** A globális Skill a beszélgetés létrehozásakor kerül a kontextusba. Ha egy beszélgetés közben módosítod vagy újra feltöltöd, a már létező beszélgetésre ez nem lesz hatással; az új verzió használatához új beszélgetést kell létrehozni.

### 7.4. Engedélyezés, letiltás és törlés

A Készségek panel Skill-listájában:

- **Engedélyezés/letiltás:** kattints az elem jobb oldalán lévő kapcsolóra. A beállítás a következő új beszélgetésben lép életbe.
- **Törlés:** kattints a törlés ikonra; ezzel eltávolítod a Skillt a globális skills könyvtárból.
- **Újratöltés:** kattints az eszköztár „Újratöltés” gombjára az összes Skill ismételt betöltéséhez. A meglévő beszélgetéseket ez nem érinti.

---

## 8. Gyakori kérdések

**K: Miért jelenik meg a Skill feltöltése után a description mezőben egy általános, „Project skill uploaded for...” jellegű leírás?**

A feltöltött `.md` fájlból hiányzik a frontmatter, ezért a rendszer automatikusan általános leírást készített. Add hozzá a fájl elejéhez az alábbi részt, majd töltsd fel újra:

```
---
name: a-skill-neve
description: A Skill funkciójának leírása
---
```

**K: Véletlenül Skillként töltöttem fel az agent.md tartalmát. Hogyan törölhetem?**

Keresd meg a munkaterületi fájlfában a `.skills/agent/` könyvtárat, és töröld az egész könyvtárat. Ezután a 3. fejezetben leírt módon hozd létre újra az `agent.md` fájlt a gyökérkönyvtárban az Agent segítségével.

**K: Módosítottam az agent.md vagy a SKILL.md fájlt, de a változás az új beszélgetésben sem jelent meg. Mi lehet az oka?**

Ellenőrizd a következőket:

1. A fájl a megfelelő elérési útra került: az `agent.md` a gyökérkönyvtárban, a `SKILL.md` pedig a `.skills/<név>/SKILL.md` útvonalon található.
2. A beszélgetés az `ielts-prep` munkaterülethez van kapcsolva.
3. Valóban **új beszélgetést** hoztál létre, nem a korábbit folytattad.

**K: Milyen hosszú lehet az agent.md?**

Összpontosíts a háttérre és a preferenciákra; lehetőleg maradjon 300 szó alatt. A részletes műveleti szabályokat — formátumokat és aktiválási feltételeket — helyezd a `.skills/` könyvtárba. Az `agent.md` csak azokat az információkat tartalmazza, amelyeket az Agentnek minden beszélgetésben ismernie kell.

**K: A ✦ gomb csak .md fájlokat fogad el?**

Nem. `.md` és `.zip` fájlok is feltölthetők. A `.zip` csomagnak tartalmaznia kell egy `SKILL.md` fájlt; ez akkor hasznos, ha a Skillt és a hozzá tartozó segédfájlokat együtt szeretnéd csomagolni.

---

*Inno Agent v0.2.3 · A Kelet-kínai Tanárképző Egyetem Sanghaji Intelligens Oktatási Kutatóintézete*