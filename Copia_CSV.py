import subprocess
import pandas as pd
import csv

def es_flotante(n):
    n=str(n)
    pi=n.find(".")
    if pi == -1:
        return False
    return pi is n.rfind(".")
        

def copia_csv():
    
    data=pd.read_csv('TotalesNacionales_T.csv',header=0) 
    aux0=data[["Casos totales","Casos recuperados","Casos activos","Casos nuevos totales"]]
    diccionario={"Casos totales":[],"Casos recuperados":[],"Casos activos":[],"Casos nuevos totales":[]}
    for i in (range(len(aux0["Casos totales"]))):
        aux1=aux0["Casos totales"][i]
        if es_flotante(aux1) is True:
            aux1=int(aux1)
            diccionario["Casos totales"].append(aux1)
    for i in (range(len(aux0["Casos recuperados"]))):
        aux2=aux0["Casos recuperados"][i]
        if es_flotante(aux2) is True:
            aux2=int(aux2)
            diccionario["Casos recuperados"].append(aux2)
    
    for i in (range(len(aux0["Casos activos"]))):
        aux3=aux0["Casos activos"][i]
        if es_flotante(aux3) is True:
            aux3=int(aux3)
            diccionario["Casos activos"].append(aux3)
    
    for i in (range(len(aux0["Casos nuevos totales"]))):
        aux4=aux0["Casos nuevos totales"][i]
        if es_flotante(aux4) is True:
            aux4=int(aux4)
            diccionario["Casos nuevos totales"].append(aux4)
    subprocess.call("touch data.csv",shell=True)
    
    (pd.DataFrame.from_dict(data=diccionario, orient='index').to_csv('data.csv', header=False))
    
    datap = pd.read_csv('data.csv',header=0) 
    print(datap)

copia_csv()
    
