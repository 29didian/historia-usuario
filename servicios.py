# servicios.py

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.
    """
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if len(inventario) == 0:
        print("Inventario vacío")
    else:
        for p in inventario:
            print(f"{p['nombre']} - Precio: {p['precio']} - Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.
    Retorna el producto o None.
    """
    for p in inventario:
        if p["nombre"] == nombre:
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza un producto existente.
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        print("Producto actualizado")
    else:
        print("Producto no encontrado")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    """
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        print("Producto eliminado")
    else:
        print("Producto no encontrado")


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.
    Retorna una tupla con resultados.
    """
    if len(inventario) == 0:
        return (0, 0, None, None)

    unidades_totales = 0
    valor_total = 0

    producto_mas_caro = inventario[0]
    producto_mayor_stock = inventario[0]

    subtotal = lambda p: p["precio"] * p["cantidad"]

    for p in inventario:
        unidades_totales += p["cantidad"]
        valor_total += subtotal(p)

        if p["precio"] > producto_mas_caro["precio"]:
            producto_mas_caro = p

        if p["cantidad"] > producto_mayor_stock["cantidad"]:
            producto_mayor_stock = p

    return (unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock)