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

@bottle.post("/igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect(f'igra/{id_igre}/')

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]

    return bottle.template('igra', igra = igra, stanje = stanje, id_igre = id_igre, ZMAGA=model.ZMAGA, PORAZ=model.PORAZ)

@bottle.post("/igra/<id_igre:int>/") 
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')

    vislice.ugibaj(id_igre, crka)

    bottle.redirect(f'igra/{id_igre}/')

@bottle.post('/nova_igra')
def zacni_novo_igro():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie("id_igre", id_igre, secret=SKRIVNI_KLJUC, path='/')

bottle.run(reloader=True, debug=True)