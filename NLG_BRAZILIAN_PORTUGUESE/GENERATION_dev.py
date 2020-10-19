# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:50:31 2019

@author: andre
"""


# ######PRELIMINARES
# import os
# os.getcwd()
# help(os)
# os.listdir(os.curdir)


######
###

###############################################################################
#####################
###########ORDEM DA PALAVRA

###ADVÉRBIO    INÍCIO####

###########ORDEM DA PALAVRA

def adverbio_modo_switcher(i):
	#    i = int(input())

	switcher_modo = {
		1: 'bem',
		2: 'mal',
		3: 'assim',
		4: 'adrede',
		5: 'melhor',
		6: 'pior',
		7: 'depressa',
		8: 'devagar',
		9: 'acinte',
		10: 'debalde',
		11: 'cuidadosamente',
		12: 'calmamente',
		13: 'tristemente'
	}

	return switcher_modo.get(i, 'Seleção não disponível')


# adverbio_modo_switcher(2)

def adverbio_intensidade_switcher(i):
	#    i = int(input())

	switcher_intensidade = {
		1: 'muito',
		2: 'demais',
		3: 'todo',
		4: 'pouco',
		5: 'tão',
		6: 'quão',
		7: 'demasiado',
		8: 'bastante',
		9: 'imenso',
		10: 'demais',
		11: 'mais',
		12: 'menos',
		13: 'quanto',
		14: 'quase',
		15: 'tanto',
		16: 'assaz',
		17: 'tudo',
		18: 'nada'
	}
	return switcher_intensidade.get(i, 'Seleção não disponível')


# adverbio_intensidade_switcher (17)

def adverbio_lugar_switcher(i):
	#    i = int(input())

	switcher_lugar = {

		1: 'aí',
		2: 'aqui',
		3: 'acolá',
		4: 'cá',
		5: 'lá',
		6: 'ali',
		7: 'adiante',
		8: 'abaixo',
		9: 'embaixo',
		10: 'acima',
		11: 'adentro',
		12: 'dentro'
	}

	return switcher_lugar.get(i, 'Seleção não disponível')


# adverbio_lugar_switcher(5)

def adverbio_tempo_switcher(i):
	#    i = int(input())

	switcher_tempo = {
		1: 'ainda',
		2: 'agora',
		3: 'amanhã',
		4: 'à noite',
		5: 'anteontem',
		6: 'antes',
		7: 'à tarde',
		8: 'às vezes',
		9: 'atualmente',
		10: 'breve',
		11: 'cedo',
		12: 'depois',
		13: 'de manhã',
		14: 'de repente',
		15: 'de vez em quando',
		16: 'hoje',
		17: 'hoje em dia',
		18: 'já',
		19: 'logo',
		20: 'nunca',
		21: 'ontem',
		22: 'ora',
		23: 'outrora',
		24: 'quando',
		25: 'sempre',
		26: 'tarde',
		27: 'jamais',
	}
	return switcher_tempo.get(i, 'Seleção não disponível')


# adverbio_tempo_switcher(4)

def adverbio_negacao_switcher(i):
	#    i = int(input())

	switcher_negacao = {1: 'não', 2: 'nem', 3: 'tampouco', 4: 'nunca', 5: 'jamais'}
	return switcher_negacao.get(i, 'Seleção não disponível')


# adverbio_negacao_switcher(4)

def adverbio_relativo_switcher(i):
	#    i = int(input())

	switcher_relativo = {1: 'de onde', 2: 'quando', 3: 'onde',
	                     4: 'de quando', 5: 'que', 6: 'por onde'}
	return switcher_relativo.get(i, 'Seleção não disponível')


# adverbio_relativo_switcher(3)


def adverbio_afirmacao_switcher(i):
	#    i = int(input())

	switcher_afirmacao = {1: 'sim',
	                      2: 'deveras',
	                      3: 'indubitavelmente',
	                      4: 'decididamente',
	                      5: 'certamente',
	                      6: 'realmente',
	                      7: 'decerto',
	                      8: 'certo',
	                      9: 'efetivamente'
	                      }
	return switcher_afirmacao.get(i, 'Seleção não disponível')


# adverbio_afirmacao_switcher(5)


def adverbio_duvida_switcher(i):
	#    i = int(input())

	switcher_duvida = {1: 'possivelmente',
	                   2: 'provavelmente',
	                   3: 'acaso',
	                   4: 'porventura',
	                   5: 'quiçá',
	                   6: 'será',
	                   7: 'talvez',
	                   8: 'casualmente'}
	return switcher_duvida.get(i, 'Seleção não disponível')


# adverbio_duvida_switcher(3)
def adverbio(modo_insercao, tipo_de_adverbio, i):
	"""
    HHHH
    """
	#    modo_insercao = choice.Menu(['insercao_manual','insercao_menu']).ask()

	if modo_insercao == 'insercao_manual':
		tipo_de_adverbio = "NA"
		i = "NA"
		adverbio = input('Escreva o advérbio desejado:')

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Modo':

		adverbio = adverbio_modo_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Intensidade':

		adverbio = adverbio_intensidade_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Lugar':

		adverbio = adverbio_lugar_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Tempo':

		adverbio = adverbio_tempo_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Negacao':

		adverbio = adverbio_negacao_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Afirmacao':
		adverbio = adverbio_afirmacao_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Duvida':

		adverbio = adverbio_duvida_switcher(i)

	elif modo_insercao == 'insercao_menu' and tipo_de_adverbio == 'Adv_relativo':

		adverbio = adverbio_relativo_switcher(i)

	return adverbio


# adverbio("insercao_menu", "Modo", 2)

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
	return classe_verbo


# EXEMPLOS
# def_classe_de_verbo("Evento")
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


# experiencia_do_verbo2("correr")

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


# # deteccao_transitoriedade_do_verbo("ando")
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

def realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero=None, OI_tipo_de_pessoa=None,
                                          padrao_pessoa_morfologia=None):
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
	elif (padrao_de_morfologia == '-IR'):
		MI = 'ir'
	return MI


# realizacao_transitoriedade_infinitivo('-AR')


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
realizacao_transitoriedade_preterito_perfectivo_I('-IR', 'singular', '1pessoa')


###pretérito imperfectivo
# padrao_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
# OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
# OI_numero = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e numero.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
    'ei'
    '''
	if (
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ava'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
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

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
		MI = 'ias'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'unhas'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão':
		MI = 'ávamos'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == '3pessoa_do_singular'):
		MI = 'ia'

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural' and padrao_pessoa_morfologia == 'Morfologia_padrão'):
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
	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'
	):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ia'
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

	elif (
			padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural' or
			padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'
	):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'iam'

	elif (padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
		if padrao_pessoa_morfologia == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'unham'
	return MI


# realizacao_transitoriedade_preterito_imperfectivo('-IR', 'plural', '1pessoa')


def realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                       padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
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
		MI = 'éramos'

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


# realizacao_transitoriedade_preterito_perfectivo_II('-OR','plural','3pessoa')


def realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no passado volitivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I()
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
			MI = 'onha'
		else:
			MI = 'íssseis'

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
			MI = 'issem'

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
	if padrao_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		MI = 'ei'


	elif padrao_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		MI = 'i'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
		MI = 'onde'

	elif padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		MI = 'em'
		#
	elif (padrao_de_morfologia == '-ER' or '-IR') and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		MI = 'am'

	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
		MI = 'onham'
	elif (padrao_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural'):
		MI = 'ai'
	elif padrao_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		MI = 'onhamos'
	elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
		if padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR':
			MI = 'amos'
	elif padrao_de_morfologia == '-AR' and OI_numero == 'plural' and OI_tipo_de_pessoa == '1pessoa':
		MI = 'emos'

	elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
		if padrao_de_morfologia == '-AR' or padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR' or padrao_de_morfologia == '-OR':
			MI = 'Não há transitoriedade para imperativo_I na 1pessoa singular'

	elif padrao_de_morfologia == '-AR':
		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'e'
			else:
				MI = 'a'
		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			MI = 'e'

	elif padrao_de_morfologia == '-ER' or padrao_de_morfologia == '-IR':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '2pessoa' or OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'e'

	elif padrao_de_morfologia == '-OR':
		if OI_numero == 'singular':
			if OI_tipo_de_pessoa == '2pessoa' or OI_tipo_de_pessoa == '3pessoa':
				if padrao_pessoa_morfologia == '3pessoa_do_singular':
					MI = 'onha'
				else:
					MI = 'õe'

	elif padrao_de_morfologia == '-AR' and OI_numero == 'plural' and OI_tipo_de_pessoa == '1pessoa':
		MI = 'emos'

	return MI


# realizacao_transitoriedade_imperativo_I('-AR', 'plural', '2pessoa')
# realizacao_transitoriedade_imperativo_I('-OR', 'singular', '2pessoa')


#######imperativo_II (negativo)


def realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_II,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
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
		MI = 'Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida'

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


# realizacao_transitoriedade_gerundio('-IR')

######particípio


def realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa=None,
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
realizacao_transitoriedade_participio('-IR', 'plural', 'masculino')


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
# realizacao_transitoriedade_do_verbo('pretérito_perfectivo_I','-IR','plural',None,'1pessoa')
# realizacao_transitoriedade_do_verbo('pretérito_imperfectivo','-ER','plural',None,'2pessoa')
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


def formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia="Morfologia_padrão"):
	'''
    (str) -> str

    Retorna um verbo flexionado dados OE_experiencia_do_verbo,
    OI_orientacao_interpessoal_do_verbo.
    >>> formação_da_estrutura_do_verbo ()
    'levo'
    >>>formação_da_estrutura_do_verbo ()
    'levei'
    '''
	OE_experiencia_do_verbo = experiencia_do_verbo(verbo)
	OI_orientacao_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia,
	                                                                          OI_numero,
	                                                                          genero, OI_tipo_de_pessoa,
	                                                                          padrao_pessoa_morfologia)
	verbo = OE_experiencia_do_verbo + OI_orientacao_interpessoal_do_verbo
	return verbo


#
# formacao_da_estrutura_do_verbo('andar','presente','-AR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo('andar','pretérito_perfectivo_I','-AR','singular',None,'3pessoa')
# formacao_da_estrutura_do_verbo('comer','pretérito_imperfectivo','-ER','plural',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','subjuntivo_condicional','-OR','singular',None,'1pessoa')


#################
### FORMAÇÃO DOS VERBOS IRREGULARES

# VERBO agredir

def formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                           genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
	# if tipo_de_orientacao == 'OI_não_orientado':
	#     verbo = formação_verbo_agredir_não_orientado()
	# elif tipo_de_orientacao == 'OI_finito':
	#     verbo = formação_verbo_agredir_finito()
	# else:
	#     verbo = formação_verbo_agredir_não_finito()
	# return verbo

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


# formacao_verbo_agredir('agredir','particípio','-IR','plural','masculino',None)
# formacao_verbo_agredir('agredir','particípio','-IR','singular','masculino',None)
# formacao_verbo_agredir('agredir','gerúndio','-IR',None,None,None)
# formacao_verbo_agredir('agredir', 'infinitivo', '-IR', None, None, None)
# formacao_verbo_agredir('agredir', 'pretérito_perfectivo_II', '-IR', 'singular', None, '1pessoa')
# formacao_verbo_agredir('agredir','pretérito_imperfectivo','-IR','singular',None,'1pessoa')

# VERBO aferir


def formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
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
# formacao_verbo_aferir('aferir', 'não_finito_concretizado', '-IR', 'singular', None, '2pessoa')
# formacao_verbo_aferir('aferir', 'subjuntivo_optativo', '-IR', 'singular', None, '2pessoa')
# formacao_verbo_aferir('aferir', 'particípio', '-IR', 'singular', 'masculino', None)
# formacao_verbo_agredir('aferir','particípio','-IR','singular','feminino',None)


# VERBO MEDIR
def formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
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


#
# formacao_verbo_medir('medir','presente','-IR','singular',None,'2pessoa')
# formacao_verbo_medir('medir','presente','-IR','singular',None,'3pessoa')
# formacao_verbo_medir('medir','presente','-IR','singular',None,'1pessoa')

formacao_verbo_medir('medir', 'infinitivo', '-IR', 'singular', 'masculino', None)


# formacao_verbo_medir('medir','particípio','-IR','singular','feminino',None)
# formacao_verbo_medir('medir','gerúndio','-IR',None,None,None)


# VERBO SABER
def formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
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
# formacao_verbo_saber('saber', 'pretérito_imperfectivo', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'presente', '-ER', 'singular', None, '3pessoa')
# formacao_verbo_saber('saber', 'presente', '-ER', 'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'particípio', '-ER', 'singular', 'feminino', None)
# formacao_verbo_saber('saber', 'gerúndio', '-ER', None, None, None)
# formacao_verbo_saber('saber', 'não_finito_concretizado', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'futuro', '-ER', 'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'passado_volitivo', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'pretérito_perfectivo_I', '-ER', 'singular', None, '3pessoa')
# formacao_verbo_saber('saber', 'pretérito_perfectivo_II', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'subjuntivo_condicional', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_saber('saber', 'subjuntivo_conjuntivo', '-ER', 'plural', None, '3pessoa')
# formacao_verbo_saber('saber', 'imperativo_II', '-ER', 'singular', None, '1pessoa')
# formacao_verbo_saber('saber', 'imperativo_I', '-ER', 'singular', None, '2pessoa')


# VERBO ESTAR

def formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
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


# VERBO DIZER


def formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
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
				MI = 'em'
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
# ##TESTE dizer
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# ###
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'presente', '-ER', numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# #futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# #subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# #subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
#
# #subjuntivo_optativo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_II
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_dizer('dizer', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_dizer('dizer', 'infinitivo', '-ER', numero, 'feminino', None))
#
# # gerúndio
# print(formacao_verbo_dizer('dizer', 'gerúndio', '-ER', None, None, None))
#
# # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_dizer('dizer', 'particípio', '-ER', numero, genero, None))
#


##DEV INÍCIO


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
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
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
def formação_verbo_ir_não_finito():
	'''
    '''
	verbo = 'ir'
	tipo_de_orientacao = OI_nao_finito()

	if tipo_de_orientacao == 'subjuntivo_condicional':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()
		ME = 'f'

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):

			MI = 'osse'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'osse'
				verbo = ME + MI

			else:
				MI = 'osses'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'osse'
				verbo = ME + MI

			else:
				MI = 'ôssemos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'osse'
				verbo = ME + MI

			else:
				MI = 'ôsseis'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'osse'
				verbo = ME + MI

			else:
				MI = 'ossem'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			ME = 'v'
			MI = 'á'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI

			else:
				MI = 'ás'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI

			else:
				MI = 'amos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI

			else:
				MI = 'ades'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI

			else:
				MI = 'ão'
				verbo = ME + MI



	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado()
		verbo = ME + MI


	elif tipo_de_orientacao == 'imperativo_I':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			return 'Imperativos não selecionam 1pessoa do singular'


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			ME = 'v'
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI

			else:
				MI = 'ai'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = 'v'
			MI = 'á'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI
			else:
				MI = 'amos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = 'i'
			MI = 'de'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI
			else:
				MI = 'ão'
				verbo = ME + MI

	elif tipo_de_orientacao == 'imperativo_II':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()
		ME = 'v'

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			print('Imperativos não selecionam 1pessoa do singular')

		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI

			else:
				MI = 'ás'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':

			MI = 'á'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI
			else:
				MI = 'amos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI
			else:
				MI = 'ades'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'á'
				verbo = ME + MI
			else:
				MI = 'ão'
				verbo = ME + MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()
		ME = 'f'

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			MI = 'or'
			verbo = ME + MI

		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'or'
				verbo = ME + MI

			else:
				MI = 'ores'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'or'
				verbo = ME + MI
			else:
				MI = 'ormos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'or'
				verbo = ME + MI
			else:
				MI = 'ordes'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'or'
				verbo = ME + MI
			else:
				MI = 'orem'
				verbo = ME + MI

	return verbo
def formação_verbo_ir_finito():
	'''
    '''

	verbo = 'ir'
	tipo_de_orientacao = OI_finito()

	if tipo_de_orientacao == 'pretérito_imperfectivo':

		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo()
		verbo = MI

	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_futuro()
		verbo = ME + MI
	elif tipo_de_orientacao == 'passado_volitivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo()
		verbo = ME + MI

	elif tipo_de_orientacao == 'presente':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = 'v'
			MI = 'ou'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ai'
				verbo = ME + MI

			else:
				MI = 'ais'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = 'v'
			MI = 'ai'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ai'
				verbo = ME + MI

			else:
				MI = 'amos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = 'i'
			MI = 'des'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = 'v'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ai'
				verbo = ME + MI

			else:
				MI = 'am'
				verbo = ME + MI


	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = 'f'
			MI = 'ui'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oi'
				verbo = ME + MI

			else:
				MI = 'oste'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = 'f'
			MI = 'oi'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oi'
				verbo = ME + MI

			else:
				MI = 'omos'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oi'
				verbo = ME + MI

			else:
				MI = 'ostes'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'oi'
				verbo = ME + MI

			else:
				MI = 'oram'
				verbo = ME + MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			ME = 'f'
			MI = 'ora'
			verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ora'
				verbo = ME + MI

			else:
				MI = 'oras'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ora'
				verbo = ME + MI

			else:
				MI = 'ôramos'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ora'
				verbo = ME + MI

			else:
				MI = 'ôreis'
				verbo = ME + MI


		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = 'f'

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ora'
				verbo = ME + MI

			else:
				MI = 'oram'
				verbo = ME + MI

	return verbo

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
for numero in OI_numeros:
	for tipo_pessoa in OI_tipo_pessoas:
		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
#
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


# # # # # ##TESTE poder
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
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



###parei aqui


# VERBO FAZER
def formação_verbo_fazer():
	'''
    '''
	verbo = 'fazer'
	tipo_de_orientacao = choice.Menu(['OI_não_orientado', 'OI_finito', 'OI_não_finito']).ask()
	if tipo_de_orientacao == 'OI_não_orientado':
		verbo = formação_verbo_fazer_não_orientado()
	elif tipo_de_orientacao == 'OI_finito':
		verbo = formação_verbo_fazer_finito()
	else:
		verbo = formação_verbo_fazer_não_finito()
	return verbo


def formação_verbo_fazer_finito():
	verbo = 'fazer'
	tipo_de_orientacao = OI_finito()
	if tipo_de_orientacao == 'presente':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = 'ço'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-2)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = ''
				verbo = ME + MI
			else:
				MI = 'es'
				verbo = ME + MI
		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'az'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-2)]
			MI = 'emos'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]
			MI = 'azeis'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]
			MI = 'azem'
			verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'iz'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ez'
				verbo = ME + MI
			else:
				MI = 'izeste'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'ez'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ez'
				verbo = ME + MI

			else:
				MI = 'izemos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ez'
				verbo = ME + MI

			else:
				MI = 'izestes'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ez'
				verbo = ME + MI
			else:
				MI = 'izeram'
				verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'izera'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izera'
				verbo = ME + MI

			else:
				MI = 'izeras'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'izera'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izera'
				verbo = ME + MI

			else:
				MI = 'izéramos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izera'
				verbo = ME + MI
			else:
				MI = 'izéreis'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'ivera'
				verbo = ME + MI
			else:
				MI = 'izeram'
				verbo = ME + MI
	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo()
		verbo = ME + MI
	elif tipo_de_orientacao == 'futuro':
		ME = verbo[slice(-3)]
		MI = realizacao_transitoriedade_futuro()[slice(1, 5)]
		verbo = ME + MI
	elif tipo_de_orientacao == 'passado_volitivo':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()
		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'aria'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'aria'
				verbo = ME + MI
			else:
				MI = 'arias'
				verbo = ME + MI
		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]
			MI = 'aria'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]
			MI = 'aríamos'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]
			MI = 'aríeis'
			verbo = ME + MI
		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]
			MI = 'ariam'
			verbo = ME + MI

	return verbo


def formação_verbo_fazer_não_finito():
	verbo = 'fazer'
	tipo_de_orientacao = OI_nao_finito()

	if tipo_de_orientacao == 'subjuntivo_condicional':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			ME = verbo[slice(-4)]
			MI = 'izesse'
			verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izesse'
				verbo = ME + MI
			else:
				MI = 'izesses'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izesse'
				verbo = ME + MI

			else:
				MI = 'izéssemos'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izesse'
				verbo = ME + MI
			else:
				MI = 'izésseis'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'izesse'
				verbo = ME + MI

			else:
				MI = 'izessem'
				verbo = ME + MI
	elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			ME = verbo[slice(-3)]
			MI = 'a'
			verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'as'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'amos'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'ais'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'am'
				verbo = ME + 'ç' + MI
	elif tipo_de_orientacao == 'subjuntivo_optativo':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
				OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
			ME = verbo[slice(-4)]
			MI = 'er'
			verbo = ME + 'iz' + MI

		if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			ME = verbo[slice(-4)]
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'er'
				verbo = ME + 'iz' + MI
			else:
				MI = 'eres'
				verbo = ME + 'iz' + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'er'
				verbo = ME + 'iz' + MI

			else:
				MI = 'ermos'
				verbo = ME + 'iz' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'er'
				verbo = ME + 'iz' + MI

			else:
				MI = 'erdes'
				verbo = ME + 'iz' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-4)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'er'
				verbo = ME + 'iz' + MI

			else:
				MI = 'erem'
				verbo = ME + 'iz' + MI
	elif tipo_de_orientacao == 'imperativo_I':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			print('Imperativos não selecionam 1pessoa do singular. Seleciona novamente:')
			formação_verbo_fazer()

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			ME = verbo[slice(-3)]
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'z'
				verbo = ME + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = 'a'
			verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'amos'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'ei'
				verbo = ME + 'z' + MI


		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'am'
				verbo = ME + 'ç' + MI
	elif tipo_de_orientacao == 'imperativo_II':
		OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
		OI_numero = choice.Menu(['singular', 'plural']).ask()

		if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
			print('Imperativos não selecionam 1pessoa do singular. Selecione novamente:')
			formação_verbo_fazer()

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':

			ME = verbo[slice(-3)]
			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'as'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
			ME = verbo[slice(-3)]
			MI = 'a'
			verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'amos'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'ais'
				verbo = ME + 'ç' + MI

		elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
			ME = verbo[slice(-3)]

			if padrao_pessoa_morfologia == '3pessoa_do_singular':
				MI = 'a'
				verbo = ME + 'ç' + MI

			else:
				MI = 'am'
				verbo = ME + 'ç' + MI
	elif tipo_de_orientacao == 'não_finito_concretizado':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado()
		verbo = ME + 'az' + MI
	return verbo


def formação_verbo_fazer_não_orientado():
	verbo = 'fazer'
	tipo_de_orientacao = OI_nao_orientado()
	if tipo_de_orientacao == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo()
	elif tipo_de_orientacao == 'gerúndio':
		MI = realizacao_transitoriedade_gerúndio()
	elif tipo_de_orientacao == 'particípio':
		ME = verbo[slice(-4)]
		OI_numero = choice.Menu(['singular', 'plural']).ask()
		gênero = choice.Menu(['masculino', 'feminino']).ask()
		if OI_numero == 'singular' and gênero == 'feminino':
			MI = 'eita'
		elif OI_numero == 'plural' and gênero == 'feminino':
			MI = 'eitas'
		elif OI_numero == 'singular' and gênero == 'masculino':
			MI = 'eito'
		elif OI_numero == 'plural' and gênero == 'masculino':
			MI = 'eitos'
	verbo = ME + MI
	return verbo


#################################################################################

def realizacao_transitoriedade_do_verbo_nao_finito(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
                                        padrao_pessoa_morfologia="Morfologia_padrão"):
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo ()
    'o'

    '''
	tipo_de_orientacao = OI_nao_finito()

	if tipo_de_orientacao == 'subjuntivo_conjuntivo':
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(),
		return MI

	elif tipo_de_orientacao == 'subjuntivo_condicional':
		MI = realizacao_transitoriedade_subjuntivo_condicional()
		return MI

	elif tipo_de_orientacao == 'subjuntivo_optativo':
		MI = realizacao_transitoriedade_subjuntivo_optativo(),
		return MI

	elif tipo_de_orientacao == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado()
		return MI

	elif tipo_de_orientacao == 'imperativo_I':
		MI = realizacao_transitoriedade_imperativo_I()
		return MI

	elif tipo_de_orientacao == 'imperativo_II':
		MI = realizacao_transitoriedade_imperativo_II()
		return MI


def realizacao_transitoriedade_do_verbo_finito():
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo ()
    'o'

    '''

	tipo_de_orientacao = OI_finito()

	if tipo_de_orientacao == 'presente':
		MI = realizacao_transitoriedade_presente()
		return MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_I':
		MI = realizacao_transitoriedade_preterito_perfectivo_I()
		return MI

	elif tipo_de_orientacao == 'pretérito_perfectivo_II':
		MI = realizacao_transitoriedade_preterito_perfectivo_II()
		return MI

	elif tipo_de_orientacao == 'pretérito_imperfectivo':
		MI = realizacao_transitoriedade_preterito_imperfectivo()
		return MI

	elif tipo_de_orientacao == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo()
		return MI

	elif tipo_de_orientacao == 'futuro':
		MI = realizacao_transitoriedade_futuro()
		return MI


def realizacao_transitoriedade_do_verbo_não_orientado():
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo ()
    'o'

    '''
	tipo_de_orientação = OI_nao_orientado()

	if tipo_de_orientação == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo()

	elif tipo_de_orientação == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio()

	elif tipo_de_orientação == 'particípio':
		MI = realizacao_transitoriedade_participio()

	return MI


def formação_da_estrutura_do_verbo_lexical_finito():
	'''
    '''
	prompt = "Qual é o verbo lematizado desejado?"
	verbo = input(prompt)

	if verbo == 'estar':
		verbo = formação_verbo_estar_finito()
	elif verbo == 'ser':
		verbo = formação_verbo_ser_finito()
	elif verbo == 'ir':
		verbo = formação_verbo_ir_finito()
	elif (verbo == 'vir' or verbo == 'intervir'):
		verbo = formação_verbo_vir_intervir_finito()
	elif verbo == 'haver':
		verbo = formação_verbo_haver_finito()
	elif verbo == 'ter':
		verbo = formação_verbo_ter_finito()
	elif verbo == 'dizer':
		verbo = formação_verbo_dizer_finito()
	elif verbo == 'saber':
		verbo = formação_verbo_saber_finito()
	elif verbo == 'fazer':
		verbo = formação_verbo_fazer_finito()
	elif verbo == 'medir':
		verbo = formação_verbo_medir_finito()
	elif verbo == 'dever':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo_finito()
		verbo = ME + MI
	elif verbo == 'poder':
		verbo = formação_verbo_poder_finito()

	else:
		ME = (verbo[slice(-2)])
		MI = realizacao_transitoriedade_do_verbo_finito()
		verbo = ME + MI
	return verbo


def formação_da_estrutura_do_verbo_lexical_não_finito():
	'''
    '''

	verbo = input("Qual é o verbo lematizado desejado?")

	if verbo == 'estar':
		verbo = formação_verbo_estar_não_finito()
	elif verbo == 'ser':
		verbo = formação_verbo_ser_não_finito()
	elif verbo == 'ir':
		verbo = formação_verbo_ir_não_finito()
	elif verbo == 'vir' or verbo == 'intervir':
		verbo = formação_verbo_vir_intervir_não_finito()
	elif verbo == 'haver':
		verbo = formação_verbo_haver_não_finito()
	elif verbo == 'ter':
		verbo = formação_verbo_ter_não_finito()
	elif verbo == 'dizer':
		verbo = formação_verbo_dizer_não_finito()
	elif verbo == 'saber':
		verbo = formação_verbo_saber_não_finito()
	elif verbo == 'fazer':
		verbo = formação_verbo_fazer_não_finito()
	elif verbo == 'medir':
		verbo = formação_verbo_medir_não_finito()
	elif verbo == 'dever':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo_não_finito()
		verbo = ME + MI
	elif verbo == 'poder':
		verbo = formação_verbo_poder_não_finito()
	else:
		ME = (verbo[slice(-2)])
		MI = realizacao_transitoriedade_do_verbo_não_finito()
		verbo = ME + MI
	return verbo


def formação_da_estrutura_do_verbo_lexical():
	'''
    '''
	verbo = input("Qual é o verbo lematizado desejado?")
	# inserir verbos irregulares
	if verbo == 'estar':
		verbo = formação_verbo_estar()
	elif verbo == 'ser':
		verbo = formação_verbo_ser()
	elif verbo == 'ir':
		verbo = formacao_verbo_ir()
	elif (
			verbo == 'vir'
			or verbo == 'intervir'
	):
		verbo = formação_verbo_vir_intervir()
	elif verbo == 'haver':
		verbo = formação_verbo_haver()
	elif verbo == 'ter':
		verbo = formação_verbo_ter()
	elif verbo == 'dizer':
		verbo = formacao_verbo_dizer()
	elif verbo == 'saber':
		verbo = formacao_verbo_saber()
	elif verbo == 'fazer':
		verbo = formação_verbo_fazer()
	elif verbo == 'medir':
		verbo = formação_verbo_medir()
	elif verbo == 'dever':
		ME = verbo[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo()
		verbo = ME + MI
	elif verbo == 'poder':
		verbo = formação_verbo_poder()

	else:
		ME = (verbo[slice(-2)])
		MI = realizacao_transitoriedade_do_verbo_finito()
		verbo = ME + MI

	return verbo


def formação_da_estrutura_do_verbo_modal():
	'''
    '''
	print("Qual é o verbo modal lematizado desejado?")
	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver', 'ter(que/de)']).ask()

	if tipo_de_modal == 'dever':
		ME = tipo_de_modal[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo()
		verbo = ME + MI

	elif tipo_de_modal == 'poder':
		verbo = formação_verbo_poder()

	elif tipo_de_modal == 'haver':
		verbo = formação_verbo_haver()

	elif tipo_de_modal == 'ter(que/de)':
		verbo = formação_verbo_ter() + ' ' + choice.Menu(['de', 'que']).ask()

	return verbo


def formação_da_estrutura_do_verbo_auxiliar():
	'''
    '''
	print("Qual é o verbo auxiliar lematizado desejado?")
	tipo_de_auxiliar = choice.Menu(['estar', 'ter', 'ir', 'vir', 'ser', 'haver']).ask()

	if tipo_de_auxiliar == 'estar':
		verbo = formação_verbo_estar()

	elif tipo_de_auxiliar == 'ter':
		verbo = formação_verbo_ter()

	elif tipo_de_auxiliar == 'haver':
		verbo = formação_verbo_haver()

	elif tipo_de_auxiliar == 'ir':
		verbo = formacao_verbo_ir()

	elif tipo_de_auxiliar == 'vir':
		verbo = formação_verbo_vir_invervir()

	elif tipo_de_auxiliar == 'ser':
		verbo = formação_verbo_ser()

	return verbo


def formação_verbo_particípio():
	prompt = "Qual é o verbo lematizado desejado?"
	verbo = input(prompt)

	ME = verbo[slice(-2)]

	MI = realizacao_transitoriedade_particípio()
	verbo_particípio = ME + MI

	return verbo_particípio


def formação_verbo_gerúndio():
	prompt = "Qual é o verbo lematizado desejado?"
	verbo = input(prompt)

	ME = verbo[slice(-2)]

	MI = realizacao_transitoriedade_gerúndio()
	verbo_gerúndio = ME + MI

	return verbo_gerúndio


def formação_da_estrutura_do_verbo_modal_não_finito():
	'''
    '''
	print("Qual é o verbo modal lematizado desejado?")

	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()

	if tipo_de_modal == 'dever':
		ME = tipo_de_modal[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo_não_finito()
		verbo = ME + MI



	elif tipo_de_modal == 'poder':
		verbo = formação_verbo_poder_não_finito()


	elif tipo_de_modal == 'haver':
		verbo = formação_verbo_haver_não_finito()

	return verbo


def formação_da_estrutura_do_verbo_modal_finito():
	'''
    '''
	print("Qual é o verbo modal lematizado desejado?")

	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()

	if tipo_de_modal == 'dever':
		ME = tipo_de_modal[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo_finito()
		verbo = ME + MI



	elif tipo_de_modal == 'poder':
		verbo = formação_verbo_poder_finito()


	elif tipo_de_modal == 'haver':
		verbo = formação_verbo_haver_finito()

	return verbo


def formação_da_estrutura_do_verbo_auxiliar_finito():
	'''
    '''

	print("Qual é o verbo auxiliar lematizado desejado?")
	tipo_de_auxiliar = choice.Menu(['estar', 'ter', 'ir', 'vir', 'ser', 'haver']).ask()

	if tipo_de_auxiliar == 'estar':
		verbo = formação_verbo_estar_finito()


	elif tipo_de_auxiliar == 'ter':
		verbo = formação_verbo_ter_finito()


	elif tipo_de_auxiliar == 'haver':
		verbo = formação_verbo_haver_finito()


	elif tipo_de_auxiliar == 'ir':
		verbo = formação_verbo_ir_finito()

	elif tipo_de_auxiliar == 'vir':
		verbo = formação_verbo_vir_finito()

	elif tipo_de_auxiliar == 'ser':
		verbo = formação_verbo_ser_finito()

	return verbo


def formação_da_estrutura_do_verbo_auxiliar_não_finito():
	'''
    '''

	print("Qual é o verbo auxiliar lematizado desejado?")
	tipo_de_auxiliar = choice.Menu(['estar', 'ter', 'ir', 'vir', 'ser', 'haver']).ask()

	if tipo_de_auxiliar == 'estar':
		verbo = formação_verbo_estar_não_finito()


	elif tipo_de_auxiliar == 'ter':
		verbo = formação_verbo_ter_não_finito()


	elif tipo_de_auxiliar == 'haver':
		verbo = formação_verbo_haver_não_finito()


	elif tipo_de_auxiliar == 'ir':
		verbo = formação_verbo_ir_não_finito()

	elif tipo_de_auxiliar == 'vir':
		verbo = formação_verbo_vir_não_finito()

	elif tipo_de_auxiliar == 'ser':
		verbo = formação_verbo_ser_não_finito()

	return verbo


def formação_verbo_não_orientado():
	'''
    '''
	verbo = input('Qual é o verbo lematizado?')
	tipo_de_orientação = OI_nao_orientado()
	if verbo == 'vir':
		if tipo_de_orientação == 'gerúndio':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_gerúndio()
			verbo = ME + MI
		elif tipo_de_orientação == 'particípio':
			ME = verbo[slice(-2)]
			MI = 'indo'
			verbo = ME + MI
		elif tipo_de_orientação == 'infinitivo':
			verbo = verbo
	elif verbo == 'dizer':
		if tipo_de_orientação == 'gerúndio':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_gerúndio()
			verbo = ME + MI
		elif tipo_de_orientação == 'particípio':
			ME = verbo[slice(-4)]
			MI = 'ito'
			verbo = ME + MI
		elif tipo_de_orientação == 'infinitivo':
			verbo = verbo
	else:
		if tipo_de_orientação == 'gerúndio':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_gerúndio()
			verbo = ME + MI
		elif tipo_de_orientação == 'particípio':
			ME = verbo[slice(-2)]
			MI = realizacao_transitoriedade_particípio()
			verbo = ME + MI
		elif tipo_de_orientação == 'infinitivo':
			verbo = verbo
	return verbo


############################################################################


#####VERBOS MODAIS


def verbo_modal():
	print("Qual é o verbo modal lematizado desejado?")

	tipo_de_modal = input("""
                                      0:poder
                                      1:dever
                                      2:haver
                                      

                       Escolha uma opção:""")

	if tipo_de_modal == '0':
		return 'poder'

	elif tipo_de_modal == '1':
		return 'dever'

	elif tipo_de_modal == '2':
		return 'haver'


###########################################################################
#########################################################################

def verbo_geral():
	'''(str)->str
    Retorna a estrutura que realiza os verbos no português.
    '''
	print('Qual o tipo_pessoa de experiência')
	TIPO_DE_EXPERIÊNCIA = choice.Menu(['Ser', 'Fazer', 'Sentir']).ask()
	if TIPO_DE_EXPERIÊNCIA == 'Ser':
		print('Selecione um lema com experiência de Ser:')
		classe_do_verbo = def_classe_de_verbo()
		if classe_do_verbo == 'lexical':
			verbo = formação_da_estrutura_do_verbo_lexical()
		elif classe_do_verbo == 'modal':
			verbo = formação_da_estrutura_do_verbo_modal()
		elif classe_do_verbo == 'auxiliar':
			verbo = formação_da_estrutura_do_verbo_auxiliar()
	elif TIPO_DE_EXPERIÊNCIA == 'Fazer':
		print('Selecione um lema com experiência de Fazer:')
		classe_do_verbo = def_classe_de_verbo()
		if classe_do_verbo == 'lexical':
			verbo = formação_da_estrutura_do_verbo_lexical()
		elif classe_do_verbo == 'modal':
			verbo = formação_da_estrutura_do_verbo_modal()
		elif classe_do_verbo == 'auxiliar':
			verbo = formação_da_estrutura_do_verbo_auxiliar()
	else:
		print('Selecione um lema com experiência de Fazer:')
		classe_do_verbo = def_classe_de_verbo()
		if classe_do_verbo == 'lexical':
			verbo = formação_da_estrutura_do_verbo_lexical()
		elif classe_do_verbo == 'modal':
			verbo = formação_da_estrutura_do_verbo_modal()
		elif classe_do_verbo == 'auxiliar':
			verbo = formação_da_estrutura_do_verbo_auxiliar()

	return verbo


######ORDEM DO GRUPO#####
#    grupo verbal
def realizacao_de_TIPO_DE_EVENTO():
	'''
    '''
	print('Qual é o tipo_pessoa de evento?')
	TIPO_DE_EVENTO = choice.Menu(['ser', 'fazer', 'sentir']).ask()

	if TIPO_DE_EVENTO == 'ser':
		prompt = 'Qual é o verbo lematizado?'
		verbo = input(prompt)


	elif TIPO_DE_EVENTO == 'fazer':
		prompt = 'Qual é o verbo lematizado?'
		verbo = input(prompt)

	elif TIPO_DE_EVENTO == 'sentir':
		prompt = 'Qual é o verbo lematizado?'
		verbo = input(prompt)

	return verbo


def realizacao_de_AGÊNCIA():
	'''
    '''
	print('Qual de Agência?')
	AGÊNCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não-agenciado']).ask()

	if AGÊNCIA == 'agenciado_passiva':
		print('Qual o verbo auxiliar de agência passiva desejado?')
		auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()
		if auxiliar_da_passiva == 'ser':
			verbo_auxiliar_da_passiva = formação_verbo_ser()
			verbo_lexical = formação_verbo_particípio()
		elif auxiliar_da_passiva == 'estar':
			verbo_auxiliar_da_passiva = formação_verbo_ser()
			verbo_lexical = formação_verbo_particípio()

		grupo_verbal_agência_passiva = verbo_auxiliar_da_passiva + ' ' + verbo_lexical

		return grupo_verbal_agência_passiva

	elif AGÊNCIA == 'agenciado_ativa':

		grupo_verbal_agência_ativa = verbo_geral()
		return grupo_verbal_agência_ativa
	elif AGÊNCIA == 'não-agenciado':
		grupo_verbal_não_agenciado = verbo_geral()
		return grupo_verbal_não_agenciado


def realizacao_de_AGÊNCIA_passiva():
	'''
    '''

	print('Qual o verbo auxiliar de agência passiva desejado?')
	auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()
	if auxiliar_da_passiva == 'ser':
		verbo_auxiliar_da_passiva = formação_verbo_ser()
		verbo_lexical = formação_verbo_particípio()
	elif auxiliar_da_passiva == 'estar':
		verbo_auxiliar_da_passiva = formação_verbo_ser()
		verbo_lexical = formação_verbo_particípio()

	grupo_verbal_agência_passiva = verbo_auxiliar_da_passiva + ' ' + verbo_lexical

	return grupo_verbal_agência_passiva


# partindo do sistema

##para grupo verbal, fiz seleções nos sistemas de tempo secundário e agenciamento
# pq as outras seleções já são feitas na ordem da palavra verbal(ficaria redundante)


def grupo_verbal():
	'''()->str
    Retorna a estrutura que realiza o grupo verbal, dadas escolhas de
    tipo_pessoa DE EVENTO, AGÊNCIA, TEMPO SECUNDÁRIO, FINITUDE E ASPECTO.
    >>>grupo_verbal()
     'ando'
    >>>grupo_verbal()
     'estou andando'
    >>>grupo_verbal()
     'andava'
    '''
	print('Qual o tipo_pessoa de evento desejado para o grupo verbal?')
	TIPO_DE_EVENTO = choice.Menu(['Ser', 'Fazer', 'Sentir']).ask()

	if TIPO_DE_EVENTO == 'Ser' or TIPO_DE_EVENTO == 'Fazer' or TIPO_DE_EVENTO == 'Sentir':
		print('Selecione um lema verbal que realize o tipo_pessoa de evento desejado:')
		print('Qual a agência do GV?')
		AGÊNCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não_agenciado_passiva',
		                       'não_agenciado']).ask()

		if AGÊNCIA == 'agenciado_ativa' or AGÊNCIA == 'não_agenciado':
			print('Há a seleção de  tempo secundário')
			TEMPO_SECUNDÁRIO = choice.Menu(['-', '1_reiteração', '2_reiterações',
			                                '3_reiterações', '4_reiterações']).ask()

			if TEMPO_SECUNDÁRIO == '-':
				print('Dêixis modal = não_modalizada')
				print('Selecione a finitude')
				FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
				if FINITUDE == 'finito':
					print('Qual a dêixis temporal?')
					DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
					if DÊIXIS_TEMPORAL == 'presente':
						print('Selecione morfologia de presente e aspecto perfectivo:')
						grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
					elif DÊIXIS_TEMPORAL == 'passado':
						print('Qual o aspecto verbal?')
						ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
						if ASPECTO == 'perfectivo':
							print('Selecione morfologia de pretérito perfectivo:')
							grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
						else:
							print('Selecione morfologia de pretérito imperfectivo:')
							grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
					elif DÊIXIS_TEMPORAL == 'futuro':
						grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()

				elif FINITUDE == 'não-finito':
					grupo_verbal = formação_da_estrutura_do_verbo_lexical_não_finito()

				elif FINITUDE == 'não-orientado':
					print('Qual o aspecto verbal?')
					ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
					if ASPECTO == 'perfectivo':
						print('Verbo não orientado e perfectivo = particípio:')
						grupo_verbal = formação_verbo_particípio()

					elif ASPECTO == 'imperfectivo':
						print('Selecione o tipo_pessoa de OI não-orientação desejada')
						não_orientado = choice.Menu(['infinitivo', 'gerúndio'])

						if não_orientado == 'infinitivo':
							verbo = input('Qual o verbo lematizado?')
							grupo_verbal = verbo
						else:
							verbo = input('Qual o verbo lematizado?')
							if verbo == 'vir':
								ME = verbo[slice(-2)]
								MI = realizacao_transitoriedade_gerúndio()
								verbo = ME + MI
								grupo_verbal = verbo
							elif verbo == 'dizer':
								ME = verbo[slice(-2)]
								MI = realizacao_transitoriedade_gerúndio()
								verbo = ME + MI
								grupo_verbal = verbo
							else:
								ME = verbo[slice(-2)]
								MI = realizacao_transitoriedade_gerúndio()
								verbo = ME + MI
								grupo_verbal = verbo

			elif TEMPO_SECUNDÁRIO == '1_reiteração':
				print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
				      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
				      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal :')
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia do perfectivo:')
					print('Qual verbo ocupa a primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual verbo realiza o Evento?')
					Evento = verbo_geral()
				else:
					print('Selecione morfologia do imperfectivo:')
					print('Qual o verbo da primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual o verbo que realiza o Evento?')
					Evento = formação_da_estrutura_do_verbo_lexical()

				grupo_verbal = verbo1 + ' ' + Evento


			elif TEMPO_SECUNDÁRIO == '2_reiterações':
				print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
				      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
				      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia do perfectivo:')
					print('Qual verbo ocupa a primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual verbo ocupa a segunda posição no grupo?')
					verbo2 = verbo_geral()
					print('Qual verbo realiza o Evento?')
					Evento = verbo_geral()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + Evento

				else:
					print('Selecione morfologia do imperfectivo:')
					print('Qual verbo ocupa a primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual o verbo ocupa a segunda posição no grupo?')
					verbo2 = verbo_geral()
					print('Qual o verbo realiza o Evento?')
					Evento = verbo_geral()

				grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + Evento

			elif TEMPO_SECUNDÁRIO == '3_reiterações':
				print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
				      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
				      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia do perfectivo:')
					print('Qual verbo ocupa a primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual verbo ocupa a segunda posição no grupo?')
					verbo2 = verbo_geral()
					print('Qual verbo ocupa a terceira posição no grupo?')
					verbo3 = verbo_geral()
					print('Qual verbo realiza o Evento?')
					Evento = verbo_geral()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + Evento
				else:
					print('Selecione morfologia do imperfectivo:')
					print('Qual verbo ocupa a primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual o verbo ocupa a segunda posição no grupo?')
					verbo2 = verbo_geral()
					print('Qual verbo ocupa a terceira posição no grupo?')
					verbo3 = verbo_geral()
					print('Qual o verbo realiza o Evento?')
					Evento = verbo_geral()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + Evento

			elif TEMPO_SECUNDÁRIO == '4_reiterações':
				print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
				      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
				      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia do perfectivo:')
					print('Qual verbo ocupa a primeira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual verbo ocupa a segunda posição no grupo?')
					verbo2 = verbo_geral()
					print('Qual verbo ocupa a terceira posição no grupo?')
					verbo3 = verbo_geral()
					print('Qual verbo ocupa a quarta posição no grupo?')
					verbo4 = verbo_geral()
					print('Qual verbo realiza o Evento?')
					Evento = verbo_geral()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento
				else:
					print('Selecione morfologia do imperfectivo:')
					print('Qual verbo ocupa a primedefira posição no grupo?')
					verbo1 = verbo_geral()
					print('Qual o verbo ocupa a segunda posição no grupo?')
					verbo2 = verbo_geral()
					print('Qual verbo ocupa a terceira posição no grupo?')
					verbo3 = verbo_geral()
					print('Qual verbo ocupa a quarta posição no grupo?')
					verbo4 = verbo_geral()
					print('Qual o verbo realiza o Evento?')
					Evento = verbo_geral()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento


		####PASSIVA

		elif AGÊNCIA == 'agenciado_passiva' or AGÊNCIA == 'não_agenciado_passiva':
			print('Quantas reiterações de TEMPO SECUNDÁRIO?')
			TEMPO_SECUNDÁRIO = choice.Menu(['1_reiteração', '2_reiterações',
			                                '3_reiterações', '4_reiterações']).ask()
			print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas '
			      'de acordo com as seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
			      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem '
			      'o grupo verbal:')

			if TEMPO_SECUNDÁRIO == '1_reiteração':
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia de perfectivo:')
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbos_passiva
				else:
					print('Selecione morfologia de imperfectivo:')
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbos_passiva
			elif TEMPO_SECUNDÁRIO == '2_reiterações':
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia de perfectivo:')
					print('Qual verbo ocupa a primeira posição do grupo verbal?')
					verbo1 = verbo_geral()
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbo1 + ' ' + verbos_passiva
				else:
					print('Selecione morfologia de imperfectivo:')
					print('Qual verbo ocupa a primeira posição do grupo verbal?')
					verbo1 = verbo_geral()
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbo1 + ' ' + verbos_passiva
			elif TEMPO_SECUNDÁRIO == '3_reiterações':
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia de perfectivo:')
					print('Qual verbo ocupa a primeira posição do grupo verbal?')
					verbo1 = verbo_geral()
					print('Qual verbo ocupa a segunda posição do grupo verbal?')
					verbo2 = verbo_geral()
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbos_passiva
				else:
					print('Selecione morfologia de imperfectivo:')
					print('Qual verbo ocupa a primeira posição do grupo verbal?')
					verbo1 = verbo_geral()
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbos_passiva

			elif TEMPO_SECUNDÁRIO == '4_reiterações':
				print('Qual o aspecto verbal?')
				ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
				if ASPECTO == 'perfectivo':
					print('Selecione morfologia de perfectivo:')
					print('Qual verbo ocupa a primeira posição do grupo verbal?')
					verbo1 = verbo_geral()
					print('Qual verbo ocupa a segunda posição do grupo verbal?')
					verbo2 = verbo_geral()
					print('Qual verbo ocupa a terceira posição do grupo verbal?')
					verbo3 = verbo_geral()
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva
				else:
					print('Selecione morfologia de imperfectivo:')
					print('Qual verbo ocupa a primeira posição do grupo verbal?')
					verbo1 = verbo_geral()
					print('Qual verbo ocupa a segunda posição do grupo verbal?')
					verbo2 = verbo_geral()
					print('Qual verbo ocupa a terceira posição do grupo verbal?')
					verbo3 = verbo_geral()
					print('Selecione os verbo da passiva:')
					verbos_passiva = realizacao_de_AGÊNCIA_passiva()
					grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva

	return grupo_verbal


def grupo_conjuntivo():
	'''
    '''

	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()

	if modo_inserção == 'inserção_manual':
		conjunção = input('Escreva a conjunção desejada:')

	elif modo_inserção == 'inserção_menu':

		print('Qual o tipo_pessoa de conjunção?')
		tipo_de_conjunção = choice.Menu(['paratática(linker)', 'hipotática(binder)']).ask()

		if tipo_de_conjunção == 'paratática(linker)':
			print('Qual o tipo_pessoa da conjunção paratática(linker)?')
			tipo_de_paratática = choice.Menu(['Aditiva', 'Adversativa', 'Conclusiva',
			                                  'Alternativa',
			                                  'Explicativa']).ask()
			if tipo_de_paratática == 'Aditiva':
				conjunção = choice.Menu(['e', 'mas ainda', 'mas também', 'nem']).ask()

			elif tipo_de_paratática == 'Adversativa':
				conjunção = choice.Menu(['contudo', 'entretanto', 'mas',
				                         'não obstante', 'no entanto',
				                         'porém', 'todavia']).ask()

			elif tipo_de_paratática == 'Alternativa':  # PRECISO VER COMO IMPLEMENTAR UM COMPLEXO COM ESTE TIPO
				conjunção = choice.Menu(['já', 'ou', 'ora',
				                         'quer']).ask()

			elif tipo_de_paratática == 'Conclusiva':
				conjunção = choice.Menu(['assim', 'então', 'logo',
				                         'por conseguinte', 'por isso',
				                         'portanto']).ask()

			elif tipo_de_paratática == 'Explicativa':
				conjunção = choice.Menu(['pois', 'porquanto', 'porque',
				                         'que']).ask()

		elif tipo_de_conjunção == 'hipotática(binder)':
			print('Qual o tipo_pessoa da conjunção hipotática(binder)?')
			tipo_de_hipotática = choice.Menu(['Causal', 'Concessiva', 'Condicional',
			                                  'Conformativa', 'Final', 'Proporcional',
			                                  'Temporal', 'Comparativa', 'Consecutiva',
			                                  'Integrante', 'Relativa']).ask()

			if tipo_de_hipotática == 'Causal':
				conjunção = choice.Menu(['porque', 'pois', 'porquanto',
				                         'como', 'pois que', 'por isso que',
				                         'á que', 'uma vez que', 'visto que',
				                         'visto como', 'que']).ask()


			elif tipo_de_hipotática == 'Concessiva':
				conjunção = choice.Menu(['embora', 'conquanto', 'ainda que',
				                         'mesmo que', 'posto que', 'bem que',
				                         'se bem que', 'apesar de que', 'nem que',
				                         'que']).ask()


			elif tipo_de_hipotática == 'Condicional':
				conjunção = choice.Menu(['se', 'caso', 'quando',
				                         'conquanto que', 'salvo se', 'sem que',
				                         'dado que', 'desde que', 'a menos que',
				                         'a não ser que']).ask()


			elif tipo_de_hipotática == 'Conformativa':
				conjunção = choice.Menu(['conforme', 'como', ''
				                                             'segundo', 'consoante']).ask()

			elif tipo_de_hipotática == 'Final':
				conjunção = choice.Menu(['para que',
				                         'a fim de que', 'porque',
				                         'que']).ask()


			elif tipo_de_hipotática == 'Proporcional':
				conjunção = choice.Menu(['à medida que', 'ao passo que', 'à proporção que',
				                         'enquanto', 'quanto mais',
				                         'quanto menos']).ask()


			elif tipo_de_hipotática == 'Temporal':
				conjunção = choice.Menu(['quando', 'antes que',
				                         'depois que', 'até que', 'logo que',
				                         'sempre que', 'assim que', 'desde que',
				                         'todas as vezes que', 'cada vez que', 'apenas',
				                         'mal', 'desde que']).ask()

			elif tipo_de_hipotática == 'Comparativa':
				conjunção = choice.Menu(['mais que', 'mais do que',
				                         'menos que', 'maior que', 'menor que',
				                         'melhor que', 'pior que',
				                         'menos do que', 'maior do que',
				                         'menor do que', 'melhor do que',
				                         'pior do que']).ask()

			elif tipo_de_hipotática == 'Consecutiva':
				conjunção = choice.Menu(['De modo que', 'De maneira que']).ask()

			elif tipo_de_hipotática == 'Integrante':
				conjunção = choice.Menu(['que', 'se']).ask()

			elif tipo_de_hipotática == 'Relativa':
				conjunção = choice.Menu(['porque', 'pois', 'porquanto',
				                         'como', 'pois que', 'por isso que',
				                         'á que', 'uma vez que', 'visto que',
				                         'visto como', 'que']).ask()

	return conjunção


def conjunção_continuativa():
	'''
    '''
	print('Qual o modo de inserção da conjunção?')
	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()

	if modo_inserção == 'inserção_manual':
		conjunção_continuativa = input('Escreva o continuativo desejado:')

	elif modo_inserção == 'inserção_menu':
		print('Escolha um continuativo:')
		conjunção_continuativa = input("""
                                 1:e 
                                 2:é 
                                 3:ah 
                                 4:mas 
                                 5:sim 
                                 6:bem 
                                 7:não 
                                 8:agora 
                                 9:então 
                                 10:pois é 
                                 11:tipo_pessoa  
                                 12:tipo_pessoa assim 
                                 13:ó 
                                 14:daí
                                 15:aí
                                 16:aí então  
                                 17:quer 
                                 18:dizer 
                                 19:assim
                                 20:em
                                 21:seguida 
                                 22:por fim 
                                 23:porque 
                                 24:porém 
                                 25:também
                                 26:é que 
                                 27:olha 
                                 
                                 
                                
                               Escolha uma opção:""")

		if conjunção_continuativa == '1':
			conjunção_continuativa = 'e'
		elif conjunção_continuativa == '2':
			conjunção_continuativa = 'é'
		elif conjunção_continuativa == '3':
			conjunção_continuativa = 'ah'
		elif conjunção_continuativa == '4':
			conjunção_continuativa = 'mas'
		elif conjunção_continuativa == '5':
			conjunção_continuativa = 'sim'
		elif conjunção_continuativa == '6':
			conjunção_continuativa = 'bem'
		elif conjunção_continuativa == '7':
			conjunção_continuativa = 'não'
		elif conjunção_continuativa == '8':
			conjunção_continuativa = 'agora'
		elif conjunção_continuativa == '9':
			conjunção_continuativa = 'então'
		elif conjunção_continuativa == '10':
			conjunção_continuativa = 'pois é'
		elif conjunção_continuativa == '11':
			conjunção_continuativa = 'tipo'
		elif conjunção_continuativa == '12':
			conjunção_continuativa = 'tipo_pessoa assim '
		elif conjunção_continuativa == '13':
			conjunção_continuativa = 'ó'
		elif conjunção_continuativa == '14':
			conjunção_continuativa = 'daí'
		elif conjunção_continuativa == '15':
			conjunção_continuativa = 'aí'
		elif conjunção_continuativa == '16':
			conjunção_continuativa = 'aí então '
		elif conjunção_continuativa == '17':
			conjunção_continuativa = 'quer'
		elif conjunção_continuativa == '18':
			conjunção_continuativa = 'dizer'
		elif conjunção_continuativa == '19':
			conjunção_continuativa = 'assim'
		elif conjunção_continuativa == '20':
			conjunção_continuativa = 'em'
		elif conjunção_continuativa == '21':
			conjunção_continuativa = 'seguida'
		elif conjunção_continuativa == '22':
			conjunção_continuativa = 'por fim'
		elif conjunção_continuativa == '23':
			conjunção_continuativa = 'porque'
		elif conjunção_continuativa == '24':
			conjunção_continuativa = 'porém'
		elif conjunção_continuativa == '25':
			conjunção_continuativa = 'também'

		elif conjunção_continuativa == '26':
			conjunção_continuativa = 'é que'
		elif conjunção_continuativa == '27':
			conjunção_continuativa = 'olha'

	return conjunção_continuativa


###ESSE TRECHO QUE SEGUE É PRA GUARDAR PRO CASO DE PRECISAR FICAR MAIS ESPECÍFICO NO GRUPO_VERBAL
#
# print ('Quais tempos secundários?')
#        TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro', 'tempo_secundário_não_orientado']).ask()
#        compilação_TEMPORAL = []
#
#
#        while  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'tempo_secundário_DT_presente' or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_passado'or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_futuro' or TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_não_orientado':
#            compilação_TEMPORAL= [TEMPO_PRIMÁRIO,TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL]
#            TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro']).ask()
#            if TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'NA':
#                break
#
#
#        if AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '+':
#            grupo_verbal = verbo_geral () + ' ' + verbo_geral ()
#
#    return  grupo_verbal
#

# #####################################


######PALAVRAS NOMINAIS- SUBSTANTIVO


# NUMERATIVOS


#### A fazer para numerativos: Eu fiz apenas o de quantidade precisa absoluta ou
# cardinais. Ainda falta fazer as outras classes de numerativos. Talvez até a
# qualificação ainda faça os ordinais


def ordinal():
	'''
    '''
	num = str(input('Qual o número?'))
	print('Qual o gênero?')
	gênero = choice.Menu(['M', 'F']).ask()
	if gênero == 'M':
		ordinal = num + 'º'
	else:
		ordinal = num + 'ª'

	return ordinal


def porcento():
	'''
    '''

	num = str(input('Qual o número?'))

	porcento = num + '%'

	return porcento


def num_cardinal_1dig_extenso():
	número_extenso = input('Escreva o número cardinal de unidade por extenso:')

	if número_extenso == 'dois':
		gênero_do_numerativo = choice.Menu(['masculino', 'feminino']).ask()

		if gênero_do_numerativo == 'feminino':

			numerativo = número_extenso[slice(-3)] + 'uas'

		elif gênero_do_numerativo == 'masculino':
			numerativo = número_extenso
	elif número_extenso == 'um':
		gênero_do_numerativo = choice.Menu(['masculino', 'feminino']).ask()

		if gênero_do_numerativo == 'feminino':

			numerativo = número_extenso + 'a'

		elif gênero_do_numerativo == 'masculino':
			numerativo = número_extenso
	else:
		numerativo = número_extenso

	return numerativo


def num_cardinal_2dig_extenso():
	número_extenso = input('Escreva o número cardinal de dezena por extenso:')

	numerativo = número_extenso

	return numerativo


def num_cardinal_3dig_extenso():
	número_extenso = input('Escreva o número cardinal de centena por extenso:')

	if (número_extenso == 'duzentos' or número_extenso == 'trezentos' or
			número_extenso == 'quatrocentos' or número_extenso == 'quinhentos' or
			número_extenso == 'seiscentos' or número_extenso == 'setecentos' or
			número_extenso == 'oitocentos' or número_extenso == 'novecentos'):

		gênero_do_numerativo = choice.Menu(['masculino', 'feminino']).ask()

		if gênero_do_numerativo == 'feminino':

			numerativo = número_extenso[slice(-2)] + 'as'

		elif gênero_do_numerativo == 'masculino':
			numerativo = número_extenso
	elif número_extenso == 'cem':
		numerativo = número_extenso

	return numerativo


def num_cardinal_4dig_extenso():  # Número com 4 dígitos
	número_extenso = input('Escreva o número cardinal de milhar por extenso:')

	if número_extenso == 'dois mil':
		gênero_do_numerativo = choice.Menu(['masculino', 'feminino']).ask()

		if gênero_do_numerativo == 'masculino':

			numerativo = número_extenso

		elif gênero_do_numerativo == 'feminino':

			numerativo = número_extenso[:1] + 'uas' + número_extenso[4:]

	else:
		numerativo = número_extenso

	return numerativo


def num_cardinal_5dig_extenso():  # Número com 5 dígitos
	número_extenso = input('Escreva o número cardinal de milhar de cinco dígitos por extenso:')

	numerativo = número_extenso

	return numerativo


def num_cardinal_6dig_extenso():  # Número com 6 dígitos

	número_extenso = input('Escreva o número cardinal de seis dígitos por extenso:')

	if (número_extenso == 'duzentos mil' or número_extenso == 'trezentos mil' or
			número_extenso == 'quatrocentos mil' or número_extenso == 'quinhentos mil' or
			número_extenso == 'seiscentos mil' or número_extenso == 'setecentos mil' or
			número_extenso == 'oitocentos mil' or número_extenso == 'novecentos mil'):

		gênero_do_numerativo = choice.Menu(['masculino', 'feminino']).ask()

		if gênero_do_numerativo == 'feminino':

			numerativo = número_extenso[slice(-6)] + 'as mil'

		elif gênero_do_numerativo == 'masculino':
			numerativo = número_extenso

	return numerativo


def num_cardinal():
	print('Numeral por extenso ou numérico?')
	realizacao_cardinal = choice.Menu(['extenso', 'numérico']).ask()
	print('Quantos dígitos tem o número?')
	dígitos = choice.Menu(['1', '2', '3', '4', '5', '6', ]).ask()

	if (realizacao_cardinal == 'numérico' and dígitos == '1' or
			realizacao_cardinal == 'numérico' and dígitos == '2' or
			realizacao_cardinal == 'numérico' and dígitos == '3' or
			realizacao_cardinal == 'numérico' and dígitos == '4'):

		num_cardinal = input('Escreva o número cardinal ')

	elif (realizacao_cardinal == 'extenso' and dígitos == '1'):

		num_cardinal = num_cardinal_1dig_extenso()

	elif (realizacao_cardinal == 'extenso' and dígitos == '2'):

		print('A dezena é inteira ou tem unidades?')
		composição_num_2dig = choice.Menu(['dezena_inteira', 'dezena+unidade']).ask()

		if composição_num_2dig == 'dezena_inteira':

			num_cardinal = num_cardinal_2dig_extenso()

		else:

			num_cardinal = num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()

	elif (realizacao_cardinal == 'extenso' and dígitos == '3'):

		print('Centena inteira, centena + dezena inteira, ou centena + dezena + unidade?')
		composição_num_3dig = choice.Menu(
			['centena_inteira', 'centena+dezena_inteira', 'centena+dezena+unidade', 'centena+unidade']).ask()

		if composição_num_3dig == 'centena_inteira':

			num_cardinal = num_cardinal_3dig_extenso()

		elif composição_num_3dig == 'centena+dezena_inteira':

			centena = num_cardinal_3dig_extenso()

			if centena == 'cem':

				centena = centena[slice(-2)] + 'ento'

				num_cardinal = centena + ' e ' + num_cardinal_2dig_extenso()

			else:
				num_cardinal = centena + ' e ' + num_cardinal_2dig_extenso()

		elif composição_num_3dig == 'centena+dezena+unidade':

			centena = num_cardinal_3dig_extenso()
			if centena == 'cem':
				centena = centena[slice(-2)] + 'ento'
				num_cardinal = centena + ' e ' + num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()
			else:
				num_cardinal = centena + ' e ' + num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()

		elif composição_num_3dig == 'centena+unidade':
			centena = num_cardinal_3dig_extenso()

			if centena == 'cem':
				centena = centena[slice(-2)] + 'ento'
				num_cardinal = centena + ' e ' + num_cardinal_1dig_extenso()
			else:
				num_cardinal = centena + ' e ' + num_cardinal_1dig_extenso()

	elif (realizacao_cardinal == 'extenso' and dígitos == '4'):

		print('Escolha a composição do número:')
		composição_num_4dig = choice.Menu(['milhar_inteira',
		                                   'milhar+unidade',
		                                   'milhar+dezena_inteira',
		                                   'milhar+dezena+unidade',
		                                   'milhar+centena_inteira',
		                                   'milhar+centena+dezena_inteira',
		                                   'milhar+centena+dezena+unidade']).ask()

		if composição_num_4dig == 'milhar_inteira':

			num_cardinal = num_cardinal_4dig_extenso()

		elif composição_num_4dig == 'milhar+unidade':

			num_cardinal = num_cardinal_4dig_extenso() + ' e ' + num_cardinal_1dig_extenso()

		elif composição_num_4dig == 'milhar+dezena_inteira':

			num_cardinal = num_cardinal_4dig_extenso() + ' e ' + num_cardinal_2dig_extenso()

		elif composição_num_4dig == 'milhar+dezena+unidade':
			num_cardinal = num_cardinal_4dig_extenso() + ' e ' + num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()

		elif composição_num_4dig == 'milhar+centena_inteira':
			num_cardinal = num_cardinal_4dig_extenso() + ' e ' + num_cardinal_3dig_extenso()

		elif composição_num_4dig == 'milhar+centena+dezena_inteira':
			milhar = num_cardinal_4dig_extenso()
			centena = num_cardinal_3dig_extenso()
			if centena == 'cem':
				centena = centena[slice(-2)] + 'ento'
			dezena = num_cardinal_2dig_extenso()

			num_cardinal = milhar + ' ' + centena + ' e ' + dezena

		elif composição_num_4dig == 'milhar+centena+dezena+unidade':

			milhar = num_cardinal_4dig_extenso()
			centena = num_cardinal_3dig_extenso()
			if centena == 'cem':
				centena = centena[slice(-2)] + 'ento'

			dezena = num_cardinal_2dig_extenso()

			unidade = num_cardinal_1dig_extenso()

			num_cardinal = milhar + ' ' + centena + ' e ' + dezena + ' e ' + unidade

	return num_cardinal


def Numerativo():
	'''
    '''
	print('Há realizacao de Numerativo?')
	real_numerativo = choice.Menu(['sim', 'NA']).ask()

	if real_numerativo == 'NA':
		Numerativo = ''
	elif real_numerativo == 'sim':
		print('Qual o tipo_pessoa de Numerativo selecionado')
		função_Numerativo = choice.Menu(['quant_precisa_absoluta(cardinais)',
		                                 'quant_precisa_div/multi(fração/multiplicativos)',
		                                 'quant_imprecisa_pron_indef_numer',
		                                 'quant_imprecisa_pron_indef_valor_alt_baixo',
		                                 'ordem_lugar_preciso(ordinal)',
		                                 'ordem_lugar_impreciso(posição_relativa'
		                                 ]).ask()

		if função_Numerativo == 'ordem_lugar_preciso(ordinal)':
			Numerativo = ordinal()

		elif função_Numerativo == 'quant_precisa_div/multi(fração/multiplicativos)':
			print('Qual o tipo?')
			tipo_precisa = choice.Menu(['porcentagem']).ask()

			if tipo_precisa == 'porcentagem':
				Numerativo = porcento()

		elif função_Numerativo == 'quant_precisa_absoluta(cardinais)':
			Numerativo = num_cardinal()
		elif função_Numerativo == 'quant_imprecisa_pron_indef_numer':
			print("""
                    1: 'algum'
                    2: 'nenhum'
                    3: 'todo'
                    4: 'muito'
                    5: 'pouco'
                    6: 'vário'
                    7: 'tanto'
                    8: 'outro'
                    9: 'quanto'
                    10: 'alguma'
                    11: 'nenhuma'
                    12: 'toda'
                    13: 'muita'
                    14: 'pouca'
                    15: 'vária'
                    16: 'tanta'
                    17:'outra'
                    18: 'quanta'
                    19:'alguns'
                    20:'nenhuns'
                    21:'todos'
                    22:'muitos'
                    23:'poucos'
                    24:'vários'
                    25:'tantos'
                    26:'outros'
                    27:'quantos'
                    28:'algumas'
                    29:'nenhumas'
                    30:'todas'
                    31:'muitas'
                    32:'poucas'
                    33:'várias'
                    34:'tantas'
                    35:'outras'
                    36:'quantas'    

                               Escolha uma opção:""")

			Numerativo = NumerativoIndefinidoSwitcher()

	return Numerativo


def NumerativoIndefinidoSwitcher():
	i = int(input())

	switcherNumInd = {
		1: 'algum',
		2: 'nenhum',
		3: 'todo', \
		4: 'muito',
		5: 'pouco',
		6: 'vário',
		7: 'tanto',
		8: 'outro',
		9: 'quanto',
		10: 'alguma',
		11: 'nenhuma',
		12: 'toda',
		13: 'muita',
		14: 'pouca',
		15: 'vária',
		16: 'tanta',
		17: 'outra',
		18: 'quanta',
		19: 'alguns',
		20: 'nenhuns',
		21: 'todos',
		22: 'muitos',
		23: 'poucos',
		24: 'vários',
		25: 'tantos',
		26: 'outros',
		27: 'quantos',
		28: 'algumas',
		29: 'nenhumas',
		30: 'todas',
		31: 'muitas',
		32: 'poucas',
		33: 'várias',
		34: 'tantas',
		35: 'outras',
		36: 'quantas',
	}

	return switcherNumInd.get(i, 'Seleção nao disponível')


#

###A palavra nominal que realiza o Ente no GRUPO NOMINAL- Flexiona para nos eixos:
#     Gênero, Número, Grau. Por enquanto, vou trabalhar apenas com Gênero e número.(ORDEM DA PALAVRA AINDA)
# COMECEI APENAS COM SUBSTANTIVOS QUE SÃO REGULARES NAS SUAS FLEXÕES: gato:gatos:gatas:

def detecção_experiência_do_substantivo():  ##dado o substantivo flexionado##
	'''(str,str,str)->

    Retorna o morfema que realiza a experiência em um substantivo, dados
    o substantivo flexionado, o gênero e o número.

    >>>detecção_experiência_do_substantivo ('', 'masculino', 'plural')
    'gat'
    '''
	raiz_experiencial_substantivo = ''
	substantivo = input('Qual é o substantivo?')
	gênero = choice.Menu(['masculino', 'feminino']).ask()
	número = choice.Menu(['singular', 'plural']).ask()

	if gênero == 'masculino' and número == 'singular':
		raiz_experiencial_substantivo = (substantivo[slice(-1)])
		return raiz_experiencial_substantivo

	elif gênero == 'feminino' and número == 'singular':
		raiz_experiencial_substantivo = (substantivo[slice(-1)])
		return raiz_experiencial_substantivo

	elif gênero == 'masculino' and número == 'plural':
		raiz_experiencial_substantivo = (substantivo[slice(-2)])
		return raiz_experiencial_substantivo

	elif gênero == 'feminino' and número == 'plural':
		raiz_experiencial_substantivo = (substantivo[slice(-2)])
		return raiz_experiencial_substantivo


# OS LEMAS QUE SERVIRÃO PARA  FUNÇÃO QUE SEGUE VIRÃO DA ANOTAÇÃO NA ONTOLOGIA:
#        o que na ontologia tiver anotado como Thing, vai servir como um
##        banco lexical do qual o operador vai selecionar(não sei ainda se
#        vai ser importado automaticamente ou se vou ter de inserir manualmente
#        )


def realizacao_experiência_do_substantivo():  ##dado o substantivo_lematizado- por enquanto, apenas para
	##substantivos regulares, com foco em masculino-feminino, singular plural. Tenho que considerar desenvolver
	#    com relação aos diferentes tipos de radicais (primitivo, derivado, composto, simples...)
	'''(str)-> str

    Retorna o morfema que realiza a experiência em um substantivo, dado
    o substantivo lematizado.

    >>>realizacao_experiência_do_substantivo ()
    'gat'
    '''
	flexão_gênero_potencial = choice.Menu(['masculino/feminino', 'não_binário']).ask()
	substantivo_lematizado = input('Qual é o substantivo lematizado?')

	if flexão_gênero_potencial == 'masculino/feminino':
		morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]

	elif flexão_gênero_potencial == 'não_binário':
		morfema_experiencial_do_substantivo = substantivo_lematizado

	return morfema_experiencial_do_substantivo


def realizacao_flexões_substantivos():
	'''(str,str,str)->

    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do substantivo e os gênero e números desejados.

    >>>realizacao_flexões_substantivos ('', '', '')
    'os'
    '''
	gênero = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()
	número = choice.Menu(['singular', 'plural']).ask()
	if gênero == 'masculino' and número == 'singular':
		morfema_flexão_substantivo = 'o'
	elif gênero == 'feminino' and número == 'singular':
		morfema_flexão_substantivo = 'a'
	elif gênero == 'masculino' and número == 'plural':
		morfema_flexão_substantivo = 'os'
	elif gênero == 'feminino' and número == 'plural':
		morfema_flexão_substantivo = 'as'
	elif gênero == 'não_binário' and número == 'singular':
		morfema_flexão_substantivo = ''
	elif gênero == 'não_binário' and número == 'plural':
		morfema_flexão_substantivo = 's'

	return morfema_flexão_substantivo


###Com relação aos substantivos comuns tenho que ver a abordagem que vou tomar
# com relação aos substantivos não binários, ou inerentemente masculinos ou femininos. Me parece
# que o sistema se organiza a realizar o gênero em alguns casos na ordem da palavra, e em
# outros casos na ordem do grupo (mesa: não parece ter uma contrapartida masculina)


def formação_da_estrutura_do_substantivo_comum():
	'''(str, str)-str

    Retorna a realizacao de um substantivo comum dados a experiência_do_substantivo
    e as flexões_desejadas.

    >>>formação_da_estrutura_do_substantivo_comum ()

    '''
	substantivo_lematizado = input('Qual é o substantivo lematizado?')

	if substantivo_lematizado[-1:] == 'm':
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexão_substantivo = 'ns'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

	elif substantivo_lematizado[-2:] == 'or':
		print('Qual o gênero')
		flexão_gênero_potencial = choice.Menu(['masculino', 'feminino']).ask()
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if flexão_gênero_potencial == 'masculino' and número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif flexão_gênero_potencial == 'feminino' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'masculino' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'feminino' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


		elif flexão_gênero_potencial == 'não_binário' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'não_binário' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 's'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
	elif substantivo_lematizado[-2:] == 'ão':
		print('Qual o gênero')
		flexão_gênero_potencial = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()
		if (flexão_gênero_potencial == 'masculino' and número == 'singular'
				or flexão_gênero_potencial == 'não_binário' and número == 'singular'):
			substantivo_comum = substantivo_lematizado
		elif flexão_gênero_potencial == 'feminino' and número == 'singular':
			print('Escolha o tipo_pessoa de feminino:')
			tipo_feminino = choice.Menu(['oa', 'ona', 'ã', 'esa', 'casos_exceção']).ask()
			if (tipo_feminino == 'oa' or tipo_feminino == 'ona' or tipo_feminino == 'ã' or
					tipo_feminino == 'esa'):
				morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
				substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino
			else:
				substantivo_comum = input('Dê entrada manual do substantivo comum')

		elif (flexão_gênero_potencial == 'masculino' and número == 'plural'
		      or flexão_gênero_potencial == 'não_binário' and número == 'plural'):
			print('Escolha o tipo_pessoa de plural:')
			tipo_ão = choice.Menu(['ãos', 'ões', 'ães']).ask()
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			substantivo_comum = morfema_experiencial_do_substantivo + tipo_ão
		elif flexão_gênero_potencial == 'feminino' and número == 'plural':
			print('Escolha o tipo_pessoa de feminino:')
			tipo_feminino = choice.Menu(['oa', 'ona', 'ã', 'esa', 'casos_exceção']).ask()
			if (tipo_feminino == 'oa' or tipo_feminino == 'ona' or tipo_feminino == 'ã' or
					tipo_feminino == 'esa'):
				morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
				substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino + 's'
			else:
				substantivo_comum = input('Dê entrada manual do substantivo comum')

	elif substantivo_lematizado[-1:] == 'x':
		substantivo_comum = substantivo_lematizado

	elif substantivo_lematizado[-1:] == 's':
		tonicidade = choice.Menu(['oxítona', 'paroxítona', 'proparoxítona']).ask()

		if tonicidade == 'paroxítona':
			substantivo_comum = substantivo_lematizado
		elif tonicidade == 'oxítona':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_número = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_número


	elif (substantivo_lematizado[-1:] == 'r' or substantivo_lematizado[-1:] == 'z'):
		print('Qual o gênero')
		flexão_gênero_potencial = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if flexão_gênero_potencial == 'masculino' and número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif flexão_gênero_potencial == 'feminino' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


		elif flexão_gênero_potencial == 'masculino' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'feminino' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


		elif flexão_gênero_potencial == 'não_binário' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'não_binário' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 'es'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

	elif substantivo_lematizado[-2:] == 'al':
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexão_substantivo = 'ais'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

	elif substantivo_lematizado[-2:] == 'el':
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexão_substantivo = 'éis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

	elif substantivo_lematizado[-2:] == 'il':
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexão_substantivo = 'is'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


	elif substantivo_lematizado[-2:] == 'ol':
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexão_substantivo = 'óis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


	elif substantivo_lematizado[-2:] == 'ul':
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if número == 'singular':

			substantivo_comum = substantivo_lematizado

		elif número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
			morfema_flexão_substantivo = 'úis'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


	else:
		print('Qual o gênero')
		flexão_gênero_potencial = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()
		print('Qual o número')
		número = choice.Menu(['singular', 'plural']).ask()

		if flexão_gênero_potencial == 'masculino' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexão_substantivo = 'o'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'feminino' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexão_substantivo = 'a'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'masculino' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexão_substantivo = 'os'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'feminino' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
			morfema_flexão_substantivo = 'as'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


		elif flexão_gênero_potencial == 'não_binário' and número == 'singular':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = ''
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

		elif flexão_gênero_potencial == 'não_binário' and número == 'plural':
			morfema_experiencial_do_substantivo = substantivo_lematizado
			morfema_flexão_substantivo = 's'
			substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

	return substantivo_comum


# ADJETIVOS

def detecção_experiência_do_adjetivo():  ##dado o adjetivo flexionado##
	'''(str,str,str)->

    Retorna o morfema que realiza a experiência em um adjetivo, dados
    o adjetivo flexionado, o gênero e o número.

    >>>detecção_experiência_do_adjetivo ('', 'masculino', 'plural')
    'esportiv'
    '''
	raiz_experiencial_adjetivo = ''
	adjetivo = input('Qual é o adjetivo?')
	gênero = choice.Menu(['masculino', 'feminino']).ask()
	número = choice.Menu(['singular', 'plural']).ask()

	if gênero == 'masculino' and número == 'singular':
		raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
		return raiz_experiencial_adjetivo

	elif gênero == 'feminino' and número == 'singular':
		raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
		return raiz_experiencial_adjetivo

	elif gênero == 'masculino' and número == 'plural':
		raiz_experiencial_adjetivo = (adjetivo[slice(-2)])
		return raiz_experiencial_adjetivo

	elif gênero == 'feminino' and número == 'plural':
		raiz_experiencial_adjetivo = (adjetivo[slice(-2)])
		return raiz_experiencial_adjetivo


def realizacao_experiência_do_adjetivo():
	'''(str)-> str

    Retorna o morfema que realiza a experiência em um adjetivo, dado
    o adjetivo lematizado.

    >>>realizacao_experiência_do_adjetivo ()
    'gat'
    '''
	flexão_gênero_potencial = choice.Menu(['masculino/feminino', 'não_binário']).ask()
	adjetivo_lematizado = input('Qual é o adjetivo lematizado?')

	if flexão_gênero_potencial == 'masculino/feminino':
		morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]

	elif flexão_gênero_potencial == 'não_binário':
		morfema_experiencial_do_adjetivo = adjetivo_lematizado

	return morfema_experiencial_do_adjetivo


def realizacao_flexões_adjetivos():
	'''(str,str,str)->

    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do adjetivo e os gênero e números desejados.

    >>>realizacao_flexões_adjetivos ('', '', '')
    'os'
    '''

	gênero = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()
	número = choice.Menu(['singular', 'plural']).ask()

	if gênero == 'masculino' and número == 'singular':
		morfema_flexão_adjetivo = 'o'


	elif gênero == 'feminino' and número == 'singular':
		morfema_flexão_adjetivo = 'a'


	elif gênero == 'masculino' and número == 'plural':
		morfema_flexão_adjetivo = 'os'


	elif gênero == 'feminino' and número == 'plural':
		morfema_flexão_adjetivo = 'as'


	elif gênero == 'não_binário' and número == 'singular':
		morfema_flexão_adjetivo = ''

	elif gênero == 'não_binário' and número == 'plural':
		morfema_flexão_adjetivo = 's'

	return morfema_flexão_adjetivo


def adjetivo_modificador():
	'''(str, str)-str

    Retorna a realizacao de um adjetivo comum dados a experiência_do_adjetivo
    e as flexões_desejadas.

    >>>estrutura_do_adjetivo ()

    '''
	print('Há realizacao de adjetivo com funções de modificação (class, epítetos)?')
	real_modificadores = choice.Menu(['sim', 'NA']).ask()

	if real_modificadores == 'NA':

		modificador = ''

	else:

		adjetivo_lematizado = input('Qual é o adjetivo lematizado?')
		flexão_gênero_potencial = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()
		número = choice.Menu(['singular', 'plural']).ask()

		if flexão_gênero_potencial == 'masculino' and número == 'singular':
			morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
			morfema_flexão_adjetivo = 'o'
			modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo

		elif flexão_gênero_potencial == 'feminino' and número == 'singular':
			morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
			morfema_flexão_adjetivo = 'a'
			modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo

		elif flexão_gênero_potencial == 'masculino' and número == 'plural':
			morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
			morfema_flexão_adjetivo = 'os'
			modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo

		elif flexão_gênero_potencial == 'feminino' and número == 'plural':
			morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
			morfema_flexão_adjetivo = 'as'
			modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo


		elif flexão_gênero_potencial == 'não_binário' and número == 'singular':
			morfema_experiencial_do_adjetivo = adjetivo_lematizado
			morfema_flexão_adjetivo = ''
			modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo

		elif flexão_gênero_potencial == 'não_binário' and número == 'plural':
			morfema_experiencial_do_adjetivo = adjetivo_lematizado
			morfema_flexão_adjetivo = 's'
			modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo

	return modificador


# PRONOMES#

# PEGUEI OS PRONOMES BÁSICOS# QUANDO CHEGAR NA ORAÇÃO, A MORFOLOGIA DOS VERBOS
# FICA UM POUCO SUBVERSIVA

def realizacao_pronominal_casoreto():
	'''(str)->str
    Retorna o pronome adequado dado uma pessoa da intelocução.

    >>>realizacao_pronominal_casoreto ('','')
    'eu'
    '''
	pessoa_da_interlocução = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
	número = choice.Menu(['singular', 'plural']).ask()

	if pessoa_da_interlocução == 'falante' and número == 'singular':
		pronome_pessoal_reto = 'eu'
		return pronome_pessoal_reto

	elif pessoa_da_interlocução == 'ouvinte' and número == 'singular':
		morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_reto = 'tu'
		else:
			pronome_pessoal_reto = 'você'

	elif pessoa_da_interlocução == 'não_interlocutor' and número == 'singular':
		gênero = choice.Menu(['masculino', 'feminino']).ask()
		if gênero == 'masculino':
			pronome_pessoal_reto = 'ele'

		else:
			pronome_pessoal_reto = 'ela'

	elif pessoa_da_interlocução == 'falante' and número == 'plural':
		pronome_pessoal_reto = 'nós'

	elif pessoa_da_interlocução == 'ouvinte' and número == 'plural':
		morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_reto = 'vós'
		else:
			pronome_pessoal_reto = 'vocês'

	elif pessoa_da_interlocução == 'não_interlocutor' and número == 'plural':
		gênero = choice.Menu(['masculino', 'feminino']).ask()
		if gênero == 'masculino':
			pronome_pessoal_reto = 'eles'
		else:
			pronome_pessoal_reto = 'elas'

	return pronome_pessoal_reto


def realizacao_pronome_caso_oblíquo():
	'''(str)->str
    Retorna o pronome oblíquo adequado dado uma pessoa da intelocução.

    >>>realizacao_pronominal_caso_oblíquo ()
    'me'
    '''
	tonicidade = choice.Menu(['átono', 'tônico']).ask()
	pessoa_da_interlocução = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
	número = choice.Menu(['singular', 'plural']).ask()
	if pessoa_da_interlocução == 'falante' and número == 'singular' and tonicidade == 'átono':
		pronome_pessoal_oblíquo = 'me'

	elif pessoa_da_interlocução == 'ouvinte' and número == 'singular' and tonicidade == 'átono':
		pronome_pessoal_oblíquo = 'te'

	elif pessoa_da_interlocução == 'não_interlocutor' and número == 'singular' and tonicidade == 'átono':
		morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()

		if morfologia_do_pronome == 'padrão':
			gênero = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()

			if gênero == 'masculino':
				pronome_pessoal_oblíquo = 'o'

			elif gênero == 'feminino':
				pronome_pessoal_oblíquo = 'a'

			else:
				pronome_pessoal_oblíquo = choice.Menu(['se', 'lhe']).ask()
		elif morfologia_do_pronome == 'não_padrão':
			gênero = choice.Menu(['masculino', 'feminino']).ask()

			if gênero == 'masculino':
				pronome_pessoal_oblíquo = 'ele'
			else:
				pronome_pessoal_oblíquo = 'ela'

	elif pessoa_da_interlocução == 'falante' and número == 'plural' and tonicidade == 'átono':
		pronome_pessoal_oblíquo = 'nos'

	elif pessoa_da_interlocução == 'ouvinte' and número == 'plural' and tonicidade == 'átono':
		pronome_pessoal_oblíquo = 'vos'

	elif pessoa_da_interlocução == 'não_interlocutor' and número == 'plural' and tonicidade == 'átono':
		morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()

		if morfologia_do_pronome == 'padrão':
			gênero = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()

			if gênero == 'masculino':
				pronome_pessoal_oblíquo = 'os'

			elif gênero == 'feminino':
				pronome_pessoal_oblíquo = 'as'

			else:
				pronome_pessoal_oblíquo = choice.Menu(['se', 'lhes']).ask()
		elif morfologia_do_pronome == 'não_padrão':
			gênero = choice.Menu(['masculino', 'feminino']).ask()

			if gênero == 'masculino':
				pronome_pessoal_oblíquo = 'eles'
			else:
				pronome_pessoal_oblíquo = 'elas'

	elif pessoa_da_interlocução == 'falante' and número == 'singular' and tonicidade == 'tônico':
		pronome_pessoal_oblíquo = 'mim'

	elif pessoa_da_interlocução == 'ouvinte' and número == 'singular' and tonicidade == 'tônico':
		morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()
		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_oblíquo = 'ti'
		else:
			pronome_pessoal_oblíquo = 'você'

	elif pessoa_da_interlocução == 'não_interlocutor' and número == 'singular' and tonicidade == 'tônico':

		gênero = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()

		if gênero == 'masculino':
			pronome_pessoal_oblíquo = 'ele'

		elif gênero == 'feminino':
			pronome_pessoal_oblíquo = 'ela'


		elif gênero == 'não_binário':
			pronome_pessoal_oblíquo = 'si'

	elif pessoa_da_interlocução == 'falante' and número == 'plural' and tonicidade == 'tônico':
		pronome_pessoal_oblíquo = 'nós'

	elif pessoa_da_interlocução == 'ouvinte' and número == 'plural' and tonicidade == 'tônico':
		morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()

		if morfologia_do_pronome == 'padrão':
			pronome_pessoal_oblíquo = 'vós'
		else:
			pronome_pessoal_oblíquo = 'vocês'


	elif pessoa_da_interlocução == 'não_interlocutor' and número == 'plural' and tonicidade == 'tônico':

		gênero = choice.Menu(['masculino', 'feminino', 'não_binário']).ask()

		if gênero == 'masculino':
			pronome_pessoal_oblíquo = 'eles'

		elif gênero == 'feminino':
			pronome_pessoal_oblíquo = 'elas'


		elif gênero == 'não_binário':
			pronome_pessoal_oblíquo = 'si'

	return pronome_pessoal_oblíquo


def pronome_relativo():
	'''
    '''
	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()

	if modo_inserção == 'inserção_manual':
		pronome_relativo = input('Escreva o pronome desejado:')

	elif modo_inserção == 'inserção_menu':

		print('Qual tipo_pessoa de relativo?')
		tipo_pronome_relativo = choice.Menu(['variável', 'invariável']).ask()
		if tipo_pronome_relativo == 'variável':

			print('Qual o gênero?')
			gênero = choice.Menu(['masculino', 'feminino']).ask()
			print('Qual o número?')
			número = choice.Menu(['singular', 'plural']).ask()

			if gênero == 'masculino' and número == 'singular':
				pronome_relativo = choice.Menu(['o qual', 'cujo', 'quanto', 'pelo quai']).ask()

			elif gênero == 'masculino' and número == 'plural':
				pronome_relativo = choice.Menu(['os quais', 'cujos', 'quantos', 'pelos quais']).ask()

			elif gênero == 'feminino' and número == 'singular':
				pronome_relativo = choice.Menu(['a qual', 'cuja', 'quanta', 'pela qual']).ask()

			elif gênero == 'feminino' and número == 'plural':
				pronome_relativo = choice.Menu(['as quais', 'cujas', 'quantas', 'pelas quais']).ask()

		elif tipo_pronome_relativo == 'invariável':
			pronome_relativo = choice.Menu(['quem', 'que',
			                                'a quem', 'a que', 'porque', 'como']).ask()

	return pronome_relativo


##PRECISO IMPLEMENTAR LETRA MAIÚSCULA NO CASO DE INICIO DE FRASE.
# SUBSTANTIVOS PRÓPRIOS VIRÃO DA LISTA DE NOMES PRÓPRIOS ANOTADOS NA GUM
# Por enquanto, vou deixar um input


def nome_próprio():
	'''(str)->str
    Retorna o nome próprio. #Futuramente parte das listas de léxicos
    advindas da anotação na GUM.
    '''
	nome_próprio = input('Qual é o nome próprio?')
	return nome_próprio.capitalize()


####DÊIXIS DO GN


def estrutura_lógica_dêixis():
	'''
    '''

	estrutura_lógica_dêixis = input("""
                         
            1: α(Dêitico_ñ_seletivo_específico) # ex.: O,A
            2: α(Dêitico_ñ_seletivo_ñ_específico) #ex.: Um,uns
            3: α(Dêitico_prox) #Este
            4: α(Dêitico_pess) #Meu
            5: β(Dêitico_prox)^α(Dêitico_pess) # ex.: Este meu
            6: β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess) # ex.: O meu
            7: β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess) # ex.: Um meu
                             
                             
                             
                             
                             
            Selecione uma opção:""")

	if estrutura_lógica_dêixis == '1':

		estrutura_lógica_dêixis = 'α(Dêitico_ñ_seletivo_específico)'

	elif estrutura_lógica_dêixis == '2':

		estrutura_lógica_dêixis = 'α(Dêitico_ñ_seletivo_ñ_específico)'

	elif estrutura_lógica_dêixis == '3':

		estrutura_lógica_dêixis = 'α(Dêitico_prox)'

	elif estrutura_lógica_dêixis == '4':

		estrutura_lógica_dêixis = 'α(Dêitico_pess)'

	elif estrutura_lógica_dêixis == '5':

		estrutura_lógica_dêixis = 'β(Dêitico_prox)^α(Dêitico_pess)'

	elif estrutura_lógica_dêixis == '6':

		estrutura_lógica_dêixis = 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)'

	elif estrutura_lógica_dêixis == '7':

		estrutura_lógica_dêixis = 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)'

	return estrutura_lógica_dêixis


# a fazer: verificar as opções que coloquei para os diferentes tipos de dêixis:
# não preciso talvez colocar todas as opções de especificidade em cada um deles
# pra não ter a possibilidade de dar erro nas escolhas.
def Dêitico_ñ_seletivo_específico():
	'''
    '''

	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	if (DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'NA' or
			DETERMINAÇÃO_espeficifidade == 'genérico(=todos,quaisquer)' and ORIENTAÇÃO == 'NA'):

		print('Selecione número:')
		número = choice.Menu(['singular', 'plural']).ask()
		print('Selecione o gênero')
		gênero = choice.Menu(['masculino', 'feminino']).ask()
		if número == 'plural' and gênero == 'masculino':
			determinante = 'os'



		elif número == 'plural' and gênero == 'feminino':
			determinante = 'as'



		elif número == 'singular' and gênero == 'masculino':
			determinante = 'o'


		elif número == 'singular' and gênero == 'feminino':
			determinante = 'a'

	return determinante


def Dêitico_ñ_seletivo_ñ_específico():
	'''
    '''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	if DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'NA':
		print('Selecione número:')
		número = choice.Menu(['singular', 'plural']).ask()
		print('Selecione o gênero')
		gênero = choice.Menu(['masculino', 'feminino']).ask()
		if número == 'singular' and gênero == 'masculino':
			determinante = 'um'


		elif número == 'plural' and gênero == 'masculino':
			determinante = 'uns'


		elif número == 'singular' and gênero == 'feminino':
			determinante = 'uma'


		elif número == 'plural' and gênero == 'feminino':
			determinante = 'umas'

	return determinante

	####


def Dêitico_prox():
	'''
    '''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()
	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa',
	                          'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade':
		print('Selecione a pessoa da interlocução:')
		pessoa_da_interlocução_proximidade = choice.Menu(
			['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']).ask()
		if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':
			print('Selecione número:')
			número = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero')
			gênero = choice.Menu(['masculino', 'feminino']).ask()

			if número == 'singular' and gênero == 'masculino':
				determinante = 'este'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'estes'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'esta'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'estas'
		elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte':
			print('Selecione número:')
			número = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero')
			gênero = choice.Menu(['masculino', 'feminino']).ask()
			if número == 'singular' and gênero == 'masculino':
				determinante = 'esse'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'esses'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'essa'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'essas'
		elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor':
			print('Selecione número:')
			número = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero')
			gênero = choice.Menu(['masculino', 'feminino']).ask()
			if número == 'singular' and gênero == 'masculino':
				determinante = 'aquele'
			elif número == 'plural' and gênero == 'masculino':
				determinante = 'aqueles'
			elif número == 'singular' and gênero == 'feminino':
				determinante = 'aquela'
			elif número == 'plural' and gênero == 'feminino':
				determinante = 'aquelas'

	return determinante


def Dêitico_pess():
	'''
    '''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()
	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':
		print('Selecione a pessoa da interlocução do possuidor')
		pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()
		if pessoa_da_interlocução_possuidor == '1s':
			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()
			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'meu'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'meus'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'minha'
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'minhas'

		elif pessoa_da_interlocução_possuidor == '2s':
			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()
			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()
			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'teu'
				else:
					determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'teus'
				else:
					determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'tua'
				else:
					determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'tuas'
				else:
					determinante = 'suas'


		elif (pessoa_da_interlocução_possuidor == '3s' or
		      pessoa_da_interlocução_possuidor == '3p'):

			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'seus'


			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'suas'


		elif pessoa_da_interlocução_possuidor == '1p':
			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'nosso'
			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'nossos'
			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'nossa'
			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'nossas'


		elif pessoa_da_interlocução_possuidor == '2p':
			print('Selecione número do objeto  possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

			if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'vosso'
				else:
					determinante = 'seu'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'vossos'
				else:
					determinante = 'seus'

			elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'vossa'
				else:
					determinante = 'sua'

			elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'vossas'
				else:
					determinante = 'suas'

	return determinante


def Dêitico_ñ_seletivo_específico_e_Dêitico_pess():
	'''
    '''

	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':

		print('Selecione a pessoa da interlocução do possuidor')
		pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

		print('Selecione número do objeto possuído:')
		número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

		print('Selecione o gênero do objeto possuído')
		gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

		if pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			determinante = 'o meu'
		elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			determinante = 'os meus'
		elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			determinante = 'a minha'
		elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			determinante = 'as minhas'

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'o teu'
			else:
				determinante = 'o seu'

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'os teus'
			else:
				determinante = 'os seus'

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'a tua'
			else:
				determinante = 'a sua'

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'as tuas'
			else:
				determinante = 'as suas'

		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
			determinante = 'o seu'
		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
			determinante = 'os seus'
		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
			determinante = 'a sua'
		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
			determinante = 'as suas'

		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			determinante = 'o nosso'
		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			determinante = 'os nossos'
		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			determinante = 'a nossa'
		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			determinante = 'as nossas'


		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'o vosso'
			else:
				determinante = 'o seu'

		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'os vossos'
			else:
				determinante = 'os seus'

		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'a vossa'
			else:
				determinante = 'a sua'

		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'as vossas'
			else:
				determinante = 'as suas'

	return determinante


def Dêitico_ñ_seletivo_ñ_específico_e_Dêitico_pess():
	'''
    '''

	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(
		['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
		 'genérico(contável)']).ask()

	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	if DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':

		print('Selecione a pessoa da interlocução do possuidor')
		pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

		print('Selecione número do objeto possuído:')
		número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

		print('Selecione o gênero do objeto possuído')
		gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

		if pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			determinante = 'um meu'
			return determinante

		elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			determinante = 'uns meus'
			return determinante
		elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			determinante = 'uma minha'
			return determinante
		elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			determinante = 'umas minhas'
			return determinante

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'um teu'
				return determinante
			else:
				determinante = 'um seu'
				return determinante

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'uns teus'
				return determinante
			else:
				determinante = 'uns seus'
				return determinante

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'uma tua'
				return determinante
			else:
				determinante = 'uma sua'
				return determinante

		elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'umas tuas'
				return determinante
			else:
				determinante = 'umas suas'
				return determinante

		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
			determinante = 'um seu'
			return determinante
		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
			determinante = 'uns seus'
			return determinante
		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
			determinante = 'uma sua'
			return determinante
		elif (
				pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino' or
				pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
			determinante = 'umas suas'
			return determinante

		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			determinante = 'um nosso'
		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			determinante = 'uns nossos'
			return determinante
		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			determinante = 'uma nossa'
			return determinante
		elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			determinante = 'umas nossas'
			return determinante


		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'um vosso'
				return determinante
			else:
				determinante = 'um seu'
				return determinante

		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'uns vossos'
				return determinante
			else:
				determinante = 'uns seus'
				return determinante

		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'uma vossa'
				return determinante
			else:
				determinante = 'uma sua'
				return determinante

		elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
			print('Selecione a morfologia do pronome:')
			morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
			if morfologia_do_pronome == 'padrão':
				determinante = 'umas vossas'
				return determinante
			else:
				determinante = 'umas suas'
				return determinante


def Dêitico_prox_e_Dêitico_pess():
	'''
    '''
	print('Selecione a especificidade:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
	                                           'genérico(de_massa)', 'genérico(contável)']).ask()
	print('Selecione a orientação:')
	ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
	                          'orientação_específica_proximidade_e_pessoa']).ask()

	if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade_e_pessoa':

		print('Selecione a pessoa da interlocução:')
		pessoa_da_interlocução_proximidade = choice.Menu(['próximo_ao_falante', 'próximo_ao_ouvinte',
		                                                  'próximo_ao_não_interlocutor']).ask()

		if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':

			print('Selecione a pessoa da interlocução do possuidor')
			pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

			print('Selecione o gênero do objeto possuído')
			gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

			if pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' \
					and gênero_obj_possuído == 'masculino':
				determinante = 'este meu'
				return determinante
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' \
					and gênero_obj_possuído == 'masculino':
				determinante = 'estes meus'
				return determinante
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' \
					and gênero_obj_possuído == 'feminino':
				determinante = 'esta minha'
				return determinante
			elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' \
					and gênero_obj_possuído == 'feminino':
				determinante = 'estas minhas'
				return determinante

			elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' \
					and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'este teu'
					return determinante
				else:
					determinante = 'este seu'
					return determinante

			elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' \
					and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'estes teus'
					return determinante
				else:
					determinante = 'estes seus'
					return determinante

			elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' \
					and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'esta tua'
					return determinante
				else:
					determinante = 'esta sua'
					return determinante

			elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' \
					and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'estas tuas'
					return determinante
				else:
					determinante = 'estas suas'
					return determinante

			elif (
					pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
					pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
				determinante = 'este seu'
				return determinante
			elif (
					pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
					pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
				determinante = 'estes seus' \
				return determinante
			elif (
					pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
					pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
				determinante = 'esta sua'
				return determinante
			elif (
					pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino' or
					pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
				determinante = 'estas suas'
				return determinante

			elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'este nosso'
				return determinante
			elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'estes nossos'
				return determinante
			elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'esta nossa'
				return determinante
			elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'estas nossas'
				return determinante

			elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'este vosso'
					return determinante
				else:
					determinante = 'este seu'
					return determinante

			elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'estes vossos'
					return determinante
				else:
					determinante = 'estes seus'
					return determinante \
 \
			elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'esta vossa'
					return determinante
				else:
					determinante = 'esta sua'
					return determinante

			elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'estas vossas'
					return determinante
				else:
					determinante = 'estas suas'
					return determinante


		elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte':

			print('Selecione a pessoa da interlocução do possuidor')
			pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

			print('Selecione o gênero_obj_possuído do objeto possuído')
			gênero_obj_possuído_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

			if pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'esse meu'
				return determinante
			elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'esses meus'
				return determinante
			elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'essa minha'
				return determinante
			elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'essas minhas'
				return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'esse teu'
					return determinante
				else:
					determinante = 'esse seu'
					return determinante \
 \
			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'esses teus'
					return determinante
				else:
					determinante = 'esses seus'
					return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'essa tua'
					return determinante
				else:
					determinante = 'essa sua'
					return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'essas tuas'
					return determinante
				else:
					determinante = 'essas suas'
					return determinante

			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
				determinante = 'esse seu'
				return determinante
			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
				determinante = 'esses seus'
				return determinante
			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
				determinante = 'essa sua'
				return determinante
			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
				determinante = 'essas suas'
				return determinante

			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'esse nosso'
				return determinante
			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'esses nossos'
				return determinante
			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'essa nossa'
				return determinante
			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'essas nossas'
				return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'esse vosso'
					return determinante
				else:
					determinante = 'esse seu'
					return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'esses vossos'
					return determinante
				else:
					determinante = 'esses seus'
					return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'essa vossa'
					return determinante
				else:
					determinante = 'essa sua'
					return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'essas vossas'
					return determinante
				else:
					determinante = 'essas suas'
					return determinante

		elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor':

			print('Selecione a pessoa da interlocução do possuidor')
			pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

			print('Selecione número do objeto possuído:')
			número_obj_possuído = choice.Menu(['singular', 'plural']).ask()

			print('Selecione o gênero_obj_possuído do objeto possuído') \
			gênero_obj_possuído_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()

			if pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'aquele meu'
				return determinante
			elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'aqueles meus'
				return determinante
			elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'aquela minha'
				return determinante
			elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'aquelas minhas'
				return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aquele teu'
					return determinante
				else:
					determinante = 'aquele seu'
					return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aqueles teus'
					return determinante
				else:
					determinante = 'aqueles seus'
					return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aquela tua'
					return determinante
				else:
					determinante = 'aquela sua'
					return determinante

			elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aquelas tuas'
					return determinante
				else:
					determinante = 'aquelas suas'
					return determinante

			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
				determinante = 'aquele seu'
				return determinante
			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
				determinante = 'aqueles seus'
				return determinante
			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
				determinante = 'aquela sua'
				return determinante
			elif (
					pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino' or
					pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
				determinante = 'aquelas suas'
				return determinante

			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				determinante = 'aquele nosso'
				return determinante
			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				determinante = 'aqueles nossos'
				return determinante
			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				determinante = 'aquela nossa'
				return determinante
			elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				determinante = 'aquelas nossas'
				return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aquele vosso'
					return determinante
				else:
					determinante = 'aquele seu'
					return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão': \
					determinante = 'aqueles vossos'
					return determinante
				else:
					determinante = 'aqueles seus'
					return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aquela vossa'
					return determinante
				else:
					determinante = 'aquela sua'
					return determinante

			elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
				print('Selecione a morfologia do pronome:')
				morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
				if morfologia_do_pronome == 'padrão':
					determinante = 'aquelas vossas'
					return determinante
				else:
					determinante = 'aquelas suas'
					return determinante

		elif DETERMINAÇÃO_espeficifidade == 'genérico(contável)' and ORIENTAÇÃO == 'NA':

			determinante = ''  # Neste caso, o grupo nominal é realizado no plural
			return determinante

		elif DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' and ORIENTAÇÃO == 'NA':

			determinante = ''  # Neste caso, o grupo nominal é realizado no singular
			return determinante


def Dêixis_geral():
	'''
    '''
	print('Há determinante?')
	real_determinante = choice.Menu(['sim', 'NA']).ask()

	if real_determinante == 'sim':

		print('Qual a sub-estrutura lógica da Dêixis?')
		estrutura_lógica = estrutura_lógica_dêixis()

		if (estrutura_lógica == 'α(Dêitico_ñ_seletivo_específico)' or
				estrutura_lógica == 'α(Dêitico_ñ_seletivo_específico)'):

			Determinante = Dêitico_ñ_seletivo_específico()

		elif estrutura_lógica == 'α(Dêitico_ñ_seletivo_ñ_específico)':
			Determinante = Dêitico_ñ_seletivo_ñ_específico()

		elif estrutura_lógica == 'α(Dêitico_prox)':
			Determinante = Dêitico_prox()

		elif estrutura_lógica == 'α(Dêitico_pess)':
			Determinante = Dêitico_pess()

		elif estrutura_lógica == 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)':
			Determinante = Dêitico_ñ_seletivo_específico_e_Dêitico_pess()

		elif estrutura_lógica == 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)':
			Determiante = Dêitico_ñ_seletivo_ñ_específico_e_Dêitico_pess()

		elif estrutura_lógica == 'β(Dêitico_prox)^α(Dêitico_pess)':
			Determinante = Dêitico_prox_e_Dêitico_pess()

	else:

		Determinante = ''

	return Determinante


def Dêitico_genérico():
	print('Selecione tipo_pessoa de dêixis genérica:')
	DETERMINAÇÃO_espeficifidade = choice.Menu(['genérico(contável)', 'genérico(de_massa)']).ask()

	if (DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' or
			DETERMINAÇÃO_espeficifidade == 'genérico(contável)'):
		determinante = ''  # Neste caso, o grupo nominal CONTÁVEL é realizado no plural e o DE MASSA no singular

	return determinante


def Ente():
	'''
    '''
	print('Qual o tipo_pessoa de Ente?')
	tipo_de_Ente = choice.Menu(['consciente', 'não_consciente', 'NA']).ask()

	if tipo_de_Ente == 'NA':
		Ente = ''
		return Ente

	elif tipo_de_Ente == 'não_consciente':
		print('Qual tipo_pessoa de não_consciente?')
		tipo_de_não_consciente = choice.Menu(['material', 'semiótico']).ask()

		if tipo_de_não_consciente == 'material':
			print('Qual tipo_pessoa de material?')
			tipo_de_não_consciente_material = choice.Menu(
				['animal', 'objeto_material', 'substância_material', 'abstração_material']).ask()

			if (tipo_de_não_consciente_material == 'animal' or
					tipo_de_não_consciente_material == 'objeto_material' or
					tipo_de_não_consciente_material == 'substância_material' or \
					tipo_de_não_consciente_material == 'abstração_material'):
				print('Qual a classe de palavra que realiza o Ente?')
				classe_palavra_Ente = choice.Menu(
					['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_oblíquo']).ask()

				if classe_palavra_Ente == 'substantivo_comum':
					Ente = formação_da_estrutura_do_substantivo_comum()

				elif classe_palavra_Ente == 'substantivo_próprio':
					Ente = nome_próprio()
				elif classe_palavra_Ente == 'pronome_caso_reto':
					Ente = realizacao_pronominal_casoreto()
				elif classe_palavra_Ente == 'pronome_caso_oblíquo':
					Ente = realizacao_pronome_caso_oblíquo()

		elif tipo_de_não_consciente == 'semiótico':
			print('Qual tipo_pessoa de semiótico?')
			tipo_de_não_consciente_semiótico = choice.Menu(
				['instituição', 'objeto_semiótico', 'abstração_semiótica']).ask()

			if (tipo_de_não_consciente_semiótico == 'instituição' or
					tipo_de_não_consciente_semiótico == 'objeto_semiótico' or
					tipo_de_não_consciente_semiótico == 'abstração_semiótica'):
				print('Qual a classe de palavra que realiza o Ente?')
				classe_palavra_Ente = choice.Menu(
					['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_oblíquo']).ask()

				if classe_palavra_Ente == 'substantivo_comum':
					Ente = formação_da_estrutura_do_substantivo_comum()

				elif classe_palavra_Ente == 'substantivo_próprio':
					Ente = nome_próprio()
				elif classe_palavra_Ente == 'pronome_caso_reto':
					Ente = realizacao_pronominal_casoreto()
				elif classe_palavra_Ente == 'pronome_caso_oblíquo':
					Ente = realizacao_pronome_caso_oblíquo()


	elif tipo_de_Ente == 'consciente':
		print('Qual a classe de palavra que realiza o Ente?')
		classe_palavra_Ente = choice.Menu(
			['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_oblíquo']).ask() \
 \
		if classe_palavra_Ente == 'substantivo_comum':
			Ente = formação_da_estrutura_do_substantivo_comum() \
 \
		elif classe_palavra_Ente == 'pronome_caso_reto':
			Ente = realizacao_pronominal_casoreto()

		elif classe_palavra_Ente == 'substantivo_próprio':
			Ente = nome_próprio()
		elif classe_palavra_Ente == 'pronome_caso_oblíquo':
			Ente = realizacao_pronome_caso_oblíquo()

	return Ente


###No caso do Ente, ainda tenho que modelar as opções de Ente realizados por substantivos compostos (devido ao padrão de
# morfologia das flexões


#####ESTRUTURA DO GRUPO NOMINAL:

##

def qualificador():
	print('Há Qualificador no gn?')
	tem_qualificador = choice.Menu(['sim', 'NA']).ask()

	if tem_qualificador == 'sim':
		realizacao_qualificador = choice.Menu(['frase-preposicional', 'oração']).ask()
		if realizacao_qualificador == 'frase-preposicional':
			Qualificador = frase_preposicional()
		else:
			Qualificador = "que" + oraçãoProjetada()
	else:
		Qualificador = ''
	return Qualificador


def estrutura_GN_downraked():
	GN_downranked = estrutura_GN()

	return GN_downranked


####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal
# com função de Numerativo no GN DE PRIMEIRO NÍVEL)
def estrutura_GN():
	print('Há dissociação entre Ente e Núcleo do GN?')
	dissociação_Ente_Núcleo = choice.Menu(['sim', 'não']).ask()

	if dissociação_Ente_Núcleo == 'não':

		Determinante = Dêixis_geral()
		numerativo = Numerativo()
		ente = Ente()
		Classificador = adjetivo_modificador() \
		Epíteto = adjetivo_modificador()
		Qualificador = qualificador()

		GN = Determinante + ' ' + numerativo + ' ' + ente + ' ' + Classificador + ' ' + Epíteto + ' ' + Qualificador

	else:

		Núcleo_lógico = estrutura_GN_downraked()
		print('Selecione o Qualificador/Ente:')
		Qualificador = qualificador()
		GN = Núcleo_lógico + ' ' + Qualificador
	return GN


########PREPOSIÇÃO
def preposição_switcher():
	i = int(input())

	switcherModo = {
		1: 'a',
		2: 'ante',
		3: 'após',
		4: 'até',
		5: 'com',
		6: 'contra',
		7: 'de',
		8: 'desde',
		9: 'em',
		10: 'entre',
		11: 'para',
		12: 'por',
		13: 'perante',
		14: 'sem',
		15: 'sob',
		16: 'sobre',
		17: 'trás',
	}

	preposição = switcherModo.get(i, 'Seleção nao disponível')
	return preposição


def Preposição():
	'''
    '''
	modo_inserção = choice.Menu(['inserção_manual',
	                             'inserção_menu']).ask()

	if modo_inserção == 'inserção_manual':
		preposição = input('Escreva a Preposição desejada:')

	else:
		print("""                   
               1:a
               2:ante
               3:após
               4:até
               5:com
               6:contra
               7:de
               8:desde
               9:em
               10:entre
               11:para
               12:por
               13:perante
               14:sem
               15:sob
               16:sobre
               17:trás
                   Escolha uma opção:""")

		preposição = preposição_switcher()

	return preposição


def frase_preposicional():
	'''
    '''
	preposição = Preposição()
	grupo_nominal = (re.sub(' +', ' ', estrutura_GN_downraked())).strip()

	if preposição == 'por':
		if grupo_nominal[:2] == 'o ':
			frase_prep = 'pel' + grupo_nominal
		elif grupo_nominal[:2] == 'a ':
			frase_prep = 'pel' + grupo_nominal
		else:
			frase_prep = preposição + ' ' + grupo_nominal
	elif preposição == 'a':
		if grupo_nominal[:2] == 'a ':
			frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
		elif grupo_nominal[:2] == 'o ':
			frase_prep = preposição + grupo_nominal
		elif grupo_nominal[:5] == 'aquel':
			frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
		else:
			frase_prep = preposição + ' ' + grupo_nominal
	elif preposição == 'de':
		if (grupo_nominal[:2] == 'o ' or
				grupo_nominal[:2] == 'a ' or
				grupo_nominal[:3] == 'est' or
				grupo_nominal[:3] == 'ist' or
				grupo_nominal[:3] == 'ess' or
				grupo_nominal[:3] == 'iss' or
				grupo_nominal[:5] == 'aquel' or
				grupo_nominal[:5] == 'aquil'):
			frase_prep = (preposição[slice(-1)]) + grupo_nominal
		elif (grupo_nominal[:2] == 'um' or
		      grupo_nominal[:2] == 'un' or
		      grupo_nominal[:2] == 'el' or
		      grupo_nominal[:4] == 'outr'):
			print("Com ou sem contração")
			contração = choice.Menu(['+contração', '-contração']).ask()
			if contração == '+contração':
				frase_prep = (preposição[slice(-1)]) + grupo_nominal
			else:
				frase_prep = preposição + ' ' + grupo_nominal
		else:
			frase_prep = preposição + ' ' + grupo_nominal
	elif preposição == 'em':
		if (
				grupo_nominal[:2] == 'o ' or
				grupo_nominal[:2] == 'a ' or
				grupo_nominal[:2] == 'el' or
				grupo_nominal[:3] == 'est' or
				grupo_nominal[:3] == 'ist' or
				grupo_nominal[:3] == 'ess' or
				grupo_nominal[:3] == 'iss' or \
				grupo_nominal[:5] == 'aquel' or
				grupo_nominal[:5] == 'aquil'
		): \
			frase_prep = 'n' + grupo_nominal
		else:
			if (
					grupo_nominal[:2] == 'um' or
					grupo_nominal[:2] == 'un' or
					grupo_nominal[:4] == 'outr'
			):
				print("Com ou sem contração?")
				contração = choice.Menu(['+contração', '-contração']).ask()
				if contração == '+contração':
					frase_prep = 'n' + grupo_nominal
				else:
					frase_prep = preposição + ' ' + grupo_nominal

	elif preposição == 'para':
		if (
				grupo_nominal[:2] == 'o ' or
				grupo_nominal[:2] == 'a '
		):

			print("Com ou sem contração") \
			contração = choice.Menu(['+contração', '-contração']).ask()
			if contração == '+contração':
				frase_prep = 'pr' + grupo_nominal
			else:
				frase_prep = preposição + ' ' + grupo_nominal
		else:
			frase_prep = preposição + ' ' + grupo_nominal
	else:
		frase_prep = preposição + ' ' + grupo_nominal
	return frase_prep


############ORDEM DA ORAÇÃO

def circunstância():
	'''
    '''
	print('Há circunstância?')
	circunstância = choice.Menu(['sim', 'não']).ask()

	if circunstância == 'não':
		Circunstância = ''
	else:
		print('Selecione o tipo_pessoa de grupo que realiza a circunstância:')
		realizacao_circunstância = choice.Menu(['grupo_nominal', 'frase_preposicional', 'grupo_adverbial']).ask()

		if realizacao_circunstância == 'grupo_nominal':
			Circunstância = estrutura_GN()
		elif realizacao_circunstância == 'frase_preposicional':
			Circunstância = frase_preposicional()
		elif realizacao_circunstância == 'grupo_adverbial':
			Circunstância = advérbio()

	return Circunstância


##SISTEMAS DA ORAÇÃO


def AGENCIAMENTO():
	## no caso de materiais meteorológicas, o Meio conflui
	# com o Processo (por isso :AG_processo_sem_alcance,AG_processo+alcance );
	# pode haver escopo (Ex.: choveu uma chuva grossa)
	print('Qual o tipo_pessoa de Agenciamento?')
	AGENCIAMENTO = choice.Menu(['AG_médio_sem_alcance',

	                            'AG_médio_com_alcance',
	                            'AG_efetivo_operativo',
	                            'AG_efetivo_receptivo_agentivo',
	                            'AG_efetivo_receptivo_não_agentivo',
	                            'AG_processo_sem_alcance',
	                            'AG_processo+alcance']).ask()

	return AGENCIAMENTO


###tipos de processo oração
# Material
##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)

# def PROCESSO_MATERIAL():
#    Processo_material = choice.Menu(['PR_material_transformativo_transitivo',
#                                     'PR_material_criativo_transitivo',
#                                     'PR_material_transformativo_intransitivo',
#                                     'PR_material_criativo_intransitivo']).ask()
#
#    return Processo_material


###tipos de processo oração
# Material
##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)

def PROCESSO_MATERIAL():
	print('Qual o tipo_pessoa de ação realizada pelo processo?')
	TIPO_DE_AÇÃO = choice.Menu(['transformativo', 'criativo']).ask()

	print('Qual o tipo_pessoa de impacto?')
	IMPACTO = choice.Menu(['IMPA_transitivo', 'IMPA_intransitivo', 'IMPA_NA']).ask()
	Processo_material = 'PR_material_' + TIPO_DE_AÇÃO + '_' + IMPACTO

	return Processo_material


#
#
#

# relacional

##def atribuição_de_relação():
##    '''
##    '''
##    atribuição_de_relação = choice.Menu(['atribuição_proj_ment_cognitiva',
##                                         'atribuição_proj_ment_desiderativa',
##                                         'atribuição_proj_verbal',
##                                         'atribuição_expan_elaboração',
##                                         'atribuição_expan_intencificação',
##                                         'sem_atribuição_de_relação']).ask()
##    return atribuição_de_relação
##
#
#
#
#
#
#
# def processo_relacional():
#    '''
#    '''
#    atribuição_relação = atribuição_de_relação()
#
#    tipo_de_relacional = choice.Menu (['PR_relacional_intensivo_atributivo',
#                                       'PR_relacional_intensivo_identificativo',
#                                       'PR_relacional_possessivo_atributivo',
#                                       'PR_relacional_possessivo_identificativo',
#                                       'PR_relacional_circunstancial_atributivo',
#                                       'PR_relacional_circunstancial_identificativo']).ask()
#
#    relacional =  tipo_de_relacional + '_' +  atribuição_relação
#
#    return relacional
#
#
#


#    if (atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'intensiva_atributiva'or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'circunstancial_identificativa' or
#
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'circunstancial_identificativa'or
#
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'circunstancial_identificativa'or
#
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'circunstancial_identificativa'or
#
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'circunstancial_identificativa'or
#
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'circunstancial_identificativa'):
#
#        relacional = atribuição_relação + ' ' + tipo_de_relacional
#
#    return relacional
#
#


# TRANSITIVIDADE


##subsistemas

##agenciamento oração

##MODO

# subsistemas:

# sujeitabilidade
# coloquei aqui apenas responsabilidade e pressuposição pois
# pessoa e número já é decidido na ordem da palavra 9tenho que ver o impacto teórico que
##isso tem..não sei se preciso repetir as escolhas)

def SUJEITABILIDADE():
	'''
    '''
	print('Qual o tipo_pessoa de Sujeito?')
	RESPONSABILIDADE = choice.Menu(['SUJ_responsável',
	                                'SUJ_distante_impessoal',
	                                'SUJ_distante_não_responsável', 'SUJ_-sujeitabilidade']).ask()

	PRESSUPOSIÇÃO_DO_SUJEITO = choice.Menu(['recuperado_explícito', \
	                                        'recuperado_implícito',
	                                        'não_recuperável', 'recuperação_NA']).ask()

	SUJEITABILIDADE = RESPONSABILIDADE + '_' + PRESSUPOSIÇÃO_DO_SUJEITO

	return SUJEITABILIDADE


def TIPO_DE_MODO():
	'''
    '''
	print('Qual o tipo_pessoa de modo da oração?')
	tipo_de_modo = choice.Menu(['MOD_declarativo_+perguntafinito',
	                            'MOD_declarativo_-perguntafinito',
	                            'MOD_interrogativo_elemental',
	                            'MOD_interrogativo_polar',
	                            'MOD_imperativo']).ask()

	return tipo_de_modo


########


######

def AVALIAÇÃO_MODAL():
	'''
    '''

	AVALIAÇÃO = choice.Menu(['+', '-']).ask()

	if AVALIAÇÃO == '-':
		AVALIAÇÃO_MODAL = ''

	else:
		POLARIDADE = choice.Menu(['positiva', 'negativa']).ask()
		##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
		# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.

		if POLARIDADE == 'positiva':
			Adjunto_polaridade = ''

		elif POLARIDADE == 'negativa':
			Adjunto_polaridade = 'não'

	return Adjunto_polaridade


###
def TIPO_POLARIDADE():
	'''
    '''
	print('Qual o tipo_pessoa de polaridade?')
	tipo_polaridade = choice.Menu(['positiva', 'negativa']).ask()
	##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
	# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.

	return tipo_polaridade


def POLARIDADE():
	'''
    '''
	print('Qual o tipo_pessoa de polaridade?')
	tipo_polaridade = choice.Menu(['positiva', 'negativa']).ask()
	##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada (em que estruturas?).
	# Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.

	if tipo_polaridade == 'positiva':
		Adjunto_polaridade = ''

	elif tipo_polaridade == 'negativa':
		Adjunto_polaridade = 'não'

	return Adjunto_polaridade


##############

## Preciso resolver como vou abordar a questão deste sistema: por enquanto vou mexer apenas com
# polaridade, e ir incrementando as combinações.
#
# def TIPO_AVALIAÇÃO_MODAL ():
#    '''
#    '''
#    AVALIAÇÃO = choice.Menu (['+', '-']).ask()
#
#    if AVALIAÇÃO == '-':
#        AVALIAÇÃO_MODAL = 'AvM_sem_avaliação_modal'
#
#    else:
#        POLARIDADE = choice.Menu (['positiva','negativa']).ask()
#        ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
#        #Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
#
#        if POLARIDADE == 'positiva':
#            Adjunto_polaridade == 'AvM_polaridade_positiva'
#
#        elif POLARIDADE == 'negativa':
#            Adjunto_polaridade == 'AvM_polaridade_negativa'
#

##para o sistema de modo, AINDA não considerei o subsistema de VALIDAÇÃO. (será implementado)

def MODO():
	'''
    '''

	print('Faça as escolhas de MODO da oração:')
	MODO = SUJEITABILIDADE() + '_' + TIPO_DE_MODO()
	return MODO


# A DÊIXIS: VER, POIS ELA É DECIDIDA DESDE A ORDEM DA PALAVRA...


# TEMA


def TEMA_TEXTUAL():
	'''
    '''
	print('Há TEMA TEXTUAL?')
	Tema_textual = choice.Menu(['sim', 'não']).ask()
	if Tema_textual == 'não':
		TEMA_TEXTUAL = ''
	else:
		print('Há TEMA TEXTUAL continuativo?')
		tem_continuativo = choice.Menu(['sim', 'não']).ask()
		if tem_continuativo == 'não':
			TEMA_CONTINUATIVO = ''
		else:
			TEMA_CONTINUATIVO = conjunção_continuativa() + ','
		print('Há TEMA TEXTUAL conjuntivo?')
		tem_conjuntivo = choice.Menu(['sim', 'não']).ask()
		if tem_conjuntivo == 'não':
			TEMA_CONJUNTIVO = ''
		else:
			TEMA_CONJUNTIVO = grupo_conjuntivo()
		print('Há TEMA TEXTUAL relativo?')
		tem_relativo = choice.Menu(['sim', 'não']).ask()
		if tem_relativo == 'não':
			TEMA_RELATIVO = ''
		elif tem_relativo == 'sim':
			print('Qual a tipo_pessoa de relativo?')
			tipo_de_relativo = choice.Menu(['nominal', 'adverbial']).ask()
			if tipo_de_relativo == 'nominal':
				TEMA_RELATIVO = pronome_relativo()
			elif tipo_de_relativo == 'adverbial':
				TEMA_RELATIVO = choice.Menu(['de onde', 'quando',
				                             'onde', 'de quando', 'que', 'por onde']).ask()

		TEMA_TEXTUAL = TEMA_CONTINUATIVO + TEMA_CONJUNTIVO + TEMA_RELATIVO

	return TEMA_TEXTUAL


def TEMA_INTERPESSOAL():
	'''
    '''

	print('Há TEMA INTERPESSOAL?')

	Tema_interpessoal = choice.Menu(['sim', 'não']).ask()
	if Tema_interpessoal == 'não':
		TEMA_INTERPESSOAL = ''

	elif Tema_interpessoal == 'sim':  ###POR ENQUANTO, TRABALHANDO COM A realizacao DE APENAS 1 TEMA INTERPESSOAL

		TIPO_TEMA_INTERPESSOAL = choice.Menu(['TI_avaliação_modo', 'TI_avaliação_comentário',
		                                      'TI_encenação_troca', 'TI_encenação_papel_falante', 'TI_polaridade',
		                                      'TI_encenação_papel_ouvinte',
		                                      'TI_NA']).ask()

		if (TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_modo' or TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_comentário' or
				TIPO_TEMA_INTERPESSOAL == 'TI_polaridade'):

			tipo_realizacao = choice.Menu(['grupo_adverbial', 'frase_preposicional']).ask()
			if tipo_realizacao == 'grupo_adverbial':
				TEMA_INTERPESSOAL = advérbio() \
			else:
				TEMA_INTERPESSOAL = frase_preposicional()

		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_troca':
			TEMA_INTERPESSOAL = elemento_qu()

		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_falante':
			TEMA_INTERPESSOAL = partícula_modal()
		elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_ouvinte':
			TEMA_INTERPESSOAL = nome_próprio()  ##talvez um pronome, mas por enquanto vou deixar so o nome

	return TEMA_INTERPESSOAL


def TEMA_IDEACIONAL():
	'''
    ''' \
 \
	print('Qual a ORIENTAÇÃO MODAL do tema?')
	ORIENTAÇÃO_MODAL = choice.Menu(['orientado', 'não_orientado']).ask()

	print('Qual a ORIENTAÇÃO TRANSITIVA do tema?')
	ORIENTAÇÃO_TRANSITIVA = choice.Menu(['direcional', 'não_direcional']).ask()

	print('Qual a SELEÇÃO TEMÁTICA do tema?')
	SELEÇÃO_TEMÁTICA = choice.Menu(['default', 'proeminente']).ask()

	if ORIENTAÇÃO_MODAL == 'orientado' and ORIENTAÇÃO_TRANSITIVA == 'direcional' and SELEÇÃO_TEMÁTICA == 'default':
		print('Qual o tipo_pessoa de TEMA DEFAULT?')
		TEMA_DEFAULT = choice.Menu(['imperativo',
		                            'indicativo']).ask()

		if TEMA_DEFAULT == 'imperativo':
			TEMA_IDEACIONAL = 'TID_default_imperativo'

		elif TEMA_DEFAULT == 'indicativo':
			print('Qual o tipo_pessoa de TEMA DEFAULT INDICATIVO?')
			TEMA_DEFAULT_indicativo = choice.Menu(['declarativo',
			                                       'interrogativo_polar',
			                                       'interrogativo_sujeito_elemental']).ask()

			print('Há TEMA IDENTIFICATIVO?')
			TEMA_IDENTIFICATIVO = choice.Menu(['NA',
			                                   'equativo_codificação',
			                                   'equativo_decodificação']).ask()

			if TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'NA':

				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_NA'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'NA':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'NA':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_NA'

			elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_decodificação': \
 \
				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_decodificação'


			elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_codificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'equativo_codificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação'

			elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'equativo_codificação':

				TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_codificação'


	elif ORIENTAÇÃO_MODAL == 'não_orientado' and ORIENTAÇÃO_TRANSITIVA == 'direcional' and SELEÇÃO_TEMÁTICA == 'proeminente':

		TEMA_ÂNGULO = choice.Menu(['TID_fonte', 'TID_ponto_de_vista']).ask()

		TEMA_IDEACIONAL = TEMA_ÂNGULO



	elif ORIENTAÇÃO_MODAL == 'orientado' and ORIENTAÇÃO_TRANSITIVA == 'não_direcional' and SELEÇÃO_TEMÁTICA == 'default':

		TEMA_ELEMENTAL = choice.Menu(['TID_complemento_elemental', 'TID_adjunto_elemental']).ask()

		TEMA_IDEACIONAL = TEMA_ELEMENTAL



	elif ORIENTAÇÃO_MODAL == 'não_orientado' and ORIENTAÇÃO_TRANSITIVA == 'não_direcional' and SELEÇÃO_TEMÁTICA == 'proeminente':
		print('Qual tipo_pessoa de TEMA PROEMINENTE?')

		TEMA_PROEMINENTE = choice.Menu(['TID_perspectiva_intensificação', \
		                                'TID_perspectiva_outro',
		                                'TID_intensivo_absoluto',
		                                'TID_intensivo_relativo_papel_transitivo_nuclear_participante',
		                                'TID_intensivo_relativo_papel_transitivo_nuclear_processo',
		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_elaboração',
		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_extensão',
		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto',
		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_reprisado',
		                                'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_recuperável',
		                                'TID_intensivo_relativo_predicação_default_local',
		                                'TID_intensivo_relativo_predicação_proeminente_local'

		                                ]).ask()

		TEMA_IDEACIONAL = TEMA_PROEMINENTE

	return TEMA_IDEACIONAL


def conjunção_continuativa():
	'''
    '''
	print('Qual o modo de inserção da conjunção?')
	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()

	if modo_inserção == 'inserção_manual':
		conjunção_continuativa = input('Escreva o continuativo desejado:')

	elif modo_inserção == 'inserção_menu':
		print('Escolha um continuativo:') \
		conjunção_continuativa = input("""
                                 1:e 
                                 2:é 
                                 3:ah 
                                 4:mas 
                                 5:sim 
                                 6:bem 
                                 7:não 
                                 8:agora 
                                 9:então 
                                 10:pois é 
                                 11:tipo_pessoa  
                                 12:tipo_pessoa assim 
                                 13:ó 
                                 14:daí
                                 15:aí
                                 16:aí então  
                                 17:quer 
                                 18:dizer 
                                 19:assim
                                 20:em
                                 21:seguida 
                                 22:por fim 
                                 23:porque 
                                 24:porém 
                                 25:também
                                 26:é que 
                                 27:olha 
                                 
                                 
                                
                               Escolha uma opção:""")

		if conjunção_continuativa == '1':
			conjunção_continuativa = 'e'
		elif conjunção_continuativa == '2':
			conjunção_continuativa = 'é'
		elif conjunção_continuativa == '3':
			conjunção_continuativa = 'ah'
		elif conjunção_continuativa == '4':
			conjunção_continuativa = 'mas'
		elif conjunção_continuativa == '5':
			conjunção_continuativa = 'sim'
		elif conjunção_continuativa == '6':
			conjunção_continuativa = 'bem' \
		elif conjunção_continuativa == '7':
			conjunção_continuativa = 'não'
		elif conjunção_continuativa == '8':
			conjunção_continuativa = 'agora'
		elif conjunção_continuativa == '9':
			conjunção_continuativa = 'então'
		elif conjunção_continuativa == '10':
			conjunção_continuativa = 'pois é'
		elif conjunção_continuativa == '11':
			conjunção_continuativa = 'tipo'
		elif conjunção_continuativa == '12':
			conjunção_continuativa = 'tipo_pessoa assim '
		elif conjunção_continuativa == '13':
			conjunção_continuativa = 'ó'
		elif conjunção_continuativa == '14':
			conjunção_continuativa = 'daí'
		elif conjunção_continuativa == '15':
			conjunção_continuativa = 'aí'
		elif conjunção_continuativa == '16':
			conjunção_continuativa = 'aí então '
		elif conjunção_continuativa == '17':
			conjunção_continuativa = 'quer'
		elif conjunção_continuativa == '18':
			conjunção_continuativa = 'dizer'
		elif conjunção_continuativa == '19':
			conjunção_continuativa = 'assim'
		elif conjunção_continuativa == '20':
			conjunção_continuativa = 'em'
		elif conjunção_continuativa == '21':
			conjunção_continuativa = 'seguida'
		elif conjunção_continuativa == '22':
			conjunção_continuativa = 'por fim'
		elif conjunção_continuativa == '23':
			conjunção_continuativa = 'porque'
		elif conjunção_continuativa == '24':
			conjunção_continuativa = 'porém'
		elif conjunção_continuativa == '25':
			conjunção_continuativa = 'também'

		elif conjunção_continuativa == '26':
			conjunção_continuativa = 'é que'
		elif conjunção_continuativa == '27':
			conjunção_continuativa = 'olha'

	return conjunção_continuativa


def elemento_qu():
	'''
    '''
	elemento_qu = choice.Menu(['o que', 'quem', 'qual', 'quanto',
	                           'quantos', 'quando', 'como', 'onde',
	                           'de quem', 'por quê', 'pra quê', 'por que']).ask()

	return elemento_qu


def partícula_modal():
	'''
    '''
	modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()

	if modo_inserção == 'inserção_manual':
		partícula_modal = input('Escreva partícula modal desejada:')

	elif modo_inserção == 'inserção_menu':
		partícula_modal = choice.Menu(['né', 'ué', 'ó', 'uai', 'é']).ask()  ##HÁ MAIS PARTÍCULAS....

	return partícula_modal


## NO CASO DO SISTEMA DE AVALIAÇÃO_MODAL EU NÃO CONTEMPLEI AINDA  O SISTEMA, POR ENQUANTO VOU ME
# ATER APENAS AO SUBSISTEMA DE POLARIDADE.

####FORMAÇÃO DA ORAÇÃO


def atribuição_de_relação():
	'''
    '''
	atribuição_de_relação = choice.Menu(['atribuição_proj_ment_cognitiva',
	                                     'atribuição_proj_ment_desiderativa',
	                                     'atribuição_proj_verbal',
	                                     'atribuição_expan_elaboração',
	                                     'atribuição_expan_intencificação'
	                                     ]).ask()
	return atribuição_de_relação


def PROCESSO_RELACIONAL():
	'''
    '''
	tipo_de_relacional = choice.Menu(['PR_relacional_intensivo_atributivo',
	                                  'PR_relacional_intensivo_identificativo',
	                                  'PR_relacional_possessivo_atributivo',
	                                  'PR_relacional_circunstancial_atributivo',
	                                  'PR_relacional_possessivo_identificativo',
	                                  'PR_relacional_circunstancial_identificativo']).ask()

	return tipo_de_relacional


def TRANSITIVIDADE(): \
	'''       
    '''
	print('Qual o tipo_pessoa de Processo?')
	TIPO_DE_PROCESSO = choice.Menu(['Material', 'Relacional', \
	                                'Mental', 'Verbal',
	                                'Existencial']).ask()

	if TIPO_DE_PROCESSO == 'Material':
		print('Selecione as opções do sistema da Oração Material')
		Processo = PROCESSO_MATERIAL()
		Agenciamento = AGENCIAMENTO()

		TRANSITIVIDADE = Processo + '_' + Agenciamento

	elif TIPO_DE_PROCESSO == 'Relacional':
		print('Selecione as opções do sistema da Oração Relacional')
		Processo = PROCESSO_RELACIONAL()
		Agenciamento = AGENCIAMENTO()

		TRANSITIVIDADE = Processo + '_' + Agenciamento

	elif TIPO_DE_PROCESSO == 'Existencial':
		print('Selecione as opções do sistema da Oração Existencial')
		Processo = 'PR_Existencial'
		Agenciamento = AGENCIAMENTO()

		TRANSITIVIDADE = Processo + '_' + Agenciamento

	elif TIPO_DE_PROCESSO == 'Verbal':
		print('Selecione as opções do sistema da Oração Verbal')
		Processo = 'PR_Verbal'
		Agenciamento = AGENCIAMENTO()

		TRANSITIVIDADE = Processo + '_' + Agenciamento

	elif TIPO_DE_PROCESSO == 'Mental':
		print('Selecione as opções do sistema da Oração mental')
		Processo = 'PR_Mental'
		Agenciamento = AGENCIAMENTO() \
 \
		TRANSITIVIDADE = Processo + '_' + Agenciamento

	return TRANSITIVIDADE


def oraçãoProjetada():
	oração = oração_gerar()
	return oração


def oraçãoDownranked():
	oração = oração_gerar()
	return oração


def oração_gerar():
	'''(str,str,str)->str
    Retorna a formação estrutural na lexicogramática
     (oração) de uma figura específica da semântica

    >>> oração_gerar()
    'eu bebi água'
    '''
	Transitividade = TRANSITIVIDADE()
	Modo = MODO()
	Tema_id = TEMA_IDEACIONAL()
	# ORAÇÃO MENTAL
	if Transitividade == 'PR_Mental_AG_médio_sem_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Selecione o tipo_pessoa de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
		print('Qual a FENOMENALIZAÇÃO?')
		print('Médio sem alcance: Fenomenalização = não-fenomenalização')
		FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()

		if FENOMENALIZAÇÃO == 'não-fenomenalização':
			print('Qual tipo_pessoa de não-fenomenalização?')
			print('Médio sem alcance: Não-fenomenalização = comportamento-passivo')
			TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['comportamento-passivo']).ask()

			if TIPO_DE_PROCESSO == 'superior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'comportamento-passivo':
				print('Qual tipo_pessoa de Processo superior?')
				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Humanizado)?')
					Experienciador = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade
					+ ' ' + Processo + ' ' + Circunstância + '.'
					# Ex.: Tenho pensado; Eu pensei a noite toda;
			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'comportamento-passivo':
				print('Qual tipo_pessoa de Processo inferior?')
				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
					print('Selecione verbo lematizado emotivo ou perceptivo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Animalizado)?')
					Experienciador = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Circunstância + '.'
					# 'Eu ouvi perfeitamente' - verificar se esse caso se configura como um sem alcance
					# pois apesar de não esta instanciado, há o potencial de fenômeno

	elif Transitividade == 'PR_Mental_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Selecione o tipo_pessoa de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
		print('Qual a FENOMENALIZAÇÃO?')
		FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
		if FENOMENALIZAÇÃO == 'não-fenomenalização':
			print('Médio com alcance, Não-fenomenalização = assunto ')
			print('Qual tipo_pessoa de não-fenomenalização?')
			TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['assunto']).ask()

			if TIPO_DE_PROCESSO == 'superior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'assunto':
				print('Qual tipo_pessoa de Processo superior?')
				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Humanizado)?')
					Experienciador = estrutura_GN()
					print('Qual o Assunto?')
					Assunto = circunstância()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Assunto + ' ' + Circunstância + '.'
					# Ex.: Eu sei de futebol.
			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'assunto':
				print('Qual tipo_pessoa de Processo inferior?')
				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Animalizado)?')
					Experienciador = estrutura_GN()
					print('Qual o Assunto?')
					Assunto = circunstância()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Assunto + ' ' + Circunstância + '.'

		elif FENOMENALIZAÇÃO == 'fenomenalização':
			print('Médio com alcance = mental emanente.')
			print('Qual tipo_pessoa de fenomenalização?')
			TIPO_FENOMENALIZAÇÃO = choice.Menu(['hiperfenômeno', 'fenômeno_simples']).ask()
			if TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
				print('Qual tipo_pessoa de Processo superior?')
				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Humanizado)?')
					Experienciador = estrutura_GN()
					print('Qual o Fenômeno?')
					Fenômeno = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Fenômeno + ' ' + Circunstância + '.'
			elif TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
				print('Qual tipo_pessoa de Processo superior?')
				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
					print('Qual tipo_pessoa de hiperfenômeno?')
					print('Projeção = hiperfenômeno: criativo')
					TIPO_HIPERFENÔMENO = choice.Menu(['criativo']).ask()

					if TIPO_HIPERFENÔMENO == 'criativo':
						TIPO_criativo = choice.Menu(['pensamento', 'desejo']).ask()
						if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
							TIPO_DE_COGNITIVO = choice.Menu(['pensar', 'saber', 'sonhar']).ask()
							if TIPO_DE_COGNITIVO == 'pensar' or TIPO_DE_COGNITIVO == 'saber' or TIPO_DE_COGNITIVO == 'sonhar':
								print('Selecione o verbo lexical correspondente ao tipo_pessoa de cognitivo:') \
								print('Qual o Processo?')
								Processo = grupo_verbal()
								print('Qual o Experienciador (Ente:Humanizado)?')
								Experienciador = estrutura_GN()
								print('Qual o hiperfenômeno projetado? Selecione orientado-finito')
								Pensamento = oraçãoProjetada()
								Polaridade = POLARIDADE()
								Circunstância = circunstância()
								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador \
								         + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento + ' ' + Circunstância + '.'
						elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
							TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar']).ask()
							if TIPO_DE_DESIDERATIVO == 'querer' or TIPO_DE_DESIDERATIVO == 'esperar':
								print('Selecione o verbo lexical correspondente ao tipo_pessoa de desiderativo:')
								print('Qual o Processo?')
								Processo = grupo_verbal()
								print('Qual o Experienciador (Ente:Humanizado)?')
								Experienciador = estrutura_GN()
								print('Qual o hiperfenômeno projetado?')
								print('Selecione grupo verbal não-finito_subjuntivo(condicional ou optativo)')
								Desejo = oraçãoProjetada()
								Polaridade = POLARIDADE()
								Circunstância = circunstância()
								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador \
								         + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Desejo \
								         + ' ' + Circunstância + '.'

			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
				print('Qual tipo_pessoa de Processo inferior?')
				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Animalizado)?')
					Experienciador = estrutura_GN()
					print('Qual o Fenômeno?')
					Fenômeno = estrutura_GN() \
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Fenômeno + ' ' + Circunstância + '.'

			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
				print('Qual tipo_pessoa de Processo inferior?')
				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
				print('Qual tipo_pessoa de hiperfenômeno?')
				TIPO_HIPERFENÔMENO = choice.Menu(['reativo']).ask()
				if TIPO_INFERIOR == 'emotivo' and TIPO_HIPERFENÔMENO == 'reativo':
					print('Qual o tipo_pessoa de reativo?')
					TIPO_reativo = choice.Menu(['metafenômeno']).ask()
					if TIPO_reativo == 'metafenômeno':
						TIPO_DE_EMOTIVO = choice.Menu(['gostar', 'agradar']).ask()
						print('Selecione o verbo lexical correspondente ao tipo_pessoa de emotivo:') \
						print('Qual o Processo?')
						Processo = grupo_verbal()
						print('Qual o Experienciador (Ente:Humanizado)?')
						Experienciador = estrutura_GN()
						print('Qual o metafenômeno? Metafenômenos têm natureza abstrata')
						realizacao_metafenômeno = choice.Menu(['oração_mudada_ordem', 'oração_que',
						                                       'GN+oração_qualificadora']).ask()
						if realizacao_metafenômeno == 'oração_mudada_ordem':
							print('Selecione as orientações desejadas:')
							Metafenômeno = oraçãoProjetada()

						elif realizacao_metafenômeno == 'oração_que':
							print('Selecione orientações desejadas') \
							Metafenômeno = 'que' + ' ' + oraçãoProjetada()
						else:
							print('Selecione o GN com oração qualificadora:')
							Metafenômeno = estrutura_GN()

						Polaridade = POLARIDADE()
						Circunstância = circunstância()
						oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade \
						         + ' ' + Processo + ' ' + Metafenômeno + ' ' + Circunstância + '.'

				elif TIPO_INFERIOR == 'perceptivo' and TIPO_HIPERFENÔMENO == 'reativo':
					print('Qual o tipo_pessoa de reativo?')
					TIPO_reativo = choice.Menu(['macrofenômeno']).ask()
					if TIPO_reativo == 'macrofenômeno':
						print('Qual o Processo?')
						Processo = grupo_verbal()
						print('Qual o Experienciador (Ente:Humanizado)?')
						Experienciador = estrutura_GN()
						print('Qual o macrofenômeno? Macrofenômenos têm natureza concreta')
						realizacao_macrofenômeno = choice.Menu(
							['não_finito_concretizado', 'não-orientado_gerúndio', 'oração_que',
							 'GN+oração_qualificadora']).ask()
						if realizacao_macrofenômeno == 'não_finito_concretizado':
							print('Selecione grupo verbal não-finito_concretizado')
							Macrofenômeno = oraçãoProjetada()

						elif realizacao_macrofenômeno == 'não-orientado_gerúndio':
							print('Selecione grupo verbal não-orientado_gerúndio')
							Macrofenômeno = oraçãoProjetada()
						elif realizacao_macrofenômeno == 'oração_que':
							print('Selecione orientações desejadas')
							Macrofenômeno = 'que' + ' ' + oraçãoProjetada()
						else:
							print('Selecione o GN com oração qualificadora:')
							Macrofenômeno = estrutura_GN()

						Polaridade = POLARIDADE()
						Circunstância = circunstância()
						oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' \
						         + Processo + ' ' + Macrofenômeno + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_Mental_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Efetivo operativo = mental impingente.')
		print('Selecione o tipo_pessoa de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
		print('Qual a FENOMENALIZAÇÃO?')
		FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
		if FENOMENALIZAÇÃO == 'fenomenalização':
			print('Qual tipo_pessoa de fenomenalização?')
			TIPO_FENOMENALIZAÇÃO = choice.Menu(['hiperfenômeno', 'fenômeno_simples']).ask()
			if TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
				print('Qual tipo_pessoa de Processo superior?')
				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Humanizado)?')
					Experienciador = estrutura_GN()
					print('Qual o Fenômeno Agente?')
					FenômenoAgente = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + FenômenoAgente + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
			elif TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
				print('Qual tipo_pessoa de Processo superior?')
				TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask() \
				if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
					print('Qual tipo_pessoa de hiperfenômeno?')
					print('Projeção = hiperfenômeno: criativo')
					TIPO_HIPERFENÔMENO = choice.Menu(['criativo']).ask()

					if TIPO_HIPERFENÔMENO == 'criativo':
						TIPO_criativo = choice.Menu(['pensamento', 'desejo']).ask()
						if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
							TIPO_DE_COGNITIVO = choice.Menu(['pensar', 'saber', 'sonhar']).ask()
							if TIPO_DE_COGNITIVO == 'pensar' or TIPO_DE_COGNITIVO == 'saber' or TIPO_DE_COGNITIVO == 'sonhar':
								print('Selecione o verbo lexical correspondente ao tipo_pessoa de cognitivo:')
								print('Qual o Processo?')
								Processo = grupo_verbal()
								print('Qual o Experienciador (Ente:Humanizado)?')
								Experienciador = estrutura_GN()
								print('Qual o Pensamento Agente? Selecione orientado-finito')
								PensamentoAgente = oraçãoProjetada()
								Polaridade = POLARIDADE()
								Circunstância = circunstância()
								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + ' ' + 'que' + ' ' + PensamentoAgente
								+ ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.' \
								# Ex.:PROBABILIDADE BAIXA DE OCORRÊNCIA: Que você não viria ocorreu me

						elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
							TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar']).ask()
							if TIPO_DE_DESIDERATIVO == 'querer' or TIPO_DE_DESIDERATIVO == 'esperar':
								print('Selecione o verbo lexical correspondente ao tipo_pessoa de desiderativo:')
								print('Qual o Processo?')
								Processo = grupo_verbal()
								print('Qual o Experienciador (Ente:Humanizado)?')
								Experienciador = estrutura_GN()
								print('Qual o Desejo Agente?')
								print('Selecione grupo verbal não-finito_subjuntivo(condicional ou optativo)')
								DesejoAgente = oraçãoProjetada()
								Polaridade = POLARIDADE()
								Circunstância = circunstância()
								oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + ' ' + 'que' + ' ' + DesejoAgente \
								         + ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
								# Ex.:PROBABILIDADE BAIXA DE OCORRÊNCIA: Que você não viria ocorreu me

			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
				print('Qual tipo_pessoa de Processo inferior?')
				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
				if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
					print('Selecione verbo lematizado cognitivo ou desiderativo:')
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Animalizado)?')
					Experienciador = estrutura_GN()
					print('Qual o Fenômeno/Agente?')
					FenômenoAgente = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + FenômenoAgente + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'
					# Ex.: Seus modos entristecem me

			elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
				print('Qual tipo_pessoa de Processo inferior?')
				TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
				print('Qual tipo_pessoa de hiperfenômeno?')
				TIPO_HIPERFENÔMENO = choice.Menu(['reativo']).ask()
				if TIPO_INFERIOR == 'emotivo' and TIPO_HIPERFENÔMENO == 'reativo':
					print('Qual o tipo_pessoa de reativo?')
					TIPO_reativo = choice.Menu(['metafenômeno']).ask()
					if TIPO_reativo == 'metafenômeno':
						TIPO_DE_EMOTIVO = choice.Menu(['gostar', 'agradar']).ask()
						print('Selecione o verbo lexical correspondente ao tipo_pessoa de emotivo:')
						print('Qual o Processo?')
						Processo = grupo_verbal()
						print('Qual o Experienciador (Ente:Humanizado)?')
						Experienciador = estrutura_GN()
						print('Qual o metafenômeno? Metafenômenos têm natureza abstrata')
						realizacao_metafenômeno = choice.Menu(['oração_mudada_ordem', 'oração_que', \
						                                       'GN+oração_qualificadora']).ask() \
						if realizacao_metafenômeno == 'oração_mudada_ordem':
							print('Selecione as orientações desejadas:')
							MetafenômenoAgente = oraçãoProjetada()

						elif realizacao_metafenômeno == 'oração_que':
							print('Selecione orientações desejadas')
							MetafenômenoAgente = 'que' + ' ' + oraçãoProjetada()
						else:
							print('Selecione o GN com oração qualificadora:')
							MetafenômenoAgente = estrutura_GN()

						Polaridade = POLARIDADE()
						Circunstância = circunstância()
						oração = Tema_interpessoal + ' ' + Tema_textual + ' ' \
						         + MetafenômenoAgente + ' ' + Polaridade + ' ' \
						         + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'

				elif TIPO_INFERIOR == 'perceptivo' and TIPO_HIPERFENÔMENO == 'reativo':
					print('Qual o tipo_pessoa de reativo?')
					TIPO_reativo = choice.Menu(['macrofenômeno']).ask()
					if TIPO_reativo == 'macrofenômeno':
						print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual o Experienciador (Ente:Humanizado)?')
					Experienciador = estrutura_GN()
					print('Qual o macrofenômeno? Macrofenômenos têm natureza concreta')
					realizacao_macrofenômeno = choice.Menu(
						['não_finito_concretizado', 'não-orientado_gerúndio', 'oração_que',
						 'GN+oração_qualificadora']).ask()
					if realizacao_macrofenômeno == 'não_finito_concretizado':
						print('Selecione grupo verbal não-finito_concretizado')
						MacrofenômenoAgente = oraçãoProjetada()

					elif realizacao_macrofenômeno == 'não-orientado_gerúndio':
						print('Selecione grupo verbal não-orientado_gerúndio')
						MacrofenômenoAgente = oraçãoProjetada()
					elif realizacao_macrofenômeno == 'oração_que':
						print('Selecione orientações desejadas')
						MacrofenômenoAgente = 'que' + ' ' + oraçãoProjetada()
					else:
						print('Selecione o GN com oração qualificadora:')
						Macrofenômeno = estrutura_GN() \
 \
					Polaridade = POLARIDADE()
					Circunstância = circunstância() \
					oração = Tema_interpessoal + ' ' + Tema_textual \
					         + ' ' + MacrofenômenoAgente + ' ' + Polaridade + ' ' \
					         + Processo + ' ' + Experienciador + ' ' + Circunstância + '.'


	##ORAÇÃO verbal

	elif Transitividade == 'PR_Verbal_AG_médio_sem_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Qual a Ordem do Dizente?')
		ORDEM_DO_DIZENTE = choice.Menu(['atividade', 'semioticidade']).ask()
		if ORDEM_DO_DIZENTE == 'atividade':
			TIPO_ATIVIDADE = 'fala'

			if TIPO_ATIVIDADE == 'fala':

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Dizente?')
				Dizente = estrutura_GN()
				print('Há Receptor?')
				print('Selecione a Receptividade') \
				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
				if RECEPTIVIDADE == '+receptor':
					Receptor = frase_preposicional()
				else:
					Receptor = ''
				Polaridade = POLARIDADE() \
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
				         + ' ' + Receptor + ' ' + Circunstância + '.'
				# Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...


		elif ORDEM_DO_DIZENTE == 'semioticidade':
			print('Semioticidade em Médio sem alcance = não_projeção')
			TIPO_SEMIOTICIDADE = choice.Menu(['não_projeção']).ask()

			if TIPO_SEMIOTICIDADE == 'não_projeção':
				print('Não-projeção + médio sem alcance = -verbiagem')
				TIPO_NÃO_PROJEÇÃO = '-verbiagem'
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Dizente?')
				Dizente = estrutura_GN()
				print('Há Receptor?')
				print('Selecione a Receptividade')
				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
				if RECEPTIVIDADE == '+receptor':
					Receptor = frase_preposicional()
				else:
					Receptor = ''
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_Verbal_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Qual a Ordem do Dizente?')
		ORDEM_DO_DIZENTE = choice.Menu(['semioticidade']).ask()
		print('Selecione a Receptividade')
		RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()

		if ORDEM_DO_DIZENTE == 'semioticidade':
			print('Selecione o tipo_pessoa de Semioticidade')

			TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
			if TIPO_SEMIOTICIDADE == 'projeção':
				print('Selecione o tipo_pessoa de projeção')
				TIPO_PROJEÇÃO = choice.Menu(['citativa', 'relativa']).ask()
				if TIPO_PROJEÇÃO == 'citativa':
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Dizente?')
					Dizente = estrutura_GN()
					print('Há Receptor?')
					print('Selecione a Receptividade')
					RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
					if RECEPTIVIDADE == '+receptor':
						Receptor = frase_preposicional()
					else:
						Receptor = ''
					Polaridade = POLARIDADE()
					print('Qual a oração projetada?')
					Circunstância = circunstância()
					Oração_projetada = oraçãoProjetada()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
					         + ' ' + Receptor + '"' + Oração_projetada + '" ' + ' ' + Circunstância + '.'
					# Ex.: Eu disse a ele "Eu comi o bolo".

				elif TIPO_PROJEÇÃO == 'relativa':
					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Dizente?')
					Dizente = estrutura_GN()
					print('Há Receptor?')
					print('Selecione a Receptividade')
					RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
					if RECEPTIVIDADE == '+receptor':
						Receptor = frase_preposicional()
					else:
						Receptor = ''
					Polaridade = POLARIDADE()
					print('Qual a oração projetada?')
					Oração_projetada = oraçãoProjetada()
					Circunstância = circunstância()

					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
					         + ' ' + Receptor + ' ' + 'que' + ' ' + '"' + Oração_projetada + '" ' + ' ' + Circunstância + '.'
					# Ex.: Eu disse a ele que "Eu comi o bolo".

			elif TIPO_SEMIOTICIDADE == 'não_projeção':
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Dizente?')
				Dizente = estrutura_GN()
				print('Qual é a Verbiagem?')
				Verbiagem = estrutura_GN()
				print('Há Receptor?')
				print('Selecione a Receptividade')
				RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
				if RECEPTIVIDADE == '+receptor':
					Receptor = frase_preposicional()
				else:
					Receptor = ''
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
				         + ' ' + Verbiagem + ' ' + Receptor + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_Verbal_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE()
		print('Qual é o Dizente?')
		Dizente = estrutura_GN()
		Circunstância = circunstância()

		print('O Alvo é realizado por grupo nominal ou frase preposicional?')
		realizacao_alvo = choice.Menu(['GN', 'FP']).ask()
		if realizacao_alvo == 'GN':
			print('Qual é o Alvo?')
			Alvo = estrutura_GN()
			print('Qual a localização do alvo na oração (em relação ao Processo)?')
			localização_alvo = choice.Menu(['ante_processo', 'pós_processo']).ask()
			if localização_alvo == 'ante_processo':
				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' \
				         + Alvo + ' ' + Processo + ' ' + Circunstância + '.'
			else:
				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Alvo + ' ' + Circunstância + '.' \
		else:
			print('Qual é o Alvo?')
			Alvo = frase_preposicional()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Alvo + ' ' + Circunstância + '.'


	elif Transitividade == 'PR_Verbal_AG_efetivo_receptivo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE()
		print('Qual é o Dizente?')
		Dizente = frase_preposicional()
		print('Qual é o Alvo?')
		Alvo = estrutura_GN()
		Circunstância = circunstância()

		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Alvo + ' ' + Polaridade + ' ' + Processo \
		         + ' ' + Dizente + ' ' + Circunstância + '.'

	###MATERIAL

	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()

		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		print('Qual é a Meta?')
		Meta = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
		else:
			Iniciador = ''

		print('Há resultado do processo?')
		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask() \
 \
		if TIPO_DE_RESULTADO == 'elaboração':

			print('há Resultado_elaboração atributo ou papel?')
			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
			if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
					RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
				realizacao_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
				if realizacao_atributo == 'adjetivo':
					Atributo = adjetivo_modificador()
				elif realizacao_atributo == 'frase_preposicional':
					Atributo = frase_preposicional()
			elif RESULTADO_QUALITATIVO == '-resultado':
				Atributo = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '.'

		elif TIPO_DE_RESULTADO == 'extensão':
			print('Há Participante Beneficiário na oração?')
			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
			if RECEPÇÃO == '+beneficiário':
				Beneficiário = frase_preposicional()
			elif RECEPÇÃO == '-beneficiário':
				Beneficiário = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		print('Qual é a Meta?')
		Meta = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN()
		else:
			Iniciador = ''

		print(
			'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
		CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

		if CLIENTE == '+cliente':
			Cliente = frase_preposicional()
		else:
			Cliente = ''

		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
		         + ' ' + Meta + ' ' + Cliente + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()
		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN() + grupo_verbal()
		else:
			Iniciador = ''
		print('Há Participante Beneficiário na oração?')
		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
		if RECEPÇÃO == '+beneficiário':
			Beneficiário = frase_preposicional()
		elif RECEPÇÃO == '-beneficiário':
			Beneficiário = ''
		print('Há resultado do processo?')
		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
		if TIPO_DE_RESULTADO == 'elaboração':
			print('Qual é o Escopo?')
			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
			if tipo_Escopo == 'escopo(processo)':
				Escopo = estrutura_GN()
			elif tipo_Escopo == 'escopo(entidade)':
				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Escopo + ' ' + Beneficiário + ' ' + Circunstância + '.'

		elif TIPO_DE_RESULTADO == 'intensificação':
			print('Qual é o Escopo?')
			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
			if tipo_Escopo == 'escopo(processo)':
				Escopo = estrutura_GN()
			elif tipo_Escopo == 'escopo(entidade)':
				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
			print('Há resultado locativo?')
			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
			if realizacao_locativo == 'sim':
				Resultado_locativo = frase_preposicional()
			else:
				Resultado_locativo = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Beneficiário + ' ' + Circunstância + '.'


	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA': \
 \
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()
		print('Há Participante Beneficiário na oração?')
		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
		if RECEPÇÃO == '+beneficiário':
			Beneficiário = frase_preposicional()
		elif RECEPÇÃO == '-beneficiário':
			Beneficiário = ''
		print('Há resultado do processo?')
		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
		if TIPO_DE_RESULTADO == 'elaboração':
			print('Orações médio_sem_alcance  selecionam -escopo')
			Escopo = ''
			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Beneficiário + '' + Circunstância + '.'


		elif TIPO_DE_RESULTADO == 'intensificação':
			print('Orações médio_sem_alcance selecionam -escopo')
			print('Há Participante Beneficiário na oração?')
			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
			if RECEPÇÃO == '+beneficiário':
				Beneficiário = frase_preposicional()
			elif RECEPÇÃO == '-beneficiário':
				Beneficiário = ''
			print('Há resultado locativo?')
			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
			if realizacao_locativo == 'sim':
				Resultado_locativo = frase_preposicional()
			else:
				Resultado_locativo = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Resultado_locativo + ' ' + Circunstância + ' ' + Beneficiário + '.'


	##MATERIAL METEOROLÓGICA
	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
			and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()

		print('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE()
		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN()
		else:
			Iniciador = ''
		print('Há Participante Beneficiário na oração?')
		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
		if RECEPÇÃO == '+beneficiário':
			Beneficiário = frase_preposicional()
		elif RECEPÇÃO == '-beneficiário':
			Beneficiário = ''
		tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
		print('Qual o tipo_pessoa de inTransitividade?')
		if tipo_intransitiva == 'impessoal(fenômeno_natural)':
			print('Há escopo?')
			escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
			if escopo_intransitiva == '+escopo':
				print('Qual estrutura realiza o escopo?')
				realizacao_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
				if realizacao_escopo == 'frase_preposicional':
					Escopo = frase_preposicional()
				elif realizacao_escopo == 'grupo_nominal':
					Escopo = estrutura_GN()
			elif escopo_intransitiva == '-escopo':
				Escopo = ''

		Circunstância = circunstância()

		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
		         + ' ' + Escopo + ' ' + Beneficiário + ' ' + Circunstância + '.'


	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		Tema_textual = TEMA_TEXTUAL() \
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		Polaridade = POLARIDADE()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN() + grupo_verbal()
		else:
			Iniciador = ''
		print('Há Participante Beneficiário na oração?')
		RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
		if RECEPÇÃO == '+beneficiário':
			Beneficiário = frase_preposicional()
		elif RECEPÇÃO == '-beneficiário':
			Beneficiário = ''
		Circunstância = circunstância()
		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
		         + ' ' + Processo + ' ' + Beneficiário + ' ' + Circunstância + '.'

		##########COMEÇO DE AGENCIAMENTO PASSIVA
		# (E CONSEQUENTEMENTE MUDANÇA NO TEMA IDEACIONAL: COMPLEMENTO ELEMENTAL)

	#  elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
	#          and Tema_id == 'TID_complemento_elemental':
	#      Tema_interpessoal = TEMA_INTERPESSOAL()
	#      Tema_textual=TEMA_TEXTUAL()
	#
	#      print ('Qual o Processo?')
	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
	#      print('Qual é a Meta?')
	#      Meta = estrutura_GN()
	#      Polaridade = POLARIDADE ()
	#      Circunstância = circunstância()
	#      print('Há Participante Beneficiário na oração?')
	#      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
	#      if RECEPÇÃO == '+beneficiário':
	#          Beneficiário = frase_preposicional()
	#      elif RECEPÇÃO == '-beneficiário':
	#          Beneficiário = ''
	#      print ('Há Participante Iniciador na oração?')
	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
	#      if INICIADOR == '+iniciador':
	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
	#      else:
	#          Iniciador = ''
	#
	#      print ('O Ator/Agente é realizado na oração?')
	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
	#      if realizacao_Ator == '+ator/agente':
	#          print('Qual é o Ator/Agente?')
	#          Ator = frase_preposicional()
	#      elif realizacao_Ator == '-ator/agente':
	#          Ator = ''
	#      print ('Há resultado do processo?')
	#      TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
	#
	#      if TIPO_DE_RESULTADO == 'elaboração':
	#
	#          print ('há Resultado_elaboração atributo ou papel?')
	#          RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
	#          if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
	#              RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
	#              realizacao_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
	#              if realizacao_atributo == 'adjetivo':
	#                  Atributo = adjetivo_modificador ()
	#              elif realizacao_atributo == 'frase_preposicional':
	#                  Atributo = frase_preposicional()
	#          elif RESULTADO_QUALITATIVO == '-resultado':
	#              Atributo = ''
	#
	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
	#                   + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' +Beneficiário+' '+ Circunstância +'.'
	#
	#      elif TIPO_DE_RESULTADO == 'extensão':
	#          print ('Há Participante Beneficiário na oração?')
	#          RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
	#          if RECEPÇÃO == '+beneficiário':
	#              Beneficiário = frase_preposicional()
	#          elif RECEPÇÃO == '-beneficiário':
	#              Beneficiário = ''
	#
	#
	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
	#                   + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +' '+Beneficiário+' '+ Circunstância +'.'
	#
	# ##
	#
	#  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
	#          and Tema_id == 'TID_complemento_elemental':
	#
	#      Tema_interpessoal = TEMA_INTERPESSOAL()
	#      Tema_textual=TEMA_TEXTUAL()
	#
	#      print ('Qual o Processo?')
	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
	#      print('Qual é a Meta?')
	#      Meta = estrutura_GN()
	#      Polaridade = POLARIDADE ()
	#      print('Há Participante Beneficiário na oração?')
	#      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
	#      if RECEPÇÃO == '+beneficiário':
	#          Beneficiário = frase_preposicional()
	#      elif RECEPÇÃO == '-beneficiário':
	#          Beneficiário = ''
	#      Circunstância = circunstância()
	#
	#
	#      print ('Há Participante Iniciador na oração?')
	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
	#      if INICIADOR == '+iniciador':
	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
	#      else:
	#          Iniciador = ''
	#
	#      print ('O Ator/Agente é realizado na oração?')
	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
	#      if realizacao_Ator == '+ator/agente':
	#          print('Qual é o Ator/Agente?')
	#          Ator = frase_preposicional()
	#      elif realizacao_Ator == '-ator/agente':
	#          Ator = ''
	#
	#
	#      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
	#      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
	#
	#      if CLIENTE == '+cliente':
	#          Cliente = frase_preposicional()
	#      elif CLIENTE == '-cliente':
	#          Cliente='' \
	#
	#      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
	#               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Beneficiário+' '+Circunstância +'.'

	###RELACIONAl
	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
		## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()

		print('Qual o tipo_pessoa de especificação de associação?')
		tipo_especificação_associação = choice.Menu(['entidade', 'qualidade']).ask()
		print('Qual a fase da atribuição?')
		fase_atribuição = choice.Menu(['neutra',
		                               'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
		###não vou especializar os tipos de fase.
		print('Qual o domínio da atribuição')
		domínio_atribuição = choice.Menu(['material', 'semiótico']).ask()

		if (
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador?')
			Portador = estrutura_GN() \
			print('Qual o Atributo?')
			Atributo = estrutura_GN()

			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Atributo + ' ' + Circunstância + '.'

		elif (
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador?') \
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = adjetivo_modificador()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
			# o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
			##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Atributo + ' ' + Circunstância + '.'


	###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
	##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva
	# (há a possibilidade de Agente de segunda, terceira.....ordem)

	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Atribuidor?')
			Atribuidor = estrutura_GN()
			print('Qual o Portador?')
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)

			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Portador + ' ' + Atributo + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Atribuidor?')
			Atribuidor = frase_preposicional()
			print('Qual o Portador?')
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)

			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo
			+ ' ' + Atributo + ' ' + Atribuidor + ' ' + Circunstância + '.'


	####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)

	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação':
		print('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito '
		      'deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

		if direcionalidade_voz == 'meio_operativa':
			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente'
			      'o elemento em posição temática)')
			# (confluência do Símbolo/Identificado) =
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '.'

		elif direcionalidade_voz == 'meio_receptiva':
			print('Neste caso, o Valor/Identificador conflui com o Sujeito')
			##NESTE CASO, confluência de Valor/Sujeito

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL() \
 \
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Símbolo + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação':

		print(
			'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

		if direcionalidade_voz == 'meio_operativa':
			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')

			# (confluência do Símbolo/Identificador/Sujeito) =
			# (Valor/Identificado/complemento)

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Valor + ' ' + Circunstância + '.'

		elif direcionalidade_voz == 'meio_receptiva':
			print('Neste caso, o Valor conflui com o Sujeito')
			##NESTE CASO, confluência de Valor/Identificado/Sujeito
			##(Símbolo/Identificador/Complemento)

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Símbolo + ' ' + Circunstância + '.'

	####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)

	#    ###TRUE_Efetiva_operativa
	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas) \
		# POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Designador?')
			Designador = estrutura_GN()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()  ##ou frase preposicional?
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + ' ' + Circunstância + '.'
			###rever possíveis estruturas para este tipo_pessoa de oração(pode haver 2 processos?)

	###TRUE_Efetiva_receptiva

	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Designador?')
			Designador = frase_preposicional()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()  ##ou frase preposicional?
			Polaridade = POLARIDADE()
			Circunstância = circunstância()
			#
			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Valor + ' ' + Designador + ' ' + Circunstância + '.'
	####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realizacao de cada participante;
	#        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)

	# POSSESSIVO ATRIBUTIV0

	if Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()

		if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':

			realizacao_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()

			if realizacao_atributo == 'grupo_nominal_possessivo':

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Posse?')
				Portador_Posse = estrutura_GN()
				print('Qual é o Atributo/Possuidor?')
				Atributo_Possuidor = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '.'

			elif realizacao_atributo == 'frase_preposicional':
				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Posse?')
				Portador_Posse = estrutura_GN()
				print('Qual é o Atributo/Possuidor?')
				Atributo_Possuidor = frase_preposicional()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '.'


		elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':

			##VERBO TER/POSSUIR/

			tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask() \
 \
			if tipo_possuidor == 'possuidor_portador':

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Possuidor?')
				Portador_Possuidor = estrutura_GN()
				print('Qual é o Atributo/Posse?')
				Atributo_Posse = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Atributo_Posse + ' ' + Circunstância + '.'


			###VERBOS PERTENCER A/...

			elif tipo_possuidor == 'possuidor_atributo':

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Possuidor?')
				Portador_Posse = estrutura_GN()
				print('Qual é o Atributo/Posse?')
				Atributo_Possuidor = frase_preposicional()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '.'

		# POSSESSIVO IDENTIFICATIVO


	elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()

		if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')

				print(
					'Escolha o tipo_pessoa de realizacao do Valor:')
				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

				if realizacao_Valor == 'grupo_nominal':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)/Possuído?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)/Possuidor?')
					Valor_Possuidor = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O piano é seu
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '.'

				elif realizacao_Valor == 'frase_preposicional':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)?')
					Valor_Possuidor = frase_preposicional()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O piano é do André
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '.'


			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')

				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

				if realizacao_Valor == 'grupo_nominal':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)/Possuído?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)/Possuidor?')
					Valor_Possuidor = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O seu é o piano
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '.'

				elif realizacao_Valor == 'frase_preposicional':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)?')
					Valor_Possuidor = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O do André é o piano
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '.'

		elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
			## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
			##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print(
					'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)/Possuidor?')
				Símbolo_Possuidor = estrutura_GN()
				print('Qual o Valor(Value)/Possuído?')
				Valor_Possuído = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: O produto contém plástico, Eles merecem a aposentadoria

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Valor_Possuído + ' ' + Circunstância + '.'



			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')

				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

				if realizacao_Valor == 'grupo_nominal':
					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()  ##na passiva
					print('Qual o Valor(Value)/Possuído?')
					Valor_Possuído = estrutura_GN()
					print('Qual é o Símbolo(Token)/Possuidor?')
					Símbolo_Possuidor = frase_preposicional()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O seu é o piano
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Símbolo_Possuidor + ' ' + Circunstância + '.'


	#####RELACIONAL CIRCUNSTANCIAL

	elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		print('Qual o tipo_pessoa de realizacao da Relacional Circunstancial?')
		TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()

		if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador')
			Portador = estrutura_GN()
			print('Qual é o Atributo Circunstancial?')
			Atributo_Circunstancial = circunstância()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			# Ex.: O livro é sobre a IIGuerra

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Atributo_Circunstancial + ' ' + Circunstância + '.'

		elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador')
			Portador = estrutura_GN()
			print('Qual é o Atributo Circunstancial?')
			Atributo = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			# Ex.: O livro retrata a IIGuerra
			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Atributo + ' ' + Circunstância + '.'

	elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		print('O significado circunstancial é realixado no participante ou no processo?')
		TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
			['participante_circunstancial', 'processo_circunstancial']).ask()

		if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()
				print('Qual o Valor(Value)?')
				Valor = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: Amanhá é dia 10

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo \
				         + ' ' + Valor + ' ' + Circunstância + '.'


			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, há confluência Valor/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()
				print('Qual o Valor(Value)?')
				Valor = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.:dia 10 é Amanhá

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '.'


		elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()
				print('Qual o Valor(Value)?')
				Valor = circunstância()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: A feira dura o dia

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '.'


			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, há confluência Valor/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()  ## reiterações-verbo na passiva
				print('Qual o Valor(Value)?')
				Valor = circunstância()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()

				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: O dia inteiro é ocupado pela feira

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '.'

	##ORAÇÃO EXISTENCIAL

	elif Transitividade == 'PR_Existencial_AG_NA' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
			and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()

		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Existente?')
		Existente = estrutura_GN()
		Circunstância = circunstância()

		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Processo + ' ' + Existente + ' ' + Circunstância + '.'

	#
	##
	###
	######
	####### ORAÇÕES INTERROGATIVAS POLARES

	##ORAÇÃO MATERIAL MODO INTERROGATIVO POLAR

	elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()

		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		print('Qual é a Meta?')
		Meta = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
		else:
			Iniciador = ''

		print('Há resultado do processo?')
		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()

		if TIPO_DE_RESULTADO == 'elaboração':

			print('há Resultado_elaboração atributo ou papel?')
			RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
			if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
					RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
				realizacao_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
				if realizacao_atributo == 'adjetivo':
					Atributo = adjetivo_modificador()
				elif realizacao_atributo == 'frase_preposicional':
					Atributo = frase_preposicional()
			elif RESULTADO_QUALITATIVO == '-resultado':
				Atributo = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '?'



		elif TIPO_DE_RESULTADO == 'extensão':
			print('Há Participante Beneficiário na oração?')
			RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
			if RECEPÇÃO == '+beneficiário':
				Beneficiário = frase_preposicional()
			elif RECEPÇÃO == '-beneficiário':
				Beneficiário = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + ' ' + Circunstância + '?'


	elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		print('Qual é a Meta?')
		Meta = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN()
		else:
			Iniciador = ''

		print(
			'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
		CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

		if CLIENTE == '+cliente':
			Cliente = frase_preposicional()
		else:
			Cliente = ''

		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
		         + ' ' + Processo + ' ' + Meta + ' ' + Cliente + ' ' + Circunstância + '?'


	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()

		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN() + grupo_verbal()
		else:
			Iniciador = ''

		print('Há resultado do processo?')
		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
		if TIPO_DE_RESULTADO == 'elaboração':
			print('Qual é o Escopo?')
			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
			if tipo_Escopo == 'escopo(processo)':
				Escopo = estrutura_GN()
			elif tipo_Escopo == 'escopo(entidade)':
				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Escopo + ' ' + Circunstância + '?'

		elif TIPO_DE_RESULTADO == 'intensificação':
			print('Qual é o Escopo?')
			tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
			if tipo_Escopo == 'escopo(processo)':
				Escopo = estrutura_GN()
			elif tipo_Escopo == 'escopo(entidade)':
				Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
			print('Há resultado locativo?')
			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
			if realizacao_locativo == 'sim':
				Resultado_locativo = frase_preposicional()
			else:
				Resultado_locativo = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Circunstância + '?'


	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()
		print('Há resultado do processo?')
		TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
		if TIPO_DE_RESULTADO == 'elaboração':
			print('Orações médio_sem_alcance  selecionam -escopo')
			Escopo = ''

		elif TIPO_DE_RESULTADO == 'intensificação':
			print('Orações médio_sem_alcance selecionam -escopo')

			print('Há resultado locativo?')
			realizacao_locativo = choice.Menu(['sim', 'não']).ask()
			if realizacao_locativo == 'sim':
				Resultado_locativo = frase_preposicional()
			else:
				Resultado_locativo = ''

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Resultado_locativo + ' ' + Circunstância + '?'


	##ORAÇÃO METEOROLÓGICA MODO INTERROGATIVO POLAR
	elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
			and Modo == 'sujeitabilidade_recuperação_NA_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()

		tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
		print('Qual o tipo_pessoa de inTransitividade?')
		if tipo_intransitiva == 'impessoal(fenômeno_natural)':
			print('Há escopo?')
			escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
			if escopo_intransitiva == '+escopo':
				print('Qual estrutura realiza o escopo?')
				realizacao_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
				if realizacao_escopo == 'frase_preposicional':
					Escopo = frase_preposicional()
				elif realizacao_escopo == 'grupo_nominal':
					Escopo = estrutura_GN()
			elif escopo_intransitiva == '-escopo':
				Escopo = ''
		print('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()

		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN()
		else:
			Iniciador = ''
		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
		         + ' ' + Escopo + ' ' + Circunstância + '?'


	elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()
		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Ator?')
		Ator = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()
		print('Há Participante Iniciador na oração?')
		INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
		if INICIADOR == '+iniciador':
			Iniciador = estrutura_GN() + grupo_verbal()
		else:
			Iniciador = ''

		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
		         + ' ' + Processo + ' ' + Circunstância + '?'

		##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)

	#  elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'\
	#          and Tema_id == 'TID_complemento_elemental':
	#      Tema_interpessoal = TEMA_INTERPESSOAL()
	#      Tema_textual=TEMA_TEXTUAL()
	#
	#      print ('Qual o Processo?')
	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
	#      print('Qual é a Meta?')
	#      Meta = estrutura_GN()
	#      Polaridade = POLARIDADE ()
	#      Circunstância = circunstância()
	#      print ('Há Participante Iniciador na oração?')
	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
	#      if INICIADOR == '+iniciador':
	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
	#      else:
	#          Iniciador = ''
	#
	#      print ('O Ator/Agente é realizado na oração?')
	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
	#      if realizacao_Ator == '+ator/agente':
	#          print('Qual é o Ator/Agente?')
	#          Ator = frase_preposicional()
	#      elif realizacao_Ator == '-ator/agente':
	#          Ator = ''
	#
	#
	#      print ('Há resultado do processo?')
	#      TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
	#
	#      if TIPO_DE_RESULTADO == 'elaboração':
	#
	#          print ('há Resultado_elaboração atributo ou papel?')
	#          RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
	#          if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
	#              RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
	#              realizacao_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
	#              if realizacao_atributo == 'adjetivo':
	#                  Atributo = adjetivo_modificador ()
	#              elif realizacao_atributo == 'frase_preposicional':
	#                  Atributo = frase_preposicional()
	#          elif RESULTADO_QUALITATIVO == '-resultado':
	#              Atributo = ''
	#
	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta \
	#                   + ' ' + Polaridade + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' + Circunstância +'?'
	#
	#      elif TIPO_DE_RESULTADO == 'extensão':
	#          print ('Há Participante Beneficiário na oração?')
	#          RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
	#          if RECEPÇÃO == '+beneficiário':
	#              Beneficiário = frase_preposicional()
	#          elif RECEPÇÃO == '-beneficiário':
	#              Beneficiário = ''
	#
	#
	#          oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
	#                   + Meta + ' ' + Polaridade + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +' ' + Circunstância +'?'
	#
	# ##
	#
	#  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
	#          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar'\
	#          and Tema_id == 'TID_complemento_elemental':
	#
	#      Tema_interpessoal = TEMA_INTERPESSOAL()
	#      Tema_textual=TEMA_TEXTUAL()
	#
	#      print ('Qual o Processo?')
	#      Processo = grupo_verbal() ##selecionar agenciado_passivo
	#      print('Qual é a Meta?')
	#      Meta = estrutura_GN()
	#      Polaridade = POLARIDADE ()
	#      Circunstância = circunstância()
	#
	#      print ('Há Participante Iniciador na oração?')
	#      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
	#      if INICIADOR == '+iniciador':
	#          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realizacao básica)
	#      else:
	#          Iniciador = ''
	#
	#      print ('O Ator/Agente é realizado na oração?')
	#      realizacao_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
	#      if realizacao_Ator == '+ator/agente':
	#          print('Qual é o Ator/Agente?')
	#          Ator = frase_preposicional()
	#      elif realizacao_Ator == '-ator/agente':
	#          Ator = ''
	#
	#
	#      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
	#      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
	#
	#      if CLIENTE == '+cliente':
	#          Cliente = frase_preposicional()
	#      elif CLIENTE == '-cliente':
	#          Cliente=''
	#
	#      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' '\
	#               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Circunstância +'?'
	#

	###RELACIONAl MODO INTERROGATIVO POLAR

	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
		## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
		Tema_textual = TEMA_TEXTUAL()
		Tema_interpessoal = TEMA_INTERPESSOAL()

		print('Qual o tipo_pessoa de especificação de associação?')
		tipo_especificação_associação = choice.Menu(['entidade', 'qualidade']).ask()
		print('Qual a fase da atribuição?')
		fase_atribuição = choice.Menu(['neutra',
		                               'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
		###não vou especializar os tipos de fase.
		print('Qual o domínio da atribuição')
		domínio_atribuição = choice.Menu(['material', 'semiótico']).ask()

		if (
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador?')
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = estrutura_GN()

			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Atributo + ' ' + Circunstância + '?'

		elif (
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
				tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador?')
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = adjetivo_modificador()  ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
			# o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
			##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Atributo + ' ' + Circunstância + '?'


	###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
	##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva (há a possibilidade de Agente de segunda, terceira.....ordem)
	####para desenvolver....
	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Atribuidor?')
			Atribuidor = estrutura_GN()
			print('Qual o Portador?')
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)

			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Atribuidor + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Portador + ' ' + Atributo + ' ' + Circunstância + '?'

	elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Atribuidor?')
			Atribuidor = frase_preposicional()

			print('Qual o Portador?')
			Portador = estrutura_GN()
			print('Qual o Atributo?')
			Atributo = estrutura_GN()  ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar)

			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Atributo + ' ' + Atribuidor + ' ' + Circunstância + '?'


	####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)

	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação':
		print('Apesar de Médio(middle), a direcionalidade_voz '
		      'do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina '
		      'se é operativa ou receptiva. Selecione a direcionalidade:')
		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

		if direcionalidade_voz == 'meio_operativa':
			print('Neste caso, o Símbolo/Identificado conflui com o '
			      'Sujeito(geralmente o elemento em posição temática')

			# (confluência do Símbolo/Identificado) =

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'



		elif direcionalidade_voz == 'meio_receptiva':
			print('Neste caso, o Valor/Identificador conflui com o Sujeito')
			##NESTE CASO, confluência de Valor/Sujeito

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'



	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação':

		print(
			'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
		direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

		if direcionalidade_voz == 'meio_operativa':
			print('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')

			# (confluência do Símbolo/Identificador/Sujeito) =
			# (Valor/Identificado/complemento)

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'

		elif direcionalidade_voz == 'meio_receptiva':
			print('Neste caso, o Valor conflui com o Sujeito')
			##NESTE CASO, confluência de Valor/Identificado/Sujeito
			##(Símbolo/Identificador/Complemento)

			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'


	####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)

	#    ###TRUE_Efetiva_operativa
	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		# POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Designador?')
			Designador = estrutura_GN()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()  ##ou frase preposicional?
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Designador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Símbolo + ' ' + Valor + ' ' + Circunstância + '?'
			###rever possíveis estruturas para este tipo_pessoa de oração(pode haver 2 processos?)

	###TRUE_Efetiva_receptiva

	elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		print('Qual o tipo_pessoa de atribuição de relação?')
		tipo_atribuição_relação = atribuição_de_relação()
		##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
		# elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
		##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO

		if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
		    tipo_atribuição_relação == 'atribuição_proj_ment_desiderativa',
		    tipo_atribuição_relação == 'atribuição_proj_verbal',
		    tipo_atribuição_relação == 'atribuição_expan_elaboração',
		    tipo_atribuição_relação == 'atribuição_expan_intencificação'):
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()

			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual é o Designador?')
			Designador = frase_preposicional()
			print('Qual é o Símbolo(Token)?')
			Símbolo = estrutura_GN()
			print('Qual o Valor(Value)?')
			Valor = estrutura_GN()  ##ou frase preposicional?
			Polaridade = POLARIDADE()
			Circunstância = circunstância()
			#
			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Valor + ' ' + Designador + ' ' + Circunstância + '?'
	####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realizacao de cada participante;
	#        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)

	# POSSESSIVO ATRIBUTIV0

	elif Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu(['posse_atributo', 'posse_processo']).ask()

		if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':

			realizacao_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()

			if realizacao_atributo == 'grupo_nominal_possessivo':

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Posse?')
				Portador_Posse = estrutura_GN()
				print('Qual é o Atributo/Possuidor?')
				Atributo_Possuidor = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse \
				         + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '?'

			elif realizacao_atributo == 'frase_preposicional':
				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Posse?')
				Portador_Posse = estrutura_GN()
				print('Qual é o Atributo/Possuidor?')
				Atributo_Possuidor = frase_preposicional()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '?'


		elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':

			##VERBO TER/POSSUIR/

			tipo_possuidor = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask()

			if tipo_possuidor == 'possuidor_portador':

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Possuidor?')
				Portador_Possuidor = estrutura_GN()
				print('Qual é o Atributo/Posse?')
				Atributo_Posse = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()
				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Possuidor \
				         + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Posse + ' ' + Circunstância + '?'
			###VERBOS PERTENCER A/...

			elif tipo_possuidor == 'possuidor_atributo':

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()
				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual o Portador/Possuidor?')
				Portador_Posse = estrutura_GN()
				print('Qual é o Atributo/Posse?')
				Atributo_Possuidor = frase_preposicional()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador_Posse + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Atributo_Possuidor + ' ' + Circunstância + '?'

		# POSSESSIVO IDENTIFICATIVO


	elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu(['posse_participante', 'posse_processo']).ask()

		if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')

				print(
					'Escolha o tipo_pessoa de realizacao do Valor:')
				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

				if realizacao_Valor == 'grupo_nominal':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)/Possuído?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)/Possuidor?')
					Valor_Possuidor = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O piano é seu
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '?'

				elif realizacao_Valor == 'frase_preposicional':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)?')
					Valor_Possuidor = frase_preposicional()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O piano é do André
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuído + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Valor_Possuidor + ' ' + Circunstância + '?'


			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')

				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

				if realizacao_Valor == 'grupo_nominal':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)/Possuído?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)/Possuidor?')
					Valor_Possuidor = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O seu é o piano
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '?'

				elif realizacao_Valor == 'frase_preposicional':

					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()
					print('Qual é o Símbolo(Token)?')
					Símbolo_Possuído = estrutura_GN()
					print('Qual o Valor(Value)?')
					Valor_Possuidor = estrutura_GN()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O do André é o piano
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuidor \
					         + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído + ' ' + Circunstância + '?'

		elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
			## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
			##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print(
					'Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)/Possuidor?')
				Símbolo_Possuidor = estrutura_GN()
				print('Qual o Valor(Value)/Possuído?')
				Valor_Possuído = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: O produto contém plástico, Eles merecem a aposentadoria

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo_Possuidor \
				         + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuído + ' ' + Circunstância + '?'



			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')

				realizacao_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()

				if realizacao_Valor == 'grupo_nominal':
					Tema_textual = TEMA_TEXTUAL()
					Tema_interpessoal = TEMA_INTERPESSOAL()

					print('Qual o Processo?')
					Processo = grupo_verbal()  ##na passiva
					print('Qual o Valor(Value)/Possuído?')
					Valor_Possuído = estrutura_GN()
					print('Qual é o Símbolo(Token)/Possuidor?')
					Símbolo_Possuidor = frase_preposicional()
					Polaridade = POLARIDADE()
					Circunstância = circunstância()

					# Ex.: O seu é o piano
					oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor_Possuído + ' ' + Polaridade \
					         + ' ' + Processo + ' ' + Símbolo_Possuidor + ' ' + Circunstância + '?'


	#####RELACIONAL CIRCUNSTANCIAL MODO INTERROGATIVO POLAR

	elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
		print('Qual o tipo_pessoa de realizacao da Relacional Circunstancial?')
		TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()

		if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador')
			Portador = estrutura_GN()
			print('Qual é o Atributo Circunstancial?')
			Atributo_Circunstancial = circunstância()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			# Ex.: O livro é sobre a IIGuerra

			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade \
			         + ' ' + Processo + ' ' + Atributo_Circunstancial + ' ' + Circunstância + '?'

		elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
			Tema_textual = TEMA_TEXTUAL()
			Tema_interpessoal = TEMA_INTERPESSOAL()
			print('Qual o Processo?')
			Processo = grupo_verbal()
			print('Qual o Portador')
			Portador = estrutura_GN()
			print('Qual é o Atributo Circunstancial?')
			Atributo = estrutura_GN()
			Polaridade = POLARIDADE()
			Circunstância = circunstância()

			# Ex.: O livro retrata a IIGuerra
			oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo \
			         + ' ' + Atributo + ' ' + Circunstância + '?'




	elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		print('O significado circunstancial é realixado no participante ou no processo?')
		TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu(
			['participante_circunstancial', 'processo_circunstancial']).ask()

		if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()
				print('Qual o Valor(Value)?')
				Valor = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: Amanhá é dia 10

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'


			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, há confluência Valor/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()
				print('Qual o Valor(Value)?')
				Valor = estrutura_GN()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.:dia 10 é Amanhá

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'


		elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':

			print(
				'Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo_pessoa de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
			direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

			if direcionalidade_voz == 'meio_operativa':
				print('Neste caso, há confluência Símbolo/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()
				print('Qual o Valor(Value)?')
				Valor = circunstância()
				Polaridade = POLARIDADE()
				Circunstância = circunstância()

				# Ex.: A feira dura o dia inteiro

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Valor + ' ' + Circunstância + '?'


			elif direcionalidade_voz == 'meio_receptiva':
				print('Neste caso, há confluência Valor/Sujeito/Identificado')

				Tema_textual = TEMA_TEXTUAL()
				Tema_interpessoal = TEMA_INTERPESSOAL()

				print('Qual o Processo?')
				Processo = grupo_verbal()  ## reiterações-verbo na passiva
				print('Qual o Valor(Value)?')
				Valor = circunstância()
				print('Qual é o Símbolo(Token)?')
				Símbolo = circunstância()

				Polaridade = POLARIDADE()
				Circunstância = circunstância()
				# Ex.: O dia todo é ocupado pela feira

				oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Valor + ' ' + Polaridade \
				         + ' ' + Processo + ' ' + Símbolo + ' ' + Circunstância + '?'


	##ORAÇÃO EXISTENCIAL MODO INTERROGATIVO POLAR

	elif Transitividade == 'PR_Existencial_AG_NA' \
			and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
			and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

		Tema_interpessoal = TEMA_INTERPESSOAL()
		Tema_textual = TEMA_TEXTUAL()

		print('Qual o Processo?')
		Processo = grupo_verbal()
		print('Qual é o Existente?')
		Existente = estrutura_GN()
		Polaridade = POLARIDADE()
		Circunstância = circunstância()
		oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Polaridade \
		         + ' ' + Processo + ' ' + Existente + ' ' + Circunstância + '?'

	return (re.sub(' +', ' ', oração).strip().capitalize())
