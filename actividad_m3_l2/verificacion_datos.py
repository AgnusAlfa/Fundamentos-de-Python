# ACTIVIDAD N° 2: TIPOS DE DATOS

# 1. DEFINICIÓN DE LISTAS INICIALES
a = [5, 1, 4, 9, 0]
b = list(range(3, 10)) + list(range(20, 23)) 
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]

print("--- RESULTADOS DE LA ACTIVIDAD ---")

# Función auxiliar para imprimir con formato profesional
def verificar(expresion_str, resultado):
    print(f"Expresión: {expresion_str}")
    print(f"Resultado: {resultado}")
    print(f"Tipo:      {type(resultado)}")
    print("-" * 30)

# 2. VERIFICACIÓN DE EXPRESIONES

verificar("a[2]", a[2])
verificar("b[9]", b[9])
verificar("c[1][2]", c[1][2])
verificar("e[0] == e[1]", e[0] == e[1])
verificar("len(c)", len(c))
verificar("len(c[0])", len(c[0]))
verificar("len(e)", len(e))
verificar("c[-1]", c[-1])
verificar("c[-1][+1]", c[-1][+1])
verificar("c[2:] + d[2:]", c[2:] + d[2:])
verificar("a[3:10]", a[3:10])
verificar("a[3:10:2]", a[3:10:2])
verificar("d.index('jirafa')", d.index('jirafa'))
verificar("e[c[0][1]].count(5)", e[c[0][1]].count(5))
verificar("sorted(a)[2]", sorted(a)[2])
verificar("complex(b[0], b[1])", complex(b[0], b[1]))