"""Különálló, szándékosan hibás példa. Előbb futtasd, utána javítsd."""


class ProbaBufe:
    eladasok = []

    def __init__(self, nev):
        self.nev = nev

    def rogzit(self, termek):
        self.eladasok.append(termek)


elso = ProbaBufe("Első")
masodik = ProbaBufe("Második")
elso.rogzit("tea")
print("Első:", elso.eladasok)
print("Második:", masodik.eladasok)
print("Közös lista:", elso.eladasok is masodik.eladasok)
