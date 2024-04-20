#Ordenamiento de Listas

#Ordenar una Lista de forma ascendente
my_list = [8, 10, 6, 2, 4]  # lista a ordenar
print("Lista Desordenada", my_list)
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print("Lista Ordenada de Forma Ascendente", my_list)

#Ordenar una lista de numeros ingresados por el usuario
my_list = []
swapped = True
num = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nOrdenada:")
print(my_list)

#Ordenar una lista con el comando estandar de Python
my_list = [8, 10, 6, 2, 4]
print("Lista Desordenada",my_list)
my_list.sort()
print("Lista Ordenada de Forma Ascendente",my_list)

