#!/bin/sh
# inno-preset-torles.sh — az Inno Agent hub-ról letöltött presetjeinek és a
# belőlük készült munkaterületeknek a nullázása EGY GÉPEN, hogy a következő
# megnyitás a hub AKTUÁLIS (javított) változatát töltse le.
#
# Használat (felhasználói joggal; a szerver fusson — a képen belépéskor indul):
#   sh inno-preset-torles.sh                 # MINDEN preset: cache + munkaterület
#   sh inno-preset-torles.sh --preset <id>    # csak egy kártya (pl. diszkret-matematika-1)
#   sh inno-preset-torles.sh --lista          # csak kilistáz, nem módosít
#   sh inno-preset-torles.sh --csak-cache     # csak a letöltött cache (munkaterület marad)
#   sh inno-preset-torles.sh --vegleges       # a félretétel helyett TÖRLÉS (mentés nélkül)
#   INNO_HOME=/másik/telepítés sh inno-preset-torles.sh
#   INNO_PORT=3001 sh inno-preset-torles.sh
#
# MIÉRT KELL KÉT HELYEN IS NULLÁZNI (a "csak rm -rf preset-cache" nem elég)
#   1. <INNO_HOME>/runtime/data/preset-cache/<id>/  — a letöltött sablon másolata.
#      Ha megvan a preset.json, az app NEM tölt újra (ensurePresetCached), ezért
#      a régi anyagot másolja tovább.
#   2. <INNO_HOME>/workspace/.presets/<id>-<nyelv>/  — a belőle készült, nyelv-
#      enként külön munkaterület. A sablon tartalma CSAK az első megnyitáskor
#      másolódik bele, később soha nem íródik felül: a régi fájlok (és a régi
#      sablon maradványai) benne maradnak. Ezt a mappát kell félretenni/törölni,
#      és a registry-bejegyzést az app API-jával (DELETE /api/workspaces/<id>)
#      törölni, hogy a bal oldali sáv és a session-kötések konzisztensek legyenek.
#   3. A hub-kártyák NEM tűnnek el (a lista a hubról jön) — az újramegnyitás
#      hozza létre újra a munkaterületet, immár a friss tartalommal.
#
# Alapértelmezésben MINDENT FÉLRETESZ (nem töröl): a mentés a
# <INNO_HOME>/runtime/data/preset-torles-mentes-<időpont>/ mappába kerül, így a
# művelet visszavonható. --vegleges esetén nincs mentés.
#
# NEM érinti: a diák többi munkaterületét, a beállításokat/API-kulcsot, a
# beszélgetéseket, a jegyzetfüzetet, a tantárgyi skilleket.
#
# FIGYELEM: a törölt cache a hubról töltődik vissza — INTERNET kell hozzá. Offline
# teremben ne futtasd, vagy gondoskodj a friss cache behordásáról.
#
# A művelet után a böngészőben F5 (a kártya- és munkaterület-lista betöltéskor
# frissül).
set -e

usage() {
    # A fejlécet a saját fájlból olvassuk; ha pipából fut (ilyenkor $0 = "sh"),
    # beépített rövid súgó jön (a here-document pipában nem megbízható).
    if [ -r "$0" ] && [ "$(basename "$0")" != "sh" ]; then
        sed -n '2,38p' "$0" | sed 's/^# \{0,1\}//'
    else
        echo "inno-preset-torles.sh — az Inno Agent hub-ról letöltött presetek nullázása"
        echo
        echo "  sh inno-preset-torles.sh                # minden preset (cache + munkaterület)"
        echo "  sh inno-preset-torles.sh --preset <id>   # csak egy kártya"
        echo "  sh inno-preset-torles.sh --lista         # csak kilistáz"
        echo "  sh inno-preset-torles.sh --csak-cache    # csak a letöltött cache"
        echo "  sh inno-preset-torles.sh --vegleges      # félretétel helyett törlés"
        echo "  INNO_HOME=<telepítés> INNO_PORT=<port> sh inno-preset-torles.sh"
    fi
    exit 0
}

MODE="reset"        # reset | lista | csak-cache
VEGLEGES=0
PRESET=""
while [ $# -gt 0 ]; do
    case "$1" in
        --lista|-l) MODE="lista" ;;
        --csak-cache) MODE="csak-cache" ;;
        --vegleges) VEGLEGES=1 ;;
        --preset)
            shift
            PRESET="${1:-}"
            if [ -z "$PRESET" ]; then echo "Hiányzó érték: --preset <preset-id>" >&2; exit 2; fi
            ;;
        --help|-h) usage ;;
        *) echo "Ismeretlen kapcsoló: $1 (--help a súgóhoz)" >&2; exit 2 ;;
    esac
    shift
