#Listas

# Ej: Una "variable" (es una lista realmente) que contenga 5 numeros
numero = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numero)  # I mprimiendo contenido de la lista original.
 
numero[0] = 111 # Reemplaza el valor inicial de la lista en este caso 10 por 111
print("Nuevo contenido de la lista: ", numero)  # Contenido actual de la lista.

numero[1] = numero[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numero)  # Imprimiendo el contenido de la lista actual.

print(numero[0]) # Accediendo al primer elemento de la lista.

#Para conocer la longitud de una lista se utiliza la funcion len() (su nombre proviene de length - longitud).
#La intruccion Del seguido de la lista y una posicion exacta dentro de esta, nos permite eliminar el elemento presenta en esa posicion

#Tambien existen los indicies negativos, por ejemplo el numero -1 indica al ultimo elemento de una lista
#Ejemplo:
numbers = [111, 7, 2, 1]
print(numbers[-1])

#Ejercicio 

###sombrero magico con una lista de cinco números: 1, 2, 3, 4, y 5.
#escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
#escribir una línea de código que elimine el último elemento de la lista (Paso 2)
#escribir una línea de código que imprima la longitud de la lista existente (Paso 3).

sombrero= [1,2,3,4,5,]
sombrero[3]=input("Ingrese un numero para reemplazar el numero central de nuestro sombrero: ")
del sombrero[4]
print(len(sombrero))

#Agregar Elementos a una Lista:

#Append agrega el elemento indicado al final de la lista list.append(elemento)
my_list = []  

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#Insert se indica el elemento que se desea ingresar y el lugar especifico en que el se ingresara list.insert(posicion, elemento)
my_list = []  
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)

#Usando una lista y metodo for para calcular el valor de la suma de todos los elementos de la lista:

#Usando Len y For:
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#Usando solo For
my_list = [10, 1, 8, 3, 5]
total = 0
 
for i in my_list:
    total += i
 
print(total)

#Como cambiar el orden de ciertos elementos respectivos de una lista:

my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0] #Intercambio el primer elemento de mi lista, con el ultimo 
my_list[1], my_list[3] = my_list[3], my_list[1] #Intercambio el segundo elemento de mi lista, con el penultimo 
 
print(my_list)

#Miembros de los Beatles:

#paso 1: crea una lista vacía llamada beatles;
#paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
#paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
#paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
#paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
for i in range (2):
    miembro= input("Ingrese el nuevo miembro: ")
    beatles.append(miembro)
del beatles[3]
del beatles[3]
beatles.insert(0,"Ringo Starr")

