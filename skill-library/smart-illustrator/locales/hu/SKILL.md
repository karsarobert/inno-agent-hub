---
name: smart-illustrator
category: Tartalomkészítés
description: >-
  Intelligens illusztráció- és PPT infografika-generátor, három móddal: (1) Cikkillusztráció – cikk elemzése alapján illusztrációk készítése; (2) PPT/Slides – kötegelt infografikák generálása; (3) Cover – borítókép készítése. Alapértelmezés szerint képet készít, `--prompt-only` csak promptot állít elő, támogatja a Bento Grid funkcióbemutató képek stílusát (`--style bento`). Trigger szavak: illusztráció, képek, PPT, slides, borítókép, thumbnail, cover, bento grid, funkcióbemutató kép; feature showcase.
---

# Smart Illustrator – Intelligens illusztráció- és PPT generátor

## ⛔ Kötelező szabályok (megsértés = sikertelen feladat)

### 1. szabály: A felhasználó által megadott fájl = a feldolgozandó cikk

```
/smart-illustrator SKILL_05.md      → SKILL_05.md a cikk, ehhez készül illusztráció
/smart-illustrator README.md        → README.md a cikk, ehhez készül illusztráció
/smart-illustrator whatever.md      → whatever.md a cikk, ehhez készül illusztráció
```

**Bárhogy is hívják a fájlt, az a cikk, amelyhez illusztrációt kell készíteni, nem a Skill konfigurációja.**

### 2. szabály: A style fájlt kötelezően be kell olvasni

Bármilyen kép prompt elkészítése előtt **kötelezően be kell olvasni** a megfelelő style fájlt:

| Mód | Kötelezően beolvasandó fájl |
|------|---------------|
| Cikkillusztráció (alapértelmezett) | `styles/style-light.md` |
| Cover borítókép | `styles/style-cover.md` |
| `--style dark` | `styles/style-dark.md` |
| `--style bento` | `styles/style-bento.md` |

**Tilos saját System Promptot írni.**

❌ Hibás: `"Te egy szakmai infografika-tervező vagy..."` (saját alkotás)
✅ Helyes: a style fájl kódblokkjából kinyert System Prompt

---

## Használat

### Cikkillusztráció mód (alapértelmezett)

```bash
/smart-illustrator path/to/article.md
/smart-illustrator path/to/article.md --prompt-only    # Csak promptot ad ki
/smart-illustrator path/to/article.md --style dark     # Sötét stílus
/smart-illustrator path/to/article.md --no-cover       # Nem készít borítókép
```

### PPT/Slides mód

```bash
# Alapértelmezett: közvetlenül képet generál
/smart-illustrator path/to/script.md --mode slides

# Csak JSON prompt (nem hív API-t)
/smart-illustrator path/to/script.md --mode slides --prompt-only
```

**Alapértelmezett viselkedés**: Gemini API hívásával kötegelt infografikák generálása.
**`--prompt-only`**: JSON prompt kiírása és **automatikus másolása a vágólapra**, közvetlenül beilleszthető a Gemini Webbe kézi generáláshoz.

**PPT JSON formátum** (`--prompt-only` esetén kerül kiírásra):

```json
{
  "instruction": "Készítsd el egymás után a következő N darab önálló infografikát.",
  "batch_rules": { "total": "N", "one_item_one_image": true, "aspect_ratio": "16:9" },
  "style": "[a styles/style-light.md fájlból kiolvasott teljes tartalom]",
  "pictures": [
    { "id": 1, "topic": "Borító", "content": "Sorozat neve\n\nN. szakasz: Cím" },
    { "id": 2, "topic": "Téma", "content": "Eredeti tartalom" }
  ]
}
```

### Cover mód

```bash
/smart-illustrator path/to/article.md --mode cover --platform youtube
/smart-illustrator --mode cover --platform youtube --topic "Claude 4 mély értékelés"
```

**Platform méretek** (a kimenet minden esetben 2K felbontású):

| Platform | Kód | Képarány |
|------|------|--------|
| YouTube | `youtube` | 16:9 |
| Hivatalos fiók | `wechat` | 2.35:1 |
| Twitter | `twitter` | 1.91:1 |
| Xiaohongshu | `xiaohongshu` | 3:4 |

---

## Paraméterek