done

# --- telepítés, adatok, port megkeresése ------------------------------------
APP="${INNO_HOME:-$HOME/.local/opt/inno-agent}"
DATA=""
for cand in "$APP/runtime/data" "$APP/data"; do
    if [ -d "$cand" ]; then DATA="$cand"; break; fi
done
if [ -z "$DATA" ]; then
    echo "Nem találom az Inno Agent adatkönyvtárát." >&2
    echo "  keresve: $APP/runtime/data, $APP/data" >&2
    echo "  Ha más helyre települt: INNO_HOME=<telepítési mappa> sh $0" >&2
    exit 1
fi
CACHE="$DATA/preset-cache"
WS="${INNO_WORKSPACE_DIR:-$APP/workspace}"
PRESETS_WS="$WS/.presets"
BACKUP="$DATA/preset-torles-mentes-$(date +%Y%m%d-%H%M%S)"

case "$CACHE" in
    ""|/|*..*) echo "Megtagadva: gyanús útvonal ($CACHE)" >&2; exit 1 ;;
esac
if [ "$(basename "$CACHE")" != "preset-cache" ]; then
    echo "Megtagadva: a cél nem preset-cache könyvtár ($CACHE)" >&2; exit 1
fi

PORT="${INNO_PORT:-3000}"
API="http://127.0.0.1:$PORT"
if ! curl -s -m 8 "$API/health" 2>/dev/null | grep -q '"ok"'; then
    # A config.json-ból csak akkor keresünk portot, ha azt nem kérték kézzel.
    if [ -z "${INNO_PORT:-}" ]; then
        CFG="$DATA/../config/config.json"
        if [ -f "$CFG" ]; then
            P=$(sed -n 's/.*"port"[[:space:]]*:[[:space:]]*\([0-9][0-9]*\).*/\1/p' "$CFG" | head -1)
            if [ -n "$P" ] && curl -s -m 8 "http://127.0.0.1:$P/health" 2>/dev/null | grep -q '"ok"'; then
                PORT="$P"; API="http://127.0.0.1:$PORT"
            fi
        fi
    fi
fi
if ! curl -s -m 8 "$API/health" 2>/dev/null | grep -q '"ok"'; then
    echo "HIBA: az Inno Agent nem válaszol a http://127.0.0.1:$PORT címen." >&2
    echo "  Indítsd el az alkalmazást (vagy add meg a portot: INNO_PORT=<port> sh $0)." >&2
    exit 1
fi

# --- mit találtunk ----------------------------------------------------------
match_preset() {  # $1 = preset-id, $2 = szűrő (üres = minden)
    [ -z "$2" ] || [ "$1" = "$2" ]
}

CACHE_LIST=""
if [ -d "$CACHE" ]; then
    for d in "$CACHE"/*/; do
        [ -d "$d" ] || continue
        id=$(basename "$d")
        match_preset "$id" "$PRESET" || continue
        CACHE_LIST="$CACHE_LIST$id
"
    done
fi

WS_LIST=""
if [ -d "$PRESETS_WS" ]; then
    for d in "$PRESETS_WS"/*/; do
        [ -d "$d" ] || continue
        name=$(basename "$d")
        if [ -n "$PRESET" ]; then
            case "$name" in "$PRESET"-*) ;; *) continue ;; esac
        fi
        WS_LIST="$WS_LIST$name
"
    done
fi

REG_LIST=""   # registry-bejegyzés, amihez nincs mappa (kilógó bejegyzés)
for id in $(curl -s -m 15 "$API/api/workspaces" | grep -o '"id":"preset-[^"]*"' | sed 's/^"id":"//; s/"$//'); do
    if [ -n "$PRESET" ]; then
        case "$id" in "preset-$PRESET-"*) ;; *) continue ;; esac
    fi
    d="${id#preset-}"
    [ -d "$PRESETS_WS/$d" ] || REG_LIST="$REG_LIST$id
"
done

echo "Inno Agent — letöltött presetek nullázása"
echo "  Telepítés:    $APP"
echo "  Cache:        $CACHE"
echo "  Munkaterületek: $PRESETS_WS"
echo "  Szerver:      $API   (port $PORT)"
[ -n "$PRESET" ] && echo "  Szűrő:        csak a(z) \"$PRESET\" kártya"
echo
if [ -z "$CACHE_LIST" ] && [ -z "$WS_LIST" ] && [ -z "$REG_LIST" ]; then
    echo "Nincs mit tenni: ezen a gépen nincs letöltött preset."
    exit 0
