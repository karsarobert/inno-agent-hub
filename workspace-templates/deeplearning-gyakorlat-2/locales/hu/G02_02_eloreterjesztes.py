"""Három bemenet, két rejtett neuron, egy kimenet.

Ez egy kézzel beállított hálózat; a program nem tanít.
Bemenetek → súlyozott összegek + bias → ReLU → lineáris kimenet.
A mátrix egy sora egy neuron három bejövő súlyát tartalmazza.
Részletes kódbemutatás: PROGRAM_BEMUTATOK.md.
Szemléltetés: szemlelteto.html (böngészőben megnyitható).
"""

import numpy as np

print('Három bemenet, két rejtett neuron, egy kimenet.')
print('Ez egy kézzel beállított hálózat; a program nem tanít.\nBemenetek → súlyozott összegek + bias → ReLU → lineáris kimenet.\nA mátrix egy sora egy neuron három bejövő súlyát tartalmazza.')

bemenetek = np.array([1.0, 2.0, -1.0], dtype=np.float32)
rejtett_sulyok = np.array([[1.0, -1.0, 0.5],
                          [-0.5, 1.0, 1.0]], dtype=np.float32)
rejtett_bias = np.array([0.0, -1.0], dtype=np.float32)
kimeneti_sulyok = np.array([[2.0, -1.0]], dtype=np.float32)
kimeneti_bias = np.array([0.5], dtype=np.float32)

# Egy sor egy rejtett neuron súlyait tartalmazza. A @ mátrixszorzás.
sulyozott_osszegek = rejtett_sulyok @ bemenetek + rejtett_bias
rejtett_kimenetek = np.maximum(0.0, sulyozott_osszegek)
becsles = kimeneti_sulyok @ rejtett_kimenetek + kimeneti_bias


# A kiírás összeköti az ábra nyilait a mátrix soraival.
for i in range(2):
    print(f"h{i}: bemenetek={bemenetek}, sulyok={rejtett_sulyok[i]}, "
          f"bias={rejtett_bias[i]}, z={sulyozott_osszegek[i]:.4f}, "
          f"ReLU={rejtett_kimenetek[i]:.4f}")
print("Kimeneti neuron: sulyok=", kimeneti_sulyok[0], "bias=", kimeneti_bias[0])

print("Bemenetek:", bemenetek)
print("Rejtett sulyok alakja:", rejtett_sulyok.shape)
print("Sulyozott osszegek:", sulyozott_osszegek)
print("ReLU utani kimenetek:", rejtett_kimenetek)
print("Kimeneti sulyok alakja:", kimeneti_sulyok.shape)
print(f"Vegso becsles: {becsles[0]:.4f}")
