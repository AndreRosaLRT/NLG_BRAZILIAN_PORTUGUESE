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


def experiencia_do_verbo_LEX(verbo_lex):
	'''(str)-> str

    Retorna um str com o morfema experiencial (ME) que realiza
    a experiência do verbo, dado um verbo lematizado

    >>>experiencia_do_verbo_LEX()
    'lev'
    >>>experiencia_do_verbo_LEX('')
    'diz'
    >>>experiencia_do_verbo_LEX('')
    't'
    '''

	# verbo = input ('Qual é o verbo lematizado?')
	ME = (verbo_lex[slice(-2)])
	return (ME)


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
	ME = experiencia_do_verbo_LEX(verbo)
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

def realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX=None,
                                          OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX=None):
	'''(str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no infinitivo, dado
    padrão de morfologia.

    >>>realizacao_transitoriedade_infinitivo_LEX()
    'ar'
    '''
	if (padrao_de_morfologia_LEX == '-AR'):
		MI = 'ar'
	elif (padrao_de_morfologia_LEX == '-ER'):
		MI = 'er'
	elif (padrao_de_morfologia_LEX == '-IR'):
		MI = 'ir'
	elif (padrao_de_morfologia_LEX == '-IR'):
		MI = 'ir'
	return MI


# realizacao_transitoriedade_infinitivo_LEX('-AR')


######
# opções
# padrao_de_morfologia_LEX = ['-AR', '-ER', '-IR', '-OR']
# OI_tipo_de_pessoa_LEX =['1pessoa','2pessoa','3pessoa'])
# OI_numero_LEX = ['singular', 'plural']
# padrao_pessoa_morfologia_LEX = ['3pessoa_do_singular', 'Morfologia_padrão']


def realizacao_transitoriedade_presente_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                        padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str,str,str,str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no presente, dados
    a o padrão de morfologia, tipo_pessoa de orientação, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_presente()
    'o'
    :param genero_LEX:
    '''

	if (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão" or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão" or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão"
	):
		MI = 'o'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão":
		MI = 'onho'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'a'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'as'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'
	):
		MI = 'es'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular'):
		MI = 'õe'
	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'):
		MI = 'ões'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular':
		MI = 'a'
	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'
	):
		MI = 'e'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'õe'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'õe'
	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'omos'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'ais'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'e'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'eis'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'e'
	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'is'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'õe'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'ondes'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'a'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'am'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'
	):
		MI = 'em'


	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'õe'


	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'õem'

	return MI


# realizacao_transitoriedade_presente_LEX('-AR','singular','1pessoa')

# pretérito_perfectivo_I

# padrao_de_morfologia_LEX = choice.Menu(['-AR', '-ER', '-IR', '-OR']).ask()
# OI_tipo_de_pessoa_LEX = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
# OI_numero_LEX = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_perfectivo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                      padrao_pessoa_morfologia_LEX="Morfologia_padrão"
                                                      ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_LEX(,
    'ei'
    '''
	if padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão":
		MI = 'ei'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão" or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão"):
		MI = 'i'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == "Morfologia_padrão"):
		MI = 'us'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'aste'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'este'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'iste'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'useste'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'ou'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'eu'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'iu'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'ôs'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ou'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'amos'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'emos'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'imos'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'usemos'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'astes'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'estes'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'iu'
	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'istes'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ôs'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'usestes'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ou'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'aram'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'eu'
	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'eram'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'iu'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'iram'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ôs'
	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'useram'
	return MI


#
# realizacao_transitoriedade_preterito_perfectivo_I_LEX('-IR', 'singular', '1pessoa')


###pretérito imperfectivo
# padrao_de_morfologia_LEX =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
# OI_tipo_de_pessoa_LEX = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
# OI_numero_LEX = choice.Menu(['singular', 'plural']).ask()

def realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                      padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e numero.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_LEX(,
    'ei'
    '''
	if (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'):
		MI = 'ava'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'):
		MI = 'ia'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'):
		MI = 'unha'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'avas'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular'):
		MI = 'ia'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'):
		MI = 'ias'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'unhas'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ava'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'ávamos'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular'):
		MI = 'ia'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão'):
		MI = 'íamos'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'unha'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morforlogia_padrão':
		MI = 'únhamos'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
		MI = 'ava'
	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' and padrao_pessoa_morfologia_LEX == 'Morfologia_padrão':
		MI = 'áveis'
	#
	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'
	):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'íeis'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'únheis'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ava'
		else:
			MI = 'avam'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'
	):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ia'
		else:
			MI = 'iam'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'unha'
		else:
			MI = 'unham'
	return MI


# realizacao_transitoriedade_preterito_imperfectivo_LEX('-IR', 'plural', '1pessoa')


def realizacao_transitoriedade_preterito_perfectivo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                       padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_LEX(,
    'ei'
    '''
	if (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'ara'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
	      padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'era'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
	      padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'ira'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
	      padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'usera'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):
		MI = 'aras'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):
		MI = 'eras'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):
		MI = 'iras'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):
		MI = 'useras'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'áramos'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'éramos'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'íramos'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'úseramos'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'áreis'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'êreis'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'íreis'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'uséreis'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'aram'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'eram'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'iram'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'useram'
	return MI


# realizacao_transitoriedade_preterito_perfectivo_II_LEX('-OR','plural','3pessoa')


def realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no passado volitivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_LEX(,
    'ei'
    '''

	if (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'aria'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
	      padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'eria'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
	      padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'iria'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
	      padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'oria'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'arias'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'erias'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'irias'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'orias'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríamos'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríamos'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríamos'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríamos'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'aríeis'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eríeis'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iríeis'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oríeis'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'aria'
		else:
			MI = 'ariam'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'eria'
		else:
			MI = 'eriam'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'iria'
		else:
			MI = 'iriam'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'oria'
		else:
			MI = 'oriam'

	return MI


# realizacao_transitoriedade_passado_volitivo('-AR', 'singular','1pessoa')


def realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                      padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no futuro, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_LEX(,
    'ei'
    '''
	if (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular'):
		MI = 'arei'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular'):
		MI = 'erei'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular'):
		MI = 'irei'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular'):
		MI = 'orei'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ará'
		else:
			MI = 'arás'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'erá'
		else:
			MI = 'erás'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'irá'
		else:
			MI = 'irás'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'orá'
		else:
			MI = 'orás'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'ará'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'erá'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'irá'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
		MI = 'orá'
	#
	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'aremos'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'eremos'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'iremos'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'oremos'
	#
	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'areis'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'ereis'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'ireis'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		MI = 'oreis'
	#
	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'arão'

	elif (padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'erão'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'irão'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'orão'

	return MI


# realizacao_transitoriedade_futuro_LEX('-AR','plural','2pessoa')

def realizacao_transitoriedade_subjuntivo_conjuntivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                     padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no subjuntivo conjuntivo, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.
    '''
	if (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'e'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'onha'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'es'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'
	):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'as'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhas'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'emos'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'
	):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'amos'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhamos'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'eis'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'
	):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'ais'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onhais'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'e'
		else:
			MI = 'em'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'
	):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'a'
		else:
			MI = 'am'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'onham'
	return MI


# realizacao_transitoriedade_subjuntivo_conjuntivo('-ER','plural','2pessoa')
#######subjuntivo_condicional


def realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                      padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no subjuntivo condicional, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I_LEX('-AR','1pessoa','singular')
    >>>'asse'

    '''

	if (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'asse'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'esse'

	elif (
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'isse'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'usesse'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'asses'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'esses'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'isses'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usesses'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ássemos'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êssemos'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'íssemos'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'uséssemos'

	elif (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'ásseis'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'êsseis'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'onha'
		else:
			MI = 'íssseis'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usésseis'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'asse'
		else:
			MI = 'assem'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'esse'
		else:
			MI = 'essem'

	elif (padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'isse'
		else:
			MI = 'issem'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'usesse'
		else:
			MI = 'usessem'
	return MI


# realizacao_transitoriedade_subjuntivo_condicional_LEX('-AR','plural','2pessoa','3pessoa_do_singular')

###subjuntivo_optativo
def realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                   padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no subjuntivo_optativo ,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'user'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'useres'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'usermos'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userdes'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'user'
		else:
			MI = 'userem'

	return MI


# realizacao_transitoriedade_subjuntivo_optativo_LEX('-AR','plural','2pessoa')

############não_finito_concretizado

def realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                                       padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX  não_finito_concretizado,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''
	if (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'ar'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'er'

	elif (
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'ir'

	elif (
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'or'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ares'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'eres'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'ires'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ores'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'armos'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'ermos'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irmos'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ormos'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'ardes'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erdes'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irdes'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'ordes'

	elif padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ar'
		else:
			MI = 'arem'

	elif padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'er'
		else:
			MI = 'erem'

	elif padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'ir'
		else:
			MI = 'irem'

	elif padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
		if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
			MI = 'or'
		else:
			MI = 'orem'
	return MI


# realizacao_transitoriedade_nao_finito_concretizado_LEX('-AR','plural','2pessoa')

#######imperativo_I (afirmativo)



def realizacao_transitoriedade_imperativo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                            padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no imperativo_I,
    dados  o padrão de morfologia, tipo_pessoa de pessoa,número, padrão de pessoa da morfologia.

    >>>
    ''
    '''

	if OI_numero_LEX == 'singular':
		if OI_tipo_de_pessoa_LEX == '1pessoa':
			if (padrao_de_morfologia_LEX == '-AR' or
					padrao_de_morfologia_LEX == '-ER' or
					padrao_de_morfologia_LEX == '-IR' or
					padrao_de_morfologia_LEX == '-OR'):
				MI = 'Não há transitoriedade para imperativo_I na 1pessoa singular'

		elif OI_tipo_de_pessoa_LEX == '2pessoa':
			if padrao_de_morfologia_LEX == '-AR':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'a'
			elif (padrao_de_morfologia_LEX == '-ER' or padrao_de_morfologia_LEX == '-IR'):
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'e'
			elif  padrao_de_morfologia_LEX == '-OR':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'onha'
				else:
					MI = 'õe'
####
		elif OI_tipo_de_pessoa_LEX == '3pessoa':
			if padrao_de_morfologia_LEX == '-AR':
				MI = 'e'
			elif (padrao_de_morfologia_LEX == '-ER' or padrao_de_morfologia_LEX == '-IR') :
				MI = 'a'
			elif  padrao_de_morfologia_LEX == '-OR':
				MI = 'onha'
####
	elif OI_numero_LEX == 'plural':
		if OI_tipo_de_pessoa_LEX == '1pessoa':
			if padrao_de_morfologia_LEX == '-AR':
				MI = 'emos'
			elif padrao_de_morfologia_LEX == '-ER' or padrao_de_morfologia_LEX == '-IR':
				MI = 'amos'
			elif padrao_de_morfologia_LEX == '-OR':
				MI = 'onhamos'

		elif OI_tipo_de_pessoa_LEX == '2pessoa':
			if padrao_de_morfologia_LEX == '-AR':
				MI = 'ai'
			elif padrao_de_morfologia_LEX == '-ER':
				MI = 'ei'
			elif padrao_de_morfologia_LEX == '-IR':
				MI='i'
			elif padrao_de_morfologia_LEX == '-OR':
				MI = 'onde'

		elif OI_tipo_de_pessoa_LEX == '3pessoa':
			if padrao_de_morfologia_LEX == '-AR':
				MI='em'
			elif (padrao_de_morfologia_LEX == '-ER' or
			    padrao_de_morfologia_LEX == '-IR'):
				MI = 'am'
			elif padrao_de_morfologia_LEX == '-OR':
				MI= 'onham'
	return MI


#######imperativo_II (negativo)


def realizacao_transitoriedade_imperativo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
                                             padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no imperativo_II,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>
    ''
    '''

	if (padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'):
		MI = 'es'

	elif (
			(padrao_de_morfologia_LEX == '-ER' or '-IR')
			and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'as'

	elif (
			padrao_de_morfologia_LEX == '-OR'
			and OI_tipo_de_pessoa_LEX == '2pessoa'
			and OI_numero_LEX == 'singular'
	):
		MI = 'onhas'

	elif (
			padrao_de_morfologia_LEX == '-AR'
			and OI_tipo_de_pessoa_LEX == '3pessoa'
			and OI_numero_LEX == 'singular'
	):
		MI = 'e'

	elif (
			(
					padrao_de_morfologia_LEX == '-ER' or '-IR'
			)
			and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa'
			and OI_numero_LEX == 'singular'
	):
		MI = 'a'

	elif (
			padrao_de_morfologia_LEX == '-OR'
			and OI_tipo_de_pessoa_LEX == '3pessoa'
			and OI_numero_LEX == 'singular'
	):
		MI = 'onha'

	elif (
			padrao_de_morfologia_LEX == '-AR'
			and OI_tipo_de_pessoa_LEX == '1pessoa'
			and OI_numero_LEX == 'plural'
	):
		MI = 'emos'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'
	):
		MI = 'amos'

	elif (
			padrao_de_morfologia_LEX == '-OR'
			and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural'):
		MI = 'onhamos'

	elif (
			padrao_de_morfologia_LEX == '-AR'
			and OI_tipo_de_pessoa_LEX == '2pessoa'
			and OI_numero_LEX == 'plural'
	):
		MI = 'eis'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural'
	):
		MI = 'ais'

	elif (
			padrao_de_morfologia_LEX == '-OR'
			and OI_tipo_de_pessoa_LEX == '2pessoa'
			and OI_numero_LEX == 'plural'
	):
		MI = 'onhais'

	elif (
			padrao_de_morfologia_LEX == '-AR'
			and OI_tipo_de_pessoa_LEX == '3pessoa'
			and OI_numero_LEX == 'plural'
	):
		MI = 'em'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'
	):
		MI = 'am'

	elif (padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural'):
		MI = 'onham'

	elif (
			padrao_de_morfologia_LEX == '-AR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-ER' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-IR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular' or
			padrao_de_morfologia_LEX == '-OR' and OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular'
	):
		MI = 'Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida'

	return MI


# realizacao_transitoriedade_imperativo_II_LEX('-AR', '2pessoa','plural')
###gerúndio
# realizacao_transitoriedade_gerundio('-OR')

def realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX=None, OI_numero_LEX=None,
                                        OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX="Morfologia_padrão"
                                        ):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no gerúndio,
    dadoo padrão de morfologia.

    >>>
    '''
	if padrao_de_morfologia_LEX == '-AR':
		MI = 'ando'

	elif padrao_de_morfologia_LEX == '-ER':
		MI = 'endo'

	elif padrao_de_morfologia_LEX == '-IR':
		MI = 'indo'

	elif padrao_de_morfologia_LEX == '-OR':
		MI = 'ondo'

	return MI


# realizacao_transitoriedade_gerundio_LEX('-IR')

######particípio


def realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX=None,
                                          padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo_LEX no particípio,
    dados  o padrão de morfologia, tipo_pessoa de pessoa, e número.

    >>>realizacao_transitoriedade_particípio ()
    ''
    '''

	if padrao_de_morfologia_LEX == '-AR' and OI_numero_LEX == 'singular' and genero_LEX == 'feminino':
		MI = 'ada'

	elif padrao_de_morfologia_LEX == '-AR' and OI_numero_LEX == 'plural' and genero_LEX == 'feminino':
		MI = 'adas'

	elif padrao_de_morfologia_LEX == '-AR' and OI_numero_LEX == 'singular' and genero_LEX == 'masculino':
		MI = 'ado'

	elif padrao_de_morfologia_LEX == '-AR' and OI_numero_LEX == 'plural' and genero_LEX == 'masculino':
		MI = 'ados'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_numero_LEX == 'singular' and genero_LEX == 'masculino' or
			padrao_de_morfologia_LEX == '-IR' and OI_numero_LEX == 'singular' and genero_LEX == 'masculino'
	):
		MI = 'ido'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_numero_LEX == 'plural' and genero_LEX == 'masculino' or
			padrao_de_morfologia_LEX == '-IR' and OI_numero_LEX == 'plural' and genero_LEX == 'masculino'
	):
		MI = 'idos'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_numero_LEX == 'singular' and genero_LEX == 'feminino' or
			padrao_de_morfologia_LEX == '-IR' and OI_numero_LEX == 'singular' and genero_LEX == 'feminino'
	):
		MI = 'ida'

	elif (
			padrao_de_morfologia_LEX == '-ER' and OI_numero_LEX == 'plural' and genero_LEX == 'feminino' or
			padrao_de_morfologia_LEX == '-IR' and OI_numero_LEX == 'plural' and genero_LEX == 'feminino'
	):
		MI = 'idas'

	elif padrao_de_morfologia_LEX == '-OR' and OI_numero_LEX == 'singular' and genero_LEX == 'feminino':
		MI = 'osta'

	elif padrao_de_morfologia_LEX == '-OR' and OI_numero_LEX == 'singular' and genero_LEX == 'masculino':
		MI = 'osto'

	elif padrao_de_morfologia_LEX == '-OR' and OI_numero_LEX == 'plural' and genero_LEX == 'feminino':
		MI = 'ostas'

	elif padrao_de_morfologia_LEX == '-OR' and OI_numero_LEX == 'plural' and genero_LEX == 'masculino':
		MI = 'ostos'

	return MI


#
#
realizacao_transitoriedade_participio_LEX('-IR', 'plural', 'masculino')


# realizacao_transitoriedade_preterito_imperfectivo('-IR','singular','1pessoa')

def realizacao_transitoriedade_do_verbo_LEX(tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
                                            OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo_LEX no português
    brasileiro.

    >>> realizacao_transitoriedade_do_verbo_LEX()
    'o'

    '''

	if tipo_de_orientacao_LEX == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX=None,
		                                               OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX=None)

	elif tipo_de_orientacao_LEX == 'presente':
		MI = realizacao_transitoriedade_presente_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                         padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		MI = realizacao_transitoriedade_preterito_perfectivo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		MI = realizacao_transitoriedade_preterito_perfectivo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'futuro':
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                                      padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		MI = realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'imperativo_I':
		MI = realizacao_transitoriedade_imperativo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                                 padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		MI = realizacao_transitoriedade_imperativo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	elif tipo_de_orientacao_LEX == 'particípio':
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

	return MI
#
realizacao_transitoriedade_gerundio_LEX('-AR')
realizacao_transitoriedade_do_verbo_LEX('gerúndio','-AR',None,None,None)
realizacao_transitoriedade_do_verbo_LEX('presente','-AR','singular',None,'1pessoa')
realizacao_transitoriedade_do_verbo_LEX('pretérito_perfectivo_I','-IR','plural',None,'1pessoa')
realizacao_transitoriedade_do_verbo_LEX('pretérito_imperfectivo','-ER','plural',None,'2pessoa')
realizacao_transitoriedade_do_verbo_LEX('imperativo_I','-AR','singular',None,'2pessoa')
realizacao_transitoriedade_do_verbo_LEX('imperativo_II','-AR','singular',None,'2pessoa')
realizacao_transitoriedade_imperativo_I_LEX('-AR','singular','2pessoa')

# FORMAÇÃO DO verbo_LEX ###################

#
# def formação_da_estrutura_do_verbo_LEX1 (): #O tipo_de_experiência
# #aqui vai ter relação com o tipo_pessoa de configuração
#     '''
#     (str) -> str
#
#     Retorna um verbo_LEX flexionado dados OE_experiência_do_verbo_LEX,
#     OI_orientação_interpessoal_do_verbo_LEX.
#
#     >>> formação_da_estrutura_do_verbo_LEX ()
#     'levo'
#     >>>formação_da_estrutura_do_verbo_LEX ()
#     'levei'
#     '''
#     OE_experiência_do_verbo_LEX = experiencia_do_verbo_LEX()
#     OI_orientação_interpessoal_do_verbo_LEX = realizacao_transitoriedade_do_verbo_LEX ()
#
#     return OE_experiência_do_verbo_LEX + OI_orientação_interpessoal_do_verbo_LEX
# experiencia_do_verbo_LEX('andar')


#################
### FORMAÇÃO DOS verbo_LEXS IRREGULARES

# verbo_LEX agredir

def formacao_verbo_LEX_agredir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                           genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	# if tipo_de_orientacao_LEX == 'OI_não_orientado':
	#     verbo_LEX = formação_verbo_LEX_agredir_não_orientado()
	# elif tipo_de_orientacao_LEX == 'OI_finito':
	#     verbo_LEX = formação_verbo_LEX_agredir_finito()
	# else:
	#     verbo_LEX = formação_verbo_LEX_agredir_não_finito()
	# return verbo_LEX

	if tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'o'
				verbo_LEX = ME + 'id' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)] + 'id'

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'es'
					verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)] + 'id'
				MI = 'e'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)] + 'id'
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'imos'
					verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'is'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)] + 'id'
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'em'
					verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-4)] + 'id'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                      OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'imperativo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)]
					MI = 'a'
					verbo_LEX = ME + "ir" + MI
				else:
					ME = verbo_LEX[slice(-4)]
					MI = 'e'
					verbo_LEX = ME + "id" + MI
			else:
				ME = verbo_LEX[slice(-4)]
				MI = 'a'
				verbo_LEX = ME + "id" + MI

		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'id' + MI
				else:
					MI = 'amos'
					verbo_LEX = ME + 'id' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'i'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'id' + MI

				else:
					MI = 'am'
					verbo_LEX = ME + 'id' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'id' + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	return verbo_LEX


