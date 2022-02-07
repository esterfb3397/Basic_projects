# Este es el juego de piedra, papel o tijera. La piedra gana a las tijeras,las tijeras ganan al papel y el papel gana a la piedra.

import random

pi = "pi"
ti = "ti"
pa = "pa"


def jugar():
    usuario = input("Escoja una opción: Piedra(pi), Papel (pa) o Tijera (ti): ").lower().strip()
    print("usuario: ", usuario)
    print("type(usuario): ", type(usuario))

    ordenador = random.choice([pi,pa,ti])
    print("ordenador: ", ordenador)
    print("type(ordenador): ", type(ordenador))
        
    if usuario == ordenador:
        return "¡Empate!"

    if gana_usuario(usuario, ordenador):
        return "¡Ganaste!"

    return "¡Perdiste!"


def gana_usuario(usuario ,ordenador):

    
    
    if ((usuario == pi and ordenador == ti) or 
    (usuario == ti and ordenador == pa) or 
    (usuario == pa and ordenador == pi)):
        return True

    else : return False


print(jugar())