"""""
Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.
"""""
meses = ()
num = 0

meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")

num = int(input("Ingrese un numero: "))

if (num == 0):
    exit
else:
    if(num >=1 and num <=len(meses)):
        print(meses[num-1])  #le restamos uno porque los meses empiezan desde la posicion 0
    else:
        print("El numero se encuentra fuera del rango de posiciones")

#SUGERENCIA CON CORRECCION: Pequeña mejora que pODES hacer en la línea 
#donde verificas si el usuario ingresó un cero para salir del programa.En lugar de usar exit como una función,
·#pones break para salir del bucle y finalizar el programa.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    num = int(input("Ingrese un número: "))
    if num == 0:
        break
    elif 1 <= num <= len(meses):
        print(meses[num-1])
    else:
        print("El número se encuentra fuera del rango de posiciones")