# formacao_verbo_LEX_agredir('agredir','particípio','-IR','plural','masculino',None)
# formacao_verbo_LEX_agredir('agredir','particípio','-IR','singular','masculino',None)
# formacao_verbo_LEX_agredir('agredir','gerúndio','-IR',None,None,None)
# formacao_verbo_LEX_agredir('agredir', 'infinitivo', '-IR', None, None, None)
# formacao_verbo_LEX_agredir('agredir', 'pretérito_perfectivo_II', '-IR', 'singular', None, '1pessoa')
# formacao_verbo_LEX_agredir('agredir','pretérito_imperfectivo','-IR','singular',None,'1pessoa')

# verbo_LEX aferir


def formacao_verbo_LEX_aferir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                          genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	if tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'o'
				verbo_LEX = ME + 'ir' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'es'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'e'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'imos'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'is'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'em'
					verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-4)] + 'ir'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                      OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)]
					MI = 'a'
					verbo_LEX = ME + "ir" + MI
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'e'
					verbo_LEX = ME + MI
			else:
				ME = verbo_LEX[slice(-4)]
				MI = 'a'
				verbo_LEX = ME + "ir" + MI

		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'ir' + MI
				else:
					MI = 'amos'
					verbo_LEX = ME + 'ir' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'i'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'ir' + MI

				else:
					MI = 'am'
					verbo_LEX = ME + 'ir' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'ir' + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]

		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]

		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	return verbo_LEX


#
# formacao_verbo_LEX_aferir('aferir', 'não_finito_concretizado', '-IR', 'singular', None, '2pessoa')
# formacao_verbo_LEX_aferir('aferir', 'subjuntivo_optativo', '-IR', 'singular', None, '2pessoa')
# formacao_verbo_LEX_aferir('aferir', 'particípio', '-IR', 'singular', 'masculino', None)
# formacao_verbo_LEX_agredir('aferir','particípio','-IR','singular','feminino',None)


