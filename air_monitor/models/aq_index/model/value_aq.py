from datetime import datetime, date, time


class DateFormat(Exception):
    """
    Klasa zgłasza wyjątek przy niepoprawnym formacie daty
    """

    def __init__(self, date_value):
        super().__init__(f'Incorrect date format: {date_value}')


class ValueAQ:
    """
    Klasa reprezentuje indeks jakości powietrza dla wybranego parametru.
    """

    def __init__(self, name, source_date, calc_date, index_value, cat_name):
        self.__name = name
        if source_date is not None:
            try:
                self.__source_date = datetime.strptime(source_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise DateFormat(source_date)
        else:
            self.__source_date = None
        if calc_date is not None:
            try:
                self.__calc_date = datetime.strptime(calc_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise DateFormat(calc_date)
        else:
            self.__calc_date = None
        try:
            self.__index_value = float(index_value) if index_value is not None else None
        except (ValueError, TypeError):
            raise ValueError(f'Invalid index_value: {index_value}')
        self.__cat_name = cat_name

    @property
    def name(self):
        return self.__name

    @property
    def source_date(self):
        return self.__source_date

    @property
    def calc_date(self):
        return self.__calc_date

    @property
    def index_value(self):
        return self.__index_value

    @property
    def cat_name(self):
        return self.__cat_name

    def __str__(self):
        calc_date_str = self.calc_date.strftime("%Y-%m-%d %H:%M:%S") if self.calc_date else 'None'
        source_date_str = self.source_date.strftime("%Y-%m-%d %H:%M:%S") if self.source_date else 'None'
        return (f'Name: {self.name}, Source Date: {source_date_str}, '
                f'Calc.Date: {calc_date_str}, '
                f'Index Value: {self.index_value}, Cat: {self.cat_name}')

    def __repr__(self):
        calc_date_str = self.calc_date.strftime("%Y-%m-%d %H:%M:%S") if self.calc_date else 'None'
        source_date_str = self.source_date.strftime("%Y-%m-%d %H:%M:%S") if self.source_date else 'None'
        return (f"Value({self.name!r}, '{source_date_str}', "
                f"'{calc_date_str}', {self.index_value}, '{self.cat_name}')")

    def __eq__(self, other):
        return (self.name == other.name and
                self.source_date == other.source_date and
                self.calc_date == other.calc_date and
                self.index_value == other.index_value and
                self.cat_name == other.cat_name)

    def __hash__(self):
        return hash((self.name, self.source_date, self.calc_date, self.index_value, self.cat_name))
