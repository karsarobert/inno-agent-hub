# CPP_09 – Rövid munkalap

Ez referencia, nem külön kitöltendő feladat. Inno vezeti a haladást.

| Rész | Fő gondolat | Próba |
|---|---|---|
| G09_01 | Három konstruktor | 0/0, 17/0, 23/12 |
| G09_02 | Feltételes kezdőérték és állapotmegőrzés | -1 és 101 → 50; sikertelen 120 után 70 marad |
| G09_03 | Adat és díjszabás külön osztályban | 1100, 1100, 2000; másik díjszabással 1800 |
| G09_04 | Objektumok az objektumtömbben | 20, belső lapon 5, külsőn továbbra is 20 |
| P1–P3 | Jegy, pénztár, ismétlés tiltása | Négy külön hely, ötödik elutasítva |
| P4–P5 | Visszaváltás, aktív tartomány, összeg | Középső visszaváltás után 3/11000 |
| P6 | Szöveg értékként visszaadva | Aktuális és üres pénztár összefoglalója |

A projekt pontos interfésze és próbasora a PROJEKT.md-ben van. Sor 1–3, szék 1–4. Nézőtér: 12 hely; tároló: 4 jegy. A sor–szék párnak mindkét tagja egyezzen azonos helyhez. A darab az aktív elemek száma, nem az utolsó index. Hibás művelet nem változtathat állapotot. Visszaváltás után csak az aktív előtagot olvassuk. A bevételt és a jegy árát számítjuk.

Egy új program olvasásakor keresd meg: melyik a típus, hol hozunk létre objektumot, melyik konstruktor fut, mely tagok inicializálódnak, és melyik művelet csak lekérdezés. A konstruktor előtti visszatérési típus hibás. Az inicializálólista nem közönséges függvényhívás-lista. A tagobjektumok a külső konstruktor törzse előtt létrejönnek.

Mentés után RUN. Fordítási hibánál az első lényeges üzenetet nézd meg; régi binárist ne futtass sikeres új fordítás helyett. Más objektummal és határértékkel is ellenőrizd a megoldást. A húszkérdéses tesztben az első érdemi válasz számít. A gyakorlat végén nincs új feladatsor vagy házi feladat.
