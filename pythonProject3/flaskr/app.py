from flaskr import create_app
from .modelos import Cancion, db
from .modelos import Album, db
from .modelos import Usuario, db
from .modelos import Medio, db

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    u = Usuario(nombre='Juan', contrasena='12345')
    c = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete='Ozuna')
    a = Album(titulo='prueba', ano=1999, descripcion='texto', medio=Medio.CD)
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())
