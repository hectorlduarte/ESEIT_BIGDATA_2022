import numpy as np
import argparse

def calcular_suma(lista_numeros):
    """Calcular la suma de una lista de numero

    Args:
        lista_numeros (lista): Lista números con valores enteros

    Returns:
        tupla: suma
    """
    resultado = np.sum(lista_numeros)
    
    return resultado

def calcular_valores_centrales(lista_numeros):
    media = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)
    
    return media, dev_std

def calcular_extremos(lista_numeros):
    min_val = np.min(lista_numeros)
    max_val = np.max(lista_numeros)

    return min_val, max_val

def calcular_valores(lista_numeros):
    suma = calcular_suma(lista_numeros)
    media, dev_std = calcular_valores_centrales(lista_numeros)
    min_val, max_val = calcular_extremos(lista_numeros)

    return suma, media, dev_std, min_val, max_val 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", type=int, default=1, help="para decidir si imprime informe")
    
    parser.parse_args()

    arg = parser.parse_args()
    verbose = arg.verbose
    
    lista_numeros = [1, 5, 8, 3, 45, 93]
    suma, media, dev_std, min_val, max_val = calcular_valores(lista_numeros, verbose)
    print (suma, media, dev_std, min_val, max_val)

    print('DONE!!!')

if __name__ == '__main__':
    main()