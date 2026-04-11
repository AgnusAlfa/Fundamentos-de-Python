===========================================================
PROYECTO FINAL MÓDULO 4: ECOMMERCE CLI CON POO Y ROLES
===========================================================

1. DESCRIPCIÓN DEL PROYECTO

Este sistema es una evolución del ecommerce del Módulo 3, ahora estructurado 
completamente bajo el paradigma de Programación Orientada a Objetos (POO). 
Permite la gestión de un inventario por parte de un Administrador y la 
realización de compras con registro de facturación por parte de un Cliente.

2. ARQUITECTURA TÉCNICA (POO)

- HERENCIA: Se utiliza una clase base 'Usuario' de la cual heredan 'Admin' 
  y 'Cliente', compartiendo atributos base pero con métodos especializados.
- COMPOSICIÓN: La clase 'Cliente' contiene una instancia de la clase 
  'Carrito'. La clase 'Catalogo' gestiona una lista de objetos 'Producto'.
- ENCAPSULAMIENTO: La lógica de cálculo de totales, búsqueda y validación 
  reside dentro de sus respectivas clases.

3. FUNCIONALIDADES PRINCIPALES

- ROL ADMIN: 
    * Listar productos.
    * Crear nuevos productos (ID, Nombre, Categoría, Precio).
    * Actualizar datos de productos existentes.
    * Eliminar productos.
    * Guardado automático en 'catalogo.txt'.

- ROL CLIENTE:
    * Navegar por el catálogo.
    * Agregar productos al carrito (validando cantidades).
    * Ver resumen de compra y total.
    * Confirmar Compra: Genera el archivo 'ordenes.txt' con fecha, hora y detalle.
    * Vaciado automático de carrito tras la compra exitosa.

4. MANEJO DE EXCEPCIONES Y ARCHIVOS

- Se implementaron bloques try/except para capturar errores de entrada (ValueError).
- Se utiliza la excepción personalizada 'SaldoInsuficienteError'.
- Lectura y escritura de archivos:
    * 'catalogo.txt': Almacena el inventario de forma persistente.
    * 'ordenes.txt': Registra el historial de ventas realizadas.

5. REFLEXIÓN SOBRE EL APRENDIZAJE

¿Cómo ayuda la POO a organizar un sistema de Ecommerce?
La POO permite que el código sea modular. Si mañana necesitamos agregar un 
nuevo tipo de producto o un nuevo rol (ej: Repartidor), no necesitamos 
reescribir todo el programa, sino simplemente crear una nueva clase o 
heredar de las existentes. Esto hace que el sistema sea escalable y 
mucho más fácil de depurar que la programación puramente funcional.
