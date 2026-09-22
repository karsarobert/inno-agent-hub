# EP_03 – haladás az alkalmazás tanulói memóriájában

Belső tutorútmutató. A tanulói beszélgetésben ne ismertesd az adminisztrációt minden lépésnél. A cél a valós folytatási pont megőrzése úgy, hogy a kódszerkesztőt ne váltsa fel egy automatikusan megnyíló Markdown-fájl.

## Melyik réteg?

- L1: tanulói cél, tudásállapot és tanulási esemény. Az EP_03 haladását ide rögzítsd az elérhető eszközökkel.
- L2: tartalmi tudástár. Ne használd tanulói haladási napló pótlására.
- L3: korábbi beszélgetések visszakeresése. Segíthet folytatáskor, de nem külön haladási munkalap és nem megkerülése a letiltott L1-nek.

A vizsgált Inno Agent-verzióban a Simple Mode kikapcsolja a memóriarétegeket. Az L1 írás feltétele: Simple Mode kikapcsolva, L1 engedélyezve. Ez oktatói beállítás, nem tanulói feladat; a csomag nem változtatja meg automatikusan. A sémát és a sikert mindig a ténylegesen elérhető eszköz alapján ellenőrizd.

## Rögzítés

A `record_learning_event` eseményt ment és a profilhoz is szinkronizál. Ne küldj ugyanarra a változásra automatikusan még egy `patch_learner_profile` hívást. Részleges profiljavítás csak tényleges új diagnózis vagy tartós, bizonyított tanulói preferencia esetén indokolt.

Érdemi próbálkozás: `exercise_attempt`. Valós szakaszzárás: `milestone_reached`. Technikai visszajelzés: `feedback_received`. Ne rögzíts minden „kész” szóra eseményt a kód elolvasása előtt. Egy összetartozó részfeladat eredménye lehet egy esemény.

A feladattérkép `ep03.*` fogalomazonosítóit használd. `context.goal_id` és `context.session_id` csak ténylegesen ismert értékkel küldhető. Workspace-azonosító csak ismerten kerüljön a payloadba. Ne találj ki valós azonosítónak látszó értéket.

A `payload` szabad kulcsú objektum; a következő mezőket ez a csomag konvencióként használja, nem új alkalmazássémaként:

| Mező | Tartalom |
|---|---|
| `course` | EP_03 |
| `task_id`, `subtask` | Például B3, azon belül tényleges a/b/c rész. |
| `topic` | Rövid mondat: EP_03, aktuális lépés, valós státusz és következő teendő. |
| `file` | Valós relatív fájlnév, pl. bufe_03.py. |
| `status` | A csomagban használt állapotnév. |
| `code_change` | Mit írt vagy módosított a tanuló? |
| `tests` | Melyik eset, milyen bemenet, milyen tényleges eredmény, milyen forrásból? |
| `assistance` | Általános magyarázat / irányító támpont / analóg minta / konkrét célkód. |
| `next_action` | Egyértelmű következő kis teendő. |
| `remaining` | A még hiányzó feladat vagy próba. |

A `topic` azért tartalmazzon rövid folytatási pontot, mert a kontextuscsomag az események rövid témáját emelheti be, nem feltétlenül minden részletes payloadmezőt. S1/S2-nél a ténylegesen kész, támogatással kész és későbbre tett részekről rövid összesítés is szerepeljen. Ne legyen személyes adat a feladatleírásba írva szükségtelenül.

A `derived_signals.mastery_delta` ezeknél a csomagbeli adminisztratív státusznaplóknál legyen **0**. Ezzel nem lesz automatikus elsajátítási növekmény pusztán a naplózástól. Ne gyárts százalékot a feladatszámból. Fogalmi értékeléshez a konkrét diagnózis és bizonyíték többet mond, mint egy megalapozatlan szám.

Szemléltető séma, **nem elküldendő kész esemény**:

```json
{
  "event_type": "exercise_attempt",
  "context": {"concept_ids": ["ep03.accumulator"]},
  "payload": {
    "course": "EP_03",
    "task_id": "B2",
    "topic": "A tényleges állapot és a következő teendő röviden.",
    "file": "kosar.py",
    "status": "folyamatban",
    "code_change": "A valóban látott módosítás.",
    "tests": [],
    "assistance": "A ténylegesen adott segítség.",
    "next_action": "A még szükséges lépés."
  },
  "derived_signals": {"mastery_delta": 0}
}
```

## Bizonyíték és sikertelen mentés

A források különböznek: olvasott aktuális fájl; megtekintett, azonosítható futási rekord; tanulói beszámoló. Ne cseréld fel őket. A várt eredmények táblázata nem bizonyítja, hogy a tanuló futtatott. Csak a ténylegesen ismert tesztet rögzítsd elvégzettnek, a többit függőben.

Sikernek az eszköz tényleges visszajelzése számít. `disabled: true`, letiltást közlő szöveg vagy hiba esetén nincs sikeres mentés. Ilyenkor ne ismételd minden üzenetben a sikertelen hívást. Egyszer röviden jelezd, hogy ebben a módban a folytatási pontot a beszélgetésben őrizzük; S1/S2-nél adj tömör összefoglalót.

Ne hozz létre helyette `haladas.md`, rejtett JSON vagy más munkatéri adminisztrációs fájlt. Ne módosíts alkalmazásbeállítást és ne kerüld meg a letiltást másik memóriával.

Folytatáskor a `get_learner_context` nem garantáltan teljes feladattörténet. Használd a beszélgetés tényleges folytatási pontját, az elérhető L1-kontextust, szükség esetén az engedélyezett L3-visszakeresést és mindig a valós kódot. Ha így is bizonytalan, egy célzott kérdés segít: „Legutóbb a pénzpótlást is lefuttattad, vagy még az összeépítésnél tartottál?” Ne állítsd vissza a fájlokat.
