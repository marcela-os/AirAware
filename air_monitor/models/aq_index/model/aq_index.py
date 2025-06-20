from datetime import datetime, date, time


class DateFormat(Exception):
    """
    Klasa zgłasza wyjątek przy niepoprawnym formacie daty
    """

    def __init__(self, date_value):
        super().__init__(f'Incorrect date format: {date_value}')


class AqIndex:
    """
    Klasa reprezentuje indeks jakości powietrza dla stacji pomiarowej.
    """

    def __init__(self, station_id, value_index, name, calc_date, source_data_date, critical_pollution_code, param):
        self.__station_id = station_id
        self.__value_index = float(value_index) if value_index is not None else None
        self.__name = name
        if calc_date is not None:
            try:
                self.__calc_date = datetime.strptime(calc_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise DateFormat(calc_date)
        else:
            self.__calc_date = None
        if source_data_date is not None:
            try:
                self.__source_data_date = datetime.strptime(source_data_date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise DateFormat(source_data_date)
        else:
            self.__source_data_date = None
        self.__critical_pollution_code = critical_pollution_code
        self.__param = param

    @property
    def station_id(self):
        return self.__station_id

    @property
    def value_index(self):
        return self.__value_index

    @property
    def name(self):
        return self.__name

    @property
    def calc_date(self):
        return self.__calc_date

    @property
    def source_data_date(self):
        return self.__source_data_date

    @property
    def critical_pollution_code(self):
        return self.__critical_pollution_code

    @property
    def param(self):
        return self.__param

    def __str__(self):
        calc_date_str = self.calc_date.strftime("%Y-%m-%d %H:%M:%S") if self.calc_date else 'None'
        source_date_str = self.source_data_date.strftime("%Y-%m-%d %H:%M:%S") if self.source_data_date else 'None'
        return (f'Station ID: {self.station_id}, Value Index: {self.value_index}, '
                f'Cat.Name: {self.name}, Calc.Date: {calc_date_str}, '
                f'Source Date: {source_date_str}, '
                f'CP Code: {self.critical_pollution_code}, Param: {self.param}')

    def __repr__(self):
        calc_date_str = self.calc_date.strftime("%Y-%m-%d %H:%M:%S") if self.calc_date else 'None'
        source_date_str = self.source_data_date.strftime("%Y-%m-%d %H:%M:%S") if self.source_data_date else 'None'
        return (f'{self.__class__.__name__}({self.station_id}, {self.value_index}, {self.name!r}, '
                f'{calc_date_str}, '
                f'{source_date_str}, '
                f'{self.critical_pollution_code!r}, {self.param!r})')

    def __eq__(self, other):
        return (self.station_id == other.station_id and
                self.value_index == other.value_index and
                self.name == other.name and
                self.calc_date == other.calc_date and
                self.source_data_date == other.source_data_date and
                self.critical_pollution_code == other.critical_pollution_code and
                self.param == other.param)

    def __hash__(self):
        return hash((self.station_id, self.value_index, self.name,
                     self.calc_date, self.source_data_date, self.critical_pollution_code, self.param))
