import numpy as np

def convolucion(fragmento, kernel):
    frag_fila, frag_columna = fragmento.shape
    resultado = 0
    for fila in range(frag_fila):
        for columna in range(frag_columna):
            resultado += fragmento[fila, columna] * kernel[fila, columna]
    return resultado

imagen = np.array([[4, 0, 2, 1, 8, 3],
                  [11, 2, 2, 1, 5, 9],
                  [3, 3, 1, 6, 6, 8],
                  [1, 1, 7, 7, 2, 4],
                  [1, 3, 2, 1, 2, 3]])

kernel = np.array([[1, 1, 1],
                   [0, 0, 0],
                   [2, 10, 3]])

imagen_fila, imagen_columna = imagen.shape
kernel_fila, kernel_columna = kernel.shape

final = np.zeros(imagen.shape)

for fila in range(imagen_fila):
    for columna in range(imagen_columna):
        final[fila, columna] = convolucion(imagen[fila:fila + kernel_fila,columna:columna + kernel_columna], kernel)
print(final)