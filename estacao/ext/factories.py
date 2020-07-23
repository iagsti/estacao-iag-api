from estacao.ext import fakers


def consolidado_factory(length, start_date=None, end_date=None):
    data = list()
    for _ in range(length):
        data.append(fakers.fake.consolidado(start_date, end_date))
    return data


def current_conditions_factory(length):
    return [fakers.fake.current_conditions() for _ in range(length)]
