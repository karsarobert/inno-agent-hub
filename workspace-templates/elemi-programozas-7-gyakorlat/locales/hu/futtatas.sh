#!/usr/bin/env bash
set -euo pipefail
# Opcionális kézi tartalék; a felület termináljának könyvtárát nem állítja át.
if [[ $# -ne 1 ]]; then
    echo "Használat: bash futtatas.sh fajl.py" >&2
    exit 2
fi
case "$1" in
    tetelek.py|kosar_adatok.py|kosarak.py|modositas.py|onallo.py|riport.py) ;;
    *) echo "Ismeretlen gyakorlófájl." >&2; exit 2 ;;
esac
script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$script_dir"
exec python3 "$1"
