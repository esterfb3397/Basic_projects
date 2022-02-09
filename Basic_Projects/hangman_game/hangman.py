import random
from typing import Any, List
import string

from palabras import palabras
from vidas_diccionario import vidas_diccionario_visual

def obtener_palabra_valida(palabras: List[str]) -> str:
    #Seleccionamos al azar una palabra
    palabra = random.choice(palabras)

    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del ahorcado")
    print("=======================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabras)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0: 
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else "-" for letra in palabra ] #list comprehension
        #Mostrar el estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostrar las letras separadas por un espacio.
        print(f"Palabra:{' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()


        if letra_usuario in abecedario:
            if letra_usuario  in palabra:
                letras_adivinadas.add(letra_usuario)
                print(f"Adivinaste la letra {letra_usuario}")
            
            else: 
                letra_usuario not in letras_por_adivinar
                letras_adivinadas.add(letra_usuario)
                vidas = vidas -1 
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
           
    

        elif letra_usuario in len(letras_por_adivinar):
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")
       
    
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Perdiste!¡Ahorcado!Game over...La palabra correcta era: {palabra}")
    else: 
        letras_adivinadas == palabra 
        return   f"¡Enhorabuena!Advinaste la palabra : {palabra}"
   
 # Hay un error ya que cuando adivinas la palabra, en este momento es AIRE, el codigo no termina ni te da el mensaje de que has adivinado la palabra. Lo estoy estudiando para modificarlo. Lo arreglaré a medida que vaya haciendo más proyectos.   

ahorcado()




