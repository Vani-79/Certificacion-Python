#Operadores Comparativos == != <= >= min() max()

#Ejercicio

#N es un numero que se asignara y tiene que imprimir True si es Mayor o Igual a 100 y False si es Menor a 0, los numeros ingresados son 55, 99, 100, 101, -5, +123
n= int(input("Ingresa un Numero: "))
print(n>= 100)

# #Ejecucion Condicional If, Elif y Else

# #Ejemplo Identificar cual de los dos numeros ingresados por consola es Mayor
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

if number1 > number2:
    larger_number = number1
    print("El numero mas grande es: ",larger_number)
elif number1 < number2:
    larger_number = number2
    print("El numero mas grande es: ",larger_number)
else:
    number1 == number2
    print("Los numeros ingresados son de igual valor")

# #Ejemplo con 3 numeros
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

largest_number = number1
if number2 > largest_number:
    largest_number=number2
if number3 > largest_number:
    largest_number=number3
print("El numero mas grande es: ",largest_number)

# #Ejemplo 3 Numeros quiero saber que numero de los que ingreso es el mayor y cual es el menor, uso min() y max()
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

print("El numero con menor valor es", min(number1,number2,number3))
print("El numero con mayor valor es", max(number1,number2,number3))

#Ejercicio Random 
cadena = input("ingrese una cadena de texto ")
if cadena == "ESPATIFILIO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif cadena == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No",cadena+"!")

#Ejercicio Calculo de Impuestos
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

#Ejercicio Comprobar si un año ingresado por consola pertenece o no a al Calendario Gregoriano y si pertenece clasificar que tipo de año es
year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
	if year % 4 != 0:
		print("Año Común")
	elif year % 100 != 0:
		print("Año Bisiesto")
	elif year % 400 != 0:
		print("Año Común")
	else:
		print("Año Bisiesto")