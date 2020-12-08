
##importando os verbos do corpus de dev(sygmorph)

import pandas as pd
import json

verbos = pd.read_excel("./corpus/corpora_train_dev_test/verbos_dev.xlsx")
# verbos.head()
lemas = list(verbos.iloc[:]["lema"])


##TRATAR VALORES NaN

import numpy as np
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy='constant', fill_value=None,verbose=0)
imputer = imputer.fit(verbos)
verbos = imputer.transform(verbos)


pessoa_genero = list(set(verbos[:,3]))
modo = list(set(verbos[:,5]))
numero=list(set(verbos[:,4]))
tempo=list(set(verbos[:,6]))
aspecto=list(set(verbos[:,7]))

# concatenaAtributos = []
# for i in range(len(verbos)):
# 	concatenaAtributos.append(verbos[i,5] + '_' + verbos[i,6]+'_'+verbos[i,7])
# concatenaAtributos=list(set(concatenaAtributos))

def experimento_verbo(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,pessoa_genero, numero, modo, tempo, aspecto):

	if numero == 'PL':
		OI_numero = 'plural'
	elif numero == 'SG':
		OI_numero = 'singular'
	else:
		OI_numero = None

	if pessoa_genero == 1:
		OI_tipo_de_pessoa = '1pessoa'
		genero = None

	elif pessoa_genero == 2:
		OI_tipo_de_pessoa = '2pessoa'
		genero = None

	elif pessoa_genero == 3:
		OI_tipo_de_pessoa = '3pessoa'
		genero = None

	elif pessoa_genero == 'MASC':
		genero = 'masculino'
		OI_tipo_de_pessoa = None

	elif pessoa_genero == 'FEM':
		genero = 'feminino'
		OI_tipo_de_pessoa = None
	elif pessoa_genero == 'PRS' or pessoa_genero == 'NFIN':
		genero = None
		OI_tipo_de_pessoa = None

####
	if modo + '_' + tempo + '_' + aspecto == 'IND_PST_PFV':
		tipo_de_orientacao = 'pret�rito_perfectivo_I'
	elif modo + '_' + tempo + '_' + aspecto == 'IND_PST_PRF':
		tipo_de_orientacao = 'pret�rito_perfectivo_II'
	elif modo + '_' + tempo + '_' + aspecto == 'IND_PST_IPFV':
		tipo_de_orientacao = 'pret�rito_imperfectivo'
	elif modo + '_' + tempo + '_' + aspecto == 'IND_FUT_missing_value':
		tipo_de_orientacao = 'futuro'
	elif modo + '_' + tempo + '_' + aspecto == 'IND_PRS_missing_value':
		tipo_de_orientacao = 'presente'
	elif modo + '_' + tempo + '_' + aspecto == 'SBJV_PRS_missing_value':
		tipo_de_orientacao = 'subjuntivo_conjuntivo'
	elif modo + '_' + tempo + '_' + aspecto == 'SBJV_PST_IPFV':
		tipo_de_orientacao = 'subjuntivo_condicional'
	elif modo + '_' + tempo + '_' + aspecto == 'SBJV_FUT_missing_value':
		tipo_de_orientacao = 'subjuntivo_optativo'
	elif modo + '_' + tempo + '_' + aspecto == 'PST_missing_value_missing_value':
		tipo_de_orientacao = 'partic�pio'
	elif modo + '_' + tempo + '_' + aspecto == 'IMP_POS_missing_value':
		tipo_de_orientacao = 'imperativo_I'
	elif modo + '_' + tempo + '_' + aspecto == 'IMP_NEG_missing_value':
		tipo_de_orientacao = 'imperativo_II'
	elif modo + '_' + tempo + '_' + aspecto == 'COND_missing_value_missing_value':
		tipo_de_orientacao = 'passado_volitivo'
	elif modo + '_' + tempo + '_' + aspecto == 'NFIN_missing_value_missing_value':
		tipo_de_orientacao = 'n�o_finito_concretizado'
	elif numero+'_'+modo + '_' + tempo + '_' + aspecto == 'missing_value_missing_value_missing_value_missing_value':
		tipo_de_orientacao = 'ger�ndio'
	elif numero+'_'+modo + '_' + tempo + '_' + aspecto == 'NFIN_missing_value_missing_value_missing_value':
		tipo_de_orientacao = 'ger�ndio'
	verbo = verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,
		            tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa,
		            padrao_pessoa_morfologia="Morfologia_padr�o")

	return verbo


# experimento_verbo("Fazer",'Evento',"mistificar",'PRS',"missing_value","missing_value","missing_value","missing_value")



verbo =  verbos[1,0]
pessoa_genero = verbos[1,3]
modo = verbos[:,5]
numero=verbos[:,4]
tempo=verbos[:,6]
aspecto=verbos[:,7]

lista_conjugados=[]
for i in range(len(verbos)):
	verbo = verbos[i, 0]
	pessoa_genero = verbos[i, 3]
	modo = verbos[i, 5]
	numero = verbos[i, 4]
	tempo = verbos[i, 6]
	aspecto = verbos[i, 7]
	verbo_conj = experimento_verbo("Fazer",'Evento',verbo,pessoa_genero,numero,modo,tempo,aspecto)
	lista_conjugados.append(verbo_conj)

contador = 0
erros = []
acertos=[]
for i in lista_conjugados:
	if i not in verbos[:,1]:
		erros.append(i)
	else:
		acertos.append(i)
	contador+=1
'desfraldamos'in  verbos[:,1]

#presente
# print("A conjuga��o �:")
dict_presente = {}
for lema in lemas:
	conjugacao = []
	dict_presente.update({lema:conjugacao})
	for numero in OI_numeros:
		for tipo_pessoa in OI_tipo_pessoas:
			verbo = verbo_geral("Fazer",'Evento',lema,"presente",numero,None,tipo_pessoa)
			conjugacao.append(verbo)

# Serializing json
json_object = json.dumps(dict_presente, indent=4)

# Writing to sample.json
with open("./corpus/corpora_train_dev_test/dicionario_presente.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)

