import pandas as pd
import csv


def copia_csv(file):
    
    data=pd.read_csv(file,header=0) 
    aux0=data[["Casos totales acumulados","Fallecidos confirmados totales","Fallecidos sospechosos probables u otros totales","Fallecidos totales","Casos confirmados recuperados","Casos confirmados por antigeno","Casos con sospecha de reinfeccion","Casos probables acumulados","Casos activos probables","Casos nuevos totales","Casos nuevos con sintomas","Casos nuevos sin sintomas*","Casos nuevos reportados por laboratorio","Casos nuevos confirmados por antigeno","Casos activos confirmados"]]
    aux0 = aux0.fillna(0)
    new_data = []
    #for i in (range(len(aux0["Casos totales"]))):
    diccionario = {}
        
    aux1=aux0["Casos totales acumulados"][10]
    aux2=aux0["Fallecidos confirmados totales"][10]
    aux3=aux0["Fallecidos sospechosos probables u otros totales"][10]
    aux4=aux0["Fallecidos totales"][10]
    aux5=aux0["Casos confirmados recuperados"][10]
    aux6=aux0["Casos confirmados por antigeno"][10]
    aux7=aux0["Casos con sospecha de reinfeccion"][10]
    aux8=aux0["Casos probables acumulados"][10]
    aux9=aux0["Casos activos probables"][10]
    aux10=aux0["Casos nuevos totales"][10]
    aux11=aux0["Casos nuevos con sintomas"][10]
    aux12=aux0["Casos nuevos sin sintomas*"][10]
    aux13=aux0["Casos nuevos reportados por laboratorio"][10]
    aux14=aux0["Casos nuevos confirmados por antigeno"][10]
    aux15=aux0["Casos activos confirmados"][10]
    
    aux1=int(aux1)
    aux2=int(aux2)
    aux3=int(aux3)    
    aux4=int(aux4)
    aux5=int(aux5)
    aux6=int(aux6)
    aux7=int(aux7)
    aux8=int(aux8)
    aux9=int(aux9)
    aux10=int(aux10)
    aux11=int(aux11)
    aux12=int(aux12)
    aux13=int(aux13)
    aux14=int(aux14)
    aux15=int(aux15)

    diccionario["Casos totales acumulados"] = aux1
    diccionario["Casos recuperados"] = aux2
    diccionario["Casos activos"] = aux3
    diccionario["Casos nuevos totales"] = aux4
    diccionario["Casos confirmados recuperados"]= aux5
    diccionario["Casos confirmados por antigeno"]= aux6
    diccionario["Casos con sospecha de reinfeccion"]= aux7
    diccionario["Casos probables acumulados"]= aux8
    diccionario["Casos activos probables"]= aux9
    diccionario["Casos nuevos totales"]= aux10
    diccionario["Casos nuevos con sintomas"]= aux11
    diccionario["Casos nuevos sin sintomas*"]= aux12
    diccionario["Casos nuevos reportados por laboratorio"]= aux13
    diccionario["Casos nuevos confirmados por antigeno"]= aux14
    diccionario["Casos activos confirmados"]= aux15
    new_data.append(diccionario)
    
    with open('datosc19.csv', 'w') as f:
        w = csv.DictWriter(f, new_data[0].keys())
        w.writeheader()
        for diccionario in new_data:
            w.writerow(diccionario)
    
