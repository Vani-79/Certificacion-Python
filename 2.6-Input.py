#Interaccion Con el Usuario

#Generando una variable que contenga el Input
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?\n")

#Esta vez el Input contiene un mensaje para el usuario y luego ejecuta su funcionalidad
anything = input("Dime lo que sea...\n")
print("Hmm...", anything, "...¿en serio?")

#Input y Calculo a traves del dato ingresado por el Usuario

#Integer = Enteros
anything = int(input("Ingresa un número:"))
something = anything ** 2
print(anything, "al cuadrado es", something)

#Float = Reales
anything = float(input("Ingresa un número:"))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

#Ejemplo con el Teorema de Pitagoras
cat_a = float(input("Ingresa la longitud del primer cateto: "))
cat_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (cat_a**2 + cat_b**2) ** .5 #Debido a la funcionalidad de Print esta variable es innecesaria
print("La longitud de la hipotenusa es:", hypo)

#Ejemplo Correcto 
cat_a = float(input("Ingresa la longitud del primer cateto: "))
cat_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", hypo)

#Ejemplo con Cadenas de Texto
nombre = input("¿Me puedes dar tu nombre por favor? ")
apellido = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + nombre + " " + apellido+ ".")

#Al Multiplicar un Numero por una Cadena este se convierte en una replicacion, por ejemplo este codigo dibujara un cuadrado
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))

#Operaciones con las mismas variables ingresadas por un input
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
#Suma 
print("\nEl resultado de la suma es = ", a+b)
#Resta
print("El resultado de la resta es = ",a-b)
#Multiplicacion
print("El resultado de la multiplicacion es = ",a*b)
#Division
print("El resultado de la division es = ",a/b)
print("¡Eso es todo, amigos!")

#Ejercicio 1

#Utiliza la siguiente Formula:1./(x + 1./(x + 1./(x + 1./x))) y mira los resultados a los que llegas utilizando los datos: 1, 10, 100, -5
x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

#Ejercicio 2

#Calcula a que hora terminara un evento si tienes la hora en que inicia, los minutos en que inicia y cuanto dura (en minutos) usando los 3 datos por separado
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60 # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24 # corrige las horas para que estén en un rango de (0..23) 
print("El evento acaba a las = ",hour, ":", mins, sep='')

