"""EKG-jelek megfigyelése – ebben a programban még nincs hálózat.
Bemenet: a helyben tárolt normál és rendellenes jelszakaszok.
Kimenet: két görbe az ekg_jelek.png képen.
Módosítandó: minta_index; ez példát választ, nem módosítja a jel értékeit.
"""
from segedletek import betolt_adatok, index_ellenorzes, uj_mappa, jelpar_rajz, befejezes

# 1. BEÁLLÍTÁS – melyik példát vizsgáljuk meg?
# 0 = első, 1 = második, 2 = harmadik, 3 = negyedik példa.
# Először 0-val futtatunk, majd 3-ra váltunk; 0–127 közötti index választható.
minta_index = 0

# 2. ADATOK BETÖLTÉSE – külön csoportban vannak a normál és rendellenes jelek.
# Mindkét csoport 128 sort tartalmaz. Minden sor egy 140 pontból álló jel.
adatok = betolt_adatok()
normal_jelek = adatok['normal_jelek']
rendellenes_jelek = adatok['rendellenes_jelek']
index_ellenorzes(minta_index, len(normal_jelek))

# 3. EGY-EGY JEL KIVÁLASZTÁSA – a szögletes zárójel jelöli a sor kiválasztását.
# Azonos index két külön csoportban: nem ugyanannak az embernek két mérése.
normal_jel = normal_jelek[minta_index]
rendellenes_jel = rendellenes_jelek[minta_index]

# 4. ÁBRA ÉS ÖSSZEFOGLALÓ – a segéd menti a képet; nem nyit új ablakot.
mappa = uj_mappa(__file__)
jelpar_rajz(mappa, normal_jel, rendellenes_jel, minta_index)
print('\nFUTÁSI ÖSSZEFOGLALÓ')
print(f'Kiválasztott példa: {minta_index + 1}. | Mintaindex: {minta_index}')
print(f'Egy jel 140 mintapontot tartalmaz; a tömb mérete: {normal_jel.shape}')
print('Normál / rendellenes példák: 128 / 128. Az ábra skálázott jelértékeket mutat.')
befejezes(mappa, {'minta_index': minta_index, 'jelhossz': len(normal_jel)})