# verbo_LEX MEDIR
def formacao_verbo_LEX_medir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                         genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	if tipo_de_orientacao_LEX == 'presente':

		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-3)]
				MI = 'o'
				verbo_LEX = ME + 'ç' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'es'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'e'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'imos'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'is'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
					verbo_LEX = ME + MI
				else:
					MI = 'em'
					verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_I_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_perfectivo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	if tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-4)] + 'eç'
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                      OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_condicionalsubjuntivo_condicional(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                                             OI_tipo_de_pessoa_LEX,
		                                                                             padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':

		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				print('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)]
					MI = 'a'
					verbo_LEX = ME + "eç" + MI

				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'e'
					verbo_LEX = ME + MI
			else:
				ME = verbo_LEX[slice(-4)]
				MI = 'a'
				verbo_LEX = ME + "eç" + MI

		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'eç' + MI
				else:
					MI = 'amos'
					verbo_LEX = ME + 'eç' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'i'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa':
			ME = verbo_LEX[slice(-4)]

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'a'
				verbo_LEX = ME + 'eç' + MI
			else:
				MI = 'am'
				verbo_LEX = ME + 'eç' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_imperativo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'eç' + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	return verbo_LEX


#
# formacao_verbo_LEX_medir('medir','presente','-IR','singular',None,'2pessoa')
# formacao_verbo_LEX_medir('medir','presente','-IR','singular',None,'3pessoa')
# formacao_verbo_LEX_medir('medir','presente','-IR','singular',None,'1pessoa')
# formacao_verbo_LEX_medir('medir', 'infinitivo', '-IR', 'singular', 'masculino', None)
# formacao_verbo_LEX_medir('medir','particípio','-IR','singular','feminino',None)
# formacao_verbo_LEX_medir('medir','gerúndio','-IR',None,None,None)


# verbo_LEX SABER
def formacao_verbo_LEX_saber(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                         genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	if tipo_de_orientacao_LEX == 'infinitivo':
		verbo_LEX = verbo_LEX

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	#

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)

		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'presente':

		if OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular':
			ME = verbo_LEX[slice(-4)]
			MI = 'ei'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
			ME = verbo_LEX[slice(-2)]

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'e'
				verbo_LEX = ME + MI

			else:
				MI = 'es'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular':
			ME = verbo_LEX[slice(-2)]
			MI = 'e'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				ME = verbo_LEX[slice(-2)]
				MI = 'e'
				verbo_LEX = ME + MI

			else:
				ME = verbo_LEX[slice(-2)]
				MI = 'emos'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
			ME = verbo_LEX[slice(-2)]
			MI = 'eis'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				ME = verbo_LEX[slice(-2)]
				MI = 'e'
				verbo_LEX = ME + MI

			else:
				ME = verbo_LEX[slice(-2)]
				MI = 'em'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		ME = verbo_LEX[slice(-4)]
		if OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular':
			MI = 'oube'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oube'
				verbo_LEX = ME + MI

			else:
				MI = 'ste'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular':

			MI = 'oube'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oube'
				verbo_LEX = ME + MI
			else:
				MI = 'oubemos'
				verbo_LEX = ME + MI


		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':

			MI = 'oubestes'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oube'
				verbo_LEX = ME + MI

			else:
				MI = 'ouberam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = verbo_LEX[slice(-4)]
		if ((OI_tipo_de_pessoa_LEX == '1pessoa' or '3pessoa') and OI_numero_LEX == 'singular'):
			MI = 'oubera'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubera'
				verbo_LEX = ME + MI
			else:
				MI = 'ouberas'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubera'
				verbo_LEX = ME + MI
			else:
				MI = 'oubéramos'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubera'
				verbo_LEX = ME + MI

			else:
				MI = 'oubéreis'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubera'
				verbo_LEX = ME + MI

			else:
				MI = 'ouberam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':

		ME = verbo_LEX[slice(-4)]
		if (OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular'
				or OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular'):
			MI = 'oubesse'
			verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':
			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo_LEX = ME + MI
			else:
				MI = 'oubesses'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo_LEX = ME + MI
			else:
				MI = 'oubésssemos'
				verbo_LEX = ME + MI
		#
		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo_LEX = ME + MI
			else:
				MI = 'oubésseis'
				verbo_LEX = ME + MI
		#
		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'oubesse'
				verbo_LEX = ME + MI
			else:
				MI = 'oubessem'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                      OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'aib' + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'oub' + MI
	#
	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'oub' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':

		ME = verbo_LEX[slice(-4)]
		if OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular':
			return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'a'
				verbo_LEX = ME + "aib" + MI
			else:
				MI = 'e'
				verbo_LEX = ME + 'ab' + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'singular':
			MI = 'a'
			verbo_LEX = ME + 'aib' + MI

		elif OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'plural':
			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'a'
				verbo_LEX = ME + 'aib' + MI
			else:
				MI = 'amos'
				verbo_LEX = ME + 'aib' + MI

		elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
			MI = 'ei'
			verbo_LEX = ME + 'ab' + MI

		elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
			if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
				MI = 'a'
				verbo_LEX = ME + 'aib' + MI
			else:
				MI = 'am'
				verbo_LEX = ME + 'aib' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-4)]
		if OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular':
			return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"
		else:
			MI = realizacao_transitoriedade_imperativo_II_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
			                                                  OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'aib' + MI

	return verbo_LEX


#
# formacao_verbo_LEX_saber('saber', 'pretérito_imperfectivo', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_LEX_saber('saber', 'presente', '-ER', 'singular', None, '3pessoa')
# formacao_verbo_LEX_saber('saber', 'presente', '-ER', 'singular', None, '1pessoa')
# formacao_verbo_LEX_saber('saber', 'particípio', '-ER', 'singular', 'feminino', None)
# formacao_verbo_LEX_saber('saber', 'gerúndio', '-ER', None, None, None)
# formacao_verbo_LEX_saber('saber', 'não_finito_concretizado', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_LEX_saber('saber', 'futuro', '-ER', 'singular', None, '1pessoa')
# formacao_verbo_LEX_saber('saber', 'passado_volitivo', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_LEX_saber('saber', 'pretérito_perfectivo_I', '-ER', 'singular', None, '3pessoa')
# formacao_verbo_LEX_saber('saber', 'pretérito_perfectivo_II', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_LEX_saber('saber', 'subjuntivo_condicional', '-ER', 'plural', None, '2pessoa')
# formacao_verbo_LEX_saber('saber', 'subjuntivo_conjuntivo', '-ER', 'plural', None, '3pessoa')
# formacao_verbo_LEX_saber('saber', 'imperativo_II', '-ER', 'singular', None, '1pessoa')
# formacao_verbo_LEX_saber('saber', 'imperativo_I', '-ER', 'singular', None, '2pessoa')


# verbo_LEX ESTAR

def formacao_verbo_LEX_estar(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                         genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''
	ME = verbo_LEX[slice(-2)]
	if tipo_de_orientacao_LEX == 'subjuntivo_condicional':

		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa' or OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'esse'
				verbo_LEX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
				verbo_LEX = ME + 'iv' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo_LEX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo_LEX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
				verbo_LEX = ME + 'iv' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa' or OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'a'
				verbo_LEX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + 'ej' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_LEX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'ej' + MI


	elif tipo_de_orientacao_LEX == 'imperativo_I':

		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'ej' + MI
				else:
					MI = 'á'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'a'
				verbo_LEX = ME + 'ej' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				MI = 'ai'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'ej' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':

		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = 'Imperativos não selecionam 1pessoa do singular'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'a'
				verbo_LEX = ME + 'ej' + MI
		if OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_LEX = ME + 'ej' + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'ej' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':

		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa' or OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'er'
				verbo_LEX = ME + 'iv' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
				verbo_LEX = ME + 'iv' + MI

		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'
				verbo_LEX = ME + 'iv' + MI

			if OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo_LEX = ME + 'iv' + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
				verbo_LEX = ME + 'iv' + MI
	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':

		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'futuro':

		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':

		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				MI = 'ou'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'á'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '2pessoa'):

				MI = realizacao_transitoriedade_presente(padrao_de_morfologia_LEX, OI_numero_LEX,
				                                         OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'ão'
			verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				MI = 'ive'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'eve'
				verbo_LEX = ME + MI
		if OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
				verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		if OI_numero_LEX == 'singular':

			if OI_tipo_de_pessoa_LEX == '1pessoa':

				MI = 'ivera'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				MI = 'ivera'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'

				verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':

		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'infinitivo':

		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':

		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	elif tipo_de_orientacao_LEX == 'particípio':

		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	return verbo_LEX


# verbo_LEX DIZER

def formacao_verbo_LEX_dizer(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                         genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-3)]
				MI = 'go'
				verbo_LEX = ME + MI


			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = ''
					verbo_LEX = ME + MI

				else:
					MI = 'es'
					verbo_LEX = ME + MI


			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'em'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = ''
					verbo_LEX = ME + MI

				else:
					MI = 'emos'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = ''
					verbo_LEX = ME + MI

				else:
					MI = 'eis'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-2)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = ''
					verbo_LEX = ME + MI

				else:
					MI = 'em'
					verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'isse'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == "3pessoa_do_singular":
					MI = 'isse'
					verbo_LEX = ME + MI

				else:
					MI = 'isseste'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'isse'
				verbo_LEX = ME + MI

		elif OI_tipo_de_pessoa_LEX == '1pessoa':
			ME = verbo_LEX[slice(-4)]
			if padrao_pessoa_morfologia_LEX == "3pessoa_do_singular":
				MI = 'isse'
				verbo_LEX = ME + MI

			else:
				MI = 'issemos'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == "3pessoa_do_singular":
					MI = 'isse'
					verbo_LEX = ME + MI

				else:
					MI = 'issestes'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == "3pessoa_do_singular":
					MI = 'isse'
					verbo_LEX = ME + MI
				else:
					MI = 'isseram'
					verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'ia'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ia'

				else:
					MI = 'ias'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'íamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ia'
				else:
					MI = 'íeis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ia'
				else:
					MI = 'iam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'issera'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issera'
					verbo_LEX = ME + MI

				else:
					MI = 'isseras'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'issera'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issera'
					verbo_LEX = ME + MI

				else:
					MI = 'isséramos'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issera'
					verbo_LEX = ME + MI

				else:
					MI = 'isséreis'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issera'


				else:
					MI = 'isseram'

				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'iria'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'irias'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iríamos'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iríeis'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iria'
				else:
					MI = 'iriam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-3)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI[1:]
	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'issesse'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issesses'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issesse'
					verbo_LEX = ME + MI

				else:
					MI = 'isséssemos'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issésseis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'issesse'
				else:
					MI = 'issessem'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-3)]
		if OI_numero_LEX == 'singular':

			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):

				MI = 'a'
				verbo_LEX = ME + 'g' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'singular':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'g' + MI
				else:
					MI = 'as'
					verbo_LEX = ME + 'g' + MI
		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'g' + MI
				else:
					MI = 'amos'
					verbo_LEX = ME + 'g' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'g' + MI
				else:
					MI = 'ais'
					verbo_LEX = ME + 'g' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'g' + MI
				else:
					MI = 'am'
					verbo_LEX = ME + 'g' + MI


	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI


	elif tipo_de_orientacao_LEX == 'imperativo_I':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = 'Imperativos não selecionam 1pessoa do singular'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'
					verbo_LEX = ME + MI
				else:
					MI = 'iz'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'iga'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'izei'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igam'
				verbo_LEX = ME + MI


	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = 'Imperativos não selecionam 1pessoa do singular'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'
				else:
					MI = 'igas'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'iga'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igais'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iga'

				else:
					MI = 'igam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				ME = verbo_LEX[slice(-4)]
				MI = 'er'
				verbo_LEX = ME + 'iss' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'eres'
					verbo_LEX = ME + 'iss' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'ermos'
				verbo_LEX = ME + 'iss' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'
				verbo_LEX = ME + 'iss' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'

				else:
					MI = 'erem'
				verbo_LEX = ME + 'iss' + MI
	elif tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]

	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if genero_LEX == 'masculino':
				MI = 'ito'
			else:
				MI = 'ita'
		else:
			if genero_LEX == 'masculino':
				MI = 'itos'
			else:
				MI = 'itas'

		verbo_LEX = ME + MI
	return verbo_LEX


#
# ##TESTE dizer
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# ###
# print("A conjugação é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'presente', '-ER', numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# #futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# #subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# #subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
#
# #subjuntivo_optativo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
#
# # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_II
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # não_finito_concretizado
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_dizer('dizer', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_LEX_dizer('dizer', 'infinitivo', '-ER', numero, 'feminino', None))
#
# # gerúndio
# print(formacao_verbo_LEX_dizer('dizer', 'gerúndio', '-ER', None, None, None))
#
# # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_dizer('dizer', 'particípio', '-ER', numero, genero_LEX, None))
#


# verbo_LEX TER

def formacao_verbo_LEX_ter(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
                       OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                       padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	"""
    :return:
    """

	if tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-2)]

		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'esse'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'esses'
			verbo_LEX = ME + 'iv' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'essem'
			verbo_LEX = ME + 'iv' + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-2)]

		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo_LEX = ME + 'enh' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
			verbo_LEX = ME + 'enh' + MI
	###
	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'imperativo_I':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'enh' + MI
				else:
					MI = 'em'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'enh' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'enh' + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'ende'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'enh' + MI
	###
	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'enh' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'enh' + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
			verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
			verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]

		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'a'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo_LEX = ME + 'inh' + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'inh' + MI
				else:
					MI = 'amos'
					verbo_LEX = ME + 'ính' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'inh' + MI
				else:
					MI = 'eis'
					verbo_LEX = ME + 'ính' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'inh' + MI
				else:
					MI = 'am'
					verbo_LEX = ME + 'inh' + MI
	###
	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'presente':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'enho'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'ens'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'em'
			verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'endes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'

			verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'ive'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveste'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'eve'
			verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivemos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'ivestes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eve'
				else:
					MI = 'iveram'
			verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'ivera'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveras'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'ivera'
			verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéramos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'ivéreis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa' and OI_numero_LEX == 'plural':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'iveram'
			verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	return verbo_LEX


