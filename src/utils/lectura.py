def leer_matriz_archivo(nombre_archivo):
    """Lee una matriz desde un archivo de texto y la devuelve como una lista de listas."""
    with open(nombre_archivo, 'r') as f:
        lineas = f.readlines()
        matriz = []
        for linea in lineas:
            fila = [float(x) for x in linea.strip().split()]
            matriz.append(fila)
    return matriz

