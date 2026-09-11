#!/bin/sh
# reset.sh — Inno Agent: a hub-ról letöltött presetek nullázó parancsának telepítése.
#
# Használat (egy sor, bármelyik diák-gépen):
#   wget -qO- https://cdn.jsdelivr.net/gh/karsarobert/inno-agent-hub/reset.sh | sh
#   wget -qO- .../reset.sh | sh -s -- --lista        (a kapcsolók továbbadhatók)
#
# Amit csinál:
#   1. letölti az inno-preset-torles.sh-t a hub repóból,
#   2. telepíti /usr/local/bin/inno-preset-torles néven (sudo nélkül ~/.local/bin-be),
#   3. argumentum NÉLKÜL csak a --lista (kiolvasó) módot futtatja — SOHA nem töröl magától.
#
# Kapcsolók átadása: wget -qO- <URL> | sh -s -- --preset diszkret-matematika-1
set -e

BASE="${INNO_HUB_BASE:-https://raw.githubusercontent.com/karsarobert/inno-agent-hub/main}"
TMP="${TMPDIR:-/tmp}/inno-preset-torles.$$"
DEST=""

echo "Inno Agent — preset-nullázó parancs telepítése"
if ! command -v curl >/dev/null 2>&1; then
    echo "HIBA: ehhez a curl program kell (Ubuntu: sudo apt-get install curl)." >&2
    exit 1
fi

if ! curl -fsSL "$BASE/inno-preset-torles.sh" -o "$TMP"; then
    echo "HIBA: a letöltés nem sikerült. Ellenőrizd az internetet ($BASE)." >&2
    exit 1
fi
chmod +x "$TMP" 2>/dev/null || true

if [ -w /usr/local/bin ]; then
    install -m 755 "$TMP" /usr/local/bin/inno-preset-torles && DEST=/usr/local/bin/inno-preset-torles
elif sudo -n true 2>/dev/null; then
    sudo -n install -m 755 "$TMP" /usr/local/bin/inno-preset-torles && DEST=/usr/local/bin/inno-preset-torles
else
    mkdir -p "$HOME/.local/bin"
    install -m 755 "$TMP" "$HOME/.local/bin/inno-preset-torles" && DEST="$HOME/.local/bin/inno-preset-torles"
fi

echo
if [ -z "$DEST" ]; then
    echo "A telepítés nem sikerült, a letöltött példányt futtatom közvetlenül: $TMP"
    exec sh "$TMP" "$@"
fi

if [ "$#" -gt 0 ]; then
    exec "$DEST" "$@"
fi

echo "Telepítve: $DEST"
echo "Használat: inno-preset-torles [--lista | --preset <id> | --csak-cache | --vegleges]"
echo
"$DEST" --lista
