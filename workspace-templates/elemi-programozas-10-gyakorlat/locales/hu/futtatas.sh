#!/bin/sh
cd "$(dirname "$0")" || exit 1
exec python3 probak.py "${1:-A1}"
