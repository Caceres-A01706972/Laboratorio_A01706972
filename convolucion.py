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

pad_height = int((kernel_fila - 1)/2)
pad_width = int((kernel_columna -1)/2)

padded_image = np.zeros((imagen_fila + (2 * pad_height), imagen_columna + (2 * pad_width)))

padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = imagen

for fila in range(imagen_fila):
    for columna in range(imagen_columna):
        final[fila, columna] = convolucion(imagen[fila:fila + kernel_fila,columna:columna + kernel_columna], kernel)
print(final)