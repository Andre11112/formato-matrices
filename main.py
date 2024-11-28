import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.lectura import leer_matriz_archivo
from src.utils.matriz import matriz_a_coo, matriz_a_csc


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
            
            while True:
                print("\nSeleccione el formato para mostrar la matriz:")
                print("1.Formato COO")
                print("2.Formato CSC")
                print("3.Volver al menú principal")
                
                formato_opcion = input("\nSeleccione una opción: ")
                
                if formato_opcion == '1':
                    coo = matriz_a_coo(matriz)
                    print(coo)
                elif formato_opcion == '2':
                    csc = matriz_a_csc(matriz)
                    print(csc)
                elif formato_opcion == '3':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal() 