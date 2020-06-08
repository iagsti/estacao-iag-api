import unittest
import json
from datetime import datetime
from estacao.app import minimal_app
from estacao.ext import database
from estacao.ext import commands
from estacao.blueprints import restapi
from estacao.models import Consolidado


class ConsolidadoGetTest(unittest.TestCase):
    def setUp(self):
        app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
        app.app_context().push()
        database.init_app(app)
        restapi.init_app(app)
        commands.create_db()
        consolidado = self.make_consolidado()
        consolidado.save()
        self.resp = app.test_client().get('/api/v0/consolidado')

    def tearDown(self):
        commands.drop_db()

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_response_data(self):
        data = json.loads(self.resp.data)
        self.assertEqual(34, data['consolidado'][0]['vis'])

    def make_consolidado(self):
        data = self.make_data()
        return Consolidado(**data)

    def make_data(self):
        default = dict(data=datetime.now(), vis=34, tipob='tipob',
                       qtdb=34, tipom='tipom', tipoa='tipoa',
                       qtda=34, dir='Sd', vento=34, tempbar=34,
                       pressao=34, tseco=34, tumido=34, tsfc=34,
                       t5cm=34, t10cm=34, t20cm=23, t30cm=34,
                       t40cm=34, piche=34, evap_piche=34, piche_ar=34,
                       evap_piche_ar=34, tmin=34, tmax=34)
        return dict(default)
