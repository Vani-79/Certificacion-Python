#Funciones Multiparametro

#Funcion de tres parametros para identificar si las longitudes de los datos ingresados, podrian permitir la creacion de un triangulo,
#basandonos en que la suma de dos lados del triangulo siempre debe ser mayor que el tercer lado

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

#Teorema de Pitagoras:

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2 
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))

