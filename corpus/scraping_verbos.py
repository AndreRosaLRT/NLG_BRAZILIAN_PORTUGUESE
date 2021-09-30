#Importa a biblioteca usada para carregar o website
import requests
from numpy.lib.user_array import container
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook
from time import sleep
from random import randint

verbos_web=[]

for pg in np.arange(1,51,1):
    pagina = requests.get('https://www.conjugacao.com.br/verbos-populares/'+str(pg)+'/').text
    soup = BeautifulSoup(pagina,features="html.parser_me_mi")
    verb_div = soup.find_all('div',class_='wrapper')
    for container in verb_div:
        i = 0
        for i in range(len(container.contents[1])):
            verbos_web.append(container.find('ul').find_all('li')[i].text)
        i += 1

##separa��o em dados para dev e teste
verbos_web_array=np.array(verbos_web)
from sklearn.model_selection import train_test_split
verbos_web_dev, verbos_web_teste = train_test_split(verbos_web_array, test_size=0.25, random_state=0)


##SALVANDO CSV
#dev
pd.DataFrame(verbos_web_dev).to_excel("./corpus/verbos_web_dev.xlsx")
#test
pd.DataFrame(verbos_web_teste).to_excel("./corpus/verbos_web_teste.xlsx")

#
# # Serializing json DEV
# import json
# json_object=json.dumps(list(verbos_web_dev), ensure_ascii=False)
# # Writing to sample.json
# with open("./corpus/verbos_web_dev.json", "w",) as outfile:
#     outfile.write(json_object)
#
#
# # Serializing json TESTE
#
# json_object=json.dumps(list(verbos_web_teste), ensure_ascii=False)
# # Writing to sample.json
# with open("./corpus/verbos_web_teste.json", "w",) as outfile:
#     outfile.write(json_object)
