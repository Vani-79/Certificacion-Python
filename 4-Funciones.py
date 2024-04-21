#Funciones

#La palabra clave Def seguido del nombre que se desee colocar es la forma de clarar mi funcion
#def function_name():
#    cuerpo de la función

# #Funcion 1
def introduction():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    print("Hola, mi nombre es", first_name, last_name)
  
print("Bienvenido al Sistema de banco central! \n")
introduction()

# #Funcion 2
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
suma(2,3,4)

# #Funcion 3 (Se establece un valor predeterminado para la segunda variable por si no se completa o es coincidente)
def introduction(first_name, last_name="Gonsalez"):
     print("Hola, mi nombre es", first_name, last_name)
introduction("Yosvani", "Alfaro")

# #Return

# #Ejemplo
# #En este caso el return con el if, revisa la condicion dada por el argumento de la funcion, si este coincide la funcion continua, pero si este no coincide se termina.
def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return 
    
    print("¡Feliz año nuevo!")

happy_new_year()
happy_new_year(False)

# #Ejemplo 2
# #Funcion que nos dice si un numero es par o impar

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))#El 2 es par
print(strange_function(1))#El 1 es impar

# #Ejemplo 3 devolviendo una lisa

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(9)) #Crea una lista apartir del ciclo for con los numeros desde siguiente que indicamos hasta 0, de forma decreciente

#Ejemplo 4
#Año Bisiesto.

def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
print(is_year_leap(1900))
print(is_year_leap(2000))
print(is_year_leap(2016))
print(is_year_leap(1987))

#Cuantos Dias tiene el mes segun el año.
def days_in_month(year,month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

print(days_in_month(1900,2))
print(days_in_month(2000,2))
print(days_in_month(2016,1))
print(days_in_month(1987,11))

#Si un numero es primo o no
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True
#Encuentra que numeros del 1 al 20 son primos (utilizando la funcion que se creo arriba)
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
print("El Valor Ingresado es 13 por que podemos decir que es:",is_prime(13),", Osea es primo")
print("El Valor Ingresado es 12 por que podemos decir que es:",is_prime(12),", Osea no es primo")