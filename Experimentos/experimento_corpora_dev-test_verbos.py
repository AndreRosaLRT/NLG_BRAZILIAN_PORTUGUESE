# -*- coding: utf-8 -*-


##PRELIMINARES
import pandas as pd
import json
import numpy as np
from sklearn.impute import SimpleImputer
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *
flexionar_verbo('Ser','Evento','manter','3','none','SG','SBJV','PRS','none')
verbo_geral("Fazer", 'Evento', 'manter', 'subjuntivo_conjuntivo', 'singular', None, '3pessoa')

#
#
# def flexionarVerboExp(tipo_de_experiencia, funcao_no_grupo_verbal,
#                     verbo, pessoa_genero, numero, modo, tempo, aspecto):
#     if numero == 'PL':
#         oi_numero = 'plural'
#     elif numero == 'SG':
#         oi_numero = 'singular'
#     else:
#         oi_numero = None
#
#     if pessoa_genero == '1':
#         oi_tipo_de_pessoa = '1pessoa'
#         genero = None
#
#     elif pessoa_genero == '2':
#         oi_tipo_de_pessoa = '2pessoa'
#         genero = None
#
#     elif pessoa_genero == '3':
#         oi_tipo_de_pessoa = '3pessoa'
#         genero = None
#
#     elif pessoa_genero == 'MASC':
#         genero = 'masculino'
#         oi_tipo_de_pessoa = None
#
#     elif pessoa_genero == 'FEM':
#         genero = 'feminino'
#         oi_tipo_de_pessoa = None
#     elif pessoa_genero == 'PRS' or pessoa_genero == 'NFIN':
#         genero = None
#         oi_tipo_de_pessoa = None
#         oi_numero = None
#
#     ####
#     if modo + '_' + tempo + '_' + aspecto == 'IND_PST_PFV':
#         tipo_de_orientacao = 'pretérito_perfectivo_I'
#     elif modo + '_' + tempo + '_' + aspecto == 'IND_PST_PRF':
#         tipo_de_orientacao = 'pretérito_perfectivo_II'
#     elif modo + '_' + tempo + '_' + aspecto == 'IND_PST_IPFV':
#         tipo_de_orientacao = 'pretérito_imperfectivo'
#     elif modo + '_' + tempo + '_' + aspecto == 'IND_FUT_none':
#         tipo_de_orientacao = 'futuro'
#     elif modo + '_' + tempo + '_' + aspecto == 'IND_PRS_none':
#         tipo_de_orientacao = 'presente'
#     elif modo + '_' + tempo + '_' + aspecto == 'SBJV_PRS_none':
#         tipo_de_orientacao = 'subjuntivo_conjuntivo'
#     elif modo + '_' + tempo + '_' + aspecto == 'SBJV_PST_IPFV':
#         tipo_de_orientacao = 'subjuntivo_condicional'
#     elif modo + '_' + tempo + '_' + aspecto == 'SBJV_FUT_none':
#         tipo_de_orientacao = 'subjuntivo_optativo'
#     elif modo + '_' + tempo + '_' + aspecto == 'PST_none_none':
#         tipo_de_orientacao = 'particípio'
#     elif modo + '_' + tempo + '_' + aspecto == 'IMP_POS_none':
#         tipo_de_orientacao = 'imperativo_I'
#     elif modo + '_' + tempo + '_' + aspecto == 'IMP_NEG_none':
#         tipo_de_orientacao = 'imperativo_II'
#     elif modo + '_' + tempo + '_' + aspecto == 'COND_none_none':
#         tipo_de_orientacao = 'passado_volitivo'
#     elif modo + '_' + tempo + '_' + aspecto == 'NFIN_none_none':
#         tipo_de_orientacao = 'não_finito_concretizado'
#     elif pessoa_genero + '_' + numero + '_' + modo + '_' + tempo + '_' + aspecto == 'PRS_none_none_none_none':
#         tipo_de_orientacao = 'gerúndio'
#     elif pessoa_genero + '_' + numero + '_' + modo + '_' + tempo + '_' + aspecto == 'NFIN_none_none_none_none':
#         tipo_de_orientacao = 'infinitivo'
#     verbo = verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, verbo,tipo_de_orientacao, oi_numero, genero, oi_tipo_de_pessoa)
#
#     return verbo

