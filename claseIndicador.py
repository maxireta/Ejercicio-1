class indicador:
    def __init__(self, cant, base, act):
        self.__cant = cant
        self.__base = base
        self.__act = act
    def calcular(self):
        IPC = (self.calcular1(self.__act) / self.calcular1(self.__base))
        sine = round(((IPC % 1) * 100), 2)
        return sine
    def calcular1(self, anio):
        valor = self.__cant * anio
        return valor