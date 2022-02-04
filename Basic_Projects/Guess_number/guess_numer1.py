import random

def adivina_el_número(x):

    print("=============================")
    print("  ¡Bienvenido/a al juego! ")
    print("=============================")
    print("Tu objetivo es adivinar el número generado por el ordenador")

    numero_aleatorio = random.randint(1,x)
    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: "))
        if prediccion < numero_aleatorio:
            print("Intentalo otra vez. El número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intentalo otra vez. El numero escogido es demasiado grande.")
    
    print(f"¡Felicidades, adivinaste el número correcto {numero_aleatorio}!")


adivina_el_número(10)       

