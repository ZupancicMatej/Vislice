import model

def izpis_poraza(igra):
    return f"Žal si izgubil. Več sreče prihodnjič! Geslo je bilo: {igra.geslo}"

def izpis_zmage(igra):
    return f"Čestitke, uganil si geslo: {igra.geslo} v {len(igra.crke)} ugibih"

def izpis_igre(igra):
    besedilo = f""" GESLO: {igra.pravilni_del_gesla()}
    Nepravilne črke : {igra.nepravilni_ugibi()}
    Zmotiš se lahko le še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()}-krat."""
    return besedilo

def zahtevaj_vnos():
    vnos= input("Ugibaj: ")
    
    if len(vnos) == 1:
        return vnos
    else:
        return None

    return vnos

def pozeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))

        crka = zahtevaj_vnos()
        while crka is None:
            print ("Napačen vnos!")
            crka = zahtevaj_vnos()

        stanje = igra.ugibaj(crka)

        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break

pozeni_vmesnik()