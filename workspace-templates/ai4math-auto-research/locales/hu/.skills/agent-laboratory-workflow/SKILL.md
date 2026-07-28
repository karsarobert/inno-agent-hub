---
name: agent-laboratory-workflow
description: Akkor használd, amikor a Codexnek interaktívan kell telepítenie, konfigurálnia, ellenőriznie vagy elindítania az AI4Math Auto-Research rendszert az Agent Laboratoryval, beleértve az API-kulcsok kezelését, a felhasználó kutatási témájának begyűjtését, a teljes helyi validációt és az emberi felülvizsgálati kapukat.
---

# Agent Laboratory munkafolyamat

## Mikor használd?

Ezt a készséget az AI4Math Auto-Research fő platformjához használd. Nem állhat meg annál, hogy „az API működik”: fel kell mérnie a felhasználó kutatási szándékát, telepítenie vagy frissítenie kell az Agent Laboratoryt, ellenőriznie kell a környezetet, valódi modell-füsttesztet kell futtatnia, majd korlátozott kutatási munkafolyamatot kell indítania, amikor a felhasználó az Auto-Research indítását kéri.

Általános szakirodalmi kérdezz-felelekhez ne ezt a készséget használd; arra a PaperQA2 vagy a paper-to-skill modul való.

## Bemenetek

- Telepítési célkönyvtár, alapértelmezés szerint `external/agent-laboratory`.
- Conda-környezet neve, alapértelmezés szerint `ai4math-agent-lab`.
- API-kulcsok, például `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` vagy `S2_API_KEY`.
- OpenAI-kompatibilis álnevek, például `LLM_API_KEY`, `LLM_BASE_URL` és `LLM_MODEL_ID`.
- A felhasználó kutatási témája.
- Futtatási mód: `hybrid`, `core`, `research`, `codex-native` vagy `full`.
- Kísérleti YAML útvonala; kutatási módban az alapértelmezett a `templates/interactive-auto-research.yaml`.

## Kimenetek

- Telepítési terv vagy végrehajtott telepítés.
- Helyi validációs jelentés, amely lefedi a repository fájljait, a függőségek állapotát, a fordítási ellenőrzéseket és az esetleges upstream teszteket.
- Valódi modell-füstteszt eredménye, és kérés esetén az Agent Laboratory kutatási futásának eredménye.
- Hiányzó API-kulcsokról szóló jelentés, titkos értékek kiírása nélkül.
- A `external/agent-laboratory/.ai4math_runs/` alatt előállított futásidejű YAML útvonala, kitakart API-kulcsokkal.
- Futtatási diagnózis vagy helyreállítási jelentés, ha az upstream munkafolyamat korán leáll.
- `codex_research/` alatti Codex-natív kutatási munkaterület, ha az Agent Laboratory nem tud befejeződni vagy a felhasználó nem kíván további LLM API-t használni.

## Munkafolyamat

### Alapértelmezett Agent belépési pont

Ha a felhasználó azt mondja, hogy „Indítsd az Auto Research-et”, „Telepítsd és használd nekem”, „Interaktív bevitel után indíts kutatást”, vagy ennek megfelelő kérést ad, futtasd a varázslót:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --wizard \
  --env-manager conda \
  --conda-mirror tuna \
  --installer uv \
  --lightweight-imports
```

A varázsló a következőket kéri be a felhasználótól:

- Kutatási téma.
- OpenAI-kompatibilis alap-URL, alapértelmezés: `https://chat.ecnu.edu.cn/open/api/v1`.
- Modellazonosító, alapértelmezés: `ecnu-plus`.
- API-kulcs, rejtett bevitelként, ha még nincs megadva `LLM_API_KEY` vagy `OPENAI_API_KEY` változóban.
- Futtatási mód:
  - `hybrid`: ajánlott; először korlátozott Agent Laboratory futás, majd a befejezetlen szakaszok átadása Codexnek.
  - `core`: csak az Agent Laboratory hívási láncának telepítése, ellenőrzése és tesztelése.
  - `research`: korlátozott Agent Laboratory munkafolyamat szakirodalmi áttekintéstől a jelentésig.
  - `codex-native`: nincs további modell-API; hozz létre Codex-kutatási munkaterületet, és a kódoló ügynök közvetlenül végezze el a kutatási szakaszokat.
  - `full`: a kiválasztott upstream/teljes kísérleti YAML használata nagyobb költségkerettel.
- Telepítse/frissítse-e a függőségeket.
- Fusson-e alapszintű füstteszt a kutatás indítása előtt.

### Nem interaktív Agent belépési pont

Ha a felhasználó már megadta a konfigurációt, a kódoló ügynök további kérdések nélkül indíthatja a futást:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --wizard \
  --wizard-mode hybrid \
  --research-topic "Investigate a lightweight numerical optimization idea for least squares preconditioning" \
  --env-manager conda \
  --conda-mirror tuna \
  --installer uv \
  --llm-model-id ecnu-plus \
  --openai-base-url https://chat.ecnu.edu.cn/open/api/v1 \
  --lightweight-imports \
  --yes \
  --interactive-api