# 
# ##TESTE ter
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# #presente
# print("A conjugação é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'presente', '-ER', numero, None, tipo_pessoa))
# 
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# 
# #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# 
# ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# 
# ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# 
# # futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'futuro', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_optativo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# 
# # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# 
# # imperativo_II
# 
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# 
# # # não_finito_concretizado
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ter('ter', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_LEX_ter('ter', 'infinitivo', '-ER', numero, 'feminino', None))
# 
# # # gerúndio
# print(formacao_verbo_LEX_ter('ter', 'gerúndio', '-ER', None, None, None))
# #
# # # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_ter('ter', 'particípio', '-ER', numero, genero_LEX, None))

# ####################################################################################

# verbo_LEX SER

def formacao_verbo_LEX_ser(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                       padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		if OI_numero_LEX == 'singular':
			ME = 'er'
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'a'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':

			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'amos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = 'er'
					MI = 'a'
				else:
					ME = 'ér'
					MI = 'eis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'er'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]

		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'ou'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = ''
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'é'
				else:
					MI = 'és'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = ''
				MI = 'é'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'omos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'ois'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = ''
					MI = 'é'
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'ão'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':

		ME = 'f'
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'ui'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'oi'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
					verbo_LEX = ME + MI
				else:
					MI = 'omos'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'ostes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = 'f'
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'ora'
				verbo_LEX = ME + MI


			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':

		ME = 'f'
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'osse'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
					verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                                      padrao_pessoa_morfologia_LEX="Morfologia_padrão")
		verbo_LEX = ME + 'ej' + MI
	###
	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'or'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo_LEX = ME + MI



		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'imperativo_I':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'ej' + MI
				else:
					MI = 'ê'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'ej' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'ede'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'ej' + MI
	###
	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = verbo_LEX[slice(-2)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'ej' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa' and OI_numero_LEX == 'plural':
				MI = 'ais'
				verbo_LEX = ME + 'ej' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'ej' + MI

	return verbo_LEX


# # ##TESTE ser
OI_numero_LEXs = ['singular', "plural"]
OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# ###
# # #presente
# print("A conjugação é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'presente', '-ER', numero, None, tipo_pessoa))
# 
# # ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# 
# # #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # 
# # ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# 
# # ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# 
# # # futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'futuro', '-ER', numero, None, tipo_pessoa))
# 
# # # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# 
# # subjuntivo_optativo
# 
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# 
# # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# 
# # # imperativo_II
# 
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# 
# # # # não_finito_concretizado
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ser('ser', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # infinitivo
# print(formacao_verbo_LEX_ser('ser', 'infinitivo', '-ER', numero, 'feminino', None))
# #
# # # # gerúndio
# print(formacao_verbo_LEX_ser('ser', 'gerúndio', '-ER', None, None, None))
# # #
# # # # particípio
genero_LEXs = ['masculino', 'feminino']
for numero in OI_numero_LEXs:
	for genero_LEX in genero_LEXs:
		print(formacao_verbo_LEX_ser('ser', 'particípio', '-ER', numero, genero_LEX, None))


# ####################################################################################

# verbo_LEX IR

def formacao_verbo_LEX_ir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                      genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao_LEX == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = MI
	###
	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'v'
				MI = 'ou'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'ais'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'v'
				MI = 'ai'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'amos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'i'
				MI = 'des'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ai'
				else:
					MI = 'am'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'f'
				MI = 'ui'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oste'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'f'
				MI = 'oi'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'omos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'ostes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'f'

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'oi'
				else:
					MI = 'oram'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				ME = 'f'
				MI = 'ora'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oras'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôramos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'ôreis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'f'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ora'
				else:
					MI = 'oram'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = 'f'
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'osse'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'osses'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôssemos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ôsseis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'osse'
				else:
					MI = 'ossem'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				ME = 'v'
				MI = 'á'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'imperativo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ai'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'v'
				MI = 'á'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = 'i'
				MI = 'de'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = 'v'
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'imperativo_II':
		ME = 'v'
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'á'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'amos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ades'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ão'
				verbo_LEX = ME + MI
	###
	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = 'f'
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'or'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ores'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ormos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'ordes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'or'
				else:
					MI = 'orem'
				verbo_LEX = ME + MI

	return verbo_LEX


# #
# # #
# # # # ##TESTE ir
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'presente', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # #####pretérito_imperfectivo
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # ###passado_volitivo
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # # futuro
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'futuro', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_conjuntivo
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_ir('ir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
# 
# # # # subjuntivo_optativo
# # #
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # imperativo_I
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_II
# #
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # não_finito_concretizado
# #
# # for numero in OI_numero_LEXs:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_LEX_ir('ir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# #
# # # # # infinitivo
# # print(formacao_verbo_LEX_ir('ir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # #
# # # # # # gerúndio
# # print(formacao_verbo_LEX_ir('ir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# # # genero_LEXs = ['masculino', 'feminino']
# # for numero in OI_numero_LEXs:
# # 	for genero_LEX in genero_LEXs:
# # 		print(formacao_verbo_LEX_ir('ir', 'particípio', '-IR', numero, genero_LEX, None))


# verbo_LEXS VIR E INTERVIR


def formacao_verbo_LEX_vir_intervir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
                                OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                                padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''
	ME = verbo_LEX[slice(-2)]

	if tipo_de_orientacao_LEX == 'infinitivo':
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'inha'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inhas'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínhamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'ínheis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'inha'
				else:
					MI = 'inham'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'particípio':
		if OI_numero_LEX == 'singular':
			if genero_LEX == 'masculino':
				MI = 'indo'
			else:
				MI = 'inda'
		else:
			if genero_LEX == 'masculino':
				MI = 'indos'
			else:
				MI = 'indas'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'enho'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if verbo_LEX == 'vir':
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'em'
					else:
						MI = 'ens'
					verbo_LEX = ME + MI
				else:
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'ém'
					else:
						MI = 'éns'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if verbo_LEX == 'vir':
					MI = 'em'
				else:
					MI = 'ém'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'imos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'indes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'em'
				else:
					MI = 'êm'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'im'
				verbo_LEX = ME + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieste'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'eio'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'iemos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'iestes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'eio'
				else:
					MI = 'ieram'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'iera'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieras'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéramos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'iéreis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iera'
				else:
					MI = 'ieram'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'iesse'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iesses'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iéssemos'
				verbo_LEX = ME + '' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'iésseis'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'iesse'
				else:
					MI = 'iessem'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'a'
				verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhas'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enhais'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'enha'
				else:
					MI = 'enham'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if verbo_LEX == 'vir':
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'a'
						verbo_LEX = ME + 'enh' + MI
					else:
						MI = 'em'
						verbo_LEX = ME + MI
				else:
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'a'
						verbo_LEX = ME + 'enh' + MI
					else:
						MI = 'ém'
						verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'enh' + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'enhamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'inde'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'enh' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'enh' + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_LEX = verbo_LEX = ME + 'enh' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = verbo_LEX = ME + 'enh' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'ier'
				verbo_LEX = ME + MI

			if OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ieres'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'iermos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierdes'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ier'
				else:
					MI = 'ierem'
				verbo_LEX = ME + MI
	return verbo_LEX


#
# # #
# # # # ##TESTE intervir
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_LEX_vir_intervir('intervir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_LEX_vir_intervir('intervir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_vir_intervir('intervir', 'particípio', '-IR', numero, genero_LEX, None))
#
# ######################################
#
#
# # # # ##TESTE vir
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # #presente
# # print("A conjugação é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'presente', '-IR', numero, None, tipo_pessoa))
#
# # # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
#
# # # # # futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'futuro', '-IR', numero, None, tipo_pessoa))
#
# # # # # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
#
# # # # subjuntivo_optativo
# # #
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# #
# # # # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# #
# # # # # imperativo_II
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
#
# # # # # # não_finito_concretizado
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
#
# # # # infinitivo
# print(formacao_verbo_LEX_vir_intervir('vir', 'infinitivo', '-IR', numero, 'feminino', None))
# # #
# # # # # # gerúndio
# print(formacao_verbo_LEX_vir_intervir('vir', 'gerúndio', '-IR', None, None, None))
# # # # #
# # # # # # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_vir_intervir('vir', 'particípio', '-IR', numero, genero_LEX, None))


# verbo_LEX HAVER
def formacao_verbo_LEX_haver(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
                         OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                         padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = 'ido'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			ME = verbo_LEX[slice(-4)]
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'ei'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'á'
				else:
					MI = 'ás'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'á'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)]
					MI = 'á'
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'emos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					ME = verbo_LEX[slice(-4)]
					MI = 'á'
				else:
					ME = verbo_LEX[slice(-2)]
					MI = 'eis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'ão'

		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'e'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'este'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'e'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'emos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'estes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'e'
				else:
					MI = 'eram'

		verbo_LEX = ME + 'ouv' + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'era'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'eras'


			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'era'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éramos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'éreis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'era'
				else:
					MI = 'eram'
		verbo_LEX = ME + 'ouv' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '2pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				ME = verbo_LEX[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
				                                                           OI_tipo_de_pessoa_LEX,
				                                                           padrao_pessoa_morfologia_LEX)
				verbo_LEX = ME + 'ouv' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
					verbo_LEX = ME + 'ud' + MI
				else:
					MI = 'éssemos'
					verbo_LEX = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo_LEX = ME + 'ouv' + MI
			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
				                                                           OI_tipo_de_pessoa_LEX,
				                                                           padrao_pessoa_morfologia_LEX)
				verbo_LEX = ME + 'ouv' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				ME = verbo_LEX[slice(-4)]
				MI = 'a'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
			verbo_LEX = ME + 'aj' + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ais'
				verbo_LEX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'aj' + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'aj' + MI
				else:
					MI = 'á'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'a'
				verbo_LEX = ME + 'aj' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'ei'
				verbo_LEX = ME + 'av' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'aj' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'
				verbo_LEX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'a'
				verbo_LEX = ME + 'aj' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + MI
				else:
					MI = 'amos'
					verbo_LEX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'
				verbo_LEX = ME + 'aj' + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'aj' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'er'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo_LEX = ME + 'ouv' + MI

	return verbo_LEX


