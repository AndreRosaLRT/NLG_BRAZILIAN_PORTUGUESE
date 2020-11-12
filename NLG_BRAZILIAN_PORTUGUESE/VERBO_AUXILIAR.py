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
def_classe_de_verbo("Evento")


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


def experiencia_do_verbo_AUX(verbo_AUX):
	'''(str)-> str

    Retorna um str com o morfema experiencial (ME) que realiza
    a experiência do verbo, dado um verbo lematizado

    >>>experiencia_do_verbo_AUX()
    'lev'
    >>>experiencia_do_verbo_AUX('')
    'diz'
    >>>experiencia_do_verbo_AUX('')
    't'
    '''

	# verbo = input ('Qual é o verbo lematizado?')
	ME = (verbo_AUX[slice(-2)])
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
	ME = experiencia_do_verbo_AUX(verbo)
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

def realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX=None,
                                              OI_tipo_de_pessoa_AUX=None, padrao_pessoa_morfologia_AUX=None):
	'''(str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no infinitivo, dado
    padrão de morfologia.

    >>>realizacao_transitoriedade_infinitivo_AUX()
    'ar'
    '''
	if (padrao_de_morfologia_AUX == '-AR'):
		MI = 'ar'
	elif (padrao_de_morfologia_AUX == '-ER'):
		MI = 'er'
	elif (padrao_de_morfologia_AUX == '-IR'):
		MI = 'ir'
	elif (padrao_de_morfologia_AUX == '-IR'):
		MI = 'ir'
	return MI


# realizacao_transitoriedade_infinitivo_AUX('-AR')


######
# opções
# padrao_de_morfologia_AUX = ['-AR', '-ER', '-IR', '-OR']
# OI_tipo_de_pessoa_AUX =['1pessoa','2pessoa','3pessoa'])
# OI_numero_AUX = ['singular', 'plural']
# padrao_pessoa_morfologia_AUX = ['3pessoa_do_singular', 'Morfologia_padrão']


def realizacao_transitoriedade_presente_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                            padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str,str,str,str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no presente, dados
    a o padrão de morfologia, tipo_pessoa de orientação, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_presente()
    'o'
    :param genero_AUX:
    '''

	if (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão" or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão" or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão"
	):
		MI = 'o'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão":
		MI = 'onho'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'a'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'as'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'
	):
		MI = 'es'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular'):
		MI = 'õe'
	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'):
		MI = 'ões'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular':
		MI = 'a'
	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'
	):
		MI = 'e'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'õe'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'õe'
	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'omos'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'ais'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'eis'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'e'
	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'is'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'õe'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'ondes'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'am'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'
	):
		MI = 'em'


	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'õe'


	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'õem'

	return MI


# realizacao_transitoriedade_presente_AUX('-AR','singular','1pessoa')

# pretérito_perfectivo_I

# padrao_de_morfologia_AUX = choice.Menu(['-AR', '-ER', '-IR', '-OR']).ask()
# OI_tipo_de_pessoa_AUX = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
# OI_numero_AUX = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_perfectivo_I_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
                                                          OI_tipo_de_pessoa_AUX,
                                                          padrao_pessoa_morfologia_AUX="Morfologia_padrão"
                                                          ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_AUX(,
    'ei'
    '''
	if padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão":
		MI = 'ei'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão" or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão"):
		MI = 'i'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == "Morfologia_padrão"):
		MI = 'us'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'aste'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'este'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'iste'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'useste'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'ou'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'eu'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'iu'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'ôs'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'usemos'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'astes'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'estes'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'istes'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ôs'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'usestes'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'aram'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'eram'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'iu'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'iram'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'useram'
	return MI


#
# realizacao_transitoriedade_preterito_perfectivo_I_AUX('-IR', 'singular', '1pessoa')


###pretérito imperfectivo
# padrao_de_morfologia_AUX =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
# OI_tipo_de_pessoa_AUX = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
# OI_numero_AUX = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_imperfectivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
                                                          OI_tipo_de_pessoa_AUX,
                                                          padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e numero.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_AUX(,
    'ei'
    '''
	if (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'):
		MI = 'ava'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'):
		MI = 'ia'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'):
		MI = 'unha'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'avas'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular'):
		MI = 'ia'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'):
		MI = 'ias'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'unhas'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'ávamos'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular'):
		MI = 'ia'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão'):
		MI = 'íamos'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morforlogia_padrão':
		MI = 'únhamos'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
		MI = 'ava'
	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' and padrao_pessoa_morfologia_AUX == 'Morfologia_padrão':
		MI = 'áveis'
	#
	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'
	):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'íeis'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'únheis'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ava'
		else:
			MI = 'avam'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'
	):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'iam'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'unham'
	return MI


# realizacao_transitoriedade_preterito_imperfectivo_AUX('-IR', 'plural', '1pessoa')


def realizacao_transitoriedade_preterito_perfectivo_II_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
                                                           OI_tipo_de_pessoa_AUX,
                                                           padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_AUX(,
    'ei'
    '''
	if (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'ara'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
	      padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'era'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
	      padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'ira'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
	      padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'usera'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):
		MI = 'aras'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):
		MI = 'eras'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):
		MI = 'iras'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):
		MI = 'useras'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'áramos'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'éramos'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'íramos'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'úseramos'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'áreis'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'êreis'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'íreis'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'uséreis'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'aram'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'eram'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'iram'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'useram'
	return MI