```

Ha a felhasználó kifejezetten el kívánja kerülni az instabil modellátjárókat, vagy nincs további API-kulcsa, ezt használd:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --wizard \
  --wizard-mode codex-native \
  --research-topic "USER_RESEARCH_TOPIC" \
  --codex-workspace-dir codex_research \
  --yes
```

### Kézi lépések

Ezeket az egyes szakaszok hibakeresésénél használd.

1. Készíts száraz futású tervet:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py --dry-run
```

2. Telepítsd a függőségeket:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --deploy \
  --env-manager conda \
  --conda-mirror tuna \
  --installer uv
```

Az alapértelmezett irányelv a conda-környezet plusz uv telepítő tartalékmegoldás: a futtatókörnyezet maradjon condában, de használd a `uv pip --python /opt/anaconda3/envs/<env>/bin/python` parancsot, ha a normál pip megakad vagy a hálózati olvasás hibázik.

3. Futtasd a helyi validációt:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py --verify
```

4. Ellenőrizd az API-kulcsok elérhetőségét értékeik kiírása nélkül:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py --check-api
```

ChatECNU vagy más OpenAI-kompatibilis átjáró esetén titkos adatot csak folyamatszintű környezeti változóként adj meg:

```bash
export LLM_API_KEY="<hidden>"
export LLM_BASE_URL="https://chat.ecnu.edu.cn/open/api/v1"
export LLM_MODEL_ID="ecnu-plus"
```

A szkript ezeket futásidőben `OPENAI_API_KEY` és `OPENAI_BASE_URL` változókra képezi le anélkül, hogy a titkot YAML-be írná.

5. Futtasd az alapszintű füsttesztet. Ez valós hívásokat végez az Agent Laboratory `query_model`, `PhDStudentAgent` és generált kódot kezelő segédútvonalán keresztül:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --core-smoke \
  --env-manager conda \
  --llm-backend ecnu-plus \
  --lightweight-imports
```

6. Futtass kutatási munkafolyamatot az interaktív sablonnal. A kutatási mód nem ál-futtatás: szakirodalmi áttekintéssel indul, két cikket ad hozzá, majd tervalkotáson, adatelőkészítésen, kísérleten és az eredmények értelmezésén át a jelentésírásig halad:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --run-experiment \
  --experiment-yaml "$(pwd)/skills/agent-laboratory-workflow/templates/interactive-auto-research.yaml" \
  --research-topic "USER_RESEARCH_TOPIC" \
  --env-manager conda \
  --llm-backend ecnu-plus \
  --compile-latex false \
  --lightweight-imports \
  --experiment-timeout-seconds 600
```

A futtató ideiglenes futásidejű YAML-t ír a `external/agent-laboratory/.ai4math_runs/` könyvtárba, és távol tartja az API-kulcsokat ettől a fájltól.

7. Nagyobb kísérletet csak `core` vagy `research` siker után futtass:

```bash
python skills/agent-laboratory-workflow/scripts/bootstrap_agent_laboratory.py \
  --run-experiment \
  --experiment-yaml experiment_configs/MATH_agentlab.yaml \
  --llm-backend gpt-4o-mini \
  --compile-latex false
```

8. Jegyezd fel a létrehozott naplókat, állapotmentéseket, jelentéseket és hibamódokat a feladatjegyzetekben.

9. Ha a kísérlet hibázik, időtúllép, vagy elégtelen részleges eredményt ad, válaszadás előtt vizsgáld meg a futást:

```bash
python skills/agent-laboratory-workflow/scripts/inspect_agent_laboratory_run.py \
  --target-dir external/agent-laboratory \
  --format markdown \
  --output auto_research_recovery_report.md
```

A diagnózis alapján jelentsd a leállt szakaszt, a befejezett szakaszokat, a visszanyert szakirodalmi áttekintés / terv / kód / jelentés töredékeit, valamint azt, hogy az eredmény kész kutatási lelet vagy csak helyreállítható részleges állapot.

10. Készíts Codex-natív átadási munkaterületet, ha az Agent Laboratory nem tud befejeződni, vagy a felhasználó a `codex-native` módot választja:

```bash
python skills/agent-laboratory-workflow/scripts/prepare_codex_research_workspace.py \
  --target-dir external/agent-laboratory \
  --research-topic "USER_RESEARCH_TOPIC" \
  --output-dir codex_research \
  --json
```

Ezután a Codexnek ebben a munkaterületben kell befejeznie a hátralévő szakaszokat: töltse ki a `plan.md` fájlt, írja meg és futtassa a `src/experiment.py` fájlt, mentse a kimeneteket az `outputs/` alá, majd írja meg a `report.md` fájlt.

## Validáció

