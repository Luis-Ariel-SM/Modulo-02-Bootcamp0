import turtle
# Ejecutando help(turtle) en la consola se pueden ver todas las funciones de esta libreria

tortuga = turtle.Turtle() # la variable tortuga es una instancia de clase turtle.(La clase es el bloque de codigo que define las caracteristicas de esta clase)
tortuga.forward(50) # A las variables/instancias de los objetos no se accede directamente. Estas van acompañadas por un metodo o atributo
                    #(funcion que realiza un objeto de clase Turtle, en este caso es .forward, el parametro es lo que va dentro del parentesis.

                
# Creando nuestro 1er objeto:
class Perro (): # Asi se define la clase por convenio, el nombre de la clase (Perro) siempre inicia en mayusculas como los nombre propios
    def __init__(self, nombre, edad, peso): # Esta funcion va siempre, es la funcion constructora donde se definen las variables de estado. El 1er parametro de los metodos de una clase siempre es la propia instancia, por convenio se pone (self)
        self.nombre = nombre # atributo nombre de la misma clase (Perro) sera el que se ha informado en la 1era posicion. Funciona bajo la logica de los parametros de entrada
        self.edad = edad
        self.peso = peso
    
    def ladrar (self):
        if self.peso >= 8:
            print("Guau, Guau")
        else:
            print("guau, guau")
            
    def __str__(self):
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso) # Metodo especifico que nos devuelve una cadena cuando hacemos un print de una funcion.



