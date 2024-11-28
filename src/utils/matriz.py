from src.formatos.coo import FormatoCOO
from src.formatos.csc import FormatoCSC

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

def matriz_a_csc(matriz):
    valores = []
    filas = []
    p_columnas = [0]
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if num_filas > 0 else 0

    for j in range(num_columnas):
        for i in range(num_filas):
            if matriz[i][j] != 0:
                valores.append(matriz[i][j])
                filas.append(i)
        p_columnas.append(len(valores))

    return FormatoCSC(valores, filas, p_columnas, (num_filas, num_columnas)) 