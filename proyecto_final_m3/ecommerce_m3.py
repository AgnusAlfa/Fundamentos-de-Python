# =========================================================
# PROYECTO FINAL MÓDULO 3 - ECOMMERCE CLI
# =========================================================

# 1. CATÁLOGO DE PRODUCTOS
catalogo = {
    1: {"nombre": "Camiseta Algodón", "precio": 15000, "categoria": "ropa"},
    2: {"nombre": "Pantalón Denim", "precio": 35000, "categoria": "ropa"},
    3: {"nombre": "Audífonos Bluetooth", "precio": 45000, "categoria": "tecnologia"},
    4: {"nombre": "Mouse Inalámbrico", "precio": 12000, "categoria": "tecnologia"},
    5: {"nombre": "Lámpara de Escritorio", "precio": 22000, "categoria": "hogar"},
    6: {"nombre": "Taza de Cerámica", "precio": 5000, "categoria": "hogar"}
}

# 2. CARRITO DE COMPRAS
carrito = []


# 3. FUNCIONES DEL PROGRAMA
def mostrar_menu():
    print("\n" + "="*30)
    print(" Bienvenido/a a tu Ecommerce")
    print("="*30)
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")
    print("="*30)

def listar_productos(cat):
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    for id_prod, info in cat.items():
        print(f"ID: {id_prod} | {info['nombre']} | Categoría: {info['categoria']} | Precio: ${info['precio']}")
    print("-" * 30)

def buscar_producto(cat, termino):
    print(f"\n--- RESULTADOS PARA: '{termino}' ---")
    encontrado = False
    termino = termino.lower() 
    for id_prod, info in cat.items():
        if termino in info['nombre'].lower() or termino in info['categoria'].lower():
            print(f"ID: {id_prod} | {info['nombre']} | Categoría: {info['categoria']} | Precio: ${info['precio']}")
            encontrado = True
    if not encontrado:
        print("No se encontraron productos que coincidan con tu búsqueda.")
    print("-" * 30)

def agregar_al_carrito(cat, carr):
    print("\n--- AGREGAR AL CARRITO ---")
    try:
        id_ingresado = int(input("Ingresa el ID del producto: "))
        if id_ingresado in cat:
            cantidad = int(input(f"¿Cuántas unidades de '{cat[id_ingresado]['nombre']}' deseas?: "))
            if cantidad > 0:
                item_carrito = {
                    "id": id_ingresado,
                    "nombre": cat[id_ingresado]["nombre"],
                    "precio": cat[id_ingresado]["precio"],
                    "cantidad": cantidad
                }
                carr.append(item_carrito)
                print(f"¡Éxito! Se agregaron {cantidad}x '{cat[id_ingresado]['nombre']}' al carrito.")
            else:
                print("Error: La cantidad debe ser mayor a 0.")
        else:
            print("Error: ID no encontrado.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

def ver_carrito_y_total(carr):
    """Muestra los ítems en el carrito, calcula el subtotal por producto y el total final."""
    print("\n--- TU CARRITO DE COMPRAS ---")
    
    # Validamos si el carrito está vacío usando len()
    if len(carr) == 0:
        print("Tu carrito está vacío. ¡Anímate a comprar algo!")
        return # El return vacío detiene la función aquí para no hacer cálculos innecesarios
        
    total_compra = 0
    
    # Recorremos la lista del carrito para mostrar cada ítem
    for item in carr:
        # Calculamos el subtotal (precio * cantidad) de ese producto en específico
        subtotal = item["precio"] * item["cantidad"]
        print(f"- {item['cantidad']}x {item['nombre']} (${item['precio']} c/u) | Subtotal: ${subtotal}")
        
        # Vamos sumando el subtotal al gran total
        total_compra += subtotal
        
    print("-" * 30)
    print(f"TOTAL A PAGAR: ${total_compra}")
    print("-" * 30)

def vaciar_carrito(carr):
    """Limpia todos los elementos de la lista del carrito."""
    # El método .clear() vacía la lista por completo
    carr.clear()
    print("\n¡El carrito ha sido vaciado exitosamente!")


# 4. CICLO PRINCIPAL DEL PROGRAMA
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        listar_productos(catalogo)
        
    elif opcion == "2":
        termino_busqueda = input("\nIngresa el nombre o categoría a buscar: ")
        buscar_producto(catalogo, termino_busqueda)
        
    elif opcion == "3":
        agregar_al_carrito(catalogo, carrito)
        
    elif opcion == "4":
        # Llamamos a la nueva función y le pasamos la lista del carrito
        ver_carrito_y_total(carrito)
        
    elif opcion == "5":
        # Llamamos a la función para vaciar, pasándole la lista del carrito
        vaciar_carrito(carrito)
        
    elif opcion == "0":
        print("\n¡Gracias por visitar nuestro Ecommerce! Hasta pronto.")
        break
        
    else:
        print("\nError: Opción no válida. Por favor, ingresa un número del 0 al 5.")