fi
[ -n "$CACHE_LIST" ] && { echo "  Letöltött cache ($(printf '%s' "$CACHE_LIST" | grep -c .) db):"; printf '%s' "$CACHE_LIST" | sed 's/^/    - /'; }
[ -n "$WS_LIST" ] && { echo "  Megnyitott preset-munkaterület ($(printf '%s' "$WS_LIST" | grep -c .) db):"; printf '%s' "$WS_LIST" | sed 's/^/    - .presets\//'; }
[ -n "$REG_LIST" ] && { echo "  Kilógó registry-bejegyzés (mappa nélkül):"; printf '%s' "$REG_LIST" | sed 's/^/    - /'; }
echo

if [ "$MODE" = "lista" ]; then
    echo "Csak lista (--lista): nem módosítottam semmit."
    exit 0
fi

if [ "$VEGLEGES" -eq 0 ]; then
    mkdir -p "$BACKUP"
    echo "  Mentés helye: $BACKUP"
fi
echo

# --- 1) munkaterületek + registry ------------------------------------------
if [ "$MODE" != "csak-cache" ]; then
    for name in $WS_LIST; do
        dir="$PRESETS_WS/$name"
        id="preset-$name"
        if [ "$VEGLEGES" -eq 0 ]; then
            mv "$dir" "$BACKUP/"
            echo "[félretéve]  munkaterület: .presets/$name"
        fi
        res=$(curl -s -m 20 -X DELETE "$API/api/workspaces/$id?removeFiles=1" || true)
        case "$res" in
            *'"deleted":true'*) echo "[registry]   $id → törölve (API)" ;;
            *) echo "[registry]   $id → az app nem ismerte (mappa: $([ "$VEGLEGES" -eq 1 ] && echo törlés || echo félretéve))" ;;
        esac
        if [ "$VEGLEGES" -eq 1 ] && [ -d "$dir" ]; then
            rm -rf "$dir"
            echo "[törölve]    munkaterület: .presets/$name"
        fi
    done
    for id in $REG_LIST; do
        res=$(curl -s -m 20 -X DELETE "$API/api/workspaces/$id?removeFiles=1" || true)
        case "$res" in
            *'"deleted":true'*) echo "[registry]   $id → törölve (kilógó bejegyzés)" ;;
            *) echo "[registry]   $id → nem sikerült törölni" ;;
        esac
    done
fi

# --- 2) letöltött cache ----------------------------------------------------
if [ -n "$CACHE_LIST" ]; then
    for id in $CACHE_LIST; do
        dir="$CACHE/$id"
        [ -d "$dir" ] || continue
        if [ "$VEGLEGES" -eq 0 ]; then
            mv "$dir" "$BACKUP/"
            echo "[félretéve]  cache: $id"
        else
            rm -rf "$dir"
            echo "[törölve]    cache: $id"
        fi
    done
    if [ -d "$CACHE" ] && [ -z "$(ls -A "$CACHE" 2>/dev/null)" ]; then
        rmdir "$CACHE" 2>/dev/null || true
    fi
fi

# --- 3) kártyalista frissítése (metaadatok) --------------------------------
for loc in hu en; do
    curl -s -m 30 "$API/api/preset-library?contentLocale=$loc&refresh=1" >/dev/null 2>&1 || true
done

# --- 4) ellenőrzés: mi maradt? --------------------------------------------
LEFT_WS=$(ls -1 "$PRESETS_WS" 2>/dev/null | grep -c . || true)
LEFT_CACHE=$(ls -1 "$CACHE" 2>/dev/null | grep -c . || true)
LEFT_REG=$(curl -s -m 15 "$API/api/workspaces" | grep -o '"id":"preset-[^"]*"' | grep -c . || true)
echo
echo "Ellenőrzés: preset-munkaterület a gépen: ${LEFT_WS:-0}, letöltött cache-bejegyzés: ${LEFT_CACHE:-0}, registry-bejegyzés: ${LEFT_REG:-0}"
if [ "$VEGLEGES" -eq 0 ]; then
    echo "Mentés (visszavonáshoz): $BACKUP"
    echo "  visszaállítás: a mentett mappákat vissza kell másolni a fenti helyekre,"
    echo "                 és a kártyát újra megnyitni (a registry-bejegyzést az app újra létrehozza)."
fi
echo "KÉSZ. A böngészőben nyomj F5-öt; a kártya újramegnyitásakor az app a hub friss"
echo "tartalmát tölti le. A diák többi munkaterülete és a beállítások érintetlenek."
