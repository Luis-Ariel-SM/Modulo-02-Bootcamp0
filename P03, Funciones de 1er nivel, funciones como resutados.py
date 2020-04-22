
#Funcion para calcular el valor maximo de una lista
def v_maximo (*lista):# el asterisco significa que todo lo que entrara en la funcion se convertira en una lista
    if len (lista) == 0:
        return 0
    
    maximo = lista [0]
    for indice in range (1, len(lista)):
        if lista [indice] > maximo:
            maximo = lista [indice]
            
    return maximo

# Funcion para calcular el valor minimo de una lista
def v_minimo (*lista):
    if len (lista) == 0:
        return 0
    
    minimo = lista [0]
    for indice in range (1, len(lista)):
        if lista [indice] < minimo:
            minimo = lista [indice]
            
    return minimo

# Funcion para calcular la media
def v_media (*lista):
    if len (lista) == 0:
        return 0
    
    suma = 0
    for indice in lista:
        suma += indice
        
    return suma / len(lista)
  
print (v_maximo (1,3,-1,15,9))
print (v_minimo (1,3,-1,15,9))
print (v_media  (1,3,-1,15,9))

# Seguimos en la demostracion con un diccionario guardando las funciones antes creadas

funciones = {
    'maxi': v_maximo,
    'mini': v_minimo,
    'medi': v_media
}

def return_funciones (nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():
        return funciones [nombre]
    
    return None
        
print (return_funciones ())
