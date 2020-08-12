from estacao.models import Consolidado
from estacao.normalize import Normalize


class ConsolidadoRepository:
    def __init__(self, date_ini, date_end):
        self.model = Consolidado
        self.date_ini = date_ini + ' 00:00:00'
        self.date_end = date_end + ' 23:59:59'

    def all(self):
        self.make_query()
        self.set_data()
        self.to_dict()
        self.set_date()
        return self.data

    def make_query(self):
        model = self.model
        between = model.data.between(self.date_ini, self.date_end)
        query = model.query.with_entities(
            model.data, model.vis, model.tipob, model.qtdb,
            model.tipom, model.qtdm, model.tipoa, model.qtda,
            model.dir, model.vento, model.temp_bar, model.pressao,
            model.tseco, model.tumido, model.tsfc, model.t5cm,
            model.t10cm, model.t20cm, model.t30cm, model.t40cm,
            model.piche, model.evap_piche, model.evap_piche_ar,
            model.piche_ar, model.tmin, model.tmax
        ).filter(between)
        setattr(self, 'query', query)

    def set_data(self):
        data = self.query.all()
        setattr(self, 'data', data)

    def to_dict(self):
        data = self.data
        data_list = list()
        for row in data:
            dict_data = self.set_dict(row)
            data_list.append(dict_data)
        setattr(self, 'data', data_list)

    def set_dict(self, data):
        keys = ('data', 'vis', 'tipob', 'qtdb', 'tipom', 'qtdm',
                'tipoa', 'qtda', 'dir', 'vento', 'temp_bar',
                'pressao', 'tseco', 'tumido', 'tsfc', 't5cm',
                't10cm', 't20cm', 't30cm', 't40cm', 'piche',
                'evap_piche', 'piche_ar', 'evap_piche_ar',
                'tmin', 'tmax')
        data_dict = dict()
        for item in range(len(keys)):
            dict_key = keys[item]
            data_dict[dict_key] = data[item]
        return data_dict

    def set_pressao_hpa(self):
        data = getattr(self, 'data')
        normalize = Normalize()
        for item in data:
            pressao = item.get('pressao')
            temp_bar = item.get('temp_bar')
            pressao_hpa = normalize.trans_p(pressao, temp_bar)
            item['pressao_hpa'] = pressao_hpa

    def set_date(self):
        for row in self.data:
            date = row.get('data')
            row.update(data=date.strftime('%Y-%m-%d %H:%M'))
