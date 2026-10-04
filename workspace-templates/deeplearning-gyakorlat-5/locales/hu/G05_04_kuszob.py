"""Küszöbös döntés – a rekonstrukciós hibából riasztás vagy elfogadás lesz.
Bemenet: eredeti jelek és rögzített referencia-rekonstrukciók. Nincs új tanítás.
Kimenet: darabszámok, hibaeloszlas.png, dontesek.png, precision_recall.png.
Módosítandó: kuszob (0.04 → 0.025 → 0.06). Pozitív osztály = rendellenes.
"""
from segedletek import (np, betolt_adatok, betolt_referencia, uj_mappa,
                       hibak_rajz, dontes_rajz, precision_recall_rajz, befejezes)

# 1. BEÁLLÍTÁS – a küszöböt elérő hibánál riasztunk.
# Csak a döntési határt változtatjuk, a rekonstrukciókat nem.
kuszob = 0.04
if not isinstance(kuszob, (int, float)) or not np.isfinite(kuszob) or kuszob < 0:
    raise SystemExit('A kuszob véges, nemnegatív szám legyen!')

# 2. ADATOK ÉS HIBÁK – a rögzített rekonstrukciókból újraszámítjuk ugyanazokat a MAE-ket.
adatok = betolt_adatok()
referencia = betolt_referencia()
normal_elteresek = np.abs(adatok['normal_jelek'] - referencia['normal_vissza'])
rendellenes_elteresek = np.abs(adatok['rendellenes_jelek'] - referencia['rendellenes_vissza'])
normal_hibak = np.mean(normal_elteresek, axis=1)
rendellenes_hibak = np.mean(rendellenes_elteresek, axis=1)

# 3. DÖNTÉS – True = a szabály rendellenesnek jelzi az adott jelet.
# A normál csoporton adott riasztás téves, a rendellenes csoporton helyes.
normal_riasztas = normal_hibak >= kuszob
rendellenes_riasztas = rendellenes_hibak >= kuszob

# 4. A NÉGY ESET MEGSZÁMLÁLÁSA – np.sum megszámolja a True értékeket.
# A ~ megfordítja a logikai tömböt: ahol nem riasztottunk, ott lesz True.
teves_riasztas = int(np.sum(normal_riasztas))                # FP: normálra riasztás.
helyes_normal = int(np.sum(~normal_riasztas))                # TN: normált elfogad.
helyes_rendellenes = int(np.sum(rendellenes_riasztas))        # TP: rendellenest észlel.
elnezett_rendellenes = int(np.sum(~rendellenes_riasztas))     # FN: rendellenest elnéz.

# 5. PRECISION – A RIASZTÁSOKBÓL INDULUNK. Közülük hány volt jogos?
# Az összes riasztás = helyes riasztás (TP) + téves riasztás (FP).
riasztasok = helyes_rendellenes + teves_riasztas
precision = helyes_rendellenes / riasztasok if riasztasok > 0 else None

# 6. RECALL – A VALÓDI RENDELLENESSÉGEKBŐL INDULUNK. Közülük hányat találtunk meg?
# A valóban rendellenesek = észleltek (TP) + elnézettek (FN).
valodi_rendellenessegek = helyes_rendellenes + elnezett_rendellenes
recall = helyes_rendellenes / valodi_rendellenessegek

# 7. ÖSSZEFOGLALÓ – előbb darabszámok, utána ugyanazokból a két külön arány.
print('\nFUTÁSI ÖSSZEFOGLALÓ')
print(f'Küszöb: {kuszob:.3f} | Pozitív osztály: rendellenes')
print(f'Helyesen jelzett rendellenességek (TP): {helyes_rendellenes}')
print(f'Elnézett rendellenességek (FN): {elnezett_rendellenes}')
print(f'Téves riasztások (FP): {teves_riasztas}')
print(f'Helyesen elfogadott normál jelek (TN): {helyes_normal}')
print(f'PRECISION: {riasztasok} riasztásból {helyes_rendellenes} jogos, {teves_riasztas} téves.')
if precision is None:
    print('Precision: nem értelmezhető, mert nincs riasztás.')
else:
    print(f'Precision = {helyes_rendellenes}/{riasztasok} = {precision:.1%}')
print(f'RECALL: {valodi_rendellenessegek} valódi rendellenességből {helyes_rendellenes} észlelt, {elnezett_rendellenes} elnézett.')
print(f'Recall = {helyes_rendellenes}/{valodi_rendellenessegek} = {recall:.1%}')

# 8. KÉPEK MENTÉSE – a két sávon látszik, miből indul a két külön arányszám.
mappa = uj_mappa(__file__)
hibak_rajz(mappa, normal_hibak, rendellenes_hibak, kuszob)
dontes_rajz(mappa, helyes_rendellenes, elnezett_rendellenes, teves_riasztas, helyes_normal, kuszob)
precision_recall_rajz(mappa, helyes_rendellenes, elnezett_rendellenes, teves_riasztas)
befejezes(mappa, {'kuszob': kuszob, 'TP': helyes_rendellenes, 'FN': elnezett_rendellenes,
                 'FP': teves_riasztas, 'TN': helyes_normal, 'precision': precision, 'recall': recall,
                 'forras': 'mellekelt_30_epochas_referencia', 'pozitiv': 'rendellenes'})
