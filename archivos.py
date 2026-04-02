# archivos.py

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if len(inventario) == 0:
        print("No hay datos para guardar")
        return

    try:
        archivo = open(ruta, "w", encoding="utf-8")

        if incluir_header:
            archivo.write("nombre,precio,cantidad\n")

        for p in inventario:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            archivo.write(linea)

        archivo.close()
        print(f"Inventario guardado en: {ruta}")

    except Exception as e:
        print("Error al guardar:", e)


def cargar_csv(ruta):
    """
    Carga un archivo CSV y retorna lista de productos.
    """
    inventario = []
    errores = 0

    try:
        archivo = open(ruta, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()

        if lineas[0].strip() != "nombre,precio,cantidad":
            print("Encabezado inválido")
            return []

        for linea in lineas[1:]:
            partes = linea.strip().split(",")

            if len(partes) != 3:
                errores += 1
                continue

            try:
                nombre = partes[0]
                precio = float(partes[1])
                cantidad = int(partes[2])

                if precio < 0 or cantidad < 0:
                    errores += 1
                    continue

                inventario.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

            except:
                errores += 1

        print(f"Archivo cargado. Filas inválidas: {errores}")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado")
    except UnicodeDecodeError:
        print("Error de codificación")
    except Exception as e:
        print("Error:", e)

    return []