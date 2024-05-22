# escribir un programa que tome dos numeros como entrada y realice operaciones basicas
numero1 = int(input("ingrese el numero: "))
numero2 = int(input("ingrese el numero: "))
operacion = int(input("ingrese el operador: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2 if numero2 != 0 else "Indefinida (división por cero no permitida)"

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} y {numero2} es: {division}")


