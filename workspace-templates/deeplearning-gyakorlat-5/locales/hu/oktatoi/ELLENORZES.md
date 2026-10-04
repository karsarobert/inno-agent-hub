# Elvégzett ellenőrzések – 2026-10-04

Környezet: Linux x86-64, Python 3.12.14, NumPy 2.3.5, Matplotlib 3.10.8,
TensorFlow CPU 2.20.0, Keras 3.15.1. A TensorFlow számára látható GPU-lista üres.

A teljes környezetellenőrzés és mind a négy program elindult, az összes előírt
módosítással. Összesen 13 sikeres futás: környezet; G01 index 0/3; G02 10/30 epocha
és opcionális 16-os bottleneck; G03 index 0/3; G04 küszöb 0.04/0.025/0.06, továbbá
0 és 1 határeset. A futások külön munkakönyvtárból is működnek. Mindegyik kép és
JSON-összefoglaló létrejött, nem volt stderr-figyelmeztetés.

A 10 és 30 epochás modell azonos kezdősúlyokat kapott. Az ismételt 30 epochás
futás rekonstrukciói ebben a környezetben bitazonosak a mellékelt referenciával.
Ellenőriztük a 896 kiválasztott forrássor diszjunktságát, a küszöbök négy
konfúziósmátrix-értékét, a nulla riasztásnál nem értelmezhető precisiont, és az
érvénytelen indexek érthető elutasítását.

A mért teljes Run-idő a két normál tanításnál kb. 7,0–7,8 másodperc volt, beleértve
az importot, mérést és ábramentést. Más gépen eltérhet. A tesztben legfeljebb két
ellenőrző folyamat futott egyszerre; a hallgató egymás után futtatja a példákat.
A részletes gépi jegyzőkönyv: ellenorzott_futasok.json.

Az 1.1-es változat új ábrái is elkészültek: a kétsoros axis=1 példa, a precision
és recall két külön csoportját bemutató sávok, valamint a saját 10 és 30 epochás
futás összehasonlítása. Ezeket képként is ellenőriztük. A 16-os bottleneckhez
nem készült félrevezető összehasonlítás a 8-as bottleneck korábbi futásával.
A rövid mappanevek sorszámozását és a korábbi tartalom megőrzését külön is
ellenőriztük. A csomag nem tartalmazza a tesztfutások nezet mappáját.

A mintaábrák a mintakepek mappában vannak. Az élő Innoagent-beszélgetést az
alkalmazásban nem teszteltük; ehhez az AGENT_PROBAFORGATOKONYV.md ad célzott próbákat.
A tutori utasítások és a Python-futások ellenőrzése nem bizonyítja önmagában az
alkalmazás üzenetkezelésének hibamentességét.
