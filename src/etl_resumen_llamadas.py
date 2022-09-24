# pseudo código
# mai()
#   datos = get_data(filename)
#   reporte = generate_report(datos)
#   save_data(reporte)
import os
import pandas as pd
from pathlib import Path, PosixPath

root_dir = Path('.').resolve()

def get_data(filename):
 #   root_dir = Path('.').resolve().parent
    
    data_dir = "Data"
    file_path = os.path.join(root_dir, "ESEIT_BIGDATA_2022", data_dir, filename)
    file_path

    datos = pd.read_csv(file_path, sep=";", encoding="latin-1")
    print('get_data')
    print('La tabla contiene', datos.shape[0], 'filas', datos.shape[1], 'Columnas')

    return datos

def generate_report(datos):
    # Crear un diccionario vacio
    dict_resumen = dict()

# loop para llamar el diccionario de columnas con valores únicos
    for col in datos.columns:
        valores_unicos = datos[col].unique()
        n_valores = len(valores_unicos)
        dict_resumen[col] = n_valores
    
    reporte = pd.DataFrame.from_dict(dict_resumen)

def main():
    filename = 'llamadas123_julio_2022.csv' 
    datos = get_data(filename)

    print (datos)

    return 

if __name__ == '__main__':
    main