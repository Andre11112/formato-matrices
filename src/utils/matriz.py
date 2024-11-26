from src.formatos.coo import FormatoCOO

def matriz_a_coo(matriz):
    valores = []
    filas = []
    columnas = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:  
                valores.append(matriz[i][j])
                filas.append(i)
                columnas.append(j)
    
    return FormatoCOO(valores, filas, columnas, (len(matriz), len(matriz[0]) )) 