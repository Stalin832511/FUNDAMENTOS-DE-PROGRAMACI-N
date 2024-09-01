# Definir la matriz bidimensional de 3x3
matriz = [
    [9, 2, 4],
    [6, 5, 1],
    [3, 8, 7]
]

# Función para ordenar una fila específica de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila):
    for i in range(len(matriz[fila])):
        for j in range(len(matriz[fila]) - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiar los elementos si están en el orden incorrecto
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Ordenar la fila 1 (segunda fila)
fila_a_ordenar = 1
ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
