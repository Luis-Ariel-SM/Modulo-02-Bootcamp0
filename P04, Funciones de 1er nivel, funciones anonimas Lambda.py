from P02Modulo_to_import import suma_todos # cuando importes modulos el nombre o puede tener espacios

print(suma_todos(3, lambda x: x**3))

doble = lambda x: x*2
triple = lambda x: x*3

print(suma_todos(3, doble))
print(suma_todos(100,triple))


