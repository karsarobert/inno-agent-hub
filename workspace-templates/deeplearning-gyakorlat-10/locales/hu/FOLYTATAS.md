# Technikai helyreállítás — kész kóddal

A megértett fogalmakat nem vizsgáztatjuk újra. Egyszerre egyetlen aktuális cellát adjon a tutor, teljes kóddal. Az alábbi felsorolás oktatói/tutori támpont; nem kell a hallgatónak egyszerre végigfuttatnia mindent.

## Elveszett változók a CAM-részben

E01→C01→C02 kell. C03 rögzíti a célosztályt; C04 építi az aktivációs próbát; C05 definiálja a rajzolási/CAM-segédeket. C06/C07 ezután ismételhető. Az osztályozó nem tanul, de a korábban igazolt értelmezést nem kell újramondani.

## Letöltési hiba

Az A01-ben használt labels.csv és final_files.zip pontos referenciafájlját az oktató előre a dl10_data mappába helyezheti. Az ellenőrzőösszegek a lecke A01-kódjában vannak. A két fájl a forrásként adott PTE_DL10_AGE_PRED notebook Drive-azonosítóiból származik. Ne hagyd ki a hash-ellenőrzést és ne használj néma szintetikus helyettesítést. C01 nem tölt le képet külső forrásból: a DL10_assets.zip helyi példányát vagy a Colab feltöltőgombját használja. Kernel-/futásvesztés után, ha a fájlok is eltűntek, ugyanazt a képcsomagot töltsd fel újra; GPU-t előtte állíts be.

## Elveszett kernel, de a helyi eredményfájlok megvannak

Egyenként állítsd vissza E01, C01, C02, C03, C04, C05, A01, A02, A03, A04, A05, B02, F01, F02, M01 állapotát. A helyi adatellenőrzés és a cache-azonosítás ismétlésével ugyanazokat a mintákat igazoljuk; a cache-találatot így kell nevezni. M01 nulláról újraépíti a kis fejet. Ezután add az alábbi R01 helyreállító cellát a kész fejhez, fit nélkül. R01 a validációs vektorokból az értékelő adatfolyamot is helyreállítja.

```python
from types import SimpleNamespace
fej_fajl = munkamappa / "age_head_best.weights.h5"
required = [fej_fajl, munkamappa / "head_history.json", munkamappa / "selection.json"]
if not all(utvonal.exists() for utvonal in required):
    raise RuntimeError("Completed training files are missing. Restart head training at M01.")
fej_validacios_adatok = tf.data.Dataset.from_tensor_slices((validacios_jellemzok, validacios_korok)).batch(BATCH).with_options(beallitasok)
korfej.load_weights(fej_fajl)
tortenet = SimpleNamespace(history=json.loads((munkamappa / "head_history.json").read_text()))
valasztas = json.loads((munkamappa / "selection.json").read_text())
cam_results_path = munkamappa / "cam_results.json"
cam_eredmenyek = json.loads(cam_results_path.read_text()) if cam_results_path.exists() else {"status": "CAM execution not recovered"}
print("Restored completed head and the saved pre-test selection:", valasztas)
```

M03-mal a választott checkpoint újramérhető, de a teszt alapján nem választható másik állapot. Ha már vannak megbeszélt teszteredmények, a results.json és test_errors.csv táblázataiból idézd őket. Ha a futási változók is kellenek, a változatlan fejjel V01→V02 újrafuttatható technikai helyreállításként; ez nem új kísérlet és nem tesztre hangolás. V03 a mintákat, X01 a regressziós térképet állítja helyre. A fenti visszaállítás C04 és C05 kész segédeit is helyrehozza X01-hez.

Ha csak M01-től szeretnétek új tanítást, a F02-ig szükséges állapot és érvényes cache megléte után M01→M02→M03 következik. Részben megszakadt M02-t nem tekintünk pontosan folytathatónak pusztán a best súlyfájlból: új fej, friss optimalizáló és új history kell. A korábbi megértés elfogadott marad.

Az oktatói cache opcionálisan a dl10_results/feature_cache alá másolható. Csak azonos képsorrend, képhash, bázissúly, előfeldolgozás és TensorFlow-verzió mellett használódik; eltérésnél a program újra számol. Sem kézi fájlnév-átírással, sem a névben lévő hash átírásával nem szabad egyezést erőltetni.

A helyreállító R01-kód változatlan átadása kötelező, nem feladatváz. Nincs végső fájlbekérés.
