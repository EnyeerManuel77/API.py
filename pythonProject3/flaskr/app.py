from flaskr import create_app
from .modelos import Album, db
from .modelos import db, Cancion, Usuario, Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    Album_Schema = AlbumSchema()
    A = Album(titulo='Prueba', ano=1999, descripcion='texto', medio=Medio.CD)
    db.session.add(A)
    db.session.commit()
    print([Album_Schema.dumps(Album) for Album in Album.query.all()])
