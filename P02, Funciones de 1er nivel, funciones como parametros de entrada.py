# Las funciones de 1er nivel es una propiedad de Python que admite funciones como parametros de entrada de otras funciones

def normal (x): # Paso 3, con la invocacion y el parametro de entrada dada en el paso 2.3 se ejecuta aqui el bloque de codigo devolviendo
    return x    # el resultado que volvera a la invocacion agregandose a la variable "result"

def cuadrado (x):
    return x * x

def cubo (x):
    return x**3


def suma_todos (limit_to, normal): # Paso 2
    result = 0
    for i in range (limit_to+1): # 2.1 Aqui se activa el 1er parametro de entrada que es 100
        result += normal(i) #2.3 Aqui se activa el 2do parametro de entrada que es la invocacion a la funcion "normal" dandole como
        # parametro de entrada a esta invocacion el valor que adquiera la variable i de la iteracion for
        
    return result

print (suma_todos(100, normal)) #Paso 1- Se invoca a la funcion suma_todos, El 2do parametro de entrada es la otra funcion nombrada "normal"
print (suma_todos(3, cuadrado))
print (suma_todos(3, cubo))
