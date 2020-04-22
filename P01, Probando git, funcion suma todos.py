def suma_todos(limit_to):
    resultado = 0
    for i in range (0, limit_to+1):
        resultado += i
                
    return resultado


def suma_todos_cuadrados (limit_to):
    result = 0
    for i in range (limit_to+1):
        result+=i*i
        
    return result

print (suma_todos(100))
print (suma_todos_cuadrados(3))
