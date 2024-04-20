#Operaciones con Listas

# #Rebanada [:], nos permite copiar un elemento de una lista, mas no su nombre
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# #Mismo Codigo pero sin Rebanada
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

#En este caso el 1 marca desde que elemento se muestra 
#y el segundo numero menos el primero , indica cuantos valores de la lista se imprimiran en este caso 2 valores 
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3] #Posicion 1 (6), y segundo numero (3) menos primer numero (1) indica cuantos valores se generan en la nueva lista (2), siendo en este caso (8,6) ya que 8 es el valor en posicion 1
new_list2 = my_list[0:2]#Posicion 0 (1), y segundo numero (2) menos primer numero (0) indica cuantos valores se generan en la nueva lista (2), siendo en este caso (10,8) ya que 10 es el valor en posicion 0 
new_list3 = my_list[2:5]#Posicion 2 (6), y segundo numero (5) menos primer numero (2) indica cuantos valores se generan en la nueva lista (3), siendo en este caso (6,4,2) ya que 6 es el valor en posicion 2
print(new_list)
print(new_list2)
print(new_list3)

#Rebanadas con Indices Negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]#En este caso se empieza desde posicion 1 y el Indice negativo Indica el primer elemento que no se incluye en la rebanada o nueva lista, en este caso seria el numero 2
print(new_list)

#Del
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]#En este caso la Elminacion de elementos empieza desde la posicion 1 osea el numero 8 y termina en la posicion 3 osea el numero 4, 
                #Es decir que la lista eliminara el numero de la posicion en la que empieza hasta el numero anterior de la poscion en que acaba 
print(my_list)

#Del 
my_list = [10, 8, 6, 4, 2]
del my_list[:] #Elimina todo el contenido de la Lista
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list #Elimina la Lista al Completo, incluido el nombre
print(my_list) #Por ende este print da error de ejecucion ya que la lista no existe

#In y Not In permite verificar si un valor esta o no esta dentro de una lista
my_list = [0, 3, 12, 8, 2]

print(5 in my_list) #False
print(5 not in my_list) #True
print(12 in my_list) #True

#Descubrir el numero mas alto dentro de una lista
my_list = [3, 11, 5, 1, 9, 7, 15, 13,17]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

#Una forma mas simple de hacer lo mismo
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)

#Ecnontrar los numeros coincidentes
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
 
for number in bets:
    if number in drawn:
        hits += 1
 
print(hits)

#Toma los numeros de esta lista dada y genera una nueva lista apartir de esta pero sin numeros repetidos
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list=[]
for num in my_list:
    if num not in new_list:
        new_list.append(num)
print("La lista con elementos únicos:\n", new_list)
