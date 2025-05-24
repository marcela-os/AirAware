from datetime import datetime, date, time

class DateFormat(Exception):
    def __init__(self,  date_value):
        super().__init__(f'Incorrect date format: {date_value}')

class Value:
    def __init__(self, date_value, value):
        try:
            self.__datetime = datetime.strptime(date_value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise DateFormat(date_value)
        self.__value = float(value) if value is not None else None

    @property
    def date(self):
        return self.__datetime.date()

    @property
    def time(self):
        return self.__datetime.time()

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f'Date: {self.__datetime}, Value: {self.__value}'

    def __repr__(self):
        return f"Value(date='{self.__datetime.strftime('%Y-%m-%d %H:%M:%S')}', value={self.__value})"
