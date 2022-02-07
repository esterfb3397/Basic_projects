import random

def adivina_el_juego_PC(x):
    print("=============================")
    print("  ¡Bienvenido/a al juego! ")
    print("=============================")
    print(f"Selecciona un número entre 1 y {x} para que el PC lo adivine")

    limite_inferior = 1 
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #Generamos predicción
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior #puede ser también el limite_superior

        #Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {prediccion}. Si es muy alta, ingresa (A).Si es muy baja, ingresa (B). Si es correcta, ingresa (C)").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    print(f"¡Genial! EL ordenador ha adivinado el número {prediccion}")
    

adivina_el_juego_PC(10)
