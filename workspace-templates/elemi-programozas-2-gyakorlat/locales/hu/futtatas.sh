#!/usr/bin/env bash
# Kézi tartalék indítás: a gyermekfolyamat is a gyakorlófájl mappájában indul.
set -euo pipefail
csomag_mappa="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  printf '%s\n' 'Használat: bash futtatas.sh [koszontes.py|tetel.py|bufe_02.py|dontes.py|kategoriak.py|onallo.py|alapertek.py|parossag.py]' 'Alapértelmezett: koszontes.py. A program válaszait a terminálba írd.' 'Ez a segéd nem módosítja a felület Futtatás gombját vagy a szülőterminál mappáját.'
  exit 0
fi
program="${1:-koszontes.py}"
if [[ "$program" == */* || "$program" == .* || "$program" != *.py ]]; then
  printf '%s\n' 'Csak a python_gyakorlat mappa .py fájljának nevét add meg, útvonal nélkül.' >&2
  exit 2
fi
if [[ ! -f "$csomag_mappa/python_gyakorlat/$program" ]]; then
  printf 'Nem található: %s\n' "$program" >&2
  exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
  printf '%s\n' 'A python3 nem érhető el. Kérd az oktató segítségét.' >&2
  exit 127
fi
if [[ $# -gt 0 ]]; then shift; fi
cd -- "$csomag_mappa/python_gyakorlat"
exec python3 "$program" "$@"
