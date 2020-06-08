from estacao.ext.database import db
from estacao.models import Consolidado
from datetime import date


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Drops database"""
    db.drop_all()


def populate_db():
    consolidado = Consolidado(data=date.fromisoformat('2020-02-01'),
                              vis=34, tipob='tipob',
                              qtdb=34, tipom='tipom', tipoa='tipoa',
                              qtda=34, dir='Sd', vento=34, tempbar=34,
                              pressao=34, tseco=34, tumido=34, tsfc=34,
                              t5cm=34, t10cm=34, t20cm=23, t30cm=34,
                              t40cm=34, piche=34, evap_piche=34, piche_ar=34,
                              evap_piche_ar=34, tmin=34, tmax=34)
    consolidado.save()
    return Consolidado.query.all()


def init_app(app):
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))
