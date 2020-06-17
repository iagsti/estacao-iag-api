from estacao.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Consolidado(db.Model, SerializerMixin):
    data = db.Column(db.DateTime, primary_key=True)
    vis = db.Column(db.Integer)
    tipob = db.Column(db.String)
    qtdb = db.Column(db.Integer)
    tipom = db.Column(db.String)
    tipoa = db.Column(db.String)
    qtda = db.Column(db.Integer)
    dir = db.Column(db.String)
    vento = db.Column(db.Float)
    tempbar = db.Column(db.Float)
    pressao = db.Column(db.Float)
    tseco = db.Column(db.Float)
    tumido = db.Column(db.Float)
    tsfc = db.Column(db.Float)
    t5cm = db.Column(db.Float)
    t10cm = db.Column(db.Float)
    t20cm = db.Column(db.Float)
    t30cm = db.Column(db.Float)
    t40cm = db.Column(db.Float)
    piche = db.Column(db.Float)
    evap_piche = db.Column(db.Float)
    piche_ar = db.Column(db.Float)
    evap_piche_ar = db.Column(db.Float)
    tmin = db.Column(db.Float)
    tmax = db.Column(db.Float)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Pressao(db.Model, SerializerMixin):
    data = db.Column(db.DateTime, primary_key=True)
    pressao = db.Column(db.Float)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Users(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20))
    password = db.Column(db.String(128))

    def save(self):
        db.session.add(self)
        db.session.commit()


class Umidade(db.Model, SerializerMixin):
    data = db.Column(db.DateTime, primary_key=True)
    ur = db.Column(db.Float)

    def save(self):
        db.session.add(self)
        db.session.commit()
