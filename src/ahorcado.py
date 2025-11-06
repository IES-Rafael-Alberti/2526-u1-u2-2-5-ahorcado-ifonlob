import random
import os

"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Irene Foncubierta Lobatón    
Fecha: 6/11/2025
"""

def solicitar_letra(letras_usadas:list[str])->str:
    '''
    Solicita una letra al jugador.
    
    La letra tiene que ser válida (solo una letra) y no puede contener carácteres especiales ni números ni estar ya usada.
    
    Parameters
    ----------
    letras_usadas: list of str
        Lista de letras que ya se han usado
    
    Returns
    -------
    letra:
        La letra introducida por consola por el jugador.
    
    '''
    letra = input("Ahora indique una letra:\n").upper()
    while not letra.isalpha() or len(letra) != 1 or letra in letras_usadas:
        if letra in letras_usadas:
            print("Ya has introducido esa letra, introduzca una diferente.")
        else:
            print("Por favor, introduzca una letra solamente.")
        letra = input("Introduzca una letra:").upper()
    return letra

def actualizar_estado(lista_palabra_a_adivinar, guiones, letra)->tuple[bool,list[str]]:
    '''
    Actualiza la palabra según la letra introducida por el jugador.
    
    Parameters
    ----------
    lista_palabra_a_adivinar : list of str
        Lista que incluye la palabra que el jugador tiene que adivinar
    guiones : list of str
        Lista que simula los huecos vacíos aún por adivinar.
    letra : str
        La letra introducida por consola por el jugador.

    
    Returns
    -------
    bool
        True si la letra se encuentra en la palabra, False en caso contrario.
    list of str
        Lista actualizada de los huecos vacíos con las letras acertadas.
    '''
    letra_encontrada = False
    for i in range(len(lista_palabra_a_adivinar)):
        if lista_palabra_a_adivinar[i].upper() == letra:
            guiones[i] = letra
            letra_encontrada = True
    return letra_encontrada, guiones

def comprobar_disponibilidad(letra_encontrada, letras_usadas, letra, intentos):
    """
    Actualiza la lista de letras usadas y los intentos según si la letra está o no en la palabra.

    Parameters
    ----------
    letra_encontrada : bool
        Indica si la letra introducida se encontró en la palabra.
    letras_usadas : list of str
        Lista de letras que ya han sido usadas.
    letra : str
        La letra introducida por el jugador.
    intentos : int
        Número actual de intentos restantes.

    Returns
    -------
    list of str
        Lista actualizada de letras usadas.
    int
        Número actualizado de intentos restantes.
    """
    if not letra_encontrada:
        print("La letra introducida no se encuentra en la palabra.")
        intentos -= 1
    letras_usadas.append(letra)
    return letras_usadas, intentos

def actualizar_palabra(intentos, letras_usadas, guiones):
    """
    Muestra el estado actual del juego con la palabra parcial, los intentos restantes y las letras usadas.

    Parameters
    ----------
    intentos : int
        Número actual de intentos que le quedan al jugador.
    letras_usadas : list of str
        Lista de letras que el jugador ya ha utilizado.
    guiones : list of str
        Representación actual de la palabra con letras adivinadas y guiones bajos.

    Returns
    -------
    None
        La función solo imprime información en la consola y no retorna ningún valor.
    """
    print("Tu palabra se queda de la siguiente forma:\n")
    print(" ".join(guiones))
    print("Te quedan", intentos, "intentos.")
    print("")
    if len(letras_usadas) > 0:
        print("Recuerde que ya ha usado las siguientes letras:", " , ".join(letras_usadas))

def comprobar_palabra(palabra_a_adivinar, intentos):
    """
    Solicita una palabra al jugador, verifica si es válida y si coincide con la palabra a adivinar.

    Permite al jugador introducir la palabra o escribir 'Skip' para saltar el turno. 
    
    Si la palabra introducida es válida y coincide, marca como adivinada, 
    en caso contrario si no se elige 'Skip' y no se acierta la palabra reduce el número de intentos.

    Parameters
    ----------
    palabra_a_adivinar : str
        Palabra que el jugador debe adivinar.
    intentos : int
        Número actual de intentos restantes del jugador.

    Returns
    -------
    bool
        True si la palabra fue adivinada correctamente, False en caso contrario.
    int
        Número actualizado de intentos restantes.
    """

    palabra = input("Introduzca la palabra o introduzca 'Skip' para saltar turno si no desea introducir una palabra:\n")
    while not palabra.isalpha() and palabra != "Skip":
        print("Introduzca una palabra válida, por favor. (Revise si ha introducido carácteres especiales.)")
        palabra = input("Introduzca la palabra o introduzca 'Skip' para saltar turno si no desea introducir una palabra:\n").upper()
    while len(palabra) != len(palabra_a_adivinar) and palabra != "Skip":
        print("Introduzca una palabra válida, por favor. (Revise si la longitud de la palabra corresponde con la de la palabra a adivinar.)")
        palabra = input("Introduzca la palabra o introduzca 'Skip' para saltar turno si no desea introducir una palabra:\n")
    adivinado = False
    if palabra.lower() == palabra_a_adivinar:
        adivinado = True
    elif palabra == "Skip":
        adivinado = False
    else:
        print("No has acertado la palabra, siga intentándolo.")
        intentos -= 1
        print("Te quedan", intentos, "intentos.\n")
    if not adivinado and palabra != "Skip" and intentos == 0:
        print("Has perdido. La palabra era:", palabra_a_adivinar)
    return adivinado, intentos

def jugar():
    try:
        ancho = os.get_terminal_size().columns
    except OSError:
        ancho = 50  
    palabras_ahorcado = [
        "montaña", "pelota", "elefante", "naranja", "carpeta", "tren",
        "jardín", "zapato", "camiseta", "limón", "escuela", "parque",
        "ventana", "mariposa", "coche"
    ]
    palabra_a_adivinar = random.choice(palabras_ahorcado)
    lista_palabra_a_adivinar = list(palabra_a_adivinar)
    letras_usadas = []
    intentos = 6
    guiones = ["_"] * len(palabra_a_adivinar)
    adivinado = False
    print("==================".center(ancho))
    print("JUEGO DEL AHORCADO".center(ancho))
    print("==================".center(ancho))
    print(f"Bienvenido al juego del ahorcado. La palabra a adivinar posee", len(palabra_a_adivinar), "letras distribuidas de la siguiente forma:\n")
    print("Tienes 6 intentos.")
    print(" ".join(guiones))
    print(" ")
    mensaje_victoria = False
    while not adivinado and intentos > 0:
        letra = solicitar_letra(letras_usadas)
        letra_encontrada, guiones = actualizar_estado(lista_palabra_a_adivinar, guiones, letra)
        letras_usadas, intentos = comprobar_disponibilidad(letra_encontrada, letras_usadas, letra, intentos)
        actualizar_palabra(intentos, letras_usadas, guiones)
        if "_" not in guiones:
            adivinado = True
        else:
            adivinado, intentos = comprobar_palabra(palabra_a_adivinar, intentos)
        if adivinado and not mensaje_victoria:
            if intentos == 5:
                print("¡Felicidades! Has adivinado la palabra con tan solo un fallo.")
            elif intentos == 6:
                print("¡Felicidades! Has adivinado la palabra sin fallar.")
            else: 
                print("¡Felicidades! Has adivinado la palabra con tan solo",(6 - intentos),"fallos.")
            mensaje_victoria = True
        if intentos == 0 and not adivinado:
            print("Has perdido. La palabra era:", palabra_a_adivinar)
    """
    Ejecuta una partida completa del juego del ahorcado.

    El juego selecciona una palabra al azar de una lista predefinida y gestiona la lógica de turnos, 
    entrada de letras, comprobación de aciertos y control de intentos restantes. Muestra mensajes de victoria, derrota y el estado actual de la partida por consola.

    Parameters
    ----------
    None

    Returns
    -------
    None
        La función no retorna ningún valor; toda la interacción se realiza mediante mensajes en consola.
    """

def main():
    jugar()

if __name__ == "__main__":
    main()
