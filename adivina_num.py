# escribe un programa que genere un numero aleatorio y que permita al usuario adivinar cual es. Proporcionar pistas como "Muy alto" y "Muy bajo" hasta que el usuario adivine el numero.

import random

def adivinar_numero():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("Tienes que adivinar un número entre 1 y 10")
    for _ in range(10):  
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break
    else:
        print(f"Lo siento, no adivinaste el número. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivinar_numero()
