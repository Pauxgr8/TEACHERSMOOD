# Menú principal
menu_principal = "------- Menú principal -------\n1. Ingrese una tarea\n2. Visualizar tareas\n3. Eliminar tarea\n4. Salir\n---------------"
print(menu_principal)

texto = "Bienvenidos /as"
nombre = "Proyecto_Paula.py"

with open(nombre, 'w') as archivo:
    archivo.write(texto)

tareas_actuales = []
seleccion = int(input("Seleccione una opción: "))

while seleccion <= 4:
    if seleccion == 1:
        tarea_nueva = input("Ingrese una tarea: ")
        tareas_actuales.append(tarea_nueva)
        
    elif seleccion == 2:
        print("Tareas actuales:")
        for idx, tarea in enumerate(tareas_actuales, start=1):
            print(f"{idx}-{tarea}")
        
    elif seleccion == 3:
        if len(tareas_actuales) > 0:
            print("Tareas actuales:")
            for idx, tarea in enumerate(tareas_actuales, start=1):
                print(f"{idx}-{tarea}")
            tarea_eliminar = int(input("Seleccione la tarea a eliminar: ")) - 1
            if 0 <= tarea_eliminar < len(tareas_actuales):
                tareas_actuales.pop(tarea_eliminar)
            else:
                print("Índice de tarea inválido.")
        else:
            print("No hay tareas para eliminar.")
        
    elif seleccion == 4:
        print("Salida exitosa. ¡Lindo Día!")
        break
    
    else:
        print("Error. Opción inválida.")

    print(menu_principal)
    seleccion = int(input("Seleccione una opción: "))
