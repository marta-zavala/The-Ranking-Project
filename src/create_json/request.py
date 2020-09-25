import requests
import json
import os
import re
from dotenv import load_dotenv
import pandas as pd
from regexfunctions import *
load_dotenv()

# Creo la funcion para hacer la request a la API de github
def getpulls(num,token= os.getenv("TOKEN")):
    headers = {"Authorization": f"token {token}"}
    res=requests.get(f'https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls/{num}',headers=headers)
    if res.status_code == 404:
        return 'exit'
    
    comment=requests.get(f'https://api.github.com/repos/ironhack-datalabs/datamad0820/issues/{num}/comments',headers=headers)
    data=res.json()
    comment=comment.json()
    return{
        'Id':data['number'],
        'User':data['user']['login'],
        'User 2':user2(comment),
        'User 3':user3(comment),
        'Instructor':instructor(comment),
        'Lab':lab(data['title']),
        'State':data['state'],
        'Open':data['created_at'],
        'Closed':data['closed_at'],
        'Url': url(comment),
        'Grade':grade(comment)
    }   

# Creo un bucle para realizar todas las requests. 
# En el bucle incluyo un pass, para que no se guarde info de una pull request inexistente (si se pone break para nantes de tiempo, ya que hay un rango en el que no existen pull requests)
data=[]
for i in range (1,800):
    if getpulls(i)=='exit':
        pass
    else:
        data.append(getpulls(i))


# Convierto mis datos a json para importarlos a MongoDB
jsn = pd.DataFrame(data)
jsn.to_json('output/pull.json',orient="records")


# Importo los datos en MongoDb por la terminal: ~mongoimport -d <NombreBBDD> -c <Coleccion> --jsonArray <archivo.json>
