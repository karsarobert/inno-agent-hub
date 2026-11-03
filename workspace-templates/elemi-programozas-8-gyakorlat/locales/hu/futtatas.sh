#!/usr/bin/env bash
set -euo pipefail
# Kézi tartalék; a felületi terminál munkamappáját nem állítja át.
if [[ $# -ne 1 ]]; then
    echo "Használat: bash futtatas.sh fajl.py" >&2
    exit 2
fi
case "$1" in
    rendeles.py|velemeny.py|blokk.py|naplo.py|onallo.py|napi_riport.py) ;;
    *) echo "Ismeretlen gyakorlófájl." >&2; exit 2 ;;
esac
script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$script_dir"
exec python3 "$1"
