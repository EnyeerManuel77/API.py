from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
import enum


db = SQLAlchemy()


class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(128))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(128))
    albumes = db.relationship('Album', secondary='album_cancion', back_populates='canciones')

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.minutos, self.segundos, self.interprete)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    contrasena = db.Column(db.Integer)
    albumes = db.relationship('Album', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return "{}-{}".format(self.nombre, self.contrasena)

albumes_canciones = db.Table('album_cancion', \
    db.Column('album_id', db.Integer, db.ForeignKey('album.id'), primary_key=True),
    db.Column('cancion_id', db.Integer, db.ForeignKey('cancion.id'), primary_key=True)
)

class Medio(enum.Enum):
    DISCO = 1
    CASETE = 2
    CD = 3
class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(130))
    ano = db.Column(db.Integer)
    descripcion = db.Column(db.String(130))
    medio = db.Column(db.Enum(Medio))
    usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    canciones = db.relationship('Cancion', secondary='album_cancion', back_populates='albumes')
    __table_args__=(db.UniqueConstraint('usuario', 'titulo', name='titulo_unico_album'),)


    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo, self.ano, self.descripcion, self.medio)

class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr,  obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}

class AlbumSchema(SQLAlchemyAutoSchema):
    medio = EnumADiccionario(attribute=('medio'))
    class Meta:
        model = Album
        inclide_relationships = True
        load_instance = True

class CancioneSchema(SQLAlchemyAutoSchema):
    def _serialize(self, value, attr,  obj, **kwargs):
        if value is None:
            return None
        return {'llave':value.name, 'valor':value.value}