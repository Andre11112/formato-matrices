class FormatoCOO:
    """
    constructor de la clase FormatoCOO
    """
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

    """
    metodo para imprimir la matriz en formato COO
    """
    def __str__(self):
        
        valores_int = [int(valor) for valor in self.valores]
        return f"MATRIZ EN FORMATO COO\nvalores: {valores_int}\nfilas: {self.filas}\ncolumnas: {self.columnas}"