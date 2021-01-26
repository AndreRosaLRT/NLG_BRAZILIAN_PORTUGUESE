# -*- coding: utf-8 -*-
##importando os verbos do corpus de dev(sygmorph)


import pandas as pd
import json

verbos = pd.read_excel("./corpus/corpora_train_dev_test/verbos_dev_2.xls")


# verbos.head()
lemas = list(verbos.iloc[:]["lema"])


##TRATAR VALORES NaN

import numpy as np
import sklearn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy='constant', fill_value=None,verbose=0)
imputer = imputer.fit(verbos)
verbos = imputer.transform(verbos)

#
# pessoa_genero = list(set(verbos[:,3]))
# modo = list(set(verbos[:,5]))
# numero=list(set(verbos[:,4]))
# tempo=list(set(verbos[:,6]))
# aspecto=list(set(verbos[:,7]))
#
# concatenaAtributos = []
# for i in range(len(verbos)):
# 	concatenaAtributos.append(str(verbos[i,3]) + '_'+verbos[i,4] + '_'+verbos[i,5] + '_' + verbos[i,6]+'_'+verbos[i,7])
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
		OI_numero=None

####
	if modo + '_' + tempo + '_' + aspecto == 'IND_PST_PFV':
		tipo_de_orientacao = 'pretérito_perfectivo_I'
	elif modo + '_' + tempo + '_' + aspecto == 'IND_PST_PRF':
		tipo_de_orientacao = 'pretérito_perfectivo_II'
	elif modo + '_' + tempo + '_' + aspecto == 'IND_PST_IPFV':
		tipo_de_orientacao = 'pretérito_imperfectivo'
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
		tipo_de_orientacao = 'particípio'
	elif modo + '_' + tempo + '_' + aspecto == 'IMP_POS_missing_value':
		tipo_de_orientacao = 'imperativo_I'
	elif modo + '_' + tempo + '_' + aspecto == 'IMP_NEG_missing_value':
		tipo_de_orientacao = 'imperativo_II'
	elif modo + '_' + tempo + '_' + aspecto == 'COND_missing_value_missing_value':
		tipo_de_orientacao = 'passado_volitivo'
	elif modo + '_' + tempo + '_' + aspecto == 'NFIN_missing_value_missing_value':
		tipo_de_orientacao = 'não_finito_concretizado'
	elif pessoa_genero + '_' + numero + '_' + modo + '_' + tempo + '_' + aspecto == 'PRS_missing_value_missing_value_missing_value_missing_value':
		tipo_de_orientacao = 'gerúndio'
	elif pessoa_genero+'_'+numero + '_' +modo + '_' + tempo + '_' + aspecto == 'NFIN_missing_value_missing_value_missing_value_missing_value':
		tipo_de_orientacao = 'infinitivo'
	verbo = verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,
		            tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)

	return verbo



# verbo_geral('Fazer', 'Evento', 'desfazer','infinitivo',)
#
#
# # experimento_verbo("Fazer",'Evento','assoprar','NFIN')
# experimento_verbo("Fazer",'Evento',"derruir",3,'SG','IND','PST','IPFV')
# experimento_verbo("Sentir",'Evento',"expedir",2,'PL','SBJV','PST','IPFV')
# experimento_verbo("Fazer",'Evento',"estralar",2,'PL','IND','PST','PFV')





#
# verbo =  verbos[1,1]
# pessoa_genero = verbos[1,3]
# modo = verbos[:,5]
# numero=verbos[:,4]
# tempo=verbos[:,6]
# aspecto=verbos[:,7]

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
contador_erros = 0
contador_acertos = 0
erros = []
acertos=[]

for conj in lista_conjugados:
	if conj not in verbos[:,1]:
		erros.append(conj)
		contador_erros+=1
	else:
		acertos.append(conj)
		contador_acertos+=1
	contador+=1

porcertangem_acerto = contador_acertos/1000
porcertangem_acerto*100
# Serializing json

json_object=json.dumps(acertos, ensure_ascii=False)
# Writing to sample.json
with open("./corpus/corpora_train_dev_test/acertos_conjugação_dev.json", "w",) as outfile:
    outfile.write(json_object)


json_object=json.dumps(erros, ensure_ascii=False)
# Writing to sample.json
with open("./corpus/corpora_train_dev_test/erros_conjugação_dev.json", "w",) as outfile:
    outfile.write(json_object)
#


#
# #presente
# # print("A conjugação é:")
# dict_presente = {}
# for lema in lemas:
# 	conjugacao = []
# 	dict_presente.update({lema:conjugacao})
# 	for numero in OI_numeros:
# 		for tipo_pessoa in OI_tipo_pessoas:
# 			verbo = verbo_geral("Fazer",'Evento',lema,"presente",numero,None,tipo_pessoa)
# 			conjugacao.append(verbo)
#
# # Serializing json
# json_object = json.dumps(dict_presente, indent=4)
#
# # Writing to sample.json
# with open("./corpus/corpora_train_dev_test/dicionario_presente.json", "w", encoding="utf-8") as outfile:
#     outfile.write(json_object)

##EXEMPLO TESTE NO DAMATA
import json
sinonimos = json.load(open('./mineração_lexicon/dic_sin_cbow.json'))
#
# verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,
# 		            tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)

TIPO_DE_EXPERIENCIA='Fazer'
funcao_no_grupo_verbal='Evento'
verbo
tipo_de_orientacao='pretérito_perfectivo_I'
OI_numero='singular'
genero=None
OI_tipo_de_pessoa='3pessoa'

texto="Em 25 de março de 2020, o Instituto Nacional de Pesquisas Espaciais(INPE) VP[aspect=simple,tense=past,voice=active,person=3rd,number=singular] registrar alertas de desmatamento de 5.91 km2 na RESERVA EXTRATIVISTA CHICO MENDES/AC."
texto_token = texto.split()
lista_oracao,texto_novo, i =[], [], 0
for token in texto_token:
	if 'VP[' in token:
		indice = texto_token.index(token)
		del texto_token[indice]
		verbo_infinitivo = texto_token[indice]
		if verbo_infinitivo in sinonimos:
			for sinonimo in sinonimos[verbo_infinitivo]:
				texto_token[indice] = verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, sinonimo,tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)
				texto_novo = ' '.join(texto_token)
				lista_oracao.append(texto_novo)

# Serializing json
import codecs

json_object = json.dumps(lista_oracao,  ensure_ascii=False,indent=4)

# Writing to sample.json
path = r'D:/Users/andre/Documents/GitHub/NLG_BRAZILIAN_PORTUGUESE_19-11/corpus/corpora_train_dev_test'
with codecs.open(path + "/teste_DAMATA.json", "w",encoding='utf-8' ) as outfile:
	json.dump(json_object,outfile, ensure_ascii=False)

	outfile.write(json_object)



