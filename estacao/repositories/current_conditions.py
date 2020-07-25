from sqlalchemy import func
from datetime import datetime

from estacao.ext.database import db
from estacao.models import Consolidado
from estacao.normalize import Normalize

FLOAT_ROUND = 2


class CurrentConditionsRepository:
    def __init__(self):
        self.model = Consolidado
        self.session = db.session

    def get_conditions(self):
        self.load_data()
        self.to_dict()
        self.format_date()
        self.normalize()
        self.map_data()
        self.round_data()
        return self.data

    def load_data(self):
        m = self.model
        current_date = datetime.now().strftime('%Y-%m-%d')
        max_data = func.max(m.data)
        query = self.session.query(max_data, m.vis, m.tipob, m.qtdb, m.tipom,
                                   m.tipoa, m.qtda, m.dir, m.vento, m.temp_bar,
                                   m.pressao, m.tseco, m.tumido, m.tmin, m.tmax
                                   ).filter(m.data.like(current_date+'%'))
        self.data = query.first()

    def to_dict(self):
        keys = ['data', 'vis', 'tipob', 'qtdb', 'tipom',
                'tipoa', 'qtda', 'dir', 'vento', 'temp_bar',
                'pressao', 'tseco', 'tumido', 'tmin', 'tmax']
        data_dict = dict()
        for item in range(len(keys)):
            dict_key = keys[item]
            data_dict[dict_key] = self.data[item]
        self.data = data_dict

    def format_date(self):
        date_format = '%Y-%m-%d %H:%M'
        formatted_date = self.data.get('data').strftime(date_format)
        self.data.update(data=formatted_date)

    def normalize(self):
        norm = Normalize()
        pressao = self.data.get('pressao')
        temp_bar = self.data.get('temp_bar')
        tseco = self.data.get('tseco')
        tumido = self.data.get('tumido')
        p_hpa = norm.trans_p(pressao, temp_bar)
        temp_orvalho = round(norm.td(tseco, tumido, p_hpa), FLOAT_ROUND)
        umidade_relativa = round(norm.rh_tw(tseco, tumido, p_hpa), FLOAT_ROUND)

        self.data['ponto_orvalho'] = temp_orvalho
        self.data['umidade_relativa'] = umidade_relativa

    def map_data(self):
        current_conditions = {
            'data': self.data.get('data'),
            'temperatura_ar': self.data.get('tseco'),
            'temperatura_ponto_orvalho': self.data.get('ponto_orvalho'),
            'umidade_relativa': self.data.get('umidade_relativa'),
            'temperatura_min': self.data.get('tmin'),
            'temperatura_max': self.data.get('tmax'),
            'visibilidade': self.data.get('vis'),
            'vento': self.data.get('vento'),
            'pressao': self.data.get('pressao'),
            'nuvens_baixas': self.data.get('tipob'),
            'nuvens_medias': self.data.get('tipom'),
            'nuvens_altas': self.data.get('tipoa')
        }
        self.data = current_conditions

    def round_data(self):
        for key in self.data.keys():
            if isinstance(self.data.get(key), float):
                self.data[key] = round(self.data.get(key), FLOAT_ROUND)