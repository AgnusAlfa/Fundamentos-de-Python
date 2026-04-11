
import datetime  
# Librería para registrar la fecha y hora de las compras

# 1. Definición de la Clase Producto
class Producto:
    def __init__(self, id_prod, nombre, categoria, precio):
        self.id = id_prod
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self):
        # Este método define cómo se ve el producto al imprimirlo
        return f"ID: {self.id} | {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio}"



# 2. Jerarquía de Usuarios (Herencia)
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_bienvenida(self):
        print(f"\nBienvenido/a {self.nombre} al sistema.")

class Admin(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rol = "ADMIN"

class Cliente(Usuario):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.rol = "CLIENTE"
        # Ahora el cliente TIENE un objeto Carrito (Composición)
        self.carrito = Carrito()



# 3. Clase para gestionar el Catálogo (Contenedor de Productos)

class Catalogo:
    def __init__(self):
        # Lista que guardará objetos de la clase Producto
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al catálogo.")

    def listar_productos(self):
        print("\n--- CATÁLOGO ACTUAL ---")
        if not self.productos:
            print("El catálogo está vacío.")
        else:
            for prod in self.productos:
                # Aquí se usa el método __str__ de la clase Producto
                print(prod)

    def buscar_por_id(self, id_buscar):
        for prod in self.productos:
            if prod.id == id_buscar:
                return prod
        return None

    def eliminar_producto(self, id_eliminar):
        prod = self.buscar_por_id(id_eliminar)
        if prod:
            self.productos.remove(prod)
            print(f"Producto ID {id_eliminar} eliminado exitosamente.")
        else:
            print("Error: No se encontró el producto.")

    def buscar_producto(self, termino):
        print(f"\n--- RESULTADOS PARA: '{termino}' ---")
        encontrados = [p for p in self.productos if termino.lower() in p.nombre.lower() or termino.lower() in p.categoria.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron coincidencias.")

    # Guardar en archivo
    def guardar_datos(self):
        try:
            with open("catalogo.txt", "w") as f:
                for p in self.productos:
                    # Guardamos los datos separados por comas
                    f.write(f"{p.id},{p.nombre},{p.categoria},{p.precio}\n")
            print("Datos sincronizados en 'catalogo.txt'.")
        except Exception as e:
            print(f"Error al guardar archivo: {e}")


# 4. Clase para gestionar el Carrito de Compras

class Carrito:
    def __init__(self):
        # Lista de diccionarios: {"producto": objeto, "cantidad": int}
        self.items = [] 

    def agregar(self, producto, cantidad):
        if cantidad > 0:
            self.items.append({"producto": producto, "cantidad": cantidad})
            print(f"¡Éxito! Agregado: {cantidad}x {producto.nombre}")
        else:
            print("Error: La cantidad debe ser mayor a 0.")

    def ver_total(self):
        print("\n--- RESUMEN DE CARRITO ---")
        total = 0
        if not self.items:
            print("El carrito está vacío.")
        else:
            for item in self.items:
                p = item["producto"]
                cant = item["cantidad"]
                subtotal = p.precio * cant
                total += subtotal
                print(f"- {p.nombre} x{cant}: ${subtotal} (${p.precio} c/u)")
            print("-" * 30)
            print(f"TOTAL A PAGAR: ${total}")
        return total

    def confirmar_compra(self):
        """
        Valida el carrito, registra la venta en ordenes.txt 
        y vacía el carrito tras el éxito.
        """
        # 1. Validar si el carrito está vacío
        if not self.items:
            print("\nError: El carrito está vacío. No hay productos para comprar.")
            return

        total_compra = self.ver_total()
        # Obtenemos fecha y hora actual
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%S")

        try:
            # Registrar la compra en un archivo
            with open("ordenes.txt", "a") as f:
                f.write(f"\n--- ORDEN DE COMPRA: {ahora} ---\n")
                for item in self.items:
                    p = item["producto"]
                    f.write(f"Producto: {p.nombre} | Cantidad: {item['cantidad']} | Subtotal: ${p.precio * item['cantidad']}\n")
                f.write(f"TOTAL DE LA VENTA: ${total_compra}\n")
                f.write("=" * 40 + "\n")
            
            # Vaciar el carrito tras confirmar
            self.items.clear()
            print("\n¡Compra confirmada! Los detalles se han guardado en 'ordenes.txt'.")
            print("Su carrito ahora está vacío.")
            
        except Exception as e:
            print(f"Error crítico al registrar la orden: {e}")




# 5. Excepciones personalizadas

class SaldoInsuficienteError(Exception):
    """Excepción para cuando el cliente no tiene dinero (opcional)"""
    pass


# 6. Función principal (MENÚ)

def ejecutar_programa():
    sistema_catalogo = Catalogo()
    
    # Productos iniciales de prueba
    sistema_catalogo.agregar_producto(Producto(1, "Teclado Mecánico", "Tecnología", 35000))
    sistema_catalogo.agregar_producto(Producto(2, "Silla Gamer", "Hogar", 120000))
    sistema_catalogo.agregar_producto(Producto(3, "Camiseta Algodón", "Ropa", 15000))
    sistema_catalogo.agregar_producto(Producto(4, "Pantalón Denim", "Ropa", 35000))
    sistema_catalogo.agregar_producto(Producto(5, "Audífonos Bluetooth", "Tecnología", 45000))
    sistema_catalogo.agregar_producto(Producto(6, "Mouse Inalámbrico", "Tecnología", 12000))
    sistema_catalogo.agregar_producto(Producto(7, "Lámpara Escritorio", "Hogar", 22000))
    sistema_catalogo.agregar_producto(Producto(8, "Taza Cerámica", "Hogar", 5000))

    while True:
        print("\n" + "="*35)
        print("   SISTEMA ECOMMERCE POO")
        print("="*35)
        print("1) Entrar como ADMINISTRADOR")
        print("2) Entrar como CLIENTE")
        print("0) Salir y Guardar")
        
        try:
            opcion = input("\nSelecciona tu rol: ")

            # --- MODO ADMINISTRADOR ---
            if opcion == "1":
                print("\n--- MODO ADMINISTRADOR (CRUD) ---")
                print("a) Listar catálogo")
                print("b) Crear producto")
                print("c) Actualizar producto")
                print("d) Eliminar producto")
                
                sub_op = input("Elige una acción: ").lower()

                if sub_op == "a":
                    sistema_catalogo.listar_productos()
                elif sub_op == "b":
                    try:
                        id_n = int(input("Nuevo ID: "))
                        nom_n = input("Nombre: ")
                        cat_n = input("Categoría: ")
                        pre_n = int(input("Precio: "))
                        sistema_catalogo.agregar_producto(Producto(id_n, nom_n, cat_n, pre_n))
                    except ValueError:
                        print("Error: ID y Precio deben ser números.")
                elif sub_op == "c":
                    try:
                        id_u = int(input("ID del producto a actualizar: "))
                        prod = sistema_catalogo.buscar_por_id(id_u)
                        if prod:
                            prod.nombre = input(f"Nuevo nombre [{prod.nombre}]: ") or prod.nombre
                            prod.precio = int(input(f"Nuevo precio [{prod.precio}]: ") or prod.precio)
                            print("Producto actualizado con éxito.")
                        else:
                            print("Error: Producto no encontrado.")
                    except ValueError:
                        print("Error: El precio debe ser un número.")
                elif sub_op == "d":
                    try:
                        id_e = int(input("ID del producto a eliminar: "))
                        sistema_catalogo.eliminar_producto(id_e)
                    except ValueError:
                        print("Error: El ID debe ser un número.")

            # --- MODO CLIENTE ---
            elif opcion == "2":
                nombre_cliente = input("Tu nombre: ")
                cliente = Cliente(nombre_cliente)
                print(f"\n¡Hola {cliente.nombre}!")
                
                while True:
                    print("\n--- MENÚ CLIENTE ---")
                    print("a) Ver catálogo y Agregar productos")
                    print("b) Ver carrito y Total")
                    print("c) Confirmar Compra (Finalizar)")
                    print("d) Volver al inicio")
                    
                    sub_op = input("Selecciona: ").lower()

                    if sub_op == "a":
                        sistema_catalogo.listar_productos()
                        try:
                            id_p = int(input("\nID del producto a comprar: "))
                            cant = int(input("Cantidad: "))
                            p_selec = sistema_catalogo.buscar_por_id(id_p)
                            if p_selec:
                                cliente.carrito.agregar(p_selec, cant)
                            else:
                                print("Error: El producto no existe.")
                        except ValueError:
                            print("Error: Ingresa números válidos.")

                    elif sub_op == "b":
                        cliente.carrito.ver_total()

                    elif sub_op == "c":
                        cliente.carrito.confirmar_compra()
                        # Si compra con éxito, lo sacamos al menú principal
                        if not cliente.carrito.items: break 

                    elif sub_op == "d":
                        break

            # --- SALIDA ---
            elif opcion == "0":
                print("Guardando datos y saliendo del sistema...")
                sistema_catalogo.guardar_datos()
                break
            
            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Iniciar la aplicación
if __name__ == "__main__":
    ejecutar_programa()