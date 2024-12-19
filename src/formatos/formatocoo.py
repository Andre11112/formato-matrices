"""
Esta es la implemntacion del formato COO para matrices.
guardamos los valores diferentes de cero junto con sus posiciones fila,columna
"""

class FormatoCOO:
    def __init__(self, valores, filas, columnas, shape):
        self.valores = valores
        self.filas = filas
        self.columnas = columnas
        self.shape = shape

    """
    metodo para obtener el elemento de la matriz en la posicion i,j
    si encuentra el elemento, retorna el valor, si no, retorna 0
    """   

    def obtener_elemento(self, i, j):
        for index in range(len(self.filas)):
            if self.filas[index] == i and self.columnas[index] == j:
                return self.valores[index]
        return 0

    def obtener_fila(self, i):
        """da la la fila i va elemnto por elemento"""
        return [self.obtener_elemento(i, j) for j in range(self.shape[1])]

    def obtener_columna(self, j):
        """devuelve la fila j va elemento por elemenento"""
        return [self.obtener_elemento(i, j) for i in range(self.shape[0])]

    
    def __str__(self):
        """print al formato de manera organizada """
        
        valores_int = [int(valor) for valor in self.valores]
        return f"MATRIZ EN FORMATO COO\nvalores: {valores_int}\nfilas: {self.filas}\ncolumnas: {self.columnas}"
