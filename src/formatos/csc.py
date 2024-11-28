class FormatoCSC:
    def __init__(self, valores, filas, p_columnas, shape):
        self.valores = valores
        self.filas = filas
        self.p_columnas = p_columnas
        self.shape = shape

    def obtener_elemento(self, i, j):
        start = self.p_columnas[j]
        end = self.p_columnas[j + 1]
        for index in range(start, end):
            if self.filas[index] == i:
                return self.valores[index]
        return 0

    def __str__(self):
        valores_int = [int(valor) for valor in self.valores]
        return f"MATRIZ EN FORMATO CSC\nvalores: {valores_int}\nfilas: {self.filas}\nPivote de las Columnas: {self.p_columnas}"
