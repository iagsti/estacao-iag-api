from estacao.ext import fakers


def consolidado_factory(length):
    data = list()
    for _ in range(length):
        data.append(fakers.fake.consolidado())
    return data
