"""Szakaszonkénti ellenőrzések. Példa: python3 probak.py A1
Választható: A1, A2, A3, B1, Z1, mind.
A Z1 ideiglenes mappában dolgozik, nem írja át a munkamappád jelentését.
"""
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import io
import os
import sys
from bufe import Bufe

ARAK = {"tea": 300, "szendvics": 700, "viz": 0}


def uj():
    return Bufe("Iskolai büfé", ARAK)


def allapot(bufe):
    return dict(bufe.arak), bufe.bevetel, list(bufe.eladasok)


def value_error_kell(muvelet):
    try:
        muvelet()
    except ValueError:
        return
    raise AssertionError("A műveletnek ValueError-t kellett volna jeleznie.")


def a1():
    arak = dict(ARAK)
    elso = Bufe("  Iskolai büfé  ", arak)
    masodik = Bufe("Másik", arak)
    assert elso.nev == "Iskolai büfé", "A név tisztítása hibás."
    assert elso.bevetel == 0, "A kezdeti bevétel nem 0."
    assert elso.eladasok == [], "A kezdeti lista nem üres."
    assert elso.eladasok is not masodik.eladasok, "Közös értékesítési lista."
    assert elso.arak == arak, "A másolt árlista tartalma eltér."
    assert elso.arak is not arak, "Az árlista nem saját másolat."
    assert elso.arak is not masodik.arak, "A két büfé árlistája közös."
    arak["tea"] = 999
    assert elso.arak["tea"] == 300, "A külső átírás megváltoztatta a büfét."
    assert masodik.arak["tea"] == 300
    value_error_kell(lambda: Bufe("", ARAK))
    value_error_kell(lambda: Bufe("   ", ARAK))


def a2():
    bufe = uj()
    elotte = allapot(bufe)
    assert bufe.tetel_osszege("tea", 2) == 600
    assert bufe.tetel_osszege("viz", 3) == 0
    assert allapot(bufe) == elotte, "A lekérdezés állapotot módosított."
    for termek, darab in [("tea", 0), ("tea", -1), ("kave", 1)]:
        value_error_kell(lambda t=termek, d=darab: bufe.tetel_osszege(t, d))
        assert allapot(bufe) == elotte, "A hibás lekérdezés módosított."


def a3():
    bufe = uj()
    assert bufe.elad("tea", 2) == 600
    assert bufe.elad("szendvics", 1) == 700
    assert bufe.elad("viz", 3) == 0
    assert bufe.bevetel == 1300
    assert bufe.eladasok == [
        ("tea", 2, 600), ("szendvics", 1, 700), ("viz", 3, 0)
    ], "Az értékesítési rekordok hibásak."
    elotte = allapot(bufe)
    for termek, darab in [("tea", 0), ("tea", -2), ("kave", 1)]:
        value_error_kell(lambda t=termek, d=darab: bufe.elad(t, d))
        assert allapot(bufe) == elotte, "Az elutasított eladás módosított."


def b1():
    elso = uj()
    masodik = Bufe("Másik", ARAK)
    elso.elad("tea", 2)
    assert masodik.bevetel == 0
    assert masodik.eladasok == []
    assert elso is not masodik
    masik = elso
    masik.elad("szendvics", 1)
    assert masik is elso
    assert elso.bevetel == 1300
    assert masodik.bevetel == 0
    elotte = allapot(elso)
    kimenet = io.StringIO()
    with redirect_stdout(kimenet):
        felirat = str(elso)
    assert felirat == "Iskolai büfé: 2 értékesítés, 1300 Ft bevétel"
    assert kimenet.getvalue() == "", "A __str__ ne írjon ki külön szöveget."
    assert allapot(elso) == elotte, "A __str__ állapotot változtatott."


