#!/usr/bin/env bash
# A csomag saját python_gyakorlat mappájából választ fájlt.
set -euo pipefail
csomag_mappa="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  printf '%s\n' 'Használat: bash futtatas.sh [hello.py|bufe1.py|…|teglalap.py]' 'Alapértelmezett fájl: hello.py. A program bemenetét a terminálba írd.'
  exit 0
fi
program="${1:-hello.py}"
if [[ "$program" == */* || "$program" == .* || "$program" != *.py ]]; then
  printf '%s\n' 'Csak a python_gyakorlat mappa .py fájljának nevét add meg, útvonal nélkül.' >&2
  exit 2
fi
if [[ ! -f "$csomag_mappa/python_gyakorlat/$program" ]]; then
  printf 'Nem található: %s\n' "$program" >&2
  exit 2
fi
if ! command -v python3 >/dev/null 2>&1; then
  printf '%s\n' 'A python3 nem érhető el. Kérd az oktató segítségét a környezet beállításához.' >&2
  exit 127
fi
if [[ $# -gt 0 ]]; then shift; fi
exec python3 "$csomag_mappa/python_gyakorlat/$program" "$@"
