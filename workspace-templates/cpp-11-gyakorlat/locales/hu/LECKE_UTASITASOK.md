# Óravezetési útmutató

A pontos feladatok és próbák a FELADATOK.md-ben vannak. A négy blokk külön alkalmon is megoldható; nem feltétel a 24 feladat egy ülésben. Minden feladat saját, rövid maines program. Tipikusan 1–6 sort kell pótolni vagy javítani, a teljes vázat nem kell újraírni. Az időkeret tájékoztató, nem automatikus teljesítési feltétel.

07: mezőelérés → másolat → mutató → tömb → hatókör → unió. A union esetében csak az aktív tag olvasható; ne követelj fix sizeof-értékeket.

08: lekérdező → privát hozzáférési hiba → foglalás → const → két példány → objektumtömb. Elutasításkor az állapot változatlan maradjon. A G08_03-nál a második kérés már az első utáni készletet használja.

09: két konstruktor → tartománykorlátozás → tömbkonstrukció → inicializáló lista → utolsó elem kivétele → kész virtuális példa. A G09_04 forrásellenőrzése kötelező. A G09_05 a logikai elemszámot változtatja, nem a tömb kapacitását. Az öröklődésnél nincs új hierarchiatervezés vagy dinamikus memória.

10: mentés → hozzáfűzés → negatívak számlálása → EOF-hiba → sorvalidálás → ideiglenes listás betöltés. Magyarázd el a megnyitás, írás, lezárás külön hibalehetőségeit. A G10_03 szűk bemeneti szerződésű egyszerű számlálás: az EOF-ellenőrzés nem általános szigorú parser. Az eofbit önmagában nem jelenti a kivonatoló művelet hibáját; fail/bad mellett nincs új érték. A G10_05 teljes tokenellenőrző segédfüggvényt kap. G10_06-nál az üres fájl érvényes, az üres sor hibás; a korábbi állapot csak teljes siker után cserélhető le.

Segítségkor a meglévő kód konkrét soraira utalj. A kérdésekből feladatonként csak a rögzített 1–2-t használd, és mindig a kód ellenőrzése után. Külön pontozás vagy záróteszt nincs; a visszajelzés a kódra és a fogalmak megértésére térjen ki.
