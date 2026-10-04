"""Jelenkénti rekonstrukciós hiba – az eredetit a visszaállított jellel hasonlítjuk össze.
Bemenet: eredeti jelek és a mellékelt, korábbi tanításból mentett rekonstrukciók.
Kimenet: axis_1.png, rekonstrukciok.png, hibaeloszlas.png, MAE-értékek.
Módosítandó: minta_index (0 → 3). Nincs tanítás, TensorFlow sem szükséges.
"""
from segedletek import (np, betolt_adatok, betolt_referencia, index_ellenorzes,
                       uj_mappa, rekonstrukcio_rajz, hibak_rajz, axis_szemleltetes, befejezes)

# 1. BEÁLLÍTÁS – 0 az első, 3 a negyedik példát választja ki mindkét csoportból.
# Az indexváltás nem módosítja a hálózatot vagy a teljes csoport hibaeloszlását.
minta_index = 0

# 2. BETÖLTÉS – mindig a mellékelt 30 epochás referencia, nem a saját utolsó futás.
adatok = betolt_adatok()
referencia = betolt_referencia()
normal_jelek = adatok['normal_jelek']
rendellenes_jelek = adatok['rendellenes_jelek']
normal_vissza = referencia['normal_vissza']
rendellenes_vissza = referencia['rendellenes_vissza']
index_ellenorzes(minta_index, len(normal_jelek))

# 3. KÖZÖS KIS PÉLDA – ezek szemléltető eltérések, nem az EKG-mérés eredményei.
# Két sor = két külön jel; a sor négy száma négy pont abszolút eltérése.
szemlelteto_elteresek = np.array([
    [0.1, 0.1, 0.3, 0.3],  # Az első jel saját átlaga: 0.2.
    [0.4, 0.4, 0.4, 0.4],  # A második jel saját átlaga: 0.4.
])
sajat_atlagok = np.mean(szemlelteto_elteresek, axis=1)  # Két eredmény: [0.2, 0.4].
kozos_atlag = np.mean(szemlelteto_elteresek)             # Egy eredmény: 0.3.

# 4. A VALÓDI JELEK MAE-JA – három jól elkülöníthető lépésben.
# Kivonás: minden eredeti pontot a saját rekonstruált pontjával vetünk össze.
elteresek = normal_jelek - normal_vissza
# Abszolút érték: a pozitív és negatív eltérések ne oltsák ki egymást.
abszolut_elteresek = np.abs(elteresek)
# axis=1: minden sor 140 pontját külön átlagoljuk → 128 jelhez 128 hiba.
normal_hibak = np.mean(abszolut_elteresek, axis=1)

# Ugyanez a három lépés a rendellenes jeleken.
rendellenes_elteresek = rendellenes_jelek - rendellenes_vissza
rendellenes_abszolut = np.abs(rendellenes_elteresek)
rendellenes_hibak = np.mean(rendellenes_abszolut, axis=1)

# 5. ÁBRÁZOLÁS – egy kiemelt pár és a teljes csoport eloszlása külön képen.
mappa = uj_mappa(__file__)
axis_szemleltetes(mappa, szemlelteto_elteresek)
rekonstrukcio_rajz(mappa, [normal_jelek[minta_index], rendellenes_jelek[minta_index]],
                  [normal_vissza[minta_index], rendellenes_vissza[minta_index]],
                  [f'Normál referencia · {minta_index+1}. példa (index {minta_index})',
                   f'Rendellenes referencia · {minta_index+1}. példa (index {minta_index})'],
                  'rekonstrukciok.png')
hibak_rajz(mappa, normal_hibak, rendellenes_hibak)

# 6. ÖSSZEFOGLALÓ – külön a szemléltetés és külön a valódi EKG-eredmények.
print('\nSZEMLÉLTETŐ PÉLDA (nem EKG-mérés)')
print(f'Jelenkénti átlagok: {sajat_atlagok} | Közös átlag: {kozos_atlag:.1f}')
print('\nFUTÁSI ÖSSZEFOGLALÓ')
print(f'Kiválasztott példa: {minta_index + 1}. | Mintaindex: {minta_index}')
print(f'Normál jel MAE: {normal_hibak[minta_index]:.6f}')
print(f'Rendellenes jel MAE: {rendellenes_hibak[minta_index]:.6f}')
print(f'Összes normál jel átlagos MAE: {np.mean(normal_hibak):.6f}')
print(f'Összes rendellenes jel átlagos MAE: {np.mean(rendellenes_hibak):.6f}')
print('Az index csak a kiemelt jelpárt változtatja; a teljes csoport hisztogramja nem változik.')
np.savetxt(mappa / 'hibak.csv', np.column_stack([normal_hibak, rendellenes_hibak]),
           delimiter=',', header='normal_mae,rendellenes_mae', comments='')
befejezes(mappa, {'minta_index': minta_index, 'forras': 'mellekelt_30_epochas_referencia',
                  'normal_mae': float(normal_hibak[minta_index]),
                  'rendellenes_mae': float(rendellenes_hibak[minta_index])})
