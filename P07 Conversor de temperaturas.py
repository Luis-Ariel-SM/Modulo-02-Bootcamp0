class Termometro():
    def __init__(self):
        self.unidad_medida = 'C'
        self.temperatura = 0
    
    def conversor (self, temperatura, unidad):
        if unidad == 'C':
            return "{}º F".format(temperatura * 9/5 + 32)
        elif unidad == 'F':
            return "{}º C".format((temperatura - 32) * 9/5)
        else:
            return "Unidad incorrecta"
    
    def __str__(self):
        return "{}º {}".format(self.temperatura, self.unidad_medida)

c = Termometro()
print(c.conversor(0,"C"))
print(c.conversor(0,"F"))