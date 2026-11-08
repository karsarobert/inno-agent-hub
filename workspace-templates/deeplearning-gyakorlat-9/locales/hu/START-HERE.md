# Indítás · 9. gyakorlat

1. Csomagold ki a ZIP-et. A `PTE_DL9_CNN_LAB.ipynb` notebookot nyisd meg Google Colabban a notebook megnyitása/feltöltése lehetőséggel, vagy helyi Jupyterben. A kódot ott futtatod; az Innoagenttel a magyarázatot és az eredményeket beszéled meg.
2. Colabban válassz GPU-t: Futtatókörnyezet → Futtatókörnyezet típusának módosítása → GPU → Mentés. E01 ténylegesen ellenőrzi; GPU: [] esetén megáll. A menü neve a felület nyelvétől függhet. Helyi Jupyter CPU-n is használható, lassabban.
3. Indítsd a 9. lecke oktató által beállított Innoagentjét. Írd: „Megnyitottam a 9. gyakorlat notebookját, kezdjük E01-gyel.” Ha már futtattad, a környezet/TF/GPU sorokat küldd el.
4. Egyszerre csak az aktuális cellát futtasd; a tutor magyaráz, majd a kód vagy az eredmény jelentéséről kérdez. Minden kód teljes. A kész kódot nem kell visszaküldeni, csak a kért rövid kiírást és értelmezést. Hibánál a releváns kód és az utolsó hibasorok segítenek.
5. B01 és R00 a két `forrasok` HTML-hez kapcsolódó megfigyelés. Böngészőben nyisd meg őket; CDN/kapcsolati gondnál a tutor szöveges példával segít. Ne töltsd a HTML-t Python-kódcellába. Z01 beszélgetés.

A letöltéshez internet kell: a CIFAR-10 archívum kb.170 MB, a felbontott gyorsítótár több helyet foglal. Az adatok a Keras helyi gyorsítótárába, a futás kimenetei a `dl9_results` mappába kerülnek. Colab újraindításkor a helyi fájlok elveszhetnek; saját célú mentés opcionális. A teljes notebook és a tanulási eredmény nem beadandó. A két CNN6–6 epochát kap; egy futó tanítást várj meg.

Helyi telepítésnél az oktató/technikai környezet használhatja a requirements.txt-t. A lecke nem kér terminálhasználatot a tanulótól. Kipróbált referencia: Python 3.12,TensorFlow 2.21.0 CPU; más verzió/eszköz eltérő számokat adhat. Az Innoagent élő platformján és Colab GPU-n a futást külön érdemes órakezdés előtt ellenőrizni.
