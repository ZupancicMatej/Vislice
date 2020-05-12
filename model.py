STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

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

