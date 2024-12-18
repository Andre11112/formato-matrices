class FormatoCSR:
    def __init__(self, valores, columnas, p_filas, shape):
        self.valores = valores
        self.columnas = columnas
        self.p_filas = p_filas
        self.shape = shape

    def obtener_elemento(self, i, j):
        start = self.p_filas[i]
        end = self.p_filas[i + 1]
        for index in range(start, end):
            if self.columnas[index] == j:
                return self.valores[index]
        return 0

    def obtener_fila(self, i):
        return [self.obtener_elemento(i, j) for j in range(self.shape[1])]

    def obtener_columna(self, j):
        return [self.obtener_elemento(i, j) for i in range(self.shape[0])]

    def __str__(self):
        valores_str = [int(v) if v.is_integer() else v for v in self.valores]
        return f"Formato CSR: {valores_str}, {self.columnas}, {self.p_filas}"