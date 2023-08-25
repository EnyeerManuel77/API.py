from flaskr import create_app
from .modelos import Album, db
from .modelos import db, Cancion, Usuario, Medio
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones/'Canciones')
api.add_resource(VistaCancion,'/canciones/<int:id_cancion>')

with app.app_context():
    Album_Schema = AlbumSchema()
    a = Album(titulo='Prueba', ano=1999, descripcion='texto', medio=Medio.CD)
    db.session.add(a)
    db.session.commit()
    print([Album_Schema.dumps(Album) for Album in Album.query.all()])
