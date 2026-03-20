# EJERCICIO 1: Decisión simple
# Propósito: Solicitar un número y determinar si es mayor o igual a 18.

# Solicitar al usuario ingresar un número
# Se usa int() para convertir la entrada de texto a número entero
numero_ingresado = int(input("Ingresa un número: "))

# Evaluar si el número es mayor o igual a 18
if numero_ingresado >= 18:
    print("Eres mayor de edad")
else:
    # Si no se cumple la condición anterior
    print("Eres menor de edad")


# EJERCICIO 2: Decisión múltiple con elif
# Propósito: Evaluar una calificación entre 1 y 7 y mostrar su equivalente.

# Solicitamos la calificación al usuario
# Usamos float() por si la nota incluye decimales, o int() si son solo enteros
calificacion_usuario = float(input("Ingresa una calificación (1 a 7): "))

# Estructura de decisión múltiple para evaluar la nota
if calificacion_usuario == 7:
    print("Excelente")
elif calificacion_usuario == 6:
    print("Muy bien")
elif calificacion_usuario == 5:
    print("Bien")
elif calificacion_usuario == 4:
    print("Suficiente")
elif calificacion_usuario < 4:
# Captura cualquier nota menor que 4 según el requerimiento
    print("Insuficiente")


# EJERCICIO 3: Condiciones anidadas
# Propósito: Clasificar un número usando un if dentro de otro if.


# Solicitar un número entero al usuario
numero_entero = int(input("ÍTEM 3 - Ingresa un número entero: "))

# Primera gran decisión: ¿Es el número mayor o igual a cero?
if numero_entero >= 0:
# Si entramos aquí, el número no es negativo.
# Ahora anidamos otro if para distinguir entre positivo y cero.
    if numero_entero > 0:
        print("Número positivo")
    else:
    # Si es >= 0 pero no es > 0, entonces es cero
        print("Es cero")
else:
# Si la primera condición (>= 0) fue falsa, el número es negativo
    print("Número negativo")


# EJERCICIO 4: Condición de borde
# Propósito: Evaluar si un número está dentro de un rango específico o en sus límites.

# Solicitamos un número al usuario
# Variable en snake_case: numero_ingresado_rango
numero_ingresado_rango = int(input("ÍTEM 4 - Ingresa un número entre 1 y 100: "))

# Evaluamos si el número es exactamente 1 o exactamente 100
# Usamos el operador lógico 'or' (o) para verificar ambos extremos
if numero_ingresado_rango == 1 or numero_ingresado_rango == 100:
    print("Estás en un límite permitido")

# Evaluamos si el número está dentro del rango (mayor que 1 Y menor que 100)
# Usamos el operador lógico 'and' (y) para asegurar que cumpla ambas condiciones
elif numero_ingresado_rango > 1 and numero_ingresado_rango < 100:
    print("Dentro del rango")

# Si no es 1, no es 100, y no está entre 2 y 99, entonces está fuera del rango
else:
    print("Fuera del rango")