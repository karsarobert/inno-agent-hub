# Oktatói ellenőrzés – 2. módszertani változat

Dátum: 2026. szeptember 13. Környezet: Linux x86-64, Python 3.12.14,
CPU; a fő csomagverziók a requirements.txt-ben szerepelnek.

## Az átdolgozott Python-programok

Mind a hét alapváltozatot újra lefuttattuk, hibamentesen. A programok célját
bemutató kiírások és az új futási összefoglalók is megjelentek.

| Program | Megfigyelt alapérték |
|---|---|
| G02_01 | Becslés −1; veszteség 16; gradiens −8; új súly 0,6; új veszteség 5,76 |
| G02_02 | z = (−1,5; −0,5), a = (0; 0), végső becslés 0,5 |
| G02_03 | 11 paraméter; bemenet (1,3), kimenet (1,1); becslés 0,5 |
| G02_04 | 11 jellemző; 815 tanító-, 272 validációs és 272 tesztminta |
| G02_05 | 40 epoch; végső validációs MAE 0,5625 |
| G02_06 | 692 paraméter; validációs accuracy 0,8100 |
| G02_07 | 8-as türelem; 92 epoch; visszaállított validációs MAE 0,5108 |

A kísérletek külön ellenőrzési másolatban futottak; a csomag forrásai a
kiinduló beállításokat tartalmazzák. A G02_06 módosított (16,16) rejtett
rétegeinél a kimenet 388 paramétert mutatott. Az új JSON-beállítások és a
napló végén lévő összefoglaló a tényleges paraméterszámot őrzik meg.

A G02_07 4-es türelemmel 64 epochig futott; visszaállított validációs
MAE-je 0,5253 volt. A kisebb validációs MAE előre rögzített szempontja
alapján a 8-as türelmet választottuk. Az ezzel és bekapcsolt végső teszttel
végzett új futás 0,4814 teszt MAE-t adott. Az összefoglaló a kiválasztott
8-as türelmet igazolta. A teszteredményből nem választottunk új beállítást.

A korábbi változatban már lefuttatott további próbák számítási kódja nem
változott: G02_01 ráta 0,1 → új súly −0,2; G02_02 harmadik bemenet 2 →
becslés −2; G02_03 első bias 2 → becslés 1,5. A szemléltetőben ezeket a
példákat ismét ellenőriztük. A korábbi 20 epochos regressziós próba MAE-je
0,6058 volt; ez korábbi mérés, nem egy most megismételt 20 epochos futás.

## A helyi HTML-szemléltető

A JavaScript működését helyi DOM-szimulációban ellenőriztük:

- lapváltás és léptetés, első/utolsó lépés gombjai;
- az egy súly alap- és kisebb rátájú példája;
- túl nagy ráta esetén a növekvő veszteség visszajelzése;
- mindhárom hálózati előbeállítás és egy egyedi súly módosítása;
- üres vagy hibás bevitelnél az eredmény elrejtése és a hiba jelzése;
- skálázási példa: 12 → 1,2 a 0–10 tanítótartomány mellett;
- hálózati SVG-k, súly- és biasfeliratok, NumPy/Keras elrendezés.

A hálózati és a súlyváltozást bemutató SVG-ábrákból képet rendereltünk, és
vizuálisan ellenőriztük őket. A HTML nem tölt le futtatáshoz külső könyvtárat,
képet vagy betűkészletet. A teljes oldal böngészős elrendezését ebben az
ellenőrzésben nem teszteltük; a DOM-szimuláció nem böngészős próba.

## Csomag és módszertani ellenőrzés

Ellenőriztük a Python-szintaxist, a dokumentumok fájlhivatkozásait, a HTML
azonosítóit, a 90 perces időbeosztást és a ZIP épségét. A csomagból az
ellenőrzési eredménymappákat és a fejlesztői segédprogramokat kihagytuk.

A tutorutasítások szöveges ellenőrzést kaptak a tesztbeszélgetésben jelzett
problémákra: bevezetés és kódmagyarázat a futás előtt; szemléltetés;
kevesebb kötelező kézi számolás; pontos visszajelzés; aktuális konfiguráció
ellenőrzése; indokolt modellválasztás. Az átdolgozott utasításokkal új,
teljes Innoagent-beszélgetést itt nem futtattunk. A beépített magyarázó
szövegek segítik a következetes tanítást, de az utasításkövetés további
valós kipróbálást igényel.

A tanítási eredmények konkrét próbafuttatások megfigyelései, nem garantált
hallgatói célértékek. A 90 perces terv előre telepített környezetet feltételez;
a külön jelölt módosítási próbák választhatók.