# # # # # ##TESTE haver
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # imperativo_II
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # não_finito_concretizado
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_haver('haver', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # infinitivo
# print(formacao_verbo_LEX_haver('haver', 'infinitivo', '-ER', numero, 'feminino', None))
# # # #
# # # # # # # gerúndio
# print(formacao_verbo_LEX_haver('haver', 'gerúndio', '-ER', None, None, None))
# # # # # #
# # # # # # # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_haver('haver', 'particípio', '-ER', numero, genero_LEX, None))

# verbo_LEX PODER

def formacao_verbo_LEX_poder(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
                         OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''
	if tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                           padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_passado_volitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                     OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX,
		                                               OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'presente':

		if OI_tipo_de_pessoa_LEX == '1pessoa' and OI_numero_LEX == 'singular':
			ME = verbo_LEX[slice(-3)]
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia_LEX,
			                                         OI_numero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
			verbo_LEX = ME + 'ss' + MI


		else:
			ME = verbo_LEX[slice(-2)]
			MI = realizacao_transitoriedade_presente(padrao_de_morfologia_LEX,
			                                         OI_numero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
			verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'ude'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udeste'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'ôde'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udemos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'udestes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ôde'
				else:
					MI = 'uderam'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'udera'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'uderas'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'udera'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'udéramos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'udéreis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'udera'
				else:
					MI = 'uderam'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '2pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
				                                                           OI_tipo_de_pessoa_LEX,
				                                                           padrao_pessoa_morfologia_LEX)
				verbo_LEX = ME + 'ud' + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = realizacao_transitoriedade_subjuntivo_condicional_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
				                                                           OI_tipo_de_pessoa_LEX,
				                                                           padrao_pessoa_morfologia_LEX)
				verbo_LEX = ME + 'ud' + MI

			elif OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'éssemos'
				verbo_LEX = ME + 'ud' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'esse'
				else:
					MI = 'ésseis'
				verbo_LEX = ME + 'ud' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-4)]

		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'ossa'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossas'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossais'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ode'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'ossa'
				verbo_LEX = ME + MI

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'odei'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = ('Imperativos não selecionam 1pessoa do singular')

			if OI_tipo_de_pessoa_LEX == '2pessoa':

				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossas'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'ossa'
				verbo_LEX = ME + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossamos'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossais'
				verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ossa'
				else:
					MI = 'ossam'
				verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-4)]
		MI = realizacao_transitoriedade_subjuntivo_optativo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                        OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + 'ud' + MI

	return verbo_LEX


