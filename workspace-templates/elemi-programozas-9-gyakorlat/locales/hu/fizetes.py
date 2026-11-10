# A1: Az összeg a paraméterből jön; a visszatérő pénz önálló felajánlás.
# A helykitöltő még nem kérdez és nem ellenőriz.
def fizetest_beker(fizetendo):
    return 0


fizetendo = 800
atadott = fizetest_beker(fizetendo)
print("Átadott összeg:", atadott, "Ft")
print("Visszajáró:", atadott - fizetendo, "Ft")
