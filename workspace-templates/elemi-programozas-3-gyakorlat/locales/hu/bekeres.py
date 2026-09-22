# W2: a függvény most még a negatív számot is visszaadja.
def nemnegativ_egesz_beker(kerdes):
    szam = int(input(kerdes))
    # Ide írd az ismételt bekérést.
    return szam


kave_darabszam = nemnegativ_egesz_beker("Hány kávét kérsz? ")
print(f"Elfogadott darabszám: {kave_darabszam}")