- A `--dry-run --json` klónozási, conda-, telepítési, ellenőrzési és kísérleti parancsokat ad vissza a célkönyvtár létrehozása nélkül.
- A `--verify --json` ellenőrzi a telepített repositoryt, és strukturált JSON-ként jelenti a hibákat.
- Minden valódi kísérlet előtt teljes helyi validáció fut.
- A kísérletek nem írhatnak ki API-kulcsokat.
- Az OpenAI-kompatibilis útválasztást az Agent Laboratory `query_model` importálásával és a konfigurált `LLM_MODEL_ID` meghívásával kell validálni.
- A `--wizard` az előnyben részesített felhasználói belépési pont. Egyesíti a telepítést, a validációt, a füsttesztet és az indítást.
- A `--yes` lehetővé teszi, hogy a kódoló ügynök a megadott értékeket és alapértelmezett megerősítéseket további igen/nem kérdések nélkül használja.
- A `--research-topic` felülírja a sablon témáját a létrehozott futásidejű YAML-ben.
- A kutatási módnak meg kell őriznie a teljes kutatási ívet: szakirodalmi áttekintés -> terv -> adatok -> kísérlet -> értelmezés -> jelentés. Ezt a cikkek számával, lépésszámmal és időkorláttal korlátozd, ne kutatási szakaszok kihagyásával.
- A hibrid mód nem állhat meg Agent Laboratory hiba esetén. Ha az upstream korán leáll, hozz létre Codex-munkaterületet, és közvetlenül fejezd be a hátralévő kutatási szakaszokat.

## Hibamódok

- Ha a célkönyvtár hiányzik, futtasd a `--deploy` parancsot.
- Ha a conda metaadatai vagy csomagletöltései hibáznak, próbáld újra `--conda-mirror tuna` kapcsolóval; ha a pip megakad vagy `IncompleteRead` hibát ad, futtasd újra a telepítést `--installer uv` kapcsolóval.
- Ha a conda nem érhető el, tartalékmegoldásként használd a `--env-manager uv` opciót, és jegyezd fel az okot.
- Ha API-kulcsok hiányoznak, állj meg és kérdezd meg a felhasználót; ne találj ki és ne kódolj be titkokat.
- Ha egy egyéni modellnév nem ismert, futtasd újra a `--deploy` műveletet; a telepítés alkalmazza az `AI4MATH_OPENAI_COMPATIBLE_PATCH` javítást az Agent Laboratory modellútválasztójára.
- Ha a LaTeX nem érhető el vagy hibázik, használd a `--compile-latex false` opciót.
- Ha az indítás nehézsúlyú opcionális importoknál megakad, futtasd újra a füsttesztet `--lightweight-imports` opcióval; a teljes kísérletek továbbra is használhatják az eredeti upstream importkészletet.
- Ha a teljes munkafolyamat időtúllép, jelentsd az időtúllépést és a létrehozott futásidejű YAML útvonalát; majd növeld a `--experiment-timeout-seconds` értékét, vagy futtasd újra `research` módban kisebb témával.
- Ha backend 500, időtúllépés vagy kapcsolati hiba szakítja meg a munkafolyamatot, futtasd az `inspect_agent_laboratory_run.py` programot a telepítési könyvtárral. Ne állíts befejezett Auto-Research eredményt csak szakirodalmi állapot alapján.
- Ha a diagnózis szerint a szakirodalmi áttekintés elkészült, de a későbbi szakaszok üresek, használd a visszanyert áttekintést kiinduló anyagként, majd vagy futtasd újra stabilabb backenddel / nagyobb időkorláttal, vagy a kódoló ügynökkel állíts elő tervet, futtatható kísérletet és jelentést a visszanyert állapotból.
- Ha a felhasználó `codex-native` módot választ, ne kérj LLM API-kulcsot és ne futtasd az Agent Laboratoryt. Hozd létre a Codex-munkaterületet, és a jelenlegi kódoló ügynökként végezd el a kutatást.
- Ha a kísérlet generált kódot hív, azt tartsd a külső telepítési könyvtáron belül, és újrafelhasználás előtt ellenőrizd a kimeneteit.

## Emberi interakciós szerződés

A kódoló ügynök csak olyan értékeket kérjen a felhasználótól, amelyeket nem lehet biztonságosan kikövetkeztetni:

- Kutatási téma vagy kutatási irány.
- API-kulcs, kizárólag rejtett bevitelként.
- `core`, `research` vagy `full` futtatása.
- Folytasson-e, ha az ellenőrzés sikeres, de a teljes munkafolyamat várhatóan lassú vagy költséges.

E válaszok után az ügynök hajtsa végre a munkafolyamatot, javítsa a helyreállítható környezeti hibákat, és konkrét leleteket vagy strukturált hibajelentést adjon vissza.

## Hivatkozások

- `references/agent-laboratory-deployment.md`: telepítési megjegyzések és forráslinkek.
- `scripts/bootstrap_agent_laboratory.py`: telepítő, validáló és kísérletfuttató.
