# La recursividad es un paradigma de programacion basado en funciones solo se necesitan a asi mismas y se invocan a si mismas. Su mayor
# problema es que puede ejecutar bucles infinitos ya que no para de llamarse por lo cual su punto mas importante es la condicion de
# parada. Es un codigo original y elegante a nivel de sintaxis pero muy poco eficiente lastrando asi su utilidad.

# 1er ejemplo:
def retrocontador (entrada):
     print ("{},".format(entrada), end = "")
     
   # if entrada == 0: Esta seria otra sintaxis para ejecutar la salida del bucle. Cuando tu valor sea 0...
   #     return      ... te paras aqui

     if entrada > 0: # condicion de salida, si el numero es mayor que 0...
         retrocontador (entrada - 1) # ... vuelve a ejecutarte restandote el valor. Cuando llegue a 0 parará de ejecutarse
        
retrocontador (10)