class FormatoCOO:
    def __init__(self, valores, filas, columnas, shape):
        self.valores = valores
        self.filas = filas
        self.columnas = columnas
        self.shape = shape

    def obtener_elemento(self, i, j):
        for index in range(len(self.filas)):
            if self.filas[index] == i and self.columnas[index] == j:
                return self.valores[index]
        return 0

    def __str__(self):
        
        valores_int = [int(valor) for valor in self.valores]
        return f"Valores: {valores_int}\nFilas: {self.filas}\nColumnas: {self.columnas}"
