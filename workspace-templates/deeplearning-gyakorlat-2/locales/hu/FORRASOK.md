# Források és átdolgozási döntések

## A felhasználó oktatási anyagai

- **DL_02.html:** a korábban elkészített második elméleti óra. A gyakorlat
  az egyetlen súly tanulásától az előreterjesztésen át a tanítható modellekig
  követi a fogalmi sorrendet. Az első két program a részletes számpéldákhoz kapcsolódik.
- **PTE_DL2.ipynb / PTE_DL2(1).ipynb:** a gyakorlati témák forrása, különösen
  a Keras-modellépítés, boradatokon végzett regresszió, pontcsoportok
  osztályozása és a tanulási görbék értelmezése. A notebookot önállóan
  futtatható, teljes Python-programokká dolgoztuk át.
- **Deep Learning 2023 02.pptx:** a második elméleti óra eredeti diasora;
  a hozzá készült HTML közvetítésével adja a fogalmi hátteret.
- **deeplearning-gyakorlat-1-hu.zip:** a korábbi Innoagent-munkaterület és
  a magyar tutorfolyamat folytonossága. Az első alkalom témakorlátait nem
  vettük át a második alkalomra.
- **cpp_02.zip:** a tutor bemutatkozása, magyarázó stílusa, a hallgatói
  szerkesztés és futtatás, az egyenként feltett kérdések és a saját szavas
  kódmagyarázat módszertani mintája. A C++-feladatokat és a fordítási lépést
  Python-környezetre nem másoltuk át.

## A 2 × 45 perchez igazított változat

A kész programokban nincs kitöltendő rész. Minden lépés egy kis módosítást
és az eredmény értelmezését kéri. A telepítés az óra előtti előkészítés.
A példák helyi CPU-n futnak, az adatfájl a csomagban van.

A boradatok azonos teljes sorait egyszer szerepeltetjük; három külön
adathalmazt használunk, és a skálázót csak tanítóadatokon illesztjük.
A kis hálózatokkal a kód és az alapfogalmak áttekinthetők. A módszer nem
egy adott pontosság vagy optimális hálózati felépítés ígérete.

A teszthalmazt a modellválasztás után használjuk. A hetedik program a
korai leállítást mutatja be a már ismert regressziós példán. Dropout és
batch normalizáció nem szerepel sem az alapfeladatokban, sem a házi feladatban.

## Technikai háttér

Az alábbi hivatalos dokumentációk a használt fogalmakhoz és hívásokhoz adnak hátteret:

- [TensorFlow: helyi pip-telepítés](https://www.tensorflow.org/install/pip)
- [Keras: Dense réteg és a kernel elrendezése](https://keras.io/api/layers/core_layers/dense/)
- [Keras: tanítás, kiértékelés és előrejelzés](https://keras.io/api/models/model_training_apis/)
- [Keras: EarlyStopping](https://keras.io/api/callbacks/early_stopping/)
- [Keras: to_categorical](https://keras.io/api/utils/python_utils/#to_categorical-function)
- [scikit-learn: train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [scikit-learn: MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
- [scikit-learn: StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- [scikit-learn: make_blobs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html)

A boradatok részletes eredete és licence az `adatok/FORRAS.md` fájlban található.
A saját próbafuttatások adatait az `ELLENORZES.md` rögzíti; ezek nem a
hallgatók jövőbeli futásainak eredményei.

## A második módszertani változat alapja

A felhasználó által átadott „markdown(7).md beillesztve” tesztbeszélgetés és
az ahhoz közösen elfogadott észrevételek: új programok konkrét bevezetése,
a kódblokkok előzetes magyarázata, vizuális támogatás, arányos kérdezés,
ellenőrzött módosítások és a validáción alapuló modellválasztás.
A szemlelteto.html ezekhez a Python-példákhoz készített saját SVG-ábrákat
és számításokat tartalmaz. A boros mintasor forrása a mellékelt CSV.
