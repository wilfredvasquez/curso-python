def gestor_tareas():

    while True:
        print("\nGestor de Tareas")
        print("1.- Agregar tarea")
        print("2.- Ver todas las tareas")
        print("3.- Salir")

        opcion = input("Elige una opción")

        if opcion == "1":
            tarea = input("Escribe la tarea")
            with open("tareas.txt", "a") as archivo:
                archivo.write(tarea + "\n")
            print("Tarea Guardada")
        elif opcion == "2":
            try:
                with open("tareas.txt", "r") as archivo:
                    print("\nTareas:")
                    print(archivo.read())
            except FileNotFoundError:
                print("No hay tareas registradas")
        elif opcion == "3":
            print("Saliendo del gestor de tareas")
            break
        else:
            print("Opción no valida. Intenta de nuevo")


gestor_tareas()
