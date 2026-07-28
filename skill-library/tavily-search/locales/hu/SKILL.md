---
name: tavily-search
category: Kutatás és keresés
description: >-
  Valós idejű internetes keresés a Tavily API segítségével, a modell tanítási határidő utáni legfrissebb információk beszerzése.
  Akkor használd, ha a felhasználó közelmúltbeli eseményekről, valós idejű adatokról, aktuális állapotról, árakról, verziószámokról és más könnyen elavuló tényekről kérdez,
  vagy egyértelműen „keress rá / nézz utána / segíts keresni” kérést fogalmaz meg; tiszta fogalmi magyarázatok, csevegés,
  illetve a meglévő kontextusból elvégezhető következtetés esetén ne hívd meg.
---

## Végrehajtási lépések

### 1. Keresés indítása

Cseréld le a `<QUERY>` értéket a keresőkifejezésre (őrizd meg a felhasználó eredeti nyelvét, magyar és angol egyaránt lehet), majd hajtsd végre:

```bash
curl -s -X POST "https://api.tavily.com/search" \
  -H "Content-Type: application/json" \
  -d '{"api_key":"YOUR_TAVILY_API_KEY","query":"<QUERY>","max_results":5,"include_answer":true,"search_depth":"basic"}'
```

Állítható paraméterek:
- `max_results`: a visszaadott találatok száma, alapértelmezett 5; tágabb kérdés vagy több forrásból történő megerősítés esetén növeld 8–10-re.
- `search_depth`: `basic` (gyors, alapértelmezett) vagy `advanced` (mélyebb, tovább tart, fontos lekérdezéseknél használandó).
- `topic`: alapértelmezett `general`; hírek keresésekor adható hozzá `"topic":"news"`.

### 2. Válasz feldolgozása

A válasz JSON formátumú, ezeket a mezőket használd:

| Mező | Használat |
|---|---|
| `answer` | A Tavily által szintetizált közvetlen válasz, a válasz fő részeként |
| `results[].title` | Forrás címe |
| `results[].url` | Forrás hivatkozása |
| `results[].content` | Forrás összegzése, idézetnél az első ~300 karaktert vedd |
| `results[].score` | Relevancia 0–1, 0,5 alatti forrásokat hagyd figyelmen kívül |

### 3. Válasz összeállítása

1. A `answer` segítségével add meg a következtetést; ha az `answer` üres, akkor a magas pontszámú `results` alapján magad állítsd össze.
2. A következtetés alatt 2–3 magas pontszámú forrást sorolj fel, `[Cím](url)` formátumban.
3. A végén jelöld meg „Forrás: Tavily valós idejű keresés”, hogy a felhasználó tudja: ez internetes találat, nem a modell memóriája.

### Hibakezelés

- HTTP 401 / `Unauthorized`: az API-kulcs érvénytelen vagy nem lett lecserélve, kérd meg a felhasználót, hogy ellenőrizze a `YOUR_TAVILY_API_KEY` értéket.
- HTTP 432 / kvóta elfogyott: tájékoztasd a felhasználót, hogy a havi ingyenes keret (1000 keresés) elfogyott.
- Hálózati időtúllépés vagy üres találat: tősd hozzá, hogy a keresés sikertelen volt, ne találj ki tartalmat.
