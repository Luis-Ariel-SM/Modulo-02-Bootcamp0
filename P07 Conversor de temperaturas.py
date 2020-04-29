class Termometro():
    def __init__(self):
        self.__unidad_medida = 'C'
        self.__temperatura = 0
    
    def __conversor (self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}º C".format((temperatura - 32) * 9/5)
        else:
            return "Unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.__temperatura, self.__unidad_medida)

    def unidadMedida (self, uniM = None):
        if uniM == None:
            return self.__unidad_medida
        else:
            if uniM == "F" or uniM == "C":
                self.__unidad_medida = uniM
                
    def temp (self, temperatura = None):
        if temperatura == None:
            return self.__temperatura
        else:
            self.__temperatura = temperatura
            
    def mide (self, uniM = None):
        if uniM == None or uniM == self.__unidad_medida:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidad_medida)
        