# Deep Learning 2026 · 7. gyakorlat · Innoagent+Colab · 1.0

Az agent beszélgető tutor; a hallgató a Colabban szerkeszt és futtat. A csomag meglévő
Innoagent alkalmazáshoz ad munkaterületi utasításokat, nem telepít vagy konfigurál önálló alkalmazást.
Első használat előtt olvasd el a START-HERE.md fájlt.

## Fájlok

| Fájl | Szerep |
|---|---|
|agent.md|A tutor kötelező működése, Colab-munkamegosztása, visszajelzése és lezárása.|
|LECKE_UTASITASOK.md|A 32 cella pontos célja, teendője, bizonyítéka és elfogadási szempontja.|
|PROGRAM_BEMUTATOK.md|Fogalmi magyarázatok és hibakeresési támasz.|
|HALADAS.md|Üres belső haladási minta; natív memória hiányában opcionális jegyzet.|
|PTE_DL7_FELADATOK.ipynb|Cellánként rendezett hallgatói munkapéldány, önállóan kitöltendő cellákkal.|
|DL_07_gyakorlat.html|A korábban elkészült, eltérő adatokon dolgozó offline segédlet.|
|CELLA_TERKEP.json|A forrásnotebook és az új cellaazonosítók kapcsolata.|

## Munkamenet

Megnyitás→egy cella magyarázata→Colab-kódírás/futtatás→rövid tényleges kimenet→tutori visszajelzés→következő cella.
Nem kérünk helyi Run-gombot, terminált, fájlfafrissítést vagy automatikus Colab-hozzáférést.
Az agentnek nem kell és nem szabad a hallgató teljes megoldását helyette leírnia.

A korábbi notebookban már sok kész kód volt. Az új változat külön jelzi a kész és az önálló cellákat.
R04–R06, R10, M03–M06, M09, A03–A05, A07–A09 rövid saját kódot kér; a többi cella kész,
de a kimenetét értelmezni kell. A három zárókérdés egyenként következik, nincs új kötelező feladat.

Internet és saját Colab-hozzáférés szükséges; a TensorFlow / NumPy / Pandas / scikit-learn / Matplotlib a Colabban fut.
GPU opcionális. Adatletöltési hiba esetén az oktató tudja biztosítani a hivatalos NPZ-fájlokat;
a helyi munkakönyvtárba feltöltött fájlokat a betöltőcellák felismerik.
