
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:50:31 2019

@author: andre
"""


# ######PRELIMINARES


import re

######
###

###############################################################################
#####################
###########ORDEM DA PALAVRA

###ADVÉRBIO    INÍCIO####

###########ORDEM DA PALAVRA
from builtins import zip

from nltk import unify


def adverbio_modo(indice=None):
	try:
		opcoes = ['bem','mal','assim','adrede',
				  'melhor','pior','depressa','devagar',
				  'acinte','debalde','cuidadosamente','calmamente',
				  'tristemente','alegremente', 'bondosamente',
				  'calmamente', 'discretamente', 'elegantemente','infelizmente',
				  'evidentemente']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio = ''
	return adverbio
# adverbio_modo(10)

def adverbio_intensidade(indice=None):
	try:
		opcoes = ['muito','demais','todo','pouco',
			'tão','quão','demasiado','bastante','imenso','demais',
			'mais','menos','quanto','quase','tanto',
			'assaz','tudo','nada']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio=''
	return adverbio
# adverbio_intensidade(1)
def adverbio_lugar(indice=None):
	try:
		opcoes = ['aí','aqui','acolá','cá',
			'lá','ali','adiante','abaixo','embaixo',
			'acima','adentro','dentro']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio=''
	return adverbio
# adverbio_lugar(1)

def adverbio_tempo(indice=None):
	try:
		opcoes = ['ainda', 'agora',
				  'amanhã', 'à noite', 'anteontem',
				  'antes', 'à tarde', 'às vezes', 'atualmente',
				  'breve', 'cedo', 'depois','de manhã','de repente',
				  'de vez em quando','hoje','hoje em dia',
				  'já', 'logo', 'nunca','ontem','ora',
				  'outrora','quando','sempre','tarde','jamais']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio = ''
	return adverbio

# adverbio_tempo(1)
def adverbio_negacao(indice=None):
	try:

		opcoes = ['não', 'nem', 'tampouco', 'nunca', 'jamais' ]
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio=''
	return adverbio

# adverbio_negacao(4)

def adverbio_relativo(indice=None):
	try:
		opcoes = ['de onde', 'quando', 'onde',
							 'de quando', 'que', 'por onde']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio=''
	return adverbio

# adverbio_relativo(4)


def adverbio_afirmacao(indice=None):
	try:
		opcoes = ['sim','deveras',
					'indubitavelmente','decididamente',
					  'certamente', 'realmente',
					  'decerto', 'certo',
					   'efetivamente']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio=''
	return adverbio

# adverbio_afirmacao(4)

def adverbio_duvida(indice=None):
	try:
		opcoes = ['possivelmente','provavelmente',
				  'acaso','porventura',
				   'quiçá','será','talvez',
				   'casualmente']
		nums = [x for x in range(len(opcoes))]
		adverbios = dict(zip(nums, opcoes))
		adverbio = adverbios[indice]
	except:
		adverbio=''
	return adverbio

# adverbio_duvida(4)

def adverbio(tipo_de_adverbio, indice):
	"""
	:param tipo_de_adverbio: 'Modo' 'Intensidade' 'Lugar' 'Tempo'
			'Negação' 'Afirmação' 'Dúvida' 'Adv_relativo'
	:param indice: --
	:return: advérbio
	"""
	try:
		if tipo_de_adverbio == 'Modo':

			adverbio = adverbio_modo(indice)

		elif tipo_de_adverbio == 'Intensidade':

			adverbio = adverbio_intensidade(indice)

		elif tipo_de_adverbio == 'Lugar':

			adverbio = adverbio_lugar(indice)

		elif tipo_de_adverbio == 'Tempo':

			adverbio = adverbio_tempo(indice)

		elif tipo_de_adverbio == 'Negação':

			adverbio = adverbio_negacao(indice)

		elif tipo_de_adverbio == 'Afirmação':
			adverbio = adverbio_afirmacao(indice)

		elif tipo_de_adverbio == 'Dúvida':

			adverbio = adverbio_duvida(indice)

		elif tipo_de_adverbio == 'Adv_relativo':

			adverbio = adverbio_relativo(indice)
		return adverbio
	except:
		adverbio=''
		return adverbio

# adverbio('teste', 4)

def grupo_adverbial(tipo_de_adverbio1=None, ind1=None,
					tipo_de_adverbio2=None, ind2=None,
					tipo_de_adverbio3=None, ind3=None,
					tipo_de_adverbio4=None, ind4=None,
					tipo_de_adverbio5=None, ind5=None):
	adv1 = adverbio(tipo_de_adverbio1, ind1)
	adv2 = adverbio(tipo_de_adverbio2, ind2)
	adv3 = adverbio(tipo_de_adverbio3, ind3)
	adv4 = adverbio(tipo_de_adverbio4, ind4)
	adv5=adverbio(tipo_de_adverbio5,ind5)
	advs = [adv1,adv2,adv3,adv4,adv5]
	grupo_adv =re.sub(' +', ' ', (' '.join(advs)))

	return grupo_adv

grupo_adverbial(tipo_de_adverbio1='Negação', ind1=0,
				tipo_de_adverbio2='Intensidade', ind2=0,
				tipo_de_adverbio3='Modo', ind3=10)



# grupo_adverbial(tipo_de_adverbio1='Modo',ind1=0,tipo_de_adverbio2='Modo',ind2=1,tipo_de_adverbio3='Modo',
# 				ind3=2,tipo_de_adverbio4='Modo', ind4=3, tipo_de_adverbio5='Modo',ind5=4)

###ADVÉRBIO    FIM####

####################################################################
##### VERBO INÍCIO####

def def_classe_de_verbo(funcao_no_grupo_verbal):
	'''
    (str)-> str

    Retorna um str com classe de verbo dado um verbm em str.

    >>>def_classe_de_verbo ('andar')
    lexical
    >>> def_classe_de_verbo ('ir')
    auxiliar
    >>>def_classe_de_verbo ('poder')
    'modal'
    '''

	# print("Qual é a função do verbo no grupo verbal?")
	# funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
	#                                       'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()

	if funcao_no_grupo_verbal == 'Evento' or funcao_no_grupo_verbal == 'Evento+Núcleo':
		classe_verbo = 'lexical'
	elif funcao_no_grupo_verbal == 'Auxiliar' or funcao_no_grupo_verbal == 'Auxiliar+Núcleo':
		classe_verbo = 'auxiliar'
	elif funcao_no_grupo_verbal == 'Modal' or funcao_no_grupo_verbal == 'Modal+Núcleo':
		classe_verbo = 'modal'
	else:
		classe_verbo = None

	return classe_verbo


# EXEMPLOS
# def_classe_de_verbo("Modal")
# def_classe_de_verbo("Evento+Núcleo")
# def_classe_de_verbo("Auxiliar")
# def_classe_de_verbo("Auxiliar+Núcleo")


#######################################

##A próximo função precisa ir sendo atualizada e melhorada à medida que subo na escala de ordens:
# Resolver a questão de como vou fazer para dar entrada no 'verbo'-talvez alguma
#        subfunção que pergunta ao usuário qual é a o tipo_pessoa de experiência
#        ele pretende gerar. Provavelmente vai puxar do inventário de tipos de configuração
#        que vou introduzir a partir da anotação do texto na GUM- um inventário de
#        realizações de determinados significados semânticos específicos (de lá vamos puxar
#            as informações necessárias para a geração)


####ESTA FUNÇÃO DEPENDE DE FORNECIMENTO DO PARÂMETO 'VERBO'

#        A primeira função o verbo não precisa estar lematizado, ou seja, podemos entrar qualquer verbo, mesmo conjugado e
#        a função retorna o ME. Essa opção me paree um pouco redundante pois se sabemos de antemão qual é o verbo, já sabemos
##        qual é o ME. A segunda função depende de um verbo lematizado que dependerá por sua vez de escolhas dentro de opções de
#        tipos de experiências que são realizadas por verbos lematizados (esses verbos então serão realizações de opções dentro de
#            de uma estrutura em cascata de opções que ainda preciso descobrir como fazer)

# COMENTADA POR ENQUANTO POIS ELA ESTÁ FUNCIONANDO COMO UM PARSER.
# Não vou precisar ainda desta função, pois a entrada vai ser com o verbo no infinitivo
# def experiencia_do_verbo(verbo):
#
#     '''(str)-> str
#
#     Retorna um str com o morfema experiencial (ME) que realiza
#     a experiência do verbo, dado um verbo lematizado.
#     '''
#     # verbo = input ("Qual o verbo?")
#
#     MI = realizacao_transitoriedade_do_verbo()
#     ME =  (verbo[slice(-len(MI))])
#
#     return ME
# verbo = 'ando'
# experiencia_do_verbo ('ando')


def experiencia_do_verbo(verbo):
	'''(str)-> str

    Retorna um str com o morfema experiencial (ME) que realiza
    a experiência do verbo, dado um verbo lematizado

    >>>experiencia_do_verbo()
    'lev'
    >>>experiencia_do_verbo('')
    'diz'
    >>>experiencia_do_verbo('')
    't'
    '''

	# verbo = input ('Qual é o verbo lematizado?')
	ME = (verbo[slice(-2)])
	return (ME)


# experiencia_do_verbo("correr")

##############TRANSITORIEDADE######################################################

#
#
# def deteccao_transitoriedade_do_verbo_dev(verbo,tipo_de_orientacao,tipo_de_orientacao,)
#
#
def deteccao_transitoriedade_do_verbo(verbo):
	'''
    (str) -> str

    Retorna o morfema interpessoal que realiza a orientação interpessoal
    dados o verbo, seu padrão de morfologia, seu tipo_pessoa de orientação
    e o tipo_pessoa de pessoa.

    >>>deteccao_transitoriedade_do_verbo('expus')
    'us'
    >>>deteccao_transitoriedade_do_verbo('li')
    'i'
    >>>deteccao_transitoriedade_do_verbo('bebi')
    'i'

    '''
	# verbo = input ("Qual o verbo?")
	ME = experiencia_do_verbo(verbo)
	MI = (verbo[len(ME):])
	return MI


# deteccao_transitoriedade_do_verbo("ando")
#
#
# ###################opções para tipos de orientação interpessoal
#
# tipo_nao_finito = choice.Menu(['não_finito_subjuntivo_conjuntivo', 'não_finito_subjuntivo_condicional',
#                                     'não_finito_subjuntivo_optativo','não_finito_imperativo_I','não_finito_imperativo_II',
#                                    'não_finito_concretizado']).ask()
#
# tipo_finito = choice.Menu(['finito_presente','finito_pretérito_perfectivo_I','finito_pretérito_perfectivo_II',
#                       'finito_pretérito_imperfectivo','finito_passado_volitivo','finito_futuro']).ask()
#
# tipo_nao_orientado = choice.Menu(['não_orientado_infinitivo',
#                                 'não_orientado_gerúndio',
#                                 'não_orientado_particípio'
#                                     ]).ask()


def OI_tipo_de_orientacao(tipo_de_orientacao):
	return tipo_de_orientacao


# OI_tipo_de_orientacao("não_orientado_infinitivo")


#######
# opções de padrão de morfologia('-AR', '-ER', '-IR', '-OR')

def realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero=None,
                                          OI_tipo_de_pessoa=None, padrao_pessoa_morfologia=None):
	'''(str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.

    >>>realizacao_transitoriedade_infinitivo()
    'ar'
    '''
	if (padrao_de_morfologia == '-AR'):
		MI = 'ar'
	elif (padrao_de_morfologia == '-ER'):
		MI = 'er'
	elif (padrao_de_morfologia == '-IR'):
		MI = 'ir'
	elif (padrao_de_morfologia == '-OR'):
		MI = 'or'
	return MI
# realizacao_transitoriedade_infinitivo('-AR')


def detecta_padrao_morfologia(verbo):
	'''(str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.

    >>>realizacao_transitoriedade_infinitivo()
    'ar'
    '''
	if verbo == None:
		padraoMorfologia=None
	else:
		ME = experiencia_do_verbo(verbo)
		MI = (verbo[len(ME):])
		if MI == 'ar':
			padraoMorfologia='-AR'
		elif MI == 'er':
			padraoMorfologia='-ER'
		elif MI == 'ir':
			padraoMorfologia='-IR'
		elif MI == 'or':
			padraoMorfologia='-OR'
		else:
			padraoMorfologia=None

	return padraoMorfologia

teste = detecta_padrao_morfologia(None)


######
# opções
# padrao_de_morfologia = ['-AR', '-ER', '-IR', '-OR']
# OI_tipo_de_pessoa =['1pessoa','2pessoa','3pessoa'])
# OI_numero = ['singular', 'plural']
# padrao_pessoa_morfologia = ['3pessoa_do_singular', 'Morfologia_padrão']


def realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                        padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str,str,str,str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no presente, dados
    a o padrão de morfologia, tipo_pessoa de orientação, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_presente()
    'o'
    :param genero:
    '''

	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão" or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão" or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"
	):
		MI = 'o'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão":
		MI = 'onho'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'as'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'
	):
		MI = 'es'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular'):
		MI = 'õe'
	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ões'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
		MI = 'a'
	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'
	):
		MI = 'e'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'õe'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'õe'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'omos'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ais'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'eis'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'e'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'is'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'õe'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ondes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'am'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão'
	):
		MI = 'em'


	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'õe'


	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'õem'

	return MI


# realizacao_transitoriedade_presente('-AR','singular','1pessoa')

# pretérito_perfectivo_I

# padrao_de_morfologia = choice.Menu(['-AR', '-ER', '-IR', '-OR']).ask()
# OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
# OI_numero = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"
                                                      ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
    'ei'
    '''
	if padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão":
		MI = 'ei'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão" or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"):
		MI = 'i'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"):
		MI = 'us'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'aste'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'este'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'iste'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'useste'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ou'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'eu'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'iu'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ôs'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'usemos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'astes'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'estes'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'istes'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'usestes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'aram'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'eram'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'iu'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'iram'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'useram'
	return MI
#
# realizacao_transitoriedade_preterito_perfectivo_I('-ER','singular','1pessoa')
# X=['-AR','-ER','-IR','-OR']
# Y=['plural','singular']
# Z=['1pessoa','2pessoa','3pessoa']
# for i in X:
# 	for j in Y:
# 		for p in Z:
# 			transito = realizacao_transitoriedade_preterito_perfectivo_I(i,j,p)
# 			print(transito)
#

# realizacao_transitoriedade_preterito_perfectivo_I('-IR', 'singular', '1pessoa')


###pretérito imperfectivo
# padrao_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
# OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
# OI_numero = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e numero.

    >>
    'ei'
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ava'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'
			or padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
		padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ia'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'unha'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'avas'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular'):
		MI = 'ia'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ias'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ias'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'unhas'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ávamos'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'íamos'
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ia'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ia'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'íamos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morforlogia_padrão':
		MI = 'únhamos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'
	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'áveis'
	#
	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'íeis'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ía'
		else:
			MI = 'íeis'
	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'únheis'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ava'
		else:
			MI = 'avam'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'iam'
	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ía'
		else:
			MI = 'íam'
	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'unham'
	return MI


realizacao_transitoriedade_preterito_imperfectivo('-IR', 'singular', '1pessoa')


def realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.


    'ei'
    '''
	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ara'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'era'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'ira'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'usera'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'aras'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'eras'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'iras'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'useras'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'áramos'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'êramos'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'íramos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'úseramos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'áreis'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'êreis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'íreis'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'uséreis'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'aram'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'eram'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'iram'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'useram'
	return MI

#
# X=['-AR','-ER','-IR','-OR']
# Y=['plural','singular']
# Z=['1pessoa','2pessoa','3pessoa']
# for i in X:
# 	for j in Y:
# 		for p in Z:
# 			transito = realizacao_transitoriedade_preterito_perfectivo_II(i,j,p)
# 			print(transito)

def realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no passado volitivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.


    'ei'
    '''

	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'aria'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'eria'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'iria'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
	      padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'oria'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'arias'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'erias'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'irias'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'orias'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríamos'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríamos'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríamos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríamos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríeis'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríeis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríeis'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríeis'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'ariam'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eriam'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iriam'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oriam'

	return MI


# realizacao_transitoriedade_passado_volitivo('-AR', 'singular','1pessoa')


def realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no futuro, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
    'ei'
    '''
	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'arei'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'erei'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'irei'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'):
		MI = 'orei'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ará'
		else:
			MI = 'arás'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'erá'
		else:
			MI = 'erás'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'irá'
		else:
			MI = 'irás'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'orá'
		else:
			MI = 'orás'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'ará'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'erá'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'irá'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
		MI = 'orá'
	#
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'aremos'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'eremos'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'iremos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'oremos'
	#
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'areis'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'ereis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'ireis'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'oreis'
	#
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'arão'

	elif (padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'erão'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'irão'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'orão'

	return MI


# realizacao_transitoriedade_futuro('-AR','plural','2pessoa')

def realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                     padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo conjuntivo, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'onha'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'es'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'
	):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'as'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhas'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'emos'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'
	):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'amos'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhamos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'eis'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'
	):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'ais'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhais'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'em'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'
	):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'am'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onham'
	return MI


# realizacao_transitoriedade_subjuntivo_conjuntivo('-ER','plural','2pessoa')
#######subjuntivo_condicional


def realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo condicional, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I('-AR','1pessoa','singular')
    >>>'asse'

    '''

	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'asse'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'esse'

	elif (
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'isse'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'usesse'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'asses'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'esses'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'isses'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usesses'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ássemos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êssemos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'íssemos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'uséssemos'

	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ásseis'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êsseis'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'ísseis'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usésseis'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'assem'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'essem'

	elif (padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'íssem'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usessem'
	return MI


# realizacao_transitoriedade_subjuntivo_condicional('-AR','plural','2pessoa','3pessoa_do_singular')

###subjuntivo_optativo
def realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo_optativo ,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'user'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'useres'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'usermos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userdes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userem'

	return MI


# realizacao_transitoriedade_subjuntivo_optativo('-AR','plural','2pessoa')

############não_finito_concretizado

def realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                       padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo  não_finito_concretizado,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'
	):
		MI = 'or'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ores'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ormos'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ordes'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'orem'
	return MI


# realizacao_transitoriedade_nao_finito_concretizado('-AR','plural','2pessoa')

#######imperativo_I (afirmativo)

def realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                            padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_I,
    dados  o padrão de morfologia, tipo_pessoa de pessoa,número, padrão de pessoa da morfologia.

    >>>
    ''
    '''

	if OI_numero == 'singular':
		if OI_tipo_de_pessoa == '1pessoa':
			if (padrao_de_morfologia == '-AR' or
					padrao_de_morfologia == '-ER' or
					padrao_de_morfologia == '-IR' or
					padrao_de_morfologia == '-OR'):
				MI = ''

		elif OI_tipo_de_pessoa == '2pessoa':
			if padrao_de_morfologia == '-AR':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'a'
			elif (padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR'):
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'e'
			elif  padrao_de_morfologia == '-OR':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'onha'
				else:
					MI = 'õe'
####
		elif OI_tipo_de_pessoa == '3pessoa':
			if padrao_de_morfologia == '-AR':
				MI = 'e'
			elif (padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR') :
				MI = 'a'
			elif  padrao_de_morfologia == '-OR':
				MI = 'onha'
####
	elif OI_numero == 'plural':
		if OI_tipo_de_pessoa == '1pessoa':
			if padrao_de_morfologia == '-AR':
				MI = 'emos'
			elif padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR':
				MI = 'amos'
			elif padrao_de_morfologia == '-OR':
				MI = 'onhamos'

		elif OI_tipo_de_pessoa == '2pessoa':
			if padrao_de_morfologia == '-AR':
				MI = 'ai'
			elif padrao_de_morfologia == '-ER':
				MI = 'ei'
			elif padrao_de_morfologia == '-IR':
				MI='i'
			elif padrao_de_morfologia == '-OR':
				MI = 'onde'

		elif OI_tipo_de_pessoa == '3pessoa':
			if padrao_de_morfologia == '-AR':
				MI='em'
			elif (padrao_de_morfologia == '-ER' or
			    padrao_de_morfologia == '-IR'):
				MI = 'am'
			elif padrao_de_morfologia == '-OR':
				MI= 'onham'
	return MI


# realizacao_transitoriedade_imperativo_I('-AR', 'plural', 'pessoa')
# realizacao_transitoriedade_imperativo_I('-OR', 'singular', '2pessoa')


#######imperativo_II (negativo)


def realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_II,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>

    '''

	if (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'):
		MI = 'es'

	elif (
			(padrao_de_morfologia == '-ER' or '-IR')
			and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular'
	):
		MI = 'as'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '2pessoa'
			and OI_numero == 'singular'
	):
		MI = 'onhas'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'singular'
	):
		MI = 'e'

	elif (
			(
					padrao_de_morfologia == '-ER' or '-IR'
			)
			and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'singular'
	):
		MI = 'onha'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '1pessoa'
			and OI_numero == 'plural'
	):
		MI = 'emos'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'
	):
		MI = 'amos'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural'):
		MI = 'onhamos'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '2pessoa'
			and OI_numero == 'plural'
	):
		MI = 'eis'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'
	):
		MI = 'ais'

	elif (
			padrao_de_morfologia == '-OR'
			and OI_tipo_de_pessoa == '2pessoa'
			and OI_numero == 'plural'
	):
		MI = 'onhais'

	elif (
			padrao_de_morfologia == '-AR'
			and OI_tipo_de_pessoa == '3pessoa'
			and OI_numero == 'plural'
	):
		MI = 'em'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'
	):
		MI = 'am'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		MI = 'onham'

	elif (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'
	):
		MI = ''

	return MI


# realizacao_transitoriedade_imperativo_II('-AR', '2pessoa','plural')
###gerúndio
# realizacao_transitoriedade_gerundio('-OR')

def realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero=None, OI_numero=None,
                                        OI_tipo_de_pessoa=None, padrao_pessoa_morfologia="Morfologia_padrão"
                                        ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no gerúndio,
    dadoo padrão de morfologia.

    >>>
    '''
	if padrao_de_morfologia == '-AR':
		MI = 'ando'

	elif padrao_de_morfologia == '-ER':
		MI = 'endo'

	elif padrao_de_morfologia == '-IR':
		MI = 'indo'

	elif padrao_de_morfologia == '-OR':
		MI = 'ondo'

	return MI


realizacao_transitoriedade_gerundio('-IR')

######particípio


def realizacao_transitoriedade_participio(padrao_de_morfologia,OI_numero, genero, OI_tipo_de_pessoa=None,
                                          padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no particípio,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_particípio ()
    ''
    '''

	if padrao_de_morfologia == '-AR' and OI_numero == 'singular' and genero == 'feminino':
		MI = 'ada'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'plural' and genero == 'feminino':
		MI = 'adas'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'singular' and genero == 'masculino':
		MI = 'ado'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'plural' and genero == 'masculino':
		MI = 'ados'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'singular' and genero == 'masculino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'singular' and genero == 'masculino'
	):
		MI = 'ido'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'plural' and genero == 'masculino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'plural' and genero == 'masculino'
	):
		MI = 'idos'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'singular' and genero == 'feminino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'singular' and genero == 'feminino'
	):
		MI = 'ida'

	elif (
			padrao_de_morfologia == '-ER' and OI_numero == 'plural' and genero == 'feminino' or
			padrao_de_morfologia == '-IR' and OI_numero == 'plural' and genero == 'feminino'
	):
		MI = 'idas'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'singular' and genero == 'feminino':
		MI = 'osta'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'singular' and genero == 'masculino':
		MI = 'osto'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'plural' and genero == 'feminino':
		MI = 'ostas'

	elif padrao_de_morfologia == '-OR' and OI_numero == 'plural' and genero == 'masculino':
		MI = 'ostos'

	return MI


#
#

#
# realizacao_transitoriedade_participio('-AR', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-AR', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-AR', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-AR', 'singular', 'feminino')
#
#
# realizacao_transitoriedade_participio('-ER', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-ER', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-ER', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-ER', 'singular', 'feminino')
#
# realizacao_transitoriedade_participio('-IR', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-IR', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-IR', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-IR', 'singular', 'feminino')
#
#
# realizacao_transitoriedade_participio('-OR', 'plural', 'masculino')
# realizacao_transitoriedade_participio('-OR', 'singular', 'masculino')
# realizacao_transitoriedade_participio('-OR', 'plural', 'feminino')
# realizacao_transitoriedade_participio('-OR', 'singular', 'feminino')
#



# realizacao_transitoriedade_preterito_imperfectivo('-IR','singular','1pessoa')

def realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
                                        padrao_pessoa_morfologia="Morfologia_padrão"):
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo()
    'o'

    '''

	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero=None,
		                                           OI_tipo_de_pessoa=None, padrao_pessoa_morfologia=None)

	elif tipo_de_orientacao == 'presente':
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                       	padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                      padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                       padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                    padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                        padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'imperativo_I':
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                             padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'imperativo_II':
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                              padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa=None,
		                                           padrao_pessoa_morfologia=None)
	return MI


#
# # realizacao_transitoriedade_gerundio('-AR')
# realizacao_transitoriedade_do_verbo('gerúndio','-AR',None,None,None)
# realizacao_transitoriedade_do_verbo('presente','-AR','singular',None,'1pessoa')
# for i in X:
# 	for j in Y:
# 		for k in Z:
#
# 			transito = realizacao_transitoriedade_do_verbo('pretérito_perfectivo_II',i,j,None,k)
# 			print(transito)
# realizacao_transitoriedade_do_verbo('pretérito_perfectivo_I','-AR','singular',None,'1pessoa')
# realizacao_transitoriedade_do_verbo('imperativo_I','-AR','singular',None,'2pessoa')
# realizacao_transitoriedade_do_verbo('imperativo_II','-AR','singular',None,'2pessoa')
# realizacao_transitoriedade_imperativo_I('AR','singular','1pessoa')
# realizacao_transitoriedade_do_verbo('imperativo')
# FORMAÇÃO DO VERBO ###################

#
# def formação_da_estrutura_do_verbo1 (): #O tipo_de_experiência
# #aqui vai ter relação com o tipo_pessoa de configuração
#     '''
#     (str) -> str
#
#     Retorna um verbo flexionado dados OE_experiência_do_verbo,
#     OI_orientação_interpessoal_do_verbo.
#
#     >>> formação_da_estrutura_do_verbo ()
#     'levo'
#     >>>formação_da_estrutura_do_verbo ()
#     'levei'
#     '''
#     OE_experiência_do_verbo = experiencia_do_verbo()
#     OI_orientação_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo ()
#
#     return OE_experiência_do_verbo + OI_orientação_interpessoal_do_verbo
# experiencia_do_verbo('andar')



#################
### FORMAÇÃO DOS VERBOS IRREGULARES
###VERBOS TERMINADOS EM : 'cer'


def formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
												 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		if OI_tipo_de_pessoa=='1pessoa':
			ME = verbo[slice(-3)]+'ç'
		else:
			ME = verbo[slice(-2)]

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'ç'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if (OI_tipo_de_pessoa=='3pessoa' or
			OI_tipo_de_pessoa == '1pessoa'):
			ME = verbo[slice(-3)]+'ç'
		else:
			ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'ç'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
#
# formacao_verbo_CER('enternecer','presente','-ER','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_CER('enternecer','subjuntivo_conjuntivo','-ER','singular',None,'1pessoa')
# formacao_verbo_CER('enternecer','imperativo_I','-ER','plural',None,'3pessoa')
# formacao_verbo_CER('enternecer','imperativo_II','-ER','singular',None,'2pessoa')

###VERBOS TERMINADOS EM : 'çar'

def formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_tipo_de_pessoa=='1pessoa' and OI_numero=='singular':
			ME = verbo[slice(-3)]+'c'
		else:
			ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'c'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa=='2pessoa':
			ME = verbo[slice(-2)]
		else:
			ME=verbo[slice(-3)]+'c'
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'c'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo

# formacao_verbo_ÇAR('despedaçar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_ÇAR('abraçar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_II','-AR','singular',None,'2pessoa')
#


###VERBOS TERMINADOS EM : 'Car'
def formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	if tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_tipo_de_pessoa=='1pessoa' and OI_numero=='singular':
			ME = verbo[slice(-3)]+'qu'
		else:
			ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'qu'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-3)] + 'qu'
			elif OI_tipo_de_pessoa == '1pessoa':
				ME = ''
			else:
				ME = verbo[slice(-2)]
		elif OI_numero == 'plural':
			if (OI_tipo_de_pessoa == '3pessoa' or OI_tipo_de_pessoa == '1pessoa'):
				ME = verbo[slice(-3)] + 'qu'
			else:
				ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
													 OI_tipo_de_pessoa, padrao_pessoa_morfologia)


	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular' and OI_tipo_de_pessoa == '1pessoa':
			ME = ''
		else:
			ME = verbo[slice(-3)] + 'qu'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo

# formacao_verbo_CAR('identificar','imperativo_I','-AR','singular',None,'2pessoa')
# formacao_verbo_CAR('focar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_CAR('focar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_CAR('focar','imperativo_II','-AR','singular',None,'2pessoa')



###VERBOS TERMINADOS EM : 'GAR'

def formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	if tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_tipo_de_pessoa=='1pessoa' and OI_numero=='singular':
			ME = verbo[slice(-3)]+'gu'
		else:
			ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'gu'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if (OI_tipo_de_pessoa=='3pessoa' or
			OI_tipo_de_pessoa == '1pessoa'):
			ME = verbo[slice(-3)]+'gu'
		else:
			ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)]+'gu'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
# formacao_verbo_GAR('entregar','pretérito_perfectivo_I','-AR','singular',None,'1pessoa','Morfologia_padrão')
# formacao_verbo_GAR('entregar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_GAR('entregar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_GAR('entregar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_GAR('entregar','imperativo_II','-AR','singular',None,'2pessoa')

###VERBOS TERMINADOS EM : 'RUIR'

def formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if verbo[-5:]=='truir' and tipo_de_orientacao == 'presente':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]
				MI = 'o'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-3)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ói'
				else:
					MI = 'óis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-3)]
				MI = 'ói'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-3)]
					MI = 'ói'
				else:
					ME = verbo[slice(-2)]
					MI = 'ímos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'ís'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-3)]
					MI = 'ói'
				else:
					ME = verbo[slice(-3)]+'o'
					MI = 'em'

	elif verbo[-4:]=='ruir' and tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]
				MI = 'o'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'i'
				else:
					MI = 'is'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-2)]
					MI = 'i'
				else:
					ME = verbo[slice(-2)]
					MI = 'ímos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'ís'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-2)]
					MI = 'i'
				else:
					ME = verbo[slice(-2)]
					MI = 'em'
	elif verbo[-5:]=='truir' and tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = 'ói'
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'í'
		else:
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif verbo[-4:]=='ruir' and tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-1)]
			MI = ''
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'í'
		else:
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif (verbo[-5:]=='truir' or
		verbo[-4:]=='ruir'):
		if tipo_de_orientacao == 'pretérito_imperfectivo':
			ME = verbo[slice(-2)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					MI = 'ía'

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'ías'

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'ía'

			elif OI_numero == 'plural':
				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'íamos'

				elif OI_tipo_de_pessoa == '2pessoa':
					MI = 'íeis'

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'íam'

		elif tipo_de_orientacao == 'pretérito_perfectivo_I':
			ME = verbo[slice(-2)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					MI = 'í'

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'iu'
					else:
						MI = 'íste'

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'iu'

			elif OI_numero == 'plural':
				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'iu'

					else:
						MI = 'ímos'

				elif OI_tipo_de_pessoa == '2pessoa':
					MI = 'ístes'

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'iu'
					else:
						MI = 'íram'

		elif tipo_de_orientacao == 'pretérito_perfectivo_II':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																	OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			MI ='í'+ MI[1:]

		elif tipo_de_orientacao == 'subjuntivo_condicional':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
																   OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			MI = 'í' + MI[1:]

		elif tipo_de_orientacao == 'subjuntivo_optativo':
			ME = verbo[slice(-2)]
			if (OI_tipo_de_pessoa=='2pessoa' and OI_numero=='singular' or
			OI_tipo_de_pessoa=='3pessoa' and OI_numero=='plural'):
				MI = 'í'+(realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)[1:])
			else:
				MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
																		   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'passado_volitivo':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
															 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'pretérito_imperfectivo':
			ME = verbo[slice(-2)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					MI = 'ía'

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'ías'

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'ía'

			elif OI_numero == 'plural':
				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'ímos'

				elif OI_tipo_de_pessoa == '2pessoa':
					MI = 'íeis'

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ía'
					else:
						MI = 'íam'

		elif tipo_de_orientacao == 'não_finito_concretizado':
			ME = verbo[slice(-2)]
			if (OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' or
			 OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
				MI = 'í'+(realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																	OI_tipo_de_pessoa, padrao_pessoa_morfologia)[1:])
			else:
				MI=realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																	OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'futuro':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
												   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
																  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'imperativo_II':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
														  OI_tipo_de_pessoa, padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'gerúndio':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
													 padrao_pessoa_morfologia)

		elif tipo_de_orientacao == 'particípio':
			ME = verbo[slice(-2)]
			MI = "í" + realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
													   padrao_pessoa_morfologia)[1:]

		elif tipo_de_orientacao == 'infinitivo':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
													   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
#
# verbo=formacao_verbo_RUIR('construir', 'presente', '-IR','plural' ,None, '3pessoa')
# verbo=formacao_verbo_RUIR('usufruir', 'presente', '-IR','plural' ,None, '3pessoa')
#
# verbo=formacao_verbo_RUIR('construir', 'subjuntivo_optativo', '-IR','plural' ,None, '3pessoa')
# verbo=formacao_verbo_RUIR('usufruir', 'subjuntivo_condicional', '-IR','plural' ,None, '3pessoa')
#
formacao_verbo_RUIR('construir', 'imperativo_I', '-IR','singular' ,None, '1pessoa')
# verbo=formacao_verbo_RUIR('usufruir', 'imperativo_I', '-IR','plural' ,None, '2pessoa')
#
#
# verbo=formacao_verbo_RUIR('construir', 'não_finito_concretizado', '-IR','singular' ,None, '2pessoa')
# verbo=formacao_verbo_RUIR('ruir', 'não_finito_concretizado', '-IR','singular' ,None, '2pessoa')


# #
# formacao_verbo_RUIR('construir','particípio','-IR','singular','masculino',None)
# formacao_verbo_RUIR('focar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_RUIR('focar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_RUIR('focar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_RUIR('focar','imperativo_II','-AR','singular',None,'2pessoa')

# VERBO agredir

def formacao_verbo_agredir(verbo, tipo_de_orientacao,padrao_de_morfologia, OI_numero,
                           genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	if tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'o'
				verbo = ME + 'id' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)] + 'id'

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)] + 'id'
				MI = 'e'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)] + 'id'
					MI = 'e'
					verbo = ME + MI
				else:
					ME = verbo[slice(-2)]
					MI = 'imos'
					verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)] + 'id'
					MI = 'e'
					verbo = ME + MI
				else:
					ME = verbo[slice(-2)]
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)] + 'id'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'a'
					verbo = ME + "ir" + MI
				else:
					ME = verbo[slice(-4)]
					MI = 'e'
					verbo = ME + "id" + MI
			else:
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + "id" + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'id' + MI
				else:
					MI = 'amos'
					verbo = ME + 'id' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'id' + MI

				else:
					MI = 'am'
					verbo = ME + 'id' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'id' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo
#
# formacao_verbo_agredir('agredir','particípio','plural','masculino',None)
# formacao_verbo_agredir('agredir','particípio','plural','masculino',None)
# formacao_verbo_agredir('agredir','particípio','singular','masculino',None)
# formacao_verbo_agredir('agredir','gerúndio',None,None,None)
# formacao_verbo_agredir('agredir', 'infinitivo', None, None, None)
# formacao_verbo_agredir('agredir', 'pretérito_perfectivo_II', 'singular', None, '1pessoa')
# formacao_verbo_agredir('agredir','pretérito_imperfectivo','singular',None,'1pessoa')

# VERBO aferir


def formacao_verbo_aferir(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'o'
				verbo = ME + 'ir' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'imos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)] + 'ir'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'a'
					verbo = ME + "ir" + MI
				else:
					ME = verbo[slice(-2)]
					MI = 'e'
					verbo = ME + MI
			else:
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + "ir" + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ir' + MI
				else:
					MI = 'amos'
					verbo = ME + 'ir' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ir' + MI

				else:
					MI = 'am'
					verbo = ME + 'ir' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'ir' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]

		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]

		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	return verbo


#
# formacao_verbo_aferir('aferir', 'não_finito_concretizado',  'singular', None, '2pessoa')
# formacao_verbo_aferir('aferir', 'subjuntivo_optativo',  'singular', None, '2pessoa')
# formacao_verbo_aferir('aferir', 'particípio',  'singular', 'masculino', None)
# formacao_verbo_agredir('aferir','particípio','singular','feminino',None)


# VERBO MEDIR
def formacao_verbo_medir(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-3)]
				MI = 'o'
				verbo = ME + 'ç' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'imos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	if tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)] + 'eç'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicionalsubjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'a'
					verbo = ME + "eç" + MI

				else:
					ME = verbo[slice(-2)]
					MI = 'e'
					verbo = ME + MI
			else:
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + "eç" + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'eç' + MI
				else:
					MI = 'amos'
					verbo = ME + 'eç' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'eç' + MI
			else:
				MI = 'am'
				verbo = ME + 'eç' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'eç' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	return verbo


# formacao_verbo_medir('medir','presente','-IR','singular',None,'2pessoa')


# VERBO sentir

def formacao_verbo_sentir(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-5)]+ 'int'
				MI = 'o'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'es'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

		elif OI_numero == 'plural':
			ME = verbo[slice(-2)]
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'imos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'is'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
					verbo = ME + MI
				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	if tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-5)] + 'int'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicionalsubjuntivo_condicional(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-5)] + "int"
					MI = 'a'
					verbo = ME + MI

				else:
					ME = verbo[slice(-2)]
					MI = 'e'
					verbo = ME + MI
			else:
				ME = verbo[slice(-4)] + "int"
				MI = 'a'
				verbo = ME + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)] + 'int'

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + MI
				else:
					MI = 'amos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'i'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa':
			ME = verbo[slice(-5)] + 'int'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + MI
			else:
				MI = 'am'
				verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-5)] + 'int'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
		                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	return verbo


#
# formacao_verbo_sentir('sentir','subjuntivo_conjuntivo','-IR','plural',None,'1pessoa')
# formacao_verbo_sentir('sentir','presente','-IR','singular',None,'3pessoa')
# formacao_verbo_sentir('sentir','presente','-IR','singular',None,'1pessoa')
# formacao_verbo_sentir('sentir', 'infinitivo','-IR',  'singular', 'masculino', None)
# formacao_verbo_sentir('sentir','particípio','-IR','singular','feminino',None)
# formacao_verbo_sentir('sentir','gerúndio','-IR',None,None,None)

# VERBO SABER
def formacao_verbo_saber(verbo, tipo_de_orientacao,padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'infinitivo':
		verbo = verbo

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	#

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                       padrao_pessoa_morfologia)

		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'ei'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-2)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'e'
				verbo = ME + MI

			else:
				MI = 'es'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-2)]
			MI = 'e'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

			else:
				ME = verbo[slice(-2)]
				MI = 'emos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'eis'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				ME = verbo[slice(-2)]
				MI = 'e'
				verbo = ME + MI

			else:
				ME = verbo[slice(-2)]
				MI = 'em'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-4)]
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			MI = 'oube'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oube'
				verbo = ME + MI

			else:
				MI = 'ste'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':

			MI = 'oube'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oube'
				verbo = ME + MI
			else:
				MI = 'oubemos'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			MI = 'oubestes'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oube'
				verbo = ME + MI

			else:
				MI = 'ouberam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-4)]
		if ((OI_tipo_de_pessoa == '1pessoa' or '3pessoa') and OI_numero == 'singular'):
			MI = 'oubera'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI
			else:
				MI = 'ouberas'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI
			else:
				MI = 'oubéramos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI

			else:
				MI = 'oubéreis'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubera'
				verbo = ME + MI

			else:
				MI = 'ouberam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':

		ME = verbo[slice(-4)]
		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'
				or OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			MI = 'oubesse'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubesses'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubésssemos'
				verbo = ME + MI
		#
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubésseis'
				verbo = ME + MI
		#
		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo = ME + MI
			else:
				MI = 'oubessem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
		                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'aib' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                        padrao_pessoa_morfologia)
		verbo = ME + 'oub' + MI
	#
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
		                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + 'oub' + MI

	elif tipo_de_orientacao == 'imperativo_I':

		ME = verbo[slice(-4)]
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + "aib" + MI
			else:
				MI = 'e'
				verbo = ME + 'ab' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			MI = 'a'
			verbo = ME + 'aib' + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'aib' + MI
			else:
				MI = 'amos'
				verbo = ME + 'aib' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			MI = 'ei'
			verbo = ME + 'ab' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'aib' + MI
			else:
				MI = 'am'
				verbo = ME + 'aib' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"
		else:
			MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
			                                              padrao_pessoa_morfologia)
		verbo = ME + 'aib' + MI

	return verbo


#
# formacao_verbo_saber('saber', 'pretérito_imperfectivo',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'presente',  'singular', None, '3pessoa')
# formacao_verbo_saber('saber', 'presente',  'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'particípio',  'singular', 'feminino', None)
# formacao_verbo_saber('saber', 'gerúndio',  None, None, None)
# formacao_verbo_saber('saber', 'não_finito_concretizado',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'futuro',  'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'passado_volitivo',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'pretérito_perfectivo_I',  'singular', None, '3pessoa')
# formacao_verbo_saber('saber', 'pretérito_perfectivo_II',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'subjuntivo_condicional',  'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'subjuntivo_conjuntivo',  'plural', None, '3pessoa')
# formacao_verbo_saber('saber', 'imperativo_II',  'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'imperativo_I',  'singular', None, '2pessoa')


# VERBO ESTAR

def formacao_verbo_estar(verbo, tipo_de_orientacao,padrao_de_morfologia,  OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	ME = verbo[slice(-2)]
	if tipo_de_orientacao == 'subjuntivo_condicional':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

				MI = 'esse'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
				verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
				verbo = ME + 'iv' + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

				MI = 'a'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI


	elif tipo_de_orientacao == 'imperativo_I':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ej' + MI
				else:
					MI = 'á'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'a'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				MI = 'ai'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI

	elif tipo_de_orientacao == 'imperativo_II':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'a'
				verbo = ME + 'ej' + MI
		if OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'ej' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':

		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

				MI = 'er'
				verbo = ME + 'iv' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
				verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'
				verbo = ME + 'iv' + MI

			if OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo = ME + 'iv' + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
				verbo = ME + 'iv' + MI
	elif tipo_de_orientacao == 'pretérito_imperfectivo':

		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
		                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'futuro':

		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
		                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':

		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':

				MI = 'ou'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'á'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '2pessoa'):

				MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
				                                         OI_tipo_de_pessoa, padrao_pessoa_morfologia)

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'ão'
			verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':

				MI = 'ive'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'eve'
				verbo = ME + MI
		if OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
				verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':

			if OI_tipo_de_pessoa == '1pessoa':

				MI = 'ivera'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				MI = 'ivera'
				verbo = ME + MI
		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'

				verbo = ME + MI
	elif tipo_de_orientacao == 'não_finito_concretizado':

		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                        padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':

		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':

		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	elif tipo_de_orientacao == 'particípio':

		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo
# formacao_verbo_estar('estar','presente','singular',None,'1pessoa')

# VERBO DIZER

def formacao_verbo_dizer(verbo, tipo_de_orientacao,padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':

			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-3)]
				MI = 'go'
				verbo = ME + MI


			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'es'
					verbo = ME + MI


			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]
				MI = ''
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'emos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'eis'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-2)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
					verbo = ME + MI

				else:
					MI = 'em'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'isse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == "3pessoa_do_singular":
					MI = 'isse'
					verbo = ME + MI

				else:
					MI = 'isseste'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'isse'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa':
			ME = verbo[slice(-4)]
			if padrao_pessoa_morfologia == "3pessoa_do_singular":
				MI = 'isse'
				verbo = ME + MI

			else:
				MI = 'issemos'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == "3pessoa_do_singular":
					MI = 'isse'
					verbo = ME + MI

				else:
					MI = 'issestes'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == "3pessoa_do_singular":
					MI = 'isse'
					verbo = ME + MI
				else:
					MI = 'isseram'
					verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ia'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ia'

				else:
					MI = 'ias'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'íamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ia'
				else:
					MI = 'íeis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ia'
				else:
					MI = 'iam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'issera'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'
					verbo = ME + MI

				else:
					MI = 'isseras'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'issera'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'
					verbo = ME + MI

				else:
					MI = 'isséramos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'
					verbo = ME + MI

				else:
					MI = 'isséreis'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issera'


				else:
					MI = 'isseram'

				verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'iria'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'irias'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iríamos'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iríeis'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iriam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
												OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI[1:]
	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'issesse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issesses'
				verbo = ME + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
					verbo = ME + MI

				else:
					MI = 'isséssemos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issésseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issessem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)]
		if OI_numero == 'singular':

			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):

				MI = 'a'
				verbo = ME + 'g' + MI

			elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'as'
					verbo = ME + 'g' + MI
		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'amos'
					verbo = ME + 'g' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'ais'
					verbo = ME + 'g' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'g' + MI
				else:
					MI = 'am'
					verbo = ME + 'g' + MI


	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
																padrao_pessoa_morfologia)
		verbo = ME + MI


	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':

			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
					verbo = ME + MI
				else:
					MI = 'iz'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'iga'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'izei'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igam'
				verbo = ME + MI


	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igas'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'iga'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = verbo[slice(-4)]
				MI = 'er'
				verbo = ME + 'iss' + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'eres'
					verbo = ME + 'iss' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'ermos'
				verbo = ME + 'iss' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo = ME + 'iss' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'erem'
				verbo = ME + 'iss' + MI
	elif tipo_de_orientacao == 'infinitivo':
		ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if genero == 'masculino':
				MI = 'ito'
			else:
				MI = 'ita'
		else:
			if genero == 'masculino':
				MI = 'itos'
			else:
				MI = 'itas'

		verbo = ME + MI
	return verbo
#
formacao_verbo_dizer('maldizer','presente','-ER','singular',None,'3pessoa')
#
# ##TESTE dizer
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# ###
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'presente',  numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_I',  numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_imperfectivo',  numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_II',  numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'passado_volitivo',  numero, None, tipo_pessoa))
#
# #futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'futuro',  numero, None, tipo_pessoa))
#
# #subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_conjuntivo',  numero, None, tipo_pessoa))
#
# #subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_condicional',  numero, None, tipo_pessoa))
#
#
# #subjuntivo_optativo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_optativo',  numero, None, tipo_pessoa))
#
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'imperativo_I',  numero, None, tipo_pessoa))
#
# # imperativo_II
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'imperativo_II',  numero, None, tipo_pessoa))
#
# # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'não_finito_concretizado',  numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_dizer('dizer', 'infinitivo',  numero, 'feminino', None))
#
# # gerúndio
# print(formacao_verbo_dizer('dizer', 'gerúndio',  None, None, None))
#
# # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_dizer('dizer', 'particípio',  numero, genero, None))
#

#VERBO CONTER DETER
def formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
					   OI_numero, genero, OI_tipo_de_pessoa,
					   padrao_pessoa_morfologia='Morfologia_padrão'):
	"""
    :return:
    """

	if tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'esse'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
			verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
			verbo = ME + 'iv' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
			verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
																padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'enh' + MI
				else:
					MI = 'em'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ende'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'inh' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'amos'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'eis'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'am'
					verbo = ME + 'inh' + MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
														 padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'enho'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'ens'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'em'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'endes'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'

			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ive'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'eve'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ivera'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'ivera'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo


###VERBO TRAZER

def formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
						   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	if tipo_de_orientacao == 'presente':

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]+'g'
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
													 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		else:
			if OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
				ME = verbo[slice(-2)]
				MI = ''
			else:
				ME = verbo[slice(-2)]
				MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
												 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-4)] + 'oux'
		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
			OI_tipo_de_pessoa == '3pessoa' and 	OI_numero == 'singular'):
				MI='e'
		else:
			MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-4)] + 'oux'
		MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-3)]+'r'
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
														 OI_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]+'r'
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
											   OI_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)] + 'g'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
															  OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)] + 'oux'
		MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
															   OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)] + 'oux'
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
															OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero =='singular':
			ME = verbo[slice(-2)]
			MI = ''
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero =='plural':
			ME = verbo[slice(-2)]
			MI = 'ei'
		else:
			ME = verbo[slice(-3)] + 'g'
			MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
													 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-3)] + 'g'
		MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
													  OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
																OI_tipo_de_pessoa, padrao_pessoa_morfologia)
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)

	verbo = ME + MI

	return verbo
#
# formacao_verbo_trazer('trazer','gerúndio','-ER',None,None,None)
# formacao_verbo_trazer('trazer','particípio','-ER','singular','feminino',None)
# print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None)
#
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'1pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'3pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'1pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'3pessoa','Morfologia_padrão')




















	verbo = ME + MI

	return verbo

# formacao_verbo_ÇAR('despedaçar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# formacao_verbo_ÇAR('abraçar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_I','-AR','plural',None,'3pessoa')
# formacao_verbo_ÇAR('abraçar','imperativo_II','-AR','singular',None,'2pessoa')
#


# VERBO TER

def formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                       OI_numero,genero, OI_tipo_de_pessoa,
                       padrao_pessoa_morfologia='Morfologia_padrão'):
	"""
    :return:
    """

	if tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'esse'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
			verbo = ME + 'iv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
			verbo = ME + 'iv' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
			verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'enh' + MI
				else:
					MI = 'em'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ende'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
				verbo = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
			verbo = ME+MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa' :

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME+'inh'+MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'amos'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'eis'
					verbo = ME + 'ính' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'inh' + MI
				else:
					MI = 'am'
					verbo = ME + 'inh' + MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'enho'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'ens'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'em'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'endes'

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'

			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ive'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'eve'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ivera'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'ivera'
			verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'

			elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'
			verbo = ME + MI
	###
	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	return verbo

#
# ##TESTE ter
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# #presente
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'presente', '-ER', numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_optativo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_ter('ter', 'infinitivo', '-ER', numero, 'feminino', None))
#
# # # gerúndio
# print(formacao_verbo_ter('ter', 'gerúndio', '-ER', None, None, None))
# #
# # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None))

# ####################################################################################

# VERBO SER

def formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao == 'infinitivo':
		ME=verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		if OI_numero == 'singular':
			ME = 'er'
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + MI

		elif OI_numero == 'plural':

			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'eis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'er'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                       padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                                 padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]

		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia,OI_numero, genero,
		                                           OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-2)]
				MI = 'ou'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = ''
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'é'
				else:
					MI = 'és'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = ''
				MI = 'é'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo[slice(-2)]
					MI = 'omos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				MI = 'ois'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo[slice(-2)]
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':

		ME = 'f'
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ui'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'oi'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
					verbo = ME + MI
				else:
					MI = 'omos'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ostes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ora'
				verbo = ME + MI


			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_condicional':

		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'osse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
					verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia="Morfologia_padrão")
		verbo = ME + 'ej' + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'or'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo = ME + MI



		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ej' + MI
				else:
					MI = 'ê'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'ede'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = verbo[slice(-2)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'ej' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
				MI = 'ais'
				verbo = ME + 'ej' + MI

			elif OI_tipo_de_pessoa == '3pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ej' + MI

	return verbo

# # ##TESTE ser
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # #presente
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# #
# # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_optativo
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ser('ser', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # infinitivo
# print(formacao_verbo_ser('ser', 'infinitivo', '-ER', numero, 'feminino', None))
# #
# # # # gerúndio
# print(formacao_verbo_ser('ser', 'gerúndio', '-ER', None, None, None))
# # #
# # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_ser('ser', 'particípio', '-ER', numero, genero, None))

# ####################################################################################

# VERBO IR

def formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = MI
	###
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = MI
	###
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero,
		                                         OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero,
		                                           genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				MI = 'ou'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'ais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				MI = 'ai'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = 'i'
				MI = 'des'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'am'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = 'f'
				MI = 'ui'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'f'
				MI = 'oi'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'omos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'ostes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'f'

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = 'f'
				MI = 'ora'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'osse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if  OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = 'v'
				MI = 'á'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia,
		                                                        OI_numero, OI_tipo_de_pessoa,     padrao_pessoa_morfologia)
		verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ai'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				MI = 'á'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = 'i'
				MI = 'de'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'imperativo_II':
		ME = 'v'
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'á'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo = ME + MI
	###
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'or'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo = ME + MI

	return verbo
# #
# # #
# # # # ##TESTE ir
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'presente', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'futuro', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ir('ir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# #
# # # # # infinitivo
# # print(formacao_verbo_ir('ir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # #
# # # # # # gerúndio
# # print(formacao_verbo_ir('ir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# # # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_ir('ir', 'particípio', '-IR', numero, genero, None))




# VERBOS VIR E INTERVIR


def formacao_verbo_vir_intervir(verbo, tipo_de_orientacao,padrao_de_morfologia,
                                OI_numero,genero, OI_tipo_de_pessoa,
                                padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	ME = verbo[slice(-2)]

	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero,
		                                           OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'inha'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inhas'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínhamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínheis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inham'
				verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero,
		                                         OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		if OI_numero == 'singular':
			if genero == 'masculino':
				MI = 'indo'
			else:
				MI = 'inda'
		else:
			if genero == 'masculino':
				MI = 'indos'
			else:
				MI = 'indas'
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'enho'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if verbo == 'vir':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'em'
					else:
						MI = 'ens'
					verbo = ME + MI
				else:
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'ém'
					else:
						MI = 'éns'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if verbo == 'vir':
					MI = 'em'
				else:
					MI = 'ém'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'imos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'indes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'im'
				verbo = ME + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieste'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'eio'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'iemos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'iestes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieram'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'iera'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieras'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéramos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéreis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieram'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa'or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'iesse'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iesses'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iéssemos'
				verbo = ME + '' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'iésseis'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iessem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhas'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enham'
				verbo = ME + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa' :
				if verbo =='vir':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
						verbo = ME + 'enh' + MI
					else:
						MI = 'em'
						verbo = ME + MI
				else:
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
						verbo = ME + 'enh' + MI
					else:
						MI = 'ém'
						verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'enhamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'inde'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'enh' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'a'
				verbo = ME + 'enh' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = verbo = ME + 'enh' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = verbo = ME + 'enh' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ier'
				verbo = ME + MI

			if OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ieres'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'iermos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierdes'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierem'
				verbo = ME + MI
	return verbo

#
# # #
# # # # ##TESTE intervir
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('intervir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_vir_intervir('intervir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_vir_intervir('intervir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_vir_intervir('intervir', 'particípio', '-IR', numero, genero, None))
#
# ######################################
#
#
# # # # ##TESTE vir
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_vir_intervir('vir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_vir_intervir('vir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_vir_intervir('vir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_vir_intervir('vir', 'particípio', '-IR', numero, genero, None))


# VERBO HAVER
def formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                         OI_numero,genero, OI_tipo_de_pessoa,
                         padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = 'ido'
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':
		if OI_numero == 'singular':
			ME = verbo[slice(-4)]
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'ei'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'á'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'á'
				else:
					ME = verbo[slice(-2)]
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					ME = verbo[slice(-4)]
					MI = 'á'
				else:
					ME = verbo[slice(-2)]
					MI = 'eis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'ão'

		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'e'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'este'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'e'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'estes'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'eram'

		verbo = ME + 'ouv' + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				MI = 'era'

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'eras'


			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'era'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éreis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'eram'
		verbo = ME + 'ouv' + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '2pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = verbo[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
				verbo = ME + 'ouv' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
					verbo = ME + 'ud' + MI
				else:
					MI = 'éssemos'
					verbo = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
				verbo = ME + 'ouv' + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa'  or
					OI_tipo_de_pessoa == '3pessoa'):
				ME = verbo[slice(-4)]
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo = ME + 'aj' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ais'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'aj' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
		                                                        OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'aj' + MI
				else:
					MI = 'á'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + 'aj' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				MI = 'ei'
				verbo = ME + 'av' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'aj' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'a'
				verbo = ME + 'aj' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + MI
				else:
					MI = 'amos'
					verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo = ME + 'aj' + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'aj' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa'  or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo = ME + 'ouv' + MI

	return verbo

# # # # # ##TESTE haver
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_haver('haver', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # infinitivo
# print(formacao_verbo_haver('haver', 'infinitivo', '-ER', numero, 'feminino', None))
# # # #
# # # # # # # gerúndio
# print(formacao_verbo_haver('haver', 'gerúndio', '-ER', None, None, None))
# # # # # #
# # # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_haver('haver', 'particípio', '-ER', numero, genero, None))

# VERBO PODER

def formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                         OI_numero, genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
		                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero,
		                                         OI_numero, OI_tipo_de_pessoa,
		                                         padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero,
		                                           genero, OI_tipo_de_pessoa,
		                                           padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia,
			                                         OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			verbo = ME +'ss'+ MI


		else:
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia,
			                                         OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'ude'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udeste'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'ôde'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'uderam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				MI = 'udera'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'uderas'

			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'udera'

		elif OI_numero =='plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'udéramos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'udéreis'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'uderam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '2pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):

				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
				verbo = ME + 'ud' + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '3pessoa' :
				MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
				                                                       OI_tipo_de_pessoa,
				                                                       padrao_pessoa_morfologia)
				verbo = ME + 'ud' + MI

			elif OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo = ME + 'ud' + MI

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo = ME + 'ud' + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-4)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'ossa'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossas'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ode'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'ossa'
				verbo = ME + MI

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				MI = 'odei'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa == '2pessoa':

				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossas'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'ossa'
				verbo = ME + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossais'
				verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia,
		                                                    OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME +'ud'+MI

	return verbo


# # # # ##TESTE poder
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # # #presente
# # # print("A conjugação é:")
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # subjuntivo_optativo
# # # # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_poder('poder', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # # infinitivo
# print(formacao_verbo_poder('poder', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # gerúndio
# print(formacao_verbo_poder('poder', 'gerúndio', '-ER', None, None, None))
# # # # # # #
# # # # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_poder('poder', 'particípio', '-ER', numero, genero, None))
#





# VERBO FAZER


def formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao == 'presente':
		if OI_numero  == 'singular':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-3)]
				MI = 'ço'
			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-2)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = ''
				else:
					MI = 'es'
			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'az'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-2)]
				MI = 'emos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				MI = 'azeis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'azem'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		if OI_numero=='singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'iz'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izeste'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				MI = 'ez'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izemos'

			elif OI_tipo_de_pessoa == '2pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izestes'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izeram'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				ME = verbo[slice(-4)]
				MI = 'izera'

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izeras'

			elif OI_tipo_de_pessoa == '3pessoa' :
				ME = verbo[slice(-4)]
				MI = 'izera'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izéramos'

			elif OI_tipo_de_pessoa == '2pessoa' :
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izéreis'

			elif OI_tipo_de_pessoa == '3pessoa':
				ME = verbo[slice(-4)]
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'izeram'
		verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]
		MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)[slice(1,7)]
		verbo = ME + MI

	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'aria'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'aria'
				else:
					MI = 'arias'
			elif OI_tipo_de_pessoa == '3pessoa':
				MI = 'aria'


		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'aríamos'
			elif OI_tipo_de_pessoa == '2pessoa' :
				MI = 'aríeis'
			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'ariam'
		verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		ME = verbo[slice(-4)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'izesse'

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izesses'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izéssemos'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izésseis'

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izessem'
		verbo = ME+MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		ME = verbo[slice(-3)]
		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'

			elif OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				MI = 'amos'
			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
		verbo = ME + 'ç' + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		ME = verbo[slice(-4)]

		if OI_numero == 'singular':
			if (OI_tipo_de_pessoa == '1pessoa' or
					OI_tipo_de_pessoa == '3pessoa'):
				MI = 'er'
			if OI_tipo_de_pessoa == '2pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa == '3pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo = ME + 'iz' + MI

	elif tipo_de_orientacao == 'imperativo_I':
		ME = verbo[slice(-3)]
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '1pessoa':
				verbo = 'Imperativos não selecionam 1pessoa do singular.'

			elif OI_tipo_de_pessoa == '2pessoa' :

				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ç' + MI
				else:
					MI = 'z'
					verbo = ME + MI

			elif OI_tipo_de_pessoa == '3pessoa' :
				MI = 'a'
				verbo = ME + 'ç' + MI
		elif OI_numero == 'plural':
			if OI_tipo_de_pessoa == '1pessoa' :
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo = ME + 'ç' + MI

			elif OI_tipo_de_pessoa == '2pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
					verbo = ME + 'ç' + MI
				else:
					MI = 'ei'
					verbo = ME + 'z' + MI


			elif OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo = ME + 'ç' + MI

	elif tipo_de_orientacao == 'imperativo_II':
		if tipo_de_orientacao == 'imperativo_II':
			ME = verbo[slice(-3)]
			if OI_numero == 'singular':
				if OI_tipo_de_pessoa == '1pessoa':
					verbo = 'Imperativos não selecionam 1pessoa do singular. Selecione novamente:'
				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'as'
					verbo = ME + 'ç' + MI

				elif OI_tipo_de_pessoa == '3pessoa':
					MI = 'a'
					verbo = ME + 'ç' + MI

			elif OI_numero == 'plural':

				if OI_tipo_de_pessoa == '1pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'amos'
					verbo = ME + 'ç' + MI

				elif OI_tipo_de_pessoa == '2pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'ais'
					verbo = ME + 'ç' + MI

				elif OI_tipo_de_pessoa == '3pessoa':
					if padrao_pessoa_morfologia == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'am'
					verbo = ME + 'ç' + MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'infinitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'gerúndio':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
		verbo = ME + MI

	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-4)]
		if OI_numero == 'singular':
			if genero == 'feminino':
				MI = 'eita'
			elif genero == 'masculino':
				MI = 'eito'
		elif OI_numero == 'plural':
			if genero == 'feminino':
				MI = 'eitas'
			elif genero == 'masculino':
				MI = 'eitos'
		verbo = ME + MI
	return verbo

# #
# #
# # # # # # ##TESTE fazer
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # # ###
# # # # # # #presente
# # # # print("A conjugação é:")
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # ###
# # # # print("A conjugação pretérito_perfectivo_I é:")
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # # #
# # # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # # futuro
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # subjuntivo_optativo
# # # # # #
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # # não_finito_concretizado
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_fazer('fazer', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # infinitivo
# print(formacao_verbo_fazer('fazer', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # # gerúndio
# print(formacao_verbo_fazer('fazer', 'gerúndio', '-ER', None, None, None))
# # # # # # # #
# # # # # # # # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_fazer('fazer', 'particípio', '-ER', numero, genero, None))
#

#################################################################################

def formacao_da_estrutura_do_verbo_modal(TIPO_DE_EXPERIENCIA,verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if (TIPO_DE_EXPERIENCIA == 'Ser' or
			TIPO_DE_EXPERIENCIA == 'Fazer' or
			TIPO_DE_EXPERIENCIA == 'Sentir'):

		if verbo == 'dever':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
			                                         OI_tipo_de_pessoa, padrao_pessoa_morfologia="Morfologia_padrão")
			verbo = ME + MI

		elif verbo == 'poder':
			verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
			                                   OI_numero, genero, OI_tipo_de_pessoa,
			                                   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'haver':
			verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
			                                   OI_numero, genero, OI_tipo_de_pessoa,
			                                   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'ter':

			verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
			                                 OI_numero, genero, OI_tipo_de_pessoa,
			                                 padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
	# elif verbo == 'ter de':
	# 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
	# 	                           OI_numero, genero, OI_tipo_de_pessoa,
	# 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
	return verbo


# formacao_da_estrutura_do_verbo_modal('Sentir','poder','presente','-ER','singular',None,'1pessoa')

def formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	padrao_de_morfologia=detecta_padrao_morfologia(verbo)
	if verbo == 'estar':
		verbo = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'ter':
		verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'haver':
		verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'ir':
		verbo = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'vir':
		verbo = formacao_verbo_vir_invervir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	elif verbo == 'ser':
		verbo = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

	return verbo
#
# formacao_da_estrutura_do_verbo_AUX('estar','presente','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo_AUX('ser','presente','singular',None,'1pessoa','Morfologia_padrão')

def formacao_verbo_participio(verbo, tipo_de_orientacao, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):

	ME = verbo[slice(-2)]
	padrao_de_morfologia=detecta_padrao_morfologia(verbo)
	MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa=None,padrao_pessoa_morfologia='Morfologia_padrão')
	verbo_participio = ME + MI

	return verbo_participio

# #
# formacao_verbo_participio("cortar",'particípio','singular','masculino',None)


def formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
                                       genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''
	padrao_de_morfologia = detecta_padrao_morfologia(verbo)
	if  (tipo_de_orientacao == 'imperativo_I' and OI_numero == 'singular' and OI_tipo_de_pessoa == '1pessoa' or
		tipo_de_orientacao == 'imperativo_II' and OI_numero == 'singular' and OI_tipo_de_pessoa == '1pessoa'):
			verbo_conj='-'
	else:
		if verbo == 'estar':
				verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia,
													 OI_numero,
													 genero, OI_tipo_de_pessoa,
													 padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'ter':
			verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero,
											   genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'haver':
			verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
												 OI_numero,
												 genero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'ir':
			verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											  OI_numero,
											  genero, OI_tipo_de_pessoa,
											  padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'vir':
			verbo_conj = formacao_verbo_vir_invervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
														OI_numero,
														genero, OI_tipo_de_pessoa,
														padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo == 'ser':
			verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero,
											   genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia='Morfologia_padrão')
		elif verbo[-5:] == 'fazer':
			verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
										 OI_numero, genero, OI_tipo_de_pessoa,
										 padrao_pessoa_morfologia)

		elif verbo == None:
			verbo_conj = ''
		else:

			OE_experiencia_do_verbo = experiencia_do_verbo(verbo)
			OI_orientacao_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo(tipo_de_orientacao,
																					  padrao_de_morfologia,
																					  OI_numero,
																					  genero, OI_tipo_de_pessoa,
																					  padrao_pessoa_morfologia)
			verbo_conj = OE_experiencia_do_verbo + OI_orientacao_interpessoal_do_verbo
	return verbo_conj
#
# formacao_da_estrutura_do_verbo('andar','imperativo_I','singular',None,'3pessoa')
# formacao_da_estrutura_do_verbo('comer','pretérito_imperfectivo','plural',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','presente','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','gerúndio',None,None,None)
# formacao_da_estrutura_do_verbo('cortar', 'particípio',  'singular', 'feminino', None)
# verbo = formacao_verbo_sentir('sentir', 'subjuntivo_conjuntivo', '-IR', 'plural',
# 								  None, '1pessoa')

def verbo_geral(TIPO_DE_EXPERIENCIA=None, funcao_no_grupo_verbal=None, verbo=None,
                tipo_de_orientacao=None, OI_numero=None, genero=None, OI_tipo_de_pessoa=None,
                padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna a estrutura que realiza os verbos no português.
    '''
	classe_do_verbo = def_classe_de_verbo(funcao_no_grupo_verbal)
	padrao_de_morfologia = detecta_padrao_morfologia(verbo)
	if classe_do_verbo == 'lexical':
		if (TIPO_DE_EXPERIENCIA == 'Ser' or
				TIPO_DE_EXPERIENCIA == 'Fazer' or
				TIPO_DE_EXPERIENCIA == 'Sentir'):
			if verbo == 'estar':
				verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
											 genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'sentir':
				verbo_conj = formacao_verbo_sentir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
								  genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'trazer':
				verbo_conj = formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
								  genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'ter':
				verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
										   OI_numero, genero, OI_tipo_de_pessoa,
										   padrao_pessoa_morfologia)
			elif verbo == 'ser':
				verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
										   OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'ir':
				verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
										  genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
			elif verbo == 'haver':
				verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)
			elif verbo == 'agredir':
				verbo_conj = formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
			elif verbo == 'aferir':
				verbo_conj = formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											  OI_numero, genero, OI_tipo_de_pessoa,
											  padrao_pessoa_morfologia)
			elif verbo == 'medir':
				verbo_conj = formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)
			elif verbo == 'saber':
				verbo_conj = formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia)
			elif (verbo == 'vir' or verbo == 'intervir'):
				verbo_conj = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
													OI_numero, genero, OI_tipo_de_pessoa,
													padrao_pessoa_morfologia)
			elif (verbo == 'conter' or verbo == 'deter'):
				verbo_conj = formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
													OI_numero, genero, OI_tipo_de_pessoa,
													padrao_pessoa_morfologia)
			elif verbo == 'poder':
				verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
												  OI_numero, genero, OI_tipo_de_pessoa,
												  padrao_pessoa_morfologia)

			else:
				if verbo[-4:] == 'ruir':

					verbo_conj = formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia,
												OI_numero, genero, OI_tipo_de_pessoa,
												padrao_pessoa_morfologia)

				elif verbo[-3:] == 'car':
					verbo_conj = formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
				elif verbo[-5:] == 'fazer':
					verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
												 OI_numero, genero, OI_tipo_de_pessoa,
												 padrao_pessoa_morfologia)
				elif verbo[-3:] == 'gar':
					verbo_conj = formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)
				elif verbo[-3:] == 'çar':
					verbo_conj = formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)

				elif verbo[-3:] == 'cer':
					verbo_conj = formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia,
											   OI_numero, genero, OI_tipo_de_pessoa,
											   padrao_pessoa_morfologia)

				elif verbo[-5:] == 'dizer':
					verbo_conj = formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
												 genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
				else:
					verbo_conj = formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
																genero, OI_tipo_de_pessoa,
																padrao_pessoa_morfologia)
	elif classe_do_verbo == 'modal':
		if (TIPO_DE_EXPERIENCIA == 'Ser' or
				TIPO_DE_EXPERIENCIA == 'Fazer' or
				TIPO_DE_EXPERIENCIA == 'Sentir'):

			if verbo == 'dever':
				ME = verbo[slice(-2)]
				MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
														 OI_tipo_de_pessoa,
														 padrao_pessoa_morfologia="Morfologia_padrão")
				verbo_conj = ME + MI

			elif verbo == 'poder':
				verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia='Morfologia_padrão')

			elif verbo == 'haver':
				verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
											 OI_numero, genero, OI_tipo_de_pessoa,
											 padrao_pessoa_morfologia='Morfologia_padrão')

			elif verbo == 'ter':

				verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
										   OI_numero, genero, OI_tipo_de_pessoa,
										   padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
	# elif verbo == 'ter de':
	# 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
	# 	                           OI_numero, genero, OI_tipo_de_pessoa,
	# 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
	elif classe_do_verbo == 'auxiliar':
		verbo_conj = formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
												   genero, OI_tipo_de_pessoa,
												   padrao_pessoa_morfologia)
	else:
		verbo_conj = ''
	return verbo_conj


# #EXEMPLOS
# print(verbo_geral("Fazer", 'Evento', 'desmatar', 'pretérito_perfectivo_I', 'singular', None, '3pessoa'))
# 'desmatou'
#
#
#
# verbo_geral("Fazer", 'Evento', "identificar","imperativo_I", 'singular', None, '1pessoa')

#
# verbo=verbo_geral("Fazer",'Evento','usufruir','imperativo_I','singular',None,'2pessoa')
# # verbo_geral("Fazer",'Evento','espaçar','imperativo_I','plural',None,'3pessoa')
# # formacao_verbo_ÇAR('espaçar', 'imperativo_I', '-AR','plural',None,'3pessoa')

# verbo_geral("Fazer",'Evento','desfazer','pretérito_perfectivo_II','plural',None,'1pessoa')
# # # verbo_geral("Fazer",'Evento','ficar','pretérito_perfectivo_I','singular',None,'1pessoa')
# verbo_geral("Fazer",'Evento','abraçar','presente','singular',None,'1pessoa')
# verbo_geral('Ser','Auxiliar','ter','passado_volitivo','singular',None,'1pessoa')
# verbo_geral('Fazer','Evento','ir','passado_volitivo','singular',None,'1pessoa')
# verbo_geral('Fazer','Evento','cortar', 'particípio', 'singular', 'feminino',None)
# verbo_geral('Ser','Evento','ser', 'particípio', 'singular','masculino', '1pessoa')
# verbo_geral('Sentir','Evento','enternecer','presente','singular',None,'2pessoa')
# verbo_geral('Sentir','Evento','poder','presente','singular',None,'2pessoa')
# verbo_geral(None,None,None,None,None,None,None,None)

#####ORDEM DO GRUPO#####
#    grupo verbal

#
# print('Qual de Agência?')
# 	AGENCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não-agenciado']).ask()
#
# print('Qual o verbo auxiliar de AGÊNCIA passiva desejado?')
# 		auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()
#
# print('Qual o verbo auxiliar de AGENCIA passiva desejado?')
# 	auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()

def realizacao_de_AGENCIA_passiva(verbo_AUX, tipo_de_orientacao_AUX, OI_numero_AUX,
                                  genero_AUX, OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX,
                                  TIPO_DE_EXPERIENCIA_LEX,funcao_no_grupo_verbal_POS_FINAL,  verbo_LEX,
                                  tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX,
                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''
    '''
	verbo_auxiliar_passiva = formacao_da_estrutura_do_verbo_AUX(verbo_AUX,  tipo_de_orientacao_AUX,
	                                                            OI_numero_AUX,
	                                                            genero_AUX, OI_tipo_de_pessoa_AUX,
	                                                            padrao_pessoa_morfologia_AUX)

	verbo_lexical = verbo_geral( TIPO_DE_EXPERIENCIA_LEX,funcao_no_grupo_verbal_POS_FINAL, verbo_LEX,
                    tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                    padrao_pessoa_morfologia_LEX)

	grupo_verbal_AGENCIA_passiva = verbo_auxiliar_passiva + ' ' + verbo_lexical
	return grupo_verbal_AGENCIA_passiva
#
# # #
# formacao_da_estrutura_do_verbo_AUX('ser','particípio','singular','masculino',None,'Morfologia_padrão')
# verbo_geral("Fazer",'Evento','levar','particípio','singular','masculino',None,'Morfologia_padrão')
# # # #
# realizacao_de_AGENCIA_passiva('ser','particípio','singular','masculino',None,'Morfologia_padrão','Fazer','Evento','levar','particípio','singular','masculino',None,'Morfologia_padrão')

# #




# partindo do sistema

##para grupo verbal, fiz seleções nos sistemas de tempo secundário e agenciamento
# pq as outras seleções já são feitas na ordem da palavra verbal(ficaria redundante)

# print('Qual o tipo_pessoa de evento desejado para o grupo verbal?')
# 	TIPO_DE_EVENTO = choice.Menu(['Ser', 'Fazer', 'Sentir']).ask()
# print('Selecione um lema verbal que realize o tipo_pessoa de evento desejado:')
# 		print('Qual a agência do GV?')
# 		AGÊNCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não_agenciado_passiva',
# 		                       'não_agenciado']).ask()
# print('Há a seleção de  tempo secundário')
# 			TEMPO_SECUNDARIO = choice.Menu(['-', '1_reiteração', '2_reiterações',
# 			                                '3_reiterações', '4_reiterações']).ask()
# print('Dêixis modal = não_modalizada')
# 				print('Selecione a finitude')
# 				FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
#
# print('Qual a dêixis temporal?')
# 					DEIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
# print('Qual o aspecto verbal?')
# 					ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
#
# print('Selecione o tipo_pessoa de OI não-orientação desejada')
# 						não_orientado = choice.Menu(['infinitivo', 'gerúndio'])


					#############


# Observação importante sobre o desenvolvimento da função de grupo verbal: Como os sistemas de
# FINITUDE,DEIXIS_TEMPORAL, ASPECTO na ordem do grupo são 'síndromes' de significados que reverberam
#desde o morfema, resolvi não repetir por uma questão de custo de desenvolvimento().
#########################################


def grupo_verbal(TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None,
				 funcao_no_grupo_verbal_1=None, verbo_1=None, tipo_de_orientacao_1=None,
				 OI_numero_1=None,genero_1=None, OI_tipo_de_pessoa_1=None,
				 padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None,
				 funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None,
				 OI_numero_2=None,genero_2=None, OI_tipo_de_pessoa_2=None,
				 padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None,
				 funcao_no_grupo_verbal_3=None, verbo_3=None, tipo_de_orientacao_3=None,
				 OI_numero_3=None,genero_3=None, OI_tipo_de_pessoa_3=None,
				 padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None,
				 funcao_no_grupo_verbal_4=None, verbo_4=None, tipo_de_orientacao_4=None,
				 OI_numero_4=None,genero_4=None, OI_tipo_de_pessoa_4=None,
				 padrao_pessoa_morfologia_4=None,TIPO_DE_EXPERIENCIA_LEX=None,
				 funcao_no_grupo_verbal_POS_FINAL=None, verbo_LEX=None,
				 tipo_de_orientacao_LEX=None, OI_numero_LEX=None,
				 genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
				 padrao_pessoa_morfologia_LEX='Morfologia_padrão'):

	try:
		if TIPO_DE_EXPERIENCIA_GV == 'Ser' or TIPO_DE_EXPERIENCIA_GV == 'Fazer'	or TIPO_DE_EXPERIENCIA_GV == 'Sentir':

			if AGENCIA == 'agenciado_ativa' or AGENCIA == 'não_agenciado':

				verbo1 = verbo_geral(TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1,
					 tipo_de_orientacao_1,  OI_numero_1, genero_1,
					 OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
				verbo2 = verbo_geral(TIPO_DE_EXPERIENCIA_2,
									 funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2,
									 OI_numero_2,
									 genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
				verbo3 = verbo_geral(TIPO_DE_EXPERIENCIA_3,
									 funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3,
									 OI_numero_3,
									 genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)
				verbo4 = verbo_geral(TIPO_DE_EXPERIENCIA_4,
									 funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4,
									 OI_numero_4,
									 genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4)
				Evento = verbo_geral(TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
									 verbo_LEX, tipo_de_orientacao_LEX,
									 OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX
									 , padrao_pessoa_morfologia_LEX)

				grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento

			else:
				tipo_de_orientacao_LEX = 'particípio'
				verbo_4 = 'ser'
				verbo1 = verbo_geral(TIPO_DE_EXPERIENCIA_1,
									 funcao_no_grupo_verbal_1,
									 verbo_1, tipo_de_orientacao_1,  OI_numero_1,
									 genero_1, OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
				verbo2 = verbo_geral(TIPO_DE_EXPERIENCIA_2,
									 funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2,
									 OI_numero_2,
									 genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
				verbo3 = verbo_geral(TIPO_DE_EXPERIENCIA_3,
									 funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3,
									 OI_numero_3,
									 genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)

				verbos_passiva = realizacao_de_AGENCIA_passiva(verbo_4, tipo_de_orientacao_4,
															   OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
															   padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX,
															   funcao_no_grupo_verbal_POS_FINAL, verbo_LEX,
															   tipo_de_orientacao_LEX,
															   OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
															   padrao_pessoa_morfologia_LEX)


				grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva
		return (re.sub(' +', ' ', grupo_verbal).strip())
	except:
		return ''
# grupo_verbal('Fazer', 'agenciado_passiva', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'Ser', 'Auxiliar', 'ser', 'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'Fazer', 'Evento', 'desmatar', 'particípio', 'singular', 'masculino', None, 'Morfologia_padrão')
# grupo_verbal(TIPO_DE_EXPERIENCIA_GV='Fazer', AGENCIA='não_agenciado', TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None, verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None,genero_1=None, OI_tipo_de_pessoa_1=None, padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None, OI_numero_2=None,genero_2=None, OI_tipo_de_pessoa_2=None, padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None, tipo_de_orientacao_3=None, OI_numero_3=None,genero_3=None, OI_tipo_de_pessoa_3=None, padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4='Ser', funcao_no_grupo_verbal_4='Auxiliar', verbo_4='ter', tipo_de_orientacao_4='presente', OI_numero_4='singular',genero_4=None, OI_tipo_de_pessoa_4='1pessoa', padrao_pessoa_morfologia_4='Morfologia_padrão',TIPO_DE_EXPERIENCIA_LEX='Fazer', funcao_no_grupo_verbal_POS_FINAL='Evento', verbo_LEX='pensar', tipo_de_orientacao_LEX='particípio', OI_numero_LEX='singular', genero_LEX='masculino', OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX='Morfologia_padrão')

# grupo_verbal('Fazer', 'não_agenciado', None, None, None, None, None, None,
# 			 None, None, None, None, None, None, None, None, None,
# 			 None, None, None, None, None, None, None, None, None, 'Ser', 'Auxiliar',
# 			 'ter', 'presente', 'singular', None, '1pessoa',
# 			 'Morfologia_padrão', 'Fazer', 'Evento', 'pensar', 'particípio', 'singular',
# 			 'masculino', None, 'Morfologia_padrão')

# grupo_conjuntivo(tipo_insercao='inserção_menu', conj_extenso=None,tipo_de_conjuncao="hipotática_relativa",indice=2)
#
# #
# # ###ESSE TRECHO QUE SEGUE É PRA GUARDAR PRO CASO DE PRECISAR FICAR MAIS ESPECÍFICO NO GRUPO_VERBAL
# # #
# # # print ('Quais tempos secundários?')
# # #        TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro', 'tempo_secundário_não_orientado']).ask()
# # #        compilação_TEMPORAL = []
# # #
# # #
# # #        while  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'tempo_secundário_DT_presente' or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_passado'or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_futuro' or TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_não_orientado':
# # #            compilação_TEMPORAL= [TEMPO_PRIMÁRIO,TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL]
# # #            TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro']).ask()
# # #            if TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'NA':
# # #                break
# # #
# # #
# # #        if AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '+':
# # #            grupo_verbal = verbo_geral () + ' ' + verbo_geral ()
# # #
# # #    return  grupo_verbal
# # #
# #
# # # #####################################
# #
#####ex###

#levo
#
# grupo_verbal(TIPO_DE_EXPERIENCIA_GV='Fazer',AGENCIA="agenciado_ativa",TIPO_DE_EXPERIENCIA_LEX="Fazer",funcao_no_grupo_verbal_POS_FINAL="Evento",verbo_LEX='trazer',tipo_de_orientacao_LEX='presente',OI_numero_LEX='singular',OI_tipo_de_pessoa_LEX='1pessoa')
#
# grupo_verbal('Fazer', 'agenciado_passiva', None, None, None,
#              None, None, None, None, None, None, None, None,None, None, None, None, None, None, None, None, None,
#              None, None, None, None, 'Ser', 'Auxiliar', 'ser', 'pretérito_perfectivo_I',
#              'singular', None, '3pessoa', 'Morfologia_padrão', 'Fazer', 'Evento',
#              'desmatar', 'particípio', 'singular', 'masculino',None,'Morfologia_padrão')

# # #estava sendo levado
#
# grupo_verbal('Fazer', 'agenciado_passiva', 'Ser', 'Auxiliar', 'estar',
#                  'pretérito_imperfectivo', '-AR', 'singular', None,
#                  '1pessoa', 'Morfologia_padrão', None, None,
#                  None, None, None, None, None, None,
#                  None, None, None, None,
#                  None, None, None, None, None,
#                  None, 'Ser', 'Auxiliar', 'ser','gerúndio','-ER',
#              'singular',None,'1pessoa','Morfologia_padrão','Fazer','Evento',
#              'levar','particípio','-AR','singular','masculino',None,'Morfologia_padrão')
#
# #'deveria ter sido levado'
# grupo_verbal('Fazer', 'agenciado_passiva', "Fazer", 'Modal', 'dever', 'passado_volitivo', '-ER', 'singular', None,
#              '1pessoa', "Morfologia_padrão", 'Ser', 'Auxiliar', 'ter', 'infinitivo', '-ER', None, None, None, None,
#              None, None, None,None, None, None, None, None, None, 'Ser', 'Auxiliar', 'ser', 'particípio', '-ER', 'singular', 'masculino', None, 'Morfologia_padrão',  "Fazer", 'Evento', 'levar', 'particípio', '-AR', 'singular', 'masculino', None, 'Morfologia_padrão')


#
# #
# ####

###########################################
#

def adverbio_modo(indice=None):
	opcoes = ['bem','mal','assim','adrede',
			  'melhor','pior','depressa','devagar',
			  'acinte','debalde','cuidadosamente','calmamente',
			  'tristemente']
	nums = [x for x in range(len(opcoes))]
	adverbios = dict(zip(nums, opcoes))
	adverbio = adverbios[indice]
	return adverbio

#####
# modo_insercao = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
# print('Qual o tipo_pessoa de conjunção?')
# 		tipo_de_conjuncao = choice.Menu(['paratática(linker)', 'hipotática(binder)']).ask()
# print('Qual o tipo_pessoa da conjunção paratática(linker)?')
# 			tipo_de_paratatica = ['Aditiva', 'Adversativa', 'Conclusiva',
# 			                                  'Alternativa',
# 			                                  'Explicativa']
#
# tipo_de_hipotática = choice.Menu(['Causal', 'Concessiva', 'Condicional',
# 			                                  'Conformativa', 'Final', 'Proporcional',
# 			                                  'Temporal', 'Comparativa', 'Consecutiva',
# 			                                  'Integrante', 'Relativa']).ask()


def grupo_conjuntivo(tipo_insercao='inserção_menu',
					 conj_extenso=None,tipo_de_conjuncao=None, indice=None):
	"""

	:param tipo_insercao:'inserção_manual', 'inserção_menu'
	:param conj_extenso: 'inserida manualmente'
	:param tipo_de_conjuncao: 'paratática_adversativa','paratática_alternativa','paratática_conclusiva','paratática_explicativa'
	'hipotática_causal','hipotática_concessiva','hipotática_condicional','hipotática_conformativa','hipotática_proporcional','hipotática_temporal','hipotática_comparativa','hipotática_consecutiva'
	'hipotática_integrante','hipotática_relativa'
	:return:
	"""

	try:
		if tipo_insercao == 'inserção_manual':
			conjuncao = conj_extenso

		elif tipo_insercao == 'inserção_menu':

			if tipo_de_conjuncao == 'paratática_aditiva':
				opçoes = ['e', 'mas ainda', 'mas também', 'nem']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'paratática_adversativa':
				opcoes = ['contudo', 'entretanto', 'mas',
										 'não obstante', 'no entanto',
										 'porém', 'todavia']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'paratática_alternativa':  # PRECISO VER COMO IMPLEMENTAR UM COMPLEXO COM ESTE TIPO
				opcoes = ['já', 'ou', 'ora','quer']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'paratática_conclusiva':
				opcoes = ['assim', 'então', 'logo',
										 'por conseguinte', 'por isso',
										 'portanto']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'paratática_explicativa':
				opcoes = ['pois', 'porquanto', 'porque','que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_causal':
				opcoes = ['porque', 'pois', 'porquanto',
						  'como', 'pois que', 'por isso que',
						  'á que', 'uma vez que', 'visto que',
						  'visto como', 'que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_concessiva':
				opcoes = ['embora', 'conquanto', 'ainda que',
										 'mesmo que', 'posto que', 'bem que',
										 'se bem que', 'apesar de que', 'nem que',
										 'que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_condicional':
				opcoes =['se', 'caso', 'quando',
										 'conquanto que', 'salvo se', 'sem que',
										 'dado que', 'desde que', 'a menos que',
										 'a não ser que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_conformativa':
				opcoes = ['conforme', 'como','segundo', 'consoante']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]
			elif tipo_de_conjuncao == 'Final':
				opcoes = ['para que',
						  'a fim de que', 'porque',
						  'que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]


			elif tipo_de_conjuncao == 'hipotática_proporcional':
				opcoes = ['à medida que', 'ao passo que', 'à proporção que',
						  'enquanto', 'quanto mais',
						  'quanto menos']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]


			elif tipo_de_conjuncao == 'hipotática_temporal':
				opcoes = ['quando', 'antes que',
						  'depois que', 'até que', 'logo que',
						  'sempre que', 'assim que', 'desde que',
						  'todas as vezes que', 'cada vez que', 'apenas',
						  'mal', 'desde que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_comparativa':
				opcoes = ['mais que', 'mais do que',
						  'menos que', 'maior que', 'menor que',
						  'melhor que', 'pior que',
						  'menos do que', 'maior do que',
						  'menor do que', 'melhor do que',
						  'pior do que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_consecutiva':
				opcoes = ['De modo que', 'De maneira que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_integrante':
				opcoes = ['que', 'se']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

			elif tipo_de_conjuncao == 'hipotática_relativa':
				opcoes = ['porque', 'pois', 'porquanto',
						  'como', 'pois que', 'por isso que',
						  'á que', 'uma vez que', 'visto que',
						  'visto como', 'que']
				nums = [x for x in range(len(opcoes))]
				conjuncoes = dict(zip(nums, opcoes))
				conjuncao = conjuncoes[indice]

		return conjuncao
	except:
		conjuncao=''
		return conjuncao

# #
# # ######PALAVRAS NOMINAIS- SUBSTANTIVO
# #
# #
# # # NUMERATIVOS
# #
# ###NUMERATIVOS  CARDINAIS ATÉ A 4 CASA(9 000) NÃOS SEI SE VOU IMPLEMENTAR ATÉ A 6 CASA.....
# #

def ordinal(cardinal,genero):
	"""
	:param cardinal:
	:param genero:
	:return: orginal
	"""
	num = str(cardinal)
	if genero == 'masculino':
		ordinal = num + 'º'
	else:
		ordinal = num + 'ª'
	return ordinal

# print(ordinal(4,'masculino'))


# #
def porcento(cardinal):
	'''
    '''
	porcento = str(cardinal) + '%'

	return porcento
# porcento(10)

##NÚMEROS CARDINAIS ATÉ A 4 CASA(9 000) NÃOS SEI SE VOU IMPLEMENTAR ATÉ A 6 CASA.....
def num_cardinal_1dig_extenso(unidadeExtenso,genero):
	if unidadeExtenso == "zero":
		numerativo = ''
	else:
		if unidadeExtenso == 'dois':
			if genero == 'feminino':
				numerativo = unidadeExtenso[slice(-3)] + 'uas'
			elif genero == 'masculino':
				numerativo = unidadeExtenso
		elif unidadeExtenso == 'um':
			if genero == 'feminino':
				numerativo = unidadeExtenso + 'a'
			elif genero == 'masculino':
				numerativo = unidadeExtenso
		else:
			numerativo = unidadeExtenso

	return numerativo
# num_cardinal_1dig_extenso('zero','feminino')

def num_cardinal_2dig_extenso(dezenaExtenso,unidadeExtenso,genero):
	if dezenaExtenso == "zero":
		numerativo = num_cardinal_1dig_extenso(unidadeExtenso,genero)
	elif dezenaExtenso == 'dez':
		if unidadeExtenso == 'zero':
			numerativo = dezenaExtenso
		elif unidadeExtenso == 'um':
			numerativo = 'onze'
		elif unidadeExtenso == 'dois':
			numerativo = 'doze'
		elif unidadeExtenso == 'três':
			numerativo = 'treze'
		elif unidadeExtenso == 'quatro':
			numerativo = 'quatorze'
		elif unidadeExtenso == 'cinco':
			numerativo = 'quinze'
		elif unidadeExtenso == 'seis':
			numerativo = 'dezesseis'
		elif unidadeExtenso == 'sete':
			numerativo = 'dezessete'
		elif unidadeExtenso == 'oito':
			numerativo = 'dezoito'
		elif unidadeExtenso == 'nove':
			numerativo = 'dezenove'
	else:
		digito1 = num_cardinal_1dig_extenso(unidadeExtenso, genero)
		if digito1 == "zero":
			digito1 = ''
		if digito1 == "":
			numerativo = dezenaExtenso +  digito1
		else:
			numerativo = dezenaExtenso + ' e ' +digito1

	return numerativo

# num_cardinal_2dig_extenso('zero','zero','feminino')

def num_cardinal_3dig_extenso(centenaExtenso,dezenaExtenso,unidadeExtenso,genero):
	if centenaExtenso == "zero":
		numerativo = num_cardinal_2dig_extenso(dezenaExtenso,unidadeExtenso,genero)
	else:
		digitos2= num_cardinal_2dig_extenso(dezenaExtenso,unidadeExtenso,genero)

		if digitos2 =='':
			if (centenaExtenso == 'duzentos' or centenaExtenso == 'trezentos' or
					centenaExtenso == 'quatrocentos' or centenaExtenso == 'quinhentos' or
					centenaExtenso == 'seiscentos' or centenaExtenso == 'setecentos' or
					centenaExtenso == 'oitocentos' or centenaExtenso == 'novecentos'):
				if genero == 'feminino':
					centena = centenaExtenso[slice(-2)] + 'as'
				elif genero == 'masculino':
					centena = centenaExtenso[slice(-2)] + 'os'
				numerativo = centena + digitos2
			else:
				numerativo = centenaExtenso
		else:
			if centenaExtenso == 'cem':
				centena = 'cento e '

			elif (centenaExtenso == 'duzentos' or centenaExtenso == 'trezentos' or
					centenaExtenso == 'quatrocentos' or centenaExtenso == 'quinhentos' or
					centenaExtenso == 'seiscentos' or centenaExtenso == 'setecentos' or
					centenaExtenso == 'oitocentos' or centenaExtenso == 'novecentos'):
				if genero == 'feminino':
					centena = centenaExtenso[slice(-2)] + 'as e '
				elif genero == 'masculino':
					centena = centenaExtenso[slice(-2)] + 'os e '

			numerativo = centena + digitos2

	return numerativo

# num_cardinal_3dig_extenso('duzentos','zero','zero', 'feminino')

def num_cardinal_4dig_extenso(milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,genero):  # Número com 4 dígitos
	if milharExtenso == "zero":
		numerativo = num_cardinal_3dig_extenso(centenaExtenso,dezenaExtenso,unidadeExtenso,genero)
	else:
		digito3 = num_cardinal_3dig_extenso(centenaExtenso,dezenaExtenso,unidadeExtenso,genero)
		if digito3 == '':
			if milharExtenso == 'dois mil':
				if genero == 'masculino':
					milhar = milharExtenso

				elif genero == 'feminino':
					milhar = milharExtenso[:1] + 'uas' + milharExtenso[4:]
			else:
				milhar = milharExtenso
		else:
			milhar = milharExtenso
			numerativo = milhar + " e " + digito3

	return numerativo

# num_cardinal_4dig_extenso('zero','trezentos', 'zero', 'três', 'feminino')

# tipoRealCard = choice.Menu(['extenso', 'numérico']).ask()

def num_cardinal(tipoRealCard, cardNumerico, milharExtenso,
				 centenaExtenso,dezenaExtenso,unidadeExtenso,genero):

	if tipoRealCard == 'numérico':
		numCardinal = cardNumerico

	elif tipoRealCard == 'extenso':
		numCardinal = num_cardinal_4dig_extenso(milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,genero)


	return numCardinal

# num_cardinal("extenso", None, 'zero','duzentos', 'zero', 'zero', 'feminino')
#
# funcaoNumerativo = choice.Menu(['quant_precisa_absoluta(cardinais)',
# 		                                 'quant_precisa_div/multi(fração/multiplicativos)',
# 		                                 'quant_imprecisa_pron_indef_numer',
# 		                                 'quant_imprecisa_pron_indef_valor_alt_baixo',
# 		                                 'ordem_lugar_preciso(ordinal)',
# 		                                 'ordem_lugar_impreciso(posição_relativa'
# 		                                 ]).ask()
# print("""
#                     'algum'
#                     'nenhum'
#                     3: 'todo'
#                     4: 'muito'
#                     5: 'pouco'
#                     6: 'vário'
#                     7: 'tanto'
#                     8: 'outro'
#                     9: 'quanto'
#                     10: 'alguma'
#                     1'nenhuma'
#                     1'toda'
#                     13: 'muita'
#                     14: 'pouca'
#                     15: 'vária'
#                     1'tanta'
#                     17:'outra'
#                     18: 'quanta'
#                     19:'alguns'
#                     20:'nenhuns'
#                     21:'todos'
#                     22:'muitos'
#                     23:'poucos'
#                     24:'vários'
#                     25:'tantos'
#                     26:'outros'
#                     27:'quantos'
#                     28:'algumas'
#                     29:'nenhumas'
#                     30:'todas'
#                     31:'muitas'
#                     32:'poucas'
#                     33:'várias'
#                     34:'tantas'
#                     35:'outras'
#                     36:'quantas'
#
#                                Escolha uma opção:""")


def Numerativo(funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
			   milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido):
	'''
    '''
	if funcaoNumerativo == 'ordem_lugar_preciso(ordinal)':
		Numerativo = ordinal(cardinal,genero)

	elif funcaoNumerativo == 'quant_precisa_div/multi(fração/multiplicativos)':
		if tipo_precisa == 'porcentagem':
			Numerativo = porcento(cardinal)

	elif funcaoNumerativo == 'quant_precisa_absoluta(cardinais)':
		Numerativo = num_cardinal(tipoRealCard, cardinal, milharExtenso,centenaExtenso,
								  dezenaExtenso,unidadeExtenso,genero)
	elif funcaoNumerativo == 'quant_imprecisa_pron_indef_numer':
		Numerativo = numIndefinido
	else:
		Numerativo=''
	return Numerativo
#
# # ordinal
# Numerativo('ordem_lugar_preciso(ordinal)','5','masculino',None,None,
# 			   None,None,None,None,None)
# #cardinal
# Numerativo('quant_precisa_absoluta(cardinais)',None,'feminino',None,"extenso",
# 			   "zero","duzentos","zero","zero",None)
#
# def NumerativoIndefinidoSwitcher():
# 	i = int(input())
#
# 	switcherNumInd = {
# 		'algum',
# 		'nenhum',
# 		3: 'todo', \
# 		4: 'muito',
# 		5: 'pouco',
# 		6: 'vário',
# 		7: 'tanto',
# 		8: 'outro',
# 		9: 'quanto',
# 		10: 'alguma',
# 		1'nenhuma',
# 		1'toda',
# 		13: 'muita',
# 		14: 'pouca',
# 		15: 'vária',
# 		16: 'tanta',
# 		17: 'outra',
# 		18: 'quanta',
# 		19: 'alguns',
# 		20: 'nenhuns',
# 		2'todos',
# 		2'muitos',
# 		23: 'poucos',
# 		24: 'vários',
# 		25: 'tantos',
# 		26: 'outros',
# 		27: 'quantos',
# 		28: 'algumas',
# 		29: 'nenhumas',
# 		30: 'todas',
# 		3'muitas',
# 		3'poucas',
# 		33: 'várias',
# 		34: 'tantas',
# 		35: 'outras',
# 		36: 'quantas',
# 	}
#
# 	return switcherNumInd.get(i, 'Seleção nao disponível')

# #
# # #
# #
# # ###A palavra nominal que realiza o Ente no GRUPO NOMINAL- Flexiona para nos eixos:
# # #     Gênero, Número, Grau. Por enquanto, vou trabalhar apenas com Gênero e número.(ORDEM DA PALAVRA AINDA)
# # # COMECEI APENAS COM SUBSTANTIVOS QUE SÃO REGULARES NAS SUAS FLEXÕES: gato:gatos:gatas:

def detectaExpSubstantivo(substantivo,genero,numero):  ##dado o substantivo flexionado##
	'''(str,str,str)->

    Retorna o morfema que realiza a experiência em um substantivo, dados
    o substantivo flexionado, o gênero e o numero.

    >>>detectaExpSubstantivo('','masculino','plural')
    'gat'
    '''


	if genero == 'masculino' and numero == 'singular':
		raizSubs = (substantivo[slice(-1)])

	elif genero == 'feminino' and numero == 'singular':
		raizSubs = (substantivo[slice(-1)])

	elif genero == 'masculino' and numero == 'plural':
		raizSubs = (substantivo[slice(-2)])

	elif genero == 'feminino' and numero == 'plural':
		raizSubs = (substantivo[slice(-2)])
	return raizSubs
# detectaExpSubstantivo('gatos','masculino','plural')
# #
# # # OS LEMAS QUE SERVIRÃO PARA  FUNÇÃO QUE SEGUE VIRÃO DA ANOTAÇÃO NA ONTOLOGIA:
# # #        o que na ontologia tiver anotado como Thing, vai servir como um
# # ##        banco lexical do qual o operador vai selecionar(não sei ainda se
# # #        vai ser importado automaticamente ou se vou ter de inserir manualmente
# # #        )
# #
# genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
# lemaSubs = input('Qual é o substantivo lematizado?')


def realizaExpSubstantivo(lemaSubs,genero):  ##dado o substantivo_lematizado- por enquanto, apenas para
	##substantivos regulares, com foco em masculino-feminino, singular plural. Tenho que considerar desenvolver
	#    com relação aos diferentes tipos de radicais (primitivo, derivado, composto, simples...)
	'''(str)-> str

    Retorna o morfema que realiza a experiência em um substantivo, dado
    o substantivo lematizado.

    >>>realizaExpSubstantivo()
    'gat'
    '''
	if genero == 'masculino' or genero =='feminino':
		morfExpSubs = lemaSubs[slice(-1)]

	elif genero == 'não-binário':
		morfExpSubs = lemaSubs

	return morfExpSubs

# realizaExpSubstantivo('gata','masculino')
# #

def realizacao_flexoes_substantivos(genero,numero):
	'''(str,str,str)->

    Retorna os morfemas que realizam as flexões de genero e numero dados
    a experiência do substantivo e os genero e numeros desejados.

	genero = choice.Menu(['masculino', 'feminino', 'não-binário']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
    >>>realizacao_flexoes_substantivos()
    'os'
    '''

	if genero == 'masculino' and numero == 'singular':
		morfema_flexao_substantivo = 'o'
	elif genero == 'feminino' and numero == 'singular':
		morfema_flexao_substantivo = 'a'
	elif genero == 'masculino' and numero == 'plural':
		morfema_flexao_substantivo = 'os'
	elif genero == 'feminino' and numero == 'plural':
		morfema_flexao_substantivo = 'as'
	elif genero == 'não-binário' and numero == 'singular':
		morfema_flexao_substantivo = ''
	elif genero == 'não-binário' and numero == 'plural':
		morfema_flexao_substantivo = 's'

	return morfema_flexao_substantivo
# realizacao_flexoes_substantivos("masculino",'plural')
# #
# # ###Com relação aos substantivos comuns tenho que ver a abordagem que vou tomar
# # # com relação aos substantivos não binários, ou inerentemente masculinos ou femininos. Me parece
# # # que o sistema se organiza a realizar o gênero em alguns casos na ordem da palavra, e em
# # # outros casos na ordem do grupo (mesa: não parece ter uma contrapartida masculina)
# #
# print('Escolha o tipo_pessoa de feminino:')
# tipo_feminino_ÃO = choice.Menu(['oa', 'ona', 'ã', 'esa', 'casos_exceção']).ask()
#
# print('Escolha o tipo_pessoa de plural:')
# tipo_masc_ÃO = choice.Menu(['ãos', 'ões', 'ães']).ask()

# terminado em 's':;;;tonicidade = choice.Menu(['oxítona', 'paroxítona', 'proparoxítona']).ask()

def substantivo_comum(substantivo_lematizado, numero,
					  genero, tipo_feminino_ÃO,
					  tipo_masc_ÃO, acentTonica):
	"""
	"""

	if substantivo_lematizado[-1:] == 'm':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'ns'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'or':

		if genero == 'masculino' and numero == 'singular':

			substantivo_comum = substantivo_lematizado

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'masculino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 's'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo
	elif substantivo_lematizado[-2:] == 'ão':

		if (genero == 'masculino' and numero == 'singular'
				or genero == 'não-binário' and numero == 'singular'):
			substantivo_comum = substantivo_lematizado

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino_ÃO

		elif (genero == 'masculino' and numero == 'plural'
		      or genero == 'não-binário' and numero == 'plural'):

			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_masc_ÃO+'s'

		elif genero == 'feminino' and numero == 'plural':

			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino_ÃO+ 's'

	elif substantivo_lematizado[-1:] == 'x':
		substantivo_comum = substantivo_lematizado

	elif substantivo_lematizado[-1:] == 's':
		if acentTonica == 'paroxítona':
			substantivo_comum = substantivo_lematizado
		elif acentTonica == 'oxítona':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_numero = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_numero

	elif (substantivo_lematizado[-1:] == 'r' or substantivo_lematizado[-1:] == 'z'):

		if genero == 'masculino' and numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'masculino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'al':
		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'ais'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'el':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'éis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'il':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'is'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'ol':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'óis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	elif substantivo_lematizado[-2:] == 'ul':

		if numero == 'singular':
			substantivo_comum = substantivo_lematizado

		elif numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexao_substantivo = 'úis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	else:

		if genero == 'masculino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'o'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'masculino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'os'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'feminino' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexao_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

		elif genero == 'não-binário' and numero == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexao_substantivo = 's'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

	return substantivo_comum
#
# substantivo_comum("ancião",'plural',"masculino", None,"ão",None)
# substantivo_comum("artesão",'singular',"feminino", "ã",None,None)
#
# substantivo_comum("carro","plural","não-binário", None, None,None)
# substantivo_comum("varal","plural", "não-binário", None, None,None)

# # # ADJETIVOS

def deteccao_experiencia_do_adjetivo(adjetivo,genero,numero):  ##dado o adjetivo flexionado##
	'''(str,str,str)->

    Retorna o morfema que realiza a experiência em um adjetivo, dados
    o adjetivo flexionado, o gênero e o número.

    >>>deteccao_experiencia_do_adjetivo()
    'esportiv'
    '''

	if numero == 'singular':
		if genero == 'masculino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-1)])

		elif genero == 'feminino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
	elif numero == 'plural':
		if genero == 'masculino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-2)])

		elif genero == 'feminino':
			raiz_experiencial_adjetivo = (adjetivo[slice(-2)])

	return raiz_experiencial_adjetivo
# deteccao_experiencia_do_adjetivo("esperto","masculino","singular")
# #


def realizacao_experiencia_do_adjetivo(adjetivo_lematizado,genero):
	'''(str)-> str
	genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
	adjetivo_lematizado =

    Retorna o morfema que realiza a experiência em um adjetivo, dado
    o adjetivo lematizado.

    >>>realizacao_experiencia_do_adjetivo()
    'gat'
    '''

	if genero == 'masculino/feminino':
		morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]

	elif genero == 'não-binário':
		morfema_experiencial_do_adjetivo = adjetivo_lematizado

	return morfema_experiencial_do_adjetivo

# realizacao_experiencia_do_adjetivo("esperto","masculino/feminino")

def realizacao_flexoes_adjetivos(genero,numero):
	"""
    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do adjetivo e os gênero e números desejados.

	:param genero: 'masculino', 'feminino', 'não-binário'
	:param numero: 'singular', 'plural'
	:return: morfema_flexao_adjetivo
	"""

	if numero == 'singular':
		if genero == 'masculino':
			morfema_flexao_adjetivo = 'o'

		elif genero == 'feminino':
			morfema_flexao_adjetivo = 'a'
		elif genero == 'não-binário':
			morfema_flexao_adjetivo = ''

	elif numero == 'plural':
		if genero == 'masculino' :
			morfema_flexao_adjetivo = 'os'

		elif genero == 'feminino' and numero == 'plural':
			morfema_flexao_adjetivo = 'as'

		elif genero == 'não-binário':
			morfema_flexao_adjetivo = 's'

	return morfema_flexao_adjetivo




def adjetivo(adjModificacao,adjetivo_lematizado,genero,numero):
	"""
	Retorna a realizacao de um adjetivo comum dados a experiência_do_adjetivo
    e as flexões_desejadas.
	:param adjModificacao:
	:param adjetivo_lematizado:
	:param genero:
	:param numero:
	:return:
	"""
	try:
		if adjModificacao == 'sim':
			if numero == 'singular':
				if genero == 'masculino':
					morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
					morfema_flexao_adjetivo = 'o'

				elif genero == 'feminino':
					morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
					morfema_flexao_adjetivo = 'a'

				elif genero == 'não-binário':
					morfema_experiencial_do_adjetivo = adjetivo_lematizado
					morfema_flexao_adjetivo = ''


			elif numero == 'plural':
				if genero == 'masculino':
					morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
					morfema_flexao_adjetivo = 'os'


				elif genero == 'feminino':
					morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
					morfema_flexao_adjetivo = 'as'

				elif genero == 'não-binário':
					morfema_experiencial_do_adjetivo = adjetivo_lematizado
					morfema_flexao_adjetivo = 's'

			adj = morfema_experiencial_do_adjetivo + morfema_flexao_adjetivo
		return adj
	except:
		adj=''
		return adj

# print(adjetivo('sim','alto','feminino','singular'))



# #
# # # PRONOMES#
# #
# # # PEGUEI OS PRONOMES BÁSICOS# QUANDO CHEGAR NA ORAÇÃO, A MORFOLOGIA DOS VERBOS
# # # FICA UM POUCO SUBVERSIVA

def realizacao_pronominal_casoreto(pessoa_da_interlocucao,genero,numero,morfologia_do_pronome="de_terceira_pessoa"):
	'''(str)->str
    Retorna o pronome adequado dado uma pessoa da intelocução.
	pessoa_da_interlocucao = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
	morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
    >>>realizacao_pronominal_casoreto ('','')
    'eu'
    '''

	if pessoa_da_interlocucao == 'falante' and numero == 'singular':
		pronome_pessoal_reto = 'eu'


	elif pessoa_da_interlocucao == 'ouvinte' and numero == 'singular':

		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_reto = 'tu'
		else:
			pronome_pessoal_reto = 'você'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'singular':
		if genero == 'masculino':
			pronome_pessoal_reto = 'ele'
		else:
			pronome_pessoal_reto = 'ela'

	elif pessoa_da_interlocucao == 'falante' and numero == 'plural':
		pronome_pessoal_reto = 'nós'

	elif pessoa_da_interlocucao == 'ouvinte' and numero == 'plural':

		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_reto = 'vós'
		else:
			pronome_pessoal_reto = 'vocês'

	elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'plural':

		if genero == 'masculino':
			pronome_pessoal_reto = 'eles'
		else:
			pronome_pessoal_reto = 'elas'

	return pronome_pessoal_reto


# realizacao_pronominal_casoreto("não_interlocutor", "feminino", "singular", morfologia_do_pronome="de_terceira_pessoa")


def realizacao_pronome_caso_obliquo(transitividade_verbo=None,tonicidade=None,pessoa_da_interlocucao=None,numero=None,
									genero=None,morfologia_do_pronome=None,reflexivo=False):
	'''(str)->str
    Retorna o pronome oblíquo adequado dado uma pessoa da intelocução.
	tonicidade = choice.Menu(['átono', 'tônico']).ask()
	pessoa_da_interlocucao = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
	numero = choice.Menu(['singular', 'plural']).ask()
	morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()
	transitividade_verbo =choice.Menu(['direto','direto_preposicionado, 'indireto']).ask()
    >>>realizacao_pronominal_caso_oblíquo ()
    'me'
    '''
	if tonicidade == 'átono' and transitividade_verbo == "direto":
		if numero == 'singular':
			if pessoa_da_interlocucao == 'falante':
				pronome_pessoal_obliquo = 'me'
			elif pessoa_da_interlocucao == 'ouvinte':
				pronome_pessoal_obliquo = 'te'
		elif numero == 'plural':
			if pessoa_da_interlocucao == 'falante':
				pronome_pessoal_obliquo = 'nos'
			elif pessoa_da_interlocucao == 'ouvinte':
				pronome_pessoal_obliquo = 'vos'

		if  pessoa_da_interlocucao == 'não_interlocutor':
			if numero == 'singular':
				if genero == 'masculino':
					if morfologia_do_pronome == 'padrão' :
						pronome_pessoal_obliquo = 'o'

				if genero == 'feminino':
					if morfologia_do_pronome == 'padrão' :
						pronome_pessoal_obliquo = 'a'

			elif numero == 'plural':
				if genero == 'masculino':
					if morfologia_do_pronome == 'padrão' :
						pronome_pessoal_obliquo = 'os'

				if genero == 'feminino':
					if morfologia_do_pronome == 'padrão' :
						pronome_pessoal_obliquo = 'as'

	if reflexivo==True:
			pronome_pessoal_obliquo = 'se'

	if pessoa_da_interlocucao == 'não_interlocutor'  and transitividade_verbo == "indireto":
		if tonicidade == 'átono':
			if numero == 'singular':
				pronome_pessoal_obliquo = 'lhe'

			elif numero == 'plural':
				if morfologia_do_pronome == 'padrão':
					pronome_pessoal_obliquo = 'lhes'


		elif tonicidade == 'tônico':
			if morfologia_do_pronome == 'não_padrão':
				if genero == 'masculino':
					if numero == 'singular':
						pronome_pessoal_obliquo = 'ele'
					elif numero =='plural':
						pronome_pessoal_obliquo = 'eles'

				elif genero == 'feminino':
					if numero == 'singular':
						pronome_pessoal_obliquo = 'ela'
					elif numero =='plural':
						pronome_pessoal_obliquo = 'elas'
			elif morfologia_do_pronome == 'padrão':
				pronome_pessoal_obliquo = 'si'

	if transitividade_verbo == 'indireto'  and tonicidade == 'tônico':
		if numero == 'singular':
			if pessoa_da_interlocucao == 'falante':
				pronome_pessoal_obliquo = 'mim'
			elif pessoa_da_interlocucao == 'ouvinte' :
				if morfologia_do_pronome == 'padrão':
					pronome_pessoal_obliquo = 'ti'
				else:
					pronome_pessoal_obliquo = 'você'
		elif numero == 'plural':
			if pessoa_da_interlocucao == 'falante':
				pronome_pessoal_obliquo = 'nós'
			elif pessoa_da_interlocucao == 'ouvinte' :
				if morfologia_do_pronome == 'padrão':
					pronome_pessoal_obliquo = 'vós'
				else:
					pronome_pessoal_obliquo = 'vocês'

	return pronome_pessoal_obliquo

#me
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='falante', numero='singular', genero=None, morfologia_do_pronome=None, reflexivo=False)
#te
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='ouvinte', numero='singular', genero=None, morfologia_do_pronome=None, reflexivo=False)
#nos
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='falante', numero='plural', genero=None, morfologia_do_pronome=None, reflexivo=False)
#vos
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='ouvinte', numero='plural', genero=None, morfologia_do_pronome=None, reflexivo=False)


#o
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='masculino', morfologia_do_pronome='padrão', reflexivo=False)
#ele
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='masculino', morfologia_do_pronome='não_padrão', reflexivo=False)
#a
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='feminino', morfologia_do_pronome='padrão', reflexivo=False)
#ela
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='feminino', morfologia_do_pronome='não_padrão', reflexivo=False)
#os
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='masculino', morfologia_do_pronome='padrão', reflexivo=False)
#eles
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='masculino', morfologia_do_pronome='não_padrão', reflexivo=False)

#as
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='feminino', morfologia_do_pronome='padrão', reflexivo=False)
#elas
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='feminino', morfologia_do_pronome='não_padrão', reflexivo=False)
#elas
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='feminino', morfologia_do_pronome='padrão', reflexivo=False)


#se
realizacao_pronome_caso_obliquo(transitividade_verbo=None, tonicidade=None, pessoa_da_interlocucao=None, numero=None, genero=None, morfologia_do_pronome=None, reflexivo=True)
#lhe
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero=None, morfologia_do_pronome=None, reflexivo=None)

#lhes
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero=None, morfologia_do_pronome='padrão', reflexivo=None)

#mim
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='falante', numero='singular', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
#ti
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='singular', genero=None, morfologia_do_pronome='padrão', reflexivo=None)

#você
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='singular', genero=None, morfologia_do_pronome='não_padrão', reflexivo=None)


#nós
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='falante', numero='plural', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
#vós
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='plural', genero=None, morfologia_do_pronome='padrão', reflexivo=None)

#você
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='plural', genero=None, morfologia_do_pronome='não_padrão', reflexivo=None)

##me
realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='falante',
									numero='singular',genero=None, morfologia_do_pronome=None, reflexivo=False)


realizacao_pronome_caso_obliquo("indireto",'tônico',"não_interlocutor",'singular','feminino',"padrão")
realizacao_pronome_caso_obliquo(transitividade_verbo='indireto',tonicidade='átono',pessoa_da_interlocucao='não_interlocutor',
								numero='plural',genero=None,morfologia_do_pronome='padrão',reflexivo=False)

#
# estrutura_GN(None, None, None,None,
# 				 None, None, None, None,
# 				None, None,None,
# 				 None,None, None,
# 				 None, None, None,
# 				 None, None, None, None,
# 				 None, None, None,None,
# 				 None, None,None,
# 				'consciente', None, None,
# 				 None, 'pronome_caso_oblíquo',None,
# 				 'singular',None, None, None, None,
# 				'falante','direto','átono', "padrão",
# 				None, None, None,None,
# 				 None,None, None,None)

##TENHO QUE VER SE FAZ SENTIDO MUDAR ESTA(inserir parâmetros??)
	# modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
	# print('Qual tipo_pessoa de relativo?')
	# tipo_pronome_relativo = choice.Menu(['variável', 'invariável']).ask()
	#

def pronome_relativo(tipo_insercao="inserção_menu",pron_extenso=None,tipo_pronome_relativo=None,
					 genero=None,numero=None, indice=None):
	"""

	:param tipo_insercao: 'inserção_manual', 'inserção_menu'
	:param pron_extenso: entre o pronome
	:param tipo_pronome_relativo: 'variável', 'invariável'
	:param genero: 'masculino','feminino'
	:param numero: 'singular','plural'
	:param indice: entre um integer com índice
	:return:
	"""
	try:
		if tipo_insercao == 'inserção_manual':
			pronome_relativo = pron_extenso

		elif tipo_insercao == 'inserção_menu':

			if tipo_pronome_relativo == 'variável':
				if numero == "plural":
					if genero == 'masculino':
						opcoes = ['os quais', 'cujos', 'quantos', 'pelos quais']
						nums = [x for x in range(len(opcoes))]
						relativos = dict(zip(nums, opcoes))
						pronome_relativo = relativos[indice]

					elif genero == 'feminino':
						opcoes = ['as quais', 'cujas', 'quantas', 'pelas quais']
						nums = [x for x in range(len(opcoes))]
						relativos = dict(zip(nums, opcoes))
						pronome_relativo = relativos[indice]

				elif numero == "singular":
					if genero == 'masculino':
						opcoes = ['o qual', 'cujo', 'quanto', 'pelo qual']
						nums = [x for x in range(len(opcoes))]
						relativos = dict(zip(nums, opcoes))
						pronome_relativo = relativos[indice]

					elif genero == 'feminino':
						opcoes = ['a qual', 'cuja', 'quanta', 'pela qual']
						nums = [x for x in range(len(opcoes))]
						relativos = dict(zip(nums, opcoes))
						pronome_relativo = relativos[indice]

			elif tipo_pronome_relativo == 'invariável':
				opcoes = ['quem', 'que',
						  'a quem', 'a que', 'porque', 'como']
				nums = [x for x in range(len(opcoes))]
				relativos = dict(zip(nums, opcoes))
				pronome_relativo = relativos[indice]

		return pronome_relativo
	except:
		pronome_relativo = ''
		return pronome_relativo
# pronome_relativo()
# pronome_relativo(tipo_insercao="inserção_menu",pron_extenso=None,tipo_pronome_relativo='variável',genero='masculino',numero='singular', indice=3)
# pronome_relativo(tipo_insercao="inserção_menu",pron_extenso=None,tipo_pronome_relativo='variável',genero='masculino',numero='plural', indice=3)
# #
pronome_relativo(tipo_insercao="inserção_menu",pron_extenso=None,tipo_pronome_relativo='invariável',indice=3)

# #
# # ##PRECISO IMPLEMENTAR LETRA MAIÚSCULA NO CASO DE INICIO DE FRASE.
# # # SUBSTANTIVOS PRÓPRIOS VIRÃO DA LISTA DE NOMES PRÓPRIOS ANOTADOS NA GUM
# # # Por enquanto, vou deixar um input
# #

def nome_proprio(nome=None):
	'''(str)->str
    Retorna o nome próprio. #Futuramente parte das listas de léxicos
    advindas da anotação na GUM.
    '''
	resul = nome
	try:
		return resul.capitalize()
	except:
		resul=''
		return resul

# nome_proprio('andre')

# # ####DÊIXIS DO GN
# #

def estrutura_logica_deixis():
	'''
    '''

	estrutura_lógica_det_dêixis = input("""

            α(Dêitico_ñ_seletivo_específico) # ex.: O,A
            α(Dêitico_ñ_seletivo_ñ_específico) #ex.: Um,uns
            3: α(Dêitico_prox) #Este
            4: α(Dêitico_pess) #Meu
            5: β(Dêitico_prox)^α(Dêitico_pess) # ex.: Este meu
            6: β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess) # ex.: O meu
            7: β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess) # ex.: Um meu





            Selecione uma opção:""")

	if estrutura_lógica_det_dêixis == '1':

		estrutura_lógica_det_dêixis = 'α(Dêitico_ñ_seletivo_específico)'

	elif estrutura_lógica_det_dêixis == '2':

		estrutura_lógica_det_dêixis = 'α(Dêitico_ñ_seletivo_ñ_específico)'

	elif estrutura_lógica_det_dêixis == '3':

		estrutura_lógica_det_dêixis = 'α(Dêitico_prox)'

	elif estrutura_lógica_det_dêixis == '4':

		estrutura_lógica_det_dêixis = 'α(Dêitico_pess)'

	elif estrutura_lógica_det_dêixis == '5':

		estrutura_lógica_det_dêixis = 'β(Dêitico_prox)^α(Dêitico_pess)'

	elif estrutura_lógica_det_dêixis == '6':

		estrutura_lógica_det_dêixis = 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)'

	elif estrutura_lógica_det_dêixis == '7':

		estrutura_lógica_det_dêixis = 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)'

	return estrutura_lógica_det_dêixis

# #
# # # a fazer: verificar as opções que coloquei para os diferentes tipos de dêixis:
# # # não preciso talvez colocar todas as opções de especificidade em cada um deles
# # # pra não ter a possibilidade de dar erro nas escolhas.
def Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,número, gênero):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()
	                          print('Selecione número:')
	número = choice.Menu(['singular', 'plural']).ask()
	print('Selecione o gênero')
	gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

	if (DETERMINAÇÃO_espeficifidade == 'específico'  and ORIENTAÇÃO == 'NA'):

		if número == 'plural' and gênero == 'masculino':
			determinante = 'os'
		elif número == 'plural' and gênero == 'feminino':
			determinante = 'as'
		elif número == 'singular' and gênero == 'masculino':
			determinante = 'o'
		elif número == 'singular' and gênero == 'feminino':
			determinante = 'a'

	return determinante
# Dêitico_ñ_seletivo_específico('específico', 'NA','plural', 'feminino')
# #
def Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,número,gênero):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	print('Selecione número:')
		número = choice.Menu(['singular', 'plural']).ask()
		print('Selecione o gênero')
		gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

	if DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'NA':
		if número == 'singular' and gênero == 'masculino':
			determinante = 'um'
		elif número == 'plural' and gênero == 'masculino':
			determinante = 'uns'
		elif número == 'singular' and gênero == 'feminino':
			determinante = 'uma'
		elif número == 'plural' and gênero == 'feminino':
			determinante = 'umas'
	return determinante
# Dêitico_ñ_seletivo_ñ_específico('não_específico','NA','plural','masculino')
# # 	####
# #

def Dêitico_prox(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,pessoa_da_interlocução_proximidade,número,gênero):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()
	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa',
	                          'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()
	print('Selecione a pessoa da interlocução:')
		pessoa_da_interlocução_proximidade = choice.Menu(
			['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']).ask()
	print('Selecione número:')
			número = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero')
			gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''


	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade':

		if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':

			if número == 'singular' and gênero == 'masculino':
				determinante = 'este'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'estes'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'esta'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'estas'

		elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte':

			if número == 'singular' and gênero == 'masculino':
				determinante = 'esse'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'esses'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'essa'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'essas'

		elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor':

			if número == 'singular' and gênero == 'masculino':
				determinante = 'aquele'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'aqueles'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'aquela'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'aquelas'

	return determinante
# Dêitico_prox('específico','orientação_específica_proximidade','próximo_ao_não_interlocutor','plural','masculino')

def Dêitico_pess(DETERMINAÇÃO_espeficifidade,ORIENTAÇÃO,pessoa_da_interlocução_possuidor,
				 número_obj_possuído,gênero_obj_possuído,morfologia_do_pronome='morfologia_terceira_pessoa'):
	'''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask

	print('Selecione a pessoa da interlocução do possuidor')
		pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

	print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()
	print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'terceira_pessoa']).ask()
    '''

	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':

		if pessoa_da_interlocução_possuidor == '1s':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'meu'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'meus'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'minha'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'minhas'

		elif pessoa_da_interlocução_possuidor == '2s':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'teu'
				else:
					determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'teus'
				else:
					determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'tua'
				else:
					determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'tuas'
				else:
					determinante = 'suas'

		elif (pessoa_da_interlocução_possuidor == '3s' or
		      pessoa_da_interlocução_possuidor == '3p'):

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'suas'

		elif pessoa_da_interlocução_possuidor == '1p':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'nosso'
			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'nossos'
			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'nossa'
			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'nossas'

		elif pessoa_da_interlocução_possuidor == '2p':

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vosso'
				else:
					determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vossos'
				else:
					determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vossa'
				else:
					determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':

				if morfologia_do_pronome == 'padrão':
					determinante = 'vossas'
				else:
					determinante = 'suas'

	return determinante
# Dêitico_pess('específico','orientação_específica_pessoa','2p','plural','feminino','padrão')


# ##talvez não use
# def Dêitico_genérico(DETERMINAÇÃO_espeficifidade):
#
# 	'''
#
# 	DETERMINAÇÃO_espeficifidade = choice.Menu(['genérico(contável)', 'genérico(de_massa)']).ask()
#
# 	:return:
# 	'''
#
#
# 	if (DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' or
# 			DETERMINAÇÃO_espeficifidade == 'genérico(contável)'):
# 		determinante = ''  # Neste caso, o grupo nominal CONTÁVEL é realizado no plural e o DE MASSA no singular
#
# 	return determinante
# #

def Deixis_geral(DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
				 gênero_beta,número_beta,morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
				 ORIENTAÇÃO_alpha,gênero_alpha,número_alpha,morfologia_do_pronome_alpha,
				 pessoa_da_interlocução_possuidor,número_obj_possuído,
				 gênero_obj_possuído,pessoa_da_interlocução_proximidade):



	if DETERMINAÇÃO_espeficifidade_alpha == 'específico':
		if ORIENTAÇÃO_alpha == 'orientação_específica_proximidade':
			alpha = Dêitico_prox(DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
										pessoa_da_interlocução_proximidade, número_alpha, gênero_alpha)
		elif ORIENTAÇÃO_alpha == 'orientação_específica_pessoa':
			alpha = Dêitico_pess(DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,pessoa_da_interlocução_possuidor,
			 número_obj_possuído,gênero_obj_possuído,morfologia_do_pronome_alpha)
		else:
			alpha = Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade_alpha,
														 ORIENTAÇÃO_alpha,número_alpha, gênero_alpha)
	elif DETERMINAÇÃO_espeficifidade_alpha == 'não_específico':
		alpha = Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade_alpha,
													   ORIENTAÇÃO_alpha, número_alpha, gênero_alpha)

	else:

		alpha = ''

	if DETERMINAÇÃO_espeficifidade_beta =='específico':

		if ORIENTAÇÃO_beta == 'orientação_específica_proximidade':
			beta = Dêitico_prox(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
								pessoa_da_interlocução_proximidade,
								número_beta, gênero_beta)
		elif ORIENTAÇÃO_beta == 'orientação_específica_pessoa':
			beta = Dêitico_pess(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
										pessoa_da_interlocução_possuidor,
										número_obj_possuído, gênero_obj_possuído, morfologia_do_pronome_beta)
		else:
			beta = Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, número_beta,
														 gênero_beta)
	elif DETERMINAÇÃO_espeficifidade_beta == 'não_específico':
		beta = Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade_beta,
													   ORIENTAÇÃO_beta, número_beta, gênero_beta)

	else:
		beta = ''

	if beta !='':
		return beta + ' ' + alpha
	else:
		return (re.sub(' +', '',( beta + ' ' + alpha) ))


#
# Deixis_geral( None,None,
# 				 None,None,None,'específico','orientação_específica_proximidade',
# 			 'masculino','singular','morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
#
# Deixis_geral(None,None,
# 				 None,None,None, 'específico',
# 				 'NA','masculino','singular','morfologia_terceira_pessoa',
# 				 None,None,
# 				 None,None)
#
# Deixis_geral('específico','orientação_específica_proximidade','masculino','singular','morfologia_terceira_pessoa',
# 			 'específico','orientação_específica_pessoa',
# 			 'masculino','singular','morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
# #
#
# print('Qual o tipo_pessoa de Ente?')
# tipo_de_Ente = choice.Menu(['consciente', 'não_consciente', 'NA']).ask()
#
# print('Qual tipo_pessoa de não_consciente?')
# tipo_de_nao_consciente = choice.Menu(['material', 'semiótico']).ask()
#
# print('Qual tipo_pessoa de material?')
# tipo_de_nao_consciente_material = choice.Menu(
# 	['animal', 'objeto_material', 'substância_material', 'abstração_material']).ask()
#
# print('Qual a classe de palavra que realiza o Ente?')
# classe_palavra_Ente = choice.Menu(
# 	['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_obliquo']).ask()
# print('Qual tipo_pessoa de semiótico?')
# tipo_de_nao_consciente_semiotico = choice.Menu(
# 	['instituição', 'objeto_semiótico', 'abstração_semiótica']).ask()


def Ente(tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
		 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
		 numero=None, genero=None, tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None,
		 nomeProprio=None,pessoa_da_interlocucao=None,transitividade_verbo=None, tonicidade=None,
		 morfologia_do_pronome=None, reflexivo=None):
	""""""

	if tipo_de_Ente == 'NA':
		Ente = ''
	else:
		if classe_palavra_Ente == 'substantivo_comum':
			Ente = substantivo_comum(substantivo_lematizado, numero, genero,
									 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica)

		elif classe_palavra_Ente == 'substantivo_próprio':
			Ente = nomeProprio
		elif classe_palavra_Ente == 'pronome_caso_reto':
			Ente = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
												  numero, morfologia_do_pronome)
		elif classe_palavra_Ente == 'pronome_caso_oblíquo':
			Ente = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
												   pessoa_da_interlocucao, numero, genero,
												   morfologia_do_pronome, reflexivo)

	return Ente
#
# #
# Ente('não_consciente','material','animal', None,'substantivo_comum','gato','singular', 'feminino')
# Ente('consciente',None,None, None,'substantivo_comum','menina','singular', 'feminino')


# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "singular",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)
# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "plural",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)
# Ente(tipo_de_Ente="não_consciente", tipo_de_nao_consciente="semiótico", tipo_de_nao_consciente_material=None,
# 	tipo_de_nao_consciente_semiotico='abstração_semiótica', classe_palavra_Ente='pronome_caso_oblíquo',
# 	 substantivo_lematizado=None, numero='plural', genero='masculino', tipo_feminino_ÃO=None,
# 	 tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,pessoa_da_interlocucao='não_interlocutor',
# 	 transitividade_verbo='indireto', tonicidade='tônico', morfologia_do_pronome='não_padrão', reflexivo=False)


# #
# # ###No caso do Ente, ainda tenho que modelar as opções de Ente realizados por substantivos compostos (devido ao padrão de
# # # morfologia das flexões
# #

#####ESTRUTURA DO GRUPO NOMINAL:

##
# print('Há Qualificador no gn?')
# tem_qualificador = choice.Menu(['sim', 'NA']).ask()
# realizacao_qualificador = choice.Menu(['frase-preposicional', 'oração']).ask()


def qualificador(indicePreposicao=None,dissocEnteNucleo=None,DETERMINAÇÃO_espeficifidade_beta=None,ORIENTAÇÃO_beta=None,
				 gênero_beta=None,número_beta=None,morfologia_do_pronome_beta=None,
				 DETERMINAÇÃO_espeficifidade_alpha=None,ORIENTAÇÃO_alpha=None,gênero_alpha=None,
				 número_alpha=None,morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
				 número_obj_possuído=None, gênero_obj_possuído=None,pessoa_da_interlocução_proximidade=None,#
				 funcaoNumerativo=None,cardinal=None,genero=None,tipo_precisa=None,tipoRealCard=None,
			  	 milharExtenso=None,centenaExtenso=None,dezenaExtenso=None,unidadeExtenso=None,numIndefinido=None,
				 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
				 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
				 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,#
				 temQualificador=None,tipoQualificador=None,epitetoModificacao=None,adjetivo_epiteto=None,
				 classificadorModificacao=None,adjetivo_classificador=None,generoAdjetivo=None, numeroAdjetivo=None,contracao=None):


	if temQualificador == 'sim':
		if tipoQualificador == 'frase-preposicional':
			Qualificador = frase_preposicional(indicePreposicao, dissocEnteNucleo, temQualificador, tipoQualificador,
						DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
						gênero_beta, número_beta, morfologia_do_pronome_beta,
						DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
						número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
						número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade,  #
						funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
						milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
						numIndefinido,
						tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
						tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado,
						numero,
						tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
						pessoa_da_interlocucao,
						transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,  #
						epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
						adjetivo_classificador, generoAdjetivo, numeroAdjetivo,contracao)
		# else:
		# 	Qualificador = "que" + oraçãoProjetada()
	else:
		Qualificador = ''
	return re.sub(' +',' ', Qualificador).strip()
#
# qualificador(indicePreposicao=10,dissocEnteNucleo=None,temQualificador='sim',tipoQualificador='frase-preposicional',
# 					DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None,generoAdjetivo='masculino', numeroAdjetivo='singular',contracao='-contração')

def estrutura_GN_downraked(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicao=None,
				 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
				 morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None,
				 gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
				 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
				 pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero=None,
				 tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
				 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
				 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
				 numero=None, tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
				 pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
				 reflexivo=None, epitetoModificacao=None, adjetivo_epiteto=None, classificadorModificacao=None,
				 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None,contracao=None):
	GN_downranked = estrutura_GN(dissocEnteNucleo, temQualificador, tipoQualificador, indicePreposicao,
				 DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, gênero_beta, número_beta,
				 morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
				 gênero_alpha, número_alpha, morfologia_do_pronome_alpha,
				 pessoa_da_interlocução_possuidor, número_obj_possuído, gênero_obj_possuído,
				 pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal, genero,
				 tipo_precisa, tipoRealCard, milharExtenso, centenaExtenso,
				 dezenaExtenso, unidadeExtenso, numIndefinido,
				 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
				 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado,
				 numero, tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
				 pessoa_da_interlocucao, transitividade_verbo, tonicidade, morfologia_do_pronome,
				 reflexivo, epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
				 adjetivo_classificador, generoAdjetivo, numeroAdjetivo,contracao)

	return re.sub(' +',' ',GN_downranked).strip()

# estrutura_GN_downraked()
# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None,
# 					   generoAdjetivo='masculino', numeroAdjetivo='singular',contracao='+contação')
#
# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='feminino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='feminino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='feminino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='árvore', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None,
# 					   generoAdjetivo='feminino', numeroAdjetivo='plural',contracao='+contação')
# #

# # ####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
# # ##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal
# # # com função de Numerativo no GN DE PRIMEIRO NÍVEL)
# 	print('Há dissociação entre Ente e Núcleo do GN?')
# 	dissocEnteNucleo = choice.Menu(['sim', 'não']).ask()

def estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicao=None,
				 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
				 morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None,
				 gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
				 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
				 pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero=None,
				 tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
				 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
				 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
				 numero=None, tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
				 pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
				 reflexivo=None, epitetoModificacao=None, adjetivo_epiteto=None, classificadorModificacao=None,
				 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None,contracao=None):
	try:
		if dissocEnteNucleo == None:

			Determinante = Deixis_geral(DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
					 gênero_beta,número_beta,morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
					 ORIENTAÇÃO_alpha,gênero_alpha,número_alpha,morfologia_do_pronome_alpha,
					 pessoa_da_interlocução_possuidor,número_obj_possuído,
					 gênero_obj_possuído,pessoa_da_interlocução_proximidade)

			numerativo = Numerativo(funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
				   milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido)

			ente = Ente(tipo_de_Ente,tipo_de_nao_consciente,tipo_de_nao_consciente_material,
			 tipo_de_nao_consciente_semiotico,classe_palavra_Ente,substantivo_lematizado,numero,
			genero, tipo_feminino_ÃO, tipo_masc_ÃO,acentTonica,nomeProprio,pessoa_da_interlocucao,
			 transitividade_verbo,tonicidade,morfologia_do_pronome,reflexivo)

			Classificador = adjetivo(classificadorModificacao,adjetivo_classificador,generoAdjetivo, numeroAdjetivo)

			Epíteto = adjetivo(epitetoModificacao,adjetivo_epiteto,generoAdjetivo, numeroAdjetivo)

			Qualificador = qualificador(temQualificador, tipoQualificador, indicePreposicao,
										DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
										gênero_beta, número_beta, morfologia_do_pronome_beta,
										DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
										número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
										número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade,  #
										funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
										milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso, numIndefinido,
										tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
										tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado,
										numero,tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
										pessoa_da_interlocucao, transitividade_verbo, tonicidade,
										morfologia_do_pronome, reflexivo,  #
										epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
										adjetivo_classificador, generoAdjetivo,
										numeroAdjetivo, contracao)

			GN = Determinante + ' ' + numerativo + ' ' + ente + ' ' + Classificador + ' ' + Epíteto + ' ' + Qualificador

		else:

			Núcleo_lógico = estrutura_GN_downraked(dissocEnteNucleo, temQualificador, tipoQualificador, indicePreposicao,
					 DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, gênero_beta, número_beta,
					 morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
					 gênero_alpha, número_alpha, morfologia_do_pronome_alpha,
					 pessoa_da_interlocução_possuidor, número_obj_possuído, gênero_obj_possuído,
					 pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal, genero,
					 tipo_precisa, tipoRealCard, milharExtenso, centenaExtenso,
					 dezenaExtenso, unidadeExtenso, numIndefinido,
					 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
					 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado,
					 numero, tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
					 pessoa_da_interlocucao, transitividade_verbo, tonicidade, morfologia_do_pronome,
					 reflexivo, epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
					 adjetivo_classificador, generoAdjetivo, numeroAdjetivo,contracao)

			Qualificador = qualificador(temQualificador,tipoQualificador,indicePreposicao,DETERMINAÇÃO_espeficifidade_beta,ORIENTAÇÃO_beta,
					 gênero_beta,número_beta,morfologia_do_pronome_beta,
					 DETERMINAÇÃO_espeficifidade_alpha,ORIENTAÇÃO_alpha,gênero_alpha,
					 número_alpha,morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
					 número_obj_possuído, gênero_obj_possuído,pessoa_da_interlocução_proximidade,#
					 funcaoNumerativo,cardinal,genero,tipo_precisa,tipoRealCard,
					 milharExtenso,centenaExtenso,dezenaExtenso,unidadeExtenso,numIndefinido,
					 tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
					 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
					 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
					 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,#
					 epitetoModificacao,adjetivo_epiteto,classificadorModificacao,adjetivo_classificador,generoAdjetivo ,
										numeroAdjetivo , contracao )

			GN = Núcleo_lógico + ' ' + Qualificador
		return  (re.sub(' +', ' ', GN).strip())
	except:
		GN = ''
		return GN
# #
#
# estrutura_GN(DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
# 			 gênero_alpha='masculino',número_alpha='singular', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s', número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 genero='não-binário', tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='instituição',classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='desmatamento', numero='singular')
#
#
# estrutura_GN(DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
# 			 gênero_alpha='masculino',número_alpha='singular', morfologia_do_pronome_alpha=None,
# 			 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
# 			 genero='não-binário', tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='instituição',classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='desmatamento', numero='singular')

# estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicao=None,
# 				 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
# 				 morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
# 				 gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
# 				 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
# 				 pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero='não-binário',
# 				 tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
# 				 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 				 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='abstração_material',
# 				 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum', substantivo_lematizado='jogo',
# 				 numero='singular', tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
# 				 pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome="Morfologia_padrão",
# 				 reflexivo=None, epitetoModificacao=None, adjetivo_epiteto=None, classificadorModificacao=None,
# 				 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None,contracao=None)
# # ########PREPOSIÇÃO
# preposicoes = ['a','ante','após','até','com','contra',
# 				   'de','desde','em','entre','para','por','perante','sem',
# 				   'sob','sobre','trás']



def preposicao(indice):
	opcoes = ['a', 'ante', 'após', 'até', 'com', 'contra',
				   'de', 'desde', 'em', 'entre', 'para', 'por', 'perante', 'sem',
				   'sob', 'sobre', 'trás']
	nums = [x for x in range(len(opcoes))]
	preposicoes = dict(zip(nums, opcoes))

	preposicao=preposicoes[indice]
	return preposicao
# preposicao(0)
# preposicao(11)


# print("Com ou sem contração")
# contracao = choice.Menu(['+contração', '-contração']).ask()

def frase_preposicional(indicePreposicao=None, dissocEnteNucleo=None, temQualificador=None,
						tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
						gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
						DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
						número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
						número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
						funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
						milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
						numIndefinido=None, tipo_de_Ente=None, tipo_de_nao_consciente=None,
						tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
						classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
						tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
						pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
						morfologia_do_pronome=None, reflexivo=None, epitetoModificacao=None,
						adjetivo_epiteto=None, classificadorModificacao=None,
						adjetivo_classificador=None,generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
	'''
    '''
	try:
		prep = preposicao(indicePreposicao)
		grupo_nominal = (re.sub(' +', ' ',
						estrutura_GN_downraked(
							dissocEnteNucleo, temQualificador, tipoQualificador, indicePreposicao,
							DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, gênero_beta, número_beta,
							morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
							gênero_alpha, número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
							número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade, funcaoNumerativo,
							cardinal, genero, tipo_precisa, tipoRealCard, milharExtenso, centenaExtenso, dezenaExtenso,
							unidadeExtenso, numIndefinido, tipo_de_Ente, tipo_de_nao_consciente,
							tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico, classe_palavra_Ente,
							substantivo_lematizado, numero, tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
							pessoa_da_interlocucao, transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
							epitetoModificacao, adjetivo_epiteto, classificadorModificacao, adjetivo_classificador,
							generoAdjetivo, numeroAdjetivo, contracao))).strip()

		if prep == 'por':
			if grupo_nominal[:2] == 'o ':
				frase_prep = 'pel' + grupo_nominal
			elif grupo_nominal[:2] == 'a ':
				frase_prep = 'pel' + grupo_nominal
			else:
				frase_prep = prep + ' ' + grupo_nominal
		elif prep == 'a':
			if grupo_nominal[:2] == 'a ':
				E = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
			elif grupo_nominal[:2] == 'o ':
				frase_prep = prep + grupo_nominal
			elif grupo_nominal[:5] == 'aquel':
				frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
			else:
				frase_prep = prep + ' ' + grupo_nominal
		elif prep == 'de':
			if (grupo_nominal[:2] == 'o ' or grupo_nominal[:2] == 'a ' or grupo_nominal[:3] == 'est' or
					grupo_nominal[:3] == 'ist' or grupo_nominal[:3] == 'ess' or grupo_nominal[:3] == 'iss'
					or grupo_nominal[:5] == 'aquel' or grupo_nominal[:5] == 'aquil'):
				frase_prep = (prep[slice(-1)]) + grupo_nominal
			elif (grupo_nominal[:2] == 'um' or  grupo_nominal[:2] == 'un' or
				  grupo_nominal[:2] == 'el' or grupo_nominal[:4] == 'outr'):

				if contracao == '+contração':
					frase_prep = (prep[slice(-1)]) + grupo_nominal
				else:
					frase_prep = prep + ' ' + grupo_nominal
			else:
				frase_prep = prep + ' ' + grupo_nominal
		elif prep == 'em':
			if (
					grupo_nominal[:2] == 'o ' or grupo_nominal[:2] == 'a ' or
					grupo_nominal[:2] == 'el' or grupo_nominal[:3] == 'est' or
					grupo_nominal[:3] == 'ist' or grupo_nominal[:3] == 'ess' or
					grupo_nominal[:3] == 'iss' or grupo_nominal[:5] == 'aquel' or
					grupo_nominal[:5] == 'aquil'
			):
				frase_prep = 'n' + grupo_nominal
			else:
				if (
						grupo_nominal[:2] == 'um' or grupo_nominal[:2] == 'un' or
						grupo_nominal[:4] == 'outr'
				):

					if contracao == '+contração':
						frase_prep = 'n' + grupo_nominal
					else:
						frase_prep = prep + ' ' + grupo_nominal

		elif prep == 'para':
			if (
					grupo_nominal[:2] == 'o ' or grupo_nominal[:2] == 'a '
			):
				if contracao == '+contração':
					frase_prep = 'pr' + grupo_nominal
				else:
					frase_prep = prep + ' ' + grupo_nominal
			else:
				frase_prep = prep + ' ' + grupo_nominal
		else:
			frase_prep = prep + ' ' + grupo_nominal
	except:
		frase_prep = ''
	return frase_prep
#
# for i in range(12):
# 	frase = frase_preposicional(indicePreposicao=i,dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,
# 					DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='feminino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído=None,
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='não-binário', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='objeto_material',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='árvore', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='alto',
# 			 classificadorModificacao=None,adjetivo_classificador=None,generoAdjetivo='feminino',
# 								numeroAdjetivo='plural', contracao='+contração')
# 	print(frase)
frase_preposicional(10,None,None,None,
					None, None,
			 None,None, None,
			 'específico','orientação_específica_proximidade',
			 'feminino',
			 'plural', 'morfologia_terceira_pessoa',
			 '1s',
			 'plural', None,
			 'próximo_ao_não_interlocutor',  #
			 None, None, 'não-binário', None, None,
			 None, None,None, None, None,
			 'consciente',None,
			None,
			 None, 'substantivo_comum',
			'menino', 'plural',
			None, None, None, None,None,
			 None, None,None,None,  #
			 'sim','alto',
			None,None,'feminino',
			'plural','+contração')
# frase_preposicional(indicePreposicao=4,
# 					 genero='não-binário',
# 					tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 					tipo_de_nao_consciente_material='abstração_material', classe_palavra_Ente='substantivo_comum',
# 					substantivo_lematizado='certeza', numero='singular')
#
# frase_preposicional(indicePreposicao=6, dissocEnteNucleo=None, temQualificador=None,
# 						tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 						gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 						DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
# 						número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
# 						número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
# 						funcaoNumerativo=None, cardinal=None, genero='não-binário', tipo_precisa=None, tipoRealCard=None,
# 						milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
# 						numIndefinido=None, tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 						tipo_de_nao_consciente_material='abstração_material', tipo_de_nao_consciente_semiotico=None,
# 						classe_palavra_Ente='substantivo_comum', substantivo_lematizado='futebol', numero='singular',
# 						tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
# 						pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
# 						morfologia_do_pronome=None, reflexivo=None, epitetoModificacao=None,
# 						adjetivo_epiteto=None, classificadorModificacao=None,
# 						adjetivo_classificador=None,generoAdjetivo=None, numeroAdjetivo=None, contracao=None)

# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			 epitetoModificacao='sim',adjetivo_epiteto='bonito',
# 			 classificadorModificacao=None,adjetivo_classificador=None)

# # ############ORDEM DA ORAÇÃO
# print('Há circunstância?')
# temCircunstancia = choice.Menu(['sim', 'não']).ask()
# print('Selecione o tipo_pessoa de grupo que realiza a circunstância:')
# realizacaoCircunstancia = choice.Menu(['grupo_nominal', 'frase_preposicional', 'grupo_adverbial']).ask()

def circunstancia(temCircunstancia=None,realizacaoCircunstancia=None,
				  indicePreposicao=None, dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None,
				  DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
				  gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
				  DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
				  número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
				  número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,  #
				  funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
				  milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
				  numIndefinido=None,
				  tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
				  tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
				  numero=None,
				  tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
				  pessoa_da_interlocucao=None,
				  transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
				  epitetoModificacao=None, adjetivo_epiteto=None, classificadorModificacao=None,
				  adjetivo_classificador=None,generoAdjetivo=None, numeroAdjetivo=None,
				  contracao=None,
				  tipo_de_adverbio1=None, ind1=None,
				  tipo_de_adverbio2=None, ind2=None,
				  tipo_de_adverbio3=None, ind3=None,
				  tipo_de_adverbio4=None, ind4=None,
				  tipo_de_adverbio5=None, ind5=None
	):
	'''
    '''

	if temCircunstancia == None:
		Circunstancia = ''
	else:
		if realizacaoCircunstancia == 'grupo_nominal':
			Circunstancia = estrutura_GN_downraked(dissocEnteNucleo, temQualificador, tipoQualificador,
												   indicePreposicao, DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
												   gênero_beta, número_beta, morfologia_do_pronome_beta,
												   DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
												   número_alpha, morfologia_do_pronome_alpha,
												   pessoa_da_interlocução_possuidor,
												   número_obj_possuído, gênero_obj_possuído,
												   pessoa_da_interlocução_proximidade,  #
												   funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
												   milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
												   numIndefinido,
												   tipo_de_Ente, tipo_de_nao_consciente,
												   tipo_de_nao_consciente_material,
												   tipo_de_nao_consciente_semiotico, classe_palavra_Ente,
												   substantivo_lematizado, numero,
												   tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
												   pessoa_da_interlocucao,
												   transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
												   #
												   epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
												   adjetivo_classificador,
												   generoAdjetivo, numeroAdjetivo, contracao)
		elif realizacaoCircunstancia == 'frase_preposicional':
			Circunstancia = frase_preposicional(indicePreposicao, dissocEnteNucleo, temQualificador, tipoQualificador,
												DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
												gênero_beta, número_beta, morfologia_do_pronome_beta,
												DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
												número_alpha, morfologia_do_pronome_alpha,
												pessoa_da_interlocução_possuidor,
												número_obj_possuído, gênero_obj_possuído,
												pessoa_da_interlocução_proximidade,  #
												funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
												milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
												numIndefinido, tipo_de_Ente, tipo_de_nao_consciente,
												tipo_de_nao_consciente_material,
												tipo_de_nao_consciente_semiotico, classe_palavra_Ente,
												substantivo_lematizado,
												numero, tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
												pessoa_da_interlocucao, transitividade_verbo, tonicidade,
												morfologia_do_pronome, reflexivo,  #
												epitetoModificacao, adjetivo_epiteto, classificadorModificacao,
												adjetivo_classificador, generoAdjetivo, numeroAdjetivo, contracao)
		elif realizacaoCircunstancia == 'grupo_adverbial':
			Circunstancia = grupo_adverbial(tipo_de_adverbio1, ind1,
											tipo_de_adverbio2, ind2,
											tipo_de_adverbio3, ind3,
											tipo_de_adverbio4, ind4,
											tipo_de_adverbio5, ind5)


	return re.sub(' +',' ',Circunstancia).strip()
circunstancia(temCircunstancia='+',realizacaoCircunstancia='grupo_adverbial', indicePreposicao=None,dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade', gênero_alpha='masculino', número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa', pessoa_da_interlocução_possuidor='1s', número_obj_possuído='plural', gênero_obj_possuído='masculino', pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',   funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None, tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='animal', tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum', substantivo_lematizado='prédio', numero='plural', tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,   epitetoModificacao='sim',adjetivo_epiteto='alto', classificadorModificacao=None,adjetivo_classificador=None,generoAdjetivo='masculino' , numeroAdjetivo='plural',contracao='-contração' ,tipo_de_adverbio1='Modo', ind1=10)







# # ##SISTEMAS DA ORAÇÃO
# #
## no caso de materiais meteorológicas, o Meio conflui
	# com o Processo (por isso :AG_processo_sem_alcance,AG_processo_com_alcance );
	# pode haver escopo (Ex.: choveu uma chuva grossa)
def AGENCIAMENTO(indice):

	"""
	:param AGENCIAMENTO= [0:'AG_médio_sem_alcance',1:'AG_médio_com_alcance',
	    2:'AG_efetivo_operativo',3:'AG_efetivo_receptivo',
	   4:'AG_efetivo_receptivo_não_agentivo',5:'AG_processo_sem_alcance',
	   6:'AG_processo_com_alcance']
	:return: AGENCIAMENTO
	"""
	try:
		opcoes = ['AG_médio_sem_alcance',
		 'AG_médio_com_alcance',
		 'AG_efetivo_operativo',
		 'AG_efetivo_receptivo',
		 'AG_efetivo_receptivo',
		 'AG_processo_sem_alcance',
		 'AG_processo_com_alcance']
		nums = [x for x in range(len(opcoes))]
		tipos = dict(zip(nums, opcoes))
		AGENCIAMENTO = tipos[indice]
	except:
		AGENCIAMENTO=None
	return AGENCIAMENTO
#
# AGENCIAMENTO(2)
# AGENCIAMENTO(5)


# #
# # ###tipos de processo oração
# # # Material
# # ##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)

def PROCESSO_MATERIAL(indice=None):
	"""

	:param indice= 0:'PR_material_transformativo_IMPA_transitivo',
			  1:'PR_material_criativo_IMPA_transitivo',
			  2:'PR_material_transformativo_IMPA_intransitivo',
			  3:'PR_material_criativo_IMPA_intransitivo'
	:return: Processo_material
	"""
	opcoes = ['PR_material_transformativo_IMPA_transitivo',
			  'PR_material_criativo_IMPA_transitivo',
			  'PR_material_transformativo_IMPA_intransitivo',
			  'PR_material_criativo_IMPA_intransitivo']
	nums = [x for x in range(len(opcoes))]
	tipos = dict(zip(nums, opcoes))
	Processo_material = tipos[indice]

	return Processo_material
# # for i in range(4):
# 	print(PROCESSO_MATERIAL(i))
# PROCESSO_MATERIAL(2)

def PROCESSO_RELACIONAL(indiceRel=None,indiceAtrib=None):
   """
	:param tipo_de_relacional= 'PR_relacional_intensivo_atributivo',
                                      'PR_relacional_intensivo_identificativo',
                                      'PR_relacional_possessivo_atributivo',
                                      'PR_relacional_possessivo_identificativo',
                                      'PR_relacional_circunstancial_atributivo',
                                      'PR_relacional_circunstancial_identificativo
	:param atribuicao_relacao= 'atribuição_proj_ment_cognitiva',
                                        'atribuição_proj_ment_desiderativa',
                                        'atribuição_proj_verbal',
                                        'atribuição_expan_elaboração',
                                        'atribuição_expan_intencificação',
                                        'sem_atribuição_de_relação'

	:return: relacional
   """
   opcoesRelacional = ['PR_relacional_intensivo_atributivo',
					   'PR_relacional_intensivo_identificativo',
					   'PR_relacional_possessivo_atributivo',
					   'PR_relacional_possessivo_identificativo',
					   'PR_relacional_circunstancial_atributivo',
					   'PR_relacional_circunstancial_identificativo']
   numsRel = [x for x in range(len(opcoesRelacional))]
   tiposRel = dict(zip(numsRel, opcoesRelacional))
   tipoRel = tiposRel[indiceRel]

   opcoesAtribuicao = ['atribuição_proj_ment_cognitiva',
			 'atribuição_proj_ment_desiderativa',
			 'atribuição_proj_verbal',
			 'atribuição_expan_elaboração',
			 'atribuição_expan_intencificação',
			 'sem_atribuição_de_relação']
   numsAtribuicao = [x for x in range(len(opcoesAtribuicao))]
   tiposAtrobuicao = dict(zip(numsAtribuicao,opcoesAtribuicao))
   tipoAtrib = tiposAtrobuicao[indiceAtrib]

   relacional =  tipoRel + '_' +  tipoAtrib

   return relacional

# PROCESSO_RELACIONAL(0,5)


# # # TRANSITIVIDADE
# #
# #
# # ##subsistemas
# #
# # ##agenciamento oração
# #
# # ##MODO
# #
# # # subsistemas:
# #
# # # sujeitabilidade
# # # coloquei aqui apenas responsabilidade e pressuposição pois
# # # pessoa e número já é decidido na ordem da palavra 9tenho que ver o impacto teórico que
# # ##isso tem..não sei se preciso repetir as escolhas)

def SUJEITABILIDADE(indiceRespo=None,indicePress=None):
	"""

	:param RESPONSABILIDADE=0:'SUJ_responsável',1:'SUJ_distante_impessoal',
	                        2:'SUJ_distante_não_responsável', 3:'SUJ_-sujeitabilidade'
	:param PRESSUPOSICAO_DO_SUJEITO = 0:'recuperado_explícito', 1:'recuperado_implícito',
	                                2:'não_recuperável', 3:'recuperação_NA'
	:return: SUJEITABILIDADE
	"""
	opcoesRespo = ['SUJ_responsável', 'SUJ_distante_impessoal',
				   'SUJ_distante_não_responsável', 'SUJ_-sujeitabilidade']
	numsRespo = [x for x in range(len(opcoesRespo))]
	tiposRespon = dict(zip(numsRespo, opcoesRespo))
	tipoRespon = tiposRespon[indiceRespo]

	opcoesPress = ['recuperado_explícito', 'recuperado_implícito',
				   'não_recuperável', 'recuperação_NA']
	numsPress = [x for x in range(len(opcoesPress))]
	tiposPress = dict(zip(numsPress,opcoesPress))
	tipoPress = tiposPress[indicePress]
	SUJEITABILIDADE = tipoRespon + '_' + tipoPress

	return SUJEITABILIDADE

# SUJEITABILIDADE(0,0)

def TIPO_DE_MODO(indiceModo):
	"""

	:param TIPO_MODO= 'MOD_declarativo_+perguntafinito', 'MOD_declarativo_-perguntafinito',
	                   'MOD_interrogativo_elemental','MOD_interrogativo_polar',
	                   'MOD_imperativo'
	:return:
	"""
	opcoes = ['MOD_declarativo_+perguntafinito', 'MOD_declarativo_-perguntafinito',
			  'MOD_interrogativo_elemental', 'MOD_interrogativo_polar',
			  'MOD_imperativo']
	try:
		nums= [x for x in range(len(opcoes))]
		tiposModo = dict(zip(nums,opcoes))
		tipoModo = tiposModo[indiceModo]
	except:
		tipoModo='MOD_declarativo_-perguntafinito'
	return tipoModo
# TIPO_DE_MODO(3)
# #
# # ########
# #
# #
# # ######


def AVALIACAO_MODAL(AVALIACAO=None,POLARIDADE=None):
	"""

	:param POLARIDADE= positiva', 'negativa'
	##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
		# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
	:param AVALIACAO= '+', '-'
	:return: AVALIACAO_MODAL
	"""

	if AVALIACAO == '-':
		AVALIACAO_MODAL = ''

	else:
		if POLARIDADE == 'positiva':
			AVALIACAO_MODAL = ''

		elif POLARIDADE == 'negativa':
			AVALIACAO_MODAL = 'não'

	return AVALIACAO_MODAL

# AVALIACAO_MODAL(AVALIACAO='+',POLARIDADE='negativa')
###

def POLARIDADE(tipo_polaridade=None):
	"""

	:param tipo_polaridade= 'positiva', 'negativa'
	:return: Adjunto_polaridade
	"""

	if tipo_polaridade == 'positiva':
		Adjunto_polaridade = ''

	elif tipo_polaridade == 'negativa':
		Adjunto_polaridade = 'não'

	return Adjunto_polaridade
# POLARIDADE('positiva')
# POLARIDADE('negativa')

# #
# # ##############
# #
# # ## Preciso resolver como vou abordar a questão deste sistema: por enquanto vou mexer apenas com
# # # polaridade, e ir incrementando as combinações.

def TIPO_AVALIACAO_MODAL(AVALIACAO=None,POLARIDADE=None):
	"""
	:param AVALIACAO= "+". "-"
	:param POLARIDADE= "positiva", "negativa"
	:return: tipo_de_avaliacao_modal
	"""

	if AVALIACAO == '-':
		tipo_de_avaliacao_modal = 'AvM_sem_avaliação_modal'

	else:
		if POLARIDADE == 'positiva':
			tipo_de_avaliacao_modal = 'AvM_polaridade_positiva'

		elif POLARIDADE == 'negativa':
			tipo_de_avaliacao_modal = 'AvM_polaridade_negativa'

	return tipo_de_avaliacao_modal
# TIPO_AVALIACAO_MODAL(AVALIACAO="-")
# TIPO_AVALIACAO_MODAL(AVALIACAO="+",POLARIDADE="negativa")
# TIPO_AVALIACAO_MODAL(AVALIACAO="+",POLARIDADE="positiva")


##para o sistema de modo, AINDA não considerei o subsistema de VALIDAÇÃO. (será implementado)

def MODO(RESPONSABILIDADE=None,PRESSUPOSICAO_DO_SUJEITO=None,TIPO_MODO=None):
	"""

	:param RESPONSABILIDADE= 0:'SUJ_responsável',1:'SUJ_distante_impessoal',
	                        2:'SUJ_distante_não_responsável', 3:'SUJ_-sujeitabilidade'
	:param PRESSUPOSICAO_DO_SUJEITO=0:'recuperado_explícito', 1:'recuperado_implícito',
	                                2:'não_recuperável', 3:'recuperação_NA'
	:param TIPO_MODO= 0:'MOD_declarativo_+perguntafinito', 1:'MOD_declarativo_-perguntafinito',
	                   2:'MOD_interrogativo_elemental',3:'MOD_interrogativo_polar',
	                   4:'MOD_imperativo'
	:return:
	"""
	MODO = SUJEITABILIDADE(RESPONSABILIDADE,PRESSUPOSICAO_DO_SUJEITO) + '_' + TIPO_DE_MODO(TIPO_MODO)
	return MODO

# MODO(RESPONSABILIDADE=0,PRESSUPOSICAO_DO_SUJEITO=0,TIPO_MODO=1)
# MODO(RESPONSABILIDADE=3,PRESSUPOSICAO_DO_SUJEITO=3,TIPO_MODO=1)

# # # A DÊIXIS: VER, POIS ELA É DECIDIDA DESDE A ORDEM DA PALAVRA...
# #
# #
# # # TEMA
# #
# Tema_textual = choice.Menu(['+', '-']).ask()
# print('Há TEMA TEXTUAL continuativo?')
# 		tem_continuativo = choice.Menu(['sim', 'não']).ask()
# print('Há TEMA TEXTUAL continuativo?')
# 		tem_continuativo = choice.Menu(['sim', 'não']).ask()
# 		if tem_continuativo == 'não':
# 			TEMA_CONTINUATIVO = ''
# 		else:
# 			TEMA_CONTINUATIVO = conjunção_continuativa() + ','
# 		print('Há TEMA TEXTUAL conjuntivo?')
# 		tem_conjuntivo = choice.Menu(['sim', 'não']).ask()
# 		if tem_conjuntivo == 'não':
# 			TEMA_CONJUNTIVO = ''
# 		else:
# 			TEMA_CONJUNTIVO = grupo_conjuntivo()
# 		print('Há TEMA TEXTUAL relativo?')
# 		tem_relativo = choice.Menu(['sim', 'não']).ask()
# 		if tem_relativo == 'não':
# 			TEMA_RELATIVO = ''
# 		elif tem_relativo == 'sim':
# 			print('Qual a tipo_pessoa de relativo?')
# 			tipo_de_relativo = choice.Menu(['nominal', 'adverbial']).ask()
# 			if tipo_de_relativo == 'nominal':
# 				TEMA_RELATIVO = pronome_relativo()
# 			elif tipo_de_relativo == 'adverbial':
# 				TEMA_RELATIVO = choice.Menu(['de onde', 'quando',
# 				                             'onde', 'de quando', 'que', 'por onde']).ask()


def conjuncao_continuativa(tipo_insercao="inserção_menu",indice=None,conj_extenso=None):
	"""

	:param tipo_insercao= "inserção_menu", "inserção_extenso"
	:param indice=  0:"e",1:"é",2:"ah",3:'mas',4:'sim',5:'bem',6:'não',7:'agora',8:'então',9:'pois é',10:'assim'
				 ,11:'ó',12:'daí',13:'aí' ,14:'aí então',15:'quer dizer',16:'assim',17:'em seguida',18:'por fim'
				  ,19:'porque',20:'porém',21:'também',22:'é que',23:'olha'
	:param conj_extenso = entre o elemento por extenso
	:return:conjuncao
	"""
	try:
		if tipo_insercao == "inserção_menu":
			opcoes = [ "e","é","ah",'mas','sim','bem','não','agora','então','pois é','assim'
					 ,'ó','daí','aí' ,'aí então','quer dizer','assim','em seguida','por fim'
					  ,'porque','porém','também','é que','olha']

			nums = [x for x in range(len(opcoes))]
			conjuncoes = dict(zip(nums, opcoes))
			conjuncao = conjuncoes[indice]
		else:
			conjuncao=conj_extenso
		return conjuncao
	except:
		conjuncao=''
		return conjuncao
# conjuncao_continuativa(tipo_insercao="inserção_menu",indice=23,conj_extenso=None)
# conjuncao_continuativa()
# print('Qual a tipo_pessoa de relativo?')
# tipo_de_relativo = choice.Menu(['nominal', 'adverbial']).ask()
# if tipo_de_relativo == 'nominal':
# 	TEMA_RELATIVO = pronome_relativo()
# elif tipo_de_relativo == 'adverbial':
# 	TEMA_RELATIVO = choice.Menu(['de onde', 'quando',
# 								 'onde', 'de quando', 'que', 'por onde']).ask()
#

def TEMA_TEXTUAL(temTemaTextual=None, tipo_insercao_Cont="inserção_menu",conj_extenso_Cont=None,indiceCont=None,
				 tipo_insercao_Conj="inserção_menu",tipo_de_conjuncao_Conj=None, conj_extensoConj=None,indiceConj=None,
				 tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None,tipo_de_relativo=None,
				 tipo_pronome_relativo=None, genero=None, numero=None, indiceRelativo=None, indiceRelativoAdv=None):
	try:
		if temTemaTextual == '+':
			TEMA_CONTINUATIVO = conjuncao_continuativa(tipo_insercao_Cont,indiceCont,conj_extenso_Cont)
			TEMA_CONJUNTIVO = grupo_conjuntivo(tipo_insercao_Conj, conj_extensoConj, tipo_de_conjuncao_Conj, indiceConj)

			if tipo_de_relativo == 'nominal':
				TEMA_RELATIVO = pronome_relativo(tipo_insercao_Rel,pron_extenso_Rel,tipo_pronome_relativo,genero,numero, indiceRelativo)
			elif tipo_de_relativo == 'adverbial':
				opcoes = ['de onde', 'quando',
						  'onde', 'de quando', 'que', 'por onde']

				nums = [x for x in range(len(opcoes))]
				relativos = dict(zip(nums, opcoes))
				TEMA_RELATIVO = relativos[indiceRelativoAdv]
			else:
				TEMA_RELATIVO=''
		TEMA_TEXTUAL = TEMA_CONTINUATIVO +' '+ TEMA_CONJUNTIVO +' '+ TEMA_RELATIVO
	except:
		TEMA_TEXTUAL=''
	return TEMA_TEXTUAL



TEMA_TEXTUAL('+', "inserção_menu",None,3, "inserção_menu",None, None,None, 'inserção_menu',None,None, None, None,None,None, None)

TEMA_TEXTUAL(temTemaTextual='+',
			 tipo_insercao_Cont="inserção_menu",indiceCont=3,conj_extenso_Cont=None,
			 tipo_insercao_Conj="inserção_menu",tipo_de_conjuncao_Conj=None, conj_extensoConj=None,indiceConj=None,
			 tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None,tipo_de_relativo=None,
			 tipo_pronome_relativo=None,
			 genero=None, numero=None, indiceRelativo=None,
			 indiceRelativoAdv=None)


# TEMA_TEXTUAL(temTemaTextual='+', tipo_insercao_Cont="inserção_menu",indiceCont=3,conj_extenso_Cont=None,
# 				 tipo_insercao_Conj="inserção_menu",tipo_de_conjuncao_Conj='paratática_adversativa',
# 			 conj_extensoConj=None,indiceConj=2,
#
# 				 tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None,tipo_de_relativo='nominal',
# 				 tipo_pronome_relativo='variável', genero='masculino', numero='singular',
# 			 indiceRelativo=3, indiceRelativoAdv=None)
#
#
# TEMA_TEXTUAL(temTemaTextual='+', tipo_insercao_Cont="inserção_menu",conj_extenso_Cont=None,indiceCont=23,
# 				 tipo_insercao_Conj="inserção_menu",tipo_de_conjuncao_Conj='paratática_alternativa',
# 			 conj_extensoConj=None,indiceConj=1,
# 				 tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None,tipo_de_relativo='nominal',
# 				 tipo_pronome_relativo='variável', genero='masculino', numero='singular', indiceRelativo=2,
# 			 indiceRelativoAdv=1)


###tema interpessoal
# TIPO_TEMA_INTERPESSOAL = choice.Menu(['TI_avaliação_modo', 'TI_avaliação_comentário',
# 		                                      'TI_encenação_troca', 'TI_encenação_papel_falante', 'TI_polaridade',
# 		                                      'TI_encenação_papel_ouvinte',
# 		                                      'TI_NA']).ask()
# tipo_realizacao = choice.Menu(['grupo_adverbial', 'frase_preposicional']).ask()


def TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL=None,tipoRealizacao=None,
					  #grupo adverbial
					  tipo_de_adverbio1=None, ind1=None,
					  tipo_de_adverbio2=None, ind2=None,
					  tipo_de_adverbio3=None, ind3=None,
					  tipo_de_adverbio4=None, ind4=None,
					  tipo_de_adverbio5=None, ind5=None,

					#frase prepos
					  indicePreposicao=None, dissocEnteNucleo=None, temQualificador=None,
					  tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
					  gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
					  DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
					  número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
					  número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
					  funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
					  milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
					  numIndefinido=None, tipo_de_Ente=None, tipo_de_nao_consciente=None,
					  tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
					  classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
					  tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
					  pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
					  morfologia_do_pronome=None, reflexivo=None, epitetoModificacao=None,
					  adjetivo_epiteto=None, classificadorModificacao=None,
					  adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None,

					#
					  indiceElemQu=None, indicePartModal=None,
					  nome_proprio=None):

	try:

		if (TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_modo' or TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_comentário'):
			if tipoRealizacao=='grupo_adverbial':
				TEMA_INT = grupo_adverbial(tipo_de_adverbio1, ind1,
										   tipo_de_adverbio2, ind2,
										   tipo_de_adverbio3, ind3,
										   tipo_de_adverbio4, ind4,
										   tipo_de_adverbio5, ind5, )
			elif tipoRealizacao=='frase_preposicional':
				TEMA_INT = frase_preposicional(indicePreposicao, dissocEnteNucleo, temQualificador,
					  tipoQualificador, DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
					  gênero_beta, número_beta, morfologia_do_pronome_beta,
					  DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
					  número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
					  número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade,
					  funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
					  milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
					  numIndefinido, tipo_de_Ente, tipo_de_nao_consciente,
					  tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
					  classe_palavra_Ente, substantivo_lematizado, numero,
					  tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
					  pessoa_da_interlocucao, transitividade_verbo, tonicidade,
					  morfologia_do_pronome, reflexivo, epitetoModificacao,
					  adjetivo_epiteto, classificadorModificacao,
					  adjetivo_classificador, generoAdjetivo, numeroAdjetivo, contracao)

		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_troca':
			TEMA_INT = elemento_qu(indiceElemQu)

		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_falante':
			TEMA_INT = particula_modal(indicePartModal)
		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_ouvinte':
			TEMA_INT = nome_proprio(nome_proprio)
	except:
		TEMA_INT=''

	return TEMA_INT

TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL="TI_avaliação_comentário",tipoRealizacao='frase_preposicional',
					  #grupo adverbial
					  tipo_de_adverbio1=None, ind1=None,
					  tipo_de_adverbio2=None, ind2=None,
					  tipo_de_adverbio3=None, ind3=None,
					  tipo_de_adverbio4=None, ind4=None,
					  tipo_de_adverbio5=None, ind5=None,

					#frase prepos
					  indicePreposicao=4, dissocEnteNucleo=None, temQualificador=None,
					  tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
					  gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
					  DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
					  número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
					  número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
					  funcaoNumerativo=None, cardinal=None, genero='não-binário', tipo_precisa=None, tipoRealCard=None,
					  milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
					  numIndefinido=None, tipo_de_Ente='não_consciente', tipo_de_nao_consciente=None,
					  tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico='abstração_semiótica',
					  classe_palavra_Ente='substantivo_comum', substantivo_lematizado='certeza', numero='singular',
					  tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
					  pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
					  morfologia_do_pronome=None, reflexivo=None, epitetoModificacao=None,
					  adjetivo_epiteto=None, classificadorModificacao=None,
					  adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None,

					#
					  indiceElemQu=None, indicePartModal=None,
					  nome_proprio=None)
TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL="TI_avaliação_comentário", tipoRealizacao='frase_preposicional',
				  indicePreposicao=4,
				  genero='não-binário',
				  tipo_de_Ente='não_consciente', tipo_de_nao_consciente='semiótico',
				  tipo_de_nao_consciente_material=None, classe_palavra_Ente='substantivo_comum',
				  substantivo_lematizado='certeza', numero='singular'
				  )
#
# TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL='TI_avaliação_comentário',
# 				  tipoRealizacao='grupo_adverbial', tipo_de_adverbio1='Modo', ind1=12)

####TEMA IDEACIONAL
# print('Qual a ORIENTAÇÃO MODAL do tema?')
# 	ORIENTAÇÃO_MODAL = choice.Menu(['orientado', 'não_orientado']).ask()
#
# 	print('Qual a ORIENTAÇÃO TRANSITIVA do tema?')
# 	ORIENTACAO_TRANSITIVA = choice.Menu(['direcional', 'não_direcional']).ask()
#
# 	print('Qual a SELEÇÃO TEMÁTICA do tema?')
# 	SELEÇÃO_TEMÁTICA = choice.Menu(['default', 'proeminente']).ask()
# print('Qual o tipo_pessoa de TEMA DEFAULT?')
# 		TEMA_DEFAULT = choice.Menu(['imperativo',
# 		                            'indicativo']).ask()
#
# print('Qual o tipo_pessoa de TEMA DEFAULT INDICATIVO?')
# 			TEMA_DEFAULT_indicativo = choice.Menu(['declarativo',
# 			                                       'interrogativo_polar',
# 			                                       'interrogativo_sujeito_elemental']).ask()
# print('Há TEMA IDENTIFICATIVO?')
# 			TEMA_IDENTIFICATIVO = choice.Menu(['NA',
# 			                                   'equativo_codificação',
# 			                                   'equativo_decodificação']).ask()
# TEMA_ÂNGULO = choice.Menu(['TID_fonte', 'TID_ponto_de_vista']).ask()
# TEMA_ELEMENTAL = choice.Menu(['TID_complemento_elemental', 'TID_adjunto_elemental']).ask()
# TEMA_PROEMINENTE = choice.Menu(['TID_perspectiva_intensificação',
# 		                                'TID_perspectiva_outro',
# 		                                'TID_intensivo_absoluto',
# 		                                'intensivo_relativo_papel_transitivo_nuclear_participante',
# 		                                'TID_intensivo_relativo_papel_transitivo_nuclear_processo',
# 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_elaboração',
# 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_extensão',
# 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto',
# 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_reprisado',
# 		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_recuperável',
# 		                                'TID_intensivo_relativo_predicação_default_local',
# 		                                'TID_intensivo_relativo_predicação_proeminente_local'
#
# 		                                ]).ask()

def TEMA_IDEACIONAL(ORIENTACAO_MODAL=None,ORIENTACAO_TRANSITIVA=None,
					SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
					TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None,
					TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
					TEMA_PROEMINENTE=None):

	if ORIENTACAO_MODAL == 'orientado' and ORIENTACAO_TRANSITIVA == 'direcional'and SELECAO_TEMATICA == 'default':

		if TEMA_DEFAULT == 'imperativo':
			TEMA_IDEACIONAL = 'TID_default_imperativo'

		elif TEMA_DEFAULT == 'indicativo':

			if TEMA_DEFAULT_indicativo == 'declarativo'and TEMA_IDENTIFICATIVO == 'NA':

				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_NA'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'NA':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental'and TEMA_IDENTIFICATIVO == 'NA':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_NA'

			elif TEMA_DEFAULT_indicativo == 'declarativo'and TEMA_IDENTIFICATIVO == 'equativo_decodificação':
				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar'and TEMA_IDENTIFICATIVO == 'equativo_decodificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_decodificação'


			elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_codificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'equativo_codificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'equativo_codificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_codificação'

	elif ORIENTACAO_MODAL == 'não_orientado' and ORIENTACAO_TRANSITIVA == 'direcional'and SELECAO_TEMATICA == 'proeminente':
		if TEMA_ANGULO =='fonte':
			TEMA_IDEACIONAL = 'TID_angulo_fonte'
		elif TEMA_ANGULO =='ponto_de_vista':
			TEMA_IDEACIONAL = 'TID_angulo_ponto_de_vista'
	elif ORIENTACAO_MODAL == 'orientado' and ORIENTACAO_TRANSITIVA == 'não_direcional'and SELECAO_TEMATICA == 'default':
		if TEMA_ELEMENTAL == 'complemento_elemental':
			TEMA_IDEACIONAL = 'TID_complemento_elemental'
		elif TEMA_ELEMENTAL == 'adjunto_elemental':
			TEMA_IDEACIONAL = 'TID_adjunto_elemental'
	elif ORIENTACAO_MODAL == 'não_orientado' and ORIENTACAO_TRANSITIVA == 'não_direcional'and SELECAO_TEMATICA == 'proeminente':

		TEMA_IDEACIONAL = 'TID_proeminente_' + TEMA_PROEMINENTE

	return TEMA_IDEACIONAL
#
# TEMA_IDEACIONAL(ORIENTACAO_MODAL='orientado',ORIENTACAO_TRANSITIVA='direcional',
# 				SELECAO_TEMATICA='default', TEMA_DEFAULT='indicativo',
# 				TEMA_DEFAULT_indicativo='declarativo', TEMA_IDENTIFICATIVO='NA',
# 				TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE=None)
#
# TEMA_IDEACIONAL(ORIENTACAO_MODAL='não_orientado',ORIENTACAO_TRANSITIVA='não_direcional',
# 				SELECAO_TEMATICA='proeminente', TEMA_DEFAULT=None,
# 				TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO='NA',
# 				TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE='intensivo_relativo_papel_transitivo_nuclear_participante')

#intensivo_relativo_papel_transitivo_nuclear_participante

# TEMA_IDEACIONAL(ORIENTACAO_MODAL='orientado',ORIENTACAO_TRANSITIVA='não_direcional',
# 				SELECAO_TEMATICA='default', TEMA_DEFAULT=None,
# 				TEMA_DEFAULT_indicativo='declarativo', TEMA_IDENTIFICATIVO='NA',
# 				TEMA_ANGULO=None, TEMA_ELEMENTAL='complemento_elemental', TEMA_PROEMINENTE=None)

def elemento_qu(indice=None):
	"""

	:param indice: 0:'o que', 1:'quem', 2:'qual', 3:'quanto',
								   4:'quantos', 5:'quando', 6:'como', :7'onde',
								  8:'de quem', 9:'por quê', 10:'pra quê', 11:'por que'
	:return:
	"""
	try:
		opcoes = ['o que', 'quem', 'qual', 'quanto',
				  'quantos', 'quando', 'como', 'onde',
				  'de quem', 'por quê', 'pra quê', 'por que']
		nums = [x for x in range(len(opcoes))]
		elementos = dict(zip(nums, opcoes))
		elemento_qu = elementos[indice]

	except:
		elemento_qu=''

	return elemento_qu

# elemento_qu()
# elemento_qu(56)
# elemento_qu(3)

def particula_modal(indice=None):
	"""

	:param indice: {0: 'né', 1: 'ué', 2: 'ó', 3: 'uai', 4: 'é'}
	##HÁ MAIS PARTÍCULAS....
	:return:
	"""
	try:
		opcoes = ['né', 'ué', 'ó', 'uai', 'é']
		nums = [x for x in range(len(opcoes))]
		particulas = dict(zip(nums, opcoes))
		particula_modal = particulas[indice]

	except:
		particula_modal=''
	return particula_modal
#
# particula_modal(1)
# particula_modal()
# #
# # ## NO CASO DO SISTEMA DE AVALIAÇÃO_MODAL EU NÃO CONTEMPLEI AINDA  O SISTEMA, POR ENQUANTO VOU ME
# # # ATER APENAS AO SUBSISTEMA DE POLARIDADE.
# #
# # ####FORMAÇÃO DA ORAÇÃO
# #
#
####
# print('Qual o tipo_pessoa de Processo?')
# 	TIPO_DE_PROCESSO = choice.Menu(['Material', 'Relacional',
# 	                                'Mental', 'Verbal',
# 	                                'Existencial']).ask()
# print('Selecione as opções do sistema da Oração Material')

def TRANSITIVIDADE(TIPO_DE_PROCESSO=None,indiceMat=None,
				   indiceAgen=None, indiceRel=None,
				   indiceAtrib=None):

	if TIPO_DE_PROCESSO == 'Material':
		Processo = PROCESSO_MATERIAL(indiceMat)
		Agenciamento = AGENCIAMENTO(indiceAgen)

	elif TIPO_DE_PROCESSO == 'Relacional':
		Processo = PROCESSO_RELACIONAL(indiceRel,indiceAtrib)
		Agenciamento = AGENCIAMENTO(indiceAgen)

	elif TIPO_DE_PROCESSO == 'Existencial':
		Processo = 'PR_Existencial'
		Agenciamento = AGENCIAMENTO(indiceAgen)

	elif TIPO_DE_PROCESSO == 'Verbal':
		Processo = 'PR_Verbal'
		Agenciamento = AGENCIAMENTO(indiceAgen)

	elif TIPO_DE_PROCESSO == 'Mental':
		Processo = 'PR_Mental'
		Agenciamento = AGENCIAMENTO(indiceAgen)

	TRANSITIVIDADE = Processo + '_' + Agenciamento
	return TRANSITIVIDADE

# #'PR_relacional_intensivo_atributivo_sem_atribuição_de_relação_AG_médio_com_alcance':
TRANSITIVIDADE(TIPO_DE_PROCESSO='Relacional',indiceMat=None, indiceAgen=1, indiceRel=0, indiceAtrib=5 )

# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=0, indiceAgen=2,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=1, indiceAgen=2,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=1, indiceAgen=2,indiceRel=None, indiceAtrib=None)
# for i in range(3):
# 	for j in range(7):
# 		print(TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=i, indiceAgen=j, indiceRel=None, indiceAtrib=None))
# #
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=0, indiceAgen=0,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=1, indiceAgen=0,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=2, indiceAgen=0,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=3, indiceAgen=0,indiceRel=None, indiceAtrib=None)
#
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=0, indiceAgen=3,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=1, indiceAgen=0,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=2, indiceAgen=0,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=3, indiceAgen=0,indiceRel=None, indiceAtrib=None)
#
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=3, indiceAgen=0,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=3, indiceAgen=1,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=2, indiceAgen=1,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=2, indiceAgen=1,indiceRel=None, indiceAtrib=None)
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Material', indiceMat=2, indiceAgen=6,indiceRel=None, indiceAtrib=None)
#

# TRANSITIVIDADE(TIPO_DE_PROCESSO='Mental', indiceMat=None, indiceAgen=1,indiceRel=None, indiceAtrib=None)
# # TRANSITIVIDADE(TIPO_DE_PROCESSO='Verbal', indiceAgen=2)



# # #




# def oracaoProjetada():
# 	oracao = gerar_oracao()
# 	return oracao
# #
# #
# # def oraçãoDownranked():
# # 	oração = gerar_oracao()
# # 	return oração
# # #
# TIPO_DE_MENTAL = choice.Menu(['superior', 'inferior']).ask()
# 		print('Qual a FENOMENALIZAÇÃO?')
# 		print('Médio sem alcance: FENOMENALIZACAO = não-fenomenalização')
# FENOMENALIZACAO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
# print('Qual tipo_pessoa de Processo superior?')
# TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
#
# print('Qual tipo_pessoa de não-fenomenalização?')
# print('Médio sem alcance: Não-fenomenalização = comportamento-passivo')
# TIPO_NAO_FENOMENALIZACAO= choice.Menu(['comportamento-passivo']).ask()
##terminar de ver a questão do tema interpessoal

def oracaoMental(
	##TRANSITIVIDADE
		TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None, indiceAtrib=None,
	# MODO
		RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
	# TEMA IDEACIONAL
		ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None, TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE=None,
	##específico do Processo Mental
		FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,

		##Processo
		TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None, verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None, padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None, padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None, tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None, padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None, tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None, padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None, verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX='Morfologia_padrão',
		# POLARIDADE
		tipo_polaridade=None,
		##PARTICIPANTES
		# P1
		P1_dissocEnteNucleo=None, P1_temQualificador=None, P1_tipoQualificador=None, P1_indicePreposicao=None, P1_DETERMINAÇÃO_espeficifidade_beta=None, P1_ORIENTAÇÃO_beta=None, P1_gênero_beta=None, P1_número_beta=None, P1_morfologia_do_pronome_beta=None, P1_DETERMINAÇÃO_espeficifidade_alpha=None, P1_ORIENTAÇÃO_alpha=None, P1_gênero_alpha=None, P1_número_alpha=None, P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocução_possuidor=None, P1_número_obj_possuído=None, P1_gênero_obj_possuído=None, P1_pessoa_da_interlocução_proximidade=None, P1_funcaoNumerativo=None, P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipoRealCard=None, P1_milharExtenso=None, P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None, P1_tipo_de_Ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None, P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_Ente=None, P1_substantivo_lematizado=None, P1_numero=None, P1_tipo_feminino_ÃO=None, P1_tipo_masc_ÃO=None, P1_acentTonica=None, P1_nomeProprio=None, P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None, P1_reflexivo=None, P1_epitetoModificacao=None, P1_adjetivo_epiteto=None, P1_classificadorModificacao=None, P1_adjetivo_classificador=None, P1_generoAdjetivo=None, P1_numeroAdjetivo=None, P1_contracao=None,
		# P2
		P2_dissocEnteNucleo=None, P2_temQualificador=None, P2_tipoQualificador=None, P2_indicePreposicao=None, P2_DETERMINAÇÃO_espeficifidade_beta=None, P2_ORIENTAÇÃO_beta=None, P2_gênero_beta=None, P2_número_beta=None, P2_morfologia_do_pronome_beta=None, P2_DETERMINAÇÃO_espeficifidade_alpha=None, P2_ORIENTAÇÃO_alpha=None, P2_gênero_alpha=None, P2_número_alpha=None, P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocução_possuidor=None, P2_número_obj_possuído=None, P2_gênero_obj_possuído=None, P2_pessoa_da_interlocução_proximidade=None, P2_funcaoNumerativo=None, P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipoRealCard=None, P2_milharExtenso=None, P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None, P2_tipo_de_Ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None, P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_Ente=None, P2_substantivo_lematizado=None, P2_numero=None, P2_tipo_feminino_ÃO=None, P2_tipo_masc_ÃO=None, P2_acentTonica=None, P2_nomeProprio=None, P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None, P2_reflexivo=None, P2_epitetoModificacao=None, P2_adjetivo_epiteto=None, P2_classificadorModificacao=None, P2_adjetivo_classificador=None, P2_generoAdjetivo=None, P2_numeroAdjetivo=None, P2_contracao=None,
		##PARTICIPANTES REALIZADOS POR FP
		PART_FP_indicePreposicao=None, PART_FP_dissocEnteNucleo=None, PART_FP_temQualificador=None, PART_FP_tipoQualificador=None, PART_FP_DETERMINAÇÃO_espeficifidade_beta=None, PART_FP_ORIENTAÇÃO_beta=None, PART_FP_gênero_beta=None, PART_FP_número_beta=None, PART_FP_morfologia_do_pronome_beta=None, PART_FP_DETERMINAÇÃO_espeficifidade_alpha=None, PART_FP_ORIENTAÇÃO_alpha=None, PART_FP_gênero_alpha=None, PART_FP_número_alpha=None, PART_FP_morfologia_do_pronome_alpha=None, PART_FP_pessoa_da_interlocução_possuidor=None, PART_FP_número_obj_possuído=None, PART_FP_gênero_obj_possuído=None, PART_FP_pessoa_da_interlocução_proximidade=None,  PART_FP_funcaoNumerativo=None, PART_FP_cardinal=None, PART_FP_genero=None, PART_FP_tipo_precisa=None, PART_FP_tipoRealCard=None, PART_FP_milharExtenso=None, PART_FP_centenaExtenso=None, PART_FP_dezenaExtenso=None, PART_FP_unidadeExtenso=None, PART_FP_numIndefinido=None, PART_FP_tipo_de_Ente=None, PART_FP_tipo_de_nao_consciente=None, PART_FP_tipo_de_nao_consciente_material=None, PART_FP_tipo_de_nao_consciente_semiotico=None, PART_FP_classe_palavra_Ente=None, PART_FP_substantivo_lematizado=None, PART_FP_numero=None, PART_FP_tipo_feminino_ÃO=None, PART_FP_tipo_masc_ÃO=None, PART_FP_acentTonica=None, PART_FP_nomeProprio=None, PART_FP_pessoa_da_interlocucao=None, PART_FP_transitividade_verbo=None, PART_FP_tonicidade=None, PART_FP_morfologia_do_pronome=None, PART_FP_reflexivo=None, PART_FP_EpitetoModificacao=None, PART_FP_adjetivo_epiteto=None, PART_FP_classificadorModificacao=None, PART_FP_adjetivo_classificador=None, PART_FP_generoAdjetivo=None, PART_FP_numeroAdjetivo=None, PART_FP_contracao=None

):
	Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen,
					   indiceRel,indiceAtrib)
	Modo = MODO(RESPONSABILIDADE,PRESSUPOSICAO_DO_SUJEITO,TIPO_MODO)

	Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL,ORIENTACAO_TRANSITIVA,SELECAO_TEMATICA, TEMA_DEFAULT, TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL, TEMA_PROEMINENTE)
	Polaridade = POLARIDADE(tipo_polaridade)
	Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
	# ORAÇÃO MENTAL declarativa
	if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		if Transitividade == 'PR_Mental_AG_médio_sem_alcance':
	
			Experienciador = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
			if FENOMENALIZACAO == 'não-fenomenalização_comportamento-passivo':
	
				if (TIPO_DE_MENTAL == 'superior_cognitivo' or
						TIPO_DE_MENTAL == 'superior_desiderativo' or
						# Ex.: Tenho pensado; Eu pensei a noite toda;
						TIPO_DE_MENTAL == 'inferior_emotivo' or
						TIPO_DE_MENTAL == 'inferior_perceptivo'):
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + '.'
						# 'Eu ouvi perfeitamente' 
				
		elif Transitividade == 'PR_Mental_AG_médio_com_alcance':
			Experienciador = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
			if FENOMENALIZACAO == 'não-fenomenalização_assunto':
				if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo' or
						TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
					Assunto = frase_preposicional(PART_FP_indicePreposicao, PART_FP_dissocEnteNucleo, PART_FP_temQualificador, PART_FP_tipoQualificador, PART_FP_DETERMINAÇÃO_espeficifidade_beta, PART_FP_ORIENTAÇÃO_beta, PART_FP_gênero_beta, PART_FP_número_beta, PART_FP_morfologia_do_pronome_beta, PART_FP_DETERMINAÇÃO_espeficifidade_alpha, PART_FP_ORIENTAÇÃO_alpha, PART_FP_gênero_alpha, PART_FP_número_alpha, PART_FP_morfologia_do_pronome_alpha, PART_FP_pessoa_da_interlocução_possuidor, PART_FP_número_obj_possuído, PART_FP_gênero_obj_possuído, PART_FP_pessoa_da_interlocução_proximidade, PART_FP_funcaoNumerativo, PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa, PART_FP_tipoRealCard, PART_FP_milharExtenso, PART_FP_centenaExtenso, PART_FP_dezenaExtenso, PART_FP_unidadeExtenso, PART_FP_numIndefinido, PART_FP_tipo_de_Ente, PART_FP_tipo_de_nao_consciente, PART_FP_tipo_de_nao_consciente_material, PART_FP_tipo_de_nao_consciente_semiotico, PART_FP_classe_palavra_Ente, PART_FP_substantivo_lematizado, PART_FP_numero, PART_FP_tipo_feminino_ÃO, PART_FP_tipo_masc_ÃO, PART_FP_acentTonica, PART_FP_nomeProprio, PART_FP_pessoa_da_interlocucao, PART_FP_transitividade_verbo, PART_FP_tonicidade, PART_FP_morfologia_do_pronome, PART_FP_reflexivo, PART_FP_EpitetoModificacao, PART_FP_adjetivo_epiteto, PART_FP_classificadorModificacao, PART_FP_adjetivo_classificador, PART_FP_generoAdjetivo, PART_FP_numeroAdjetivo, PART_FP_contracao
												 )
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto  + '.'
			# Ex.: Eu sei de futebol.
	
	
		# 'Médio com alcance = mental emanente.'
		# TIPO_FENOMENALIZACAO= choice.Menu(['hiperfenômeno', 'fenômeno_simples']
		# print('Qual tipo_pessoa de Processo superior?')
		# TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
			elif FENOMENALIZACAO == 'fenomenalização_fenômeno-simples':
				if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo'):
	
					Fenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
	
					oração =  Experienciador + ' ' + Polaridade   + ' ' + Processo + ' ' + Fenomeno + '.'
				# Ex.: Eu imaginei o jogo
				elif (TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
					# APESAR DE PARECER REDUNDANTE, EM UMA PRÓXIMA FASE, CADA UMA DESTAS ITERAÇÕES
					# VAI TER OS LEXEMAS REPRESENTATIVOS DE CADA TIPO DE PROCESSO MENTAL
					# print('Qual tipo_pessoa de Processo inferior?')
					# TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
					# print('Selecione verbo lematizado cognitivo ou desiderativo:')
	
					Fenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
	
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenomeno +  '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_criativo_pensamento':
				if TIPO_DE_MENTAL == 'superior_cognitivo':
					# 'pensar', 'saber', 'sonhar'
					Pensamento = oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento + '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_criativo_desejo':
				if TIPO_DE_MENTAL == 'superior_desiderativo':
					# print('Qual tipo_pessoa de hiperfenômeno?')
					# print('Projeção = hiperfenômeno: criativo')
				# TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar'])
					Desejo = oracaooProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Desejo + '.'
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					Metafenomeno = oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '.'
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_que':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					Metafenomeno = 'que' + ' ' + oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '.'
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					# print('Selecione o GN com oração qualificadora:')
					Metafenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
	
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '.'
	
			elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
				FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-orientado_gerúndio'):
				if TIPO_DE_MENTAL == 'inferior_perceptivo':
					Macrofenomeno = oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que' :
				if TIPO_DE_MENTAL == 'inferior_perceptivo':
					Macrofenomeno = 'que' + ' ' + oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == 'inferior_perceptivo':
					Macrofenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '.'
	
		elif Transitividade == 'PR_Mental_AG_efetivo_operativo':
			  #impingente
			ExperienciadorGN = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
			ExperienciadorFP = frase_preposicional(PART_FP_indicePreposicao, PART_FP_dissocEnteNucleo, PART_FP_temQualificador, PART_FP_tipoQualificador, PART_FP_DETERMINAÇÃO_espeficifidade_beta, PART_FP_ORIENTAÇÃO_beta, PART_FP_gênero_beta, PART_FP_número_beta, PART_FP_morfologia_do_pronome_beta, PART_FP_DETERMINAÇÃO_espeficifidade_alpha, PART_FP_ORIENTAÇÃO_alpha, PART_FP_gênero_alpha, PART_FP_número_alpha, PART_FP_morfologia_do_pronome_alpha, PART_FP_pessoa_da_interlocução_possuidor, PART_FP_número_obj_possuído, PART_FP_gênero_obj_possuído, PART_FP_pessoa_da_interlocução_proximidade, PART_FP_funcaoNumerativo, PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa, PART_FP_tipoRealCard, PART_FP_milharExtenso, PART_FP_centenaExtenso, PART_FP_dezenaExtenso, PART_FP_unidadeExtenso, PART_FP_numIndefinido, PART_FP_tipo_de_Ente, PART_FP_tipo_de_nao_consciente, PART_FP_tipo_de_nao_consciente_material, PART_FP_tipo_de_nao_consciente_semiotico, PART_FP_classe_palavra_Ente, PART_FP_substantivo_lematizado, PART_FP_numero, PART_FP_tipo_feminino_ÃO, PART_FP_tipo_masc_ÃO, PART_FP_acentTonica, PART_FP_nomeProprio, PART_FP_pessoa_da_interlocucao, PART_FP_transitividade_verbo, PART_FP_tonicidade, PART_FP_morfologia_do_pronome, PART_FP_reflexivo, PART_FP_EpitetoModificacao, PART_FP_adjetivo_epiteto, PART_FP_classificadorModificacao, PART_FP_adjetivo_classificador, PART_FP_generoAdjetivo, PART_FP_numeroAdjetivo, PART_FP_contracao)
			if FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					MetafenomenoAgente = oracaoProjetada()
					oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_que':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					MetafenomenoAgente = 'que' + ' ' + oracaoProjetada()
					oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					# print('Selecione o GN com oração qualificadora:')
					MetafenomenoAgente = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
					oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
	
			elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
				FENOMENALIZACAO == 'reativo_macrofenômeno_não-orientado_gerúndio'):
				if TIPO_DE_MENTAL == "superior_cognitivo":
					MacrofenomenoAgente = oracaoProjetada()
					oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que' :
				if TIPO_DE_MENTAL == "superior_cognitivo":
					MacrofenomenoAgente = 'que' + ' ' + oracaoProjetada()
					oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
	
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == "superior_cognitivo":
					MacrofenomenoAgente = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
					oração = MacrofenomenoAgente + ' ' +Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
	
			elif FENOMENALIZACAO == "fenomenalização_fenômeno_simples":
				if TIPO_DE_MENTAL == "superior_cognitivo" :
	
					# print('Selecione verbo lematizado cognitivo ou desiderativo:')
					FenomenoAgente = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
					oração = FenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN+ ' ' + ExperienciadorFP+ ' '+ '.'
		
	#comeca interrogativa polar
	if  Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		if Transitividade == 'PR_Mental_AG_médio_sem_alcance':

			Experienciador = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
			if FENOMENALIZACAO == 'não-fenomenalização_comportamento-passivo':

				if (TIPO_DE_MENTAL == 'superior_cognitivo' or
						TIPO_DE_MENTAL == 'superior_desiderativo' or
						# Ex.: Tenho pensado; Eu pensei a noite toda;
						TIPO_DE_MENTAL == 'inferior_emotivo' or
						TIPO_DE_MENTAL == 'inferior_perceptivo'):
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + '?'
			# 'Eu ouvi perfeitamente'

		elif Transitividade == 'PR_Mental_AG_médio_com_alcance':
			Experienciador = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
			if FENOMENALIZACAO == 'não-fenomenalização_assunto':
				if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo' or
						TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
					Assunto = frase_preposicional(PART_FP_indicePreposicao, PART_FP_dissocEnteNucleo, PART_FP_temQualificador, PART_FP_tipoQualificador, PART_FP_DETERMINAÇÃO_espeficifidade_beta, PART_FP_ORIENTAÇÃO_beta, PART_FP_gênero_beta, PART_FP_número_beta, PART_FP_morfologia_do_pronome_beta, PART_FP_DETERMINAÇÃO_espeficifidade_alpha, PART_FP_ORIENTAÇÃO_alpha, PART_FP_gênero_alpha, PART_FP_número_alpha, PART_FP_morfologia_do_pronome_alpha, PART_FP_pessoa_da_interlocução_possuidor, PART_FP_número_obj_possuído, PART_FP_gênero_obj_possuído, PART_FP_pessoa_da_interlocução_proximidade, PART_FP_funcaoNumerativo, PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa, PART_FP_tipoRealCard, PART_FP_milharExtenso, PART_FP_centenaExtenso, PART_FP_dezenaExtenso, PART_FP_unidadeExtenso, PART_FP_numIndefinido, PART_FP_tipo_de_Ente, PART_FP_tipo_de_nao_consciente, PART_FP_tipo_de_nao_consciente_material, PART_FP_tipo_de_nao_consciente_semiotico, PART_FP_classe_palavra_Ente, PART_FP_substantivo_lematizado, PART_FP_numero, PART_FP_tipo_feminino_ÃO, PART_FP_tipo_masc_ÃO, PART_FP_acentTonica, PART_FP_nomeProprio, PART_FP_pessoa_da_interlocucao, PART_FP_transitividade_verbo, PART_FP_tonicidade, PART_FP_morfologia_do_pronome, PART_FP_reflexivo, PART_FP_EpitetoModificacao, PART_FP_adjetivo_epiteto, PART_FP_classificadorModificacao, PART_FP_adjetivo_classificador, PART_FP_generoAdjetivo, PART_FP_numeroAdjetivo, PART_FP_contracao)
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '?'
			# Ex.: Eu sei de futebol.

			# 'Médio com alcance = mental emanente.'
			# TIPO_FENOMENALIZACAO= choice.Menu(['hiperfenômeno', 'fenômeno_simples']
			# print('Qual tipo_pessoa de Processo superior?')
			# TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
			elif FENOMENALIZACAO == 'fenomenalização_fenômeno-simples':
				if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo'):

					Fenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenomeno + '?'
				# Ex.: Eu imaginei o jogo
				elif (TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
					# APESAR DE PARECER REDUNDANTE, EM UMA PRÓXIMA FASE, CADA UMA DESTAS ITERAÇÕES
					# VAI TER OS LEXEMAS REPRESENTATIVOS DE CADA TIPO DE PROCESSO MENTAL
					# print('Qual tipo_pessoa de Processo inferior?')
					# TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
					# print('Selecione verbo lematizado cognitivo ou desiderativo:')

					Fenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenomeno + '?'

			elif FENOMENALIZACAO == 'hiperfenômeno_criativo_pensamento':
				if TIPO_DE_MENTAL == 'superior_cognitivo':
					# 'pensar', 'saber', 'sonhar'
					Pensamento = oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento + '?'

			elif FENOMENALIZACAO == 'hiperfenômeno_criativo_desejo':
				if TIPO_DE_MENTAL == 'superior_desiderativo':
					# print('Qual tipo_pessoa de hiperfenômeno?')
					# print('Projeção = hiperfenômeno: criativo')
					# TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar'])
					Desejo = oracaooProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Desejo + '?'
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					Metafenomeno = oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '?'
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_que':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					Metafenomeno = 'que' + ' ' + oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '?'
			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					# print('Selecione o GN com oração qualificadora:')
					Metafenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '?'

			elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
				  FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-orientado_gerúndio'):
				if TIPO_DE_MENTAL == 'inferior_perceptivo':
					Macrofenomeno = oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '?'

			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
				if TIPO_DE_MENTAL == 'inferior_perceptivo':
					Macrofenomeno = 'que' + ' ' + oracaoProjetada()
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '?'

			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == 'inferior_perceptivo':
					Macrofenomeno = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
					oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '?'

		elif Transitividade == 'PR_Mental_AG_efetivo_operativo':
			# impingente
			ExperienciadorGN = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
			ExperienciadorFP = frase_preposicional(PART_FP_indicePreposicao, PART_FP_dissocEnteNucleo, PART_FP_temQualificador, PART_FP_tipoQualificador, PART_FP_DETERMINAÇÃO_espeficifidade_beta, PART_FP_ORIENTAÇÃO_beta, PART_FP_gênero_beta, PART_FP_número_beta, PART_FP_morfologia_do_pronome_beta, PART_FP_DETERMINAÇÃO_espeficifidade_alpha, PART_FP_ORIENTAÇÃO_alpha, PART_FP_gênero_alpha, PART_FP_número_alpha, PART_FP_morfologia_do_pronome_alpha, PART_FP_pessoa_da_interlocução_possuidor, PART_FP_número_obj_possuído, PART_FP_gênero_obj_possuído, PART_FP_pessoa_da_interlocução_proximidade, PART_FP_funcaoNumerativo, PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa, PART_FP_tipoRealCard, PART_FP_milharExtenso, PART_FP_centenaExtenso, PART_FP_dezenaExtenso, PART_FP_unidadeExtenso, PART_FP_numIndefinido, PART_FP_tipo_de_Ente, PART_FP_tipo_de_nao_consciente, PART_FP_tipo_de_nao_consciente_material, PART_FP_tipo_de_nao_consciente_semiotico, PART_FP_classe_palavra_Ente, PART_FP_substantivo_lematizado, PART_FP_numero, PART_FP_tipo_feminino_ÃO, PART_FP_tipo_masc_ÃO, PART_FP_acentTonica, PART_FP_nomeProprio, PART_FP_pessoa_da_interlocucao, PART_FP_transitividade_verbo, PART_FP_tonicidade, PART_FP_morfologia_do_pronome, PART_FP_reflexivo, PART_FP_EpitetoModificacao, PART_FP_adjetivo_epiteto, PART_FP_classificadorModificacao, PART_FP_adjetivo_classificador, PART_FP_generoAdjetivo, PART_FP_numeroAdjetivo, PART_FP_contracao)
			if FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					MetafenomenoAgente = oracaoProjetada()
					oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_que':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					MetafenomenoAgente = 'que' + ' ' + oracaoProjetada()
					oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == 'inferior_emotivo':
					# print('Selecione o GN com oração qualificadora:')
					MetafenomenoAgente = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
					oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

			elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
				  FENOMENALIZACAO == 'reativo_macrofenômeno_não-orientado_gerúndio'):
				if TIPO_DE_MENTAL == "superior_cognitivo":
					MacrofenomenoAgente = oracaoProjetada()
					oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
				if TIPO_DE_MENTAL == "superior_cognitivo":
					MacrofenomenoAgente = 'que' + ' ' + oracaoProjetada()
					oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

			elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
				if TIPO_DE_MENTAL == "superior_cognitivo":
					MacrofenomenoAgente = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)
					oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

			elif FENOMENALIZACAO == "fenomenalização_fenômeno_simples":
				if TIPO_DE_MENTAL == "superior_cognitivo":
					# print('Selecione verbo lematizado cognitivo ou desiderativo:')
					FenomenoAgente = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
					oração = FenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP +'?'

	return (re.sub(' +', ' ', oração).strip().capitalize())

##revisar e testar mental: TENHO QUE TESTAR DEPOIS QUE CONSEGUIR INSERIR ORACAO PROJETADA
# ORACAO MATERIAL
# print('Há Participante Iniciador na oração?')
# INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 	print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()
# print('há Resultado_elaboração atributo ou papel?')
# 			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# realizacao_atributo = choice.Menu(['atributo_adjetivo', 'atributo_frase_preposicional']).ask()
# print('Há Participante Beneficiario na oração?')
# 			RECEPCAO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# print('Qual é o Escopo?')
# tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()


def oracaoMaterial(
##TRANSITIVIDADE
	TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None, indiceAtrib=None,
	# MODO
	RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
	# TEMA IDEACIONAL
	ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None, TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE=None,
	##Parâmetors específicos do Processo Mental
		# FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
##Parâmetors específicos do processo material
	#iniciador
	INICIADOR=None,
	

	RESULTADO_QUALITATIVO=None,realizacao_atributo=None,
		#realizado por adjetivo
	AtributoAdjModificacao=None,AtributoAdjetivo_lematizado=None,AtributoGenero=None,AtributoNumero=None,
		#realizado por frase preposicional
	ATRIB_indicePreposicao=None, ATRIB_dissocEnteNucleo=None, ATRIB_temQualificador=None, ATRIB_tipoQualificador=None, ATRIB_DETERMINAÇÃO_espeficifidade_beta=None, ATRIB_ORIENTAÇÃO_beta=None, ATRIB_gênero_beta=None, ATRIB_número_beta=None, ATRIB_morfologia_do_pronome_beta=None, ATRIB_DETERMINAÇÃO_espeficifidade_alpha=None, ATRIB_ORIENTAÇÃO_alpha=None, ATRIB_gênero_alpha=None, ATRIB_número_alpha=None, ATRIB_morfologia_do_pronome_alpha=None, ATRIB_pessoa_da_interlocução_possuidor=None, ATRIB_número_obj_possuído=None, ATRIB_gênero_obj_possuído=None, ATRIB_pessoa_da_interlocução_proximidade=None,  ATRIB_funcaoNumerativo=None, ATRIB_cardinal=None, ATRIB_genero=None, ATRIB_tipo_precisa=None, ATRIB_tipoRealCard=None, ATRIB_milharExtenso=None, ATRIB_centenaExtenso=None, ATRIB_dezenaExtenso=None, ATRIB_unidadeExtenso=None, ATRIB_numIndefinido=None, ATRIB_tipo_de_Ente=None, ATRIB_tipo_de_nao_consciente=None, ATRIB_tipo_de_nao_consciente_material=None, ATRIB_tipo_de_nao_consciente_semiotico=None, ATRIB_classe_palavra_Ente=None, ATRIB_substantivo_lematizado=None, ATRIB_numero=None, ATRIB_tipo_feminino_ÃO=None, ATRIB_tipo_masc_ÃO=None, ATRIB_acentTonica=None, ATRIB_nomeProprio=None, ATRIB_pessoa_da_interlocucao=None, ATRIB_transitividade_verbo=None, ATRIB_tonicidade=None, ATRIB_morfologia_do_pronome=None, ATRIB_reflexivo=None, ATRIB_EpitetoModificacao=None, ATRIB_adjetivo_epiteto=None, ATRIB_classificadorModificacao=None, ATRIB_adjetivo_classificador=None, ATRIB_generoAdjetivo=None, ATRIB_numeroAdjetivo=None, ATRIB_contracao=None,
		#ESCOPO
	ESCOPO=None,
		#locativo
	LOCATIVO=None,
##extensão beneficiarios
	BENEFICIARIO=None,

		##Processo
	TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None, verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None, padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None, padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None, tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None, padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None, tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None, padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None, verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX='Morfologia_padrão',
		# POLARIDADE
	tipo_polaridade=None,
		##PARTICIPANTES
		# P1
	P1_dissocEnteNucleo=None, P1_temQualificador=None, P1_tipoQualificador=None, P1_indicePreposicao=None, P1_DETERMINAÇÃO_espeficifidade_beta=None, P1_ORIENTAÇÃO_beta=None, P1_gênero_beta=None, P1_número_beta=None, P1_morfologia_do_pronome_beta=None, P1_DETERMINAÇÃO_espeficifidade_alpha=None, P1_ORIENTAÇÃO_alpha=None, P1_gênero_alpha=None, P1_número_alpha=None, P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocução_possuidor=None, P1_número_obj_possuído=None, P1_gênero_obj_possuído=None, P1_pessoa_da_interlocução_proximidade=None, P1_funcaoNumerativo=None, P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipoRealCard=None, P1_milharExtenso=None, P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None, P1_tipo_de_Ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None, P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_Ente=None, P1_substantivo_lematizado=None, P1_numero=None, P1_tipo_feminino_ÃO=None, P1_tipo_masc_ÃO=None, P1_acentTonica=None, P1_nomeProprio=None, P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None, P1_reflexivo=None, P1_epitetoModificacao=None, P1_adjetivo_epiteto=None, P1_classificadorModificacao=None, P1_adjetivo_classificador=None, P1_generoAdjetivo=None, P1_numeroAdjetivo=None, P1_contracao=None,
##PARTICIPANTE P1 REALIZADOS POR FP
	P1_FP_indicePreposicao=None, P1_FP_dissocEnteNucleo=None, P1_FP_temQualificador=None, P1_FP_tipoQualificador=None, P1_FP_DETERMINAÇÃO_espeficifidade_beta=None, P1_FP_ORIENTAÇÃO_beta=None, P1_FP_gênero_beta=None, P1_FP_número_beta=None, P1_FP_morfologia_do_pronome_beta=None, P1_FP_DETERMINAÇÃO_espeficifidade_alpha=None, P1_FP_ORIENTAÇÃO_alpha=None, P1_FP_gênero_alpha=None, P1_FP_número_alpha=None, P1_FP_morfologia_do_pronome_alpha=None, P1_FP_pessoa_da_interlocução_possuidor=None, P1_FP_número_obj_possuído=None, P1_FP_gênero_obj_possuído=None, P1_FP_pessoa_da_interlocução_proximidade=None,  P1_FP_funcaoNumerativo=None, P1_FP_cardinal=None, P1_FP_genero=None, P1_FP_tipo_precisa=None, P1_FP_tipoRealCard=None, P1_FP_milharExtenso=None, P1_FP_centenaExtenso=None, P1_FP_dezenaExtenso=None, P1_FP_unidadeExtenso=None, P1_FP_numIndefinido=None, P1_FP_tipo_de_Ente=None, P1_FP_tipo_de_nao_consciente=None, P1_FP_tipo_de_nao_consciente_material=None, P1_FP_tipo_de_nao_consciente_semiotico=None, P1_FP_classe_palavra_Ente=None, P1_FP_substantivo_lematizado=None, P1_FP_numero=None, P1_FP_tipo_feminino_ÃO=None, P1_FP_tipo_masc_ÃO=None, P1_FP_acentTonica=None, P1_FP_nomeProprio=None, P1_FP_pessoa_da_interlocucao=None, P1_FP_transitividade_verbo=None, P1_FP_tonicidade=None, P1_FP_morfologia_do_pronome=None, P1_FP_reflexivo=None, P1_FP_EpitetoModificacao=None, P1_FP_adjetivo_epiteto=None, P1_FP_classificadorModificacao=None, P1_FP_adjetivo_classificador=None, P1_FP_generoAdjetivo=None, P1_FP_numeroAdjetivo=None, P1_FP_contracao=None,

		# P2
	P2_dissocEnteNucleo=None, P2_temQualificador=None, P2_tipoQualificador=None, P2_indicePreposicao=None, P2_DETERMINAÇÃO_espeficifidade_beta=None, P2_ORIENTAÇÃO_beta=None, P2_gênero_beta=None, P2_número_beta=None, P2_morfologia_do_pronome_beta=None, P2_DETERMINAÇÃO_espeficifidade_alpha=None, P2_ORIENTAÇÃO_alpha=None, P2_gênero_alpha=None, P2_número_alpha=None, P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocução_possuidor=None, P2_número_obj_possuído=None, P2_gênero_obj_possuído=None, P2_pessoa_da_interlocução_proximidade=None, P2_funcaoNumerativo=None, P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipoRealCard=None, P2_milharExtenso=None, P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None, P2_tipo_de_Ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None, P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_Ente=None, P2_substantivo_lematizado=None, P2_numero=None, P2_tipo_feminino_ÃO=None, P2_tipo_masc_ÃO=None, P2_acentTonica=None, P2_nomeProprio=None, P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None, P2_reflexivo=None, P2_epitetoModificacao=None, P2_adjetivo_epiteto=None, P2_classificadorModificacao=None, P2_adjetivo_classificador=None, P2_generoAdjetivo=None, P2_numeroAdjetivo=None, P2_contracao=None,
	# P3
	P3_dissocEnteNucleo=None, P3_temQualificador=None, P3_tipoQualificador=None, P3_indicePreposicao=None, P3_DETERMINAÇÃO_espeficifidade_beta=None, P3_ORIENTAÇÃO_beta=None, P3_gênero_beta=None, P3_número_beta=None, P3_morfologia_do_pronome_beta=None, P3_DETERMINAÇÃO_espeficifidade_alpha=None, P3_ORIENTAÇÃO_alpha=None, P3_gênero_alpha=None, P3_número_alpha=None, P3_morfologia_do_pronome_alpha=None, P3_pessoa_da_interlocução_possuidor=None, P3_número_obj_possuído=None, P3_gênero_obj_possuído=None, P3_pessoa_da_interlocução_proximidade=None, P3_funcaoNumerativo=None, P3_cardinal=None, P3_genero=None, P3_tipo_precisa=None, P3_tipoRealCard=None, P3_milharExtenso=None, P3_centenaExtenso=None, P3_dezenaExtenso=None, P3_unidadeExtenso=None, P3_numIndefinido=None, P3_tipo_de_Ente=None, P3_tipo_de_nao_consciente=None, P3_tipo_de_nao_consciente_material=None, P3_tipo_de_nao_consciente_semiotico=None, P3_classe_palavra_Ente=None, P3_substantivo_lematizado=None, P3_numero=None, P3_tipo_feminino_ÃO=None, P3_tipo_masc_ÃO=None, P3_acentTonica=None, P3_nomeProprio=None, P3_pessoa_da_interlocucao=None, P3_transitividade_verbo=None, P3_tonicidade=None, P3_morfologia_do_pronome=None, P3_reflexivo=None, P3_epitetoModificacao=None, P3_adjetivo_epiteto=None, P3_classificadorModificacao=None, P3_adjetivo_classificador=None, P3_generoAdjetivo=None, P3_numeroAdjetivo=None, P3_contracao=None,

	##PARTICIPANTE P3 REALIZADOS POR FP
	P3_FP_indicePreposicao=None, P3_FP_dissocEnteNucleo=None, P3_FP_temQualificador=None, P3_FP_tipoQualificador=None, P3_FP_DETERMINAÇÃO_espeficifidade_beta=None, P3_FP_ORIENTAÇÃO_beta=None, P3_FP_gênero_beta=None, P3_FP_número_beta=None, P3_FP_morfologia_do_pronome_beta=None, P3_FP_DETERMINAÇÃO_espeficifidade_alpha=None, P3_FP_ORIENTAÇÃO_alpha=None, P3_FP_gênero_alpha=None, P3_FP_número_alpha=None, P3_FP_morfologia_do_pronome_alpha=None, P3_FP_pessoa_da_interlocução_possuidor=None, P3_FP_número_obj_possuído=None, P3_FP_gênero_obj_possuído=None, P3_FP_pessoa_da_interlocução_proximidade=None,  P3_FP_funcaoNumerativo=None, P3_FP_cardinal=None, P3_FP_genero=None, P3_FP_tipo_precisa=None, P3_FP_tipoRealCard=None, P3_FP_milharExtenso=None, P3_FP_centenaExtenso=None, P3_FP_dezenaExtenso=None, P3_FP_unidadeExtenso=None, P3_FP_numIndefinido=None, P3_FP_tipo_de_Ente=None, P3_FP_tipo_de_nao_consciente=None, P3_FP_tipo_de_nao_consciente_material=None, P3_FP_tipo_de_nao_consciente_semiotico=None, P3_FP_classe_palavra_Ente=None, P3_FP_substantivo_lematizado=None, P3_FP_numero=None, P3_FP_tipo_feminino_ÃO=None, P3_FP_tipo_masc_ÃO=None, P3_FP_acentTonica=None, P3_FP_nomeProprio=None, P3_FP_pessoa_da_interlocucao=None, P3_FP_transitividade_verbo=None, P3_FP_tonicidade=None, P3_FP_morfologia_do_pronome=None, P3_FP_reflexivo=None, P3_FP_EpitetoModificacao=None, P3_FP_adjetivo_epiteto=None, P3_FP_classificadorModificacao=None, P3_FP_adjetivo_classificador=None, P3_FP_generoAdjetivo=None, P3_FP_numeroAdjetivo=None, P3_FP_contracao=None


):
	Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel, indiceAtrib)
	Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
	Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT, TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL, TEMA_PROEMINENTE)
	Polaridade = POLARIDADE(tipo_polaridade)
	Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	if Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_efetivo_operativo':
		#NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDENS DE AGENTES
		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)

		INICIADOR ='+iniciador'
		Iniciador = estrutura_GN(P3_dissocEnteNucleo, P3_temQualificador, P3_tipoQualificador, P3_indicePreposicao, P3_DETERMINAÇÃO_espeficifidade_beta, P3_ORIENTAÇÃO_beta, P3_gênero_beta, P3_número_beta, P3_morfologia_do_pronome_beta, P3_DETERMINAÇÃO_espeficifidade_alpha, P3_ORIENTAÇÃO_alpha, P3_gênero_alpha, P3_número_alpha, P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocução_possuidor, P3_número_obj_possuído, P3_gênero_obj_possuído, P3_pessoa_da_interlocução_proximidade, P3_funcaoNumerativo, P3_cardinal, P3_genero, P3_tipo_precisa, P3_tipoRealCard, P3_milharExtenso, P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso, P3_numIndefinido, P3_tipo_de_Ente, P3_tipo_de_nao_consciente, P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico, P3_classe_palavra_Ente, P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ÃO, P3_tipo_masc_ÃO, P3_acentTonica, P3_nomeProprio, P3_pessoa_da_interlocucao, P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo, P3_epitetoModificacao, P3_adjetivo_epiteto, P3_classificadorModificacao, P3_adjetivo_classificador, P3_generoAdjetivo, P3_numeroAdjetivo, P3_contracao)

		try:
			if BENEFICIARIO == '+cliente':
				Cliente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade,  P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-cliente':
				Cliente = ''
		except:
			Cliente = ''
		try:
			if LOCATIVO == '+locativo':
				Locativo = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif LOCATIVO == '-locativo':
				Locativo = ''
		except:
			Locativo = ''
		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
			oração = Iniciador + ' ' + Polaridade + ' ' + Processo + ' ' + Ator + ' ' + Locativo + ' ' + Cliente + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
			oração = Iniciador + ' ' + Polaridade + ' ' + Processo + ' ' + Ator + ' ' + Locativo + ' ' + Cliente + '?'


	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance':
		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
		INICIADOR == '-iniciador'
		Iniciador = ''
		oração = Ator + ' ' + Polaridade + ' ' + Processo
		try:
			if BENEFICIARIO == '+cliente':
				Cliente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade,  P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-cliente':
				Cliente = ''
		except:
			Cliente = ''
		try:
			if LOCATIVO == '+locativo':
				Locativo = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif LOCATIVO == '-locativo':
				Locativo = ''
		except:
			Locativo = ''
		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = oração + ' ' + Locativo + ' ' + Cliente + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = oração + ' ' + Locativo + ' ' + Cliente + '?'

	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance':
		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)

		try:
			if ESCOPO == '+escopo':
				Escopo = estrutura_GN(P3_dissocEnteNucleo, P3_temQualificador, P3_tipoQualificador, P3_indicePreposicao, P3_DETERMINAÇÃO_espeficifidade_beta, P3_ORIENTAÇÃO_beta, P3_gênero_beta, P3_número_beta, P3_morfologia_do_pronome_beta, P3_DETERMINAÇÃO_espeficifidade_alpha, P3_ORIENTAÇÃO_alpha, P3_gênero_alpha, P3_número_alpha, P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocução_possuidor, P3_número_obj_possuído, P3_gênero_obj_possuído, P3_pessoa_da_interlocução_proximidade, P3_funcaoNumerativo, P3_cardinal, P3_genero, P3_tipo_precisa, P3_tipoRealCard, P3_milharExtenso, P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso, P3_numIndefinido, P3_tipo_de_Ente, P3_tipo_de_nao_consciente, P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico, P3_classe_palavra_Ente, P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ÃO, P3_tipo_masc_ÃO, P3_acentTonica, P3_nomeProprio, P3_pessoa_da_interlocucao, P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo, P3_epitetoModificacao, P3_adjetivo_epiteto, P3_classificadorModificacao, P3_adjetivo_classificador, P3_generoAdjetivo, P3_numeroAdjetivo, P3_contracao)
			elif ESCOPO =='-escopo':
				Escopo = ''
		except:
			Escopo = ''

		try:
			if LOCATIVO == '+locativo':
				Locativo = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif LOCATIVO == '-locativo':
				Locativo = ''
		except:
			Locativo = ''

		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Escopo + ' ' + Locativo + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Escopo + ' ' + Locativo + '?'

	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' :

		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo + '?'

	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' :
		# NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDENS DE AGENTES
		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
		Meta = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

		try:
			if RESULTADO_QUALITATIVO == 'resultado_atributo' or RESULTADO_QUALITATIVO == 'resultado_papel(produto)':
				if realizacao_atributo == 'atributo_adjetivo':
					Atributo = adjetivo(AtributoAdjModificacao,AtributoAdjetivo_lematizado,AtributoGenero,AtributoNumero)
				elif realizacao_atributo == 'atributo_frase_preposicional':
					Atributo = frase_preposicional(ATRIB_indicePreposicao, ATRIB_dissocEnteNucleo, ATRIB_temQualificador, ATRIB_tipoQualificador, ATRIB_DETERMINAÇÃO_espeficifidade_beta, ATRIB_ORIENTAÇÃO_beta, ATRIB_gênero_beta, ATRIB_número_beta, ATRIB_morfologia_do_pronome_beta, ATRIB_DETERMINAÇÃO_espeficifidade_alpha, ATRIB_ORIENTAÇÃO_alpha, ATRIB_gênero_alpha, ATRIB_número_alpha, ATRIB_morfologia_do_pronome_alpha, ATRIB_pessoa_da_interlocução_possuidor, ATRIB_número_obj_possuído, ATRIB_gênero_obj_possuído, ATRIB_pessoa_da_interlocução_proximidade, ATRIB_funcaoNumerativo, ATRIB_cardinal, ATRIB_genero, ATRIB_tipo_precisa, ATRIB_tipoRealCard, ATRIB_milharExtenso, ATRIB_centenaExtenso, ATRIB_dezenaExtenso, ATRIB_unidadeExtenso, ATRIB_numIndefinido, ATRIB_tipo_de_Ente, ATRIB_tipo_de_nao_consciente, ATRIB_tipo_de_nao_consciente_material, ATRIB_tipo_de_nao_consciente_semiotico, ATRIB_classe_palavra_Ente, ATRIB_substantivo_lematizado, ATRIB_numero, ATRIB_tipo_feminino_ÃO, ATRIB_tipo_masc_ÃO, ATRIB_acentTonica, ATRIB_nomeProprio, ATRIB_pessoa_da_interlocucao, ATRIB_transitividade_verbo, ATRIB_tonicidade, ATRIB_morfologia_do_pronome, ATRIB_reflexivo, ATRIB_EpitetoModificacao, ATRIB_adjetivo_epiteto, ATRIB_classificadorModificacao, ATRIB_adjetivo_classificador, ATRIB_generoAdjetivo, ATRIB_numeroAdjetivo, ATRIB_contracao)
			elif RESULTADO_QUALITATIVO == '-resultado':
					Atributo = ''
		except:
			Atributo = ''

		try:
			if BENEFICIARIO == '+recipiente':
				Recipiente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-recipiente':
				Recipiente = ''
		except:
			Recipiente = ''
		try:
			if LOCATIVO == '+locativo':
				Locativo = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif LOCATIVO == '-locativo':
				Locativo = ''
		except:
			Locativo = ''
		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo  + ' ' + Meta + ' ' + Atributo + ' ' + Locativo + ' ' + Recipiente+ '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo  + ' ' + Meta + ' ' + Atributo + ' ' + Locativo + ' ' + Recipiente+ '?'

	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo':

		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)
		Meta = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

		try:
			if BENEFICIARIO == '+cliente':
				Cliente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade,  P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-cliente':
				Cliente = ''
		except:
			Cliente = ''
		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta + ' ' + Cliente +'.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta + ' ' + Cliente +'?'

	##MATERIAL METEOROLÓGICA
	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_processo_com_alcance':
		Escopo = estrutura_GN(P3_dissocEnteNucleo, P3_temQualificador, P3_tipoQualificador, P3_indicePreposicao, P3_DETERMINAÇÃO_espeficifidade_beta, P3_ORIENTAÇÃO_beta, P3_gênero_beta, P3_número_beta, P3_morfologia_do_pronome_beta, P3_DETERMINAÇÃO_espeficifidade_alpha, P3_ORIENTAÇÃO_alpha, P3_gênero_alpha, P3_número_alpha, P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocução_possuidor, P3_número_obj_possuído, P3_gênero_obj_possuído, P3_pessoa_da_interlocução_proximidade, P3_funcaoNumerativo, P3_cardinal, P3_genero, P3_tipo_precisa, P3_tipoRealCard, P3_milharExtenso, P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso, P3_numIndefinido, P3_tipo_de_Ente, P3_tipo_de_nao_consciente, P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico, P3_classe_palavra_Ente, P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ÃO, P3_tipo_masc_ÃO, P3_acentTonica, P3_nomeProprio, P3_pessoa_da_interlocucao, P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo, P3_epitetoModificacao, P3_adjetivo_epiteto, P3_classificadorModificacao, P3_adjetivo_classificador, P3_generoAdjetivo, P3_numeroAdjetivo, P3_contracao)
		if Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração =  Processo + ' ' + Escopo + '.'
		elif Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração =  Processo + ' ' + Escopo + '?'

	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_processo_sem_alcance':
		if Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = Processo+'.'
		elif Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito'	and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = Processo + '?'

# 		##########COMEÇO DE AGENCIAMENTO PASSIVA
#
	#
	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' :
		
		Ator = frase_preposicional(P1_FP_indicePreposicao, P1_FP_dissocEnteNucleo, P1_FP_temQualificador, P1_FP_tipoQualificador, P1_FP_DETERMINAÇÃO_espeficifidade_beta, P1_FP_ORIENTAÇÃO_beta, P1_FP_gênero_beta, P1_FP_número_beta, P1_FP_morfologia_do_pronome_beta, P1_FP_DETERMINAÇÃO_espeficifidade_alpha, P1_FP_ORIENTAÇÃO_alpha, P1_FP_gênero_alpha, P1_FP_número_alpha, P1_FP_morfologia_do_pronome_alpha, P1_FP_pessoa_da_interlocução_possuidor, P1_FP_número_obj_possuído, P1_FP_gênero_obj_possuído, P1_FP_pessoa_da_interlocução_proximidade,  P1_FP_funcaoNumerativo, P1_FP_cardinal, P1_FP_genero, P1_FP_tipo_precisa, P1_FP_tipoRealCard, P1_FP_milharExtenso, P1_FP_centenaExtenso, P1_FP_dezenaExtenso, P1_FP_unidadeExtenso, P1_FP_numIndefinido, P1_FP_tipo_de_Ente, P1_FP_tipo_de_nao_consciente, P1_FP_tipo_de_nao_consciente_material, P1_FP_tipo_de_nao_consciente_semiotico, P1_FP_classe_palavra_Ente, P1_FP_substantivo_lematizado, P1_FP_numero, P1_FP_tipo_feminino_ÃO, P1_FP_tipo_masc_ÃO, P1_FP_acentTonica, P1_FP_nomeProprio, P1_FP_pessoa_da_interlocucao, P1_FP_transitividade_verbo, P1_FP_tonicidade, P1_FP_morfologia_do_pronome, P1_FP_reflexivo, P1_FP_EpitetoModificacao, P1_FP_adjetivo_epiteto, P1_FP_classificadorModificacao, P1_FP_adjetivo_classificador, P1_FP_generoAdjetivo, P1_FP_numeroAdjetivo, P1_FP_contracao)
		Meta = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

		try:
			if RESULTADO_QUALITATIVO == 'resultado_atributo' or RESULTADO_QUALITATIVO == 'resultado_papel(produto)':
				if realizacao_atributo == 'atributo_adjetivo':
					Atributo = adjetivo(AtributoAdjModificacao, AtributoAdjetivo_lematizado, AtributoGenero,
										AtributoNumero)
				elif realizacao_atributo == 'atributo_frase_preposicional':
					Atributo = frase_preposicional(ATRIB_indicePreposicao, ATRIB_dissocEnteNucleo, ATRIB_temQualificador, ATRIB_tipoQualificador, ATRIB_DETERMINAÇÃO_espeficifidade_beta, ATRIB_ORIENTAÇÃO_beta, ATRIB_gênero_beta, ATRIB_número_beta, ATRIB_morfologia_do_pronome_beta, ATRIB_DETERMINAÇÃO_espeficifidade_alpha, ATRIB_ORIENTAÇÃO_alpha, ATRIB_gênero_alpha, ATRIB_número_alpha, ATRIB_morfologia_do_pronome_alpha, ATRIB_pessoa_da_interlocução_possuidor, ATRIB_número_obj_possuído, ATRIB_gênero_obj_possuído, ATRIB_pessoa_da_interlocução_proximidade, ATRIB_funcaoNumerativo, ATRIB_cardinal, ATRIB_genero, ATRIB_tipo_precisa, ATRIB_tipoRealCard, ATRIB_milharExtenso, ATRIB_centenaExtenso, ATRIB_dezenaExtenso, ATRIB_unidadeExtenso, ATRIB_numIndefinido, ATRIB_tipo_de_Ente, ATRIB_tipo_de_nao_consciente, ATRIB_tipo_de_nao_consciente_material, ATRIB_tipo_de_nao_consciente_semiotico, ATRIB_classe_palavra_Ente, ATRIB_substantivo_lematizado, ATRIB_numero, ATRIB_tipo_feminino_ÃO, ATRIB_tipo_masc_ÃO, ATRIB_acentTonica, ATRIB_nomeProprio, ATRIB_pessoa_da_interlocucao, ATRIB_transitividade_verbo, ATRIB_tonicidade, ATRIB_morfologia_do_pronome, ATRIB_reflexivo, ATRIB_EpitetoModificacao, ATRIB_adjetivo_epiteto, ATRIB_classificadorModificacao, ATRIB_adjetivo_classificador, ATRIB_generoAdjetivo, ATRIB_numeroAdjetivo, ATRIB_contracao)
			elif RESULTADO_QUALITATIVO == '-resultado':
				Atributo = ''
		except:
			Atributo = ''

		try:
			if BENEFICIARIO == '+recipiente':
				Recipiente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-recipiente':
				Recipiente = ''
			else:
				Recipiente = ''
		except:
			Recipiente = ''
		try:
			if LOCATIVO == '+locativo':
				Locativo = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif LOCATIVO == '-locativo':
				Locativo = ''
		except:
			Locativo = ''

		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
			oração = Meta + ' ' + Polaridade + ' ' + Processo  + ' ' + Atributo + ' ' + Ator + ' ' + Locativo + ' ' + Recipiente + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
			oração = Meta + ' ' + Polaridade + ' ' + Processo  + ' ' + Atributo + ' ' + Ator + ' ' + Locativo + ' ' + Recipiente + '?'

	######################################################################
	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' :

		Ator = frase_preposicional(P1_FP_indicePreposicao, P1_FP_dissocEnteNucleo, P1_FP_temQualificador, P1_FP_tipoQualificador, P1_FP_DETERMINAÇÃO_espeficifidade_beta, P1_FP_ORIENTAÇÃO_beta, P1_FP_gênero_beta, P1_FP_número_beta, P1_FP_morfologia_do_pronome_beta, P1_FP_DETERMINAÇÃO_espeficifidade_alpha, P1_FP_ORIENTAÇÃO_alpha, P1_FP_gênero_alpha, P1_FP_número_alpha, P1_FP_morfologia_do_pronome_alpha, P1_FP_pessoa_da_interlocução_possuidor, P1_FP_número_obj_possuído, P1_FP_gênero_obj_possuído, P1_FP_pessoa_da_interlocução_proximidade, P1_FP_funcaoNumerativo, P1_FP_cardinal, P1_FP_genero, P1_FP_tipo_precisa, P1_FP_tipoRealCard, P1_FP_milharExtenso, P1_FP_centenaExtenso, P1_FP_dezenaExtenso, P1_FP_unidadeExtenso, P1_FP_numIndefinido, P1_FP_tipo_de_Ente, P1_FP_tipo_de_nao_consciente, P1_FP_tipo_de_nao_consciente_material, P1_FP_tipo_de_nao_consciente_semiotico, P1_FP_classe_palavra_Ente, P1_FP_substantivo_lematizado, P1_FP_numero, P1_FP_tipo_feminino_ÃO, P1_FP_tipo_masc_ÃO, P1_FP_acentTonica, P1_FP_nomeProprio, P1_FP_pessoa_da_interlocucao, P1_FP_transitividade_verbo, P1_FP_tonicidade, P1_FP_morfologia_do_pronome, P1_FP_reflexivo, P1_FP_EpitetoModificacao, P1_FP_adjetivo_epiteto, P1_FP_classificadorModificacao, P1_FP_adjetivo_classificador, P1_FP_generoAdjetivo, P1_FP_numeroAdjetivo, P1_FP_contracao)
		Meta = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

		try:
			if BENEFICIARIO == '+cliente':
				Cliente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-cliente':
				Cliente = ''
		except:
			Cliente = ''

		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
			oração = Meta + ' ' + Polaridade + ' ' + Processo + ' ' + Ator + ' ' + Cliente + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
			oração = Meta + ' ' + Polaridade + ' ' + Processo + ' ' + Ator + ' ' + Cliente + '?'

	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_efetivo_receptivo':
		#NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDEM DE AGENTES
		Ator = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)

		INICIADOR ='+iniciador'
		Iniciador = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)

		try:
			if BENEFICIARIO == '+cliente':
				Cliente = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade,  P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif BENEFICIARIO == '-cliente':
				Cliente = ''
		except:
			Cliente = ''
		try:
			if LOCATIVO == '+locativo':
				Locativo = frase_preposicional(P3_FP_indicePreposicao, P3_FP_dissocEnteNucleo, P3_FP_temQualificador, P3_FP_tipoQualificador, P3_FP_DETERMINAÇÃO_espeficifidade_beta, P3_FP_ORIENTAÇÃO_beta, P3_FP_gênero_beta, P3_FP_número_beta, P3_FP_morfologia_do_pronome_beta, P3_FP_DETERMINAÇÃO_espeficifidade_alpha, P3_FP_ORIENTAÇÃO_alpha, P3_FP_gênero_alpha, P3_FP_número_alpha, P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocução_possuidor, P3_FP_número_obj_possuído, P3_FP_gênero_obj_possuído, P3_FP_pessoa_da_interlocução_proximidade, P3_FP_funcaoNumerativo, P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipoRealCard, P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_Ente, P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material, P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_Ente, P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ÃO, P3_FP_tipo_masc_ÃO, P3_FP_acentTonica, P3_FP_nomeProprio, P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_EpitetoModificacao, P3_FP_adjetivo_epiteto, P3_FP_classificadorModificacao, P3_FP_adjetivo_classificador, P3_FP_generoAdjetivo, P3_FP_numeroAdjetivo, P3_FP_contracao)
			elif LOCATIVO == '-locativo':
				Locativo = ''
		except:
			Locativo = ''
		if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo  + ' ' + Locativo +' '+ Iniciador + ' ' + Cliente + '.'
		elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
			oração = Ator + ' ' + Polaridade + ' ' + Processo  + ' ' + Locativo +' '+ Iniciador + ' ' + Cliente + '?'

	return (re.sub(' +', ' ', oração).strip().capitalize())




##ORACAO RELACIONAL

print('Qual o tipo_pessoa de especificação de associação?')
especificacao_associacao = choice.Menu(['entidade', 'qualidade']).ask()
print('Qual a fase da atribuição?')
fase_atribuicao = choice.Menu(['neutra',
							   'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
###não vou especializar os tipos de fase.
print('Qual o domínio da atribuição')
dominio_atribuicao = choice.Menu(['material', 'semiótico']).ask()



def oracaoRelacional(
		##TRANSITIVIDADE
		TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None, indiceAtrib=None,
		# MODO
		RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
		# TEMA IDEACIONAL
		ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None, TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE=None,
		##Parâmetors específicos do Processo Mental
		# FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,

		# ##Parâmetors específicos do processo material
		# # iniciador
		# INICIADOR=None,
		#
		# RESULTADO_QUALITATIVO=None, realizacao_atributo=None,
		# # realizado por adjetivo
		# AtributoAdjModificacao=None, AtributoAdjetivo_lematizado=None, AtributoGenero=None, AtributoNumero=None,
		# # realizado por frase preposicional
		# ATRIB_indicePreposicao=None, ATRIB_dissocEnteNucleo=None, ATRIB_temQualificador=None, ATRIB_tipoQualificador=None, ATRIB_DETERMINAÇÃO_espeficifidade_beta=None, ATRIB_ORIENTAÇÃO_beta=None, ATRIB_gênero_beta=None, ATRIB_número_beta=None, ATRIB_morfologia_do_pronome_beta=None, ATRIB_DETERMINAÇÃO_espeficifidade_alpha=None, ATRIB_ORIENTAÇÃO_alpha=None, ATRIB_gênero_alpha=None, ATRIB_número_alpha=None, ATRIB_morfologia_do_pronome_alpha=None, ATRIB_pessoa_da_interlocução_possuidor=None, ATRIB_número_obj_possuído=None, ATRIB_gênero_obj_possuído=None, ATRIB_pessoa_da_interlocução_proximidade=None, ATRIB_funcaoNumerativo=None, ATRIB_cardinal=None, ATRIB_genero=None, ATRIB_tipo_precisa=None, ATRIB_tipoRealCard=None, ATRIB_milharExtenso=None, ATRIB_centenaExtenso=None, ATRIB_dezenaExtenso=None, ATRIB_unidadeExtenso=None, ATRIB_numIndefinido=None, ATRIB_tipo_de_Ente=None, ATRIB_tipo_de_nao_consciente=None, ATRIB_tipo_de_nao_consciente_material=None, ATRIB_tipo_de_nao_consciente_semiotico=None, ATRIB_classe_palavra_Ente=None, ATRIB_substantivo_lematizado=None, ATRIB_numero=None, ATRIB_tipo_feminino_ÃO=None, ATRIB_tipo_masc_ÃO=None, ATRIB_acentTonica=None, ATRIB_nomeProprio=None, ATRIB_pessoa_da_interlocucao=None, ATRIB_transitividade_verbo=None, ATRIB_tonicidade=None, ATRIB_morfologia_do_pronome=None, ATRIB_reflexivo=None, ATRIB_EpitetoModificacao=None, ATRIB_adjetivo_epiteto=None, ATRIB_classificadorModificacao=None, ATRIB_adjetivo_classificador=None, ATRIB_generoAdjetivo=None, ATRIB_numeroAdjetivo=None, ATRIB_contracao=None,
		# # ESCOPO
		# ESCOPO=None,
		# # locativo
		# LOCATIVO=None,
		# ##extensão beneficiarios
		# BENEFICIARIO=None,

		# PARÂMETROS ESPEĆIFICOS DA RELACIONAL
		#ATRIBUTIVAS
		especificacao_associacao=None,fase_atribuicao=None,dominio_atribuicao=None,

		##Processo
		TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None, verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None, padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None, padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None, tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None, padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None, tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None, padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None, verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX='Morfologia_padrão',
		# POLARIDADE
		tipo_polaridade=None,
		##PARTICIPANTES
		# P1
		P1_dissocEnteNucleo=None, P1_temQualificador=None, P1_tipoQualificador=None, P1_indicePreposicao=None, P1_DETERMINAÇÃO_espeficifidade_beta=None, P1_ORIENTAÇÃO_beta=None, P1_gênero_beta=None, P1_número_beta=None, P1_morfologia_do_pronome_beta=None, P1_DETERMINAÇÃO_espeficifidade_alpha=None, P1_ORIENTAÇÃO_alpha=None, P1_gênero_alpha=None, P1_número_alpha=None, P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocução_possuidor=None, P1_número_obj_possuído=None, P1_gênero_obj_possuído=None, P1_pessoa_da_interlocução_proximidade=None, P1_funcaoNumerativo=None, P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipoRealCard=None, P1_milharExtenso=None, P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None, P1_tipo_de_Ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None, P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_Ente=None, P1_substantivo_lematizado=None, P1_numero=None, P1_tipo_feminino_ÃO=None, P1_tipo_masc_ÃO=None, P1_acentTonica=None, P1_nomeProprio=None, P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None, P1_reflexivo=None, P1_epitetoModificacao=None, P1_adjetivo_epiteto=None, P1_classificadorModificacao=None, P1_adjetivo_classificador=None, P1_generoAdjetivo=None, P1_numeroAdjetivo=None, P1_contracao=None,
		##PARTICIPANTE P1 REALIZADOS POR FP
		P1_FP_indicePreposicao=None, P1_FP_dissocEnteNucleo=None, P1_FP_temQualificador=None, P1_FP_tipoQualificador=None, P1_FP_DETERMINAÇÃO_espeficifidade_beta=None, P1_FP_ORIENTAÇÃO_beta=None, P1_FP_gênero_beta=None, P1_FP_número_beta=None, P1_FP_morfologia_do_pronome_beta=None, P1_FP_DETERMINAÇÃO_espeficifidade_alpha=None, P1_FP_ORIENTAÇÃO_alpha=None, P1_FP_gênero_alpha=None, P1_FP_número_alpha=None, P1_FP_morfologia_do_pronome_alpha=None, P1_FP_pessoa_da_interlocução_possuidor=None, P1_FP_número_obj_possuído=None, P1_FP_gênero_obj_possuído=None, P1_FP_pessoa_da_interlocução_proximidade=None, P1_FP_funcaoNumerativo=None, P1_FP_cardinal=None, P1_FP_genero=None, P1_FP_tipo_precisa=None, P1_FP_tipoRealCard=None, P1_FP_milharExtenso=None, P1_FP_centenaExtenso=None, P1_FP_dezenaExtenso=None, P1_FP_unidadeExtenso=None, P1_FP_numIndefinido=None, P1_FP_tipo_de_Ente=None, P1_FP_tipo_de_nao_consciente=None, P1_FP_tipo_de_nao_consciente_material=None, P1_FP_tipo_de_nao_consciente_semiotico=None, P1_FP_classe_palavra_Ente=None, P1_FP_substantivo_lematizado=None, P1_FP_numero=None, P1_FP_tipo_feminino_ÃO=None, P1_FP_tipo_masc_ÃO=None, P1_FP_acentTonica=None, P1_FP_nomeProprio=None, P1_FP_pessoa_da_interlocucao=None, P1_FP_transitividade_verbo=None, P1_FP_tonicidade=None, P1_FP_morfologia_do_pronome=None, P1_FP_reflexivo=None, P1_FP_EpitetoModificacao=None, P1_FP_adjetivo_epiteto=None, P1_FP_classificadorModificacao=None, P1_FP_adjetivo_classificador=None, P1_FP_generoAdjetivo=None, P1_FP_numeroAdjetivo=None, P1_FP_contracao=None,

		# P2
		P2_dissocEnteNucleo=None, P2_temQualificador=None, P2_tipoQualificador=None, P2_indicePreposicao=None, P2_DETERMINAÇÃO_espeficifidade_beta=None, P2_ORIENTAÇÃO_beta=None, P2_gênero_beta=None, P2_número_beta=None, P2_morfologia_do_pronome_beta=None, P2_DETERMINAÇÃO_espeficifidade_alpha=None, P2_ORIENTAÇÃO_alpha=None, P2_gênero_alpha=None, P2_número_alpha=None, P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocução_possuidor=None, P2_número_obj_possuído=None, P2_gênero_obj_possuído=None, P2_pessoa_da_interlocução_proximidade=None, P2_funcaoNumerativo=None, P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipoRealCard=None, P2_milharExtenso=None, P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None, P2_tipo_de_Ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None, P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_Ente=None, P2_substantivo_lematizado=None, P2_numero=None, P2_tipo_feminino_ÃO=None, P2_tipo_masc_ÃO=None, P2_acentTonica=None, P2_nomeProprio=None, P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None, P2_reflexivo=None, P2_epitetoModificacao=None, P2_adjetivo_epiteto=None, P2_classificadorModificacao=None, P2_adjetivo_classificador=None, P2_generoAdjetivo=None, P2_numeroAdjetivo=None, P2_contracao=None,
		# P3
		P3_dissocEnteNucleo=None, P3_temQualificador=None, P3_tipoQualificador=None, P3_indicePreposicao=None, P3_DETERMINAÇÃO_espeficifidade_beta=None, P3_ORIENTAÇÃO_beta=None, P3_gênero_beta=None, P3_número_beta=None, P3_morfologia_do_pronome_beta=None, P3_DETERMINAÇÃO_espeficifidade_alpha=None, P3_ORIENTAÇÃO_alpha=None, P3_gênero_alpha=None, P3_número_alpha=None, P3_morfologia_do_pronome_alpha=None, P3_pessoa_da_interlocução_possuidor=None, P3_número_obj_possuído=None, P3_gênero_obj_possuído=None, P3_pessoa_da_interlocução_proximidade=None, P3_funcaoNumerativo=None, P3_cardinal=None, P3_genero=None, P3_tipo_precisa=None, P3_tipoRealCard=None, P3_milharExtenso=None, P3_centenaExtenso=None, P3_dezenaExtenso=None, P3_unidadeExtenso=None, P3_numIndefinido=None, P3_tipo_de_Ente=None, P3_tipo_de_nao_consciente=None, P3_tipo_de_nao_consciente_material=None, P3_tipo_de_nao_consciente_semiotico=None, P3_classe_palavra_Ente=None, P3_substantivo_lematizado=None, P3_numero=None, P3_tipo_feminino_ÃO=None, P3_tipo_masc_ÃO=None, P3_acentTonica=None, P3_nomeProprio=None, P3_pessoa_da_interlocucao=None, P3_transitividade_verbo=None, P3_tonicidade=None, P3_morfologia_do_pronome=None, P3_reflexivo=None, P3_epitetoModificacao=None, P3_adjetivo_epiteto=None, P3_classificadorModificacao=None, P3_adjetivo_classificador=None, P3_generoAdjetivo=None, P3_numeroAdjetivo=None, P3_contracao=None,

		##PARTICIPANTE P3 REALIZADOS POR FP
		P3_FP_indicePreposicao=None, P3_FP_dissocEnteNucleo=None, P3_FP_temQualificador=None, P3_FP_tipoQualificador=None, P3_FP_DETERMINAÇÃO_espeficifidade_beta=None, P3_FP_ORIENTAÇÃO_beta=None, P3_FP_gênero_beta=None, P3_FP_número_beta=None, P3_FP_morfologia_do_pronome_beta=None, P3_FP_DETERMINAÇÃO_espeficifidade_alpha=None, P3_FP_ORIENTAÇÃO_alpha=None, P3_FP_gênero_alpha=None, P3_FP_número_alpha=None, P3_FP_morfologia_do_pronome_alpha=None, P3_FP_pessoa_da_interlocução_possuidor=None, P3_FP_número_obj_possuído=None, P3_FP_gênero_obj_possuído=None, P3_FP_pessoa_da_interlocução_proximidade=None, P3_FP_funcaoNumerativo=None, P3_FP_cardinal=None, P3_FP_genero=None, P3_FP_tipo_precisa=None, P3_FP_tipoRealCard=None, P3_FP_milharExtenso=None, P3_FP_centenaExtenso=None, P3_FP_dezenaExtenso=None, P3_FP_unidadeExtenso=None, P3_FP_numIndefinido=None, P3_FP_tipo_de_Ente=None, P3_FP_tipo_de_nao_consciente=None, P3_FP_tipo_de_nao_consciente_material=None, P3_FP_tipo_de_nao_consciente_semiotico=None, P3_FP_classe_palavra_Ente=None, P3_FP_substantivo_lematizado=None, P3_FP_numero=None, P3_FP_tipo_feminino_ÃO=None, P3_FP_tipo_masc_ÃO=None, P3_FP_acentTonica=None, P3_FP_nomeProprio=None, P3_FP_pessoa_da_interlocucao=None, P3_FP_transitividade_verbo=None, P3_FP_tonicidade=None, P3_FP_morfologia_do_pronome=None, P3_FP_reflexivo=None, P3_FP_EpitetoModificacao=None, P3_FP_adjetivo_epiteto=None, P3_FP_classificadorModificacao=None, P3_FP_adjetivo_classificador=None, P3_FP_generoAdjetivo=None, P3_FP_numeroAdjetivo=None, P3_FP_contracao=None

):
	Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel, indiceAtrib)
	Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
	Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT, TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL, TEMA_PROEMINENTE)
	Polaridade = POLARIDADE(tipo_polaridade)
	Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)


# 	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
	if Transitividade == 'PR_relacional_intensivo_atributivo_sem_atribuição_de_relação_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
		## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
		Portador = estrutura_GN(P1_dissocEnteNucleo, P1_temQualificador, P1_tipoQualificador, P1_indicePreposicao, P1_DETERMINAÇÃO_espeficifidade_beta, P1_ORIENTAÇÃO_beta, P1_gênero_beta, P1_número_beta, P1_morfologia_do_pronome_beta, P1_DETERMINAÇÃO_espeficifidade_alpha, P1_ORIENTAÇÃO_alpha, P1_gênero_alpha, P1_número_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocução_possuidor, P1_número_obj_possuído, P1_gênero_obj_possuído, P1_pessoa_da_interlocução_proximidade, P1_funcaoNumerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipoRealCard, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_Ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_Ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ÃO, P1_tipo_masc_ÃO, P1_acentTonica, P1_nomeProprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_epitetoModificacao, P1_adjetivo_epiteto, P1_classificadorModificacao, P1_adjetivo_classificador, P1_generoAdjetivo, P1_numeroAdjetivo, P1_contracao)

		#POR ENQUANTO PARECE DESNECESSÁRIO DEIXAR TODAS AS POSSÍVILIDADES COMO ESTÃO AQUI, MAS NA HORA DE DESENVOLVER MAIS VAI SER NECESSÁRIO
		if (
				especificacao_associacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material' or
				especificacao_associacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico' or
				especificacao_associacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material' or
				especificacao_associacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico'
		):

			Atributo = estrutura_GN(P2_dissocEnteNucleo, P2_temQualificador, P2_tipoQualificador, P2_indicePreposicao, P2_DETERMINAÇÃO_espeficifidade_beta, P2_ORIENTAÇÃO_beta, P2_gênero_beta, P2_número_beta, P2_morfologia_do_pronome_beta, P2_DETERMINAÇÃO_espeficifidade_alpha, P2_ORIENTAÇÃO_alpha, P2_gênero_alpha, P2_número_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocução_possuidor, P2_número_obj_possuído, P2_gênero_obj_possuído, P2_pessoa_da_interlocução_proximidade, P2_funcaoNumerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipoRealCard, P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_Ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_Ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ÃO, P2_tipo_masc_ÃO, P2_acentTonica, P2_nomeProprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_epitetoModificacao, P2_adjetivo_epiteto, P2_classificadorModificacao, P2_adjetivo_classificador, P2_generoAdjetivo, P2_numeroAdjetivo, P2_contracao)

		oração = Portador + ' ' + Polaridade + ' ' + Processo  + ' ' + Atributo + '.'
	return (re.sub(' +', ' ', oração).strip().capitalize())
#PAREI AQUI RELACIONAL: CONTINUAR  
# 'O moço é um pedreiro.'
oracaoRelacional(
	# transitividade
	'Relacional',None,
	1, 0, 5,

	# modo
	0, 0, 1,
	# TEMA IDEACIONAL
	'orientado', 'direcional',
	'default', 'indicativo',
	'declarativo', 'NA',
	None, None, None,

##PARÂMETROS DA RELACIONAL
	 'entidade', 'neutra', 'material',
	# Processo
	'Ser', 'não_agenciado', None, None, None, None, None, None,
	None, None, None, None, None, None, None, None, None,
	None, None, None, None, None, None, None, None, None, None, None,
	None, None, None, None, None,
	'Morfologia_padrão', 'Fazer', 'Evento', 'ser', 'presente', 'singular',
	None, '3pessoa', 'Morfologia_padrão',
	# POLARIDADE
	'positiva',
	##PARTICIPANTES
	# p1
	None, None, None, None,
	None, None, None, None,
	None, 'específico', 'NA',
	'masculino', 'singular', None,
	None, None, None,
	None, None, None, 'não-binário',
	None, None, None, None,
	None, None, None,
	'consciente', None, None,
	None, 'substantivo_comum', 'moço',
	'singular', None, None, None, None,
	None, None, None, "Morfologia_padrão",
	None, None, None, None,
	None, None, None, None,
# p1 realizado por fp
	None, None, None, None,
	None, None,
	None, None, None,
	None, None,
	None,
	None, None,
	None,
	None, None,
	None,  #
	None, None, None, None, None,
	None, None, None, None, None,
	None, None,
	None,
	None, None,
	None, None,
	None, None, None, None, None,
	None, None, None, None,  #
	None, None,
	None, None, None,
	None, None,
	# p2 )
	##
	None, None, None, None,
	None, None, None, None,
	None, 'não_específico', 'NA',
	'masculino', 'singular', None,
	None, None, None,
	None, None, None, 'não-binário',
	None, None, None, None,
	None, None, None,
	'não_consciente', 'material',
	'abstração_material',
	None, 'substantivo_comum', 'pedreiro',
	'singular', None, None, None, None,
	None, None, None, "Morfologia_padrão",
	None, None, None, None,
	None, None, None, None,
	# p3
	None, None, None, None,
	None, None,
	None, None, None,
	None, None, None,
	None, None, None,
	None, None, None,
	None, None, None, None, None,
	None, None, None, None,
	None,
	None, None, None,
	None, None,
	None, None,
	None, None, None, None,
	None,
	None, None, None, None,
	None, None, None,
	None, None, None, None,
	# realizados por frase preposicional
	None, None, None, None,
	None, None,
	None, None, None,
	None, None,
	None,
	None, None,
	None,
	None, None,
	None,  #
	None, None, None, None, None,
	None, None, None, None, None,
	None, None,
	None,
	None,None,
	None, None,
	None, None, None, None, None,
	None, None, None, None,  #
	None,None,
	None, None, None,
	None, None)





#
# 		elif (
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material' or
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico' or
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material' or
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico'):
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador?') \
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = adjetivo()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
# 			# o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
# 			##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Atributo + ' ' + Circunstancia + '.'
#
#
# 	###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
# 	##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva
# 	# (há a possibilidade de Agente de segunda, terceira.....ordem)
#
# 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Atribuidor?')
# 			Atribuidor = estrutura_GN()
# 			print('Qual o Portador?')
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
#
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Portador + ' ' + Atributo + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Atribuidor?')
# 			Atribuidor = frase_preposicional()
# 			print('Qual o Portador?')
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
#
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo
# 			+ ' ' + Atributo + ' ' + Atribuidor + ' ' + Circunstancia + '.'
#
#
# 	####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)
#
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação':
# 		print('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito '
# 		      'deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 		if direcionalidade_voz == 'meio_operativa':
# 			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente'
# 			      'o elemento em posição temática)')
# 			# (confluência do Símbolo/Identificado) =
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstancia + '.'
#
# 		elif direcionalidade_voz == 'meio_receptiva':
# 			print('Neste caso, o Valor/Identificador conflui com o Sujeito')
# 			##NESTE CASO, confluência de Valor/Sujeito
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL() \
#  \
# 					print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Símbolo + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação':
#
# 		print(
# 			'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 		if direcionalidade_voz == 'meio_operativa':
# 			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
#
# 			# (confluência do Símbolo/Identificador/Sujeito) =
# 			# (Valor/Identificado/complemento)
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Valor + ' ' + Circunstancia + '.'
#
# 		elif direcionalidade_voz == 'meio_receptiva':
# 			print('Neste caso, o Valor conflui com o Sujeito')
# 			##NESTE CASO, confluência de Valor/Identificado/Sujeito
# 			##(Símbolo/Identificador/Complemento)
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Símbolo + ' ' + Circunstancia + '.'
#
# 	####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)
#
# 	#    ###TRUE_Efetiva_operativa
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas) \
# 		# POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Designador?')
# 			Designador = estrutura_GN()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()  ##ou frase preposicional?
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + ' ' + Circunstancia + '.'
# 			###rever possíveis estruturas para este tipo_pessoa de oração(pode haver 2 processos?)
#
# 	###TRUE_Efetiva_receptiva
#
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Designador?')
# 			Designador = frase_preposicional()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()  ##ou frase preposicional?
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
# 			#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Valor + ' ' + Designador + ' ' + Circunstancia + '.'
# 	####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realizacao de cada participante;
# 	#        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)
#
# 	# POSSESSIVO ATRIBUTIV0
#
# 	if Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()
#
# 		if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':
#
# 			realizacao_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()
#
# 			if realizacao_atributo == 'grupo_nominal_possessivo':
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Posse?')
# 				Portador_Posse = estrutura_GN()
# 				print('Qual é o Atributo/Possuidor?')
# 				Atributo_Possuidor = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstancia + '.'
#
# 			elif realizacao_atributo == 'frase_preposicional':
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Posse?')
# 				Portador_Posse = estrutura_GN()
# 				print('Qual é o Atributo/Possuidor?')
# 				Atributo_Possuidor = frase_preposicional()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstancia + '.'
#
#
# 		elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':
#
# 			##VERBO TER/POSSUIR/
#
# 			tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask() \
#  \
# 			if tipo_possuidor == 'possuidor_portador':
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Possuidor?')
# 				Portador_Possuidor = estrutura_GN()
# 				print('Qual é o Atributo/Posse?')
# 				Atributo_Posse = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Atributo_Posse + ' ' + Circunstancia + '.'
#
#
# 			###VERBOS PERTENCER A/...
#
# 			elif tipo_possuidor == 'possuidor_atributo':
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Possuidor?')
# 				Portador_Posse = estrutura_GN()
# 				print('Qual é o Atributo/Posse?')
# 				Atributo_Possuidor = frase_preposicional()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstancia + '.'
#
# 		# POSSESSIVO IDENTIFICATIVO
#
#
# 	elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()
#
# 		if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')
#
# 				print(
# 					'Escolha o tipo_pessoa de realizacao do Valor:')
# 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
#
# 				if realizacao_Valor == 'grupo_nominal':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)/Possuído?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)/Possuidor?')
# 					Valor_Possuidor = estrutura_GN()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O piano é seu
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstancia + '.'
#
# 				elif realizacao_Valor == 'frase_preposicional':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)?')
# 					Valor_Possuidor = frase_preposicional()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O piano é do André
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstancia + '.'
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')
#
# 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
#
# 				if realizacao_Valor == 'grupo_nominal':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)/Possuído?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)/Possuidor?')
# 					Valor_Possuidor = estrutura_GN()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O seu é o piano
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstancia + '.'
#
# 				elif realizacao_Valor == 'frase_preposicional':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)?')
# 					Valor_Possuidor = estrutura_GN()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O do André é o piano
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstancia + '.'
#
# 		elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
# 			## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
# 			##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print(
# 					'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)/Possuidor?')
# 				Símbolo_Possuidor = estrutura_GN()
# 				print('Qual o Valor(Value)/Possuído?')
# 				Valor_Possuído = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: O produto contém plástico, Eles merecem a aposentadoria
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Valor_Possuído + ' ' + Circunstancia + '.'
#
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')
#
# 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
#
# 				if realizacao_Valor == 'grupo_nominal':
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()  ##na passiva
# 					print('Qual o Valor(Value)/Possuído?')
# 					Valor_Possuído = estrutura_GN()
# 					print('Qual é o Símbolo(Token)/Possuidor?')
# 					Símbolo_Possuidor = frase_preposicional()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O seu é o piano
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Símbolo_Possuidor + ' ' + Circunstancia + '.'
#
#
# 	#####RELACIONAL CIRCUNSTANCIAL
#
# 	elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		print('Qual o tipo_pessoa de realizacao da Relacional Circunstancial?')
# 		TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()
#
# 		if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador')
# 			Portador = estrutura_GN()
# 			print('Qual é o Atributo Circunstancial?')
# 			Atributo_Circunstancial = circunstância()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			# Ex.: O livro é sobre a IIGuerra
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Atributo_Circunstancial + ' ' + Circunstancia + '.'
#
# 		elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador')
# 			Portador = estrutura_GN()
# 			print('Qual é o Atributo Circunstancial?')
# 			Atributo = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			# Ex.: O livro retrata a IIGuerra
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Atributo + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		print('O significado circunstancial é realixado no participante ou no processo?')
# 		TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
# 			['participante_circunstancial', 'processo_circunstancial']).ask()
#
# 		if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
# 				print('Qual o Valor(Value)?')
# 				Valor = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: Amanhá é dia 10
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo \
# 				         + ' ' + Valor + ' ' + Circunstancia + '.'
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
# 				print('Qual o Valor(Value)?')
# 				Valor = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.:dia 10 é Amanhá
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstancia + '.'
#
#
# 		elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
# 				print('Qual o Valor(Value)?')
# 				Valor = circunstância()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: A feira dura o dia
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstancia + '.'
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()  ## reiterações-verbo na passiva
# 				print('Qual o Valor(Value)?')
# 				Valor = circunstância()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
#
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: O dia inteiro é ocupado pela feira
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstancia + '.'
#




#
# def gerar_oracao(
# 		##TRANSITIVIDADE
# 		TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None,
# 		indiceRel=None, indiceAtrib=None,
# 		# MODO
# 		RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
# 		# TEMA IDEACIONAL
# 		ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None,
# 		TEMA_DEFAULT=None, TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None,
# 		TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE=None,
# 		#TEMA INTERPESSOAL
# 		TIPO_TEMA_INTERPESSOAL=None, tipoRealizacao=None,
# 			# realizado por grupo adverbial
# 		tipo_de_adverbio1=None, ind1=None,
# 		tipo_de_adverbio2=None, ind2=None,
# 		tipo_de_adverbio3=None, ind3=None,
# 		tipo_de_adverbio4=None, ind4=None,
# 		tipo_de_adverbio5=None, ind5=None,
#
# 		# realziado por frase prepos
# 		indicePreposicao=None, dissocEnteNucleo=None, temQualificador=None,
# 		tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 		gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 		DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
# 		número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
# 		número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
# 		funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
# 		milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
# 		numIndefinido=None, tipo_de_Ente=None, tipo_de_nao_consciente=None,
# 		tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
# 		classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
# 		tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
# 		pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
# 		morfologia_do_pronome=None, reflexivo=None, epitetoModificacao=None,
# 		adjetivo_epiteto=None, classificadorModificacao=None,
# 		adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None,
#
# 		#
# 		indiceElemQu=None, indicePartModal=None,
# 		nome_proprio=None,
#
# 	#TEMA TEXTUAL
# 		temTemaTextual='-', tipo_insercao_Cont="inserção_menu",conj_extenso_Cont=None,indiceCont=None,
# 		tipo_insercao_Conj="inserção_menu",tipo_de_conjuncao_Conj=None, conj_extensoConj=None,indiceConj=None,
# 		tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None,tipo_de_relativo=None,
# 		tipo_pronome_relativo=None, generoTemaTextual=None, numeroTemaTextual=None, indiceRelativo=None,
# 		indiceRelativoAdv=None,
#
# 		##Processo Mental
# 		 TIPO_DE_MENTAL=None, FENOMENALIZACAO=None,
#
# 		##Processo
# 		TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None,
# 		funcao_no_grupo_verbal_1=None, verbo_1=None,
# 		tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None,
# 		OI_tipo_de_pessoa_1=None, padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None,
# 		funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None, OI_numero_2=None,
# 		genero_2=None, OI_tipo_de_pessoa_2=None, padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None,
# 		funcao_no_grupo_verbal_3=None, verbo_3=None,
# 		tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None,
# 		padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None,
# 		verbo_4=None, tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None,
# 		OI_tipo_de_pessoa_4=None, padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None,
# 		funcao_no_grupo_verbal_POS_FINAL=None, verbo_LEX=None, tipo_de_orientacao_LEX=None,
# 		OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
# 		padrao_pessoa_morfologia_LEX='Morfologia_padrão',
# 		# POLARIDADE
# 		tipo_polaridade=None,
#
# ##PARTICIPANTES
# 	# P1
# 		P1_dissocEnteNucleo=None, P1_temQualificador=None, P1_tipoQualificador=None, P1_indicePreposicao=None,
# 		P1_DETERMINAÇÃO_espeficifidade_beta=None, P1_ORIENTAÇÃO_beta=None,
# 		P1_gênero_beta=None, P1_número_beta=None, P1_morfologia_do_pronome_beta=None,
# 		P1_DETERMINAÇÃO_espeficifidade_alpha=None, P1_ORIENTAÇÃO_alpha=None, P1_gênero_alpha=None,
# 		P1_número_alpha=None, P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocução_possuidor=None,
# 		P1_número_obj_possuído=None, P1_gênero_obj_possuído=None, P1_pessoa_da_interlocução_proximidade=None,
# 		P1_funcaoNumerativo=None, P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipoRealCard=None,
# 		P1_milharExtenso=None, P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None,
# 		P1_numIndefinido=None,
# 		P1_tipo_de_Ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None,
# 		P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_Ente=None, P1_substantivo_lematizado=None,
# 		P1_numero=None,
# 		P1_tipo_feminino_ÃO=None, P1_tipo_masc_ÃO=None, P1_acentTonica=None, P1_nomeProprio=None,
# 		P1_pessoa_da_interlocucao=None,
# 		P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None, P1_reflexivo=None,
# 		P1_epitetoModificacao=None, P1_adjetivo_epiteto=None, P1_classificadorModificacao=None,
# 		P1_adjetivo_classificador=None,P1_generoAdjetivo=None, P1_numeroAdjetivo=None,P1_contracao=None,
# # P2
# 		P2_dissocEnteNucleo=None, P2_temQualificador=None, P2_tipoQualificador=None, P2_indicePreposicao=None,
# 		P2_DETERMINAÇÃO_espeficifidade_beta=None, P2_ORIENTAÇÃO_beta=None,
# 		P2_gênero_beta=None, P2_número_beta=None, P2_morfologia_do_pronome_beta=None,
# 		P2_DETERMINAÇÃO_espeficifidade_alpha=None, P2_ORIENTAÇÃO_alpha=None, P2_gênero_alpha=None,
# 		P2_número_alpha=None, P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocução_possuidor=None,
# 		P2_número_obj_possuído=None, P2_gênero_obj_possuído=None, P2_pessoa_da_interlocução_proximidade=None,
# 		P2_funcaoNumerativo=None, P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipoRealCard=None,
# 		P2_milharExtenso=None, P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None,
# 		P2_numIndefinido=None,
# 		P2_tipo_de_Ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None,
# 		P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_Ente=None, P2_substantivo_lematizado=None,
# 		P2_numero=None,
# 		P2_tipo_feminino_ÃO=None, P2_tipo_masc_ÃO=None, P2_acentTonica=None, P2_nomeProprio=None,
# 		P2_pessoa_da_interlocucao=None,
# 		P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None, P2_reflexivo=None,
# 		P2_epitetoModificacao=None, P2_adjetivo_epiteto=None, P2_classificadorModificacao=None,
# 		P2_adjetivo_classificador=None,P2_generoAdjetivo=None, P2_numeroAdjetivo=None,P2_contracao=None,
# ##PARTICIPANTES REALIZADOS POR FP
# 		PART_FP_indicePreposicao=None, PART_FP_dissocEnteNucleo=None, PART_FP_temQualificador=None, PART_FP_tipoQualificador=None,
# 		PART_FP_DETERMINAÇÃO_espeficifidade_beta=None, PART_FP_ORIENTAÇÃO_beta=None,
# 		PART_FP_gênero_beta=None, PART_FP_número_beta=None, PART_FP_morfologia_do_pronome_beta=None,
# 		PART_FP_DETERMINAÇÃO_espeficifidade_alpha=None, PART_FP_ORIENTAÇÃO_alpha=None, PART_FP_gênero_alpha=None,
# 		PART_FP_número_alpha=None, PART_FP_morfologia_do_pronome_alpha=None, PART_FP_pessoa_da_interlocução_possuidor=None,
# 		PART_FP_número_obj_possuído=None, PART_FP_gênero_obj_possuído=None, PART_FP_pessoa_da_interlocução_proximidade=None,  #
# 		PART_FP_funcaoNumerativo=None, PART_FP_cardinal=None, PART_FP_genero=None, PART_FP_tipo_precisa=None, PART_FP_tipoRealCard=None,
# 		PART_FP_milharExtenso=None, PART_FP_centenaExtenso=None, PART_FP_dezenaExtenso=None, PART_FP_unidadeExtenso=None,
# 		PART_FP_numIndefinido=None,
# 		PART_FP_tipo_de_Ente=None, PART_FP_tipo_de_nao_consciente=None, PART_FP_tipo_de_nao_consciente_material=None,
# 		PART_FP_tipo_de_nao_consciente_semiotico=None, PART_FP_classe_palavra_Ente=None, PART_FP_substantivo_lematizado=None,
# 		PART_FP_numero=None, PART_FP_tipo_feminino_ÃO=None, PART_FP_tipo_masc_ÃO=None, PART_FP_acentTonica=None, PART_FP_nomeProprio=None,
# 		PART_FP_pessoa_da_interlocucao=None, PART_FP_transitividade_verbo=None, PART_FP_tonicidade=None,
# 		PART_FP_morfologia_do_pronome=None, PART_FP_reflexivo=None,
# 		PART_FP_EpitetoModificacao=None, PART_FP_adjetivo_epiteto=None, PART_FP_classificadorModificacao=None,
# 		PART_FP_adjetivo_classificador=None, PART_FP_generoAdjetivo=None, PART_FP_numeroAdjetivo=None,
# 		PART_FP_contracao=None,
#
# 	##CIRCUNSTANCIA
# 		temCircunstancia=None, realizacaoCircunstancia=None,
# 		CIRC_indicePreposicao=None, CIRC_dissocEnteNucleo=None, CIRC_temQualificador=None, CIRC_tipoQualificador=None,
# 		CIRC_DETERMINAÇÃO_espeficifidade_beta=None, CIRC_ORIENTAÇÃO_beta=None,
# 		CIRC_gênero_beta=None, CIRC_número_beta=None, CIRC_morfologia_do_pronome_beta=None,
# 		CIRC_DETERMINAÇÃO_espeficifidade_alpha=None, CIRC_ORIENTAÇÃO_alpha=None, CIRC_gênero_alpha=None,
# 		CIRC_número_alpha=None, CIRC_morfologia_do_pronome_alpha=None, CIRC_pessoa_da_interlocução_possuidor=None,
# 		CIRC_número_obj_possuído=None, CIRC_gênero_obj_possuído=None, CIRC_pessoa_da_interlocução_proximidade=None,  #
# 		CIRC_funcaoNumerativo=None, CIRC_cardinal=None, CIRC_genero=None, CIRC_tipo_precisa=None, CIRC_tipoRealCard=None,
# 		CIRC_milharExtenso=None, CIRC_centenaExtenso=None, CIRC_dezenaExtenso=None, CIRC_unidadeExtenso=None,
# 		CIRC_numIndefinido=None,
# 		CIRC_tipo_de_Ente=None, CIRC_tipo_de_nao_consciente=None, CIRC_tipo_de_nao_consciente_material=None,
# 		CIRC_tipo_de_nao_consciente_semiotico=None, CIRC_classe_palavra_Ente=None, CIRC_substantivo_lematizado=None,
# 		CIRC_numero=None, CIRC_tipo_feminino_ÃO=None, CIRC_tipo_masc_ÃO=None, CIRC_acentTonica=None, CIRC_nomeProprio=None,
# 		CIRC_pessoa_da_interlocucao=None, CIRC_transitividade_verbo=None, CIRC_tonicidade=None,
# 		CIRC_morfologia_do_pronome=None, CIRC_reflexivo=None,
# 		CIRC_EpitetoModificacao=None, CIRC_adjetivo_epiteto=None, CIRC_classificadorModificacao=None,
# 		CIRC_adjetivo_classificador=None,CIRC_generoAdjetivo=None, CIRC_numeroAdjetivo=None,
# 		CIRC_contracao=None,
# 		CIRC_tipo_de_adverbio1=None, CIRC_ind1=None,
# 				  CIRC_tipo_de_adverbio2=None, CIRC_ind2=None,
# 				  CIRC_tipo_de_adverbio3=None, CIRC_ind3=None,
# 				  CIRC_tipo_de_adverbio4=None, CIRC_ind4=None,
# 				  CIRC_tipo_de_adverbio5=None, CIRC_ind5=None
#
#
# ):
# 	'''(str,str,str)->str
#     Retorna a formação estrutural na lexicogramática
#      (oração) de uma figura específica da semântica
#
#     >>> gerar_oracao()
#     'eu bebi água'
#     '''
# 	Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO,indiceMat,indiceAgen,
# 				   indiceRel,indiceAtrib)
# 	Modo = MODO(RESPONSABILIDADE,PRESSUPOSICAO_DO_SUJEITO,TIPO_MODO)
# 	Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL,ORIENTACAO_TRANSITIVA,SELECAO_TEMATICA,
# 					TEMA_DEFAULT,
# 					TEMA_DEFAULT_indicativo,
# 					TEMA_IDENTIFICATIVO,
# 					TEMA_ANGULO,
# 					TEMA_ELEMENTAL,
# 					TEMA_PROEMINENTE)
# 	Tema_interpessoal = TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL, tipoRealizacao,
# 										  # grupo adverbial
# 										  tipo_de_adverbio1, ind1,
# 										  tipo_de_adverbio2, ind2,
# 										  tipo_de_adverbio3, ind3,
# 										  tipo_de_adverbio4, ind4,
# 										  tipo_de_adverbio5, ind5,
#
# 										  # frase prepos
# 										  indicePreposicao, dissocEnteNucleo, temQualificador,
# 										  tipoQualificador, DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
# 										  gênero_beta, número_beta, morfologia_do_pronome_beta,
# 										  DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
# 										  número_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
# 										  número_obj_possuído, gênero_obj_possuído, pessoa_da_interlocução_proximidade,
# 										  funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
# 										  milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
# 										  numIndefinido, tipo_de_Ente, tipo_de_nao_consciente,
# 										  tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
# 										  classe_palavra_Ente, substantivo_lematizado, numero,
# 										  tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
# 										  pessoa_da_interlocucao, transitividade_verbo, tonicidade,
# 										  morfologia_do_pronome, reflexivo, epitetoModificacao,
# 										  adjetivo_epiteto, classificadorModificacao,
# 										  adjetivo_classificador, generoAdjetivo, numeroAdjetivo, contracao,
# 										  #
# 										  indiceElemQu, indicePartModal,
# 										  nome_proprio)
# 	Tema_textual = TEMA_TEXTUAL(temTemaTextual, tipo_insercao_Cont, conj_extenso_Cont, indiceCont,
# 								tipo_insercao_Conj, tipo_de_conjuncao_Conj, conj_extensoConj, indiceConj,
# 								tipo_insercao_Rel, pron_extenso_Rel, tipo_de_relativo,
# 								tipo_pronome_relativo, generoTemaTextual, numeroTemaTextual, indiceRelativo,
# 								indiceRelativoAdv)
# 	Polaridade = POLARIDADE(tipo_polaridade)
# 	Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1,
# 							funcao_no_grupo_verbal_1, verbo_1,
# 							tipo_de_orientacao_1, OI_numero_1, genero_1,
# 							OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2,
# 							funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, OI_numero_2,
# 							genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2,
# 							TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
# 							tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
# 							padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4,
# 							verbo_4, tipo_de_orientacao_4, OI_numero_4, genero_4,
# 							OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX,
# 							funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX,
# 							OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
# 	Circunstancia = circunstancia(temCircunstancia, realizacaoCircunstancia,
# 								  CIRC_indicePreposicao, CIRC_dissocEnteNucleo, CIRC_temQualificador,
# 								  CIRC_tipoQualificador,
# 								  CIRC_DETERMINAÇÃO_espeficifidade_beta, CIRC_ORIENTAÇÃO_beta,
# 								  CIRC_gênero_beta, CIRC_número_beta, CIRC_morfologia_do_pronome_beta,
# 								  CIRC_DETERMINAÇÃO_espeficifidade_alpha, CIRC_ORIENTAÇÃO_alpha,
# 								  CIRC_gênero_alpha,
# 								  CIRC_número_alpha, CIRC_morfologia_do_pronome_alpha,
# 								  CIRC_pessoa_da_interlocução_possuidor,
# 								  CIRC_número_obj_possuído, CIRC_gênero_obj_possuído,
# 								  CIRC_pessoa_da_interlocução_proximidade,  #
# 								  CIRC_funcaoNumerativo, CIRC_cardinal, CIRC_genero, CIRC_tipo_precisa,
# 								  CIRC_tipoRealCard,
# 								  CIRC_milharExtenso, CIRC_centenaExtenso, CIRC_dezenaExtenso,
# 								  CIRC_unidadeExtenso,
# 								  CIRC_numIndefinido,
# 								  CIRC_tipo_de_Ente, CIRC_tipo_de_nao_consciente,
# 								  CIRC_tipo_de_nao_consciente_material,
# 								  CIRC_tipo_de_nao_consciente_semiotico, CIRC_classe_palavra_Ente,
# 								  CIRC_substantivo_lematizado,
# 								  CIRC_numero, CIRC_tipo_feminino_ÃO, CIRC_tipo_masc_ÃO,
# 								  CIRC_acentTonica, CIRC_nomeProprio,
# 								  CIRC_pessoa_da_interlocucao, CIRC_transitividade_verbo,
# 								  CIRC_tonicidade, CIRC_morfologia_do_pronome, CIRC_reflexivo,
# 								  CIRC_EpitetoModificacao, CIRC_adjetivo_epiteto,
# 								  CIRC_classificadorModificacao,
# 								  CIRC_adjetivo_classificador, CIRC_generoAdjetivo, CIRC_numeroAdjetivo,
# 								  CIRC_contracao,
# 								  CIRC_tipo_de_adverbio1, CIRC_ind1,
# 								  CIRC_tipo_de_adverbio2, CIRC_ind2,
# 								  CIRC_tipo_de_adverbio3, CIRC_ind3,
# 								  CIRC_tipo_de_adverbio4, CIRC_ind4,
# 								  CIRC_tipo_de_adverbio5, CIRC_ind5)
# 	# ORAÇÃO MENTAL
#
#
#
#
# 	##ORAÇÃO verbal
#
# 	elif Transitividade == 'PR_Verbal_AG_médio_sem_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
# 		print('Qual a Ordem do Dizente?')
# 		ORDEM_DO_DIZENTE = choice.Menu(['atividade', 'semioticidade']).ask()
# 		if ORDEM_DO_DIZENTE == 'atividade':
# 			TIPO_ATIVIDADE = 'fala'
#
# 			if TIPO_ATIVIDADE == 'fala':
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Dizente?')
# 				Dizente = estrutura_GN()
# 				print('Há Receptor?')
# 				print('Selecione a Receptividade') \
# 				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# 				if RECEPTIVIDADE == '+receptor':
# 					Receptor = frase_preposicional()
# 				else:
# 					Receptor = ''
# 				Polaridade = POLARIDADE() \
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# 				         + ' ' + Receptor + ' ' + Circunstancia + '.'
# 				# Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...
#
#
# 		elif ORDEM_DO_DIZENTE == 'semioticidade':
# 			print('Semioticidade em Médio sem alcance = não_projeção')
# 			TIPO_SEMIOTICIDADE = choice.Menu(['não_projeção']).ask()
#
# 			if TIPO_SEMIOTICIDADE == 'não_projeção':
# 				print('Não-projeção + médio sem alcance = -verbiagem')
# 				TIPO_NÃO_PROJEÇÃO = '-verbiagem'
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Dizente?')
# 				Dizente = estrutura_GN()
# 				print('Há Receptor?')
# 				print('Selecione a Receptividade')
# 				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# 				if RECEPTIVIDADE == '+receptor':
# 					Receptor = frase_preposicional()
# 				else:
# 					Receptor = ''
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_Verbal_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
# 		print('Qual a Ordem do Dizente?')
# 		ORDEM_DO_DIZENTE = choice.Menu(['semioticidade']).ask()
# 		print('Selecione a Receptividade')
# 		RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
#
# 		if ORDEM_DO_DIZENTE == 'semioticidade':
# 			print('Selecione o tipo_pessoa de Semioticidade')
#
# 			TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
# 			if TIPO_SEMIOTICIDADE == 'projeção':
# 				print('Selecione o tipo_pessoa de projeção')
# 				TIPO_PROJEÇÃO = choice.Menu(['citativa', 'relativa']).ask()
# 				if TIPO_PROJEÇÃO == 'citativa':
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Dizente?')
# 					Dizente = estrutura_GN()
# 					print('Há Receptor?')
# 					print('Selecione a Receptividade')
# 					RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# 					if RECEPTIVIDADE == '+receptor':
# 						Receptor = frase_preposicional()
# 					else:
# 						Receptor = ''
# 					Polaridade = POLARIDADE()
# 					print('Qual a oração projetada?')
# 					Circunstância = circunstância()
# 					Oração_projetada = oraçãoProjetada()
#
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# 					         + ' ' + Receptor + '"' + Oração_projetada + '" ' + ' ' + Circunstancia + '.'
# 					# Ex.: Eu disse a ele "Eu comi o bolo".
#
# 				elif TIPO_PROJEÇÃO == 'relativa':
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Dizente?')
# 					Dizente = estrutura_GN()
# 					print('Há Receptor?')
# 					print('Selecione a Receptividade')
# 					RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# 					if RECEPTIVIDADE == '+receptor':
# 						Receptor = frase_preposicional()
# 					else:
# 						Receptor = ''
# 					Polaridade = POLARIDADE()
# 					print('Qual a oração projetada?')
# 					Oração_projetada = oraçãoProjetada()
# 					Circunstância = circunstância()
#
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# 					         + ' ' + Receptor + ' ' + 'que' + ' ' + '"' + Oração_projetada + '" ' + ' ' + Circunstancia + '.'
# 					# Ex.: Eu disse a ele que "Eu comi o bolo".
#
# 			elif TIPO_SEMIOTICIDADE == 'não_projeção':
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Dizente?')
# 				Dizente = estrutura_GN()
# 				print('Qual é a Verbiagem?')
# 				Verbiagem = estrutura_GN()
# 				print('Há Receptor?')
# 				print('Selecione a Receptividade')
# 				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# 				if RECEPTIVIDADE == '+receptor':
# 					Receptor = frase_preposicional()
# 				else:
# 					Receptor = ''
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# 				         + ' ' + Verbiagem + ' ' + Receptor + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_Verbal_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		Polaridade = POLARIDADE()
# 		print('Qual é o Dizente?')
# 		Dizente = estrutura_GN()
# 		Circunstância = circunstância()
#
# 		print('O Alvo é realizado por grupo nominal ou frase preposicional?')
# 		realizacao_alvo = choice.Menu(['GN', 'FP']).ask()
# 		if realizacao_alvo == 'GN':
# 			print('Qual é o Alvo?')
# 			Alvo = estrutura_GN()
# 			print('Qual a localização do alvo na oração (em relação ao Processo)?')
# 			localização_alvo = choice.Menu(['ante_processo', 'pós_processo']).ask()
# 			if localização_alvo == 'ante_processo':
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' \
# 				         + Alvo + ' ' + Processo + ' ' + Circunstancia + '.'
# 			else:
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Alvo + ' ' + Circunstancia + '.' \
# 		else:
# 			print('Qual é o Alvo?')
# 			Alvo = frase_preposicional()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Alvo + ' ' + Circunstancia + '.'
#
#
# 	elif Transitividade == 'PR_Verbal_AG_efetivo_receptivo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		Polaridade = POLARIDADE()
# 		print('Qual é o Dizente?')
# 		Dizente = frase_preposicional()
# 		print('Qual é o Alvo?')
# 		Alvo = estrutura_GN()
# 		Circunstância = circunstância()
#
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Alvo + ' ' + Polaridade + ' ' + Processo \
# 		         + ' ' + Dizente + ' ' + Circunstancia + '.'
#
# 	###MATERIAL
#
# 	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
#
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		print('Qual é a Meta?')
# 		Meta = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# 		else:
# 			Iniciador = ''
#
# 		print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask() \
#  \
# 		if TIPO_DE_RESULTADO == 'elaboração':
#
# 			print('há Resultado_elaboração atributo ou papel?')
# 			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# 			if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# 					RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# 				realizacao_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
# 				if realizacao_atributo == 'adjetivo':
# 					Atributo = adjetivo()
# 				elif realizacao_atributo == 'frase_preposicional':
# 					Atributo = frase_preposicional()
# 			elif RESULTADO_QUALITATIVO == '-resultado':
# 				Atributo = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstancia + '.'
#
# 		elif TIPO_DE_RESULTADO == 'extensão':
# 			print('Há Participante Beneficiario na oração?')
# 			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 			if RECEPÇÃO == '+beneficiário':
# 				Beneficiario = frase_preposicional()
# 			elif RECEPÇÃO == '-beneficiário':
# 				Beneficiario = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Meta + '  ' + Beneficiario + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		print('Qual é a Meta?')
# 		Meta = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN()
# 		else:
# 			Iniciador = ''
#
# 		print(
# 			'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# 		CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()
#
# 		if CLIENTE == '+cliente':
# 			Cliente = frase_preposicional()
# 		else:
# 			Cliente = ''
#
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# 		         + ' ' + Meta + ' ' + Cliente + ' ' + Circunstancia + '.'
#
# 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN() + grupo_verbal()
# 		else:
# 			Iniciador = ''
# 		print('Há Participante Beneficiario na oração?')
# 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 		if RECEPÇÃO == '+beneficiário':
# 			Beneficiario = frase_preposicional()
# 		elif RECEPÇÃO == '-beneficiário':
# 			Beneficiario = ''
# 		print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# 		if TIPO_DE_RESULTADO == 'elaboração':
# 			print('Qual é o Escopo?')
# 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# 			if tipo_Escopo == 'escopo(processo)':
# 				Escopo = estrutura_GN()
# 			elif tipo_Escopo == 'escopo(entidade)':
# 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Escopo + ' ' + Beneficiario + ' ' + Circunstancia + '.'
#
# 		elif TIPO_DE_RESULTADO == 'intensificação':
# 			print('Qual é o Escopo?')
# 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# 			if tipo_Escopo == 'escopo(processo)':
# 				Escopo = estrutura_GN()
# 			elif tipo_Escopo == 'escopo(entidade)':
# 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
# 			print('Há resultado locativo?')
# 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# 			if realizacao_locativo == 'sim':
# 				Resultado_locativo = frase_preposicional()
# 			else:
# 				Resultado_locativo = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Beneficiario + ' ' + Circunstancia + '.'
#
#
# 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA': \
#  \
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
# 		print('Há Participante Beneficiario na oração?')
# 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 		if RECEPÇÃO == '+beneficiário':
# 			Beneficiario = frase_preposicional()
# 		elif RECEPÇÃO == '-beneficiário':
# 			Beneficiario = ''
# 		print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# 		if TIPO_DE_RESULTADO == 'elaboração':
# 			print('Orações médio_sem_alcance  selecionam -escopo')
# 			Escopo = ''
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Beneficiario + '' + Circunstancia + '.'
#
#
# 		elif TIPO_DE_RESULTADO == 'intensificação':
# 			print('Orações médio_sem_alcance selecionam -escopo')
# 			print('Há Participante Beneficiario na oração?')
# 			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 			if RECEPÇÃO == '+beneficiário':
# 				Beneficiario = frase_preposicional()
# 			elif RECEPÇÃO == '-beneficiário':
# 				Beneficiario = ''
# 			print('Há resultado locativo?')
# 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# 			if realizacao_locativo == 'sim':
# 				Resultado_locativo = frase_preposicional()
# 			else:
# 				Resultado_locativo = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Resultado_locativo + ' ' + Circunstancia + ' ' + Beneficiario + '.'
#
#
# 	##MATERIAL METEOROLÓGICA
# 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
# 			and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		Polaridade = POLARIDADE()
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN()
# 		else:
# 			Iniciador = ''
# 		print('Há Participante Beneficiario na oração?')
# 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 		if RECEPÇÃO == '+beneficiário':
# 			Beneficiario = frase_preposicional()
# 		elif RECEPÇÃO == '-beneficiário':
# 			Beneficiario = ''
# 		tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
# 		print('Qual o tipo_pessoa de inTransitividade?')
# 		if tipo_intransitiva == 'impessoal(fenômeno_natural)':
# 			print('Há escopo?')
# 			escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
# 			if escopo_intransitiva == '+escopo':
# 				print('Qual estrutura realiza o escopo?')
# 				realizacao_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
# 				if realizacao_escopo == 'frase_preposicional':
# 					Escopo = frase_preposicional()
# 				elif realizacao_escopo == 'grupo_nominal':
# 					Escopo = estrutura_GN()
# 			elif escopo_intransitiva == '-escopo':
# 				Escopo = ''
#
# 		Circunstância = circunstância()
#
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
# 		         + ' ' + Escopo + ' ' + Beneficiario + ' ' + Circunstancia + '.'
#
#
# 	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
# 		Tema_textual = TEMA_TEXTUAL() \
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		Polaridade = POLARIDADE()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN() + grupo_verbal()
# 		else:
# 			Iniciador = ''
# 		print('Há Participante Beneficiario na oração?')
# 		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 		if RECEPÇÃO == '+beneficiário':
# 			Beneficiario = frase_preposicional()
# 		elif RECEPÇÃO == '-beneficiário':
# 			Beneficiario = ''
# 		Circunstância = circunstância()
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 		         + ' ' + Processo + ' ' + Beneficiario + ' ' + Circunstancia + '.'
#
# 		##########COMEÇO DE AGENCIAMENTO PASSIVA
# 		# (E CONSEQUENTEMENTE MUDANÇA NO TEMA IDEACIONAL: COMPLEMENTO ELEMENTAL)
#
# 	#  elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
# 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 	#          and Tema_id == 'TID_complemento_elemental':
# 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# 	#      Tema_textual=TEMA_TEXTUAL()
# 	#
# 	#      print ('Qual o Processo?')
# 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# 	#      print('Qual é a Meta?')
# 	#      Meta = estrutura_GN()
# 	#      Polaridade = POLARIDADE ()
# 	#      Circunstância = circunstância()
# 	#      print('Há Participante Beneficiario na oração?')
# 	#      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 	#      if RECEPÇÃO == '+beneficiário':
# 	#          Beneficiario = frase_preposicional()
# 	#      elif RECEPÇÃO == '-beneficiário':
# 	#          Beneficiario = ''
# 	#      print ('Há Participante Iniciador na oração?')
# 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# 	#      if INICIADOR == '+iniciador':
# 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# 	#      else:
# 	#          Iniciador = ''
# 	#
# 	#      print ('O Ator/Agente é realizado na oração?')
# 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# 	#      if realizacao_Ator == '+ator/agente':
# 	#          print('Qual é o Ator/Agente?')
# 	#          Ator = frase_preposicional()
# 	#      elif realizacao_Ator == '-ator/agente':
# 	#          Ator = ''
# 	#      print ('Há resultado do processo?')
# 	#      TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
# 	#
# 	#      if TIPO_DE_RESULTADO == 'elaboração':
# 	#
# 	#          print ('há Resultado_elaboração atributo ou papel?')
# 	#          RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# 	#          if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# 	#              RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# 	#              realizacao_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
# 	#              if realizacao_atributo == 'adjetivo':
# 	#                  Atributo = adjetivo ()
# 	#              elif realizacao_atributo == 'frase_preposicional':
# 	#                  Atributo = frase_preposicional()
# 	#          elif RESULTADO_QUALITATIVO == '-resultado':
# 	#              Atributo = ''
# 	#
# 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
# 	#                   + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' +Beneficiario+' '+ Circunstancia +'.'
# 	#
# 	#      elif TIPO_DE_RESULTADO == 'extensão':
# 	#          print ('Há Participante Beneficiario na oração?')
# 	#          RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
# 	#          if RECEPÇÃO == '+beneficiário':
# 	#              Beneficiario = frase_preposicional()
# 	#          elif RECEPÇÃO == '-beneficiário':
# 	#              Beneficiario = ''
# 	#
# 	#
# 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
# 	#                   + ' ' + Processo  +'  '+ Beneficiario + ' ' + Ator +' '+Beneficiario+' '+ Circunstancia +'.'
# 	#
# 	# ##
# 	#
# 	#  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
# 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 	#          and Tema_id == 'TID_complemento_elemental':
# 	#
# 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# 	#      Tema_textual=TEMA_TEXTUAL()
# 	#
# 	#      print ('Qual o Processo?')
# 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# 	#      print('Qual é a Meta?')
# 	#      Meta = estrutura_GN()
# 	#      Polaridade = POLARIDADE ()
# 	#      print('Há Participante Beneficiario na oração?')
# 	#      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 	#      if RECEPÇÃO == '+beneficiário':
# 	#          Beneficiario = frase_preposicional()
# 	#      elif RECEPÇÃO == '-beneficiário':
# 	#          Beneficiario = ''
# 	#      Circunstância = circunstância()
# 	#
# 	#
# 	#      print ('Há Participante Iniciador na oração?')
# 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# 	#      if INICIADOR == '+iniciador':
# 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# 	#      else:
# 	#          Iniciador = ''
# 	#
# 	#      print ('O Ator/Agente é realizado na oração?')
# 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# 	#      if realizacao_Ator == '+ator/agente':
# 	#          print('Qual é o Ator/Agente?')
# 	#          Ator = frase_preposicional()
# 	#      elif realizacao_Ator == '-ator/agente':
# 	#          Ator = ''
# 	#
# 	#
# 	#      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# 	#      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
# 	#
# 	#      if CLIENTE == '+cliente':
# 	#          Cliente = frase_preposicional()
# 	#      elif CLIENTE == '-cliente':
# 	#          Cliente='' \
# 	#
# 	#      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
# 	#               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Beneficiario+' '+Circunstância +'.'
#
#
# 	##ORAÇÃO EXISTENCIAL
#
# 	elif Transitividade == 'PR_Existencial_AG_NA' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
# 			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
#
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Existente?')
# 		Existente = estrutura_GN()
# 		Circunstância = circunstância()
#
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Processo + ' ' + Existente + ' ' + Circunstancia + '.'
#
# 	#
# 	##
# 	###
# 	######
# 	####### ORAÇÕES INTERROGATIVAS POLARES
#
# 	##ORAÇÃO MATERIAL MODO INTERROGATIVO POLAR
#
# 	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
#
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		print('Qual é a Meta?')
# 		Meta = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# 		else:
# 			Iniciador = ''
#
# 		print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()
#
# 		if TIPO_DE_RESULTADO == 'elaboração':
#
# 			print('há Resultado_elaboração atributo ou papel?')
# 			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# 			if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# 					RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# 				realizacao_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
# 				if realizacao_atributo == 'adjetivo':
# 					Atributo = adjetivo()
# 				elif realizacao_atributo == 'frase_preposicional':
# 					Atributo = frase_preposicional()
# 			elif RESULTADO_QUALITATIVO == '-resultado':
# 				Atributo = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstancia + '?'
#
#
#
# 		elif TIPO_DE_RESULTADO == 'extensão':
# 			print('Há Participante Beneficiario na oração?')
# 			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
# 			if RECEPÇÃO == '+beneficiário':
# 				Beneficiario = frase_preposicional()
# 			elif RECEPÇÃO == '-beneficiário':
# 				Beneficiario = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Meta + '  ' + Beneficiario + ' ' + Circunstancia + '?'
#
#
# 	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		print('Qual é a Meta?')
# 		Meta = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN()
# 		else:
# 			Iniciador = ''
#
# 		print(
# 			'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# 		CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()
#
# 		if CLIENTE == '+cliente':
# 			Cliente = frase_preposicional()
# 		else:
# 			Cliente = ''
#
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 		         + ' ' + Processo + ' ' + Meta + ' ' + Cliente + ' ' + Circunstancia + '?'
#
#
# 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN() + grupo_verbal()
# 		else:
# 			Iniciador = ''
#
# 		print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# 		if TIPO_DE_RESULTADO == 'elaboração':
# 			print('Qual é o Escopo?')
# 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# 			if tipo_Escopo == 'escopo(processo)':
# 				Escopo = estrutura_GN()
# 			elif tipo_Escopo == 'escopo(entidade)':
# 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Escopo + ' ' + Circunstancia + '?'
#
# 		elif TIPO_DE_RESULTADO == 'intensificação':
# 			print('Qual é o Escopo?')
# 			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
# 			if tipo_Escopo == 'escopo(processo)':
# 				Escopo = estrutura_GN()
# 			elif tipo_Escopo == 'escopo(entidade)':
# 				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
# 			print('Há resultado locativo?')
# 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# 			if realizacao_locativo == 'sim':
# 				Resultado_locativo = frase_preposicional()
# 			else:
# 				Resultado_locativo = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Circunstancia + '?'
#
#
# 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
# 		print('Há resultado do processo?')
# 		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
# 		if TIPO_DE_RESULTADO == 'elaboração':
# 			print('Orações médio_sem_alcance  selecionam -escopo')
# 			Escopo = ''
#
# 		elif TIPO_DE_RESULTADO == 'intensificação':
# 			print('Orações médio_sem_alcance selecionam -escopo')
#
# 			print('Há resultado locativo?')
# 			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
# 			if realizacao_locativo == 'sim':
# 				Resultado_locativo = frase_preposicional()
# 			else:
# 				Resultado_locativo = ''
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Resultado_locativo + ' ' + Circunstancia + '?'
#
#
# 	##ORAÇÃO METEOROLÓGICA MODO INTERROGATIVO POLAR
# 	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
# 			and Modo == 'sujeitabilidade_recuperação_NA_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 		tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
# 		print('Qual o tipo_pessoa de inTransitividade?')
# 		if tipo_intransitiva == 'impessoal(fenômeno_natural)':
# 			print('Há escopo?')
# 			escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
# 			if escopo_intransitiva == '+escopo':
# 				print('Qual estrutura realiza o escopo?')
# 				realizacao_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
# 				if realizacao_escopo == 'frase_preposicional':
# 					Escopo = frase_preposicional()
# 				elif realizacao_escopo == 'grupo_nominal':
# 					Escopo = estrutura_GN()
# 			elif escopo_intransitiva == '-escopo':
# 				Escopo = ''
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
#
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN()
# 		else:
# 			Iniciador = ''
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
# 		         + ' ' + Escopo + ' ' + Circunstancia + '?'
#
#
# 	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Ator?')
# 		Ator = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
# 		print('Há Participante Iniciador na oração?')
# 		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
# 		if INICIADOR == '+iniciador':
# 			Iniciador = estrutura_GN() + grupo_verbal()
# 		else:
# 			Iniciador = ''
#
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
# 		         + ' ' + Processo + ' ' + Circunstancia + '?'
#
# 		##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)
#
# 	#  elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
# 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'\
# 	#          and Tema_id == 'TID_complemento_elemental':
# 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# 	#      Tema_textual=TEMA_TEXTUAL()
# 	#
# 	#      print ('Qual o Processo?')
# 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# 	#      print('Qual é a Meta?')
# 	#      Meta = estrutura_GN()
# 	#      Polaridade = POLARIDADE ()
# 	#      Circunstância = circunstância()
# 	#      print ('Há Participante Iniciador na oração?')
# 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# 	#      if INICIADOR == '+iniciador':
# 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# 	#      else:
# 	#          Iniciador = ''
# 	#
# 	#      print ('O Ator/Agente é realizado na oração?')
# 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# 	#      if realizacao_Ator == '+ator/agente':
# 	#          print('Qual é o Ator/Agente?')
# 	#          Ator = frase_preposicional()
# 	#      elif realizacao_Ator == '-ator/agente':
# 	#          Ator = ''
# 	#
# 	#
# 	#      print ('Há resultado do processo?')
# 	#      TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
# 	#
# 	#      if TIPO_DE_RESULTADO == 'elaboração':
# 	#
# 	#          print ('há Resultado_elaboração atributo ou papel?')
# 	#          RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
# 	#          if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
# 	#              RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
# 	#              realizacao_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
# 	#              if realizacao_atributo == 'adjetivo':
# 	#                  Atributo = adjetivo ()
# 	#              elif realizacao_atributo == 'frase_preposicional':
# 	#                  Atributo = frase_preposicional()
# 	#          elif RESULTADO_QUALITATIVO == '-resultado':
# 	#              Atributo = ''
# 	#
# 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta \
# 	#                   + ' ' + Polaridade + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' + Circunstancia +'?'
# 	#
# 	#      elif TIPO_DE_RESULTADO == 'extensão':
# 	#          print ('Há Participante Beneficiario na oração?')
# 	#          RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
# 	#          if RECEPÇÃO == '+beneficiário':
# 	#              Beneficiario = frase_preposicional()
# 	#          elif RECEPÇÃO == '-beneficiário':
# 	#              Beneficiario = ''
# 	#
# 	#
# 	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
# 	#                   + Meta + ' ' + Polaridade + ' ' + Processo  +'  '+ Beneficiario + ' ' + Ator +' ' + Circunstancia +'?'
# 	#
# 	# ##
# 	#
# 	#  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
# 	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'\
# 	#          and Tema_id == 'TID_complemento_elemental':
# 	#
# 	#      Tema_interpessoal = TEMA_INTERPESSOAL()
# 	#      Tema_textual=TEMA_TEXTUAL()
# 	#
# 	#      print ('Qual o Processo?')
# 	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
# 	#      print('Qual é a Meta?')
# 	#      Meta = estrutura_GN()
# 	#      Polaridade = POLARIDADE ()
# 	#      Circunstância = circunstância()
# 	#
# 	#      print ('Há Participante Iniciador na oração?')
# 	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
# 	#      if INICIADOR == '+iniciador':
# 	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
# 	#      else:
# 	#          Iniciador = ''
# 	#
# 	#      print ('O Ator/Agente é realizado na oração?')
# 	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
# 	#      if realizacao_Ator == '+ator/agente':
# 	#          print('Qual é o Ator/Agente?')
# 	#          Ator = frase_preposicional()
# 	#      elif realizacao_Ator == '-ator/agente':
# 	#          Ator = ''
# 	#
# 	#
# 	#      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
# 	#      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
# 	#
# 	#      if CLIENTE == '+cliente':
# 	#          Cliente = frase_preposicional()
# 	#      elif CLIENTE == '-cliente':
# 	#          Cliente=''
# 	#
# 	#      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' '\
# 	#               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Circunstancia +'?'
# 	#
#
# 	###RELACIONAl MODO INTERROGATIVO POLAR
#
# 	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
# 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
# 		## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
# 		Tema_textual = TEMA_TEXTUAL()
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 		print('Qual o tipo_pessoa de especificação de associação?')
# 		especificacao_associacao = choice.Menu(['entidade', 'qualidade']).ask()
# 		print('Qual a fase da atribuição?')
# 		fase_atribuicao = choice.Menu(['neutra',
# 		                               'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
# 		###não vou especializar os tipos de fase.
# 		print('Qual o domínio da atribuição')
# 		dominio_atribuicao = choice.Menu(['material', 'semiótico']).ask()
#
# 		if (
# 				especificacao_associacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material' or
# 				especificacao_associacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico' or
# 				especificacao_associacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material' or
# 				especificacao_associacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico'):
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador?')
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = estrutura_GN()
#
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Atributo + ' ' + Circunstancia + '?'
#
# 		elif (
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material' or
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico' or
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material' or
# 				especificacao_associacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico'):
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador?')
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = adjetivo()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
# 			# o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
# 			##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Atributo + ' ' + Circunstancia + '?'
#
#
# 	###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
# 	##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva (há a possibilidade de Agente de segunda, terceira.....ordem)
# 	####para desenvolver....
# 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Atribuidor?')
# 			Atribuidor = estrutura_GN()
# 			print('Qual o Portador?')
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
#
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Portador + ' ' + Atributo + ' ' + Circunstancia + '?'
#
# 	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Atribuidor?')
# 			Atribuidor = frase_preposicional()
#
# 			print('Qual o Portador?')
# 			Portador = estrutura_GN()
# 			print('Qual o Atributo?')
# 			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)
#
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Atributo + ' ' + Atribuidor + ' ' + Circunstancia + '?'
#
#
# 	####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)
#
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação':
# 		print('Apesar de Médio(middle), a direcionalidade_voz '
# 		      'do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina '
# 		      'se é operativa ou receptiva. Selecione a direcionalidade:')
# 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 		if direcionalidade_voz == 'meio_operativa':
# 			print('Neste caso, o Símbolo/Identificado conflui com o '
# 			      'Sujeito(geralmente o elemento em posição temática')
#
# 			# (confluência do Símbolo/Identificado) =
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstancia + '?'
#
#
#
# 		elif direcionalidade_voz == 'meio_receptiva':
# 			print('Neste caso, o Valor/Identificador conflui com o Sujeito')
# 			##NESTE CASO, confluência de Valor/Sujeito
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstancia + '?'
#
#
#
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação':
#
# 		print(
# 			'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 		if direcionalidade_voz == 'meio_operativa':
# 			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
#
# 			# (confluência do Símbolo/Identificador/Sujeito) =
# 			# (Valor/Identificado/complemento)
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstancia + '?'
#
# 		elif direcionalidade_voz == 'meio_receptiva':
# 			print('Neste caso, o Valor conflui com o Sujeito')
# 			##NESTE CASO, confluência de Valor/Identificado/Sujeito
# 			##(Símbolo/Identificador/Complemento)
#
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstancia + '?'
#
#
# 	####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)
#
# 	#    ###TRUE_Efetiva_operativa
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		# POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Designador?')
# 			Designador = estrutura_GN()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()  ##ou frase preposicional?
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + ' ' + Circunstancia + '?'
# 			###rever possíveis estruturas para este tipo_pessoa de oração(pode haver 2 processos?)
#
# 	###TRUE_Efetiva_receptiva
#
# 	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		print('Qual o tipo_pessoa de atribuição de relação?')
# 		tipo_atribuição_relação = atribuição_de_relação()
# 		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
# 		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
# 		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
#
# 		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
# 		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
# 		    tipo_atribuição_relação == 'atribuição_proj_verbal',
# 		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
# 		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual é o Designador?')
# 			Designador = frase_preposicional()
# 			print('Qual é o Símbolo(Token)?')
# 			Símbolo = estrutura_GN()
# 			print('Qual o Valor(Value)?')
# 			Valor = estrutura_GN()  ##ou frase preposicional?
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
# 			#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Valor + ' ' + Designador + ' ' + Circunstancia + '?'
# 	####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realizacao de cada participante;
# 	#        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)
#
# 	# POSSESSIVO ATRIBUTIV0
#
# 	elif Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()
#
# 		if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':
#
# 			realizacao_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()
#
# 			if realizacao_atributo == 'grupo_nominal_possessivo':
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Posse?')
# 				Portador_Posse = estrutura_GN()
# 				print('Qual é o Atributo/Possuidor?')
# 				Atributo_Possuidor = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse \
# 				         + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstancia + '?'
#
# 			elif realizacao_atributo == 'frase_preposicional':
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Posse?')
# 				Portador_Posse = estrutura_GN()
# 				print('Qual é o Atributo/Possuidor?')
# 				Atributo_Possuidor = frase_preposicional()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstancia + '?'
#
#
# 		elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':
#
# 			##VERBO TER/POSSUIR/
#
# 			tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask()
#
# 			if tipo_possuidor == 'possuidor_portador':
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Possuidor?')
# 				Portador_Possuidor = estrutura_GN()
# 				print('Qual é o Atributo/Posse?')
# 				Atributo_Posse = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor \
# 				         + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Posse + ' ' + Circunstancia + '?'
# 			###VERBOS PERTENCER A/...
#
# 			elif tipo_possuidor == 'possuidor_atributo':
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual o Portador/Possuidor?')
# 				Portador_Posse = estrutura_GN()
# 				print('Qual é o Atributo/Posse?')
# 				Atributo_Possuidor = frase_preposicional()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstancia + '?'
#
# 		# POSSESSIVO IDENTIFICATIVO
#
#
# 	elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()
#
# 		if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')
#
# 				print(
# 					'Escolha o tipo_pessoa de realizacao do Valor:')
# 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
#
# 				if realizacao_Valor == 'grupo_nominal':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)/Possuído?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)/Possuidor?')
# 					Valor_Possuidor = estrutura_GN()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O piano é seu
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstancia + '?'
#
# 				elif realizacao_Valor == 'frase_preposicional':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)?')
# 					Valor_Possuidor = frase_preposicional()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O piano é do André
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstancia + '?'
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')
#
# 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
#
# 				if realizacao_Valor == 'grupo_nominal':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)/Possuído?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)/Possuidor?')
# 					Valor_Possuidor = estrutura_GN()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O seu é o piano
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstancia + '?'
#
# 				elif realizacao_Valor == 'frase_preposicional':
#
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()
# 					print('Qual é o Símbolo(Token)?')
# 					Símbolo_Possuído = estrutura_GN()
# 					print('Qual o Valor(Value)?')
# 					Valor_Possuidor = estrutura_GN()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O do André é o piano
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor \
# 					         + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstancia + '?'
#
# 		elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
# 			## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
# 			##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print(
# 					'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)/Possuidor?')
# 				Símbolo_Possuidor = estrutura_GN()
# 				print('Qual o Valor(Value)/Possuído?')
# 				Valor_Possuído = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: O produto contém plástico, Eles merecem a aposentadoria
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor \
# 				         + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuído + ' ' + Circunstancia + '?'
#
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')
#
# 				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
#
# 				if realizacao_Valor == 'grupo_nominal':
# 					Tema_textual = TEMA_TEXTUAL()
# 					Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 					print('Qual o Processo?')
# 					Processo = grupo_verbal()  ##na passiva
# 					print('Qual o Valor(Value)/Possuído?')
# 					Valor_Possuído = estrutura_GN()
# 					print('Qual é o Símbolo(Token)/Possuidor?')
# 					Símbolo_Possuidor = frase_preposicional()
# 					Polaridade = POLARIDADE()
# 					Circunstância = circunstância()
#
# 					# Ex.: O seu é o piano
# 					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade \
# 					         + ' ' + Processo + ' ' + Símbolo_Possuidor + ' ' + Circunstancia + '?'
#
#
# 	#####RELACIONAL CIRCUNSTANCIAL MODO INTERROGATIVO POLAR
#
# 	elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
# 		print('Qual o tipo_pessoa de realizacao da Relacional Circunstancial?')
# 		TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()
#
# 		if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador')
# 			Portador = estrutura_GN()
# 			print('Qual é o Atributo Circunstancial?')
# 			Atributo_Circunstancial = circunstância()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			# Ex.: O livro é sobre a IIGuerra
#
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
# 			         + ' ' + Processo + ' ' + Atributo_Circunstancial + ' ' + Circunstancia + '?'
#
# 		elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
# 			Tema_textual = TEMA_TEXTUAL()
# 			Tema_interpessoal = TEMA_INTERPESSOAL()
# 			print('Qual o Processo?')
# 			Processo = grupo_verbal()
# 			print('Qual o Portador')
# 			Portador = estrutura_GN()
# 			print('Qual é o Atributo Circunstancial?')
# 			Atributo = estrutura_GN()
# 			Polaridade = POLARIDADE()
# 			Circunstância = circunstância()
#
# 			# Ex.: O livro retrata a IIGuerra
# 			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
# 			         + ' ' + Atributo + ' ' + Circunstancia + '?'
#
#
#
#
# 	elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		print('O significado circunstancial é realixado no participante ou no processo?')
# 		TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
# 			['participante_circunstancial', 'processo_circunstancial']).ask()
#
# 		if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
# 				print('Qual o Valor(Value)?')
# 				Valor = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: Amanhá é dia 10
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstancia + '?'
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
# 				print('Qual o Valor(Value)?')
# 				Valor = estrutura_GN()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.:dia 10 é Amanhá
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstancia + '?'
#
#
# 		elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
#
# 			print(
# 				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
# 			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()
#
# 			if direcionalidade_voz == 'meio_operativa':
# 				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
# 				print('Qual o Valor(Value)?')
# 				Valor = circunstância()
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
#
# 				# Ex.: A feira dura o dia inteiro
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstancia + '?'
#
#
# 			elif direcionalidade_voz == 'meio_receptiva':
# 				print('Neste caso, há confluência Valor/Sujeito/Identificado')
#
# 				Tema_textual = TEMA_TEXTUAL()
# 				Tema_interpessoal = TEMA_INTERPESSOAL()
#
# 				print('Qual o Processo?')
# 				Processo = grupo_verbal()  ## reiterações-verbo na passiva
# 				print('Qual o Valor(Value)?')
# 				Valor = circunstância()
# 				print('Qual é o Símbolo(Token)?')
# 				Símbolo = circunstância()
#
# 				Polaridade = POLARIDADE()
# 				Circunstância = circunstância()
# 				# Ex.: O dia todo é ocupado pela feira
#
# 				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
# 				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstancia + '?'
#
#
# 	##ORAÇÃO EXISTENCIAL MODO INTERROGATIVO POLAR
#
# 	elif Transitividade == 'PR_Existencial_AG_NA' \
# 			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
# 			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
#
# 		Tema_interpessoal = TEMA_INTERPESSOAL()
# 		Tema_textual = TEMA_TEXTUAL()
#
# 		print('Qual o Processo?')
# 		Processo = grupo_verbal()
# 		print('Qual é o Existente?')
# 		Existente = estrutura_GN()
# 		Polaridade = POLARIDADE()
# 		Circunstância = circunstância()
# 		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Polaridade \
# 		         + ' ' + Processo + ' ' + Existente + ' ' + Circunstancia + '?'
#
# 	return (re.sub(' +', ' ', oração).strip().capitalize())

# #
# # def flexionarVerbo(experience='none', functionInGroup='none',
# #                    lemma='none', person='none', gender='none', number='none',
# #                    mood='none', tense='none', aspect='none'):
# #     if number == 'Plur':
# #         OI_numero = 'plural'
# #     elif number == 'Sing':
# #         OI_numero = 'singular'
# #     else:
# #         OI_numero = None
# #
# #     if person == '1':
# #         OI_tipo_de_pessoa = '1pessoa'
# #
# #     elif person == '2':
# #         OI_tipo_de_pessoa = '2pessoa'
# #
# #     elif person == '3':
# #         OI_tipo_de_pessoa = '3pessoa'
# #     else:
# #         OI_tipo_de_pessoa = None
# #
# #     if gender == 'Masc':
# #         genero = 'masculino'
# #
# #     elif gender == 'Fem':
# #         genero = 'feminino'
# #
# #     else:
# #         genero = None
# #
# #     ####
# #     if mood + '_' + tense + '_' + aspect == 'Ind_Past_Perf':
# #         tipo_de_orientacao = 'pretérito_perfectivo_I'
# #     elif mood + '_' + tense + '_' + aspect == 'Ind_Past_Perf':
# #         tipo_de_orientacao = 'pretérito_perfectivo_II'
# #     elif mood + '_' + tense + '_' + aspect == 'Ind_Past_Imp':
# #         tipo_de_orientacao = 'pretérito_imperfectivo'
# #     elif mood + '_' + tense + '_' + aspect == 'Ind_Fut_none':
# #         tipo_de_orientacao = 'futuro'
# #     elif mood + '_' + tense + '_' + aspect == 'Ind_Pres_none':
# #         tipo_de_orientacao = 'presente'
# #     elif mood + '_' + tense + '_' + aspect == 'Sub_Pres_none':
# #         tipo_de_orientacao = 'subjuntivo_conjuntivo'
# #     elif mood + '_' + tense + '_' + aspect == 'Sub_Past_Imp':
# #         tipo_de_orientacao = 'subjuntivo_condicional'
# #     elif mood + '_' + tense + '_' + aspect == 'Sub_Fut_none':
# #         tipo_de_orientacao = 'subjuntivo_optativo'
# #     elif mood + '_' + tense + '_' + aspect == 'none_Past_Perf':
# #         tipo_de_orientacao = 'particípio'
# #     elif mood == 'Imp_POS':
# #         tipo_de_orientacao = 'imperativo_I'
# #     elif mood == 'Imp_NEG':
# #         tipo_de_orientacao = 'imperativo_II'
# #     elif mood + '_' + tense + '_' + aspect == 'Cnd_Past_none':
# #         tipo_de_orientacao = 'passado_volitivo'
# #     elif mood + '_' + tense + '_' + aspect == 'none_Inf_none':
# #         tipo_de_orientacao = 'não_finito_concretizado'
# #     elif person + '_' + gender + '_' + number + '_' + mood + '_' + tense + '_' + aspect == 'none_none_none_none_Pres_Prog':
# #         tipo_de_orientacao = 'gerúndio'
# #     elif person + '_' + gender + '_' + number + '_' + mood + '_' + tense + '_' + aspect == 'none_none_none_none_Inf_none':
# #         tipo_de_orientacao = 'infinitivo'
# #     verb = verbo_geral(experience, functionInGroup, lemma, tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)
# #     return verb
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # flexionarVerbo(experience="Fazer", functionInGroup='Evento', lemma="registrar", person='none', gender='none',
# #                number='none', mood='none', tense='Pres', aspect='Prog')
# #
# # flexionarVerbo(experience="Fazer", functionInGroup='Evento', lemma="registrar", person='none', gender='Masc',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# #
# # flexionarVerbo(experience="Fazer", functionInGroup='Evento', lemma="registrar", person='1', gender='none',
# #                number='Plur', mood='none', tense='Inf', aspect='none')
# #
# # #
# # # ######verbos exemplos para o robô
# # # TEVE
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='ter', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# #
# # # REGISTROU
# # flexionarVerbo(experience="Fazer", functionInGroup='Evento', lemma="registrar", person='3', gender='none',
# #                number='Sing', mood='Ind', tense='Past', aspect='Perf')
# #
# # # DIVULGOU
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='reportar', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# # # DIVULGOU
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='divulgar', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# # # identificou
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='identificar', person='3', gender='none',
# #                number='Sing', mood='Ind', tense='Past', aspect='Perf')
# # # #mostrou
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='mostrar', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# # # #foram (auxiliar)
# # flexionarVerbo(experience='Ser', functionInGroup='Auxiliar', lemma='ser', person='3', gender='none', number='Plur',
# #                mood='Ind', tense='Past', aspect='Perf')
# # # #desmatados
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='desmatar', person='none', gender='Masc',
# #                number='Plur', mood='none', tense='Past', aspect='Perf')
# # # #foi (EVENTO)
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='ser', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# #
# # # #teve
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='ter', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# # #
# # # #atingido
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='atingir', person='none', gender='Masc',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# # #
# # # #foi (auxiliar)
# # flexionarVerbo(experience='Ser', functionInGroup='Auxiliar', lemma='ser', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# # #
# # # #devastada
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='devastar', person='none', gender='Fem',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# # #
# # # #devastado
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='devastar', person='none', gender='Masc',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# # # #deixa
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='deixar', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Pres', aspect='none')
# # # #SOMANDO
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='somar', person='none', gender='none', number='none',
# #                mood='none', tense='Pres', aspect='Prog')
# # # #somam
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='somar', person='3', gender='none', number='Plur',
# #                mood='Ind', tense='Pres', aspect='none')
# # # soma
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='somar', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Pres', aspect='none')
# # # somaram
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='somar', person='3', gender='none', number='Plur',
# #                mood='Ind', tense='Past', aspect='Perf')
# # # TEM
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='ter', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Pres', aspect='none')
# # # acumulando
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='acumular', person='none', gender='none',
# #                number='none', mood='none', tense='Pres', aspect='Prog')
# #
# # # #ACUMULOU
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='acumular', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# # # ACUMULA
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='acumular', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Pres', aspect='none')
# # # atingindo
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='atingir', person='none', gender='none', number='none',
# #                mood='none', tense='Pres', aspect='Prog')
# # #
# # # 'analisado'
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='analisar', person='none', gender='Masc',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# #
# # # 'desmatados'
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='desmatar', person='none', gender='Masc',
# #                number='Plur', mood='none', tense='Past', aspect='Perf')
# #
# # # 'desmatado'
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='desmatar', person='none', gender='Masc',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# #
# # # 'desmatada'
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='desmatar', person='none', gender='Fem',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# # # AFETADO
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='afetar', person='none', gender='Masc',
# #                number='Sing', mood='none', tense='Past', aspect='Perf')
# # # GERADO
# # flexionarVerbo(experience='Fazer', functionInGroup='Evento', lemma='gerar', person='none', gender='Masc', number='Sing',
# #                mood='none', tense='Past', aspect='Perf')
# #
# # # RASTREOU
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='rastrear', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')
# #
# # # alertou
# # flexionarVerbo(experience='Ser', functionInGroup='Evento', lemma='alertar', person='3', gender='none', number='Sing',
# #                mood='Ind', tense='Past', aspect='Perf')


if __name__ == "__main__":
	##exemplos oração mental
# 	print(oracaoMental(
# 		# transitividade
# 		'Mental', None,
# 		1, None, None,
#
# 		# modo
# 		0, 0, 1,
# 		# TEMA IDEACIONAL
# 		'orientado', 'direcional',
# 		'default', 'indicativo',
# 		'declarativo', 'NA',
# 		None, None, None,
#
# 		##Processo Mental
# 		'não-fenomenalização_assunto', 'superior_cognitivo',
# 		# Processo
# 		'Fazer', 'não_agenciado', None, None, None, None, None, None,
# 		None, None, None, None, None, None, None, None, None,
# 		None, None, None, None, None, None, None, None, None, None, None,
# 		None, None, None, None, None,
# 		'Morfologia_padrão', 'Fazer', 'Evento', 'saber', 'presente', 'singular',
# 		None, '1pessoa', 'Morfologia_padrão',
# 		# POLARIDADE
# 		'positiva',
#
# 		##PARTICIPANTES
# 		None, None, None, None,
# 		None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, None, None, None,
# 		None, None, None, None,
# 		None,
# 		'consciente', None, None,
# 		None, 'pronome_caso_reto',
# 		None, 'singular',
# 		None, None, None, None,
# 		'falante',
# 		None, None, "Morfologia_padrão", None,
# 		None, None, None,
# 		None, None, None, None,
# 		# realizados por frase preposicional
# 		6, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None, 'não-binário', None, None,
# 		None, None, None, None,
# 		None, 'não_consciente', 'material',
# 		'abstração_material', None,
# 		'substantivo_comum', 'futebol', 'singular',
# 		None, None, None, None,
# 		None, None, None,
# 		None, None, None,
# 		None, None,
# 		None, None, None, None
# 	))
# 	print(oracaoMental(
# 	# transitividade
# 	'Mental', None,
# 	1, None, None,
#
# 	# modo
# 	0, 0, 1,
# 	# TEMA IDEACIONAL
# 	'orientado', 'direcional',
# 	'default', 'indicativo',
# 	'declarativo', 'NA',
# 	None, None, None,
#
# 	##Processo Mental
# 	'fenomenalização_fenômeno-simples', 'superior_cognitivo',
# # Processo
# 	'Sentir', 'não_agenciado', None, None, None, None, None, None,
# 	None, None, None, None, None, None, None, None, None,
# 	None, None, None, None, None, None, None, None, None, None, None,
# 	None, None, None, None, None,
# 	'Morfologia_padrão', 'Fazer', 'Evento', 'imaginar', 'pretérito_perfectivo_I', 'singular',
# 	None, '1pessoa', 'Morfologia_padrão',
# 	# POLARIDADE
# 	'positiva',
# 	##PARTICIPANTES
# 	# p1
# 	None, None, None, None,
# 	None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None, None, None,
# 	None, None, None, None,
# 	None,
# 	'consciente', None, None,
# 	None, 'pronome_caso_reto',
# 	None, 'singular',
# 	None, None, None, None,
# 	'falante',
# 	None, None, "Morfologia_padrão", None,
# 	None, None, None,
# 	None, None, None, None,
# # p2
# 	None, None, None, None,
# 	None, None, None, None,
# 	None, 'específico', 'NA',
# 	'masculino', 'singular', None,
# 	None, None, None,
# 	None, None, None, 'não-binário',
# 	None, None, None, None,
# 	None, None, None,
# 	'não_consciente', 'material', 'abstração_material',
# 	None, 'substantivo_comum', 'jogo',
# 	'singular', None, None, None, None,
# 	None, None, None, "Morfologia_padrão",
# 	None, None, None, None,
# 	None, None, None, None,
#
# 	# realizados por frase preposicional
# 	None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None, None, None, None,
# 	None, None, None, None,
# 	None, None,None,
# 	None, None,
# 	None, None, None,
# 	None, None, None, None,
# 	None, None, None,
# 	None, None, None,
# 	None, None,
# 	None, None, None, None,
# 	))



#impingente

	print(oracaoMental(
		# transitividade
		'Mental', None,
		1, None, None,

		# modo
		0, 0, 1,
		# TEMA IDEACIONAL
		'orientado', 'direcional',
		'default', 'indicativo',
		'declarativo', 'NA',
		None, None, None,

		##Processo Mental
		'fenomenalização_fenômeno-simples', 'superior_cognitivo',
		# Processo
		'Sentir', 'agenciado_ativa', None, None, None, None, None, None,
		None, None, None, None, None, None, None, None, None,
		None, None, None, None, None, None, None, None, None, None, None,
		None, None, None, None, None,
		'Morfologia_padrão', 'Fazer', 'Evento', 'agradar', 'presente', 'singular',
		None, '3pessoa', 'Morfologia_padrão',
		# POLARIDADE
		'positiva',
		##PARTICIPANTES
		# p1
		None, None, None, None,
		None, None, None, None,
		None, 'específico', 'NA',
		'feminino', 'singular', None,
		None, None, None,
		None, None, None, 'não-binário',
		None, None, None, None,
		None, None, None,
		'não_consciente', 'material', 'abstração_material',
		None, 'substantivo_comum', 'inovação',
		'singular', None, None, None, None,
		None, None, None, "Morfologia_padrão",
		None, None, None, None,
		None, None, None, None,

		# p2
		None, None, None, None,
		None, None,
		None, None, None,
		None, None, None,
		None, None, None,
		None, None, None,
		None, None, None, None, None,
		None, None, None, None,
		None,
		'consciente', None, None,
		None, 'pronome_caso_oblíquo',
		None, 'singular',
		None, None, None, None,
		'falante',
		'direto', 'átono', "padrão", None,
		None, None, None,
		None, None, None, None,

		# realizados por frase preposicional
		None, None, None,
		None, None, None,
		None, None, None,
		None, None, None,
		None, None, None,
		None, None, None,
		None, None, None, None, None,
		None, None, None, None,
		None, None, None,
		None, None,
		None, None, None,
		None, None, None, None,
		None, None, None,
		None, None, None,
		None, None,
		None, None, None, None
	))