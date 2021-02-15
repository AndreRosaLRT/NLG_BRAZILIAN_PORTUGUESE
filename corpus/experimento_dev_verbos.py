# -*- coding: utf-8 -*-


##PRELIMINARES
import pandas as pd
import json
import numpy as np
import sklearn
from sklearn.impute import SimpleImputer
from NLG_BRAZILIAN_PORTUGUESE.GENERATION_dev import *
###FUNCAO EXPERIMENTO
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

##EXEMPLOS
# verbo_geral('Fazer', 'Evento', 'desfazer','infinitivo',)
# #
# experimento_verbo("Fazer",'Evento',"andar",'PRS','missing_value','missing_value','missing_value','missing_value')
# experimento_verbo("Fazer",'Evento',"fazer",1,'PL','IND','PST','PFV')
# experimento_verbo("Sentir",'Evento',"expedir",2,'PL','SBJV','PST','IPFV')
# experimento_verbo("Fazer",'Evento',"extrair",3,'PL','SBJV','PST','IPFV')
# verbo_geral("Fazer",'Evento',"extrair",'subjuntivo_condicional', 'plural', None, '3pessoa')



###################EXPERIMENTO CORPUS DE DESENVOLVIMENTO#################
##importando os verbos do corpus de dev(sygmorph)
verbos = pd.read_excel("./corpus/corpora_train_dev_test/verbos_dev_2.xls")
lemas = list(verbos.iloc[:]["lema"])
##TRATAR VALORES NaN
imputer = SimpleImputer(missing_values = np.nan, strategy='constant', fill_value='missing_value',verbose=0)
imputer = imputer.fit(verbos)
verbos = imputer.transform(verbos)
###
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


###EXPERIMENTO CORPUS TESTE

verbos_TESTE = pd.read_excel("./corpus/corpora_train_dev_test/verbos_test_1.xls")
lemas_TESTE = list(verbos_TESTE.iloc[:]["lema"])

##TRATAR VALORES NaN
imputer = SimpleImputer(missing_values = np.nan, strategy='constant', fill_value='missing_value',verbose=0)
imputer = imputer.fit(verbos_TESTE)
verbos_TESTE = imputer.transform(verbos_TESTE)

lista_conjugados_TESTE=[]
for i in range(len(verbos_TESTE)):
	verbo = verbos_TESTE[i, 0]
	pessoa_genero = verbos_TESTE[i, 3]
	modo = verbos_TESTE[i, 5]
	numero = verbos_TESTE[i, 4]
	tempo = verbos_TESTE[i, 6]
	aspecto = verbos_TESTE[i, 7]
	verbo_conj = experimento_verbo("Fazer",'Evento',verbo,pessoa_genero,numero,modo,tempo,aspecto)
	lista_conjugados_TESTE.append(verbo_conj)

contador_TESTE = 0
contador_erros_TESTE = 0
contador_acertos_TESTE = 0
erros_TESTE = []
acertos_TESTE=[]

for conj in lista_conjugados_TESTE:
	if conj not in verbos_TESTE[:,1]:
		erros_TESTE.append(conj)
		contador_erros_TESTE+=1
	else:
		acertos_TESTE.append(conj)
		contador_acertos_TESTE+=1
	contador_TESTE+=1

porcertangem_acerto_TESTE = contador_acertos_TESTE/1000
porcertangem_acerto_TESTE*100
# Serializing json

json_object=json.dumps(acertos_TESTE, ensure_ascii=False)
# Writing to sample.json
with open("./corpus/corpora_train_dev_test/acertos_conjugação_TESTE.json", "w",) as outfile:
    outfile.write(json_object)


json_object=json.dumps(erros_TESTE, ensure_ascii=False)
# Writing to sample.json
with open("./corpus/corpora_train_dev_test/erros_conjugação_TESTE.json", "w",) as outfile:
    outfile.write(json_object)

#

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









