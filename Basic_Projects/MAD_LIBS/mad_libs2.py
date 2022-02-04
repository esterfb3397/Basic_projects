#Different ways to concatenate
lenguaje = "Python" # Cadena de caracteres asignada a una variable.

# Algunas alternativas
#print("Quiero aprender " + lenguaje) # Concatenar
#print("Quiero aprender {}".format(lenguaje)) # Método .format()
#print(f"Quiero aprender {lenguaje}") # f-string

# Cuando estableces una variable al principio y luego quieres establecer una definición,el código te va coger el nombre dado en la variable.

def add(x: str):
    #lenguaje = "Java"
    print(f"Quiero aprender {lenguaje}")

print(add("hola"))