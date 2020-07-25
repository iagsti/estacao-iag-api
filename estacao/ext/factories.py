from estacao.ext import fakers


def consolidado_factory(length, start_date=None, end_date=None, randomic=True):
    data = list()
    for _ in range(length):
        data.append(fakers.fake.consolidado(start_date, end_date, randomic))
    return data


def current_conditions_factory(length, **kwargs):
    return [fakers.fake.current_conditions(**kwargs) for _ in range(length)]
