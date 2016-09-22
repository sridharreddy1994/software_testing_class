from bottle import route, run, get

@get('/posts/<id>')
def posts(id):
    return {'id':int(id),'title':'','body':'','userId':1}

run(host="localhost", port=56789)