| Paraméter | Alapértelmezett | Leírás |
|------|--------|------|
| `--mode` | `article` | `article` / `slides` / `cover` |
| `--platform` | `youtube` | Borítókép platformja (csak cover módban) |
| `--topic` | - | Borítókép témája (csak cover módban) |
| `--prompt-only` | `false` | Prompt kiírása a vágólapra, API hívása nélkül (minden módban használható) |
| `--style` | `light` | Stílus: `light` / `dark` / `minimal` / `bento` |
| `--no-cover` | `false` | Nem készít borítókép |
| `--ref` | - | Referenciakép elérési útja (többször is használható) |
| `-c, --candidates` | `1` | Jelöltképek száma (maximum 4) |
| `-a, --aspect-ratio` | - | Képarány: `16:9` (szöveges illusztráció/borítókép alapértelmezett), `3:2` (alternatív fekvő), `3:4` (csak álló platformok) |
| `--engine` | `auto` | Motor kiválasztása: `auto` (automatikus) / `mermaid` / `gemini` / `excalidraw` |
| `--mermaid-embed` | `false` | Mermaid kimenet kódblokként PNG helyett (régi viselkedés) |
| `--save-config` | - | Mentés projekt konfigurációba |
| `--no-config` | `false` | config.json letiltása |

> **`--no-config` hatóköre**: csak a `config.json`-t tiltja le, **nincs hatással** a `styles/style-*.md` fájlokra.

---

## Konfigurációs fájlok

**Prioritás**: CLI paraméter > projekt szint > felhasználói szint

| Szint | Elérési út |
|------|------|
| Projekt szint | `.smart-illustrator/config.json` |
| Felhasználói szint | `~/.smart-illustrator/config.json` |

```json
{ "references": ["./refs/style-ref-01.png"] }
```

---

## Háromszintű illusztrációs motor

| Prioritás | Motor | Alkalmazási eset | Kimenet |
|--------|------|---------|------|
| **1** | Gemini | Metaforaképek, kreatív képek, borítókép, olyan fogalmak, amelyek nem fejezhetők ki diagrammal | PNG |
| **2** | Excalidraw | Fogalmi diagramok, összehasonlító képek, egyszerű folyamatok (≤ 8 csomópont), kapcsolati ábrák, kézrajzolt stílusú vázlatok | PNG |
| **3** | Mermaid | **Kizárólag**: összetett folyamatok (> 8 csomópont), többrétegű architektúra-diagramok, több szereplős szekvenciadiagramok, többágú döntési fák | PNG |

Kiválasztási logika:
- Metafora, érzelem, kreatív kifejezés szükséges → Gemini
- Fogalmi kapcsolat, összehasonlítás, egyszerű folyamat → Excalidraw (**a legtöbb diagram-helyzetben ez az első választás**)
- **Csak** akkor, ha több mint 8 csomópont, több réteg/több szereplős összetett strukturált ábra van → Mermaid
- A Mermaid vizuális kifejezőereje korlátozott, ha Excalidraw használható, ne Mermaid-t használj
- Egyetlen cél: a cikk vonzerejének növelése

Excalidraw generálása előtt kötelezően be kell olvasni a `references/excalidraw-guide.md` fájlt.

### Mermaid sémantikus színpaletta

Minden színnek rögzített jelentése van, **kötelezően `classDef` + `class` segítségével alkalmazni**:

| Szemantika | Kitöltés színe | Szegély színe | Használat |
|------|--------|--------|------|
| input | #d3f9d8 | #2f9e44 | Bemenet, kiindulópont, adatforrás |
| process | #e5dbff | #5f3dc4 | Feldolgozás, következtetés, alapvető logika |
| decision | #ffe3e3 | #c92a2a | Döntési pont, elágazás |
| action | #ffe8cc | #d9480f | Végrehajtás, eszközhívás |
| output | #c5f6fa | #0c8599 | Kimenet, eredmény, végpont |
| storage | #fff4e6 | #e67700 | Tárolás, memória, adatbázis |
| meta | #e7f5ff | #1971c2 | Cím, csoportosítás, metaadat |

**classDef írásmód** (az ábra végére helyezendő):

```
classDef input fill:#d3f9d8,stroke:#2f9e44,color:#1a1a1a
classDef process fill:#e5dbff,stroke:#5f3dc4,color:#1a1a1a
classDef decision fill:#ffe3e3,stroke:#c92a2a,color:#1a1a1a
classDef action fill:#ffe8cc,stroke:#d9480f,color:#1a1a1a
classDef output fill:#c5f6fa,stroke:#0c8599,color:#1a1a1a
class A input
class B,C process
class D output
```

### Mermaid elrendezési szabályok

- **Elrendezési irány**: alapértelmezés szerint `TB` (fentről le), vízszintes folyamatoknál `LR`
- **Nyíl hierarchia**: `-->` fő folyamat / `-.->` opcionális/segéd útvonal / `==>` kiemelt hangsúly
- **Csoportosítás**: `subgraph` használatával a kapcsolódó csomópontok csoportosítása, rövid címmel
- **Csomópont szövege**: ≤ 8 karakter, nincs emoji, tilos a `1.` formátum (használj `①` vagy `Step 1:` formátumot)
- **Csomópontok száma**: egy ábrán legfeljebb 15 csomópont, az összetett tartalmat oszd fel több ábrára

