#Excepciones
#Try - Except

#Except:
#ZeroDivisionError: Cualquier ejecucion que tenga el divisor con valor 0
#ValueError: El valor es del tipo correcto pero no es capaz de usarse para calcular
#TypeError: El tipo de dato ingresado no coincide con el esperado
#AttributeError: Intenta usar un metodo o funcion que no existe o coincide con el contexto 
#SyntaxError: El codigo en cuestion viola las leyes de escritura o sintaxis de python

# Ejemplo 1
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

# Ejemplo 2 (Conozco que tipo de error me pueden dar cada parte del codigo)
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')
except:
    print('Ha sucedido algo extraño, ¡lo siento!') #Except por Defecto, debe ir siempre como el utlimo excepto

