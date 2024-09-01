# Definir la matriz bidimensional de 3x3
matriz = [
    [4, 7, 1],
    [8, 5, 2],
    [9, 6, 3]
]

# Definir la función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Retorna la posición si se encuentra el valor
    return None  # Retorna None si el valor no se encuentra

# Valor a buscar en la matriz
valor_a_buscar = int(input("Ingresa el valor a buscar en la matriz: "))

# Llamar a la función y obtener el resultado
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
