"""
Implementacion del formato CSR para matrices dispersas.
almacena valores no cero por filas, usando punteros para indicar inicio y fin de cada fila
"""

class FormatoCSR:
    def __init__(self, valores, columnas, p_filas, shape):
        self.valores = valores
        self.columnas = columnas
        self.p_filas = p_filas
        self.shape = shape

    def obtener_elemento(self, i, j):
        """obtiene el elemento en la posición i y j de la matriz"""
        start = self.p_filas[i]
        end = self.p_filas[i + 1]
        for index in range(start, end):
            if self.columnas[index] == j:
                return self.valores[index]
        return 0

    def obtener_fila(self, i):
        """nos da toda la fila i va elemento por elemento"""
        return [self.obtener_elemento(i, j) for j in range(self.shape[1])]

    def obtener_columna(self, j):
        """nos da toda la columna j va elemento por elemento"""
        return [self.obtener_elemento(i, j) for i in range(self.shape[0])]

    def __str__(self):
        """mostrar la matriz de manera organizada en consola"""
        valores_int = [int(valor) for valor in self.valores]
        return f"MATRIZ EN FORMATO CSR\nvalores: {valores_int}\nPivote de las filas: {self.p_filas}\nPivote de las Columnas: {self.columnas}"