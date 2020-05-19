import random

STEVILO_DOVOLJENIH_NAPAK = 9

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

ZACETEK = 'S'

class Igra:
    def __init__(self, geslo, crke=[]):
        self.geslo = geslo.lower()
        
        self.crke = [z.lower() for z in crke]

    def napacne_crke(self):
        napacne = [c for c in self.crke if c not in self.geslo]
        return napacne

    def pravilne_crke(self):
        pravilne = [c for c in self.crke if c in self.geslo]
        return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False

        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        pravilni_del = ""
        for c in self.geslo:
            if c in self.crke:
                pravilni_del += c
            else:
                pravilni_del += "_"

    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.lower()

        if crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(crka)

        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

with open('besede.txt', encoding="utf-8") as f:
    bazen_besed = f.read().split("\n")

def nova_igra():
    beseda = random.choice(bazen_besed)

    igra = Igra(beseda)

    return igra

class Vislice:
    def __init__(self):
        self.igre = {}

    def prost_id_igre(self):
        if self.igre.keys():
            return max(self.igre.keys()) + 1
        else: 
            return 0
    
    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()

        self.igre[id_igre] = (igra, ZACETEK)

        return id_igre

    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(crka)

        self.igre[id_igre] = (igra, novo_stanje)
