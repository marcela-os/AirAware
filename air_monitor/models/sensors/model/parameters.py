class Param:
    """
    Klasa reprezentuje parametr pomiarowy z nazwą, wzorem, kodem i identyfikatorem.
    """

    def __init__(self, name, formula, code, param_id):
        self.__name = name
        self.__formula = formula
        self.__code = code
        self.__param_id = param_id

    @property
    def name(self):
        return self.__name
    @property
    def formula(self):
        return self.__formula
    @property
    def code(self):
        return self.__code
    @property
    def param_id(self):
        return self.__param_id

    def __str__(self):
        return f'Name: {self.name}, Formula: {self.formula}, Code: {self.code}, ID: {self.param_id}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.formula}, {self.code}, {self.param_id})'

    def __eq__(self, other):
        return self.name == other.name and self.formula == other.formula and self.code == other.code and self.param_id == other.param_id

    def __hash__(self):
        return hash((self.name, self.formula, self.code, self.param_id))
