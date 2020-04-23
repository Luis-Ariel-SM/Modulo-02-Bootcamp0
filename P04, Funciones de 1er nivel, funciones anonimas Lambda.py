from P02Modulo_to_import import suma_todos # cuando importes modulos el nombre o puede tener espacios
from functools import reduce # hay que importar reduce para poderlo utilizar

# Ejemplo de funciones lambdas, funciones pequeñas y anonimas que generalmente se utilizaran una vez en un momento dado, su construccion
# es sencilla y no retornan nada ya que adquieren automaticamente el valor de lo que se ejecute dentro de ellas 

print(suma_todos(3, lambda x: x**3))

doble = lambda x: x*2
triple = lambda x: x*3

print(suma_todos(3, doble))
print(suma_todos(100,triple))


# Operador map

# Este operador trabaja sobre todos los elementos de una lista

lista = [1, 3, -1, 15, 9]
lista_dobles = map(lambda x:x*2,lista)# Traduccion: Coge cada uno de los valores de una lista, aplicales la siguiente funcion
# (multiplicara cada uno de esos valores por 2 en este ejemplo) y al final se pone el nombre de la lista en cuestion sobre la sacara
# los valores
print (list(lista_dobles))

# Operador filter

# Filtra los valores de la lista que cumplan una condicion definida, igual trabajara uno a uno sobre todos los valores de la lista y
# devolvera solo el que cumpla la condicion pedida

lista = [1, 2, -1, 15, 9]

def es_par(x): # La funcion siempre tiene que devolver True o False, para todos los valores de x = True, devolvera x (en este caso,
    return x % 2 == 0  # el unico valor de la lista que da True y cumple el parametro es el 2 
    

lista_dobles = filter(lambda x: x % 2 == 0, lista)# Traduccion del ejemplo: Filtra y devuelveme los valores cuyo resto entre 2 sea igual a 0
lista_dobles_clasicc = filter(es_par, lista)# Mismo ejemplo con una funcion clasica. Se llama a la funcion dentro del filter y detras
                                            # de la coma se nombra a las lista sobre la que utlizara los datos para trabajar
print (list(lista_dobles))
print (list(lista_dobles_clasicc))

# Operador reduce

# Igual trabajara uno a uno sobre todos los valores de la lista convirtiendolos al final en un unico valor. El reduce hay que importarlo
# desde la libreria functools, este operador problemas provocando errores matematicos en los resultados esperados

lista = [1, 2, -1, 15, 9]

sumatorio = reduce(lambda x, y: x + y, lista) # En este lambda el 1er parametro ('x') funciona como variable acumuladora. 0+1=1; 1+2=3; 3-1=2; 2+15=17; 17+9=26
print (sumatorio)                             # EL segundo parametro ('y') indica el valor individual a sumar

suma100 = reduce(lambda x, y: x + y, range(0,101)) # Se le puede meter un rango para que trabaje sobre el. Un range es una lista igual
print (suma100)

copia_lista = lista [:] # Asi es como se crean las copias de las listas, lo que hagas en esta copia no funciona en la lista original
copia_lista.insert(0,0) # Agregando los valores neutros para la suma  en la posicion 0 de la funcion lambda. Esto se hace porque el
                        # reduce tiene problemas y en las iteraciones utiliza lo 2 primeros indices generando errores matematicos, por
                        # eso se le ajusta el indice para que empieze por 0
                   
suma_dobles = reduce(lambda x, y: x + y*2, copia_lista)
print (suma_dobles)