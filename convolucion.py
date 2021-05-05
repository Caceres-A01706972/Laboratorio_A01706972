m = [[12,7,3],
    [4,5,6],
    [7,8,9]]

kernel = [[5,8,1],
        [6,1,2],
        [4,1,1]]

resultado = [[0,0,0],
            [0,0,0],
            [0,0,0]]

#Iteramos sobre las filas de m
for i in range(len(m)):
    #Iteramos sobre las columnas de kernel
    for j in range(len(kernel[0])):
        #Iteramos sobre las filas de kernel
        for k in range(len(kernel)):
            resultado[i][j] += m[i][k] * kernel[k][j]

for r in resultado:
    print(r)

