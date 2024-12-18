from src.formatos.formatocoo import FormatoCOO
from src.formatos.formatocsc import FormatoCSC
from src.formatos.formatocsr import FormatoCSR

"""
metodo para convertir una matriz a formato COO
"""
def matriz_a_coo(matriz):
    valores = []
    filas = []
    columnas = []

    """
    se recorre la matriz y se guardan los valores, filas y columnas en las listas
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:  
                valores.append(matriz[i][j])
                filas.append(i)
                columnas.append(j)
    
    return FormatoCOO(valores, filas, columnas, (len(matriz), len(matriz[0]) )) 

"""
metodo para convertir una matriz a formato CSC
"""
def matriz_a_csc(matriz):
    valores = []
    filas = []
    p_columnas = [0]
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if num_filas > 0 else 0

    """
    se recorre la matriz y se guardan los valores, filas y columnas en las listas
    """
    for j in range(num_columnas):
        for i in range(num_filas):
            if matriz[i][j] != 0:
                valores.append(matriz[i][j])
                filas.append(i)
        p_columnas.append(len(valores))

    return FormatoCSC(valores, filas, p_columnas, (num_filas, num_columnas)) 

"""
metodo para convertir una matriz a formato CSR
"""
def matriz_a_csr(matriz):
    valores = []
    columnas = []
    p_filas = [0]
    num_filas = len(matriz)
    num_columnas = len(matriz[0]) if num_filas > 0 else 0
    
    """
    se recorre la matriz y se guardan los valores, columnas en las listas
    los indices de las columnas se guardan en la lista columnas
    los indices de las filas se guardan en la lista p_filas
    
    """
    for i in range(num_filas):
        for j in range(num_columnas):
            if matriz[i][j] != 0:
                valores.append(matriz[i][j])
                columnas.append(j)
        p_filas.append(len(valores))
    
    return FormatoCSR(valores, columnas, p_filas, (num_filas, num_columnas)) 

    

