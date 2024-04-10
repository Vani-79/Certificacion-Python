# Print

# \n Hace un Salto de Linea, Parecido a print()

print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")

# Print posee dos argumentos de Palabra clave (end y sep) y estos constan del argumento (end) un = y el valor que tendra el argumento, estos siempre se deben usar despues del ultimo argumento de posicion

print("Mi nombre es", "Python.", end="")
print("Monty Python.")

# Pyton de normal separa los datos en espacios cuando se utilizan comas en la cadena de texto de un print, pero esto se puede cambiar utilizando la palabra clave "sep"

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

# Tambien se pueden usar juntos

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

# Resultado esperado: Programming***Essentials***in...Python

print("Programming","Essentials","in", sep="***",end="...")
print("Python")

# Para hacer un print multilinea se ocupa triple comilla ("""  Hola  """)

