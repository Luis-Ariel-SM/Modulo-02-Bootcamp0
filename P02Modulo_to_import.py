def normal (x):
    return x    

def cuadrado (x):
    return x * x

def cubo (x):
    return x**3


def suma_todos (limit_to, normal):
    result = 0
    for i in range (limit_to+1):
        result += normal(i)
        
    return result

if __name__ == '__main__': # se evita que se ejecuten estos bloques de codigo en el lugar donde se hallan importado, significa que los
    # ficheros con nombre main son ejecutados directamente desde la consola como codigos principales, cuando se importan cambian de nombre
    # y se ejecutan como codigo importado. Aqui se le dice que solo se activen si son ejecutados desde la consola como principales.Por
    # ejemplo, estos scripts aqui serian codigo principal pero importado en otro sitio, el principal o main seria el original del otro
    # sitio y el de este fichero solo seria un modulo agregado ejecutandose ademas todo su codigo, lo cual puede ser incomodo. Es por
    # eso que mediante esta via se evita y solo se le dice que se ejecute en su __main__...probar print(__main__) en consola
    
    print (suma_todos(100, normal)) 
    print (suma_todos(3, cuadrado))
    print (suma_todos(3, cubo))