# realizacao_transitoriedade_preterito_perfectivo_II_AUX('-OR','plural','3pessoa')


def realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                                    padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no passado volitivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_AUX(,
    'ei'
    '''

	if (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'aria'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
	      padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'eria'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
	      padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'iria'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
	      padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'oria'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'arias'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'erias'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'irias'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'orias'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríamos'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríamos'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríamos'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríamos'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríeis'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríeis'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríeis'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríeis'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'ariam'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eriam'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iriam'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oriam'

	return MI


# realizacao_transitoriedade_passado_volitivo('-AR', 'singular','1pessoa')


def realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                          padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no futuro, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_AUX(,
    'ei'
    '''
	if (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular'):
		MI = 'arei'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular'):
		MI = 'erei'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular'):
		MI = 'irei'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular'):
		MI = 'orei'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ará'
		else:
			MI = 'arás'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'erá'
		else:
			MI = 'erás'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'irá'
		else:
			MI = 'irás'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'orá'
		else:
			MI = 'orás'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'ará'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'erá'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'irá'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'):
		MI = 'orá'
	#
	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'aremos'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'eremos'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'iremos'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'oremos'
	#
	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'areis'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'ereis'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'ireis'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		MI = 'oreis'
	#
	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'arão'

	elif (padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'erão'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'irão'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'orão'

	return MI


# realizacao_transitoriedade_futuro_AUX('-AR','plural','2pessoa')

def realizacao_transitoriedade_subjuntivo_conjuntivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                                         padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no subjuntivo conjuntivo, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.
    '''
	if (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'onha'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'es'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'
	):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'as'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhas'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'emos'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'
	):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'amos'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhamos'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'eis'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'
	):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'ais'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhais'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'em'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'
	):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'am'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onham'
	return MI


# realizacao_transitoriedade_subjuntivo_conjuntivo('-ER','plural','2pessoa')
#######subjuntivo_condicional


def realizacao_transitoriedade_subjuntivo_condicional_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
                                                          OI_tipo_de_pessoa_AUX,
                                                          padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no subjuntivo condicional, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_AUX('-AR','1pessoa','singular')
    >>>'asse'

    '''

	if (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'asse'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'esse'

	elif (
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'isse'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'usesse'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'asses'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'esses'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'isses'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usesses'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ássemos'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êssemos'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'íssemos'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'uséssemos'

	elif (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ásseis'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êsseis'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'íssseis'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usésseis'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'assem'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'essem'

	elif (padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'issem'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usessem'
	return MI


# realizacao_transitoriedade_subjuntivo_condicional_AUX('-AR','plural','2pessoa','3pessoa_do_singular')

###subjuntivo_optativo
def realizacao_transitoriedade_subjuntivo_optativo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                                       padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no subjuntivo_optativo ,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'user'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'useres'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'usermos'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userdes'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userem'

	return MI


# realizacao_transitoriedade_subjuntivo_optativo_AUX('-AR','plural','2pessoa')

############não_finito_concretizado

def realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
                                                           OI_tipo_de_pessoa_AUX,
                                                           padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX  não_finito_concretizado,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'or'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ores'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':

		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ormos'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ordes'

	elif padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
		if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'orem'
	return MI


# realizacao_transitoriedade_nao_finito_concretizado_AUX('-AR','plural','2pessoa')

#######imperativo_I (afirmativo)


def realizacao_transitoriedade_imperativo_I_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                                padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no imperativo_I,
    dados  o padrão de morfologia, tipo_pessoa de pessoa,número, padrão de pessoa da morfologia.

    >>>
    ''
    '''

	if OI_numero_AUX == 'singular':
		if OI_tipo_de_pessoa_AUX == '1pessoa':
			if (padrao_de_morfologia_AUX == '-AR' or
					padrao_de_morfologia_AUX == '-ER' or
					padrao_de_morfologia_AUX == '-IR' or
					padrao_de_morfologia_AUX == '-OR'):
				MI = 'Não há transitoriedade para imperativo_I na 1pessoa singular'

		elif OI_tipo_de_pessoa_AUX == '2pessoa':
			if padrao_de_morfologia_AUX == '-AR':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'a'
			elif (padrao_de_morfologia_AUX == '-ER' or padrao_de_morfologia_AUX == '-IR'):
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'e'
			elif padrao_de_morfologia_AUX == '-OR':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'onha'
				else:
					MI = 'õe'
		####
		elif OI_tipo_de_pessoa_AUX == '3pessoa':
			if padrao_de_morfologia_AUX == '-AR':
				MI = 'e'
			elif (padrao_de_morfologia_AUX == '-ER' or padrao_de_morfologia_AUX == '-IR'):
				MI = 'a'
			elif padrao_de_morfologia_AUX == '-OR':
				MI = 'onha'
	####
	elif OI_numero_AUX == 'plural':
		if OI_tipo_de_pessoa_AUX == '1pessoa':
			if padrao_de_morfologia_AUX == '-AR':
				MI = 'emos'
			elif padrao_de_morfologia_AUX == '-ER' or padrao_de_morfologia_AUX == '-IR':
				MI = 'amos'
			elif padrao_de_morfologia_AUX == '-OR':
				MI = 'onhamos'

		elif OI_tipo_de_pessoa_AUX == '2pessoa':
			if padrao_de_morfologia_AUX == '-AR':
				MI = 'ai'
			elif padrao_de_morfologia_AUX == '-ER':
				MI = 'ei'
			elif padrao_de_morfologia_AUX == '-IR':
				MI = 'i'
			elif padrao_de_morfologia_AUX == '-OR':
				MI = 'onde'

		elif OI_tipo_de_pessoa_AUX == '3pessoa':
			if padrao_de_morfologia_AUX == '-AR':
				MI = 'em'
			elif (padrao_de_morfologia_AUX == '-ER' or
			      padrao_de_morfologia_AUX == '-IR'):
				MI = 'am'
			elif padrao_de_morfologia_AUX == '-OR':
				MI = 'onham'
	return MI


#######imperativo_II (negativo)


def realizacao_transitoriedade_imperativo_II_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
                                                 padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no imperativo_II,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''

	if (padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'):
		MI = 'es'

	elif (
			(padrao_de_morfologia_AUX == '-ER' or '-IR')
			and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'as'

	elif (
			padrao_de_morfologia_AUX == '-OR'
			and OI_tipo_de_pessoa_AUX == '2pessoa'
			and OI_numero_AUX == 'singular'
	):
		MI = 'onhas'

	elif (
			padrao_de_morfologia_AUX == '-AR'
			and OI_tipo_de_pessoa_AUX == '3pessoa'
			and OI_numero_AUX == 'singular'
	):
		MI = 'e'

	elif (
			(
					padrao_de_morfologia_AUX == '-ER' or '-IR'
			)
			and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa'
			and OI_numero_AUX == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia_AUX == '-OR'
			and OI_tipo_de_pessoa_AUX == '3pessoa'
			and OI_numero_AUX == 'singular'
	):
		MI = 'onha'

	elif (
			padrao_de_morfologia_AUX == '-AR'
			and OI_tipo_de_pessoa_AUX == '1pessoa'
			and OI_numero_AUX == 'plural'
	):
		MI = 'emos'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'
	):
		MI = 'amos'

	elif (
			padrao_de_morfologia_AUX == '-OR'
			and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'plural'):
		MI = 'onhamos'

	elif (
			padrao_de_morfologia_AUX == '-AR'
			and OI_tipo_de_pessoa_AUX == '2pessoa'
			and OI_numero_AUX == 'plural'
	):
		MI = 'eis'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural'
	):
		MI = 'ais'

	elif (
			padrao_de_morfologia_AUX == '-OR'
			and OI_tipo_de_pessoa_AUX == '2pessoa'
			and OI_numero_AUX == 'plural'
	):
		MI = 'onhais'

	elif (
			padrao_de_morfologia_AUX == '-AR'
			and OI_tipo_de_pessoa_AUX == '3pessoa'
			and OI_numero_AUX == 'plural'
	):
		MI = 'em'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'
	):
		MI = 'am'

	elif (padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural'):
		MI = 'onham'

	elif (
			padrao_de_morfologia_AUX == '-AR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-ER' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-IR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular' or
			padrao_de_morfologia_AUX == '-OR' and OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular'
	):
		MI = 'Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida'

	return MI


# realizacao_transitoriedade_imperativo_II_AUX('-AR', '2pessoa','plural')
###gerúndio
# realizacao_transitoriedade_gerundio('-OR')

def realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX=None, OI_numero_AUX=None,
                                            OI_tipo_de_pessoa_AUX=None, padrao_pessoa_morfologia_AUX="Morfologia_padrão"
                                            ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no gerúndio,
    dadoo padrão de morfologia.

    >>>
    '''
	if padrao_de_morfologia_AUX == '-AR':
		MI = 'ando'

	elif padrao_de_morfologia_AUX == '-ER':
		MI = 'endo'

	elif padrao_de_morfologia_AUX == '-IR':
		MI = 'indo'

	elif padrao_de_morfologia_AUX == '-OR':
		MI = 'ondo'

	return MI


# realizacao_transitoriedade_gerundio_AUX('-IR')

######particípio


def realizacao_transitoriedade_participio_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
                                              OI_tipo_de_pessoa_AUX=None,
                                              padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_AUX no particípio,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_particípio ()
    ''
    '''

	if padrao_de_morfologia_AUX == '-AR' and OI_numero_AUX == 'singular' and genero_AUX == 'feminino':
		MI = 'ada'

	elif padrao_de_morfologia_AUX == '-AR' and OI_numero_AUX == 'plural' and genero_AUX == 'feminino':
		MI = 'adas'

	elif padrao_de_morfologia_AUX == '-AR' and OI_numero_AUX == 'singular' and genero_AUX == 'masculino':
		MI = 'ado'

	elif padrao_de_morfologia_AUX == '-AR' and OI_numero_AUX == 'plural' and genero_AUX == 'masculino':
		MI = 'ados'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_numero_AUX == 'singular' and genero_AUX == 'masculino' or
			padrao_de_morfologia_AUX == '-IR' and OI_numero_AUX == 'singular' and genero_AUX == 'masculino'
	):
		MI = 'ido'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_numero_AUX == 'plural' and genero_AUX == 'masculino' or
			padrao_de_morfologia_AUX == '-IR' and OI_numero_AUX == 'plural' and genero_AUX == 'masculino'
	):
		MI = 'idos'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_numero_AUX == 'singular' and genero_AUX == 'feminino' or
			padrao_de_morfologia_AUX == '-IR' and OI_numero_AUX == 'singular' and genero_AUX == 'feminino'
	):
		MI = 'ida'

	elif (
			padrao_de_morfologia_AUX == '-ER' and OI_numero_AUX == 'plural' and genero_AUX == 'feminino' or
			padrao_de_morfologia_AUX == '-IR' and OI_numero_AUX == 'plural' and genero_AUX == 'feminino'
	):
		MI = 'idas'

	elif padrao_de_morfologia_AUX == '-OR' and OI_numero_AUX == 'singular' and genero_AUX == 'feminino':
		MI = 'osta'

	elif padrao_de_morfologia_AUX == '-OR' and OI_numero_AUX == 'singular' and genero_AUX == 'masculino':
		MI = 'osto'

	elif padrao_de_morfologia_AUX == '-OR' and OI_numero_AUX == 'plural' and genero_AUX == 'feminino':
		MI = 'ostas'

	elif padrao_de_morfologia_AUX == '-OR' and OI_numero_AUX == 'plural' and genero_AUX == 'masculino':
		MI = 'ostos'

	return MI


#
#
# realizacao_transitoriedade_participio('-IR', 'plural', 'masculino')


# realizacao_transitoriedade_preterito_imperfectivo('-IR','singular','1pessoa')

def realizacao_transitoriedade_do_verbo_AUX(tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
                                            OI_numero_AUX, genero_AUX, OI_tipo_de_pessoa_AUX,
                                            padrao_pessoa_morfologia_AUX="Morfologia_padrão"):
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo_AUX no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo_AUX()
    'o'

    '''

	if tipo_de_orientacao_AUX == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX=None,
		                                               OI_tipo_de_pessoa_AUX=None, padrao_pessoa_morfologia_AUX=None)

	elif tipo_de_orientacao_AUX == 'presente':
		MI = realizacao_transitoriedade_presente_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                             padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':
		MI = realizacao_transitoriedade_preterito_perfectivo_I_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                           OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		MI = realizacao_transitoriedade_preterito_perfectivo_II_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':
		MI = realizacao_transitoriedade_preterito_imperfectivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                           OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'futuro':
		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                          OI_tipo_de_pessoa_AUX,
		                                                          padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'subjuntivo_condicional':
		MI = realizacao_transitoriedade_subjuntivo_condicional_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                           OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':
		MI = realizacao_transitoriedade_subjuntivo_optativo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                        OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'imperativo_I':
		MI = realizacao_transitoriedade_imperativo_I_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                                 padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'imperativo_II':
		MI = realizacao_transitoriedade_imperativo_II_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                  OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	elif tipo_de_orientacao_AUX == 'particípio':
		MI = realizacao_transitoriedade_participio_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
		                                               OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

	return MI


#
realizacao_transitoriedade_gerundio_AUX('-AR')
realizacao_transitoriedade_do_verbo_AUX('gerúndio', '-AR', None, None, None)
realizacao_transitoriedade_do_verbo_AUX('presente', '-AR', 'singular', None, '1pessoa')
realizacao_transitoriedade_do_verbo_AUX('pretérito_perfectivo_I', '-IR', 'plural', None, '1pessoa')
realizacao_transitoriedade_do_verbo_AUX('pretérito_imperfectivo', '-ER', 'plural', None, '2pessoa')
realizacao_transitoriedade_do_verbo_AUX('imperativo_I', '-AR', 'singular', None, '2pessoa')
realizacao_transitoriedade_do_verbo_AUX('imperativo_II', '-AR', 'singular', None, '2pessoa')
realizacao_transitoriedade_imperativo_I_AUX('-AR', 'singular', '2pessoa')


# verbo_AUX TER

def formacao_verbo_AUX_ter(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
                           OI_numero_AUX, genero_AUX, OI_tipo_de_pessoa_AUX,
                           padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	"""
    :return:
    """

	if tipo_de_orientacao_AUX == 'subjuntivo_condicional':
		ME = verbo_AUX[slice(-2)]

		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'esse'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
			verbo_AUX = ME + 'iv' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
			verbo_AUX = ME + 'iv' + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		ME = verbo_AUX[slice(-2)]

		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo_AUX = ME + 'enh' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
			verbo_AUX = ME + 'enh' + MI
	###
	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'imperativo_I':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'enh' + MI
				else:
					MI = 'em'
					verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'a'
				verbo_AUX = ME + 'enh' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'enh' + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'ende'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'enh' + MI
	###
	elif tipo_de_orientacao_AUX == 'imperativo_II':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa' and OI_numero_AUX == 'singular':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'a'
				verbo_AUX = ME + 'enh' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'enh' + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
			verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
			verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':
		ME = verbo_AUX[slice(-2)]

		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'a'
			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo_AUX = ME + 'inh' + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'inh' + MI
				else:
					MI = 'amos'
					verbo_AUX = ME + 'ính' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'inh' + MI
				else:
					MI = 'eis'
					verbo_AUX = ME + 'ính' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'inh' + MI
				else:
					MI = 'am'
					verbo_AUX = ME + 'inh' + MI
	###
	elif tipo_de_orientacao_AUX == 'futuro':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'passado_volitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'presente':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'enho'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'ens'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'em'
			verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'endes'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'

			verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'ive'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'eve'
			verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
			verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'ivera'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'ivera'
			verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'

			elif OI_tipo_de_pessoa_AUX == '3pessoa' and OI_numero_AUX == 'plural':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'
			verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'infinitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                               padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'gerúndio':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'particípio':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_participio_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
		                                               OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	return verbo_AUX


# verbo_AUX HAVER
def formacao_verbo_AUX_haver(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
                             OI_numero_AUX, genero_AUX, OI_tipo_de_pessoa_AUX,
                             padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao_AUX == 'infinitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                               padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                           OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'futuro':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'passado_volitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'gerúndio':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'particípio':
		ME = verbo_AUX[slice(-2)]
		MI = 'ido'
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'presente':
		if OI_numero_AUX == 'singular':
			ME = verbo_AUX[slice(-4)]
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'ei'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'á'

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					ME = verbo_AUX[slice(-4)]
					MI = 'á'
				else:
					ME = verbo_AUX[slice(-2)]
					MI = 'emos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					ME = verbo_AUX[slice(-4)]
					MI = 'á'
				else:
					ME = verbo_AUX[slice(-2)]
					MI = 'eis'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'ão'

		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'e'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'este'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'e'

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'estes'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'eram'

		verbo_AUX = ME + 'ouv' + MI

	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'era'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'eras'


			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'era'

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éramos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éreis'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'eram'
		verbo_AUX = ME + 'ouv' + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_condicional':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '2pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				ME = verbo_AUX[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
				                                                           OI_tipo_de_pessoa_AUX,
				                                                           padrao_pessoa_morfologia_AUX)
				verbo_AUX = ME + 'ouv' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
					verbo_AUX = ME + 'ud' + MI
				else:
					MI = 'éssemos'
					verbo_AUX = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo_AUX = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
				                                                           OI_tipo_de_pessoa_AUX,
				                                                           padrao_pessoa_morfologia_AUX)
				verbo_AUX = ME + 'ouv' + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				ME = verbo_AUX[slice(-4)]
				MI = 'a'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo_AUX = ME + 'aj' + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ais'
				verbo_AUX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'aj' + MI

	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'imperativo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'aj' + MI
				else:
					MI = 'á'
					verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'a'
				verbo_AUX = ME + 'aj' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'ei'
				verbo_AUX = ME + 'av' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'aj' + MI

	elif tipo_de_orientacao_AUX == 'imperativo_II':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				MI = 'a'
				verbo_AUX = ME + 'aj' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + MI
				else:
					MI = 'amos'
					verbo_AUX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_AUX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = verbo_AUX[slice(-4)]
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'aj' + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':
		ME = verbo_AUX[slice(-4)]
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo_AUX = ME + 'ouv' + MI

	return verbo_AUX


# # # # # ##TESTE haver
# OI_numero_AUXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # ###passado_volitivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # futuro
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_I
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # imperativo_II
#
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # não_finito_concretizado
#
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_haver('haver', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # infinitivo
# print(formacao_verbo_AUX_haver('haver', 'infinitivo', '-ER', numero, 'feminino', None))
# # # #
# # # # # # # gerúndio
# print(formacao_verbo_AUX_haver('haver', 'gerúndio', '-ER', None, None, None))
# # # # # #
# # # # # # # particípio
# genero_AUXs = ['masculino', 'feminino']
# for numero in OI_numero_AUXs:
# 	for genero_AUX in genero_AUXs:
# 		print(formacao_verbo_AUX_haver('haver', 'particípio', '-ER', numero, genero_AUX, None))


# verbo_AUX ESTAR

def formacao_verbo_AUX_estar(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX, OI_numero_AUX,
                             genero_AUX, OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	'''
    '''
	ME = verbo_AUX[slice(-2)]
	if tipo_de_orientacao_AUX == 'subjuntivo_condicional':

		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa' or OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'esse'
				verbo_AUX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
				verbo_AUX = ME + 'iv' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo_AUX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo_AUX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
				verbo_AUX = ME + 'iv' + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa' or OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'a'
				verbo_AUX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + 'ej' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_AUX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'ej' + MI


	elif tipo_de_orientacao_AUX == 'imperativo_I':

		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'ej' + MI
				else:
					MI = 'á'
					verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'a'
				verbo_AUX = ME + 'ej' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				MI = 'ai'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'ej' + MI

	elif tipo_de_orientacao_AUX == 'imperativo_II':

		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'a'
				verbo_AUX = ME + 'ej' + MI
		if OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_AUX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'ej' + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':

		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa' or OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'er'
				verbo_AUX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
				verbo_AUX = ME + 'iv' + MI

		elif OI_numero_AUX == 'plural':

			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'
				verbo_AUX = ME + 'iv' + MI

			if OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo_AUX = ME + 'iv' + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
				verbo_AUX = ME + 'iv' + MI
	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':

		MI = realizacao_transitoriedade_preterito_imperfectivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                           OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	elif tipo_de_orientacao_AUX == 'futuro':

		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'passado_volitivo':

		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	elif tipo_de_orientacao_AUX == 'presente':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				MI = 'ou'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'á'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '2pessoa'):

				MI = realizacao_transitoriedade_presente(padrao_de_morfologia_AUX, OI_numero_AUX,
				                                         OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'ão'
			verbo_AUX = ME + MI
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				MI = 'ive'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'eve'
				verbo_AUX = ME + MI
		if OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
				verbo_AUX = ME + MI
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		if OI_numero_AUX == 'singular':

			if OI_tipo_de_pessoa_AUX == '1pessoa':

				MI = 'ivera'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				MI = 'ivera'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':

			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'

				verbo_AUX = ME + MI
	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':

		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'infinitivo':

		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                               padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'gerúndio':

		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	elif tipo_de_orientacao_AUX == 'particípio':

		MI = realizacao_transitoriedade_participio_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
		                                               OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	return verbo_AUX


# verbo_AUXS VIR E INTERVIR


def formacao_verbo_AUX_vir_intervir(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
                                    OI_numero_AUX, genero_AUX, OI_tipo_de_pessoa_AUX,
                                    padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	'''
    '''
	ME = verbo_AUX[slice(-2)]

	if tipo_de_orientacao_AUX == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                               padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'inha'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inhas'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínhamos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínheis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inham'
				verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'futuro':
		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'particípio':
		if OI_numero_AUX == 'singular':
			if genero_AUX == 'masculino':
				MI = 'indo'
			else:
				MI = 'inda'
		else:
			if genero_AUX == 'masculino':
				MI = 'indos'
			else:
				MI = 'indas'
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'presente':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'enho'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if verbo_AUX == 'vir':
					if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
						MI = 'em'
					else:
						MI = 'ens'
					verbo_AUX = ME + MI
				else:
					if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
						MI = 'ém'
					else:
						MI = 'éns'
					verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if verbo_AUX == 'vir':
					MI = 'em'
				else:
					MI = 'ém'
				verbo_AUX = ME + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'imos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'indes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'
				verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'im'
				verbo_AUX = ME + MI
			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieste'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'eio'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'iemos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'iestes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieram'
				verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'iera'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieras'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéramos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéreis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieram'
				verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_condicional':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'iesse'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iesses'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iéssemos'
				verbo_AUX = ME + '' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'iésseis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iessem'
				verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'a'
				verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhas'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhamos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhais'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enham'
				verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI

	elif tipo_de_orientacao_AUX == 'imperativo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if verbo_AUX == 'vir':
					if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
						MI = 'a'
						verbo_AUX = ME + 'enh' + MI
					else:
						MI = 'em'
						verbo_AUX = ME + MI
				else:
					if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
						MI = 'a'
						verbo_AUX = ME + 'enh' + MI
					else:
						MI = 'ém'
						verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'a'
				verbo_AUX = ME + 'enh' + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'enhamos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'inde'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'enh' + MI

	elif tipo_de_orientacao_AUX == 'imperativo_II':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'a'
				verbo_AUX = ME + 'enh' + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_AUX = verbo_AUX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = verbo_AUX = ME + 'enh' + MI

	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'ier'
				verbo_AUX = ME + MI

			if OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ieres'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'iermos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierdes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierem'
				verbo_AUX = ME + MI
	return verbo_AUX


#
# # #
# # # # ##TESTE intervir
# OI_numero_AUXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_AUX_vir_intervir('intervir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_AUX_vir_intervir('intervir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# genero_AUXs = ['masculino', 'feminino']
# for numero in OI_numero_AUXs:
# 	for genero_AUX in genero_AUXs:
# 		print(formacao_verbo_AUX_vir_intervir('intervir', 'particípio', '-IR', numero, genero_AUX, None))
#
# ######################################
#
#
# # # # ##TESTE vir
# OI_numero_AUXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_AUX_vir_intervir('vir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_AUX_vir_intervir('vir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# genero_AUXs = ['masculino', 'feminino']
# for numero in OI_numero_AUXs:
# 	for genero_AUX in genero_AUXs:
# 		print(formacao_verbo_AUX_vir_intervir('vir', 'particípio', '-IR', numero, genero_AUX, None))


# verbo_AUX HAVER


# verbo_AUX IR

def formacao_verbo_AUX_ir(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX, OI_numero_AUX,
                          genero_AUX, OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao_AUX == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                               padrao_pessoa_morfologia_AUX)
		verbo_AUX = MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                           OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = MI
	###
	elif tipo_de_orientacao_AUX == 'futuro':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'passado_volitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'gerúndio':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'particípio':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_participio_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
		                                               OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'presente':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'v'
				MI = 'ou'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'ais'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'v'
				MI = 'ai'
				verbo_AUX = ME + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'amos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'i'
				MI = 'des'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'am'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'f'
				MI = 'ui'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'f'
				MI = 'oi'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'omos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'ostes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'f'

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				ME = 'f'
				MI = 'ora'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo_AUX = ME + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_condicional':
		ME = 'f'
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'osse'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				ME = 'v'
				MI = 'á'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'imperativo_I':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ai'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'v'
				MI = 'á'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = 'i'
				MI = 'de'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'imperativo_II':
		ME = 'v'
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'á'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'or'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo_AUX = ME + MI

	return verbo_AUX


# #
# # #
# # # # ##TESTE ir
# OI_numero_AUXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'presente', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # #####pretérito_imperfectivo
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###passado_volitivo
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # # futuro
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'futuro', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_conjuntivo
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_condicional
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ir('ir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # imperativo_I
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_II
# #
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # não_finito_concretizado
# #
# # for numero in OI_numero_AUXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_AUX_ir('ir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# #
# # # # # infinitivo
# # print(formacao_verbo_AUX_ir('ir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # #
# # # # # # gerúndio
# # print(formacao_verbo_AUX_ir('ir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# # # genero_AUXs = ['masculino', 'feminino']
# # for numero in OI_numero_AUXs:
# # 	for genero_AUX in genero_AUXs:
# # 		print(formacao_verbo_AUX_ir('ir', 'particípio', '-IR', numero, genero_AUX, None))


# verbo_AUXS VIR E INTERVIR


# verbo_AUX SER

def formacao_verbo_AUX_ser(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
                           OI_tipo_de_pessoa_AUX,
                           padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao_AUX == 'infinitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                               padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_imperfectivo':
		if OI_numero_AUX == 'singular':
			ME = 'er'
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'a'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + MI

		elif OI_numero_AUX == 'plural':

			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'amos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'eis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = 'er'
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'futuro':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, OI_tipo_de_pessoa_AUX,
		                                           padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'passado_volitivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                     OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'gerúndio':
		ME = verbo_AUX[slice(-2)]

		MI = realizacao_transitoriedade_gerundio_AUX(padrao_de_morfologia_AUX, genero_AUX, OI_numero_AUX,
		                                             OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'particípio':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_participio_AUX(padrao_de_morfologia_AUX, OI_numero_AUX, genero_AUX,
		                                               OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'presente':
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				ME = verbo_AUX[slice(-2)]
				MI = 'ou'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = ''
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'é'
				else:
					MI = 'és'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				ME = ''
				MI = 'é'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo_AUX[slice(-2)]
					MI = 'omos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				ME = verbo_AUX[slice(-2)]
				MI = 'ois'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo_AUX[slice(-2)]
					MI = 'ão'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_I':

		ME = 'f'
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				MI = 'ui'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'oi'
				verbo_AUX = ME + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
					verbo_AUX = ME + MI
				else:
					MI = 'omos'
					verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'ostes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'pretérito_perfectivo_II':
		ME = 'f'
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'ora'
				verbo_AUX = ME + MI


			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_condicional':

		ME = 'f'
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'osse'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
					verbo_AUX = ME + MI
		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_conjuntivo':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                      OI_tipo_de_pessoa_AUX,
		                                                      padrao_pessoa_morfologia_AUX="Morfologia_padrão")
		verbo_AUX = ME + 'ej' + MI
	###
	elif tipo_de_orientacao_AUX == 'não_finito_concretizado':
		ME = verbo_AUX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_AUX(padrao_de_morfologia_AUX, OI_numero_AUX,
		                                                            OI_tipo_de_pessoa_AUX, padrao_pessoa_morfologia_AUX)
		verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero_AUX == 'singular':
			if (OI_tipo_de_pessoa_AUX == '1pessoa' or
					OI_tipo_de_pessoa_AUX == '3pessoa'):
				MI = 'or'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo_AUX = ME + MI



		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo_AUX = ME + MI
	###
	elif tipo_de_orientacao_AUX == 'imperativo_I':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
					verbo_AUX = ME + 'ej' + MI
				else:
					MI = 'ê'
					verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'a'
				verbo_AUX = ME + 'ej' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa':
				MI = 'ede'
				verbo_AUX = ME + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'ej' + MI
	###
	elif tipo_de_orientacao_AUX == 'imperativo_II':
		ME = verbo_AUX[slice(-2)]
		if OI_numero_AUX == 'singular':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				verbo_AUX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_AUX == '2pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_AUX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':
				MI = 'a'
				verbo_AUX = ME + 'ej' + MI

		elif OI_numero_AUX == 'plural':
			if OI_tipo_de_pessoa_AUX == '1pessoa':
				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_AUX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_AUX == '2pessoa' and OI_numero_AUX == 'plural':
				MI = 'ais'
				verbo_AUX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_AUX == '3pessoa':

				if padrao_pessoa_morfologia_AUX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_AUX = ME + 'ej' + MI

	return verbo_AUX


# # ##TESTE ser
OI_numero_AUXs = ['singular', "plural"]
OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# ###
# # #presente
# print("A conjugação é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'presente', '-ER', numero, None, tipo_pessoa))
# 
# # ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# 
# # #####pretérito_imperfectivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # 
# # ### "pretérito_perfectivo_II"
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# 
# # ###passado_volitivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# 
# # # futuro
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'futuro', '-ER', numero, None, tipo_pessoa))
# 
# # # subjuntivo_conjuntivo
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_condicional
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_optativo
# 
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# 
# # imperativo_I
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# 
# # # imperativo_II
# 
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# 
# # # # não_finito_concretizado
# for numero in OI_numero_AUXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_AUX_ser('ser', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # infinitivo
# print(formacao_verbo_AUX_ser('ser', 'infinitivo', '-ER', numero, 'feminino', None))
# #
# # # # gerúndio
# print(formacao_verbo_AUX_ser('ser', 'gerúndio', '-ER', None, None, None))
# # #
# # # # particípio
genero_AUXs = ['masculino', 'feminino']
for numero in OI_numero_AUXs:
	for genero_AUX in genero_AUXs:
		print(formacao_verbo_AUX_ser('ser', 'particípio', '-ER', numero, genero_AUX, None))


# ####################################################################################

def formacao_da_estrutura_do_verbo_AUX(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX, OI_numero_AUX,
                                       genero_AUX, OI_tipo_de_pessoa_AUX,
                                       padrao_pessoa_morfologia_AUX='Morfologia_padrão'):
	'''
    '''

	if verbo_AUX == 'estar':
		verbo_AUX = formacao_verbo_AUX_estar(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
		                                     OI_numero_AUX,
		                                     genero_AUX, OI_tipo_de_pessoa_AUX,
		                                     padrao_pessoa_morfologia_AUX='Morfologia_padrão')

	elif verbo_AUX == 'ter':
		verbo_AUX = formacao_verbo_AUX_ter(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
		                                   OI_numero_AUX,
		                                   genero_AUX, OI_tipo_de_pessoa_AUX,
		                                   padrao_pessoa_morfologia_AUX='Morfologia_padrão')

	elif verbo_AUX == 'haver':
		verbo_AUX = formacao_verbo_AUX_haver(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
		                                     OI_numero_AUX,
		                                     genero_AUX, OI_tipo_de_pessoa_AUX,
		                                     padrao_pessoa_morfologia_AUX='Morfologia_padrão')

	elif verbo_AUX == 'ir':
		verbo_AUX = formacao_verbo_AUX_ir(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
		                                  OI_numero_AUX,
		                                  genero_AUX, OI_tipo_de_pessoa_AUX,
		                                  padrao_pessoa_morfologia_AUX='Morfologia_padrão')

	elif verbo_AUX == 'vir':
		verbo_AUX = formacao_verbo_AUX_vir_invervir(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
		                                            OI_numero_AUX,
		                                            genero_AUX, OI_tipo_de_pessoa_AUX,
		                                            padrao_pessoa_morfologia_AUX='Morfologia_padrão')

	elif verbo_AUX == 'ser':
		verbo_AUX = formacao_verbo_AUX_ser(verbo_AUX, tipo_de_orientacao_AUX, padrao_de_morfologia_AUX,
		                                   OI_numero_AUX,
		                                   genero_AUX, OI_tipo_de_pessoa_AUX,
		                                   padrao_pessoa_morfologia_AUX='Morfologia_padrão')

	else:
		verbo_AUX = ''
	return verbo_AUX

# formacao_da_estrutura_do_verbo_AUX('ser','pretérito_perfectivo_I','-ER','singular',None,'1pessoa')
