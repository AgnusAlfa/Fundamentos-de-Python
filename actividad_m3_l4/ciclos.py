# EJERCICIO 1: Uso básico de while
# Propósito: Imprimir los números del 1 al 5 en pantalla.
# Qué hace el ciclo: Imprime el valor actual del contador en cada vuelta.
# Qué controla su finalización: La condición 'contador_numeros <= 5'. 
# Cuando el contador llega a 6, la condición se vuelve falsa y el ciclo termina.

# Inicializamos la variable contador en 1 (usando snake_case)
contador_numeros = 1

# Mientras el contador sea menor o igual a 5, el ciclo se ejecutará
while contador_numeros <= 5:
    print(contador_numeros)
    
    # Es crucial incrementar el contador en 1 en cada vuelta para evitar un ciclo infinito
    contador_numeros += 1


# EJERCICIO 2: Uso básico de for
# Propósito: Recorrer una lista de frutas e imprimirlas una por una.
# Qué hace el ciclo: Toma cada elemento de la lista y lo asigna temporalmente 
# a la variable 'fruta'. Luego ejecuta el print.
# Qué controla su finalización: El ciclo termina automáticamente cuando 
# se han recorrido todos los elementos de la lista 'lista_frutas'.

# Definimos la lista de frutas (usando snake_case)
lista_frutas = ["manzana", "plátano", "naranja"]

# Iniciamos el ciclo for para recorrer la lista
for fruta in lista_frutas:
    print(fruta)


# EJERCICIO 3: Condición en un ciclo
# Propósito: Recorrer números del 1 al 10 e identificar pares e impares.
# Qué hace el ciclo: Evalúa cada número con el operador módulo (%).
# Qué controla su finalización: La función range(1, 11) genera una secuencia 
# finita; el ciclo termina al procesar el último número (10).


# Usamos range(1, 11) para que incluya del 1 al 10
for numero_actual in range(1, 11):
    # Verificamos si el número es par usando el operador resto (%)
    if numero_actual % 2 == 0:
        print(f"{numero_actual}: Par")
    else:
        # Si el resto no es 0, el número es impar
        print(f"{numero_actual}: Impar")

    
# EJERCICIO 4: Ciclo infinito controlado con break
# Propósito: Solicitar números hasta que el usuario ingrese un 0.
# Qué hace el ciclo: Se ejecuta indefinidamente debido a la condición 'True'.
# Qué controla su finalización: La sentencia 'break', que se activa únicamente si el 'numero_ingresado' es igual a 0.


# Iniciamos un bucle que, en teoría, duraría para siempre
while True:
    # Solicitamos el número dentro del ciclo (snake_case)
    numero_ingresado = int(input("ÍTEM 4 - Ingresa un número (0 para salir): "))
    
    # Verificamos la condición de salida
    if numero_ingresado == 0:
        print("Saliendo del ciclo...")
        break  # Rompe el ciclo inmediatamente y sale
    
    # Si no es 0, el ciclo continúa y vuelve a pedir el número
    print(f"Ingresaste el {numero_ingresado}. ¡Intenta con otro!")


# EJERCICIO 5: Ciclo anidado
# Propósito: Imprimir las tablas de multiplicar del 1 al 3.
# Qué hace el ciclo: El primer for define qué tabla estamos calculando. 
# Por cada número de esa tabla, el segundo for recorre los multiplicadores del 1 al 10.
# Qué controla su finalización: Los rangos finitos de range(1, 4) y range(1, 11).

# Ciclo exterior: controla el número de la tabla (1, 2 y 3)
for numero_tabla in range(1, 4):
    print(f"--- Tabla del {numero_tabla} ---")
    
    # Ciclo interior: realiza las multiplicaciones del 1 al 10 para cada tabla
    for multiplicador in range(1, 11):
        resultado_multiplicacion = numero_tabla * multiplicador
        print(f"{numero_tabla} x {multiplicador} = {resultado_multiplicacion}")
    
    # Imprimimos un espacio en blanco al terminar cada tabla para que se vea ordenado
    print()


# EJERCICIO 6: Uso de continue
# Propósito: Recorrer una lista de nombres y omitir uno específico.
# Qué hace el ciclo: Compara cada nombre con "Juan". Si coinciden, usa continue 
# para saltar el print y seguir con el siguiente nombre de la lista.
# Qué controla su finalización: Se detiene automáticamente al terminar 
# de recorrer la lista 'lista_nombres'.

# Definimos la lista de nombres (snake_case)
lista_nombres = ["María", "Juan", "Andrés", "Lucía"]

print("Lista de nombres (omitiendo a Juan):")

for nombre in lista_nombres:
    # Si el nombre actual es "Juan", saltamos la iteración
    if nombre == "Juan":
        continue  # Esta línea hace que Python ignore el print de abajo solo para Juan
    
    # Este print solo se ejecuta para los nombres que NO son "Juan"
    print(nombre)