# Inno Agent Hub

[中文](README.md) | [Magyar](README.hu.md)

> Az Inno Agent dokumentációinak, Skilljeinek és munkaterület-sablonjainak gyűjteménye — egy erőforrástár, amely segít **gyorsan elkezdeni a munkát, helyzet szerint válogatni, és bármikor hozzájárulni**.

[![主项目](https://img.shields.io/badge/main--repo-inno--agent-blue)](https://github.com/hhyqhh/inno-agent)
[![教程](https://img.shields.io/badge/docs-tutorial-green)](./how-to/skill-tutorial.md)
[![Skills](https://img.shields.io/badge/skills-library-orange)](./skill-library/)

---

## Mi ez?

Az [Inno Agent](https://github.com/hhyqhh/inno-agent) egy **helyben futó, hosszú távú memóriával rendelkező** személyes tanulási asszisztens. A „munkaterületi kontextus + Skill-csomag” összeállítással az általános LLM-et az adott tanulási helyzethez igazodó, dedikált Agentté alakítja.

Ez a repozitórium az Inno Agenthez kapcsolódó összes **külső erőforrást** gyűjti össze:

- **Hogyan használd** — bevezető oktatóanyagok, témaspecifikus útmutatók
- **Mire képes** — saját fejlesztésű / gyűjtött Skill-csomagok, azonnal használhatók
- **Hogyan építsd fel** — helyzetekhez előkészített munkaterület-sablonok (`agent.md` + Skill-összeállítások)

A főprojekt kódja a [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) repozitóriumban található; ez a repozitórium **nem tartalmaz futtatókódot**, kizárólag dokumentációt és erőforrásokat.

---

## Repozitórium-navigáció

| Könyvtár | Tartalom | Kinek ajánlott |
|---|---|---|
| 🛠 [`how-to/`](./how-to/) | Bevezető és témaspecifikus útmutatók: Skill-írás, munkaterület-konfigurálás stb. | Első alkalommal használóknak / testreszabást végzőknek |
| 🎨 [`skill-library/`](./skill-library/) | Skill-gyűjtemény leírásokkal és eredménybemutatókkal | Akik közvetlenül használni szeretnének valamit |
| 📦 [`workspace-templates/`](./workspace-templates/) | Munkaterület-sablonok: `agent.md` + `.skills` összeállítások | Akik egy kattintással szeretnének egy adott helyzethez munkaterületet létrehozni |

---

## Gyors kezdés

Válaszd ki a szerepednek megfelelő belépési pontot:

**🚀 Új felhasználó vagyok** — kezdd a [`how-to/skill-tutorial.md`](./how-to/skill-tutorial.md) dokumentummal, és az IELTS-felkészülési példát követve hozd létre az első munkaterületedet.

**🎯 Kipróbálnék egy kész Skillt** — böngészd a [`skill-library/`](./skill-library/) könyvtárat, tölts le egy Skill-csomagot, majd az útmutató alapján töltsd fel a munkaterületedre. Jelenleg a következők érhetők el:

- [`edu-solid-geometry`](./skill-library/edu-solid-geometry/) — térgeometriai feladat → Three.js-alapú interaktív feladatmegoldó oldal
- [`edu-analytic-geometry`](./skill-library/edu-analytic-geometry/) — kúpszeletfeladat → Canvas-alapú interaktív feladatmegoldó oldal

**📦 Egy adott helyzethez egy kattintással szeretnék munkaterületet létrehozni** — válassz sablont a [`workspace-templates/`](./workspace-templates/) könyvtárból, majd másold be az `agent.md` és a `.skills/` tartalmát. Jelenleg a következők érhetők el:

- [`ielts-prep`](./workspace-templates/ielts-prep/) — IELTS-angolnyelv-vizsgára felkészítő munkaterület
- **VeryMath AI4Math sorozat** (7 sablon) — a nyílt forrású [VeryMath](https://github.com/VeryMath) szervezettől; a matematikai formalizálás, tudományos cikkek olvasása és írása, számítógépes matematika, optimalizálás, automatizált kutatás, evolúciós kísérletek és más területek helyzeteit fedi le

**🧑‍🏫 Saját Skillt szeretnék írni** — olvasd el a [`how-to/skill-tutorial.md`](./how-to/skill-tutorial.md) útmutatót; bemutatja az `agent.md` és a SKILL-csomagok tervezését, valamint feltöltésük módját.

---

## A Skill és a Workspace kapcsolata

```
┌──────────────────────────────────────────────────────────┐
│  Inno Agent-munkaterület                                  │
│                                                          │
│   agent.md             ← munkaterületi kontextus         │
│                          (tanulási háttér / preferenciák)│
│   .skills/             ← célzott képességek              │
│                          (aktiválási feltételek/formátum/│
│                           folyamat)                       │
│     └─ xxx/SKILL.md                                      │
│   files/               ← a tanulási anyagaid             │
│                                                          │
└──────────────────────────────────────────────────────────┘
              ▲                       ▲
              │                       │
   workspace-templates/        skill-library/
   (teljes munkaterület         (egyetlen képesség
    átvétele)                    kiválasztása)
```

Részletekért lásd a [`how-to/skill-tutorial.md`](./how-to/skill-tutorial.md) „Tervezési alapelvek” című szakaszát.

---

## Hozzájárulás

Szívesen fogadjuk a saját Skilljeidet vagy munkaterület-sablonjaidat:

1. **Új Skill** → hozz létre egy új könyvtárat a `skill-library/` alatt, amely tartalmazza a `SKILL.md` fájlt és a szükséges `lib/scripts/template/references/` elemeket. A rendeltetést és a várt eredményt a `SKILL.md` frontmatterének `description` mezőjében írd le, továbbá vedd fel egy sorban a Skillt a `skill-library/README.md` Skill-listájába. Az eredményképeket a `skill-library/assets/<skill-name>/` könyvtárba helyezd.
2. **Új Workspace-sablon** → hozz létre egy új könyvtárat a `workspace-templates/` alatt, amely tartalmazza az `agent.md` fájlt és a `.skills/` könyvtárat; a könyvtár `README.md` fájljában ismertesd a megfelelő felhasználási helyzeteket.
3. **Oktatóanyag- vagy dokumentációjavítás** → küldj közvetlenül PR-t a `how-to/` könyvtárhoz.

> ⚠️ **Kötelező: `category` kategóriacímke** — Az Inno Agent kliens a `category` alapján csoportosítja és szűri a Skilleket / előbeállításokat; **ha nem adod meg, az elem a „Kategorizálatlan” csoportba kerül**. Új Skill vagy új Workspace-sablon beküldésekor **kötelező a `category` mezőt felvenni** a frontmatterbe / a `preset.json` fájlba. A részletes kategórialista és használat a lenti „[Kategóriacímkék (kötelező)](#kategóriacímkék-kötelező)” szakaszban található.

Beküldés előtt ellenőrizd az alábbiakat:
- **Felvetted a `category` mezőt** (lásd lent a „Kategóriacímkék” részt)
- Ne committolj helyi fájlokat, például `.DS_Store`-t vagy képernyőfelvételt (`*.mov`) (ezeket a `.gitignore` már figyelmen kívül hagyja)
- Az eredmény bemutatásához GIF-et / PNG-t használj; ne helyezz el közvetlenül videófájlokat
- Elsődlegesen kínai nyelvű dokumentációt írj; szükség esetén angol magyarázatot is mellékelj

---

## Kategóriacímkék (kötelező)

Az Inno Agent kliens a `category` alapján jeleníti meg csoportokba rendezve a Skilleket / előbeállításokat (a Skill-könyvtár böngészője és az egyszerű mód előbeállításkártyái egyaránt ezen csoportosítás szerint működnek), és támogatja a keresési szűrést. **Minden új elemnek tartalmaznia kell `category` mezőt**; ennek hiányában az elem a „Kategorizálatlan” csoportba kerül, ami jelentősen rontja a használati élményt.

### Jelenlegi kategórialista

**Skill-kategóriák** (a `SKILL.md` frontmatterében):

| Kategória | Használati helyzet |
|---|---|
| `教学辅导` | Magántanítás / feladatmegoldás / magyarázat, önálló tanulás támogatása, házi feladat javítása, vizsgatémák felbontása (pl. tutor, math-tutor, socratic-tutor, homework-grader, comment-on-docx, edu-* sorozat) |
| `内容创作` | Vizuális, képes-szöveges, prezentációs, frontendes művészeti és más kreatív eredmények előállítása (pl. baoyu-comic, smart-illustrator, frontend-design, canvas-design, theme-factory) |
| `文档处理` | Office / PDF / Markdown / weboldal → strukturált szöveg olvasása, írása és konvertálása (pl. docx, pdf, pptx, xlsx, markitdown, baoyu-url-to-markdown) |
| `研究检索` | Akadémiai keresés, internetes keresés, hivatkozáskezelés, mélyreható kutatási jelentések (pl. paper-lookup, tavily-search, citation-management, storm-research) |
| `开发工具` | LLM-alkalmazásfejlesztés, prompt engineering, MCP / Skill metaképességek, kódértelmezés és tesztelés (pl. claude-api, mcp-builder, prompt-engineer, skill-creator, understand, webapp-testing) |

**Előbeállítás-kategóriák** (a `preset.json` fájlban):

| Kategória | Használati helyzet |
|---|---|
| `教学` | Óravázlat-, feladat-, magyarázat- és oktatástámogatási munkaterületek (pl. lesson-plan, classroom-quiz, knowledge-explain, math-interactive, scenario-explain, teaching-webpage, ielts-prep) |
| `演示` | Diavetítés-, prezentáció- és megosztási oldalhoz készült munkaterületek (pl. ppt-creation) |
| `verymath` | MI-támogatott matematikai formalizálási munkaterületek (Lean 4 / mathlib környezet beállítása, tételek formalizálása, bizonyítások javítása; forrás: [VeryMath/AI4Math-Lean-Agents](https://github.com/VeryMath/AI4Math-Lean-Agents)) |

> Új kategóriára van szükséged, amely nem szerepel a táblázatban? Előbb nyiss egy issue-t megbeszélésre. **Ne hozz létre elhamarkodottan új kategóriát**, mert az kliensoldalon sok, egyetlen elemet tartalmazó, elkülönült csoportot eredményez.

### Hozzáadás módja

**Skill** — a `SKILL.md` frontmatterében a `name:` után szúrj be egy `category: <érték>` sort:

```yaml
---
name: my-awesome-skill
category: 教学辅导
description: >-
  用一段话讲清这个 skill 做什么...
---
```

**Előbeállítás** — add hozzá a `category` mezőt a `preset.json` fájlhoz (a legáttekinthetőbb, ha a `description` és az `icon` közé helyezed):

```json
{
  "id": "my-template",
  "name": "我的模板",
  "description": "一句话说明用途",
  "category": "教学",
  "icon": "book-open"
}
```

> A `category` egyszerű felső szintű sztringmező; **ne ágyazd be**, ne használj tömböt, és ne lokalizáld (a kínai címkéket kell használni, mert a kliens sztringegyezés alapján csoportosít).

---

## Kapcsolódó projektek

- [`hhyqhh/inno-agent`](https://github.com/hhyqhh/inno-agent) — főprojekt (az Inno Agent futtatókörnyezete)
- [`wy51ai/edulab`](https://github.com/wy51ai/edulab) — oktatási területhez tartozó Skillek upstream forrása
- [**VeryMath**](https://github.com/VeryMath) — AI4Math matematikai Agent; a repozitórium `verymath` kategóriájában található 7 munkaterület-sablon upstream forrása. A VeryMath az MI-Agentekkel támogatott matematikai kutatásra összpontosít, többek között Lean 4-es formalizált bizonyításra, számítógépes matematikára, matematikai optimalizálásra, tudományos cikkek olvasására és írására, valamint automatizált kutatásra. Kapcsolódó repozitóriumok:
  - [`AI4Math-Lean-Agents`](https://github.com/VeryMath/AI4Math-Lean-Agents) → `ai4math-lean-agents` sablon
  - [`AI4Math-Paper-Reading`](https://github.com/VeryMath/AI4Math-Paper-Reading) → `ai4math-paper-reading` sablon
  - [`AI4Math-Paper-Writing`](https://github.com/VeryMath/AI4Math-Paper-Writing) → `ai4math-paper-writing` sablon
  - [`AI4Math-Computational-Mathematics`](https://github.com/VeryMath/AI4Math-Computational-Mathematics) → `ai4math-computational-mathematics` sablon
  - [`AI4Math-Optimization`](https://github.com/VeryMath/AI4Math-Optimization) → `ai4math-optimization` sablon
  - [`AI4Math-Auto-Research`](https://github.com/VeryMath/AI4Math-Auto-Research) → `ai4math-auto-research` sablon
  - [`AI4Math-Evolving`](https://github.com/VeryMath/AI4Math-Evolving) → `ai4math-evolving` sablon

---

## Licenc

A dokumentáció és a Skill-tartalmak az egyes alkönyvtárakban megjelölt licencek szerint érhetők el; ha nincs külön feltüntetve, alapértelmezetten a főprojekt licence az irányadó.
