#!/usr/bin/env bash
set -euo pipefail
# Kézi tartalék. Csak ennek a gyermekfolyamatnak a munkamappáját állítja.
if [[ $# -ne 1 ]]; then
    echo "Használat: bash futtatas.sh fajl.py" >&2
    exit 2
fi
case "$1" in
    indulas.py|sorszam.py|bekeres.py|tartomany.py|napi_osszesito.py|kosar.py|blokk.py|bufe_03.py|onallo.py|rajz.py) ;;
    *) echo "Ismeretlen gyakorlófájl." >&2; exit 2 ;;
esac
script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$script_dir"
if [[ ! -f "$1" ]]; then
    echo "A kért gyakorlófájl még nem létezik: $1" >&2
    exit 2
fi
exec python3 "$1"
