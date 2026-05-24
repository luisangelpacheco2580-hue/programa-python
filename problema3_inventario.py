## Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación
# Código del curso: 213022
# Fase 5 - Evaluación Final POA

# Estudiante: Luis Angel Pacheco Pushaina
# Grupo: 213022_162
# Programa: Ingeniería de Sistemas

# Problema seleccionado:
# Problema 3 - Control de inventario y reabastecimiento

# Código fuente de autoría propia
#  -------------------------------------------------
# Nombre: Luis Angel Pacheco Pushaina
# Curso: Fundamentos de Programación
# Código curso: 213022
# Actividad: Fase 5 - Evaluación Final POA
# Problema seleccionado: Problema 3 - Inventario
# -------------------------------------------------
inventario = [
    ["A101", "Teclado", 5, 10],
    ["A102", "Mouse", 15, 10],
    ["A103", "Monitor", 3, 8],
    ["A104", "Impresora", 7, 7],
    ["A105", "Parlantes", 2, 6]
]
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0

    return cantidad_pedir
print("\n--- REPORTE DE INVENTARIO ---")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("\n--------------------------------")
    print(f"Código: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")
    print(f"Cantidad a pedir: {cantidad_pedir}")

