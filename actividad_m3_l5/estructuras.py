# =========================================================
# ACTIVIDAD 5: Explorando Estructuras de Datos
# =========================================================

# ---------------------------------------------------------
# ÍTEM 1: CREAR ESTRUCTURAS
# ---------------------------------------------------------
# 1. Lista (list): Colección ordenada y mutable.
lista_compras = ["pan", "leche", "huevos"]

# 2. Tupla (tuple): Colección ordenada pero inmutable (no cambia).
tupla_coordenadas = (10.5, 20.8, 30.2)

# 3. Conjunto (set): Colección desordenada de elementos únicos.
conjunto_id = {101, 102, 103}

# 4. Diccionario (dict): Colección de pares clave-valor.
diccionario_auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2022
}

print("--- ÍTEM 1: Mostrar Estructuras ---")
print("Lista:", lista_compras)
print("Tupla:", tupla_coordenadas)
print("Conjunto:", conjunto_id)
print("Diccionario:", diccionario_auto)
print() # Espacio en blanco para ordenar la terminal

# Diferencias principales:
# La Lista es modificable; la Tupla protege los datos; el Conjunto no permite 
# repetidos; y el Diccionario asocia datos a través de etiquetas (claves).


# ---------------------------------------------------------
# ÍTEM 2: ACCEDER A ELEMENTOS
# ---------------------------------------------------------
print("--- ÍTEM 2: Acceder a Elementos ---")
# Imprime el segundo elemento de la lista (índice 1)
print(f"Segundo elemento de la lista: {lista_compras[1]}")

# Imprime una clave y su valor desde el diccionario
print(f"La marca del auto es: {diccionario_auto['marca']}")
print()

# ¿Por qué no puedes acceder por índice a un set?
# RESPUESTA: Porque los conjuntos (sets) son estructuras desordenadas. 
# Sus elementos no tienen una posición fija asignada, por lo tanto, 
# no existe un índice [0] o [1] al cual llamar.


# ---------------------------------------------------------
# ÍTEM 3: CONTAR E ITERAR
# ---------------------------------------------------------
print("--- ÍTEM 3: Contar e Iterar ---")
# Usa len() para mostrar la cantidad de elementos
print(f"Cantidad en la lista: {len(lista_compras)}")
print(f"Cantidad en la tupla: {len(tupla_coordenadas)}")
print(f"Cantidad en el conjunto: {len(conjunto_id)}")
print(f"Cantidad en el diccionario: {len(diccionario_auto)}")
print()

# Itera sobre cada estructura usando un for
print("Iterando la lista:")
for item in lista_compras:
    print(f"- {item}")

print("Iterando la tupla:")
for item in tupla_coordenadas:
    print(f"- {item}")

print("Iterando el conjunto:")
for item in conjunto_id:
    print(f"- {item}")

print("Iterando el diccionario:")
for clave, valor in diccionario_auto.items():
    print(f"- {clave}: {valor}")
print()


# ---------------------------------------------------------
# ÍTEM 4: MODIFICAR ESTRUCTURAS
# ---------------------------------------------------------
print("--- ÍTEM 4: Modificar Estructuras ---")

# Agrega un nuevo elemento a la lista y al conjunto
lista_compras.append("café")
conjunto_id.add(104)

# Borra un elemento de la lista
lista_compras.remove("leche")

# Agrega una nueva clave al diccionario
diccionario_auto["color"] = "Rojo"

# Intenta modificar la tupla y comenta qué ocurre
try:
    tupla_coordenadas[0] = 50.5 
except TypeError as e:
    # Comentario de lo que ocurre:
    print("Intento de modificar tupla fallido.")
    print(f"Error: {e}")
    print("Explicación: Las tuplas son inmutables, Python bloquea cualquier cambio una vez creadas.")

print("\nEstructuras después de las modificaciones:")
print("Lista final:", lista_compras)
print("Conjunto final:", conjunto_id)
print("Diccionario final:", diccionario_auto)