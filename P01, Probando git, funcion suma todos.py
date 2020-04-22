def suma_todos(limit_to):
    resultado = 0
    for i in range (0, limit_to+1):
        resultado += i
        print (resultado)
        
    return resultado

print (suma_todos(100))