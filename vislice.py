import bottle, model
SKRIVNI_KLJUC = 'Uganil si najbolj skrit ključ vseh časov.'

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get("/")
def index():
    return bottle.template('views/index.tpl')

@bottle.get('/img/<picture>')
def static_file(picture):
    return bottle.static_file(picture, root='/img')

@bottle.post('/nova_igra')
def zacni_novo_igro():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNI_KLJUC, path='/')
    bottle.redirect('/igra/')

@bottle.get("/igra/")
def pokazi_igro(id_igre):
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    igra, stanje = vislice.igre[id_igre]

    return bottle.template('igra', igra = igra, stanje = stanje, id_igre = id_igre, ZMAGA=model.ZMAGA, PORAZ=model.PORAZ)

@bottle.post("/igra/") 
def ugibaj(id_igre):
    id_igre = bottle.request.get_cookie("id_igre", secret=SKRIVNI_KLJUC)
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre, crka)

    bottle.redirect(f'igra/{id_igre}/')

bottle.run(reloader=True, debug=True)