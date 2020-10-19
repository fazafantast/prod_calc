import csv
import re
import datetime

from .exceptions import ProdCalcException


class ProdCalc:
    __data = None

    def __init__(self):
        _months = list(range(1, 13))
        try:
            # Данные хранящиеся в `prod_calc.csv`, взяты с сайта открытых данных России:
            # https://data.gov.ru/opendata/7708660670-proizvcalendar
            with open('./prodcalc/data/prod_calc.csv', newline='') as f:
                fieldnames = ['year'] + _months
                reader = csv.DictReader(f, delimiter=',', quotechar='"', fieldnames=fieldnames)
                self.__data = {}
                for row in reader:
                    year = int(row['year'])
                    self.__data[year] = {}
                    for month in _months:
                        self.__data[year][month] = []
                        days = row[month].split(',')
                        for day in days:
                            _day = int(re.sub('\D', '', day))
                            self.__data[year][month].append(_day)
                    # print(type(row), row['year'], row)
            print(self.__data)
        except OSError:
            raise Exception('Библиотека повреждена, отсутствуют инициализационные данные')

    def _check_date(self, date) -> datetime.date:
        if isinstance(date, datetime.datetime):
            return date.date()
        elif isinstance(date, datetime.date):
            return date
        raise ProdCalcException('Дата неожиданного типа.')

    def is_working_day(self, date=None) -> bool:
        if date is None:
            date = datetime.date.today()
        date = self._check_date(date)
        if self.__data.get(date.year) and self.__data[date.year].get(date.month):
            return date.day not in self.__data[date.year][date.month]
        raise ProdCalcException('Дата вне диапазона календаря')

    def previous_working_day(self, date=None) -> datetime.date:
        if date is None:
            date = datetime.date.today()
        date = self._check_date(date)
        while True:
            date = date - datetime.timedelta(days=1)
            if self.is_working_day(date):
                return date

