# escribe un programa que permita al usuario agregar, eliminar y mostrar una lista de tareas pendientes.

def mostrar_menu():
    print("\nMenú de Tareas Pendientes:")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

def agregar_tarea(tareas):
    tarea = input("Introduce la tarea que quieres agregar: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Introduce el número de la tarea que quieres eliminar: "))
        if 1 <= indice <= len(tareas):
            tarea = tareas.pop(indice - 1)
            print(f"Tarea '{tarea}' eliminada.")
        else:
            print("Número de tarea no válido.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

def mostrar_tareas(tareas):
    if tareas:
        print("\nLista de Tareas Pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("\nNo hay tareas pendientes.")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            eliminar_tarea(tareas)
        elif opcion == '3':
            mostrar_tareas(tareas)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()
