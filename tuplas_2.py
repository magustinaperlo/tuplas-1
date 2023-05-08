"""""
Crea una tupla con números, pide al usuario un número por teclado e indica cuantas veces se repite según lo halle en la tupla que has creado.
RESUELVE validar los ingresos del usuario.
""" 
num = 0
con = 0
tupla_numeros = ()

tupla_numeros = (1,6,1,2,3,1,1,7,5,8,5,3,8,3,6,1,6,6,6,6,8,8,4,9,9)

num = int(input("Ingrese un numero: "))

if num > 0 and num < 10:
    for i in tupla_numeros:
        if num ==  i:
            con = con + 1
    print("El numero "+ str(num) + " se repite "+ str(con) + " veces")
else:
    print("El numero ingresado no se encuentra en la tupla")

