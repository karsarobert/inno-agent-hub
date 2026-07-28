---
name: teacher-report-generator
description: A tanuló által jóváhagyott, adatminimalizáló C++ haladási jelentés készítése a helyi progress.json és feedback fájlokból.
---

# Tanári haladási jelentés

## Előfeltétel: egyértelmű jóváhagyás

A jelentés generálása előtt mondd el, milyen fájlokból dolgozol, és kérj kifejezett jóváhagyást. A `progress.json` fájlban a `consent.shareTeacherReport` mezőt csak jóváhagyás után állíthatod `true` értékre. Név vagy azonosító helyett alapértelmezetten `Tanuló` szerepeljen.

## Engedélyezett források

- `progress.json`;
- a tanuló által kijelölt `feedback/` fájlok;
- a tanuló által választott beadandók rövid összesítése.

Ne idézz teljes chatet, ne továbbíts forráskódot, és ne vegyél fel új személyes adatot.

## Kimenet

Másold a `templates/teacher-report.md` szerkezetét, töltsd ki ellenőrizhető állításokkal, és mentsd `teacher-report.md` néven a munkatér gyökerébe. A jelentés elején szerepeljen, hogy ez a tanuló által jóváhagyott összesítés.

## Minőségi követelmények

- A kompetenciaszinthez mindig kapcsolj bizonyítékot vagy jelöld, ha még nincs elég adat.
- A visszatérő nehézséget semleges, fejlesztő nyelven fogalmazd meg.
- Egyetlen, reális következő javasolt lépést adj.
- A jelentés exportja vagy leadása a tanuló feladata; ezt a készség nem automatizálja.