def z1():
    from feldolgozas import munkamenetet_futtat
    adatok = {
        "jo.txt": "tea;2\nszendvics;1\nviz;3\n",
        "vegyes.txt": "tea;2\nkave;1\n\nszendvics;1\ntea;0\nviz;3\ntea;alma\nhibassor",
        "hibas.txt": "kave;1\ntea;0\ntea;-2\ntea;alma\nhibassor\n",
        "ures.txt": "",
    }
    elvart = {
        "jo.txt": (3, 6, 1300, 0, 0),
        "vegyes.txt": (3, 6, 1300, 4, 1),
        "hibas.txt": (0, 0, 0, 5, 0),
        "ures.txt": (0, 0, 0, 0, 0),
    }
    eredeti_mappa = Path.cwd()
    with TemporaryDirectory(prefix="ep10_proba_") as mappa:
        try:
            os.chdir(mappa)
            for nev, tartalom in adatok.items():
                Path(nev).write_bytes(tartalom.encode("utf-8"))
            for nev, vart in elvart.items():
                eredeti = Path(nev).read_bytes()
                with redirect_stdout(io.StringIO()):
                    siker = munkamenetet_futtat(nev, "jelentes.txt")
                assert siker is True, f"Sikertelen munkamenet: {nev}"
                jelent = Path("jelentes.txt").read_text(encoding="utf-8")
                db, darab, bevetel, hiba, ures = vart
                for sor in [
                    f"Értékesítések: {db}", f"Eladott darab: {darab}",
                    f"Bevétel: {bevetel} Ft", f"Hibás sorok: {hiba}",
                    f"Üres sorok: {ures}",
                ]:
                    assert sor in jelent.splitlines(), (nev, sor)
                allapotjel = "Részleges" if hiba else "Teljes"
                assert f"Állapot: {allapotjel}" in jelent.splitlines()
                assert Path(nev).read_bytes() == eredeti, "Módosult a bemenet."
                if nev == "vegyes.txt":
                    for sorszam in [2, 5, 7, 8]:
                        assert any(s.startswith(f"{sorszam}. sor: ") for s in jelent.splitlines())
                    assert "viz;3;0" in jelent.splitlines()
            with redirect_stdout(io.StringIO()):
                assert munkamenetet_futtat("jo.txt", "jelentes.txt") is True
                assert munkamenetet_futtat("jo.txt", "jelentes.txt") is True
            jelent = Path("jelentes.txt").read_text(encoding="utf-8")
            assert jelent.splitlines().count("Büfé: Iskolai büfé") == 1
            Path("jelentes.txt").write_bytes(b"REGI JELENTES")
            with redirect_stdout(io.StringIO()):
                siker = munkamenetet_futtat("ep10_hianyzo.txt", "jelentes.txt")
            assert siker is False
            assert Path("jelentes.txt").read_bytes() == b"REGI JELENTES"
            Path("bemeneti_mappa").mkdir()
            with redirect_stdout(io.StringIO()):
                siker = munkamenetet_futtat("bemeneti_mappa", "jelentes.txt")
            assert siker is False
            assert Path("jelentes.txt").read_bytes() == b"REGI JELENTES"
            Path("cel_mappa").mkdir()
            kimenet = io.StringIO()
            with redirect_stdout(kimenet):
                siker = munkamenetet_futtat("jo.txt", "cel_mappa")
            assert siker is False
            assert "Jelentés elkészült:" not in kimenet.getvalue()
        finally:
            os.chdir(eredeti_mappa)


PROBAK = {"A1": a1, "A2": a2, "A3": a3, "B1": b1, "Z1": z1}

if __name__ == "__main__":
    szakasz = sys.argv[1] if len(sys.argv) > 1 else "A1"
    valasztott = list(PROBAK) if szakasz.lower() == "mind" else [szakasz.upper()]
    if any(nev not in PROBAK for nev in valasztott):
        print("Választható: A1, A2, A3, B1, Z1, mind")
        raise SystemExit(2)
    for nev in valasztott:
        try:
            PROBAK[nev]()
        except Exception as hiba:
            print(f"{nev}: eltérés – {type(hiba).__name__}: {hiba}")
            raise SystemExit(1)
        else:
            print(f"{nev}: az ellenőrzések rendben.")
    print("A kód szerkezetét és a feladat értelmezését is ellenőrizzétek.")
