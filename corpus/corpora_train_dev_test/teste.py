

import pandas as pd
import json



###EXPERIMENTO CORPUS TESTE

verbos_VERIFICACAO = pd.read_excel("D:/Users/andre/Documents/GitHub/NLG_BRAZILIAN_PORTUGUESE_19-11/corpus/corpora_train_dev_test/verbos_verificar_filtro.xls")


# verbos.head()
lemas_VERIFICACAO = list(verbos_VERIFICACAO.iloc[:]["lema"])
from NLG_BRAZILIAN_PORTUGUESE.GENERATION_dev import *


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
	verbo = verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo, tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)

	return verbo


##TRATAR VALORES NaN

import numpy as np
import sklearn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy='constant', fill_value='missing_value',verbose=0)
imputer = imputer.fit(verbos_VERIFICACAO)
verbos_VERIFICACAO = imputer.transform(verbos_VERIFICACAO)

lista_conjugados_VERIFICACAO=[]
for i in range(len(verbos_VERIFICACAO)):
	verbo = verbos_VERIFICACAO[i, 0]
	pessoa_genero = verbos_VERIFICACAO[i, 3]
	modo = verbos_VERIFICACAO[i, 5]
	numero = verbos_VERIFICACAO[i, 4]
	tempo = verbos_VERIFICACAO[i, 6]
	aspecto = verbos_VERIFICACAO[i, 7]
	verbo_conj = experimento_verbo("Fazer",'Evento',verbo,pessoa_genero,numero,modo,tempo,aspecto)
	lista_conjugados_VERIFICACAO.append(verbo_conj)