**`--engine` paraméter**:
- `auto` (alapértelmezett): a tartalom típusa alapján automatikus választás (prioritás: Gemini > Excalidraw > Mermaid)
- `gemini`: kizárólag Gemini kényszerítése (kreatív tartalomhoz)
- `excalidraw`: kizárólag Excalidraw kényszerítése (kézrajzolt fogalmi diagramokhoz)
- `mermaid`: kizárólag Mermaid kényszerítése (műszaki dokumentációhoz)

---

## Végrehajtási folyamat

### 1. lépés: Cikk elemzése

1. Cikk tartalmának beolvasása
2. Illusztrációs pozíciók azonosítása (általában 3-5 hely)
3. Minden pozícióhoz motor meghatározása (Gemini / Excalidraw / Mermaid)

### 2. lépés: Képek generálása

#### Mermaid (strukturált ábra) → PNG

1. Mermaid kód generálása, mentés ideiglenes `.mmd` fájlként
2. A mermaid-export.ts hívása nagy felbontású PNG exportálásához:

```bash
npx -y bun ~/.claude/skills/smart-illustrator/scripts/mermaid-export.ts \
  -i {diagram neve}.mmd -o {diagram neve}.png -w 2400
```

3. PNG kép hivatkozás beszúrása a cikkbe
4. Az `.mmd` forrásfájl megőrzése későbbi szerkesztéshez

A `--mermaid-embed` paraméter használatakor közvetlenül Mermaid kódblokkot ágyazz be (régi viselkedés).

#### Excalidraw (kézrajzolt/fogalmi diagram) → PNG

1. A `references/excalidraw-guide.md` beolvasása a JSON specifikációhoz
2. Excalidraw JSON generálása, mentés `.excalidraw` fájlként
3. Az excalidraw-export.ts hívása PNG exportálásához:

```bash
npx -y bun ~/.claude/skills/smart-illustrator/scripts/excalidraw-export.ts \
  -i {diagram neve}.excalidraw -o {diagram neve}.png -s 2
```

4. PNG kép hivatkozás beszúrása a cikkbe
5. Az `.excalidraw` forrásfájl megőrzése későbbi szerkesztéshez

Ha a függőség nincs telepítve, degradáció: javasold a felhasználónak, hogy nyissa meg az excalidraw.com oldalt és exportáljon onnan.

#### Gemini (kreatív/vizuális ábra)

**Parancssablon** (HEREDOC + prompt-file használat kötelező):

```bash
# 1. lépés: prompt írása
cat > /tmp/image-prompt.txt <<'EOF'
{A style fájlból kinyert System Prompt}

**Tartalom**: {illusztráció tartalma}
EOF

# 2. lépés: script hívása
GEMINI_API_KEY=$GEMINI_API_KEY npx -y bun ~/.claude/skills/smart-illustrator/scripts/generate-image.ts \
  --prompt-file /tmp/image-prompt.txt \
  --output {kimeneti út}.png \
  --aspect-ratio 16:9
```

**Borítókép** (16:9):

```bash
cat > /tmp/cover-prompt.txt <<'EOF'
{A style-cover.md fájlból kinyert System Prompt}

**Tartalom**:
- Alapgondolat: {téma}
- Vizuális metafora: {dizájn}
EOF

GEMINI_API_KEY=$GEMINI_API_KEY npx -y bun ~/.claude/skills/smart-illustrator/scripts/generate-image.ts \
  --prompt-file /tmp/cover-prompt.txt \
  --output {cikk neve}-cover.png \
  --aspect-ratio 16:9
```

**Paraméterátadás**: a felhasználó által megadott `--no-config`, `--ref`, `-c` paramétereket át kell adni a scriptnek.

### 3. lépés: Illusztrált cikk létrehozása

Mentés `{cikk neve}-image.md` néven, tartalmazza:
- YAML frontmatter a borítókép deklarálásával
- Szöveges illusztrációk beszúrása

### 4. lépés: Kimenet megerősítése

Jelentés: hány kép készült, a kimeneti fájlok listája.

---

## `--prompt-only` mód

Amikor `--prompt-only` módot használsz, **nem hív API-t**, hanem:

1. JSON prompt generálása
2. **Automatikus másolás a vágólapra** (`pbcopy` segítségével)
3. Egyidejű mentés fájlba biztonsági mentésként

```bash
# Végrehajtás módja
echo '{generált JSON}' | pbcopy
echo "✓ A JSON prompt a vágólapra másolva"

# Egyidejű biztonsági mentés
echo '{generált JSON}' > /tmp/smart-illustrator-prompt.json
echo "✓ A biztonsági mentés elmentve: /tmp/smart-illustrator-prompt.json"
```

A felhasználó közvetlenül beillesztheti a Gemini Webbe a képek kézi generálásához.

---

## Kimeneti fájlok

```
article.md              # Eredeti cikk (nem módosítva)
article-image.md        # Illusztrált cikk
article-cover.png       # Borítókép (16:9)
article-image-01.png    # Gemini illusztráció
```
