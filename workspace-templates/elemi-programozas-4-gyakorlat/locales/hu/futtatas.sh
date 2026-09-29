#!/usr/bin/env bash
set -euo pipefail
# Kézi tartalék. A felület termináljának könyvtárát ez nem változtatja meg.
if [[ $# -ne 1 ]]; then
    echo "Használat: bash futtatas.sh fajl.py" >&2
    exit 2
fi
case "$1" in
    szoveg.py|kodresz.py|karakterszam.py|listamuveletek.py|feldolgozas.py|kosar_04.py|bufe_04.py|onallo.py) ;;
    *) echo "Ismeretlen gyakorlófájl." >&2; exit 2 ;;
esac
script_dir="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd -- "$script_dir"
exec python3 "$1"
