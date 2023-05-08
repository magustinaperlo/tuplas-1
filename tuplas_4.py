"""""
Crea una tupla con valores ya predefinidos del 1 al 10, pide al usuario un índice por teclado y muestra los valores de la tupla.
RESUELVE el caso en que no exista ese índice en la tupla.
"""
tupla_numeros = ()
indece = 0

tupla_numeros = (1,2,3,4,5,6,7,8,9,10)
 
indice = int(input("Ingrese un indice: "))
 
if indice >= 0 and indice < len(tupla_numeros):
    print(tupla_numeros[indice]) #si el usuario ingresa 5 se imprime la posicion 5 que en la tupla es el numero 6
else:
    print("Indice no valido")