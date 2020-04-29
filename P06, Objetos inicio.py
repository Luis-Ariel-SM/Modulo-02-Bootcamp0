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

# Herencias y subclases:

class Perro_asistencia(Perro): # Subclase de la clase Perro.
    def __init__ (self, nombre, edad, peso, amo): # Se define la funcion constructora tipica de esta subclase
        Perro.__init__(self, nombre, edad, peso)  # Se copia instacia de la clase "padre" para poder ejecutar su funcionalidad
        self.amo = amo
        self.trabajando = False
        
    def __str__(self):
        return "Perro de asistencia de {}".format(self.amo) # Aunque tambien herede esta funcion de la clase "padre" habria que mo
                                                            # dificarla para ajustar el print a la informacion propia de esta, a esto
                                                            # se le llama: sobreescribir un metodo)
    def pasear (self):
        print ("{} ayudo a mi dueño, {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self): # Sobreescribiendo la funcion ladrar
        if self.trabajando:
            print("Shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self) # Aqui se ha invocado al metodo "padre" para respetar el resultado incial de la misma de tener en cuenta
                               # el ladrido segun el peso. Se hubiera podido poner un print pero se perderia este detalle
   
# Otro ejemplo a tener en cuenta

class Dog():
    def __init__ (self): # Se puede crear una clase vacia, no es obligatorio definir los atributos de manera privada a la clase inicialmente
        self.nombre = "" # Aqui si que se tiene que definir los atributos aunque la clase este vacia para que estos existan y luego se les
        self.edad = None # Va difiniendo el valor
        self.peso = None
   