# # # # ##TESTE poder
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # # # # #presente
# # # print("A conjugação é:")
# 
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'presente', '-ER', numero, None, tipo_pessoa))
# 
# # # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # futuro
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'futuro', '-ER', numero, None, tipo_pessoa))
# 
# # # # # # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # subjuntivo_optativo
# # # # #
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # imperativo_II
# 
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# 
# # # # # # # não_finito_concretizado
# 
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_poder('poder', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# 
# # # # # # infinitivo
# print(formacao_verbo_LEX_poder('poder', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # gerúndio
# print(formacao_verbo_LEX_poder('poder', 'gerúndio', '-ER', None, None, None))
# # # # # # #
# # # # # # # # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_poder('poder', 'particípio', '-ER', numero, genero_LEX, None))
# 


# verbo_LEX FAZER


def formacao_verbo_LEX_fazer(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                         genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):
	'''
    '''

	if tipo_de_orientacao_LEX == 'presente':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-3)]
				MI = 'ço'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-2)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = ''
				else:
					MI = 'es'
			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'az'
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-2)]
				MI = 'emos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'azeis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'azem'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_I':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'iz'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izeste'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'ez'
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izemos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izestes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ez'
				else:
					MI = 'izeram'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_perfectivo_II':
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'izera'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izeras'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				MI = 'izera'
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izéramos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izera'
				else:
					MI = 'izéreis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				ME = verbo_LEX[slice(-4)]
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'ivera'
				else:
					MI = 'izeram'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'pretérito_imperfectivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_preterito_imperfectivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                           OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'futuro':
		ME = verbo_LEX[slice(-3)]
		MI = \
		realizacao_transitoriedade_futuro_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                      padrao_pessoa_morfologia_LEX)[
			slice(1, 7)]
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'passado_volitivo':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'aria'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'aria'
				else:
					MI = 'arias'
			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'aria'


		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'aríamos'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				MI = 'aríeis'
			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'ariam'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_condicional':
		ME = verbo_LEX[slice(-4)]

		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'izesse'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izesses'
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izéssemos'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izésseis'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'izesse'
				else:
					MI = 'izessem'
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_conjuntivo':
		ME = verbo_LEX[slice(-3)]
		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'a'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'as'

			elif OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'

		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				MI = 'amos'
			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'ais'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
		verbo_LEX = ME + 'ç' + MI

	elif tipo_de_orientacao_LEX == 'subjuntivo_optativo':
		ME = verbo_LEX[slice(-4)]

		if OI_numero_LEX == 'singular':
			if (OI_tipo_de_pessoa_LEX == '1pessoa' or
					OI_tipo_de_pessoa_LEX == '3pessoa'):
				MI = 'er'
			if OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'eres'
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'ermos'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erdes'

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'er'
				else:
					MI = 'erem'
		verbo_LEX = ME + 'iz' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_I':
		ME = verbo_LEX[slice(-3)]
		if OI_numero_LEX == 'singular':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				verbo_LEX = 'Imperativos não selecionam 1pessoa do singular.'

			elif OI_tipo_de_pessoa_LEX == '2pessoa':

				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'ç' + MI
				else:
					MI = 'z'
					verbo_LEX = ME + MI

			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				MI = 'a'
				verbo_LEX = ME + 'ç' + MI
		elif OI_numero_LEX == 'plural':
			if OI_tipo_de_pessoa_LEX == '1pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'amos'
				verbo_LEX = ME + 'ç' + MI

			elif OI_tipo_de_pessoa_LEX == '2pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
					verbo_LEX = ME + 'ç' + MI
				else:
					MI = 'ei'
					verbo_LEX = ME + 'z' + MI


			elif OI_tipo_de_pessoa_LEX == '3pessoa':
				if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
					MI = 'a'
				else:
					MI = 'am'
				verbo_LEX = ME + 'ç' + MI

	elif tipo_de_orientacao_LEX == 'imperativo_II':
		if tipo_de_orientacao_LEX == 'imperativo_II':
			ME = verbo_LEX[slice(-3)]
			if OI_numero_LEX == 'singular':
				if OI_tipo_de_pessoa_LEX == '1pessoa':
					verbo_LEX = 'Imperativos não selecionam 1pessoa do singular. Selecione novamente:'
				elif OI_tipo_de_pessoa_LEX == '2pessoa':
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'as'
					verbo_LEX = ME + 'ç' + MI

				elif OI_tipo_de_pessoa_LEX == '3pessoa':
					MI = 'a'
					verbo_LEX = ME + 'ç' + MI

			elif OI_numero_LEX == 'plural':

				if OI_tipo_de_pessoa_LEX == '1pessoa':
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'amos'
					verbo_LEX = ME + 'ç' + MI

				elif OI_tipo_de_pessoa_LEX == '2pessoa':
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'ais'
					verbo_LEX = ME + 'ç' + MI

				elif OI_tipo_de_pessoa_LEX == '3pessoa':
					if padrao_pessoa_morfologia_LEX == '3pessoa_do_singular':
						MI = 'a'
					else:
						MI = 'am'
					verbo_LEX = ME + 'ç' + MI

	elif tipo_de_orientacao_LEX == 'não_finito_concretizado':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_nao_finito_concretizado_LEX(padrao_de_morfologia_LEX, OI_numero_LEX,
		                                                            OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'infinitivo':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_infinitivo_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, OI_tipo_de_pessoa_LEX,
		                                               padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'gerúndio':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_gerundio_LEX(padrao_de_morfologia_LEX, genero_LEX, OI_numero_LEX,
		                                             OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX)
		verbo_LEX = ME + MI

	elif tipo_de_orientacao_LEX == 'particípio':
		ME = verbo_LEX[slice(-4)]
		if OI_numero_LEX == 'singular':
			if genero_LEX == 'feminino':
				MI = 'eita'
			elif genero_LEX == 'masculino':
				MI = 'eito'
		elif OI_numero_LEX == 'plural':
			if genero_LEX == 'feminino':
				MI = 'eitas'
			elif genero_LEX == 'masculino':
				MI = 'eitos'
		verbo_LEX = ME + MI
	return verbo_LEX


# #
# #
# # # # # # ##TESTE fazer
# OI_numero_LEXs = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # # ###
# # # # # # #presente
# # # # print("A conjugação é:")
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'presente', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # ###
# # # # print("A conjugação pretérito_perfectivo_I é:")
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # #####pretérito_imperfectivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # # #
# # # # # # ### "pretérito_perfectivo_II"
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # ###passado_volitivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # # futuro
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # subjuntivo_conjuntivo
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # subjuntivo_condicional
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # subjuntivo_optativo
# # # # # #
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # imperativo_I
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # imperativo_II
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # # não_finito_concretizado
#
# for numero in OI_numero_LEXs:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_LEX_fazer('fazer', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
#
# # # # # # # infinitivo
# print(formacao_verbo_LEX_fazer('fazer', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # # gerúndio
# print(formacao_verbo_LEX_fazer('fazer', 'gerúndio', '-ER', None, None, None))
# # # # # # # #
# # # # # # # # # particípio
# genero_LEXs = ['masculino', 'feminino']
# for numero in OI_numero_LEXs:
# 	for genero_LEX in genero_LEXs:
# 		print(formacao_verbo_LEX_fazer('fazer', 'particípio', '-ER', numero, genero_LEX, None))
#

#################################################################################


def formacao_da_estrutura_do_verbo_LEX_finito():
	'''
    '''
	prompt = "Qual é o verbo_LEX lematizado desejado?"
	verbo_LEX = input(prompt)

	if verbo_LEX == 'estar':
		verbo_LEX = formação_verbo_LEX_estar_finito()
	elif verbo_LEX == 'ser':
		verbo_LEX = formação_verbo_LEX_ser_finito()
	elif verbo_LEX == 'ir':
		verbo_LEX = formação_verbo_LEX_ir_finito()
	elif (verbo_LEX == 'vir' or verbo_LEX == 'intervir'):
		verbo_LEX = formação_verbo_LEX_vir_intervir_finito()
	elif verbo_LEX == 'haver':
		verbo_LEX = formação_verbo_LEX_haver_finito()
	elif verbo_LEX == 'ter':
		verbo_LEX = formação_verbo_LEX_ter_finito()
	elif verbo_LEX == 'dizer':
		verbo_LEX = formação_verbo_LEX_dizer_finito()
	elif verbo_LEX == 'saber':
		verbo_LEX = formação_verbo_LEX_saber_finito()
	elif verbo_LEX == 'fazer':
		verbo_LEX = formação_verbo_LEX_fazer_finito()
	elif verbo_LEX == 'medir':
		verbo_LEX = formação_verbo_LEX_medir_finito()
	elif verbo_LEX == 'dever':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo_LEX_finito()
		verbo_LEX = ME + MI
	elif verbo_LEX == 'poder':
		verbo_LEX = formação_verbo_LEX_poder_finito()

	else:
		ME = (verbo_LEX[slice(-2)])
		MI = realizacao_transitoriedade_do_verbo_LEX_finito()
		verbo_LEX = ME + MI
	return verbo_LEX


def formação_da_estrutura_do_verbo_LEX_nao_finito():
	'''
    '''

	verbo_LEX = input("Qual é o verbo_LEX lematizado desejado?")

	if verbo_LEX == 'estar':
		verbo_LEX = formação_verbo_LEX_estar_não_finito()
	elif verbo_LEX == 'ser':
		verbo_LEX = formação_verbo_LEX_ser_não_finito()
	elif verbo_LEX == 'ir':
		verbo_LEX = formação_verbo_LEX_ir_não_finito()
	elif verbo_LEX == 'vir' or verbo_LEX == 'intervir':
		verbo_LEX = formação_verbo_LEX_vir_intervir_não_finito()
	elif verbo_LEX == 'haver':
		verbo_LEX = formação_verbo_LEX_haver_não_finito()
	elif verbo_LEX == 'ter':
		verbo_LEX = formação_verbo_LEX_ter_não_finito()
	elif verbo_LEX == 'dizer':
		verbo_LEX = formação_verbo_LEX_dizer_não_finito()
	elif verbo_LEX == 'saber':
		verbo_LEX = formação_verbo_LEX_saber_não_finito()
	elif verbo_LEX == 'fazer':
		verbo_LEX = formação_verbo_LEX_fazer_não_finito()
	elif verbo_LEX == 'medir':
		verbo_LEX = formação_verbo_LEX_medir_não_finito()
	elif verbo_LEX == 'dever':
		ME = verbo_LEX[slice(-2)]
		MI = realizacao_transitoriedade_do_verbo_LEX_não_finito()
		verbo_LEX = ME + MI
	elif verbo_LEX == 'poder':
		verbo_LEX = formação_verbo_LEX_poder_não_finito()
	else:
		ME = (verbo_LEX[slice(-2)])
		MI = realizacao_transitoriedade_do_verbo_LEX_não_finito()
		verbo_LEX = ME + MI
	return verbo_LEX



# def formação_verbo_gerúndio():
# 	prompt = "Qual é o verbo lematizado desejado?"
# 	verbo = input(prompt)
#
# 	ME = verbo[slice(-2)]
#
# 	MI = realizacao_transitoriedade_gerúndio()
# 	verbo_gerúndio = ME + MI
#
# 	return verbo_gerúndio
#
#
# def formação_da_estrutura_do_verbo_modal_não_finito():
# 	'''
#     '''
# 	print("Qual é o verbo modal lematizado desejado?")
#
# 	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
#
# 	if tipo_de_modal == 'dever':
# 		ME = tipo_de_modal[slice(-2)]
# 		MI = realizacao_transitoriedade_do_verbo_não_finito(
#
# 	elif tipo_de_modal == 'haver':
# 		verbo = formação_verbo_haver_não_finito()
#
# 	return verbo
#
#
# def formação_da_estrutura_do_verbo_modal_finito():
# 	'''
#     '''
# 	print("Qual é o verbo modal lematizado desejado?")
#
# 	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
#
# 	if tipo_de_modal == 'dever':
# 		ME = tipo_de_modal[slice(-2)]
# 		MI = realizacao_transitoriedade_do_verbo_finito()
# 		verbo = ME + MI
#
#
#
# 	elif tipo_de_modal == 'poder':
# 		verbo = formação_verbo_poder_finito()
#
#
# 	elif tipo_de_modal == 'haver':
# 		verbo = formação_verbo_haver_finito()
#
# 	return verbo
#
#
# def formação_da_estrutura_do_verbo_auxiliar_finito():
# 	'''
#     '''
#
# 	print("Qual é o verbo auxiliar lematizado desejado?")
# 	tipo_de_auxiliar = choice.Menu(['estar', 'ter', 'ir', 'vir', 'ser', 'haver']).ask()
#
# 	if tipo_de_auxiliar == 'estar':
# 		verbo = formação_verbo_estar_finito()
#
#
# 	elif tipo_de_auxiliar == 'ter':
# 		verbo = formação_verbo_ter_finito()
#
#
# 	elif tipo_de_auxiliar == 'haver':
# 		verbo = formação_verbo_haver_finito()
#
#
# 	elif tipo_de_auxiliar == 'ir':
# 		verbo = formação_verbo_ir_finito()
#
# 	elif tipo_de_auxiliar == 'vir':
# 		verbo = formação_verbo_vir_finito()
#
# 	elif tipo_de_auxiliar == 'ser':
# 		verbo = formação_verbo_ser_finito()
#
# 	return verbo
#
#
# def formação_da_estrutura_do_verbo_auxiliar_não_finito():
# 	'''
#     '''
#
# 	print("Qual é o verbo auxiliar lematizado desejado?")
# 	tipo_de_auxiliar = choice.Menu(['estar', 'ter', 'ir', 'vir', 'ser', 'haver']).ask()
#
# 	if tipo_de_auxiliar == 'estar':
# 		verbo = formação_verbo_estar_não_finito()
#
#
# 	elif tipo_de_auxiliar == 'ter':
# 		verbo = formação_verbo_ter_não_finito()
#
#
# 	elif tipo_de_auxiliar == 'haver':
# 		verbo = formação_verbo_haver_não_finito()
#
#
# 	elif tipo_de_auxiliar == 'ir':
# 		verbo = formação_verbo_ir_não_finito()
#
# 	elif tipo_de_auxiliar == 'vir':
# 		verbo = formação_verbo_vir_não_finito()
#
# 	elif tipo_de_auxiliar == 'ser':
# 		verbo = formação_verbo_ser_não_finito()
#
# 	return verbo
#
#
# def formação_verbo_não_orientado():
# 	'''
#     '''
# 	verbo = input('Qual é o verbo lematizado?')
# 	tipo_de_orientação = OI_nao_orientado()
# 	if verbo == 'vir':
# 		if tipo_de_orientação == 'gerúndio':
# 			ME = verbo[slice(-2)]
# 			MI = realizacao_transitoriedade_gerúndio()
# 			verbo = ME + MI
# 		elif tipo_de_orientação == 'particípio':
# 			ME = verbo[slice(-2)]
# 			MI = 'indo'
# 			verbo = ME + MI
# 		elif tipo_de_orientação == 'infinitivo':
# 			verbo = verbo
# 	elif verbo == 'dizer':
# 		if tipo_de_orientação == 'gerúndio':
# 			ME = verbo[slice(-2)]
# 			MI = realizacao_transitoriedade_gerúndio()
# 			verbo = ME + MI
# 		elif tipo_de_orientação == 'particípio':
# 			ME = verbo[slice(-4)]
# 			MI = 'ito'
# 			verbo = ME + MI
# 		elif tipo_de_orientação == 'infinitivo':
# 			verbo = verbo
# 	else:
# 		if tipo_de_orientação == 'gerúndio':
# 			ME = verbo[slice(-2)]
# 			MI = realizacao_transitoriedade_gerúndio()
# 			verbo = ME + MI
# 		elif tipo_de_orientação == 'particípio':
# 			ME = verbo[slice(-2)]
# 			MI = realizacao_transitoriedade_particípio()
# 			verbo = ME + MI
# 		elif tipo_de_orientação == 'infinitivo':
# 			verbo = verbo
# 	return verbo
#

############################################################################



###########################################################################
#########################################################################

def formacao_da_estrutura_do_verbo_LEX(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                                   genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''
    (str) -> str

    Retorna um verbo_LEX flexionado dados OE_experiencia_do_verbo_LEX,
    OI_orientacao_interpessoal_do_verbo_LEX.
    >>> formação_da_estrutura_do_verbo_LEX ()
    'levo'
    >>>formação_da_estrutura_do_verbo_LEX ()
    'levei'
    '''
	OE_experiencia_do_verbo_LEX = experiencia_do_verbo_LEX(verbo_LEX)
	OI_orientacao_interpessoal_do_verbo_LEX = realizacao_transitoriedade_do_verbo_LEX(tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
	                                                                          OI_numero_LEX,
	                                                                          genero_LEX, OI_tipo_de_pessoa_LEX,
	                                                                          padrao_pessoa_morfologia_LEX)
	verbo_LEX = OE_experiencia_do_verbo_LEX + OI_orientacao_interpessoal_do_verbo_LEX
	return verbo_LEX


# #
# formacao_da_estrutura_do_verbo_LEX('andar','presente','-AR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo_LEX('andar','pretérito_perfectivo_I','-AR','singular',None,'3pessoa')
# formacao_da_estrutura_do_verbo_LEX('comer','pretérito_imperfectivo','-ER','plural',None,'1pessoa')
# formacao_da_estrutura_do_verbo_LEX('expor','subjuntivo_condicional','-OR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo_LEX('expor','gerúndio','-OR',None,None,None)
# formacao_da_estrutura_do_verbo_LEX('cortar', 'particípio', '-AR', 'singular', 'feminino', None)
#
# TIPO_DE_EXPERIENCIA_LEX = ['Ser', 'Fazer', 'Sentir']
# funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
#                                       'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()


def verbo_LEX_geral(funcao_no_grupo_verbal_POS_FINAL, TIPO_DE_EXPERIENCIA_LEX, verbo_LEX,
                    tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                    padrao_pessoa_morfologia_LEX="Morfologia_padrão"):
	'''(str)->str
    Retorna a estrutura que realiza os verbo_LEXs no português.
    '''
	classe_do_verbo_LEX = def_classe_de_verbo(funcao_no_grupo_verbal_POS_FINAL)
	if classe_do_verbo_LEX == 'lexical':
		if TIPO_DE_EXPERIENCIA_LEX == 'Ser':

			if verbo_LEX == 'estar':
				verbo_LEX = formacao_verbo_LEX_estar(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX,
				                                     genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'dizer':
				verbo_LEX = formacao_verbo_LEX_dizer(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX,
				                                     genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'ter':
				verbo_LEX = formacao_verbo_LEX_ter(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                   OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                   padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'ser':
				verbo_LEX = formacao_verbo_LEX_ser(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                   OI_numero_LEX, genero_LEX,
				                                   OI_tipo_de_pessoa_LEX,
				                                   padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'ir':
				verbo_LEX = formacao_verbo_LEX_ir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                  OI_numero_LEX,
				                                  genero_LEX, OI_tipo_de_pessoa_LEX,
				                                  padrao_pessoa_morfologia_LEX='Morfologia_padrão')

			elif verbo_LEX == 'haver':
				verbo_LEX = formacao_verbo_LEX_haver(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')

			else:
				verbo_LEX = formacao_da_estrutura_do_verbo_LEX(verbo_LEX, tipo_de_orientacao_LEX,
				                                               padrao_de_morfologia_LEX, OI_numero_LEX,
				                                               genero_LEX, OI_tipo_de_pessoa_LEX,
				                                               padrao_pessoa_morfologia_LEX="Morfologia_padrão")

		elif TIPO_DE_EXPERIENCIA_LEX == 'Fazer':
			if verbo_LEX == 'fazer':
				verbo_LEX = formacao_verbo_LEX_fazer(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX,
				                                     genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'agredir':
				verbo_LEX = formacao_verbo_LEX_agredir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                       OI_numero_LEX,
				                                       genero_LEX, OI_tipo_de_pessoa_LEX,
				                                       padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'ir':
				verbo_LEX = formacao_verbo_LEX_ir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                  OI_numero_LEX,
				                                  genero_LEX, OI_tipo_de_pessoa_LEX,
				                                  padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'aferir':
				verbo_LEX = formacao_verbo_LEX_aferir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                      OI_numero_LEX,
				                                      genero_LEX, OI_tipo_de_pessoa_LEX,
				                                      padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'medir':
				verbo_LEX = formacao_verbo_LEX_medir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX,
				                                     genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')

			elif (verbo_LEX == 'intervir' or verbo_LEX == 'vir'):
				verbo_LEX = formacao_verbo_LEX_vir_intervir(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                            OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                            padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			else:
				verbo_LEX = formacao_da_estrutura_do_verbo_LEX(verbo_LEX, tipo_de_orientacao_LEX,
				                                               padrao_de_morfologia_LEX, OI_numero_LEX,
				                                               genero_LEX, OI_tipo_de_pessoa_LEX,
				                                               padrao_pessoa_morfologia_LEX="Morfologia_padrão")

		elif TIPO_DE_EXPERIENCIA_LEX == 'Sentir':
			if verbo_LEX == 'saber':
				verbo_LEX = formacao_verbo_LEX_saber(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX,
				                                     genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'poder':
				verbo_LEX = formacao_verbo_LEX_poder(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			elif verbo_LEX == 'dizer':
				verbo_LEX = formacao_verbo_LEX_dizer(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX,
				                                     genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')
			else:
				verbo_LEX = formacao_da_estrutura_do_verbo_LEX(verbo_LEX, tipo_de_orientacao_LEX,
				                                               padrao_de_morfologia_LEX, OI_numero_LEX,
				                                               genero_LEX, OI_tipo_de_pessoa_LEX,
				                                               padrao_pessoa_morfologia_LEX="Morfologia_padrão")

	elif classe_do_verbo_LEX == 'modal':
		if (TIPO_DE_EXPERIENCIA_LEX == 'Ser' or
				TIPO_DE_EXPERIENCIA_LEX == 'Fazer' or
				TIPO_DE_EXPERIENCIA_LEX == 'Sentir'):

			if verbo_LEX == 'dever':
				ME = verbo_LEX[slice(-2)]
				MI = realizacao_transitoriedade_do_verbo_LEX(tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                             OI_numero_LEX, genero_LEX,
				                                             OI_tipo_de_pessoa_LEX,
				                                             padrao_pessoa_morfologia_LEX="Morfologia_padrão")
				verbo_LEX = ME + MI

			elif verbo_LEX == 'poder':
				verbo_LEX = formacao_verbo_LEX_poder(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')

			elif verbo_LEX == 'haver':
				verbo_LEX = formacao_verbo_LEX_haver(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                     OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                     padrao_pessoa_morfologia_LEX='Morfologia_padrão')

			elif verbo_LEX == 'ter':

				verbo_LEX = formacao_verbo_LEX_ter(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
				                                   OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
				                                   padrao_pessoa_morfologia_LEX='Morfologia_padrão') + ' ' + 'que'
	# elif verbo_LEX == 'ter de':
	# 	verbo_LEX = formacao_verbo_LEX_ter(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
	# 	                           OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
	# 	                           padrao_pessoa_morfologia_LEX='Morfologia_padrão') + ' ' + 'de'


	return verbo_LEX


# verbo_LEX_geral('Evento','Fazer','cortar','presente','-AR','plural',None,'3pessoa')


def formacao_verbo_participio_LEX(verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX, OI_numero_LEX,
                         genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX='Morfologia_padrão'):

	ME = verbo_LEX[slice(-2)]

	MI = realizacao_transitoriedade_participio_LEX(padrao_de_morfologia_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX=None, padrao_pessoa_morfologia_LEX="Morfologia_padrão")
	verbo_participio = ME + MI

	return verbo_participio


# formacao_verbo_participio_LEX('cortar', 'particípio', '-AR', 'singular','masculino', None)
