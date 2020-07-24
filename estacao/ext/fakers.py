from faker import Faker
from faker.providers import BaseProvider
from estacao.models import Consolidado
from datetime import datetime


fake = Faker()


class ConsolidadoProvider(BaseProvider):
    def consolidado(self, start_date=None, end_date=None):
        if not (start_date and end_date):
            start_date = datetime(2018, 1, 1, 13, 48, 10)
            end_date = datetime(2018, 1, 1, 13, 48, 10)
        obj = Consolidado(
            data=fake.date_time_between_dates(start_date, end_date),
            vis=34,
            tipob='tipob',
            qtdb=fake.random_element(elements=(12, 50)),
            tipom='tipom',
            tipoa='tipoa',
            qtda=fake.random_element(elements=(12, 50)),
            dir=fake.random_element(elements=('Su', 'No', 'Le', 'O')),
            vento=fake.random_element(elements=(12, 50)),
            temp_bar=fake.random_element(elements=(12, 50)),
            pressao=fake.random_element(elements=(12, 50)),
            tseco=fake.random_element(elements=(12, 50)),
            tumido=fake.random_element(elements=(12, 50)),
            tsfc=fake.random_element(elements=(12, 50)),
            t5cm=fake.random_element(elements=(12, 50)),
            t10cm=fake.random_element(elements=(12, 50)),
            t20cm=23,
            t30cm=fake.random_element(elements=(12, 50)),
            t40cm=fake.random_element(elements=(12, 50)),
            piche=fake.random_element(elements=(12, 50)),
            evap_piche=fake.random_element(elements=(12, 50)),
            piche_ar=fake.random_element(elements=(12, 50)),
            evap_piche_ar=fake.random_element(elements=(12, 50)),
            tmin=fake.random_element(elements=(12, 50)),
            tmax=fake.random_element(elements=(12, 50)))
        return obj


class CurrentConditionsProvider(BaseProvider):
    def current_conditions(self):
        data = datetime.now()
        return dict(data=data, temperatura_ar=20.0,
                    temperatura_ponto_orvalho=19,
                    umidade_relativa=90, temperatura_min=18,
                    temperatura_max=23, visibilidade=10,
                    vento=30, pressao=160, nuvens_baixas='Cum/20',
                    nuvens_medias='Nim/20', nuvens_altas='Cir/30')


providers = (
    ConsolidadoProvider,
    CurrentConditionsProvider,
)


for provider in providers:
    fake.add_provider(provider)
