# 📦 Sistema de Inventario en Python

## 🧾 Descripción

Este proyecto consiste en un sistema de inventario desarrollado en Python que permite gestionar productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), así como guardar y cargar datos utilizando archivos CSV.

El sistema está diseñado de forma modular, utilizando funciones, listas, diccionarios y manejo de archivos, garantizando persistencia de la información entre ejecuciones.

---

## 🎯 Objetivo

Implementar un inventario funcional que:

* Permita gestionar productos.
* Calcule estadísticas del negocio.
* Guarde y cargue datos desde archivos CSV.
* Maneje errores sin cerrar el programa.

---

## 🧱 Estructura del proyecto

```
📁 proyecto_inventario/
│
├── app.py          # Programa principal (menú)
├── servicios.py    # Lógica del inventario (CRUD + estadísticas)
├── archivos.py     # Manejo de archivos CSV
├── diagrama.png    # Diagrama de flujo del sistema
└── README.md       # Documentación del proyecto
```


### 📌 Gestión de inventario

* Agregar productos
* Mostrar inventario
* Buscar productos
* Actualizar productos
* Eliminar productos

### 📊 Estadísticas

* Total de unidades
* Valor total del inventario
* Producto más caro
* Producto con mayor stock

### 💾 Persistencia (CSV)

* Guardar inventario en archivo CSV
* Cargar inventario desde CSV
* Validación de datos
* Manejo de errores

---

## 📁 Formato del archivo CSV

El archivo debe tener el siguiente formato:

```
nombre,precio,cantidad
Laptop,2500,5
Mouse,50,10
```

---

## 🛡️ Validaciones implementadas

* Entradas numéricas válidas
* Precios y cantidades no negativas
* Validación de encabezado en CSV
* Manejo de errores:

  * Archivo no encontrado
  * Error de formato
  * Problemas de lectura/escritura

---

## 🔄 Política de carga de datos

Al cargar un archivo CSV, el sistema permite:

* **Sobrescribir** el inventario actual
* **Fusionar** datos:

  * Si el producto existe → suma cantidades
  * Si el precio cambia → se actualiza

---

## 🧠 Tecnologías usadas

* Python
* Listas
* Diccionarios
* Funciones
* Archivos (CSV)

---

## 📌 Autor

Didian Cassiani

---

## ✅ Estado del proyecto

✔ Funcional
✔ Modular
✔ Cumple con todos los requisitos de la actividad

---
