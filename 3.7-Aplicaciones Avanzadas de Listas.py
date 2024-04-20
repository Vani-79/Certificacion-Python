#Aplicaciones Avanzadas de Listas

cuadrado = [x ** 2 for x in range(10)] #Imprime el cuadrado de un numero, en este caso como es rango 10, empieza desde el 0 y termina con el 10 (sin incluir el 10)
print(cuadrado)

cuadrados = [x ** 2 for x in range(0,10,2)]#Imprime el cuadrado de un numero, hasta rango 10 y tiene un salto de 2
print(cuadrados)

#Listas de Dos Dimensiones

#Ajedrez:
tablero = []
vacio= ""
 
for i in range(8):
    row = [vacio for i in range(8)]
    tablero.append(row)
print(tablero)

empty=""
board = [[empty for i in range(8)] for j in range(8)]
print(board)