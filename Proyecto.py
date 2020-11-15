from GitImport import instalador # importe de la funcion que obtiene la base de datos actualizada
import pandas as pd
import subprocess

def existe_data():
    aux0=subprocess.call('find TotalesNacionales_T.csv',shell=True)
    return aux0

def lector_data():
    aux0=existe_data()
    if aux0 == 1:
        instalador()
        data = lector_data()
        return data
    data = pd.read_csv('TotalesNacionales_T.csv',header=0) 
    return data

def porcentual(data):

    lista_porcentajes= []
    for i in (range(len(data['Casos nuevos totales'])-1)):
        
        actual= data['Casos nuevos totales'][i+1]
        anterior= data['Casos nuevos totales'][i]

        if anterior == 0:
            lista_porcentajes.append(((anterior-actual)/actual)*-1)

        else:
            porcentual= ((actual-anterior)/anterior)

            lista_porcentajes.append(round(porcentual,4))
            
    variaciones= {'porcentajes': lista_porcentajes}
    return variaciones


if __name__ == '__main__':
    data = lector_data()

    variaciones= porcentual(data)
    print(variaciones)
    
    
