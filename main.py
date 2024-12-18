import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.lectura import leer_matriz_archivo
from src.utils.matriz import matriz_a_coo, matriz_a_csc, matriz_a_csr


def menu_principal():
    csc = None
    coo = None
    csr = None

    while True:
        print("\n=== MENÚ MATRICES DISPERSAS ===")
        print("1. Cargar matriz desde archivo")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '1':
            nombre_archivo = input("Ingrese el nombre del archivo de la matriz: ")
            #aqui esta la ruta con las carptas para solo poner el nombre
            nombre_archivo = os.path.join('src', 'matrices_txt', nombre_archivo + '.txt') 
            matriz = leer_matriz_archivo(nombre_archivo)
            
            while True:
                print("\nSeleccione el formato para mostrar la matriz:")
                print("1. Formato COO")
                print("2. Formato CSC")
                print("3. Formato CSR")
                print("4. Volver al menú principal")
                
                formato_opcion = input("\nSeleccione una opción: ")
                
                if formato_opcion == '1':
                    coo = matriz_a_coo(matriz)
                    print(coo)
                    formato_seleccionado = coo
                elif formato_opcion == '2':
                    csc = matriz_a_csc(matriz)
                    print(csc)
                    formato_seleccionado = csc
                elif formato_opcion == '3':
                    csr = matriz_a_csr(matriz)
                    print(csr)
                    formato_seleccionado = csr
                elif formato_opcion == '4':
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
                    continue

                # Mostrar opciones para obtener elementos, filas y columnas
                while True:
                    print("\nSeleccione una opción:")
                    print("1. Obtener elemento (i, j)")
                    print("2. Obtener fila (i)")
                    print("3. Obtener columna (j)")
                    print("4. Volver a seleccionar formato")
                    
                    opcion_detalle = input("\nSeleccione una opción: ")
                    
                    if opcion_detalle == '1':
                        i = int(input("Ingrese el índice de la fila (i): "))
                        j = int(input("Ingrese el índice de la columna (j): "))
                        print(f"Elemento en ({i}, {j}): {formato_seleccionado.obtener_elemento(i, j)}")
                    elif opcion_detalle == '2':
                        i = int(input("Ingrese el índice de la fila (i): "))
                        print(f"Fila {i}: {formato_seleccionado.obtener_fila(i)}")
                    elif opcion_detalle == '3':
                        j = int(input("Ingrese el índice de la columna (j): "))
                        print(f"Columna {j}: {formato_seleccionado.obtener_columna(j)}")
                    elif opcion_detalle == '4':
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")

        elif opcion == '2':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal() 