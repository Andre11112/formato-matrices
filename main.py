import sys
import os

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.lectura import leer_matriz_archivo
from src.utils.matriz import matriz_a_coo

def menu_principal():
    while True:
        print("\n=== MENÚ MATRICES DISPERSAS ===")
        print("1. Cargar matriz desde archivo")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            nombre_archivo = input("Ingrese el nombre del archivo de la matriz: ")
            #aqui añadimos la ruta con las carptas para solo poner el nombre
            nombre_archivo = os.path.join('src', 'matrices_txt', nombre_archivo + '.txt') 
            matriz = leer_matriz_archivo(nombre_archivo)
            coo = matriz_a_coo(matriz)
            print(coo)
        
        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal() 