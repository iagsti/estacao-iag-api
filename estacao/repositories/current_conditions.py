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
        self.load_temperature('min', 'tmin')
        self.load_temperature('max', 'tmax')
        self.to_dict()
        self.format_date()
        self.normalize()
        self.map_data()
        self.round_data()
        return self.data

    def load_temperature(self, db_func, col):
        m = self.model
        attribute = getattr(m, col)
        dates = self.make_dates()
        between = m.data.between(dates.get('cur_date_ini'),
                                 dates.get('cur_date_end'))

        temperature = getattr(func, db_func)(attribute)

        subquery = self.session.query(
            temperature
        ).filter(
            between
        ).filter(attribute != 0).subquery()

        query = self.session.query(
            m.data, getattr(m, col)
        ).filter(attribute == subquery).filter(between)

        setattr(self, col, query.first())

    def load_data(self):
        m = self.model
        query = self.session.query(
            m.data, m.vis, m.tipob, m.qtdb, m.tipom,
            m.tipoa, m.qtda, m.dir, m.vento, m.temp_bar,
            m.pressao, m.tseco, m.tumido
        ).order_by(m.data.desc())
        self.data = query.first()

    def to_dict(self):
        keys = ['data', 'vis', 'tipob', 'qtdb', 'tipom',
                'tipoa', 'qtda', 'dir', 'vento', 'temp_bar',
                'pressao', 'tseco', 'tumido']
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
        self.data['pressao'] = p_hpa

    def map_data(self):
        current_conditions = {
            'data': self.data.get('data'),
            'temperatura_ar': self.data.get('tseco'),
            'temperatura_ponto_orvalho': self.data.get('ponto_orvalho'),
            'umidade_relativa': self.data.get('umidade_relativa'),
            'temperatura_min': self.tmin[1],
            'temperatura_min_date': self.tmin[0].strftime('%Y-%m-%d %H:%M'),
            'temperatura_max': self.tmax[1],
            'temperatura_max_date': self.tmax[0].strftime('%Y-%m-%d %H:%M'),
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

    def make_dates(self):
        time_ini = '00:00:00'
        time_end = '23:59:59'
        cur_date = datetime.now().strftime('%Y-%m-%d')
        cur_date_ini = cur_date + ' ' + time_ini
        cur_date_end = cur_date + ' ' + time_end

        return {'cur_date': cur_date,
                'cur_date_ini': cur_date_ini,
                'cur_date_end': cur_date_end}
