# Upstream (eredeti inno-agent-hub) fejlesztések — elemzés és beolvasztási terv

Készült: 2026-09-27 · forrás: `origin/main` = https://github.com/Chloris-Blaxk/inno-agent-hub (35 commit, utolsó: `b01d114`)
Összehasonlítás alapja: a fork pont (`933909d`, 2026-07-.. előtti állapot)

## 1. Számok egy pillantás alatt

| Szempont | Nálunk (fork `main`) | Upstream (`origin/main`) |
|---|---|---|
| Commit a fork pont óta | 85 | 35 |
| Változott fájl a fork pont óta | 527 | 188 |
| Skill-mappa | 47 | 81 (80 `SKILL.md`) |
| Preset-mappa | 26 | 24 |
| Magyar nyelvi overlay | 46 (skill) + a kártyák hu rétege | 0 |
| Törölt fájl a fork pont óta | — | **0** |

**Ütközési felület: pontosan 1 fájl** — `workspace-templates/README.md` (1 ütköző hunk, a 65. sor környékén).
Ellenőrizve próba-merge-dzsel (`git merge --no-commit --no-ff origin/main` külön ágon, majd `--abort`):
187 fájl változott (+15 029 / −10), a gyökér `README.md` **automatikusan** összefésülődött (a mi magyar
fordítás-hivatkozásaink és az ő új metaadat-szekciójuk is benne marad), és kizárólag a
`workspace-templates/README.md` jelzett konfliktust. Minden más fájl, amit ők módosítottak, nálunk
érintetlen, és fordítva. Az upstream beolvasztása tehát gyakorlatilag konfliktusmentes, és **egyetlen
magyar réteget sem veszélyeztet** (nincs törlésük).

## 2. Amit az upstream csinált (témák szerint)

1. **Oktatáskutatási skill-csomag (a legnagyobb blokk, 29 skill).** Egy teljes `education-*` sorozat:
   kutatástervezés (qualitative/quantitative/mixed methods), adattisztítás, leíró és inferenciális
   statisztika, reliabilitás-validitás, faktoranalízis/SEM előkészítés, meta-analízis, szisztematikus
   review (PRISMA), kódolás- és kódolói megbízhatóság, tematikus elemzés, learning analytics, program- és
   szakpolitika-elemzés, irodalmi térkép, elmélet-illesztés, kutatásikérdés-generálás, mintavétel,
   kérdőív- és skála-fejlesztés, pszichometria, bizonyíték-ellenőrzés, cikk-típus útválasztó.
   (Szerzők: wirelessqa, Chloris-Blaxk.)
2. **Tanári tananyag-skillek:** `class-exam-review` (dolgozat/vizsga kiértékelése), `ketang-choubei-moxie`
   (órai feleltetés/diktálás rutin), `skill-library/assets/` alatt a hozzájuk tartozó képek/GIF-ek (10 fájl).
3. **Publikációs/tartalomkészítő skillek:** `paper-to-xhs` (cikk → Xiaohongshu-jegyzet),
   `paper-to-dialogue-video` (cikk → kétbeszélős podcast-videó felirattal), `scholar-distill`
   (kutatói profil → bizonyíték-alapú kutatóasszisztens).
