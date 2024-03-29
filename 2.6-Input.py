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