# #EXEMPLOS USO FUNÇÃO
# # # #urgir           urgia      V             3     SG  IND   PST    IPFV
# flexionarVerbo("Fazer", 'Evento', "urgir", '3', 'SG', 'IND', 'PST','IPFV')
# flexionarVerbo("Ser", 'Evento', "ser", '3', 'SG', 'IND', 'PST','PFV')
# #
# # flexionarVerbo("Fazer", 'Evento', "identificar", '1', 'SG', 'IMP', 'POS', 'none')
# # verbo_geral("Fazer", 'Evento', "identificar","imperativo_I", 'singular', None, '1pessoa')
# # flexionarVerbo("Sentir", 'Evento', "expedir", '2', 'PL', 'SBJV', 'PST', 'IPFV')
# # flexionarVerbo("Fazer", 'Evento', "assentir", '1', 'SG', 'SBJV', 'PST', 'IPFV')
# # verbo_geral("Fazer",'Evento',"sentir",'subjuntivo_conjuntivo', 'plural', None, '1pessoa')
# # flexionarVerbo("Fazer", 'Evento', 'desmatar', '1', 'SG', 'IND', 'PST',  'PRF')
# # flexionarVerbo('Sentir', 'Evento','desmatar','MASC', 'SG', 'PST', 'none', 'none')
# # flexionarVerbo("Fazer", 'Evento', "somar", '3', 'PL', 'IND', 'PRS', 'none')
# # flexionarVerbo("Fazer", 'Evento', "acumular", 'PRS', 'none', 'none', 'none', 'none')
# # # flexionarVerbo("Fazer", 'Evento', "acumular", pessoa_genero, numero, modo, tempo, aspecto)

# ###################EXPERIMENTO CORPUS DE DESENVOLVIMENTO#################

##EXPERIMENTO NO CORPUS DE DESENVOLVIMENTO DO SIGMORPHON
##importando os verbos do corpus de dev(sigmorphon)

path = 'https://raw.githubusercontent.com/sigmorphon/conll2017/master/all/task1/portuguese-dev'

verbos = pd.read_csv(path,delimiter='[\s+ ;]',names=['lema','verbo_conjugado','classe','pessoa_genero','numero',
													 'modo','tempo','aspecto'],engine='python', encoding='utf-8')


##############

##TRATAMENTO DE VALORES NaN
imputer = SimpleImputer(missing_values =None, strategy='constant', fill_value='none',verbose=0)
imputer = imputer.fit(verbos)
verbos = imputer.transform(verbos)
###
####tratamento de grafia em pt europeu:
for i in range(len(verbos[:,0])):
	if verbos[i,0][-2:] == 'ôr':
		experiencia_do_verbo(verbos[i, 0])
		verbos[i, 0] =experiencia_do_verbo(verbos[i, 0]) +'or'

for i in range(len(verbos[:, 1])):
	if verbos[i, 1][-4:] == 'ámos':
		rad = verbos[i, 1][slice(len(verbos[i, 1]) - 4)]
		verbos[i, 1]=rad+'amos'


##CONJUGANDO OS VERBOS DO SIGMORPHON
lista_conjugados=[]

for i in range(len(verbos)):
	verbo = verbos[i, 0]
	pessoa = verbos[i, 3]
	genero = verbos[i,3]
	modo = verbos[i, 5]
	numero = verbos[i, 4]
	tempo = verbos[i, 6]
	aspecto = verbos[i, 7]
	verbo_conj = flexionar_verbo("Fazer", 'Evento', verbo, pessoa,genero, numero, modo, tempo, aspecto)
	lista_conjugados.append(verbo_conj)

###FAZENDO A CONTAGEM DE ERROS E ACERTOS COM BASE NO PADRÃO OURO
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

##CALCULANDO A PORCENTAGEM DE ERROS E ACERTOS
porcertangem_acerto = (contador_acertos/1000)*100
print(porcertangem_acerto)

# Salvando os acertos e erros de conjugação em arquivos .json
json_object=json.dumps(acertos, ensure_ascii=False)
# Writing to sample.json
with open("./Experimentos/saida_experimento_dev_test/acertos_conjugação_dev.json", "w",) as outfile:
    outfile.write(json_object)

json_object=json.dumps(erros, ensure_ascii=False)
# Writing to sample.json
with open("./Experimentos/saida_experimento_dev_test/erros_conjugação_dev.json", "w",) as outfile:
    outfile.write(json_object)


###EXPERIMENTO CORPUS TESTE
path2='https://raw.githubusercontent.com/sigmorphon/conll2017/master/answers/task1/portuguese-uncovered-test'
verbos_TESTE = pd.read_csv(path2,sep='[\s+ ;]',names=['lema','verbo_conjugado','classe','pessoa_genero','numero','modo','tempo','aspecto'],engine='python', encoding='utf-8')

