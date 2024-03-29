#Variables

#Crear una Variable
var= 1
print(var)

#Como Imprimir mas de una Variable
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

#Como Asignar un nueva Valor a una Variable ya Existente

#Ejemplo 1
var = 1
print(var)
var = var + 1
print(var)

#Ejemplo 2, en este caso es como si no se Hubiese Hecho la primera Declaracion de la Variable
var = 100
var = 200 + 300
print(var)

# Ejemplo de Calculo con Variables: Teorema de Pitagoras
a = 3
b = 4
c = (a ** 2 + b ** 2) ** 0.5
print("Si el Cateto A es de" ,a,"\ny El cateto B es de",b,"\nLa Hipotenusa sera de", c)

#Ejercicio 1 
jhon = 3 
mary = 5 
adam = 6
print(jhon,mary,adam)
total_apples = jhon + mary + adam
print(total_apples)

#Ejercicio 2
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61 # 1 Milla son 1.61 kilometros por ende la variable debe tomar los datos ingresados en millas y multiplicarlo por 1.61
kilometers_to_miles = kilometers / 1.61 #Tambien puede multiplicarse por 0.62

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")

#Ejercicio 3
#Utiliza la siguiente formula 3x3 - 2x2 + 3x - 1, asignandole a la variable X los valores: 0, 1, -1 respectivamente

print("X vale 0")
x =  0 
x = float(x)
y= 3*x**3 - 2*x**2 + 3*x -1
print("y =", y,"\n")

print("X vale 1")
x =  1
x = float(x)
y= 3*x**3 - 2*x**2 + 3*x -1
print("y =", y,"\n")

print("X vale -1")
x =  -1
x = float(x)
y= 3*x**3 - 2*x**2 + 3*x -1
print("y =", y,"\n")

