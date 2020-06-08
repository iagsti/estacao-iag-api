import unittest
from datetime import datetime
from estacao.app import minimal_app
from estacao.ext import database
from estacao.ext import commands
from estacao.models import Consolidado


class ConsolidadoTest(unittest.TestCase):
    def setUp(self):
        print('consolidado init')
        app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
        app.app_context().push()
        database.init_app(app)
        commands.create_db()
        self.obj = self.make_consolidado()

    def tearDown(self):
        print('consolidado end')
        commands.drop_db()

    def test_instance(self):
        """It should be an instance of Consolidado"""
        self.assertIsInstance(self.obj, Consolidado)

    def test_has_save_attribute(self):
        """Consolidado should have save attribute"""
        self.assertTrue(hasattr(self.obj, 'save'))

    def test_save_data(self):
        """Data should be saved"""
        self.obj.save()
        self.assertTrue(self.obj.query.count() > 0)

    def make_consolidado(self):
        return Consolidado(data=datetime.now(), vis=34, tipob='tipob',
                           qtdb=34, tipom='tipom', tipoa='tipoa',
                           qtda=34, dir='Sd', vento=34, tempbar=34,
                           pressao=34, tseco=34, tumido=34, tsfc=34,
                           t5cm=34, t10cm=34, t20cm=23, t30cm=34,
                           t40cm=34, piche=34, evap_piche=34, piche_ar=34,
                           evap_piche_ar=34, tmin=34, tmax=34)