4. **Platform-metaadat (ez a legfontosabb üzemeltetési újdonság):**
   - `skill-library/packs.json`: skillek csomagokba szervezve („skill pack" definíció).
   - `skill-library/scenarios.json`: forgatókönyv/featured lista (a bemutató oldal „csillagtérképe" ezt használja).
   - Mind a 78 `SKILL.md` kapott `subject:` és `kind:` frontmattert (pl. `subject: 跨学科`, `kind: 教研科研`).
   - `README.md`-ben hivatkozás az „Innoskill platformra" és a backend-integrációs útmutatóra.
5. **Bemutató weboldal:** `docs/` (galaxis-stílusú skill-böngésző, kereső, kategóriaszűrő), hozzá
   `.github/workflows/pages.yml` (GitHub Pages automatikus build), `scripts/build_skills_site.py`,
   `scripts/riso_art.py`, `scripts/{site,map}_template.html`, favicon/og kép, 404 oldal.
6. **Négy új munkaterület-preset:**
   | Preset | Név | Mit tud |
   |---|---|---|
   | `question-led-learning` | 追问式学习 („kérdés-vezérelt tanulás") | Az agent csak fogalmi magot ad, a tanuló saját kérdésekkel halad, a végén visszamondás és transzfer ellenőrzi a megértést. |
   | `task-alignment` | 任务对齐与验收 („feladat-egyeztetés és átvétel") | Bonyolult feladatoknál először feltárás + visszamondás + kérdések, majd „feladat-szerződés" rögzítése, végül bizonyíték-alapú átvétel. |
   | `adaptive-math-learning-agent` | 中小学数学错因诊断 („matematika hibadiagnózis") | Általános iskolai/középiskolai feladatok hibaelemzése, valódi hibaok igazolása, többábrázolásos magyarázat, célzott gyakorlás, transzfer-teszt. |
   | `modular-learning` | 模块化渐进学习 („moduláris haladó tanulás") | Először domain-térkép és önállóan tanulható egységek, majd a tanulói profillal és teljesítménnyel vezérelt útvonal. |

## 3. Mi érinti a mi munkánkat?

- **46 megosztott skill:** az upstream ezekben KIZÁRÓLAG frontmattert írt (`subject`/`kind`, fájlonként
  ≤4 hozzáadott sor, 0 érdemi tartalomváltozás — ellenőrizve mind a 46 esetben). Nálunk pont ezekhez a
  skillekhez van magyar overlay (`skill-library/<skill>/locales/hu/SKILL.md`). Beolvasztás után az angol
  törzs megkapja a két új mezőt, a magyar overlay nem — **ez nem ütközés**, de eldöntendő, hogy a magyar
  rétegbe is felvesszük-e a `subject`/`kind` sorokat (lásd 4. pont).
- **Az alkalmazás nem olvassa a `subject`/`kind` mezőt.** Ellenőriztem a telepített app kódjában
  (`src/content-source/`, `src/agent/`, web UI): sehol nincs ilyen mező-feldolgozás, a frontmatter az
  upstream platformjához (Innoskill) és a bemutató oldalhoz kell. Vagyis a magyar skillek ettől nem
  veszítenek funkciót; csak akkor van jelentősége, ha a kártyákat/skilleket fel akarjuk tölteni az
  upstream platformra vagy a bemutató oldalra.
- **`README.md`:** a mi változatunkban magyar nyelvű fordítások vannak (a mi utolsó commitunk:
  „docs: add Hungarian README translations"), ők közben az Innoskill-hivatkozást és a metaadat-leírást
  tették bele. A próba-merge szerint ez **automatikusan** összefésülődik (nem kell kézzel nyúlni hozzá),
  de érdemes átolvasni: a magyar fordítás-hivatkozás és az ő új szekciója is benne van.
- **`workspace-templates/README.md`:** ez az EGYETLEN ütközés (1 hunk). Nálunk a 26 kártya indexsora,
  náluk más szerkezetű lista — kézi döntés kell: a mi soraink maradnak (C++ 1–4, DL 1–4, EP, diszkrét
  matek stb.), és az övéikből csak az új elemeket vesszük át.
- **Nincs törlésük**, tehát nem tűnik el semmilyen fájlunk (sem hu overlay, sem kártya).
- **A 4 új preset kínai nyelvű**, nincs hozzájuk semmilyen lokális overlay (az upstreamnél egyáltalán nincs
  `locales/` réteg a skill-könyvtárban). Ha kellenek a tanórán, a magyarítás külön munka.
- **GitHub Pages:** a `docs/` + workflow bekerülése a forkba elindíthatja a Pages-buildet a fork repón.
  Ez nem árt, de érdemes tudni: a publikált oldal az ő tartalmukat mutatja majd.

## 4. Kockázatok és nyitott döntések

1. **Magyar overlay-ek konzisztenciája:** ha valaha az upstream platformra töltünk fel skillt, a magyar
   `SKILL.md`-ből hiányozni fog a `subject`/`kind`. Két lehetőség: (a) most, a beolvasztással együtt
   felvesszük a 46 magyar overlay-be is a két sort (egyszeri, gépi munka, a meglévő értékek átemelésével),
   vagy (b) hagyjuk, és csak akkor foglalkozunk vele, ha platformra töltünk.
2. **README-ütközés:** a `README.md`-ben a mi magyar fordításaink és az ő Innoskill-szekciójuk ütközik —
   kézi munka, de kicsi.
3. **Kínai nyelvű új preselek:** a 4 új kártya kínaiul van; ha a magyar tanórán meg akarnak jelenni,
   lokalizálni kell őket (külön feladat, ez nem a beolvasztás része).
4. **Bemutató oldal (Pages):** eldöntendő, hogy a fork publikálja-e (a saját tartalmunkkal) vagy
   kapcsoljuk ki a workflow-t.
5. **A mi 26 presetünk vs az ő 24-ük:** nincs átfedés a kártyákban (az ő 4 új kártyájuk új id), tehát a
   kártyakészlet ütközés nélkül bővül 26 → 30-ra.

## 5. Javasolt sorrend (nem most, külön munka)

1. **Fázis 1 — biztonsági pont:** a mostani állapot megjelölve (`stable` branch + `hu-2026.09.27` tag) —
   kész. Bármikor visszaállítható.
2. **Fázis 2 — beolvasztás külön ágon:** `git checkout -b upstream-merge` a main-ről, majd
   `git merge origin/main`. Várható: 2 README-ütközés, minden más automatikus. Az ágon fut a
   teszt (`npx vitest run`), a hub-katalógus ellenőrzés és egy eldobható példányos E2E.
3. **Fázis 3 — kiadás:** ha zöld, `main` → `stable` léptetés + új tag (pl. `hu-2026.10.01`), és a
   telepítők automatikusan ezt kapják (`INNO_HUB_REF` alapértéke `stable`).

Amit NEM érdemes átvenni/automatikusan elfogadni: a `README.md` és a `workspace-templates/README.md`
szövegének felülírása (a magyar fordításaink és a kártyaindexünk elvesznének).

## 6. Ellenőrzött tények (hogy később is reprodukálható legyen)

- `git rev-list --count HEAD..origin/main` = 35; `origin/main..HEAD` = 85.
- `git diff --name-only 933909d origin/main | wc -l` = 188; közös a saját változásainkkal: 2 fájl.
- `git diff --name-status 933909d origin/main` törölt fájlok: 0.
- 46 megosztott skill diffje: fájlonként csak `SKILL.md`, ≤4 hozzáadott sor (a `subject`/`kind` sorok).
- Az app kódja nem használ `subject`/`kind` mezőt (grep a telepített `apps/inno-agent/src` alatt).
- A nyers adatgyűjtés: `/home/karsa-robert/.hermes/cache/scratch/upstream_data.json`
  (a szkriptek: `collect_upstream.py`, `analyze_upstream.py` ugyanott).
