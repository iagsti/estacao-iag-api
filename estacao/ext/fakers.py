from faker import Faker
from faker.providers import BaseProvider
from estacao.models import Consolidado
from datetime import datetime


fake = Faker()


class ConsolidadoProvider(BaseProvider):
    def consolidado(self, ):
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
                tempbar=fake.random_element(elements=(12, 50)),
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
                tmax=fake.random_element(elements=(12, 50)),
            )

        return obj


providers = (
    ConsolidadoProvider,
)


for provider in providers:
    fake.add_provider(provider)
