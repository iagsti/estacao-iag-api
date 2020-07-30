from faker import Faker
from faker.providers import BaseProvider
from estacao.models import Consolidado
from datetime import datetime


fake = Faker()


class ConsolidadoProvider(BaseProvider):
    def consolidado(self, start_date=None, end_date=None, randomic=True):
        float_elements = fake.random_element(elements=(12, 50))
        dir_element = fake.random_element(elements=('Su', 'No', 'Le', 'O'))
        if not randomic:
            float_elements = 20.0
            dir_element = 'Su'
        if not (start_date and end_date):
            start_date = datetime(2018, 1, 1, 13, 48, 10)
            end_date = datetime(2018, 1, 1, 13, 48, 10)
        obj = Consolidado(
            data=fake.date_time_between_dates(start_date, end_date),
            vis=9, tipob='tipob', qtdb=float_elements, tipom='tipom',
            qtdm='qtdm', tipoa='tipoa', qtda=float_elements, dir=dir_element,
            vento=float_elements, temp_bar=float_elements,
            pressao=float_elements, tseco=float_elements,
            tumido=float_elements, tsfc=float_elements,
            t5cm=float_elements, t10cm=float_elements, t20cm=23,
            t30cm=float_elements, t40cm=float_elements, piche=float_elements,
            evap_piche=float_elements, piche_ar=float_elements,
            evap_piche_ar=float_elements, tmin=float_elements,
            tmax=float_elements)
        return obj


class CurrentConditionsProvider(BaseProvider):
    def current_conditions(self, **kwargs):
        now = datetime.now()
        default = dict(data=str(now.date()), temperatura_ar=20.0,
                       temperatura_ponto_orvalho=19,
                       umidade_relativa=90, temperatura_min=18,
                       temperatura_max=23, visibilidade=10,
                       vento=30, pressao=160, nuvens_baixas='Cum/20',
                       nuvens_medias='Nim/20', nuvens_altas='Cir/30')
        data = dict(default, **kwargs)
        return data


providers = (
    ConsolidadoProvider,
    CurrentConditionsProvider,
)


for provider in providers:
    fake.add_provider(provider)
