#Tuplas y Diccionarios:

#Tuplas(a diferencia de las listas, estas se crean con parentesis o simplemente separando los datos con , ademas pueden ser de distintos tipos los datos):
# #Funciones que conocen las Tuplas
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#Diccionarios:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#Keys, me genera una lista de las claves que contiene un diccionario
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])

#Agregar un valor nuevo al diccionario:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.update({"pato": "canard"})
print(dictionary)

#Reemplazar un valor del diccionario:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)

#Eliminando una clave:
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)

#Ejemplo tuplas y diccionarios
school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break

if name in school_class:
    school_class[name] += (score,)
else:
    school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)