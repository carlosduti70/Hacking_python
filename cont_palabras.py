def palabras(lista):
    contador = 0
    for i in lista:
        palabras = i.split()
        contador += len(palabras)
    return contador

mi_lista = ["Hola, mundo", "Esta es una lista de cadenas", "Python es divertido"]
total_palabras = palabras(mi_lista)
print(total_palabras)