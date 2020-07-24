from estacao.models import Consolidado
from sqlalchemy import func
from datetime import datetime
from estacao.ext.database import db


class TemperaturaRepository:
    def __init__(self):
        self.model = Consolidado
        self.session = self.model.query.session

    def get_temperatura_min(self, start_date, end_date):
        self.make_subquery(feature='tmin')
        self.make_select(sql_func='min', feature='tmin')
        self.make_group()
        self.make_date_interval(start_date, end_date)
        self.make_query(feature='tmin')
        return self.query.all()

    def get_temperatura_max(self, start_date, end_date):
        self.make_subquery(feature='tmax')
        self.make_select(sql_func='max', feature='tmax')
        self.make_group()
        self.make_date_interval(start_date, end_date)
        self.make_query(feature='tmax')
        return self.query.all()

    def make_subquery(self, feature):
        data = getattr(self.model, 'data')
        feature_attr = getattr(self.model, feature)
        query = self.session.query(data, feature_attr)
        query_filter = query.filter(feature_attr != -99 and feature_attr != 0)
        self.subquery = query_filter.subquery()

    def make_select(self, sql_func, feature):
        select = getattr(func, sql_func)(self.subquery.columns[feature])
        self.select = select

    def make_group(self):
        self.group = self.subquery.columns['data']

    def make_date_interval(self, start_date, end_date):
        interval = self.subquery.columns['data'].between(start_date, end_date)
        self.date_interval = interval

    def make_query(self, feature):
        data = self.subquery.columns['data']
        select = self.select
        feature = self.subquery.columns[feature]
        query = self.session.query(data, select, feature).group_by(self.group)
        self.query = query.having(self.date_interval)


class CurrentConditionsRepository:
    def __init__(self):
        self.model = Consolidado
        self.session = db.session

    def get_conditions(self):
        self.load_data()
        self.to_dict()
        self.format_date()
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
        for item in range(len(keys) - 1):
            dict_key = keys[item]
            data_dict[dict_key] = self.data[item]
        self.data = data_dict

    def format_date(self):
        date_format = '%Y-%m-%d %H:%M'
        formatted_date = self.data.get('data').strftime(date_format)
        self.data.update(data=formatted_date)
