# EJERCICIO 1: Secuencia de pares e impares
# Propósito: Mostrar números siguientes según si es par o impar, validando que esté en el rango de 1 a 100.

print("--- EJERCICIO 1 ---")

# Usamos un bucle infinito para seguir preguntando si el usuario se equivoca
while True:
    numero_ingresado = int(input("Ingresa un número (entre 1 y 100): "))

    # 1. Validar el rango (Condición de error)
    if numero_ingresado <= 0 or numero_ingresado > 100:
        print("No es posible realizarlo. Por favor, intenta de nuevo.\n")
        # Al no haber un 'break' aquí, el ciclo while vuelve al principio automáticamente
        
    # 2. Si el número es correcto, evaluamos si es Par
    elif numero_ingresado % 2 == 0:
        print("Resultado: usted ha ingresado un numero par y los números pares siguientes son:")
        # range(inicio, fin, salto). Sumamos 2 para empezar desde el siguiente par.
        # Ponemos 101 como fin para asegurarnos de que el 100 esté incluido.
        for n in range(numero_ingresado + 2, 101, 2):
            print(n, end=" ")  # end=" " hace que se impriman hacia el lado y no hacia abajo
        print("\n") # Salto de línea final
        break # Rompemos el bucle porque ya terminamos la tarea
        
    # 3. Si no es error y no es par, obligatoriamente es Impar
    else:
        print("Resultado: usted ha ingresado un número impar y los números impares siguientes son:")
        # Ponemos 100 como fin para que llegue hasta el 99.
        for n in range(numero_ingresado + 2, 100, 2):
            print(n, end=" ")
        print("\n") # Salto de línea final
        break # Rompemos el bucle



# EJERCICIO 2: Sistema de Notas
# Propósito: Leer 5 notas (entre 0 y 10), mostrar todas, 
# calcular la media, identificar la mayor y la menor.

print("--- EJERCICIO 2 ---")

# Creamos una lista vacía para almacenar las notas del alumno
notas = []

# Usamos un bucle while que se repetirá hasta que tengamos exactamente 5 notas válidas
while len(notas) < 5:
    # Solicitamos la nota. Usamos float() por si el usuario ingresa decimales (ej: 6.5)
    nota_ingresada = float(input(f"Ingresa la nota {len(notas) + 1} (entre 0 y 10): "))
    
    # Validamos que la nota esté en el rango permitido (entre 0 y 10)
    if 0 <= nota_ingresada <= 10:
        notas.append(nota_ingresada)  # Si es válida, la guardamos en la lista
    else:
        print("Error: La nota debe estar comprendida entre 0 y 10. Intenta de nuevo.\n")

# Realizamos los cálculos usando las funciones nativas de Python
nota_media = sum(notas) / len(notas)  # sum() suma todo, len() cuenta cuántas hay
nota_maxima = max(notas)              # max() busca el número más alto
nota_minima = min(notas)              # min() busca el número más bajo

# Mostramos los resultados finales
print("\n--- Resultados del Alumno ---")
print(f"Todas las notas ingresadas: {notas}")
print(f"Nota media (promedio): {nota_media}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
print("\n") # Salto de línea para separar del próximo ejercicio



# EJERCICIO 3: Días de un mes
# Propósito: Pedir al usuario un número de mes (1-12) y 
# mostrar la cantidad de días que tiene.

print("--- EJERCICIO 3 ---")

# Usamos un bucle infinito para validar que el mes ingresado sea correcto
while True:
    mes_ingresado = int(input("Ingresa un número de mes (del 1 al 12): "))
    
    # Validamos que el número esté en el rango de meses del año
    if 1 <= mes_ingresado <= 12:
        
        # Agrupamos los meses que tienen 31 días (Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre)
        if mes_ingresado in [1, 3, 5, 7, 8, 10, 12]:
            print(f"El mes {mes_ingresado} tiene 31 días.")
            
        # Agrupamos los meses que tienen 30 días (Abril, Junio, Septiembre, Noviembre)
        elif mes_ingresado in [4, 6, 9, 11]:
            print(f"El mes {mes_ingresado} tiene 30 días.")
            
        # El caso especial de Febrero
        elif mes_ingresado == 2:
            print(f"El mes {mes_ingresado} tiene 28 días (o 29 si es año bisiesto).")
            
        # Rompemos el ciclo porque ya entregamos la respuesta correcta
        break
        
    else:
        # Mensaje de error si ingresa un número como 15 o -2
        print("Error: Número de mes inválido. Por favor, ingresa un número del 1 al 12.\n")

print("\n¡TRABAJO PRÁCTICO COMPLETADO CON ÉXITO!")