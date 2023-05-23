"""""
Tenemos una lista de Tuplas que representan ciertas caracteristicas de una serie de productos. Cada tupla tiene 4 elementos:
nombre del producto, precio, cantidad disponible, marca
Se desea obtener una lista de productos que cumplan con ciertas condiciones de busqueda:  percio maximo y marca especifica
"""""
marca_especifica = ""
precio_maximo = 0

lista_tuplas = [("Microondas",30000,8,"Samsung"),("tv",90000,15,"Sony"),("Heladera",75000,12,"Drean"),("Celular",56000,23,"Xiaomi")]

precio_maximo = int(input("Ingrese precio maximo: "))
marca_especifica = (input("Ingrese marca especifica: "))

lista_final = []



for t in lista_tuplas:
    if t[1] <= precio_maximo and t[3] == marca_especifica:
        lista_final.append(t)

print(lista_final)

#CORRECCIOON:
#El problema radica en que estás comparando el precio (t[1])
# en lugar de la marca (t[3]) dentro del bucle for en la condición del if.

marca_especifica = input("Ingrese marca específica: ").lower()
precio_maximo = int(input("Ingrese precio máximo: "))

lista_tuplas = [
    ("Microondas", 30000, 8, "Samsung"),
    ("TV", 90000, 15, "Sony"),
    ("Heladera", 75000, 12, "Drean"),
    ("Celular", 56000, 23, "Xiaomi")
]

lista_final = []

for t in lista_tuplas:
    if t[2] <= precio_maximo and t[3].lower() == marca_especifica:
        lista_final.append(t)

print(lista_final)
