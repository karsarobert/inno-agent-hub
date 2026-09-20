# Változások – 1.1

A 2026. szeptember 20-i tesztbeszélgetés és a jóváhagyott észrevételek alapján.

| Megfigyelés | Javítás |
|---|---|
| A hallgató a tanítási beállításokat csak megnézte. | Kötelező negyedik spirálfutás: 50–50 hálózaton a ráta 0.01 → 0.001; minden más azonos. |
| Kimaradt a két gradiens, a fit és a predict/argmax részletes bemutatása. | Konkrét kódblokkok és futtatás előtti bemutatási feltételek az agentben és a forgatókönyvben. |
| A categorical/sparse különbség csak a hibás tesztválasz után került elő. | Az első spirálfutás előtt címkealak–veszteség táblázat és példa. |
| Inno előre megadta az összehasonlítás válaszát. | Semleges adatok → hallgatói értelmezés → visszajelzés; nincs előre kiemelt győztes. |
| A választási szabály csak az eredmények után hangzott el. | Kisebb validációs loss, pontos egyezésnél kevesebb paraméter: az első spirálfutás ELŐTT közlendő. |
| A választási indok készen bemásolható volt. | A hallgató saját futást választ és saját indokot ír; a tutor csak utána segít a beillesztésben. |
| A nagyobb modell kisebb loss-a és alacsonyabb pontossága elsikkadt. | Külön értelmezési pont és tanítópélda a két mutató eltérő rangsoráról. |
| A grafikonokra általános igen/nem kérdések jutottak. | Külön tanítási és validációs megfigyelés, egy konkrét mátrixcella értelmezése. |
| A végső teszt után azonnal elkezdődött a kvíz. | Kötelező várakozás a tesztábrák értelmezésére; a program záróüzenete is ezt kéri. |
| A 100% általános érvényűnek tűnhetett. | Az adott 120 pontra vonatkozó eredmény, új pontokra nem garancia. |
| A záró összegzés biztos tudást állított. | „A válaszaid alapján…” megfogalmazás; futás, szerkesztés, értelmezés és felismerés elkülönítése. |
| Az új kötelező futás időt igényel. | Új 45+45 perces menetrend; nincs plusz kötelező batch- vagy regressziós kísérlet. |

A tíz kódértési kérdés és a helyes válaszok változatlanok; a kérdéseket
megelőző tanítás lett teljesebb. Inno továbbra is bemutatkozik, Run-nal
futtatást kér, hiányzó csomagnál az oktatóhoz irányít, figyelmeztet a Nézet
frissítésére, és egyértelműen lezárja az órát.

## Frissítés

Az 1.1 ZIP-et új mappába csomagold ki, ezt nyisd meg munkaterületként, és
indíts új beszélgetést az új agent.md-vel. A korábbi hallgatói módosításokat
és eredményeket őrizd meg a régi mappában. A korábbi preset nem frissül
magától attól, hogy az új csomagot letöltötted.

## Megjelenítés

A hallgatói szöveghez egyszerű kódblokkokat és szabályos táblázatokat kérünk.
Az alkalmazás automatikus eszközpaneljét és exportformázását a tananyag nem
kapcsolja ki. Az új tutori működés élő felületi újratesztelése oktatói feladat;
a technikai futásellenőrzés részletei az ELLENORZES.md-ben találhatók.
