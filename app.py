# app.py

from servicios import *
from archivos import *

inventario = []
ejecutando = True

while ejecutando:

    print("\n--- MENÚ ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    try:
        opcion = int(input("Seleccione opción: "))

        if opcion == 1:
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 2:
            mostrar_inventario(inventario)

        elif opcion == 3:
            nombre = input("Buscar nombre: ")
            p = buscar_producto(inventario, nombre)
            print(p if p else "No encontrado")

        elif opcion == 4:
            nombre = input("Nombre: ")
            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad: "))
            actualizar_producto(inventario, nombre, precio, cantidad)

        elif opcion == 5:
            nombre = input("Nombre: ")
            eliminar_producto(inventario, nombre)

        elif opcion == 6:
            datos = calcular_estadisticas(inventario)
            print("Unidades:", datos[0])
            print("Valor total:", datos[1])

            if datos[2]:
                print("Más caro:", datos[2]["nombre"])

            if datos[3]:
                print("Mayor stock:", datos[3]["nombre"])

        elif opcion == 7:
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif opcion == 8:
            ruta = input("Ruta archivo: ")
            nuevos = cargar_csv(ruta)

            if len(nuevos) > 0:
                decision = input("¿Sobrescribir? (S/N): ")

                if decision.upper() == "S":
                    inventario = nuevos
                else:
                    # FUSIÓN
                    for nuevo in nuevos:
                        existente = buscar_producto(inventario, nuevo["nombre"])

                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)

        elif opcion == 9:
            ejecutando = False

        else:
            print("Opción inválida")

    except ValueError:
        print("Entrada inválida")