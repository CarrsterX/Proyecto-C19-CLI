from GitImport import instalador # importe de la funcion que obtiene la base de datos actualizada
import pandas as pd


def lector_data():
    data = pd.read_csv('activos_vs_recuperados.csv',header=0) 
    return data

if __name__ == '__main__':
    instalador()# funcion generadora de la base de datos 
    data = lector_data()
    print(data['activos'])