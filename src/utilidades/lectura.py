def leer_matriz_archivo(nombre_archivo):
    #le el archivo txt y lo retorna como una lista de listas de
    #todos los numeros que se leeyeron en la matiz  en el txxt
    with open(nombre_archivo, 'r') as f:
        lineas = f.readlines()
        matriz = []
        for linea in lineas:
            fila = [float(x) for x in linea.strip().split()]
            matriz.append(fila)
    return matriz

