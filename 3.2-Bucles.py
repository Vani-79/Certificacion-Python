# Bucles
# Ingresar tantos numeros como desee e imprime el numero mas grande ingresado
largest_number = -99999999
number = int(input("Introduce un número o escribe -1 para detener: "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Introduce un número o escribe -1 para detener: "))
print("El número más grande es:", largest_number)

# Contador de Pares e Impares
impar = 0
par = 0
number = int(input("Introduce un número o escribe 0 para detener: ")) 
while number != 0:

    if number % 2 == 1:
        impar += 1
    else:
       par += 1
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
print("Conteo de números impares:", impar)
print("Conteo de números pares:", par)

# Ingresar el mismo numero que hay en una variable 
secret_number = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
number = int(input("Adivina el numero secreto "))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
print("¡Bien hecho, muggle! Eres libre ahora.")

# For
for i in range(10):
    print("El valor de i es", i)

# Si se usar for con range y dos argumentos, esto indica desde que valor empieza y en cual acaba (sin incluirlo)
for i in range(2, 8):
    print("El valor de i es", i)


# Si se usar for con range y tres argumentos, esto indica desde que valor empieza, en cual acaba (sin incluirlo) y de cuanto en cuanto va saltando
for i in range(2, 8, 3):
    print("El valor de i es", i)

# Potencias con el ciclo For (power equivale al numero base y expo es el exponente)
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

# Contar Mississippis 
for i in range (1, 6):
    print(i, "Mississippi")
print("Listos o no aqui voy")

# Break (El for se pausara cuando I obtenga el valor 3) 
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# Continue (ya que el continue no especifica nada distinto a hacer o cambiar, sigue su paso normal)
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

# Pedir palabras constantemente hasta que el usuario indique la palabra secreta
palabra_clave = "chupacabra"
while True:
    # Pide una palabra al Usuario
    palabra = input("Ingrese una palabra: ")
    # Aplica la condicion
    if palabra == palabra_clave:
        print("Has dejado el bucle con éxito.")
        break