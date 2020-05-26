import bottle, model
SKRIVNI_KLJUC = 'Uganil si najbolj skrit ključ vseh časov.'

DATOTEKA_S_STANJEM = 'stanje.json'

bottle.TEMPLATE_PATH.insert(0, 'views')

vislice = model.Vislice(DATOTEKA_S_STANJEM)

@bottle.get("/")
def index():
    return bottle.template('index')

@bottle.get('/img/<picture>')
def static_file(picture):
    return bottle.static_file(picture, 'img')

@bottle.post('/nova_igra')
def nova_igra():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = vislice.nova_igra()
    vislice.zapisi_igre_v_datoteko()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNI_KLJUC, path='/')
    bottle.redirect('/igra/')

@bottle.get("/igra/")
def pokazi_igro():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    igra, stanje = vislice.igre[id_igre]

    return bottle.template('igra', igra = igra, stanje = stanje, id_igre = id_igre, ZMAGA=model.ZMAGA, PORAZ=model.PORAZ)

@bottle.post("/igra/") 
def ugibaj():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    crka = bottle.request.forms.crka

    vislice.ugibaj(id_igre, crka)
    vislice.zapisi_igre_v_datoteko()

    bottle.redirect(f'igra/')

bottle.run(reloader=True, debug=True)