#VERIFIQUEI UM ERRO NA COLUNA DE VERBO CONJUGADO DO VERBO REMOER NO FUTURO DE INDIVATIVO, QUE CAUSOU UM ERRO
# NO TESTE DE ACURÁCIA: TRATEI O ERRO
# verbos_TESTE.query('lema == "remoer"')
verbos_TESTE.loc[940,['verbo_conjugado']] = 'remoeremos'

# verbos_TESTE.query('lema == "assentir"')
# verbos_TESTE.query('lema == "manter"')
#
##TRATAR VALORES NaN
# imputer = SimpleImputer(missing_values = np.nan, strategy='constant', fill_value='none',verbose=0)

imputer = SimpleImputer(missing_values = None, strategy='constant', fill_value='none',verbose=0)
imputer = imputer.fit(verbos_TESTE)
verbos_TESTE = imputer.transform(verbos_TESTE)
####tratamento de grafia em pt de portugal:
# verbos_TESTE.query('lema == "manter"')

#####tratamento de grafia em pt europeu:
for i in range(len(verbos_TESTE[:,0])):
	if verbos_TESTE[i,0][-2:] == 'ôr':
		experiencia_do_verbo(verbos_TESTE[i, 0])
		verbos_TESTE[i, 0] =experiencia_do_verbo(verbos_TESTE[i, 0]) +'or'

for i in range(len(verbos_TESTE[:, 1])):
	if verbos_TESTE[i, 1][-4:] == 'ámos':
		rad = verbos_TESTE[i, 1][slice(len(verbos_TESTE[i, 1]) - 4)]
		verbos_TESTE[i, 1]=rad+'amos'

##CONJUGANDO OS VERBOS DO SIGMORPHON
lista_conjugados_TESTE=[]
for i in range(len(verbos_TESTE)):
	verbo = verbos_TESTE[i, 0]
	pessoa = verbos_TESTE[i, 3]
	genero = verbos_TESTE[i, 3]
	modo = verbos_TESTE[i, 5]
	numero = verbos_TESTE[i, 4]
	tempo = verbos_TESTE[i, 6]
	aspecto = verbos_TESTE[i, 7]
	verbo_conj = flexionar_verbo("Fazer", 'Evento', verbo, pessoa, genero, numero, modo, tempo, aspecto)

	lista_conjugados_TESTE.append(verbo_conj)

##CALCULANDO A PORCENTAGEM DE ERROS E ACERTOS

contador_TESTE = 0
contador_erros_TESTE = 0
contador_acertos_TESTE = 0
erros_TESTE = []
acertos_TESTE=[]

verficar2=verbos_TESTE[:,1]
acertos2=acertos_TESTE

for conj in lista_conjugados_TESTE:
	if conj not in verbos_TESTE[:,1]:
		erros_TESTE.append(conj)
		contador_erros_TESTE+=1
	else:
		acertos_TESTE.append(conj)
		contador_acertos_TESTE+=1
	contador_TESTE+=1

# CALCULANDO A PORCENTAGEM DE ACERTOS
porcertangem_acerto_TESTE = (contador_acertos_TESTE/1000)*100
print(porcertangem_acerto_TESTE)
#SALVANDO ERROS E ACERTOS EM ARQUIVOS JSON
json_object=json.dumps(acertos_TESTE, ensure_ascii=False)
# Writing to sample.json
with open("./Experimentos/saida_experimento_dev_test/acertos_conjugação_TESTE.json", "w",) as outfile:
    outfile.write(json_object)

json_object=json.dumps(erros_TESTE, ensure_ascii=False)
# Writing to sample.json
with open("./Experimentos/saida_experimento_dev_test/erros_conjugação_TESTE.json", "w",) as outfile:
    outfile.write(json_object)


##EXEMPLO TESTE NO DAMATA:

##importando sinonimos
sinonimos = json.load(open('/home/andrerosa/PROJETO_TESE/NLG_BRAZILIAN_PORTUGUESE_19-11/Experimentos/'
						   'mineracao_lexicon_pre_exp_aplicacao/dic_sin_cbow.json'))
#
# verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,
# 		            tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)

TIPO_DE_EXPERIENCIA='Fazer'
funcao_no_grupo_verbal='Evento'

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
path =r'/home/andrerosa/git_workspace/NLG_BRAZILIAN_PORTUGUESE_19-11/corpus/corpora_train_dev_test'
with codecs.open(path + "/teste_DAMATA.json", "w",encoding='utf-8' ) as outfile:
	json.dump(json_object,outfile, ensure_ascii=False)
	outfile.write(json_object)




