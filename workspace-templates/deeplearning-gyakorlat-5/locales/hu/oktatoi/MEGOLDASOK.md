# Mért referenciaeredmények és értelmezés

Ezek a csomag készítésekor CPU-n mért eredmények. Ne mondd meg őket előre a hallgatónak; a saját futását és megfigyelését értékelje. A rögzített referencia darabszámai ellenőrizhetők, a saját tanítás utolsó tizedesjegyei környezetenként eltérhetnek.

## Tanítás

| Epocha | Bottleneck | Tanítási MAE, végső súlyokkal | Normál validációs MAE | 0. normál gyakorlópélda MAE | Teljes futás |
|---:|---:|---:|---:|---:|---:|
| 10 | 8 | 0.033397 | 0.030211 | 0.019023 | 6.96 s |
| 30 | 8 | 0.025963 | 0.023619 | 0.016702 | 7.84 s |
| 30 | 16 | 0.026187 | 0.023750 | 0.017864 | 7.25 s |

A 10 és 30 epochás, 8-as bottleneckkel készült futás kezdősúly-azonosítója azonos. A hosszabb tanítás itt javította a normál rekonstrukciót. A 16-os bottleneck most nem adott kisebb validációs hibát: ez elfogadandó tapasztalat, nem hibás hallgatói futás. Más architektúránál a kezdő súlymátrixok és azonosítóik is eltérnek.

## Egyes jelek MAE-ja a rögzített referenciában

| Index | Normál | Rendellenes |
|---:|---:|---:|
| 0 | 0.016702 | 0.071006 |
| 3 | 0.010389 | 0.067872 |

Ezekben a kiemelt példákban a rendellenes jel hibája nagyobb. A teljes eloszlás ettől még átfed: nem minden normál hiba kisebb minden rendellenes hibánál. A hisztogram mindkét indexnél ugyanaz.

## Küszöb – pozitív = rendellenes

| Küszöb | TP | FN | FP | TN | Precision | Recall |
|---:|---:|---:|---:|---:|---:|---:|
| 0.025 | 128 | 0 | 49 | 79 | 72.3% | 100.0% |
| 0.040 | 128 | 0 | 11 | 117 | 92.1% | 100.0% |
| 0.060 | 121 | 7 | 6 | 122 | 95.3% | 94.5% |

- 0.04 → 0.025: nem lesz több TP, mert már az alapfutás is mind a 128 rendellenest észlelte. Az FP viszont 11-ről 49-re nő. A kisebb küszöb itt több téves riasztást, változatlan recallt ad.
- 0.04 → 0.06: FP 11 → 6, FN 0 → 7. A kevesebb téves riasztásért hét elnézett rendellenességgel fizetünk.
- 0.06-nál precision = 121/(121+6) ≈ 95,3%; recall = 121/(121+7) ≈ 94,5%.
- Küszöb 0: minden jel riaszt, TP=128, FP=128, precision=50%, recall=100%.
- Küszöb 1: itt nincs riasztás, TP=0, FP=0, recall=0%, precision nem értelmezhető. A program nem oszt nullával.

A 0.04-en mért 100% recall ennek a kis gyakorlóadatrészletnek és rögzített modellnek az eredménye. Nem általános teljesítményígéret és nem klinikai érzékenységbecslés. A küszöböt ezen a halmazon vizsgáljuk; végső értékeléshez külön, érintetlen és a felhasználási helyzetet képviselő adatok kellenének.
