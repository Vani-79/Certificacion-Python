#Alcances
# Los alcances son en donde y hasta donde es capaz de el codigo identificar una variable o una funcion, por ejemplo una variable creada dentro de una funcion, solo tiene alcance en esa funcion
# En cambio una funcion tiene un alcance completo en el codigo.

#Ejemplo: 
# def scope_test():
#     x = 123
# scope_test()
# print(x) Este codigo da error "no se reconoce el parametro x" debido a que solo la funcion conoce esa variable y su parametro

#Ejemplo 2 
def my_function():
    print("¿Conozco a la variable?", var)
var = 1
my_function()
print(var) # Pese a que la variable se inicio despues de la funcion creada, la funcion conoce lo que esta fuera de si misma y lo adjunta

#Ejemplo 3
#Si tengo dos variables con el mismo nombre, una definida dentro de la funcion y otra definida en el cuerpo general de mi codigo, depende de donde se haga el llamado reconocera un valor u otro
def my_function():
    var = 2
    print("¿Conozco a la variable?", var) #En este caso el llamado se hace desde dentro de la funcion, por ende reconoce el valor 2

var = 1
my_function()
print(var) #En este caso el llamado se hace desde dentro de la funcion, por ende reconoce el valor 2

#Global
#La palabra clave Global nos permite extender el alcance de una variable para todo el codigo

#Ej:
def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)

var = 1
my_function()
print(var) #El resultado es 2, ya que en el momento en que se inicializo la variable como "Global" se le dio el valor "2"



