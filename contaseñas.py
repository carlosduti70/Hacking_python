# escribe un programa que genere una contraseña aleatoria de una longitud especificada por el usuario. Esta debe contener letras, numeros y caracteres especiales.

import random
import string

def generar_contraseña(longitud):
    # Definir los caracteres que se pueden usar en la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña: "))
            if longitud <= 0:
                print("La longitud debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

    contraseña = generar_contraseña(longitud)
    print(f"Tu contraseña generada es: {contraseña}")

if __name__ == "__main__":
    main()