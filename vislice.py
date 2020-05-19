import bottle, model

vislice = model.Vislice()

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get("/")
def index():
    return bottle.template('views/index.tpl')

@bottle.get('/img/<picture>')
def static_file(picture):
    bottle.static_file(picture, 'img')

@bottle.get("/igra/")
def nova_igra():
    pass

def pokazi_igro(id_igre):
    pass

def ugibaj(id_igre):
    pass


bottle.run(reloader=True, debug=True)