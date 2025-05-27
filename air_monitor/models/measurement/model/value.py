from datetime import datetime, date, time


class DateFormat(Exception):
    def __init__(self, date_value):
        super().__init__(f'Incorrect date format: {date_value}')


class Value:
    """
    Klasa reprezentuje pojedynczy pomiar wykonany przez czujnik.
    """

    def __init__(self, date_value, code, value):
        if date_value is not None:
            try:
                self.__date_value = datetime.strptime(date_value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise DateFormat(date_value)
        else:
            self.__date_value = None
        self.__code = code
        try:
            self.__value = float(value) if value is not None else None
        except (ValueError, TypeError):
            self.__value = None

    @property
    def date(self):
        return self.__date_value.date()

    @property
    def time(self):
        return self.__date_value.time()

    @property
    def code(self):
        return self.__code

    @property
    def value(self):
        return self.__value

    def __str__(self):
        date_value_str = self.__date_value.strftime('%Y-%m-%d %H:%M:%S') if self.__date_value else 'None'
        return f'Date: {date_value_str}, Value: {self.__value}, Position Code: {self.__code}'

    def __repr__(self):
        date_value_str = self.__date_value.strftime('%Y-%m-%d %H:%M:%S') if self.__date_value else 'None'
        return (f"Value ('{date_value_str}', "
                f" {self.__value}, '{self.code}')")
