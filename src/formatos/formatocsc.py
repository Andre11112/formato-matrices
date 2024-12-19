"""
Esta es la implementación del formato CSC para matrices dispersas.
guardamos los valores por columnas 
"""

class FormatoCSC:
    def __init__(self, valores, filas, p_columnas, shape):
        self.valores = valores
        self.filas = filas
        self.p_columnas = p_columnas
        self.shape = shape

    """
    metodo para obtener el elemento de la matriz en la posicion i,j
    se comienza en el pivote de la columna j y se recorre hasta el pivote de la columna j+1
    si encuentra el elemennto, retorna el valor, si no, retorna 0
    """   
    def obtener_elemento(self, i, j):
        start = self.p_columnas[j]
        end = self.p_columnas[j + 1]
        for index in range(start, end):
            if self.filas[index] == i:
                return self.valores[index]
        return 0  # Si no lo encuentra, significa que es un cero

    def obtener_fila(self, i):
        """nos da toda la fila i va elemento por elemento"""
        return [self.obtener_elemento(i, j) for j in range(self.shape[1])]

    def obtener_columna(self, j):
        """nos da toda la columna j va elemento por elemento"""
        return [self.obtener_elemento(i, j) for i in range(self.shape[0])]

    def __str__(self):
        """mostrar la matrizde manera organizada en consola"""
        valores_int = [int(valor) for valor in self.valores]
        return f"MATRIZ EN FORMATO CSC\nvalores: {valores_int}\nfilas: {self.filas}\nPivote de las Columnas: {self.p_columnas}"
