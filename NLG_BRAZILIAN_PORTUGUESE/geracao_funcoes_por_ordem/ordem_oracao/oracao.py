
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_nominal import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.frase_preposicional import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_verbal import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_adverbial import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_conjuntivo import *


def circunstancia(realizacao_circunstancia=None,
                  indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
                  tipo_qualificador=None, indice_preposicao_qualif=None, determinacao_especificidade_beta=None,
                  orientacao_beta=None,
                  genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
                  determinacao_especificidade_alpha=None, orientacao_alpha=None, genero_alpha=None,
                  numero_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
                  numero_obj_possuido=None, genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
                  tipo_numerativo=None, cardinal=None, genero_numerativo=None, tipo_de_ente=None,
                  tipo_de_nao_consciente=None,
                  tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
                  classe_palavra_ente=None, substantivo_lematizado=None, numero=None,
                  tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_prop=None,
                  pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                  morfologia_do_pronome=None, reflexivo=None,
                  adjetivo_epiteto=None,
                  adjetivo_classificador=None, genero_adjetivo=None, numero_adjetivo=None,
                  contracao=None,
                  tipo_de_adverbio1=None, ind1=None,
                  tipo_de_adverbio2=None, ind2=None,
                  tipo_de_adverbio3=None, ind3=None,
                  tipo_de_adverbio4=None, ind4=None,
                  tipo_de_adverbio5=None, ind5=None
                  ):
    """
    Ex.:
    >>> circunstancia('grupo_adverbial', None,None,tem_qualificador=None,tipo_qualificador=None,
    ...indice_preposicao_qualif=None, determinacao_especificidade_beta=None, orientacao_beta=None,
    ...genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
    ...determinacao_especificidade_alpha='específico', orientacao_alpha='orientação_específica_proximidade',
    ...genero_alpha='masculino', numero_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
    ...pessoa_da_interlocucao_possuidor='1s', numero_obj_possuido='plural', genero_obj_possuido='masculino',
    ...pessoa_da_interlocucao_proximidade='próximo_ao_não_interlocutor',   tipo_numerativo=None, cardinal=None,
    ...genero_numerativo=None, tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
    ...tipo_de_nao_consciente_material='animal', tipo_de_nao_consciente_semiotico=None,
    ...classe_palavra_ente='substantivo_comum', substantivo_lematizado='prédio', numero='plural',
    ...tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_prop=None, pessoa_da_interlocucao=None,
    ...transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
    ...adjetivo_epiteto='alto', adjetivo_classificador=None,genero_adjetivo='masculino' ,
    ...numero_adjetivo='plural',contracao='-contração' ,tipo_de_adverbio1='Modo', ind1=10) -> 'cuidadosamente'

    :param realizacao_circunstancia:
    :param indice_preposicao_frase:
    :param dissoc_ente_nucleo:
    :param tem_qualificador:
    :param tipo_qualificador:
    :param indice_preposicao_qualif:
    :param determinacao_especificidade_beta:
    :param orientacao_beta:
    :param genero_beta:
    :param numero_beta:
    :param morfologia_do_pronome_beta:
    :param determinacao_especificidade_alpha:
    :param orientacao_alpha:
    :param genero_alpha:
    :param numero_alpha:
    :param morfologia_do_pronome_alpha:
    :param pessoa_da_interlocucao_possuidor:
    :param numero_obj_possuido:
    :param genero_obj_possuido:
    :param pessoa_da_interlocucao_proximidade:
    :param tipo_numerativo:
    :param cardinal:
    :param genero_numerativo:
    :param tipo_de_ente:
    :param tipo_de_nao_consciente:
    :param tipo_de_nao_consciente_material:
    :param tipo_de_nao_consciente_semiotico:
    :param classe_palavra_ente:
    :param substantivo_lematizado:
    :param numero:
    :param tipo_feminino_ao:
    :param tipo_masc_ao:
    :param acent_tonica:
    :param nome_prop:
    :param pessoa_da_interlocucao:
    :param transitividade_verbo:
    :param tonicidade:
    :param morfologia_do_pronome:
    :param reflexivo:
    :param adjetivo_epiteto:
    :param adjetivo_classificador:
    :param genero_adjetivo:
    :param numero_adjetivo:
    :param contracao:
    :param tipo_de_adverbio1:
    :param ind1:
    :param tipo_de_adverbio2:
    :param ind2:
    :param tipo_de_adverbio3:
    :param ind3:
    :param tipo_de_adverbio4:
    :param ind4:
    :param tipo_de_adverbio5:
    :param ind5:
    :return:
    """
    circ = ''

    try:
        if realizacao_circunstancia == 'grupo_nominal':
            circ = estrutura_gn(dissoc_ente_nucleo, tem_qualificador, tipo_qualificador, indice_preposicao_qualif,
                                determinacao_especificidade_beta, orientacao_beta, genero_beta, numero_beta,
                                morfologia_do_pronome_beta, determinacao_especificidade_alpha, orientacao_alpha,
                                genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                                pessoa_da_interlocucao_possuidor, numero_obj_possuido, genero_obj_possuido,
                                pessoa_da_interlocucao_proximidade, tipo_numerativo, cardinal, genero_numerativo,
                                tipo_de_ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado, numero,
                                tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_prop, pessoa_da_interlocucao,
                                transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo, adjetivo_epiteto,
                                adjetivo_classificador, genero_adjetivo, numero_adjetivo, contracao)
        elif realizacao_circunstancia == 'frase_preposicional':
            circ = frase_preposicional(indice_preposicao_frase, dissoc_ente_nucleo, tem_qualificador, tipo_qualificador,
                                       indice_preposicao_qualif, determinacao_especificidade_beta, orientacao_beta,
                                       genero_beta, numero_beta, morfologia_do_pronome_beta,
                                       determinacao_especificidade_alpha, orientacao_alpha, genero_alpha, numero_alpha,
                                       morfologia_do_pronome_alpha, pessoa_da_interlocucao_possuidor,
                                       numero_obj_possuido, genero_obj_possuido, pessoa_da_interlocucao_proximidade,
                                       tipo_numerativo, cardinal, genero_numerativo, tipo_de_ente,
                                       tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                       tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado,
                                       numero, tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_prop,
                                       pessoa_da_interlocucao, transitividade_verbo, tonicidade, morfologia_do_pronome,
                                       reflexivo, adjetivo_epiteto, adjetivo_classificador, genero_adjetivo,
                                       numero_adjetivo, contracao)
        elif realizacao_circunstancia == 'grupo_adverbial':
            circ = grupo_adverbial(tipo_de_adverbio1, ind1, tipo_de_adverbio2, ind2, tipo_de_adverbio3, ind3,
                                   tipo_de_adverbio4, ind4, tipo_de_adverbio5, ind5)
        return re.sub(' +', ' ', circ).strip()
    except ValueError:
        return ''


#
# circunstancia('grupo_adverbial', None,None,tem_qualificador=None,tipo_qualificador=None,indice_preposicao_qualif=None,
#               determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None, numero_beta=None,
#               morfologia_do_pronome_beta=None, determinacao_especificidade_alpha='específico',
#               orientacao_alpha='orientação_específica_proximidade', genero_alpha='masculino',
#               numero_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
#               pessoa_da_interlocucao_possuidor='1s', numero_obj_possuido='plural', genero_obj_possuido='masculino',
#               pessoa_da_interlocucao_proximidade='próximo_ao_não_interlocutor',   tipo_numerativo=None, cardinal=None,
#               genero_numerativo=None, tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
#               tipo_de_nao_consciente_material='animal', tipo_de_nao_consciente_semiotico=None,
#               classe_palavra_ente='substantivo_comum', substantivo_lematizado='prédio', numero='plural',
#               tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_prop=None,
#               pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#               morfologia_do_pronome=None, reflexivo=None,  adjetivo_epiteto='alto', adjetivo_classificador=None,
#               genero_adjetivo='masculino' , numero_adjetivo='plural',contracao='-contração' ,tipo_de_adverbio1='Modo',
#               ind1=10)


# for i ordem_lugar_preciso in range (12):
# 	# print(circunstancia(realizacao_circunstancia='frase_preposicional',indice_preposicao_frase=6, dissoc_ente_nucleo=None, tem_qualificador=None,
# 	# 							tipo_qualificador=None,indice_preposicao_qualif=None, determinacao_especificidade_beta=None, orientacao_beta=None,
# 	# 							genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
# 	# 							determinacao_especificidade_alpha='específico', orientacao_alpha='NA',
# 	# 							genero_alpha='feminino', numero_alpha='singular', morfologia_do_pronome_alpha=None,
# 	# 							pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
# 	# 							genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
# 	# 							funcao_numerativo='ordem_lugar_preciso(ordinal)', cardinal=2, genero='feminino', tipo_precisa=None,
# 	# 							tipo_real_card=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None,
# 	# 							unidadeExtenso=None, numIndefinido=None, tipo_de_ente='não_consciente',
# 	# 							tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='abstração_material',
# 	# 							tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
# 	# 							substantivo_lematizado='guerra', numero='singular', tipo_feminino_ao=None,
# 	# 							tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
# 	# 							transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
# 	# 							adjetivo_epiteto=None, adjetivo_classificador=None, genero_adjetivo='feminino',
# 	# 							numero_adjetivo='singular', contracao=None ))
#
# 'ordem_lugar_preciso(ordinal)','2','feminino',None,None,
# 			   None,None,None,None,None


# # ##SISTEMAS DA ORAÇÃO
# #
## no caso de materiais meteorológicas, o Meio conflui
# com o Processo (por isso :AG_processo_sem_alcance,AG_processo_com_alcance );
# pode haver escopo (Ex.: choveu uma chuva grossa)
def agenciamento(indice=None):
    """

    Ex.:

    >>> agenciamento(0) -> 'AG_médio_sem_alcance'

    :param indice:
    [0:'AG_médio_sem_alcance',1:'AG_médio_com_alcance',
    2:'AG_efetivo_operativo',3:'AG_efetivo_receptivo',
    4:'AG_efetivo_receptivo_não_agentivo',5:'AG_processo_sem_alcance',
    6:'AG_processo_com_alcance']
    :return: agenciamento
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
        agn = tipos[indice]
    except (KeyError, ValueError, TypeError):
        agn = None
    return agn


# #
# # ###tipos de processo oração
# # # Material
# # ##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)

def processo_material(indice=None):
    """

    Exs.:

    >>> for j in range(4):
    ...print(processo_material(j))
    ..."PR_material_transformativo_IMPA_transitivo"
    ..."PR_material_criativo_IMPA_transitivo"
    ..."PR_material_transformativo_IMPA_intransitivo"
    ..."PR_material_criativo_IMPA_intransitivo"

    :param indice:
        [0:'PR_material_transformativo_IMPA_transitivo',
        1:'PR_material_criativo_IMPA_transitivo',
        2:'PR_material_transformativo_IMPA_intransitivo',
        3:'PR_material_criativo_IMPA_intransitivo']
    :return: tipos de processo material
    """
    try:
        opcoes = ['PR_material_transformativo_IMPA_transitivo',
                  'PR_material_criativo_IMPA_transitivo',
                  'PR_material_transformativo_IMPA_intransitivo',
                  'PR_material_criativo_IMPA_intransitivo']
        nums = [x for x in range(len(opcoes))]
        tipos = dict(zip(nums, opcoes))
        tipo_material = tipos[indice]

    except (KeyError, ValueError, TypeError):
        tipo_material = None
    return tipo_material


def processo_relacional(indice_rel=None):
    """
    Exs.:

    >>> processo_relacional(0) -> "PR_relacional_intensivo_atributivo"

    :param indice_rel:
    ['PR_relacional_intensivo_atributivo',
   'PR_relacional_intensivo_identificativo',
   'PR_relacional_possessivo_atributivo',
   'PR_relacional_possessivo_identificativo',
   'PR_relacional_circunstancial_atributivo',
   'PR_relacional_circunstancial_identificativo]

    :return:
    """
    try:
        opcoes_relacional = ['PR_relacional_intensivo_atributivo',
                             'PR_relacional_intensivo_identificativo',
                             'PR_relacional_possessivo_atributivo',
                             'PR_relacional_possessivo_identificativo',
                             'PR_relacional_circunstancial_atributivo',
                             'PR_relacional_circunstancial_identificativo']
        nums_rel = [x for x in range(len(opcoes_relacional))]
        tipos_rel = dict(zip(nums_rel, opcoes_relacional))
        tipo_relacional = tipos_rel[indice_rel]

        return tipo_relacional
    except (ValueError, TypeError, KeyError):
        return None


def atribuicao_relacao(indice_atrib=None):
    """
    Exe.:

    >>> atribuicao_relacao(0) -> 'atribuição_proj_ment_cognitiva'

    :param indice_atrib:
    'atribuição_proj_ment_cognitiva',
    'atribuição_proj_ment_desiderativa',
    'atribuição_proj_verbal',
    'atribuição_expan_elaboração',
    'atribuição_expan_intencificação',
    'sem_atribuição_de_relação'
    :return:
    """
    opcoes_atribuicao = ['atribuição_proj_ment_cognitiva',
                         'atribuição_proj_ment_desiderativa',
                         'atribuição_proj_verbal',
                         'atribuição_expan_elaboração',
                         'atribuição_expan_intencificação',
                         'sem_atribuição_de_relação']
    nums_atribuicao = [x for x in range(len(opcoes_atribuicao))]
    tipos_atrobuicao = dict(zip(nums_atribuicao, opcoes_atribuicao))
    try:
        tipo_atrib = tipos_atrobuicao[indice_atrib]

        return tipo_atrib
    except (ValueError, TypeError, KeyError):
        return ''


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

def sujeitabilidade(indice_respo=None, indice_press=None):
    """
    Ex.:

    >>> sujeitabilidade(0,0) -> 'SUJ_responsável_recuperado_explícito'

    :param indice_respo:'SUJ_responsável',1:'SUJ_distante_impessoal',
                            2:'SUJ_distante_não_responsável', 3:'SUJ_-sujeitabilidade'
    :param indice_press:'recuperado_explícito', 1:'recuperado_implícito',
                                    2:'não_recuperável', 3:'recuperação_NA'
    :return: tipo de sujeitabilidade
    """
    try:
        opcoes_respo = ['SUJ_responsável', 'SUJ_distante_impessoal',
                        'SUJ_distante_não_responsável', 'SUJ_-sujeitabilidade']
        nums_respo = [x for x in range(len(opcoes_respo))]
        tipos_respon = dict(zip(nums_respo, opcoes_respo))
        tipo_respon = tipos_respon[indice_respo]

        opcoes_press = ['recuperado_explícito', 'recuperado_implícito',
                        'não_recuperável', 'recuperação_NA']
        nums_press = [x for x in range(len(opcoes_press))]
        tipos_press = dict(zip(nums_press, opcoes_press))
        tipo_press = tipos_press[indice_press]
        tipo_sujeitabilidade = tipo_respon + '_' + tipo_press

        return tipo_sujeitabilidade
    except (ValueError, KeyError, TypeError):
        return 'SUJ_responsável_recuperado_explícito'


def tipo_de_modo(indice_modo):
    """
    Retorna tipo de modo.

    Ex.:

    >>> tipo_de_modo(0) -> 'MOD_declarativo_+perguntafinito'

    :param indice_modo: 'MOD_declarativo_+perguntafinito', 'MOD_declarativo_-perguntafinito',
                       'MOD_interrogativo_elemental','MOD_interrogativo_polar',
                       'MOD_imperativo'
    :return: tipo de modo
    """
    try:
        opcoes = ['MOD_declarativo_+perguntafinito', 'MOD_declarativo_-perguntafinito',
                  'MOD_interrogativo_elemental', 'MOD_interrogativo_polar',
                  'MOD_imperativo']

        nums = [x for x in range(len(opcoes))]
        tipos_modo = dict(zip(nums, opcoes))
        tipo_modo = tipos_modo[indice_modo]
    except (ValueError, KeyError, TypeError):
        tipo_modo = 'MOD_declarativo_-perguntafinito'
    return tipo_modo


def avaliacao_modal(avaliacao: bool = False, polar: str = None) -> str:
    """

    :param polar= positiva', 'negativa'
    ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada.
        # Por enquanto vou modelar apenas a realizacao/ou não do adjunto-polaridade 'não'.
    :param avaliacao= '+', '-'
    :return: AVALIACAO_MODAL
    """
    aval_modal = ''
    try:
        if avaliacao is False:
            aval_modal = ''
        else:
            if polar == 'positiva':
                aval_modal = ''

            elif polar == 'negativa':
                aval_modal = 'não'

        return aval_modal
    except (ValueError, TypeError, KeyError):
        return ''


###

def polaridade(tipo_polaridade=None):
    """

    :param tipo_polaridade= 'positiva', 'negativa'
    :return: Adjunto_polaridade
    """
    adjunto_polaridade = ''
    try:
        if tipo_polaridade == 'positiva':
            adjunto_polaridade = ''

        elif tipo_polaridade == 'negativa':
            adjunto_polaridade = 'não'

        return adjunto_polaridade
    except (ValueError, KeyError, TypeError, UnboundLocalError):
        return ''


# POLARIDADE('positiva')
# POLARIDADE('negativa')

# #
# # ##############
# #
# # ## Preciso resolver como vou abordar a questão deste sistema: por enquanto vou mexer apenas com
# # # polaridade, e ir incrementando as combinações.

def tipo_avaliacao_modal(avaliacao=False, polar=None):
    """
    Retorna tipo de avaliação modal:

    Ex.:

    >>> tipo_avaliacao_modal(True, 'positiva') -> 'AvM_polaridade_positiva'
    :param avaliacao= "+". "-"
    :param polar= "positiva", "negativa"
    :return: tipo_de_avaliacao_modal
    """
    tipo_de_avaliacao_modal = ''
    try:
        if avaliacao is False:
            tipo_de_avaliacao_modal = 'AvM_sem_avaliação_modal'

        else:
            if polar == 'positiva':
                tipo_de_avaliacao_modal = 'AvM_polaridade_positiva'

            elif polar == 'negativa':
                tipo_de_avaliacao_modal = 'AvM_polaridade_negativa'

        return tipo_de_avaliacao_modal
    except (ValueError, KeyError, TypeError):
        return 'AvM_sem_avaliação_modal'


##para o sistema de modo, AINDA não considerei o subsistema de VALIDAÇÃO. (será implementado)

def modo(responsabilidade=None, pressuposicao_do_sujeito=None, tipo_modo=None):
    """
    Retorna o Modo. Ex.:

    >>> modo(0,0,1) -> 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito'
    >>> modo(3,3,1) -> 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito'

    :param responsabilidade:[0:'SUJ_responsável',1:'SUJ_distante_impessoal',
                            2:'SUJ_distante_não_responsável', 3:'SUJ_-sujeitabilidade']
    :param pressuposicao_do_sujeito: [0:'recuperado_explícito', 1:'recuperado_implícito',
                                    2:'não_recuperável', 3:'recuperação_NA']
    :param tipo_modo: 0:['MOD_declarativo_+perguntafinito', 1:'MOD_declarativo_-perguntafinito',
                       2:'MOD_interrogativo_elemental',3:'MOD_interrogativo_polar',
                       4:'MOD_imperativo']
    :return: Modo
    """

    return sujeitabilidade(responsabilidade, pressuposicao_do_sujeito) + '_' + tipo_de_modo(tipo_modo)


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


def conjuncao_continuativa(indice=None):
    """
    Retorna conjunção continuativa dado um índice.
    >>> conjuncao_continuativa(indice=23) -> 'olha'
    >>> conjuncao_continuativa(indice=8) -> 'então'

    :param indice: [0:"e",1:"é",2:"ah",3:'mas',4:'sim',5:'bem',6:'não',7:'agora',8:'então',9:'pois é',10:'assim'
                 ,11:'ó',12:'daí',13:'aí' ,14:'aí então',15:'quer dizer',16:'assim',17:'em seguida',18:'por fim'
                  ,19:'porque',20:'porém',21:'também',22:'é que',23:'olha']

    :return: conjunção continuativa
    """
    try:

        opcoes = ["e", "é", "ah", 'mas', 'sim', 'bem', 'não', 'agora', 'então', 'pois é', 'assim'
            , 'ó', 'daí', 'aí', 'aí então', 'quer dizer', 'assim', 'em seguida', 'por fim'
            , 'porque', 'porém', 'também', 'é que', 'olha']

        nums = [x for x in range(len(opcoes))]
        conjuncoes = dict(zip(nums, opcoes))
        conjuncao = conjuncoes[indice]

        return conjuncao
    except:
        return ''


#
# conjuncao_continuativa()
# print('Qual a tipo_pessoa de relativo?')
# tipo_de_relativo = choice.Menu(['nominal', 'adverbial']).ask()
# if tipo_de_relativo == 'nominal':
# 	TEMA_RELATIVO = pronome_relativo()
# elif tipo_de_relativo == 'adverbial':
# 	TEMA_RELATIVO = choice.Menu(['de onde', 'quando',
# 								 'onde', 'de quando', 'que', 'por onde']).ask()
#

def elemento_qu(indice=None):
    """
    Retorna elementos QU.

    Ex.:
    >>> elemento_qu(0) -> 'o que'

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
        elem_qu = elementos[indice]
        return elem_qu
    except:
        return ''


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
        return particula_modal
    except:
        return ''


def tema_textual(tem_tema_textual=False, indice_cont=None,
                 tipo_de_conjuncao=None,
                 indice_conj=None, tipo_de_relativo=None,
                 tipo_pronome_relativo=None, genero=None, numero=None,
                 indice_relativo=None, indice_relativo_adv=None):
    """
    Retorna tema textual dados os parametros. Ex:

    >>> tema_textual(True,None,'paratática_adversativa',3) -> 'não obstante'

    :param tem_tema_textual: [True, False]
   
    :param indice_cont: [0:"e",1:"é",2:"ah",3:'mas',4:'sim',5:'bem',6:'não',7:'agora',8:'então',9:'pois é',10:'assim'
                 ,11:'ó',12:'daí',13:'aí' ,14:'aí então',15:'quer dizer',16:'assim',17:'em seguida',18:'por fim'
                  ,19:'porque',20:'porém',21:'também',22:'é que',23:'olha']
    
    :param tipo_de_conjuncao: paratática_aditiva': {0: 'e', 1: 'mas ainda', 2: 'mas também', 3: 'nem'},
    'paratática_adversativa':{0: 'contudo', 1: 'entretanto', 2: 'mas', 3: 'não obstante',4: 'no entanto',
    5: 'porém', 6: 'todavia'},
    'paratática_alternativa': {0: 'já', 1: 'ou', 2: 'ora', 3: 'quer'},
    'paratática_conclusiva':{0: 'assim', 1: 'então', 2: 'logo', 3: 'por conseguinte', 4: 'por isso', 5: 'portanto'},
    'paratática_explicativa':{0: 'pois', 1: 'porquanto', 2: 'porque', 3: 'que'},
    'hipotática_causal':{0: 'porque', 1: 'pois', 2: 'porquanto', 3: 'como', 4: 'pois que', 5: 'por isso que',
    6: 'á que', 7: 'uma vez que', 8: 'visto que', 9: 'visto como', 10: 'que'},
    'hipotática_concessiva':{0: 'embora', 1: 'conquanto', 2: 'ainda que', 3: 'mesmo que', 4: 'posto que',
    5: 'bem que', 6: 'se bem que', 7: 'apesar de que', 8: 'nem que', 9: 'que'},
    'hipotática_condicional':{0: 'se', 1: 'caso', 2: 'quando', 3: 'conquanto que',  4: 'salvo se', 5: 'sem que',
    6: 'dado que', 7: 'desde que',8: 'a menos que', 9: 'a não ser que'},
    'hipotática_conformativa':{0: 'conforme', 1: 'como', 2: 'segundo', 3: 'consoante'},
    'hipotátiva_final':{0: 'para que', 1: 'a fim de que', 2: 'porque', 3: 'que'},
    'hipotática_proporcional':{0: 'à medida que', 1: 'ao passo que', 2: 'à proporção que', 3: 'enquanto',
    4: 'quanto mais', 5: 'quanto menos'},
    'hipotática_temporal':{0: 'quando', 1: 'antes que', 2: 'depois que', 3: 'até que', 4: 'logo que',
    5: 'sempre que', 6: 'assim que', 7: 'desde que', 8: 'todas as vezes que', 9: 'cada vez que', 10: 'apenas',
    11: 'mal', 12: 'desde que'},
    'hipotática_comparativa':{0: 'mais que', 1: 'mais do que', 2: 'menos que', 3: 'maior que', 4: 'menor que',
    5: 'melhor que', 6: 'pior que', 7: 'menos do que', 8: 'maior do que', 9: 'menor do que',
    10: 'melhor do que', 11: 'pior do que'},
    'hipotática_consecutiva':{0: 'De modo que', 1: 'De maneira que'},
    'hipotática_integrante':{0: 'que', 1: 'se'},
    'hipotática_relativa':{0: 'porque', 1: 'pois', 2: 'porquanto', 3: 'como', 4: 'pois que', 5: 'por isso que',
    6: 'á que', 7: 'uma vez que', 8: 'visto que', 9: 'visto como', 10: 'que'}
    :param indice_conj:
    :param tipo_de_relativo:
    :param tipo_pronome_relativo:
    :param genero:
    :param numero:
    :param indice_relativo:
    :param indice_relativo_adv:
    :return:
    """

    tema_continuativo, tema_conjuntivo, tema_relativo = '', '', ''

    try:
        if tem_tema_textual is True:
            tema_continuativo = conjuncao_continuativa(indice_cont)
            tema_conjuntivo = grupo_conjuntivo(tipo_de_conjuncao, indice_conj)

            if tipo_de_relativo == 'nominal':
                tema_relativo = pronome_relativo(tipo_pronome_relativo, genero,
                                                 numero, indice_relativo)
            elif tipo_de_relativo == 'adverbial':
                opcoes = ['de onde', 'quando',
                          'onde', 'de quando', 'que', 'por onde', 'qual']

                nums = [x for x in range(len(opcoes))]
                relativos = dict(zip(nums, opcoes))
                tema_relativo = relativos[indice_relativo_adv]
            else:
                tema_relativo = ''
        tema_text = tema_continuativo + ' ' + tema_conjuntivo + ' ' + tema_relativo
    except:
        tema_text = ''
    return re.sub(' +', ' ', tema_text).strip()


###tema interpessoal
# TIPO_TEMA_INTERPESSOAL = choice.Menu().ask()
# tipo_realizacao = choice.Menu(['grupo_adverbial', 'frase_preposicional']).ask()


def tema_interpessoal(tipo_tema_interpessoal=None, tipo_realizacao=None,

                      tipo_de_adverbio1=None, ind1=None,
                      tipo_de_adverbio2=None, ind2=None,
                      tipo_de_adverbio3=None, ind3=None,
                      tipo_de_adverbio4=None, ind4=None,
                      tipo_de_adverbio5=None, ind5=None,

                      # frase prepos
                      indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
                      tipo_qualificador=None, indice_preposicao_qualif=None,
                      determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None, numero_beta=None,
                      morfologia_do_pronome_beta=None, determinacao_especificidade_alpha=None, orientacao_alpha=None,
                      genero_alpha=None, numero_alpha=None, morfologia_do_pronome_alpha=None,
                      pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None, genero_obj_possuido=None,
                      pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None, cardinal=None,
                      genero_numerativo=None,
                      tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                      tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
                      numero_subs=None, genero_subs=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
                      nome_prop_fp=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                      morfologia_do_pronome=None, reflexivo=None, adjetivo_epiteto=None,
                      adjetivo_classificador=None, genero_adjetivo=None, numero_adjetivo=None, contracao=None,
                      #

                      indice_elem_qu=None, indice_part_modal=None,
                      nome_prop=None
                      ):
    """
    Retorna o Tema interpessoal.
    
    Ex.:
    
    >>> tema_interpessoal("TI_avaliação_comentário", 'grupo_adverbial','Modo', 18) -> 'infelizmente'
    >>> tema_interpessoal('TI_avaliação_comentário','grupo_adverbial','Modo',12) -> 'tristemente'
    
    :param tipo_tema_interpessoal: ['TI_avaliação_modo', 'TI_avaliação_comentário',
                                'TI_encenação_troca', 'TI_encenação_papel_falante', 'TI_polaridade',
                                'TI_encenação_papel_ouvinte','TI_NA']
    :param tipo_realizacao: ['grupo_adverbial','frase_preposicional]
    :param tipo_de_adverbio1: 
    :param ind1: 
    :param tipo_de_adverbio2: 
    :param ind2: 
    :param tipo_de_adverbio3: 
    :param ind3: 
    :param tipo_de_adverbio4: 
    :param ind4: 
    :param tipo_de_adverbio5: 
    :param ind5: 
    :param indice_preposicao_frase: 
    :param dissoc_ente_nucleo: 
    :param tem_qualificador: 
    :param tipo_qualificador: 
    :param indice_preposicao_qualif: 
    :param determinacao_especificidade_beta: 
    :param orientacao_beta: 
    :param genero_beta: 
    :param numero_beta: 
    :param morfologia_do_pronome_beta: 
    :param determinacao_especificidade_alpha: 
    :param orientacao_alpha: 
    :param genero_alpha: 
    :param numero_alpha: 
    :param morfologia_do_pronome_alpha: 
    :param pessoa_da_interlocucao_possuidor: 
    :param numero_obj_possuido: 
    :param genero_obj_possuido: 
    :param pessoa_da_interlocucao_proximidade: 
    :param tipo_numerativo: 
    :param cardinal: 
    :param genero_numerativo: 
    :param tipo_de_ente: 
    :param tipo_de_nao_consciente: 
    :param tipo_de_nao_consciente_material: 
    :param tipo_de_nao_consciente_semiotico: 
    :param classe_palavra_ente: 
    :param substantivo_lematizado: 
    :param numero_subs: 
    :param genero_subs: 
    :param tipo_feminino_ao: 
    :param tipo_masc_ao: 
    :param acent_tonica: 
    :param nome_prop_fp: 
    :param pessoa_da_interlocucao: 
    :param transitividade_verbo: 
    :param tonicidade: 
    :param morfologia_do_pronome: 
    :param reflexivo: 
    :param adjetivo_epiteto: 
    :param adjetivo_classificador: 
    :param genero_adjetivo: 
    :param numero_adjetivo: 
    :param contracao: 
    :param indice_elem_qu: 
    :param indice_part_modal: 
    :param nome_prop: 
    :return: 
    """
    tema_int = ''
    try:

        if tipo_tema_interpessoal == 'TI_avaliação_modo' or tipo_tema_interpessoal == 'TI_avaliação_comentário':
            if tipo_realizacao == 'grupo_adverbial':
                tema_int = grupo_adverbial(tipo_de_adverbio1, ind1,
                                           tipo_de_adverbio2, ind2,
                                           tipo_de_adverbio3, ind3,
                                           tipo_de_adverbio4, ind4,
                                           tipo_de_adverbio5, ind5, )
            elif tipo_realizacao == 'frase_preposicional':
                tema_int = frase_preposicional(indice_preposicao_frase, dissoc_ente_nucleo,
                                               tem_qualificador,
                                               tipo_qualificador, indice_preposicao_qualif,
                                               determinacao_especificidade_beta, orientacao_beta,
                                               genero_beta, numero_beta,
                                               morfologia_do_pronome_beta, determinacao_especificidade_alpha,
                                               orientacao_alpha,
                                               genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                                               pessoa_da_interlocucao_possuidor, numero_obj_possuido,
                                               genero_obj_possuido,
                                               pessoa_da_interlocucao_proximidade, tipo_numerativo,
                                               cardinal,
                                               genero_numerativo,
                                               tipo_de_ente, tipo_de_nao_consciente,
                                               tipo_de_nao_consciente_material,
                                               tipo_de_nao_consciente_semiotico, classe_palavra_ente,
                                               substantivo_lematizado,
                                               numero_subs, genero_subs, tipo_feminino_ao,
                                               tipo_masc_ao, acent_tonica,
                                               nome_prop_fp, pessoa_da_interlocucao,
                                               transitividade_verbo, tonicidade,
                                               morfologia_do_pronome, reflexivo, adjetivo_epiteto,
                                               adjetivo_classificador, genero_adjetivo, numero_adjetivo,
                                               contracao)

        elif tipo_tema_interpessoal == 'TI_encenação_troca':
            tema_int = elemento_qu(indice_elem_qu)

        elif tipo_tema_interpessoal == 'TI_encenação_papel_falante':
            tema_int = particula_modal(indice_part_modal)
        elif tipo_tema_interpessoal == 'TI_encenação_papel_ouvinte':
            tema_int = nome_proprio(nome_prop)
    except:
        tema_int = ''

    return tema_int
#

# #


####TEMA IDEACIONAL

# TEMA_ÂNGULO = choice.Menu().ask()
# TEMA_ELEMENTAL = choice.Menu().ask()
# TEMA_PROEMINENTE = choice.Menu().ask()


def tema_ideacional(orientacao_modal=None, orientacao_transitiva=None,
                    selecao_tematica=None, tema_default=None,
                    tema_default_indicativo=None, tema_identificativo=None,
                    tema_angulo=None, tema_elemental=None,
                    tema_proeminente=None):
    """
    Ex.:

    >>> tema_ideacional(orientacao_modal='orientado', orientacao_transitiva='direcional',
    ...selecao_tematica='default', tema_default='indicativo',
    ...tema_default_indicativo='declarativo', tema_identificativo='NA',
    ...tema_angulo=None, tema_elemental=None,
    ...tema_proeminente=None) -> 'TID_default_indicativo_declarativo_TIdentif_NA'

    >>> tema_ideacional('não_orientado','não_direcional','proeminente', None,None, 'NA',
    ...None,None, 'intensivo_relativo_papel_transitivo_nuclear_participante')
    -> 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante'

    :param orientacao_modal:['orientado', 'não_orientado']
    :param orientacao_transitiva:['direcional', 'não_direcional']
    :param selecao_tematica:['default', 'proeminente']
    :param tema_default:['imperativo','indicativo']
    :param tema_default_indicativo:['declarativo','interrogativo_polar','interrogativo_sujeito_elemental']
    :param tema_identificativo:['NA','equativo_codificação','equativo_decodificação']
    :param tema_angulo:['TID_fonte', 'TID_ponto_de_vista']
    :param tema_elemental:['TID_complemento_elemental', 'TID_adjunto_elemental']
    :param tema_proeminente:['perspectiva_intensificação','perspectiva_outro',
# 		                                'intensivo_absoluto',
# 		                                'intensivo_relativo_papel_transitivo_nuclear_participante',
# 		                                'intensivo_relativo_papel_transitivo_nuclear_processo',
# 		                                'intensivo_relativo_papel_transitivo_circunstancial_expansão_elaboração',
# 		                                'intensivo_relativo_papel_transitivo_circunstancial_expansão_extensão',
# 		                                'intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto',
# 		                                'intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_reprisado',
# 		                                'intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_recuperável',
# 		                                'intensivo_relativo_predicação_default_local',
# 		                                'intensivo_relativo_predicação_proeminente_local']
    :return: tipo de tema ideacional
    """
    tema_id = ''
    if orientacao_modal == 'orientado' and orientacao_transitiva == 'direcional' and selecao_tematica == 'default':

        if tema_default == 'imperativo':
            tema_id = 'TID_default_imperativo'

        elif tema_default == 'indicativo':

            if tema_default_indicativo == 'declarativo' and tema_identificativo == 'NA':

                tema_id = 'TID_default_indicativo_declarativo_TIdentif_NA'

            elif tema_default_indicativo == 'interrogativo_polar' and tema_identificativo == 'NA':

                tema_id = 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'

            elif tema_default_indicativo == 'interrogativo_sujeito_elemental' and tema_identificativo == 'NA':

                tema_id = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_NA'

            elif tema_default_indicativo == 'declarativo' and tema_identificativo == 'equativo_decodificação':
                tema_id = 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação'

            elif tema_default_indicativo == 'interrogativo_polar' and tema_identificativo == 'equativo_decodificação':

                tema_id = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação'

            elif tema_default_indicativo == 'interrogativo_sujeito_elemental' and tema_identificativo == 'equativo_decodificação':

                tema_id = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_decodificação'

            elif tema_default_indicativo == 'declarativo' and tema_identificativo == 'equativo_codificação':

                tema_id = 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação'

            elif tema_default_indicativo == 'interrogativo_polar' and tema_identificativo == 'equativo_codificação':

                tema_id = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação'

            elif tema_default_indicativo == 'interrogativo_sujeito_elemental' and tema_identificativo == 'equativo_codificação':

                tema_id = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_codificação'

    elif orientacao_modal == 'não_orientado' and orientacao_transitiva == 'direcional' and selecao_tematica == 'proeminente':
        if tema_angulo == 'fonte':
            tema_id = 'TID_angulo_fonte'
        elif tema_angulo == 'ponto_de_vista':
            tema_id = 'TID_angulo_ponto_de_vista'
    elif orientacao_modal == 'orientado' and orientacao_transitiva == 'não_direcional' and selecao_tematica == 'default':
        if tema_elemental == 'complemento_elemental':
            tema_id = 'TID_complemento_elemental'
        elif tema_elemental == 'adjunto_elemental':
            tema_id = 'TID_adjunto_elemental'
    elif orientacao_modal == 'não_orientado' and orientacao_transitiva == 'não_direcional' and selecao_tematica == 'proeminente':

        tema_id = 'TID_proeminente_' + tema_proeminente

    return tema_id


# # ## NO CASO DO SISTEMA DE AVALIAÇÃO_MODAL EU NÃO CONTEMPLEI AINDA  O SISTEMA, POR ENQUANTO VOU ME
# # # ATER APENAS AO SUBSISTEMA DE POLARIDADE.
# #
# # ####FORMAÇÃO DA ORAÇÃO
# #
#
####
# print('Qual o tipo_pessoa de Processo?')
# 	TIPO_DE_PROCESSO = choice.Menu().ask()
# print('Selecione as opções do sistema da Oração Material')


def transitividade(tipo_de_processo=None, indice_material=None,
                   indice_agenciamento=None, indice_relacional=None):
    """
    Retorna a transitividade da oração.

    Ex.:

    >>> transitividade(tipo_de_processo='Relacional',indice_material=None, indice_agenciamento=1, indice_relacional=0)
    -> 'PR_relacional_intensivo_atributivo_sem_atribuição_de_relação_AG_médio_com_alcance':
    for i in range(3):
        for j in range(7):
            print(transitividade(tipo_de_processo='Material', indice_material=i,
            indice_agenciamento=j, indice_relacional=None))
    :param tipo_de_processo: ['Material', 'Relacional',
                            'Mental', 'Verbal',
                            'Existencial']
    :param indice_material: [0:"PR_material_transformativo_IMPA_transitivo",
    1:"PR_material_criativo_IMPA_transitivo"
    2:"PR_material_transformativo_IMPA_intransitivo",
    3:"PR_material_criativo_IMPA_intransitivo]
    :param indice_agenciamento: [0:'AG_médio_sem_alcance',1:'AG_médio_com_alcance',
    2:'AG_efetivo_operativo',3:'AG_efetivo_receptivo',
    4:'AG_efetivo_receptivo_não_agentivo',5:'AG_processo_sem_alcance',
    6:'AG_processo_com_alcance']
    :param indice_relacional:  [0:'PR_relacional_intensivo_atributivo',
   1:'PR_relacional_intensivo_identificativo',
   2:'PR_relacional_possessivo_atributivo',
   3:'PR_relacional_possessivo_identificativo',
   4:'PR_relacional_circunstancial_atributivo',
   5'PR_relacional_circunstancial_identificativo]
    :return:
    """
    processo, agnciamento = '', ''
    if tipo_de_processo == 'Material':
        processo = processo_material(indice_material)
        agnciamento = agenciamento(indice_agenciamento)

    elif tipo_de_processo == 'Relacional':
        processo = processo_relacional(indice_relacional)
        agnciamento = agenciamento(indice_agenciamento)

    elif tipo_de_processo == 'Existencial':
        processo = 'PR_Existencial'
        agnciamento = agenciamento(indice_agenciamento)

    elif tipo_de_processo == 'Verbal':
        processo = 'PR_Verbal'
        agnciamento = agenciamento(indice_agenciamento)

    elif tipo_de_processo == 'Mental':
        processo = 'PR_Mental'
        agnciamento = agenciamento(indice_agenciamento)

    real_transitividade = processo + '_' + agnciamento
    return real_transitividade

# 
# 
# transitividade(tipo_de_processo='Material', indice_material=0, indice_agenciamento=2,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=1, indice_agenciamento=2,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=1, indice_agenciamento=2,indice_relacional=None)
# for i in range(3):
# 	for j in range(7):
# 		print(transitividade(tipo_de_processo='Material', indice_material=i, indice_agenciamento=j, indice_relacional=None))
# # #
# transitividade(tipo_de_processo='Material', indice_material=0, indice_agenciamento=0,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=1, indice_agenciamento=0,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=2, indice_agenciamento=0,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=3, indice_agenciamento=0,indice_relacional=None)
#
# transitividade(tipo_de_processo='Material', indice_material=0, indice_agenciamento=3,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=1, indice_agenciamento=0,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=2, indice_agenciamento=0,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=3, indice_agenciamento=0,indice_relacional=None)
#
# transitividade(tipo_de_processo='Material', indice_material=3, indice_agenciamento=0,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=3, indice_agenciamento=1,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=2, indice_agenciamento=1,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=2, indice_agenciamento=1,indice_relacional=None)
# transitividade(tipo_de_processo='Material', indice_material=2, indice_agenciamento=6,indice_relacional=None)
#

# transitividade(tipo_de_processo='Mental', indice_material=None, indice_agenciamento=1,indice_relacional=None)
# # transitividade(tipo_de_processo='Verbal', indice_agenciamento=2)


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
# aqui dev
def oracao_mental(
        # TRANSITIVIDADE
        tipo_de_processo=None, indice_material=None, indice_agenciamento=None, indice_relacional=None, indice_atrib=None,
        # MODO
        responsabilidade=None, pressuposicao_do_sujeito=None, tipo_modo=None,
        # TEMA INTERPESSOAL
        tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
        t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
        t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None, t_inter_fp_numero_beta=None,
        t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None, t_inter_fp_orientacao_alpha=None,
        t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
        t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None, t_inter_fp_genero_obj_possuido=None,
        t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
        t_inter_fp_genero_numerativo=None,
        t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None, t_inter_fp_tipo_de_nao_consciente_material=None,
        t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None, t_inter_fp_substantivo_lematizado=None,
        t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None, t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
        t_inter_fp_nome_prop_fp=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None, t_inter_fp_tonicidade=None,
        t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
        t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None, t_inter_fp_contracao=None,
        #
        # 		#
        t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        t_text_tem_tema_textual=False, t_text_indice_cont=None,
        t_text_tipo_de_conjuncao=None,
        t_text_indice_conj=None, t_text_tipo_de_relativo=None,
        t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
        t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
        # TEMA IDEACIONAL
        orientacao_modal=None, orientacao_transitiva=None,
        selecao_tematica=None, tema_default=None,
        tema_default_indicativo=None, tema_identificativo=None,
        tema_angulo=None, tema_elemental=None,
        tema_proeminente=None,
        ##específico do Processo Mental
        fenomenalizacao=None, tipo_de_mental=None,

        ##Processo
        tipo_de_experiencia_gv=None, agencia=None, tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex=None, funcao_no_grupo_verbal_pos_final=None,
        verbo_lex=None, tipo_de_orientacao_lex=None, oi_numero_lex=None, genero_lex=None, oi_tipo_de_pessoa_lex=None,
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
        p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
        p1_cardinal=None, p1_genero_numerativo=None,
        p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
        p1_numero_subs=None,p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None, p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
        p1_reflexivo=None, p1_adjetivo_epiteto=None, p1_adjetivo_classificador=None, p1_genero_adjetivo=None,
        p1_numero_adjetivo=None, p1_contracao=None,
        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
        p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
        p2_cardinal=None, p2_genero_numerativo=None,
        p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
        p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
        p2_nome_proprio=None,
        p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
        p2_reflexivo=None, p2_adjetivo_epiteto=None, p2_adjetivo_classificador=None, p2_genero_adjetivo=None,
        p2_numero_adjetivo=None, p2_contracao=None,
        ##PARTICIPANTES REALIZADOS POR FP
        part_fp_indice_preposicao_frase=None, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
        part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
        part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
        part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
        part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
        part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
        part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
        part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None, 
        part_fp_tipo_numerativo=None,  part_fp_cardinal=None,
         part_fp_genero_numerativo=None, part_fp_tipo_de_ente=None,
        part_fp_tipo_de_nao_consciente=None, part_fp_tipo_de_nao_consciente_material=None,
        part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente=None,
        part_fp_substantivo_lematizado=None, part_fp_numero_subs=None,part_fp_genero_subs=None,
        part_fp_tipo_feminino_ao=None,
        part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
        part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
        part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None, part_fp_adjetivo_epiteto=None,
        part_fp_adjetivo_classificador=None, part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
        part_fp_contracao=None,
        ##CIRCUNSTANCIA
        CIRC_ORACAO_realizacaoCircunstancia=None, CIRC_ORACAO_indice_preposicao_frase=None,
        CIRC_ORACAO_dissoc_ente_nucleo=None, CIRC_ORACAO_tem_qualificador=None, CIRC_ORACAO_tipo_qualificador=None,
        CIRC_ORACAO_indice_preposicao_qualif=None, CIRC_ORACAO_determinacao_especificidade_beta=None,
        CIRC_ORACAO_orientacao_beta=None, CIRC_ORACAO_genero_beta=None, CIRC_ORACAO_numero_beta=None,
        CIRC_ORACAO_morfologia_do_pronome_beta=None, CIRC_ORACAO_determinacao_especificidade_alpha=None,
        CIRC_ORACAO_orientacao_alpha=None, CIRC_ORACAO_genero_alpha=None, CIRC_ORACAO_numero_alpha=None,
        CIRC_ORACAO_morfologia_do_pronome_alpha=None, CIRC_ORACAO_pessoa_da_interlocucao_possuidor=None,
        CIRC_ORACAO_numero_obj_possuido=None, CIRC_ORACAO_genero_obj_possuido=None,
        CIRC_ORACAO_pessoa_da_interlocucao_proximidade=None, CIRC_ORACAO_funcao_numerativo=None,
        CIRC_ORACAO_cardinal=None, CIRC_ORACAO_genero=None, CIRC_ORACAO_tipo_precisa=None,
        CIRC_ORACAO_tipo_real_card=None, CIRC_ORACAO_milharExtenso=None, CIRC_ORACAO_centenaExtenso=None,
        CIRC_ORACAO_dezenaExtenso=None, CIRC_ORACAO_unidadeExtenso=None, CIRC_ORACAO_numIndefinido=None,
        CIRC_ORACAO_tipo_de_ente=None, CIRC_ORACAO_tipo_de_nao_consciente=None,
        CIRC_ORACAO_tipo_de_nao_consciente_material=None, CIRC_ORACAO_tipo_de_nao_consciente_semiotico=None,
        CIRC_ORACAO_classe_palavra_ente=None, CIRC_ORACAO_substantivo_lematizado=None, CIRC_ORACAO_numero=None,
        CIRC_ORACAO_tipo_feminino_ao=None, CIRC_ORACAO_tipo_masc_ao=None, CIRC_ORACAO_acent_tonica=None,
        CIRC_ORACAO_nome_proprio=None, CIRC_ORACAO_pessoa_da_interlocucao=None, CIRC_ORACAO_transitividade_verbo=None,
        CIRC_ORACAO_tonicidade=None, CIRC_ORACAO_morfologia_do_pronome=None, CIRC_ORACAO_reflexivo=None,
        CIRC_ORACAO_adjetivo_epiteto=None, CIRC_ORACAO_adjetivo_classificador=None, CIRC_ORACAO_genero_adjetivo=None,
        CIRC_ORACAO_numero_adjetivo=None, CIRC_ORACAO_contracao=None, CIRC_ORACAO_tipo_de_adverbio1=None,
        CIRC_ORACAO_ind1=None, CIRC_ORACAO_tipo_de_adverbio2=None, CIRC_ORACAO_ind2=None,
        CIRC_ORACAO_tipo_de_adverbio3=None, CIRC_ORACAO_ind3=None, CIRC_ORACAO_tipo_de_adverbio4=None,
        CIRC_ORACAO_ind4=None, CIRC_ORACAO_tipo_de_adverbio5=None, CIRC_ORACAO_ind5=None

):
    try:
        transitividade_ = transitividade(tipo_de_processo, indice_material, indice_agenciamento, indice_relacional, indice_atrib)
        Modo = modo(responsabilidade, pressuposicao_do_sujeito, tipo_modo)
        tema_interp = tema_interpessoal(tipo_tema_interpessoal, t_inter_tipo_realizacao, t_inter_tipo_de_adverbio1,
                                              t_inter_ind_adv_1, t_inter_tipo_de_adverbio2, t_inter_ind_adv_2,
                                              t_inter_tipo_de_adverbio3, t_inter_ind_adv_3, t_inter_tipo_de_adverbio4,
                                              t_inter_ind_adv_4, t_inter_tipo_de_adverbio5, t_inter_ind_adv_5,
                                              t_inter_fp_indice_preposicao_frase,
                                              t_inter_fp_dissoc_ente_nucleo, t_inter_fp_tem_qualificador,
                                              t_inter_fp_tipo_qualificador,
                                              t_inter_fp_indice_preposicao_qualif,
                                              t_inter_fp_determinacao_especificidade_beta,
                                              t_inter_fp_orientacao_beta, t_inter_fp_genero_beta,
                                              t_inter_fp_numero_beta,
                                              t_inter_fp_morfologia_do_pronome_beta,
                                              t_inter_fp_determinacao_especificidade_alpha,
                                              t_inter_fp_orientacao_alpha,
                                              t_inter_fp_genero_alpha, t_inter_fp_numero_alpha,
                                              t_inter_fp_morfologia_do_pronome_alpha,
                                              t_inter_fp_pessoa_da_interlocucao_possuidor,
                                              t_inter_fp_numero_obj_possuido, t_inter_fp_genero_obj_possuido,
                                              t_inter_fp_pessoa_da_interlocucao_proximidade,
                                              t_inter_fp_tipo_numerativo, t_inter_fp_cardinal,
                                              t_inter_fp_genero_numerativo,
                                              t_inter_fp_tipo_de_ente, t_inter_fp_tipo_de_nao_consciente,
                                              t_inter_fp_tipo_de_nao_consciente_material,
                                              t_inter_fp_tipo_de_nao_consciente_semiotico,
                                              t_inter_fp_classe_palavra_ente,
                                              t_inter_fp_substantivo_lematizado,
                                              t_inter_fp_numero_subs, t_inter_fp_genero_subs,
                                              t_inter_fp_tipo_feminino_ao, t_inter_fp_tipo_masc_ao,
                                              t_inter_fp_acent_tonica,
                                              t_inter_fp_nome_prop_fp, t_inter_fp_pessoa_da_interlocucao,
                                              t_inter_fp_transitividade_verbo, t_inter_fp_tonicidade,
                                              t_inter_fp_morfologia_do_pronome, t_inter_fp_reflexivo,
                                              t_inter_fp_adjetivo_epiteto,
                                              t_inter_fp_adjetivo_classificador, t_inter_fp_genero_adjetivo,
                                              t_inter_fp_numero_adjetivo, t_inter_fp_contracao,
                                              t_inter_indice_elem_qu,
                                              t_inter_indice_part_modal, t_inter_nome_proprio)
        tema_text = tema_textual(t_text_tem_tema_textual, t_text_indice_cont,
                                    t_text_tipo_de_conjuncao,
                                    t_text_indice_conj, t_text_tipo_de_relativo,
                                    t_text_tipo_pronome_relativo, t_text_genero, t_text_numero,
                                    t_text_indice_relativo, t_text_indice_relativo_adv)
        tema_id = tema_ideacional(orientacao_modal, orientacao_transitiva,
                                  selecao_tematica, tema_default,
                                  tema_default_indicativo, tema_identificativo,
                                  tema_angulo, tema_elemental,
                                  tema_proeminente)
        polar = polaridade(tipo_polaridade)
        Processo = grupo_verbal(tipo_de_experiencia_gv, agencia, tipo_de_experiencia_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, oi_numero_1, genero_1, oi_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, tipo_de_experiencia_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, oi_numero_2, genero_2, oi_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, tipo_de_experiencia_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, oi_numero_3, genero_3, oi_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, tipo_de_experiencia_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, oi_numero_4, genero_4, oi_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final,
                                verbo_lex, tipo_de_orientacao_lex, oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                padrao_pessoa_morfologia_lex)
        Circunstancia = circunstancia(CIRC_ORACAO_realizacaoCircunstancia, CIRC_ORACAO_indice_preposicao_frase,
                                      CIRC_ORACAO_dissoc_ente_nucleo, CIRC_ORACAO_tem_qualificador,
                                      CIRC_ORACAO_tipo_qualificador, CIRC_ORACAO_indice_preposicao_qualif,
                                      CIRC_ORACAO_determinacao_especificidade_beta, CIRC_ORACAO_orientacao_beta,
                                      CIRC_ORACAO_genero_beta, CIRC_ORACAO_numero_beta,
                                      CIRC_ORACAO_morfologia_do_pronome_beta,
                                      CIRC_ORACAO_determinacao_especificidade_alpha, CIRC_ORACAO_orientacao_alpha,
                                      CIRC_ORACAO_genero_alpha, CIRC_ORACAO_numero_alpha,
                                      CIRC_ORACAO_morfologia_do_pronome_alpha,
                                      CIRC_ORACAO_pessoa_da_interlocucao_possuidor, CIRC_ORACAO_numero_obj_possuido,
                                      CIRC_ORACAO_genero_obj_possuido, CIRC_ORACAO_pessoa_da_interlocucao_proximidade,
                                      cardinal=CIRC_ORACAO_cardinal, genero_numerativo=CIRC_ORACAO_numIndefinido,
                                      tipo_de_ente=CIRC_ORACAO_tipo_de_ente,
                                      tipo_de_nao_consciente=CIRC_ORACAO_tipo_de_nao_consciente,
                                      tipo_de_nao_consciente_material=CIRC_ORACAO_tipo_de_nao_consciente_material,
                                      tipo_de_nao_consciente_semiotico=CIRC_ORACAO_tipo_de_nao_consciente_semiotico,
                                      classe_palavra_ente=CIRC_ORACAO_classe_palavra_ente,
                                      substantivo_lematizado=CIRC_ORACAO_substantivo_lematizado,
                                      numero=CIRC_ORACAO_numero, tipo_feminino_ao=CIRC_ORACAO_tipo_feminino_ao,
                                      tipo_masc_ao=CIRC_ORACAO_tipo_masc_ao, acent_tonica=CIRC_ORACAO_acent_tonica,
                                      nome_prop=CIRC_ORACAO_nome_proprio,
                                      pessoa_da_interlocucao=CIRC_ORACAO_pessoa_da_interlocucao,
                                      transitividade_verbo=CIRC_ORACAO_transitividade_verbo,
                                      tonicidade=CIRC_ORACAO_tonicidade,
                                      morfologia_do_pronome=CIRC_ORACAO_morfologia_do_pronome,
                                      reflexivo=CIRC_ORACAO_reflexivo, adjetivo_epiteto=CIRC_ORACAO_adjetivo_epiteto,
                                      adjetivo_classificador=CIRC_ORACAO_adjetivo_classificador,
                                      genero_adjetivo=CIRC_ORACAO_genero_adjetivo,
                                      numero_adjetivo=CIRC_ORACAO_numero_adjetivo, contracao=CIRC_ORACAO_contracao,
                                      tipo_de_adverbio1=CIRC_ORACAO_tipo_de_adverbio1, ind1=CIRC_ORACAO_ind1,
                                      tipo_de_adverbio2=CIRC_ORACAO_tipo_de_adverbio2, ind2=CIRC_ORACAO_ind2,
                                      tipo_de_adverbio3=CIRC_ORACAO_tipo_de_adverbio3, ind3=CIRC_ORACAO_ind3,
                                      tipo_de_adverbio4=CIRC_ORACAO_tipo_de_adverbio4, ind4=CIRC_ORACAO_ind4,
                                      tipo_de_adverbio5=CIRC_ORACAO_tipo_de_adverbio5, ind5=CIRC_ORACAO_ind5)

        # ORAÇÃO MENTAL declarativa

        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

            if transitividade_ == 'PR_Mental_AG_médio_sem_alcance':

                Experienciador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador,
                                              p1_tipo_qualificador,
                                              p1_indice_preposicao_qualif,
                                              p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                              p1_genero_beta, p1_numero_beta,
                                              p1_morfologia_do_pronome_beta,
                                              p1_determinacao_especificidade_alpha, p1_orientacao_alpha,
                                              p1_genero_alpha, p1_numero_alpha,
                                              p1_morfologia_do_pronome_alpha,
                                              p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido,
                                              p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                              p1_tipo_numerativo,
                                              p1_cardinal, p1_genero_numerativo,
                                              p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                              p1_tipo_de_nao_consciente_material,
                                              p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                              p1_substantivo_lematizado,
                                              p1_numero_subs, p1_genero_subs, p1_tipo_feminino_ao,
                                              p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio,
                                              p1_pessoa_da_interlocucao, p1_transitividade_verbo,
                                              p1_tonicidade, p1_morfologia_do_pronome,
                                              p1_reflexivo, p1_adjetivo_epiteto,
                                              p1_adjetivo_classificador, p1_genero_adjetivo,
                                              p1_numero_adjetivo, p1_contracao)
                if fenomenalizacao == 'não-fenomenalização_comportamento-passivo':

                    if (tipo_de_mental == 'superior_cognitivo' or
                            tipo_de_mental == 'superior_desiderativo' or
                            # Ex.: Tenho pensado; Eu pensei a noite toda;
                            tipo_de_mental == 'inferior_emotivo' or
                            tipo_de_mental == 'inferior_perceptivo'):
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + '.'
                    # 'Eu ouvi perfeitamente'

            elif transitividade_ == 'PR_Mental_AG_médio_com_alcance':
                Experienciador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador,
                                              p1_tipo_qualificador, p1_indice_preposicao_qualif,
                                              p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                              p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                              p1_determinacao_especificidade_alpha, p1_orientacao_alpha,
                                              p1_genero_alpha, p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                              p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido,
                                              p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                              p1_tipo_numerativo, p1_cardinal, p1_genero_numerativo,
                                              p1_tipo_de_ente, p1_tipo_de_nao_consciente, 
                                              p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                              p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero_subs,
                                              p1_genero_subs, p1_tipo_feminino_ao,p1_tipo_masc_ao, 
                                              p1_acent_tonica, p1_nome_proprio,
                                              p1_pessoa_da_interlocucao, p1_transitividade_verbo,
                                              p1_tonicidade, p1_morfologia_do_pronome,
                                              p1_reflexivo, p1_adjetivo_epiteto,
                                              p1_adjetivo_classificador, p1_genero_adjetivo,
                                              p1_numero_adjetivo, p1_contracao)
                if fenomenalizacao == 'não-fenomenalização_assunto':
                    if (tipo_de_mental == 'superior_cognitivo' or tipo_de_mental == 'superior_desiderativo' or
                            tipo_de_mental == 'inferior_emotivo' or tipo_de_mental == 'inferior_perceptivo'):
                        Assunto = frase_preposicional(part_fp_indice_preposicao_frase,
                                                      part_fp_dissoc_ente_nucleo, part_fp_tem_qualificador,
                                                      part_fp_tipo_qualificador,
                                                      part_fp_indice_preposicao_qualif,
                                                      part_fp_determinacao_especificidade_beta,
                                                      part_fp_orientacao_beta, part_fp_genero_beta,
                                                      part_fp_numero_beta, part_fp_morfologia_do_pronome_beta,
                                                      part_fp_determinacao_especificidade_alpha,
                                                      part_fp_orientacao_alpha, part_fp_genero_alpha,
                                                      part_fp_numero_alpha,
                                                      part_fp_morfologia_do_pronome_alpha,
                                                      part_fp_pessoa_da_interlocucao_possuidor,
                                                      part_fp_numero_obj_possuido,
                                                      part_fp_genero_obj_possuido,
                                                      part_fp_pessoa_da_interlocucao_proximidade,
                                                      part_fp_tipo_numerativo, part_fp_cardinal,
                                                      part_fp_genero_numerativo, part_fp_tipo_de_ente,
                                                      part_fp_tipo_de_nao_consciente,
                                                      part_fp_tipo_de_nao_consciente_material,
                                                      part_fp_tipo_de_nao_consciente_semiotico,
                                                      part_fp_classe_palavra_ente,
                                                      part_fp_substantivo_lematizado, part_fp_numero_subs,
                                                      part_fp_genero_subs,
                                                      part_fp_tipo_feminino_ao,
                                                      part_fp_tipo_masc_ao, part_fp_acent_tonica,
                                                      part_fp_nome_proprio,
                                                      part_fp_pessoa_da_interlocucao,
                                                      part_fp_transitividade_verbo, part_fp_tonicidade,
                                                      part_fp_morfologia_do_pronome, part_fp_reflexivo,
                                                      part_fp_adjetivo_epiteto,
                                                      part_fp_adjetivo_classificador, part_fp_genero_adjetivo,
                                                      part_fp_numero_adjetivo,
                                                      part_fp_contracao)
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Assunto + '.'
                # Ex.: Eu sei de futebol.

                # 'Médio com alcance = mental emanente.'
                # TIPO_FENOMENALIZACAO= choice.Menu(['hiperfenômeno', 'fenômeno_simples']
                # print('Qual tipo_pessoa de Processo superior?')
                # TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                elif fenomenalizacao == 'fenomenalização_fenômeno-simples':
                    if (tipo_de_mental == 'superior_cognitivo' or tipo_de_mental == 'superior_desiderativo'):

                        Fenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                              p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                              p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                              p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                              p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                              p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                              p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                              p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                              p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                              p2_tipo_de_ente, p2_tipo_de_nao_consciente, 
                                              p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                              p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                              p2_genero_subs, p2_tipo_feminino_ao,p2_tipo_masc_ao, 
                                              p2_acent_tonica, p2_nome_proprio,
                                              p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                              p2_tonicidade, p2_morfologia_do_pronome,
                                              p2_reflexivo, p2_adjetivo_epiteto,
                                              p2_adjetivo_classificador, p2_genero_adjetivo,
                                              p2_numero_adjetivo, p2_contracao)

                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Fenomeno + '.'
                    # Ex.: Eu imaginei o jogo
                    elif (tipo_de_mental == 'inferior_emotivo' or tipo_de_mental == 'inferior_perceptivo'):
                        # APESAR DE PARECER REDUNDANTE, EM UMA PRÓXIMA FASE, CADA UMA DESTAS ITERAÇÕES
                        # VAI TER OS LEXEMAS REPRESENTATIVOS DE CADA TIPO DE PROCESSO MENTAL
                        # print('Qual tipo_pessoa de Processo inferior?')
                        # TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')

                        Fenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                              p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                              p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                              p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                              p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                              p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                              p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                              p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                              p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                              p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                              p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                              p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                              p2_genero_subs, p2_tipo_feminino_ao,p2_tipo_masc_ao,
                                              p2_acent_tonica, p2_nome_proprio,
                                              p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                              p2_tonicidade, p2_morfologia_do_pronome,
                                              p2_reflexivo, p2_adjetivo_epiteto,
                                              p2_adjetivo_classificador, p2_genero_adjetivo,
                                              p2_numero_adjetivo, p2_contracao)

                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Fenomeno + '.'

                elif fenomenalizacao == 'hiperfenômeno_criativo_pensamento':
                    if tipo_de_mental == 'superior_cognitivo':
                        # 'pensar', 'saber', 'sonhar'
                        Pensamento = oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento + '.'

                elif fenomenalizacao == 'hiperfenômeno_criativo_desejo':
                    if tipo_de_mental == 'superior_desiderativo':
                        # print('Qual tipo_pessoa de hiperfenômeno?')
                        # print('Projeção = hiperfenômeno: criativo')
                        # TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar'])
                        Desejo = oracaooProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + 'que' + ' ' + Desejo + '.'
                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
                    if tipo_de_mental == 'inferior_emotivo':
                        Metafenomeno = oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Metafenomeno + '.'
                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_que':
                    if tipo_de_mental == 'inferior_emotivo':
                        Metafenomeno = 'que' + ' ' + oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Metafenomeno + '.'
                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == 'inferior_emotivo':
                        # print('Selecione o GN com oração qualificadora:')
                        Metafenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                    p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                    p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                    p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                    p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                    p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                                    p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                    p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                    p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                    p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                    p2_tipo_de_nao_consciente_material,
                                                    p2_tipo_de_nao_consciente_semiotico,
                                                    p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                                    p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                    p2_acent_tonica, p2_nome_proprio,
                                                    p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                    p2_tonicidade, p2_morfologia_do_pronome,
                                                    p2_reflexivo, p2_adjetivo_epiteto,
                                                    p2_adjetivo_classificador, p2_genero_adjetivo,
                                                    p2_numero_adjetivo, p2_contracao)

                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Metafenomeno + '.'

                elif (fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_não-orientado_gerúndio'):
                    if tipo_de_mental == 'inferior_perceptivo':
                        Macrofenomeno = oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Macrofenomeno + '.'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if tipo_de_mental == 'inferior_perceptivo':
                        Macrofenomeno = 'que' + ' ' + oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Macrofenomeno + '.'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == 'inferior_perceptivo':
                        Macrofenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                     p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                     p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                     p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                     p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                     p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                                     p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                     p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                     p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                     p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                     p2_tipo_de_nao_consciente_material,
                                                     p2_tipo_de_nao_consciente_semiotico,
                                                     p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                                     p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                     p2_acent_tonica, p2_nome_proprio,
                                                     p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                     p2_tonicidade, p2_morfologia_do_pronome,
                                                     p2_reflexivo, p2_adjetivo_epiteto,
                                                     p2_adjetivo_classificador, p2_genero_adjetivo,
                                                     p2_numero_adjetivo, p2_contracao)
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Macrofenomeno + '.'

            elif transitividade_ == 'PR_Mental_AG_efetivo_operativo':
                # impingente
                ExperienciadorGN = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                              p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                              p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                              p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                              p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                              p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                              p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                              p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                              p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                              p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                              p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                              p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                              p2_genero_subs, p2_tipo_feminino_ao,p2_tipo_masc_ao,
                                              p2_acent_tonica, p2_nome_proprio,
                                              p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                              p2_tonicidade, p2_morfologia_do_pronome,
                                              p2_reflexivo, p2_adjetivo_epiteto,
                                              p2_adjetivo_classificador, p2_genero_adjetivo,
                                              p2_numero_adjetivo, p2_contracao)
                ExperienciadorFP = frase_preposicional(part_fp_indice_preposicao_frase,
                                                       part_fp_dissoc_ente_nucleo, part_fp_tem_qualificador,
                                                       part_fp_tipo_qualificador,
                                                       part_fp_indice_preposicao_qualif,
                                                       part_fp_determinacao_especificidade_beta,
                                                       part_fp_orientacao_beta, part_fp_genero_beta,
                                                       part_fp_numero_beta,
                                                       part_fp_morfologia_do_pronome_beta,
                                                       part_fp_determinacao_especificidade_alpha,
                                                       part_fp_orientacao_alpha, part_fp_genero_alpha,
                                                       part_fp_numero_alpha,
                                                       part_fp_morfologia_do_pronome_alpha,
                                                       part_fp_pessoa_da_interlocucao_possuidor,
                                                       part_fp_numero_obj_possuido,
                                                       part_fp_genero_obj_possuido,
                                                       part_fp_pessoa_da_interlocucao_proximidade,
                                                       part_fp_tipo_numerativo, part_fp_cardinal,
                                                       part_fp_genero_numerativo, part_fp_tipo_de_ente,
                                                       part_fp_tipo_de_nao_consciente,
                                                       part_fp_tipo_de_nao_consciente_material,
                                                       part_fp_tipo_de_nao_consciente_semiotico,
                                                       part_fp_classe_palavra_ente,
                                                       part_fp_substantivo_lematizado, part_fp_numero_subs,
                                                       part_fp_genero_subs,
                                                       part_fp_tipo_feminino_ao,
                                                       part_fp_tipo_masc_ao, part_fp_acent_tonica,
                                                       part_fp_nome_proprio,
                                                       part_fp_pessoa_da_interlocucao,
                                                       part_fp_transitividade_verbo, part_fp_tonicidade,
                                                       part_fp_morfologia_do_pronome, part_fp_reflexivo,
                                                       part_fp_adjetivo_epiteto,
                                                       part_fp_adjetivo_classificador,
                                                       part_fp_genero_adjetivo, part_fp_numero_adjetivo,
                                                       part_fp_contracao)
                if fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
                    if tipo_de_mental == 'inferior_emotivo':
                        MetafenomenoAgente = oracaoProjetada()
                        oracao = MetafenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_que':
                    if tipo_de_mental == 'inferior_emotivo':
                        MetafenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oracao = MetafenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == 'inferior_emotivo':
                        # print('Selecione o GN com oração qualificadora:')
                        MetafenomenoAgente = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                          p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                          p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                          p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                          p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                          p2_genero_alpha, p2_numero_alpha,
                                                          p2_morfologia_do_pronome_alpha,
                                                          p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                          p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                          p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                          p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                          p2_tipo_de_nao_consciente_material,
                                                          p2_tipo_de_nao_consciente_semiotico,
                                                          p2_classe_palavra_ente, p2_substantivo_lematizado,
                                                          p2_numero_subs,
                                                          p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                          p2_acent_tonica, p2_nome_proprio,
                                                          p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                          p2_tonicidade, p2_morfologia_do_pronome,
                                                          p2_reflexivo, p2_adjetivo_epiteto,
                                                          p2_adjetivo_classificador, p2_genero_adjetivo,
                                                          p2_numero_adjetivo, p2_contracao)
                        oracao = MetafenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif (fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      fenomenalizacao == 'reativo_macrofenômeno_não-orientado_gerúndio'):
                    if tipo_de_mental == "superior_cognitivo":
                        MacrofenomenoAgente = oracaoProjetada()
                        oracao = MacrofenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if tipo_de_mental == "superior_cognitivo":
                        MacrofenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oracao = MacrofenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == "superior_cognitivo":
                        MacrofenomenoAgente = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                           p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                           p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                           p2_genero_beta, p2_numero_beta,
                                                           p2_morfologia_do_pronome_beta,
                                                           p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                           p2_genero_alpha, p2_numero_alpha,
                                                           p2_morfologia_do_pronome_alpha,
                                                           p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                           p2_genero_obj_possuido,
                                                           p2_pessoa_da_interlocucao_proximidade,
                                                           p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                           p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                           p2_tipo_de_nao_consciente_material,
                                                           p2_tipo_de_nao_consciente_semiotico,
                                                           p2_classe_palavra_ente, p2_substantivo_lematizado,
                                                           p2_numero_subs,
                                                           p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                           p2_acent_tonica, p2_nome_proprio,
                                                           p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                           p2_tonicidade, p2_morfologia_do_pronome,
                                                           p2_reflexivo, p2_adjetivo_epiteto,
                                                           p2_adjetivo_classificador, p2_genero_adjetivo,
                                                           p2_numero_adjetivo, p2_contracao)
                        oracao = MacrofenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif fenomenalizacao == "fenomenalização_fenômeno_simples":
                    if tipo_de_mental == "superior_cognitivo":
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')
                        FenomenoAgente = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador,
                                                      p1_tipo_qualificador,
                                                      p1_indice_preposicao_qualif,
                                                      p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                                      p1_genero_beta, p1_numero_beta,
                                                      p1_morfologia_do_pronome_beta,
                                                      p1_determinacao_especificidade_alpha,
                                                      p1_orientacao_alpha, p1_genero_alpha,
                                                      p1_numero_alpha,
                                                      p1_morfologia_do_pronome_alpha,
                                                      p1_pessoa_da_interlocucao_possuidor,
                                                      p1_numero_obj_possuido,
                                                      p1_genero_obj_possuido,
                                                      p1_pessoa_da_interlocucao_proximidade,
                                                      p1_tipo_numerativo,
                                                      p1_cardinal, p1_genero_numerativo,
                                                      p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                                      p1_tipo_de_nao_consciente_material,
                                                      p1_tipo_de_nao_consciente_semiotico,
                                                      p1_classe_palavra_ente, p1_substantivo_lematizado,
                                                      p1_numero_subs, p1_genero_subs,
                                                      p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                                      p1_acent_tonica, p1_nome_proprio,
                                                      p1_pessoa_da_interlocucao, p1_transitividade_verbo,
                                                      p1_tonicidade, p1_morfologia_do_pronome,
                                                      p1_reflexivo, p1_adjetivo_epiteto,
                                                      p1_adjetivo_classificador, p1_genero_adjetivo,
                                                      p1_numero_adjetivo, p1_contracao)
                        oracao = FenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

        # comeca interrogativa polar
        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

            if transitividade_ == 'PR_Mental_AG_médio_sem_alcance':

                Experienciador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                              p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                              p1_orientacao_beta,
                                              p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                              p1_determinacao_especificidade_alpha, p1_orientacao_alpha,
                                              p1_genero_alpha, p1_numero_alpha,
                                              p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                              p1_numero_obj_possuido,
                                              p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                              p1_tipo_numerativo,
                                              p1_cardinal, p1_genero_numerativo,
                                              p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                              p1_tipo_de_nao_consciente_material,
                                              p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                              p1_substantivo_lematizado,
                                              p1_numero_subs, p1_genero_subs, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                              p1_acent_tonica, p1_nome_proprio,
                                              p1_pessoa_da_interlocucao, p1_transitividade_verbo, p1_tonicidade,
                                              p1_morfologia_do_pronome,
                                              p1_reflexivo, p1_adjetivo_epiteto, p1_adjetivo_classificador,
                                              p1_genero_adjetivo,
                                              p1_numero_adjetivo, p1_contracao)
                if fenomenalizacao == 'não-fenomenalização_comportamento-passivo':

                    if (tipo_de_mental == 'superior_cognitivo' or
                            tipo_de_mental == 'superior_desiderativo' or
                            # Ex.: Tenho pensado; Eu pensei a noite toda;
                            tipo_de_mental == 'inferior_emotivo' or
                            tipo_de_mental == 'inferior_perceptivo'):
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + '?'
            # 'Eu ouvi perfeitamente'

            elif transitividade_ == 'PR_Mental_AG_médio_com_alcance':
                Experienciador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                              p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                              p1_orientacao_beta,
                                              p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                              p1_determinacao_especificidade_alpha, p1_orientacao_alpha,
                                              p1_genero_alpha, p1_numero_alpha,
                                              p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                              p1_numero_obj_possuido,
                                              p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                              p1_tipo_numerativo,
                                              p1_cardinal, p1_genero_numerativo,
                                              p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                              p1_tipo_de_nao_consciente_material,
                                              p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                              p1_substantivo_lematizado,
                                              p1_numero_subs, p1_genero_subs, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                              p1_acent_tonica, p1_nome_proprio,
                                              p1_pessoa_da_interlocucao, p1_transitividade_verbo, p1_tonicidade,
                                              p1_morfologia_do_pronome,
                                              p1_reflexivo, p1_adjetivo_epiteto, p1_adjetivo_classificador,
                                              p1_genero_adjetivo,
                                              p1_numero_adjetivo, p1_contracao)
                if fenomenalizacao == 'não-fenomenalização_assunto':
                    if (tipo_de_mental == 'superior_cognitivo' or tipo_de_mental == 'superior_desiderativo' or
                            tipo_de_mental == 'inferior_emotivo' or tipo_de_mental == 'inferior_perceptivo'):
                        Assunto = frase_preposicional(part_fp_indice_preposicao_frase,
                                                       part_fp_dissoc_ente_nucleo, part_fp_tem_qualificador,
                                                       part_fp_tipo_qualificador,
                                                       part_fp_indice_preposicao_qualif,
                                                       part_fp_determinacao_especificidade_beta,
                                                       part_fp_orientacao_beta, part_fp_genero_beta,
                                                       part_fp_numero_beta,
                                                       part_fp_morfologia_do_pronome_beta,
                                                       part_fp_determinacao_especificidade_alpha,
                                                       part_fp_orientacao_alpha, part_fp_genero_alpha,
                                                       part_fp_numero_alpha,
                                                       part_fp_morfologia_do_pronome_alpha,
                                                       part_fp_pessoa_da_interlocucao_possuidor,
                                                       part_fp_numero_obj_possuido,
                                                       part_fp_genero_obj_possuido,
                                                       part_fp_pessoa_da_interlocucao_proximidade,
                                                       part_fp_tipo_numerativo, part_fp_cardinal,
                                                       part_fp_genero_numerativo, part_fp_tipo_de_ente,
                                                       part_fp_tipo_de_nao_consciente,
                                                       part_fp_tipo_de_nao_consciente_material,
                                                       part_fp_tipo_de_nao_consciente_semiotico,
                                                       part_fp_classe_palavra_ente,
                                                       part_fp_substantivo_lematizado, part_fp_numero_subs,
                                                       part_fp_genero_subs,
                                                       part_fp_tipo_feminino_ao,
                                                       part_fp_tipo_masc_ao, part_fp_acent_tonica,
                                                       part_fp_nome_proprio,
                                                       part_fp_pessoa_da_interlocucao,
                                                       part_fp_transitividade_verbo, part_fp_tonicidade,
                                                       part_fp_morfologia_do_pronome, part_fp_reflexivo,
                                                       part_fp_adjetivo_epiteto,
                                                       part_fp_adjetivo_classificador,
                                                       part_fp_genero_adjetivo, part_fp_numero_adjetivo,
                                                       part_fp_contracao)
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Assunto + '?'
                # Ex.: Eu sei de futebol.

                # 'Médio com alcance = mental emanente.'
                # TIPO_FENOMENALIZACAO= choice.Menu(['hiperfenômeno', 'fenômeno_simples']
                # print('Qual tipo_pessoa de Processo superior?')
                # TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                elif fenomenalizacao == 'fenomenalização_fenômeno-simples':
                    if (tipo_de_mental == 'superior_cognitivo' or tipo_de_mental == 'superior_desiderativo'):

                        Fenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                                p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                                p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                p2_acent_tonica, p2_nome_proprio,
                                                p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                p2_tonicidade, p2_morfologia_do_pronome,
                                                p2_reflexivo, p2_adjetivo_epiteto,
                                                p2_adjetivo_classificador, p2_genero_adjetivo,
                                                p2_numero_adjetivo, p2_contracao)

                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Fenomeno + '?'
                    # Ex.: Eu imaginei o jogo
                    elif (tipo_de_mental == 'inferior_emotivo' or tipo_de_mental == 'inferior_perceptivo'):
                        # APESAR DE PARECER REDUNDANTE, EM UMA PRÓXIMA FASE, CADA UMA DESTAS ITERAÇÕES
                        # VAI TER OS LEXEMAS REPRESENTATIVOS DE CADA TIPO DE PROCESSO MENTAL
                        # print('Qual tipo_pessoa de Processo inferior?')
                        # TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')

                        Fenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                                p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                                p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                p2_acent_tonica, p2_nome_proprio,
                                                p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                p2_tonicidade, p2_morfologia_do_pronome,
                                                p2_reflexivo, p2_adjetivo_epiteto,
                                                p2_adjetivo_classificador, p2_genero_adjetivo,
                                                p2_numero_adjetivo, p2_contracao)

                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Fenomeno + '?'

                elif fenomenalizacao == 'hiperfenômeno_criativo_pensamento':
                    if tipo_de_mental == 'superior_cognitivo':
                        # 'pensar', 'saber', 'sonhar'
                        Pensamento = oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento + '?'

                elif fenomenalizacao == 'hiperfenômeno_criativo_desejo':
                    if tipo_de_mental == 'superior_desiderativo':
                        # print('Qual tipo_pessoa de hiperfenômeno?')
                        # print('Projeção = hiperfenômeno: criativo')
                        # TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar'])
                        Desejo = oracaooProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + 'que' + ' ' + Desejo + '?'
                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
                    if tipo_de_mental == 'inferior_emotivo':
                        Metafenomeno = oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Metafenomeno + '?'
                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_que':
                    if tipo_de_mental == 'inferior_emotivo':
                        Metafenomeno = 'que' + ' ' + oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Metafenomeno + '?'
                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == 'inferior_emotivo':
                        # print('Selecione o GN com oração qualificadora:')
                        Metafenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                              p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                              p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                              p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                              p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                              p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                              p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                              p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                              p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                              p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                              p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                              p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                              p2_genero_subs, p2_tipo_feminino_ao,p2_tipo_masc_ao,
                                              p2_acent_tonica, p2_nome_proprio,
                                              p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                              p2_tonicidade, p2_morfologia_do_pronome,
                                              p2_reflexivo, p2_adjetivo_epiteto,
                                              p2_adjetivo_classificador, p2_genero_adjetivo,
                                              p2_numero_adjetivo, p2_contracao)

                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Metafenomeno + '?'

                elif (fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_não-orientado_gerúndio'):
                    if tipo_de_mental == 'inferior_perceptivo':
                        Macrofenomeno = oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Macrofenomeno + '?'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if tipo_de_mental == 'inferior_perceptivo':
                        Macrofenomeno = 'que' + ' ' + oracaoProjetada()
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Macrofenomeno + '?'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == 'inferior_perceptivo':
                        Macrofenomeno = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                     p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                     p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                     p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                     p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                     p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                                     p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                     p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                     p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                     p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                     p2_tipo_de_nao_consciente_material,
                                                     p2_tipo_de_nao_consciente_semiotico,
                                                     p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                                     p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                     p2_acent_tonica, p2_nome_proprio,
                                                     p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                     p2_tonicidade, p2_morfologia_do_pronome,
                                                     p2_reflexivo, p2_adjetivo_epiteto,
                                                     p2_adjetivo_classificador, p2_genero_adjetivo,
                                                     p2_numero_adjetivo, p2_contracao)
                        oracao = Experienciador + ' ' + polar + ' ' + Processo + ' ' + Macrofenomeno + '?'

            elif transitividade_ == 'PR_Mental_AG_efetivo_operativo':
                # impingente
                ExperienciadorGN = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                                p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                                p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                p2_acent_tonica, p2_nome_proprio,
                                                p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                p2_tonicidade, p2_morfologia_do_pronome,
                                                p2_reflexivo, p2_adjetivo_epiteto,
                                                p2_adjetivo_classificador, p2_genero_adjetivo,
                                                p2_numero_adjetivo, p2_contracao)
                ExperienciadorFP = frase_preposicional(part_fp_indice_preposicao_frase,
                                           p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                              p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                              p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                              p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                              p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                              p2_genero_alpha, p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                              p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                              p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                              p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                              p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                              p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                              p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero_subs,
                                              p2_genero_subs, p2_tipo_feminino_ao,p2_tipo_masc_ao,
                                              p2_acent_tonica, p2_nome_proprio,
                                              p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                              p2_tonicidade, p2_morfologia_do_pronome,
                                              p2_reflexivo, p2_adjetivo_epiteto,
                                              p2_adjetivo_classificador, p2_genero_adjetivo,
                                              p2_numero_adjetivo, p2_contracao            part_fp_dissoc_ente_nucleo, part_fp_tem_qualificador,
                                                       part_fp_tipo_qualificador,
                                                       part_fp_indice_preposicao_qualif,
                                                       part_fp_determinacao_especificidade_beta,
                                                       part_fp_orientacao_beta, part_fp_genero_beta,
                                                       part_fp_numero_beta,
                                                       part_fp_morfologia_do_pronome_beta,
                                                       part_fp_determinacao_especificidade_alpha,
                                                       part_fp_orientacao_alpha, part_fp_genero_alpha,
                                                       part_fp_numero_alpha,
                                                       part_fp_morfologia_do_pronome_alpha,
                                                       part_fp_pessoa_da_interlocucao_possuidor,
                                                       part_fp_numero_obj_possuido,
                                                       part_fp_genero_obj_possuido,
                                                       part_fp_pessoa_da_interlocucao_proximidade,
                                                       part_fp_tipo_numerativo, part_fp_cardinal,
                                                       part_fp_genero_numerativo, part_fp_tipo_de_ente,
                                                       part_fp_tipo_de_nao_consciente,
                                                       part_fp_tipo_de_nao_consciente_material,
                                                       part_fp_tipo_de_nao_consciente_semiotico,
                                                       part_fp_classe_palavra_ente,
                                                       part_fp_substantivo_lematizado, part_fp_numero_subs,
                                                       part_fp_genero_subs,
                                                       part_fp_tipo_feminino_ao,
                                                       part_fp_tipo_masc_ao, part_fp_acent_tonica,
                                                       part_fp_nome_proprio,
                                                       part_fp_pessoa_da_interlocucao,
                                                       part_fp_transitividade_verbo, part_fp_tonicidade,
                                                       part_fp_morfologia_do_pronome, part_fp_reflexivo,
                                                       part_fp_adjetivo_epiteto,
                                                       part_fp_adjetivo_classificador,
                                                       part_fp_genero_adjetivo, part_fp_numero_adjetivo,
                                                       part_fp_contracao)
                if fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
                    if tipo_de_mental == 'inferior_emotivo':
                        MetafenomenoAgente = oracaoProjetada()
                        oracao = MetafenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_oração_que':
                    if tipo_de_mental == 'inferior_emotivo':
                        MetafenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oracao = MetafenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif fenomenalizacao == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == 'inferior_emotivo':
                        # print('Selecione o GN com oração qualificadora:')
                        MetafenomenoAgente = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                          p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                          p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                          p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                                          p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                          p2_genero_alpha, p2_numero_alpha,
                                                          p2_morfologia_do_pronome_alpha,
                                                          p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                          p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                                          p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                          p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                          p2_tipo_de_nao_consciente_material,
                                                          p2_tipo_de_nao_consciente_semiotico,
                                                          p2_classe_palavra_ente, p2_substantivo_lematizado,
                                                          p2_numero_subs,
                                                          p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                          p2_acent_tonica, p2_nome_proprio,
                                                          p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                          p2_tonicidade, p2_morfologia_do_pronome,
                                                          p2_reflexivo, p2_adjetivo_epiteto,
                                                          p2_adjetivo_classificador, p2_genero_adjetivo,
                                                          p2_numero_adjetivo, p2_contracao)
                        oracao = MetafenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif (fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      fenomenalizacao == 'reativo_macrofenômeno_não-orientado_gerúndio'):
                    if tipo_de_mental == "superior_cognitivo":
                        MacrofenomenoAgente = oracaoProjetada()
                        oracao = MacrofenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if tipo_de_mental == "superior_cognitivo":
                        MacrofenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oracao = MacrofenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif fenomenalizacao == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if tipo_de_mental == "superior_cognitivo":
                        MacrofenomenoAgente = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador,
                                                           p2_tipo_qualificador, p2_indice_preposicao_qualif,
                                                           p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                                           p2_genero_beta, p2_numero_beta,
                                                           p2_morfologia_do_pronome_beta,
                                                           p2_determinacao_especificidade_alpha, p2_orientacao_alpha,
                                                           p2_genero_alpha, p2_numero_alpha,
                                                           p2_morfologia_do_pronome_alpha,
                                                           p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                                           p2_genero_obj_possuido,
                                                           p2_pessoa_da_interlocucao_proximidade,
                                                           p2_tipo_numerativo, p2_cardinal, p2_genero_numerativo,
                                                           p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                                           p2_tipo_de_nao_consciente_material,
                                                           p2_tipo_de_nao_consciente_semiotico,
                                                           p2_classe_palavra_ente, p2_substantivo_lematizado,
                                                           p2_numero_subs,
                                                           p2_genero_subs, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                                           p2_acent_tonica, p2_nome_proprio,
                                                           p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                                           p2_tonicidade, p2_morfologia_do_pronome,
                                                           p2_reflexivo, p2_adjetivo_epiteto,
                                                           p2_adjetivo_classificador, p2_genero_adjetivo,
                                                           p2_numero_adjetivo, p2_contracao)
                        oracao = MacrofenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif fenomenalizacao == "fenomenalização_fenômeno_simples":
                    if tipo_de_mental == "superior_cognitivo":
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')
                        FenomenoAgente = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                                      p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                                      p1_orientacao_beta,
                                                      p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                                      p1_determinacao_especificidade_alpha, p1_orientacao_alpha,
                                                      p1_genero_alpha, p1_numero_alpha,
                                                      p1_morfologia_do_pronome_alpha,
                                                      p1_pessoa_da_interlocucao_possuidor,
                                                      p1_numero_obj_possuido,
                                                      p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                                      p1_tipo_numerativo,
                                                      p1_cardinal, p1_genero_numerativo,
                                                      p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                                      p1_tipo_de_nao_consciente_material,
                                                      p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                                      p1_substantivo_lematizado,
                                                      p1_numero_subs, p1_genero_subs, p1_tipo_feminino_ao,
                                                      p1_tipo_masc_ao,
                                                      p1_acent_tonica, p1_nome_proprio,
                                                      p1_pessoa_da_interlocucao, p1_transitividade_verbo, p1_tonicidade,
                                                      p1_morfologia_do_pronome,
                                                      p1_reflexivo, p1_adjetivo_epiteto, p1_adjetivo_classificador,
                                                      p1_genero_adjetivo,
                                                      p1_numero_adjetivo, p1_contracao)
                        oracao = FenomenoAgente + ' ' + polar + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

        return re.sub(' +', ' ', ' '.join((tema_interp, tema_text, oracao))).strip().capitalize()
    except:
        return ""


# oracaoMental()
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
        TIPO_DE_PROCESSO=None, indice_material=None, indice_agenciamento=None, indice_relacional=None, indice_atrib=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, t_inter_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
        t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
        t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
        t_inter_fp_numero_beta=None, t_inter_fp_morfologia_do_pronome_beta=None,
        t_inter_fp_determinacao_especificidade_alpha=None, t_inter_fp_orientacao_alpha=None,
        t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
        t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
        t_inter_fp_genero_obj_possuido=None, t_inter_fp_pessoa_da_interlocucao_proximidade=None,
        t_inter_fp_funcao_numerativo=None, t_inter_fp_cardinal=None, t_inter_fp_genero=None,
        t_inter_fp_tipo_precisa=None, t_inter_fp_tipo_real_card=None, t_inter_fp_milharExtenso=None,
        t_inter_fp_centenaExtenso=None, t_inter_fp_dezenaExtenso=None, t_inter_fp_unidadeExtenso=None,
        t_inter_fp_numIndefinido=None, t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
        t_inter_fp_tipo_de_nao_consciente_material=None, t_inter_fp_tipo_de_nao_consciente_semiotico=None,
        t_inter_fp_classe_palavra_ente=None, t_inter_fp_substantivo_lematizado=None, t_inter_fp_numero=None,
        t_inter_fp_tipo_feminino_ao=None, t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
        t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
        t_inter_fp_tonicidade=None, t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None,
        t_inter_fp_adjetivo_epiteto=None, t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None,
        t_inter_fp_numero_adjetivo=None, t_inter_fp_contracao=None,
        #
        # 		#
        t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        t_text_tem_tema_textual='-', t_text_tipo_insercao_cont="inserção_menu", t_text_conj_extenso_Cont=None,
        t_text_indiceCont=None,
        t_text_tipo_insercao_Conj="inserção_menu", t_text_tipo_de_conjuncao_Conj=None, t_text_conj_extensoConj=None,
        t_text_indiceConj=None,
        t_text_tipo_insercao_Rel='inserção_menu', t_text_pron_extenso_Rel=None, t_text_tipo_de_relativo=None,
        t_text_tipo_pronome_relativo=None, t_text_generoTemaTextual=None, t_text_numeroTemaTextual=None,
        t_text_indice_relacionalativo=None,
        t_text_indice_relacionalativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,
        ##Parâmetors específicos do Processo Mental
        # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
        ##Parâmetors específicos do processo material
        # iniciador
        INICIADOR=None,

        RESULTADO_QUALITATIVO=None, realizacao_atributo=None,
        # realizado por adjetivo
        AtributoAdjModificacao=None, AtributoAdjetivo_lematizado=None, AtributoGenero=None, AtributoNumero=None,
        # realizado por frase preposicional
        ATRIB_indicePreposicao=None, ATRIB_dissoc_ente_nucleo=None, ATRIB_tem_qualificador=None,
        ATRIB_tipo_qualificador=None, ATRIB_determinacao_especificidade_beta=None, ATRIB_orientacao_beta=None,
        ATRIB_genero_beta=None, ATRIB_numero_beta=None, ATRIB_morfologia_do_pronome_beta=None,
        ATRIB_determinacao_especificidade_alpha=None, ATRIB_orientacao_alpha=None, ATRIB_genero_alpha=None,
        ATRIB_numero_alpha=None, ATRIB_morfologia_do_pronome_alpha=None, ATRIB_pessoa_da_interlocucao_possuidor=None,
        ATRIB_numero_obj_possuido=None, ATRIB_genero_obj_possuido=None, ATRIB_pessoa_da_interlocucao_proximidade=None,
        ATRIB_funcao_numerativo=None, ATRIB_cardinal=None, ATRIB_genero=None, ATRIB_tipo_precisa=None,
        ATRIB_tipo_real_card=None, ATRIB_milharExtenso=None, ATRIB_centenaExtenso=None, ATRIB_dezenaExtenso=None,
        ATRIB_unidadeExtenso=None, ATRIB_numIndefinido=None, ATRIB_tipo_de_ente=None, ATRIB_tipo_de_nao_consciente=None,
        ATRIB_tipo_de_nao_consciente_material=None, ATRIB_tipo_de_nao_consciente_semiotico=None,
        ATRIB_classe_palavra_ente=None, ATRIB_substantivo_lematizado=None, ATRIB_numero=None,
        ATRIB_tipo_feminino_ao=None, ATRIB_tipo_masc_ao=None, ATRIB_acent_tonica=None, ATRIB_nome_proprio=None,
        ATRIB_pessoa_da_interlocucao=None, ATRIB_transitividade_verbo=None, ATRIB_tonicidade=None,
        ATRIB_morfologia_do_pronome=None, ATRIB_reflexivo=None, ATRIB_adjetivo_epiteto=None,
        ATRIB_adjetivo_classificador=None, ATRIB_genero_adjetivo=None, ATRIB_numero_adjetivo=None, ATRIB_contracao=None,
        # ESCOPO
        ESCOPO=None,
        # locativo
        LOCATIVO=None,
        ##extensão beneficiarios
        BENEFICIARIO=None,

        ##Processo
        tipo_de_experiencia_gv=None, agencia=None, tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex=None, funcao_no_grupo_verbal_pos_final=None,
        verbo_lex=None, tipo_de_orientacao_lex=None, oi_numero_lex=None, genero_lex=None, oi_tipo_de_pessoa_lex=None,
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
        p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_funcao_numerativo=None,
        p1_cardinal=None, p1_genero=None, p1_tipo_precisa=None, p1_tipo_real_card=None, p1_milharExtenso=None,
        p1_centenaExtenso=None, p1_dezenaExtenso=None, p1_unidadeExtenso=None, p1_numIndefinido=None,
        p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
        p1_numero=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None, p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
        p1_reflexivo=None, p1_adjetivo_epiteto=None, p1_adjetivo_classificador=None, p1_genero_adjetivo=None,
        p1_numero_adjetivo=None, p1_contracao=None,
        ##PARTICIPANTE P1 REALIZADOS POR FP
        p1_FP_indice_preposicao_frase=None, p1_FP_dissoc_ente_nucleo=None, p1_FP_tem_qualificador=None,
        p1_FP_tipo_qualificador=None, p1_FP_indice_preposicao_qualif=None, p1_FP_determinacao_especificidade_beta=None,
        p1_FP_orientacao_beta=None, p1_FP_genero_beta=None, p1_FP_numero_beta=None,
        p1_FP_morfologia_do_pronome_beta=None, p1_FP_determinacao_especificidade_alpha=None,
        p1_FP_orientacao_alpha=None, p1_FP_genero_alpha=None, p1_FP_numero_alpha=None,
        p1_FP_morfologia_do_pronome_alpha=None, p1_FP_pessoa_da_interlocucao_possuidor=None,
        p1_FP_numero_obj_possuido=None, p1_FP_genero_obj_possuido=None, p1_FP_pessoa_da_interlocucao_proximidade=None,
        p1_FP_funcao_numerativo=None, p1_FP_cardinal=None, p1_FP_genero=None, p1_FP_tipo_precisa=None,
        p1_FP_tipo_real_card=None, p1_FP_milharExtenso=None, p1_FP_centenaExtenso=None, p1_FP_dezenaExtenso=None,
        p1_FP_unidadeExtenso=None, p1_FP_numIndefinido=None, p1_FP_tipo_de_ente=None, p1_FP_tipo_de_nao_consciente=None,
        p1_FP_tipo_de_nao_consciente_material=None, p1_FP_tipo_de_nao_consciente_semiotico=None,
        p1_FP_classe_palavra_ente=None, p1_FP_substantivo_lematizado=None, p1_FP_numero=None,
        p1_FP_tipo_feminino_ao=None, p1_FP_tipo_masc_ao=None, p1_FP_acent_tonica=None, p1_FP_nome_proprio=None,
        p1_FP_pessoa_da_interlocucao=None, p1_FP_transitividade_verbo=None, p1_FP_tonicidade=None,
        p1_FP_morfologia_do_pronome=None, p1_FP_reflexivo=None, p1_FP_adjetivo_epiteto=None,
        p1_FP_adjetivo_classificador=None, p1_FP_genero_adjetivo=None, p1_FP_numero_adjetivo=None, p1_FP_contracao=None,

        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
        p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_funcao_numerativo=None,
        p2_cardinal=None, p2_genero=None, p2_tipo_precisa=None, p2_tipo_real_card=None, p2_milharExtenso=None,
        p2_centenaExtenso=None, p2_dezenaExtenso=None, p2_unidadeExtenso=None, p2_numIndefinido=None,
        p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
        p2_numero=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None, p2_nome_proprio=None,
        p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
        p2_reflexivo=None, p2_adjetivo_epiteto=None, p2_adjetivo_classificador=None, p2_genero_adjetivo=None,
        p2_numero_adjetivo=None, p2_contracao=None,
        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
        p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_funcao_numerativo=None,
        p3_cardinal=None, p3_genero=None, p3_tipo_precisa=None, p3_tipo_real_card=None, p3_milharExtenso=None,
        p3_centenaExtenso=None, p3_dezenaExtenso=None, p3_unidadeExtenso=None, p3_numIndefinido=None,
        p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
        p3_numero=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None, p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None, p3_adjetivo_epiteto=None, p3_adjetivo_classificador=None, p3_genero_adjetivo=None,
        p3_numero_adjetivo=None, p3_contracao=None,

        ##PARTICIPANTE P3 REALIZADOS POR FP
        p3_FP_indice_preposicao_frase=None, p3_FP_dissoc_ente_nucleo=None, p3_FP_tem_qualificador=None,
        p3_FP_tipo_qualificador=None, p3_FP_indice_preposicao_qualif=None, p3_FP_determinacao_especificidade_beta=None,
        p3_FP_orientacao_beta=None, p3_FP_genero_beta=None, p3_FP_numero_beta=None,
        p3_FP_morfologia_do_pronome_beta=None, p3_FP_determinacao_especificidade_alpha=None,
        p3_FP_orientacao_alpha=None, p3_FP_genero_alpha=None, p3_FP_numero_alpha=None,
        p3_FP_morfologia_do_pronome_alpha=None, p3_FP_pessoa_da_interlocucao_possuidor=None,
        p3_FP_numero_obj_possuido=None, p3_FP_genero_obj_possuido=None, p3_FP_pessoa_da_interlocucao_proximidade=None,
        p3_FP_funcao_numerativo=None, p3_FP_cardinal=None, p3_FP_genero=None, p3_FP_tipo_precisa=None,
        p3_FP_tipo_real_card=None, p3_FP_milharExtenso=None, p3_FP_centenaExtenso=None, p3_FP_dezenaExtenso=None,
        p3_FP_unidadeExtenso=None, p3_FP_numIndefinido=None, p3_FP_tipo_de_ente=None, p3_FP_tipo_de_nao_consciente=None,
        p3_FP_tipo_de_nao_consciente_material=None, p3_FP_tipo_de_nao_consciente_semiotico=None,
        p3_FP_classe_palavra_ente=None, p3_FP_substantivo_lematizado=None, p3_FP_numero=None,
        p3_FP_tipo_feminino_ao=None, p3_FP_tipo_masc_ao=None, p3_FP_acent_tonica=None, p3_FP_nome_proprio=None,
        p3_FP_pessoa_da_interlocucao=None, p3_FP_transitividade_verbo=None, p3_FP_tonicidade=None,
        p3_FP_morfologia_do_pronome=None, p3_FP_reflexivo=None, p3_FP_adjetivo_epiteto=None,
        p3_FP_adjetivo_classificador=None, p3_FP_genero_adjetivo=None, p3_FP_numero_adjetivo=None, p3_FP_contracao=None,
        ##CIRCUNSTANCIA
        CIRC_ORACAO_realizacaoCircunstancia=None, CIRC_ORACAO_indice_preposicao_frase=None,
        CIRC_ORACAO_dissoc_ente_nucleo=None, CIRC_ORACAO_tem_qualificador=None, CIRC_ORACAO_tipo_qualificador=None,
        CIRC_ORACAO_indice_preposicao_qualif=None, CIRC_ORACAO_determinacao_especificidade_beta=None,
        CIRC_ORACAO_orientacao_beta=None, CIRC_ORACAO_genero_beta=None, CIRC_ORACAO_numero_beta=None,
        CIRC_ORACAO_morfologia_do_pronome_beta=None, CIRC_ORACAO_determinacao_especificidade_alpha=None,
        CIRC_ORACAO_orientacao_alpha=None, CIRC_ORACAO_genero_alpha=None, CIRC_ORACAO_numero_alpha=None,
        CIRC_ORACAO_morfologia_do_pronome_alpha=None, CIRC_ORACAO_pessoa_da_interlocucao_possuidor=None,
        CIRC_ORACAO_numero_obj_possuido=None, CIRC_ORACAO_genero_obj_possuido=None,
        CIRC_ORACAO_pessoa_da_interlocucao_proximidade=None, CIRC_ORACAO_funcao_numerativo=None,
        CIRC_ORACAO_cardinal=None, CIRC_ORACAO_genero=None, CIRC_ORACAO_tipo_precisa=None,
        CIRC_ORACAO_tipo_real_card=None, CIRC_ORACAO_milharExtenso=None, CIRC_ORACAO_centenaExtenso=None,
        CIRC_ORACAO_dezenaExtenso=None, CIRC_ORACAO_unidadeExtenso=None, CIRC_ORACAO_numIndefinido=None,
        CIRC_ORACAO_tipo_de_ente=None, CIRC_ORACAO_tipo_de_nao_consciente=None,
        CIRC_ORACAO_tipo_de_nao_consciente_material=None, CIRC_ORACAO_tipo_de_nao_consciente_semiotico=None,
        CIRC_ORACAO_classe_palavra_ente=None, CIRC_ORACAO_substantivo_lematizado=None, CIRC_ORACAO_numero=None,
        CIRC_ORACAO_tipo_feminino_ao=None, CIRC_ORACAO_tipo_masc_ao=None, CIRC_ORACAO_acent_tonica=None,
        CIRC_ORACAO_nome_proprio=None, CIRC_ORACAO_pessoa_da_interlocucao=None, CIRC_ORACAO_transitividade_verbo=None,
        CIRC_ORACAO_tonicidade=None, CIRC_ORACAO_morfologia_do_pronome=None, CIRC_ORACAO_reflexivo=None,
        CIRC_ORACAO_adjetivo_epiteto=None, CIRC_ORACAO_adjetivo_classificador=None, CIRC_ORACAO_genero_adjetivo=None,
        CIRC_ORACAO_numero_adjetivo=None, CIRC_ORACAO_contracao=None, CIRC_ORACAO_tipo_de_adverbio1=None,
        CIRC_ORACAO_ind1=None, CIRC_ORACAO_tipo_de_adverbio2=None, CIRC_ORACAO_ind2=None,
        CIRC_ORACAO_tipo_de_adverbio3=None, CIRC_ORACAO_ind3=None, CIRC_ORACAO_tipo_de_adverbio4=None,
        CIRC_ORACAO_ind4=None, CIRC_ORACAO_tipo_de_adverbio5=None, CIRC_ORACAO_ind5=None
):
    try:
        transitividade_ = transitividade(TIPO_DE_PROCESSO, indice_material, indice_agenciamento, indice_relacional, indice_atrib)
        Modo = modo(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = tema_interpessoal(TIPO_TEMA_INTERPESSOAL, t_inter_tipoRealizacao, t_inter_tipo_de_adverbio1,
                                              t_inter_ind1, t_inter_tipo_de_adverbio2, t_inter_ind2,
                                              t_inter_tipo_de_adverbio3, t_inter_ind3, t_inter_tipo_de_adverbio4,
                                              t_inter_ind4, t_inter_tipo_de_adverbio5, t_inter_ind5,
                                              t_inter_fp_indice_preposicao_frase, t_inter_fp_dissoc_ente_nucleo,
                                              t_inter_fp_tem_qualificador, t_inter_fp_tipo_qualificador,
                                              t_inter_fp_indice_preposicao_qualif,
                                              t_inter_fp_determinacao_especificidade_beta, t_inter_fp_orientacao_beta,
                                              t_inter_fp_genero_beta, t_inter_fp_numero_beta,
                                              t_inter_fp_morfologia_do_pronome_beta,
                                              t_inter_fp_determinacao_especificidade_alpha, t_inter_fp_orientacao_alpha,
                                              t_inter_fp_genero_alpha, t_inter_fp_numero_alpha,
                                              t_inter_fp_morfologia_do_pronome_alpha,
                                              t_inter_fp_pessoa_da_interlocucao_possuidor,
                                              t_inter_fp_numero_obj_possuido, t_inter_fp_genero_obj_possuido,
                                              t_inter_fp_pessoa_da_interlocucao_proximidade,
                                              t_inter_fp_funcao_numerativo, t_inter_fp_cardinal, t_inter_fp_genero,
                                              t_inter_fp_tipo_precisa, t_inter_fp_tipo_real_card,
                                              t_inter_fp_milharExtenso, t_inter_fp_centenaExtenso,
                                              t_inter_fp_dezenaExtenso, t_inter_fp_unidadeExtenso,
                                              t_inter_fp_numIndefinido, t_inter_fp_tipo_de_ente,
                                              t_inter_fp_tipo_de_nao_consciente,
                                              t_inter_fp_tipo_de_nao_consciente_material,
                                              t_inter_fp_tipo_de_nao_consciente_semiotico,
                                              t_inter_fp_classe_palavra_ente, t_inter_fp_substantivo_lematizado,
                                              t_inter_fp_numero, t_inter_fp_tipo_feminino_ao, t_inter_fp_tipo_masc_ao,
                                              t_inter_fp_acent_tonica, t_inter_fp_nome_proprio,
                                              t_inter_fp_pessoa_da_interlocucao, t_inter_fp_transitividade_verbo,
                                              t_inter_fp_tonicidade, t_inter_fp_morfologia_do_pronome,
                                              t_inter_fp_reflexivo, t_inter_fp_adjetivo_epiteto,
                                              t_inter_fp_adjetivo_classificador, t_inter_fp_genero_adjetivo,
                                              t_inter_fp_numero_adjetivo, t_inter_fp_contracao, t_inter_indice_elem_qu,
                                              t_inter_indice_part_modal, t_inter_nome_proprio)
        Tema_textual = tema_textual(t_text_tem_tema_textual, t_text_tipo_insercao_cont, t_text_indiceCont,
                                    t_text_tipo_de_conjuncao_Conj, t_text_conj_extensoConj, t_text_indiceConj,
                                    t_text_tipo_insercao_Rel, t_text_pron_extenso_Rel, t_text_tipo_de_relativo,
                                    t_text_tipo_pronome_relativo, t_text_generoTemaTextual, t_text_numeroTemaTextual)
        tema_id = tema_ideacional(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        polar = polaridade(tipo_polaridade)
        Processo = grupo_verbal(tipo_de_experiencia_gv, agencia, tipo_de_experiencia_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, oi_numero_1, genero_1, oi_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, tipo_de_experiencia_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, oi_numero_2, genero_2, oi_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, tipo_de_experiencia_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, oi_numero_3, genero_3, oi_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, tipo_de_experiencia_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, oi_numero_4, genero_4, oi_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final,
                                verbo_lex, tipo_de_orientacao_lex, oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                padrao_pessoa_morfologia_lex)
        Circunstancia = circunstancia(CIRC_ORACAO_realizacaoCircunstancia, CIRC_ORACAO_indice_preposicao_frase,
                                      CIRC_ORACAO_dissoc_ente_nucleo, CIRC_ORACAO_tem_qualificador,
                                      CIRC_ORACAO_tipo_qualificador, CIRC_ORACAO_indice_preposicao_qualif,
                                      CIRC_ORACAO_determinacao_especificidade_beta, CIRC_ORACAO_orientacao_beta,
                                      CIRC_ORACAO_genero_beta, CIRC_ORACAO_numero_beta,
                                      CIRC_ORACAO_morfologia_do_pronome_beta,
                                      CIRC_ORACAO_determinacao_especificidade_alpha, CIRC_ORACAO_orientacao_alpha,
                                      CIRC_ORACAO_genero_alpha, CIRC_ORACAO_numero_alpha,
                                      CIRC_ORACAO_morfologia_do_pronome_alpha,
                                      CIRC_ORACAO_pessoa_da_interlocucao_possuidor, CIRC_ORACAO_numero_obj_possuido,
                                      CIRC_ORACAO_genero_obj_possuido, CIRC_ORACAO_pessoa_da_interlocucao_proximidade,
                                      cardinal=CIRC_ORACAO_cardinal, genero_numerativo=CIRC_ORACAO_numIndefinido,
                                      tipo_de_ente=CIRC_ORACAO_tipo_de_ente,
                                      tipo_de_nao_consciente=CIRC_ORACAO_tipo_de_nao_consciente,
                                      tipo_de_nao_consciente_material=CIRC_ORACAO_tipo_de_nao_consciente_material,
                                      tipo_de_nao_consciente_semiotico=CIRC_ORACAO_tipo_de_nao_consciente_semiotico,
                                      classe_palavra_ente=CIRC_ORACAO_classe_palavra_ente,
                                      substantivo_lematizado=CIRC_ORACAO_substantivo_lematizado,
                                      numero=CIRC_ORACAO_numero, tipo_feminino_ao=CIRC_ORACAO_tipo_feminino_ao,
                                      tipo_masc_ao=CIRC_ORACAO_tipo_masc_ao, acent_tonica=CIRC_ORACAO_acent_tonica,
                                      nome_prop=CIRC_ORACAO_nome_proprio,
                                      pessoa_da_interlocucao=CIRC_ORACAO_pessoa_da_interlocucao,
                                      transitividade_verbo=CIRC_ORACAO_transitividade_verbo,
                                      tonicidade=CIRC_ORACAO_tonicidade,
                                      morfologia_do_pronome=CIRC_ORACAO_morfologia_do_pronome,
                                      reflexivo=CIRC_ORACAO_reflexivo, adjetivo_epiteto=CIRC_ORACAO_adjetivo_epiteto,
                                      adjetivo_classificador=CIRC_ORACAO_adjetivo_classificador,
                                      genero_adjetivo=CIRC_ORACAO_genero_adjetivo,
                                      numero_adjetivo=CIRC_ORACAO_numero_adjetivo, contracao=CIRC_ORACAO_contracao,
                                      tipo_de_adverbio1=CIRC_ORACAO_tipo_de_adverbio1, ind1=CIRC_ORACAO_ind1,
                                      tipo_de_adverbio2=CIRC_ORACAO_tipo_de_adverbio2, ind2=CIRC_ORACAO_ind2,
                                      tipo_de_adverbio3=CIRC_ORACAO_tipo_de_adverbio3, ind3=CIRC_ORACAO_ind3,
                                      tipo_de_adverbio4=CIRC_ORACAO_tipo_de_adverbio4, ind4=CIRC_ORACAO_ind4,
                                      tipo_de_adverbio5=CIRC_ORACAO_tipo_de_adverbio5, ind5=CIRC_ORACAO_ind5)

        if transitividade_ == 'PR_material_transformativo_IMPA_intransitivo_AG_efetivo_operativo':
            # NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDENS DE AGENTES
            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

            INICIADOR = '+iniciador'
            Iniciador = estrutura_gn(p3_dissoc_ente_nucleo, p3_tem_qualificador, p3_tipo_qualificador,
                                     p3_indice_preposicao_qualif, p3_determinacao_especificidade_beta,
                                     p3_orientacao_beta, p3_genero_beta, p3_numero_beta, p3_morfologia_do_pronome_beta,
                                     p3_determinacao_especificidade_alpha, p3_orientacao_alpha, p3_genero_alpha,
                                     p3_numero_alpha, p3_morfologia_do_pronome_alpha,
                                     p3_pessoa_da_interlocucao_possuidor, p3_numero_obj_possuido,
                                     p3_genero_obj_possuido, p3_pessoa_da_interlocucao_proximidade,
                                     p3_funcao_numerativo, p3_cardinal, p3_genero, p3_tipo_precisa, p3_tipo_real_card,
                                     p3_milharExtenso, p3_centenaExtenso, p3_dezenaExtenso, p3_unidadeExtenso,
                                     p3_numIndefinido, p3_tipo_de_ente, p3_tipo_de_nao_consciente,
                                     p3_tipo_de_nao_consciente_material, p3_tipo_de_nao_consciente_semiotico,
                                     p3_classe_palavra_ente, p3_substantivo_lematizado, p3_numero, p3_tipo_feminino_ao,
                                     p3_tipo_masc_ao, p3_acent_tonica, p3_nome_proprio, p3_pessoa_da_interlocucao,
                                     p3_transitividade_verbo, p3_tonicidade, p3_morfologia_do_pronome)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                  p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                  p3_FP_indice_preposicao_qualif,
                                                  p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                  p3_FP_genero_beta, p3_FP_numero_beta,
                                                  p3_FP_morfologia_do_pronome_beta,
                                                  p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                  p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                  p3_FP_morfologia_do_pronome_alpha,
                                                  p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                  p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                  p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                  p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                  p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                  p3_FP_numIndefinido, p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                  p3_FP_tipo_de_nao_consciente_material,
                                                  p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                  p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                  p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                  p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                  p3_FP_tonicidade)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                   p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                   p3_FP_indice_preposicao_qualif,
                                                   p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                   p3_FP_genero_beta, p3_FP_numero_beta,
                                                   p3_FP_morfologia_do_pronome_beta,
                                                   p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                   p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                   p3_FP_morfologia_do_pronome_alpha,
                                                   p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                   p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                   p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                   p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                   p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                   p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                                   p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                                   p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                   p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                   p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                   p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                   p3_FP_tonicidade)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Iniciador, polar, Processo, Ator, Locativo, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Iniciador, polar, Processo, Ator, Locativo, Cliente + '?'))


        elif transitividade_ == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance':
            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            INICIADOR == '-iniciador'
            Iniciador = ''
            oracao = Ator + ' ' + polar + ' ' + Processo
            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                  p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                  p3_FP_indice_preposicao_qualif,
                                                  p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                  p3_FP_genero_beta, p3_FP_numero_beta,
                                                  p3_FP_morfologia_do_pronome_beta,
                                                  p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                  p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                  p3_FP_morfologia_do_pronome_alpha,
                                                  p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                  p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                  p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                  p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                  p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                  p3_FP_numIndefinido, p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                  p3_FP_tipo_de_nao_consciente_material,
                                                  p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                  p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                  p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                  p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                  p3_FP_tonicidade)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                   p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                   p3_FP_indice_preposicao_qualif,
                                                   p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                   p3_FP_genero_beta, p3_FP_numero_beta,
                                                   p3_FP_morfologia_do_pronome_beta,
                                                   p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                   p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                   p3_FP_morfologia_do_pronome_alpha,
                                                   p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                   p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                   p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                   p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                   p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                   p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                                   p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                                   p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                   p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                   p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                   p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                   p3_FP_tonicidade)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((oracao, Locativo, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((oracao, Locativo, Cliente + '?'))

        elif transitividade_ == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance':
            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

            try:
                if ESCOPO == '+escopo':
                    Escopo = estrutura_gn(p3_dissoc_ente_nucleo, p3_tem_qualificador, p3_tipo_qualificador,
                                          p3_indice_preposicao_qualif, p3_determinacao_especificidade_beta,
                                          p3_orientacao_beta, p3_genero_beta, p3_numero_beta,
                                          p3_morfologia_do_pronome_beta, p3_determinacao_especificidade_alpha,
                                          p3_orientacao_alpha, p3_genero_alpha, p3_numero_alpha,
                                          p3_morfologia_do_pronome_alpha, p3_pessoa_da_interlocucao_possuidor,
                                          p3_numero_obj_possuido, p3_genero_obj_possuido,
                                          p3_pessoa_da_interlocucao_proximidade, p3_funcao_numerativo, p3_cardinal,
                                          p3_genero, p3_tipo_precisa, p3_tipo_real_card, p3_milharExtenso,
                                          p3_centenaExtenso, p3_dezenaExtenso, p3_unidadeExtenso, p3_numIndefinido,
                                          p3_tipo_de_ente, p3_tipo_de_nao_consciente,
                                          p3_tipo_de_nao_consciente_material, p3_tipo_de_nao_consciente_semiotico,
                                          p3_classe_palavra_ente, p3_substantivo_lematizado, p3_numero,
                                          p3_tipo_feminino_ao, p3_tipo_masc_ao, p3_acent_tonica, p3_nome_proprio,
                                          p3_pessoa_da_interlocucao, p3_transitividade_verbo, p3_tonicidade,
                                          p3_morfologia_do_pronome)

                elif ESCOPO == '-escopo':
                    Escopo = ''
            except:
                Escopo = ''

            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                   p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                   p3_FP_indice_preposicao_qualif,
                                                   p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                   p3_FP_genero_beta, p3_FP_numero_beta,
                                                   p3_FP_morfologia_do_pronome_beta,
                                                   p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                   p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                   p3_FP_morfologia_do_pronome_alpha,
                                                   p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                   p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                   p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                   p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                   p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                   p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                                   p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                                   p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                   p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                   p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                   p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                   p3_FP_tonicidade)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Escopo, Locativo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Escopo, Locativo + '?'))

        elif transitividade_ == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance':

            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo + '?'))

        elif transitividade_ == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo':
            # NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDENS DE AGENTES
            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            Meta = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                p2_numero_obj_possuido, p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

            try:
                if RESULTADO_QUALITATIVO == 'resultado_atributo' or RESULTADO_QUALITATIVO == 'resultado_papel(produto)':
                    if realizacao_atributo == 'atributo_adjetivo':
                        Atributo = adjetivo(AtributoAdjetivo_lematizado, AtributoGenero, AtributoNumero)
                    elif realizacao_atributo == 'atributo_frase_preposicional':
                        Atributo = frase_preposicional(ATRIB_indicePreposicao, ATRIB_dissoc_ente_nucleo,
                                                       ATRIB_tem_qualificador, ATRIB_tipo_qualificador,
                                                       ATRIB_determinacao_especificidade_beta, ATRIB_orientacao_beta,
                                                       ATRIB_genero_beta, ATRIB_numero_beta,
                                                       ATRIB_morfologia_do_pronome_beta,
                                                       ATRIB_determinacao_especificidade_alpha, ATRIB_orientacao_alpha,
                                                       ATRIB_genero_alpha, ATRIB_numero_alpha,
                                                       ATRIB_morfologia_do_pronome_alpha,
                                                       ATRIB_pessoa_da_interlocucao_possuidor,
                                                       ATRIB_numero_obj_possuido, ATRIB_genero_obj_possuido,
                                                       ATRIB_pessoa_da_interlocucao_proximidade,
                                                       ATRIB_funcao_numerativo, ATRIB_cardinal, ATRIB_genero,
                                                       ATRIB_tipo_precisa, ATRIB_tipo_real_card, ATRIB_milharExtenso,
                                                       ATRIB_centenaExtenso, ATRIB_dezenaExtenso, ATRIB_unidadeExtenso,
                                                       ATRIB_numIndefinido, ATRIB_tipo_de_ente,
                                                       ATRIB_tipo_de_nao_consciente,
                                                       ATRIB_tipo_de_nao_consciente_material,
                                                       ATRIB_tipo_de_nao_consciente_semiotico,
                                                       ATRIB_classe_palavra_ente, ATRIB_substantivo_lematizado,
                                                       ATRIB_numero, ATRIB_tipo_feminino_ao, ATRIB_tipo_masc_ao,
                                                       ATRIB_acent_tonica, ATRIB_nome_proprio,
                                                       ATRIB_pessoa_da_interlocucao, ATRIB_transitividade_verbo,
                                                       ATRIB_tonicidade, ATRIB_morfologia_do_pronome)
                elif RESULTADO_QUALITATIVO == '-resultado':
                    Atributo = ''
            except:
                Atributo = ''

            try:
                if BENEFICIARIO == '+recipiente':
                    Recipiente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                     p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                     p3_FP_indice_preposicao_qualif,
                                                     p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                     p3_FP_genero_beta, p3_FP_numero_beta,
                                                     p3_FP_morfologia_do_pronome_beta,
                                                     p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                     p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                     p3_FP_morfologia_do_pronome_alpha,
                                                     p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                     p3_FP_genero_obj_possuido,
                                                     p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                                     p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa,
                                                     p3_FP_tipo_real_card, p3_FP_milharExtenso, p3_FP_centenaExtenso,
                                                     p3_FP_dezenaExtenso, p3_FP_unidadeExtenso, p3_FP_numIndefinido,
                                                     p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                     p3_FP_tipo_de_nao_consciente_material,
                                                     p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                     p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                     p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                     p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                     p3_FP_tonicidade)
                elif BENEFICIARIO == '-recipiente':
                    Recipiente = ''
            except:
                Recipiente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                   p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                   p3_FP_indice_preposicao_qualif,
                                                   p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                   p3_FP_genero_beta, p3_FP_numero_beta,
                                                   p3_FP_morfologia_do_pronome_beta,
                                                   p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                   p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                   p3_FP_morfologia_do_pronome_alpha,
                                                   p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                   p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                   p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                   p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                   p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                   p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                                   p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                                   p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                   p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                   p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                   p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                   p3_FP_tonicidade)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Meta, Atributo, Locativo, Recipiente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Meta, Atributo, Locativo, Recipiente + '?'))

        elif transitividade_ == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo':

            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            Meta = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                p2_numero_obj_possuido, p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                  p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                  p3_FP_indice_preposicao_qualif,
                                                  p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                  p3_FP_genero_beta, p3_FP_numero_beta,
                                                  p3_FP_morfologia_do_pronome_beta,
                                                  p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                  p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                  p3_FP_morfologia_do_pronome_alpha,
                                                  p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                  p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                  p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                  p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                  p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                  p3_FP_numIndefinido, p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                  p3_FP_tipo_de_nao_consciente_material,
                                                  p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                  p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                  p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                  p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                  p3_FP_tonicidade)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Meta, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Meta, Cliente + '?'))

        ##MATERIAL METEOROLÓGICA
        elif transitividade_ == 'PR_material_transformativo_IMPA_intransitivo_AG_processo_com_alcance':
            Escopo = estrutura_gn(p3_dissoc_ente_nucleo, p3_tem_qualificador, p3_tipo_qualificador,
                                  p3_indice_preposicao_qualif, p3_determinacao_especificidade_beta, p3_orientacao_beta,
                                  p3_genero_beta, p3_numero_beta, p3_morfologia_do_pronome_beta,
                                  p3_determinacao_especificidade_alpha, p3_orientacao_alpha, p3_genero_alpha,
                                  p3_numero_alpha, p3_morfologia_do_pronome_alpha, p3_pessoa_da_interlocucao_possuidor,
                                  p3_numero_obj_possuido, p3_genero_obj_possuido, p3_pessoa_da_interlocucao_proximidade,
                                  p3_funcao_numerativo, p3_cardinal, p3_genero, p3_tipo_precisa, p3_tipo_real_card,
                                  p3_milharExtenso, p3_centenaExtenso, p3_dezenaExtenso, p3_unidadeExtenso,
                                  p3_numIndefinido, p3_tipo_de_ente, p3_tipo_de_nao_consciente,
                                  p3_tipo_de_nao_consciente_material, p3_tipo_de_nao_consciente_semiotico,
                                  p3_classe_palavra_ente, p3_substantivo_lematizado, p3_numero, p3_tipo_feminino_ao,
                                  p3_tipo_masc_ao, p3_acent_tonica, p3_nome_proprio, p3_pessoa_da_interlocucao,
                                  p3_transitividade_verbo, p3_tonicidade, p3_morfologia_do_pronome)

            if Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Processo, Escopo + '.'))
            elif Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Processo, Escopo + '?'))

        elif transitividade_ == 'PR_material_transformativo_IMPA_intransitivo_AG_processo_sem_alcance':
            if Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = Processo + '.'
            elif Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = Processo + '?'

        # 		##########COMEÇO DE AGENCIAMENTO PASSIVA
        #
        #
        elif transitividade_ == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo':

            Ator = frase_preposicional(p1_FP_indice_preposicao_frase, p1_FP_dissoc_ente_nucleo, p1_FP_tem_qualificador,
                                       p1_FP_tipo_qualificador, p1_FP_indice_preposicao_qualif,
                                       p1_FP_determinacao_especificidade_beta, p1_FP_orientacao_beta, p1_FP_genero_beta,
                                       p1_FP_numero_beta, p1_FP_morfologia_do_pronome_beta,
                                       p1_FP_determinacao_especificidade_alpha, p1_FP_orientacao_alpha,
                                       p1_FP_genero_alpha, p1_FP_numero_alpha, p1_FP_morfologia_do_pronome_alpha,
                                       p1_FP_pessoa_da_interlocucao_possuidor, p1_FP_numero_obj_possuido,
                                       p1_FP_genero_obj_possuido, p1_FP_pessoa_da_interlocucao_proximidade,
                                       p1_FP_funcao_numerativo, p1_FP_cardinal, p1_FP_genero, p1_FP_tipo_precisa,
                                       p1_FP_tipo_real_card, p1_FP_milharExtenso, p1_FP_centenaExtenso,
                                       p1_FP_dezenaExtenso, p1_FP_unidadeExtenso, p1_FP_numIndefinido,
                                       p1_FP_tipo_de_ente, p1_FP_tipo_de_nao_consciente,
                                       p1_FP_tipo_de_nao_consciente_material, p1_FP_tipo_de_nao_consciente_semiotico,
                                       p1_FP_classe_palavra_ente, p1_FP_substantivo_lematizado, p1_FP_numero,
                                       p1_FP_tipo_feminino_ao, p1_FP_tipo_masc_ao, p1_FP_acent_tonica,
                                       p1_FP_nome_proprio, p1_FP_pessoa_da_interlocucao, p1_FP_transitividade_verbo,
                                       p1_FP_tonicidade)
            Meta = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                p2_numero_obj_possuido, p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

            try:
                if RESULTADO_QUALITATIVO == 'resultado_atributo' or RESULTADO_QUALITATIVO == 'resultado_papel(produto)':
                    if realizacao_atributo == 'atributo_adjetivo':
                        Atributo = adjetivo(AtributoAdjetivo_lematizado, AtributoGenero, AtributoNumero)
                    elif realizacao_atributo == 'atributo_frase_preposicional':
                        Atributo = frase_preposicional(ATRIB_indicePreposicao, ATRIB_dissoc_ente_nucleo,
                                                       ATRIB_tem_qualificador, ATRIB_tipo_qualificador,
                                                       ATRIB_determinacao_especificidade_beta, ATRIB_orientacao_beta,
                                                       ATRIB_genero_beta, ATRIB_numero_beta,
                                                       ATRIB_morfologia_do_pronome_beta,
                                                       ATRIB_determinacao_especificidade_alpha, ATRIB_orientacao_alpha,
                                                       ATRIB_genero_alpha, ATRIB_numero_alpha,
                                                       ATRIB_morfologia_do_pronome_alpha,
                                                       ATRIB_pessoa_da_interlocucao_possuidor,
                                                       ATRIB_numero_obj_possuido, ATRIB_genero_obj_possuido,
                                                       ATRIB_pessoa_da_interlocucao_proximidade,
                                                       ATRIB_funcao_numerativo, ATRIB_cardinal, ATRIB_genero,
                                                       ATRIB_tipo_precisa, ATRIB_tipo_real_card, ATRIB_milharExtenso,
                                                       ATRIB_centenaExtenso, ATRIB_dezenaExtenso, ATRIB_unidadeExtenso,
                                                       ATRIB_numIndefinido, ATRIB_tipo_de_ente,
                                                       ATRIB_tipo_de_nao_consciente,
                                                       ATRIB_tipo_de_nao_consciente_material,
                                                       ATRIB_tipo_de_nao_consciente_semiotico,
                                                       ATRIB_classe_palavra_ente, ATRIB_substantivo_lematizado,
                                                       ATRIB_numero, ATRIB_tipo_feminino_ao, ATRIB_tipo_masc_ao,
                                                       ATRIB_acent_tonica, ATRIB_nome_proprio,
                                                       ATRIB_pessoa_da_interlocucao, ATRIB_transitividade_verbo,
                                                       ATRIB_tonicidade, ATRIB_morfologia_do_pronome)
                elif RESULTADO_QUALITATIVO == '-resultado':
                    Atributo = ''
            except:
                Atributo = ''

            try:
                if BENEFICIARIO == '+recipiente':
                    Recipiente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                     p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                     p3_FP_indice_preposicao_qualif,
                                                     p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                     p3_FP_genero_beta, p3_FP_numero_beta,
                                                     p3_FP_morfologia_do_pronome_beta,
                                                     p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                     p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                     p3_FP_morfologia_do_pronome_alpha,
                                                     p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                     p3_FP_genero_obj_possuido,
                                                     p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                                     p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa,
                                                     p3_FP_tipo_real_card, p3_FP_milharExtenso, p3_FP_centenaExtenso,
                                                     p3_FP_dezenaExtenso, p3_FP_unidadeExtenso, p3_FP_numIndefinido,
                                                     p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                     p3_FP_tipo_de_nao_consciente_material,
                                                     p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                     p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                     p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                     p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                     p3_FP_tonicidade)
                elif BENEFICIARIO == '-recipiente':
                    Recipiente = ''
                else:
                    Recipiente = ''
            except:
                Recipiente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                   p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                   p3_FP_indice_preposicao_qualif,
                                                   p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                   p3_FP_genero_beta, p3_FP_numero_beta,
                                                   p3_FP_morfologia_do_pronome_beta,
                                                   p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                   p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                   p3_FP_morfologia_do_pronome_alpha,
                                                   p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                   p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                   p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                   p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                   p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                   p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                                   p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                                   p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                   p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                   p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                   p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                   p3_FP_tonicidade)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, polar, Processo, Atributo, Ator, Locativo, Recipiente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, polar, Processo, Atributo, Ator, Locativo, Recipiente + '?'))

        ######################################################################
        elif transitividade_ == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo':

            Ator = frase_preposicional(p1_FP_indice_preposicao_frase, p1_FP_dissoc_ente_nucleo, p1_FP_tem_qualificador,
                                       p1_FP_tipo_qualificador, p1_FP_indice_preposicao_qualif,
                                       p1_FP_determinacao_especificidade_beta, p1_FP_orientacao_beta, p1_FP_genero_beta,
                                       p1_FP_numero_beta, p1_FP_morfologia_do_pronome_beta,
                                       p1_FP_determinacao_especificidade_alpha, p1_FP_orientacao_alpha,
                                       p1_FP_genero_alpha, p1_FP_numero_alpha, p1_FP_morfologia_do_pronome_alpha,
                                       p1_FP_pessoa_da_interlocucao_possuidor, p1_FP_numero_obj_possuido,
                                       p1_FP_genero_obj_possuido, p1_FP_pessoa_da_interlocucao_proximidade,
                                       p1_FP_funcao_numerativo, p1_FP_cardinal, p1_FP_genero, p1_FP_tipo_precisa,
                                       p1_FP_tipo_real_card, p1_FP_milharExtenso, p1_FP_centenaExtenso,
                                       p1_FP_dezenaExtenso, p1_FP_unidadeExtenso, p1_FP_numIndefinido,
                                       p1_FP_tipo_de_ente, p1_FP_tipo_de_nao_consciente,
                                       p1_FP_tipo_de_nao_consciente_material, p1_FP_tipo_de_nao_consciente_semiotico,
                                       p1_FP_classe_palavra_ente, p1_FP_substantivo_lematizado, p1_FP_numero,
                                       p1_FP_tipo_feminino_ao, p1_FP_tipo_masc_ao, p1_FP_acent_tonica,
                                       p1_FP_nome_proprio, p1_FP_pessoa_da_interlocucao, p1_FP_transitividade_verbo,
                                       p1_FP_tonicidade)
            Meta = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                p2_numero_obj_possuido, p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                  p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                  p3_FP_indice_preposicao_qualif,
                                                  p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                  p3_FP_genero_beta, p3_FP_numero_beta,
                                                  p3_FP_morfologia_do_pronome_beta,
                                                  p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                  p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                  p3_FP_morfologia_do_pronome_alpha,
                                                  p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                  p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                  p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                  p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                  p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                  p3_FP_numIndefinido, p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                  p3_FP_tipo_de_nao_consciente_material,
                                                  p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                  p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                  p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                  p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                  p3_FP_tonicidade)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, polar, Processo, Ator, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, polar, Processo, Ator, Cliente + '?'))

        elif transitividade_ == 'PR_material_transformativo_IMPA_intransitivo_AG_efetivo_receptivo':
            # NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDEM DE AGENTES
            Ator = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

            INICIADOR = '+iniciador'
            Iniciador = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                            p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                            p3_FP_indice_preposicao_qualif, p3_FP_determinacao_especificidade_beta,
                                            p3_FP_orientacao_beta, p3_FP_genero_beta, p3_FP_numero_beta,
                                            p3_FP_morfologia_do_pronome_beta, p3_FP_determinacao_especificidade_alpha,
                                            p3_FP_orientacao_alpha, p3_FP_genero_alpha, p3_FP_numero_alpha,
                                            p3_FP_morfologia_do_pronome_alpha, p3_FP_pessoa_da_interlocucao_possuidor,
                                            p3_FP_numero_obj_possuido, p3_FP_genero_obj_possuido,
                                            p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                            p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa, p3_FP_tipo_real_card,
                                            p3_FP_milharExtenso, p3_FP_centenaExtenso, p3_FP_dezenaExtenso,
                                            p3_FP_unidadeExtenso, p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                            p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                            p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                            p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                            p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                            p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo, p3_FP_tonicidade)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                  p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                  p3_FP_indice_preposicao_qualif,
                                                  p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                  p3_FP_genero_beta, p3_FP_numero_beta,
                                                  p3_FP_morfologia_do_pronome_beta,
                                                  p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                  p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                  p3_FP_morfologia_do_pronome_alpha,
                                                  p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                  p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                  p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                  p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                  p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                  p3_FP_numIndefinido, p3_FP_tipo_de_ente, p3_FP_tipo_de_nao_consciente,
                                                  p3_FP_tipo_de_nao_consciente_material,
                                                  p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                  p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                  p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                  p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                  p3_FP_tonicidade)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                                   p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                                   p3_FP_indice_preposicao_qualif,
                                                   p3_FP_determinacao_especificidade_beta, p3_FP_orientacao_beta,
                                                   p3_FP_genero_beta, p3_FP_numero_beta,
                                                   p3_FP_morfologia_do_pronome_beta,
                                                   p3_FP_determinacao_especificidade_alpha, p3_FP_orientacao_alpha,
                                                   p3_FP_genero_alpha, p3_FP_numero_alpha,
                                                   p3_FP_morfologia_do_pronome_alpha,
                                                   p3_FP_pessoa_da_interlocucao_possuidor, p3_FP_numero_obj_possuido,
                                                   p3_FP_genero_obj_possuido, p3_FP_pessoa_da_interlocucao_proximidade,
                                                   p3_FP_funcao_numerativo, p3_FP_cardinal, p3_FP_genero,
                                                   p3_FP_tipo_precisa, p3_FP_tipo_real_card, p3_FP_milharExtenso,
                                                   p3_FP_centenaExtenso, p3_FP_dezenaExtenso, p3_FP_unidadeExtenso,
                                                   p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                                   p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                                   p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                                   p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                                   p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                                   p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                                   p3_FP_tonicidade)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Locativo, Iniciador, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, polar, Processo, Locativo, Iniciador, Cliente + '?'))

        return (re.sub(' +', ' ', oracao).strip().capitalize())
    except:
        return ""


##ORACAO RELACIONAL
#
# print('Qual o tipo_pessoa de especificação de associação?')
# especificacao_associacao = choice.Menu(['entidade', 'qualidade']).ask()
# print('Qual a fase da atribuição?')
# fase_atribuicao = choice.Menu(['neutra',
# 							   'faseada']).ask()  ##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
# ###não vou especializar os tipos de fase.
# print('Qual o domínio da atribuição')
# dominio_atribuicao = choice.Menu(['material', 'semiótico']).ask()
#


def oracaoRelacional(
        ##TRANSITIVIDADE
        TIPO_DE_PROCESSO=None, indice_material=None, indice_agenciamento=None, indice_relacional=None, indice_atrib=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, t_inter_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
        t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
        t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
        t_inter_fp_numero_beta=None, t_inter_fp_morfologia_do_pronome_beta=None,
        t_inter_fp_determinacao_especificidade_alpha=None, t_inter_fp_orientacao_alpha=None,
        t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
        t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
        t_inter_fp_genero_obj_possuido=None, t_inter_fp_pessoa_da_interlocucao_proximidade=None,
        t_inter_fp_funcao_numerativo=None, t_inter_fp_cardinal=None, t_inter_fp_genero=None,
        t_inter_fp_tipo_precisa=None, t_inter_fp_tipo_real_card=None, t_inter_fp_milharExtenso=None,
        t_inter_fp_centenaExtenso=None, t_inter_fp_dezenaExtenso=None, t_inter_fp_unidadeExtenso=None,
        t_inter_fp_numIndefinido=None, t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
        t_inter_fp_tipo_de_nao_consciente_material=None, t_inter_fp_tipo_de_nao_consciente_semiotico=None,
        t_inter_fp_classe_palavra_ente=None, t_inter_fp_substantivo_lematizado=None, t_inter_fp_numero=None,
        t_inter_fp_tipo_feminino_ao=None, t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
        t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
        t_inter_fp_tonicidade=None, t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None,
        t_inter_fp_adjetivo_epiteto=None, t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None,
        t_inter_fp_numero_adjetivo=None, t_inter_fp_contracao=None,
        #
        # 		#
        t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        t_text_tem_tema_textual='-', t_text_tipo_insercao_cont="inserção_menu", t_text_conj_extenso_Cont=None,
        t_text_indiceCont=None,
        t_text_tipo_insercao_Conj="inserção_menu", t_text_tipo_de_conjuncao_Conj=None, t_text_conj_extensoConj=None,
        t_text_indiceConj=None,
        t_text_tipo_insercao_Rel='inserção_menu', t_text_pron_extenso_Rel=None, t_text_tipo_de_relativo=None,
        t_text_tipo_pronome_relativo=None, t_text_generoTemaTextual=None, t_text_numeroTemaTextual=None,
        t_text_indice_relacionalativo=None,
        t_text_indice_relacionalativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,
        # PARÂMETROS ESPEĆIFICOS DA RELACIONAL
        # ATRIBUTIVAS
        especificacao_tipo_modo_relacao=None, fase_atribuicao=None,
        dominio_atribuicao=None, tipo_de_realizacao_da_relacao=None,

        ##atributivas possessivas
        tipo_possuidor=None,

        ##Processo
        tipo_de_experiencia_gv=None, agencia=None, tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex=None, funcao_no_grupo_verbal_pos_final=None,
        verbo_lex=None, tipo_de_orientacao_lex=None, oi_numero_lex=None, genero_lex=None, oi_tipo_de_pessoa_lex=None,
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
        p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_funcao_numerativo=None,
        p1_cardinal=None, p1_genero=None, p1_tipo_precisa=None, p1_tipo_real_card=None, p1_milharExtenso=None,
        p1_centenaExtenso=None, p1_dezenaExtenso=None, p1_unidadeExtenso=None, p1_numIndefinido=None,
        p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
        p1_numero=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None, p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
        p1_reflexivo=None, p1_adjetivo_epiteto=None, p1_adjetivo_classificador=None, p1_genero_adjetivo=None,
        p1_numero_adjetivo=None, p1_contracao=None,
        ##PARTICIPANTE P1 REALIZADOS POR FP
        p1_FP_indice_preposicao_frase=None, p1_FP_dissoc_ente_nucleo=None, p1_FP_tem_qualificador=None,
        p1_FP_tipo_qualificador=None, p1_FP_indice_preposicao_qualif=None, p1_FP_determinacao_especificidade_beta=None,
        p1_FP_orientacao_beta=None, p1_FP_genero_beta=None, p1_FP_numero_beta=None,
        p1_FP_morfologia_do_pronome_beta=None, p1_FP_determinacao_especificidade_alpha=None,
        p1_FP_orientacao_alpha=None, p1_FP_genero_alpha=None, p1_FP_numero_alpha=None,
        p1_FP_morfologia_do_pronome_alpha=None, p1_FP_pessoa_da_interlocucao_possuidor=None,
        p1_FP_numero_obj_possuido=None, p1_FP_genero_obj_possuido=None, p1_FP_pessoa_da_interlocucao_proximidade=None,
        p1_FP_funcao_numerativo=None, p1_FP_cardinal=None, p1_FP_genero=None, p1_FP_tipo_precisa=None,
        p1_FP_tipo_real_card=None, p1_FP_milharExtenso=None, p1_FP_centenaExtenso=None, p1_FP_dezenaExtenso=None,
        p1_FP_unidadeExtenso=None, p1_FP_numIndefinido=None, p1_FP_tipo_de_ente=None, p1_FP_tipo_de_nao_consciente=None,
        p1_FP_tipo_de_nao_consciente_material=None, p1_FP_tipo_de_nao_consciente_semiotico=None,
        p1_FP_classe_palavra_ente=None, p1_FP_substantivo_lematizado=None, p1_FP_numero=None,
        p1_FP_tipo_feminino_ao=None, p1_FP_tipo_masc_ao=None, p1_FP_acent_tonica=None, p1_FP_nome_proprio=None,
        p1_FP_pessoa_da_interlocucao=None, p1_FP_transitividade_verbo=None, p1_FP_tonicidade=None,
        p1_FP_morfologia_do_pronome=None, p1_FP_reflexivo=None, p1_FP_adjetivo_epiteto=None,
        p1_FP_adjetivo_classificador=None, p1_FP_genero_adjetivo=None, p1_FP_numero_adjetivo=None, p1_FP_contracao=None,
        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
        p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_funcao_numerativo=None,
        p2_cardinal=None, p2_genero=None, p2_tipo_precisa=None, p2_tipo_real_card=None, p2_milharExtenso=None,
        p2_centenaExtenso=None, p2_dezenaExtenso=None, p2_unidadeExtenso=None, p2_numIndefinido=None,
        p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
        p2_numero=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None, p2_nome_proprio=None,
        p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
        p2_reflexivo=None, p2_adjetivo_epiteto=None, p2_adjetivo_classificador=None, p2_genero_adjetivo=None,
        p2_numero_adjetivo=None, p2_contracao=None,
        # P2 FRASE PREP
        p2_FP_indice_preposicao_frase=None, p2_FP_dissoc_ente_nucleo=None, p2_FP_tem_qualificador=None,
        p2_FP_tipo_qualificador=None, p2_FP_indice_preposicao_qualif=None, p2_FP_determinacao_especificidade_beta=None,
        p2_FP_orientacao_beta=None, p2_FP_genero_beta=None, p2_FP_numero_beta=None,
        p2_FP_morfologia_do_pronome_beta=None, p2_FP_determinacao_especificidade_alpha=None,
        p2_FP_orientacao_alpha=None, p2_FP_genero_alpha=None, p2_FP_numero_alpha=None,
        p2_FP_morfologia_do_pronome_alpha=None, p2_FP_pessoa_da_interlocucao_possuidor=None,
        p2_FP_numero_obj_possuido=None, p2_FP_genero_obj_possuido=None, p2_FP_pessoa_da_interlocucao_proximidade=None,
        p2_FP_funcao_numerativo=None, p2_FP_cardinal=None, p2_FP_genero=None, p2_FP_tipo_precisa=None,
        p2_FP_tipo_real_card=None, p2_FP_milharExtenso=None, p2_FP_centenaExtenso=None, p2_FP_dezenaExtenso=None,
        p2_FP_unidadeExtenso=None, p2_FP_numIndefinido=None, p2_FP_tipo_de_ente=None, p2_FP_tipo_de_nao_consciente=None,
        p2_FP_tipo_de_nao_consciente_material=None, p2_FP_tipo_de_nao_consciente_semiotico=None,
        p2_FP_classe_palavra_ente=None, p2_FP_substantivo_lematizado=None, p2_FP_numero=None,
        p2_FP_tipo_feminino_ao=None, p2_FP_tipo_masc_ao=None, p2_FP_acent_tonica=None, p2_FP_nome_proprio=None,
        p2_FP_pessoa_da_interlocucao=None, p2_FP_transitividade_verbo=None, p2_FP_tonicidade=None,
        p2_FP_morfologia_do_pronome=None, p2_FP_reflexivo=None, p2_FP_adjetivo_epiteto=None,
        p2_FP_adjetivo_classificador=None, p2_FP_genero_adjetivo=None, p2_FP_numero_adjetivo=None, p2_FP_contracao=None,

        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
        p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_funcao_numerativo=None,
        p3_cardinal=None, p3_genero=None, p3_tipo_precisa=None, p3_tipo_real_card=None, p3_milharExtenso=None,
        p3_centenaExtenso=None, p3_dezenaExtenso=None, p3_unidadeExtenso=None, p3_numIndefinido=None,
        p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
        p3_numero=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None, p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None, p3_adjetivo_epiteto=None, p3_adjetivo_classificador=None, p3_genero_adjetivo=None,
        p3_numero_adjetivo=None, p3_contracao=None,
        ##PARTICIPANTE P3 REALIZADOS POR FP
        p3_FP_indice_preposicao_frase=None, p3_FP_dissoc_ente_nucleo=None, p3_FP_tem_qualificador=None,
        p3_FP_tipo_qualificador=None, p3_FP_indice_preposicao_qualif=None, p3_FP_determinacao_especificidade_beta=None,
        p3_FP_orientacao_beta=None, p3_FP_genero_beta=None, p3_FP_numero_beta=None,
        p3_FP_morfologia_do_pronome_beta=None, p3_FP_determinacao_especificidade_alpha=None,
        p3_FP_orientacao_alpha=None, p3_FP_genero_alpha=None, p3_FP_numero_alpha=None,
        p3_FP_morfologia_do_pronome_alpha=None, p3_FP_pessoa_da_interlocucao_possuidor=None,
        p3_FP_numero_obj_possuido=None, p3_FP_genero_obj_possuido=None, p3_FP_pessoa_da_interlocucao_proximidade=None,
        p3_FP_funcao_numerativo=None, p3_FP_cardinal=None, p3_FP_genero=None, p3_FP_tipo_precisa=None,
        p3_FP_tipo_real_card=None, p3_FP_milharExtenso=None, p3_FP_centenaExtenso=None, p3_FP_dezenaExtenso=None,
        p3_FP_unidadeExtenso=None, p3_FP_numIndefinido=None, p3_FP_tipo_de_ente=None, p3_FP_tipo_de_nao_consciente=None,
        p3_FP_tipo_de_nao_consciente_material=None, p3_FP_tipo_de_nao_consciente_semiotico=None,
        p3_FP_classe_palavra_ente=None, p3_FP_substantivo_lematizado=None, p3_FP_numero=None,
        p3_FP_tipo_feminino_ao=None, p3_FP_tipo_masc_ao=None, p3_FP_acent_tonica=None, p3_FP_nome_proprio=None,
        p3_FP_pessoa_da_interlocucao=None, p3_FP_transitividade_verbo=None, p3_FP_tonicidade=None,
        p3_FP_morfologia_do_pronome=None, p3_FP_reflexivo=None, p3_FP_adjetivo_epiteto=None,
        p3_FP_adjetivo_classificador=None, p3_FP_genero_adjetivo=None, p3_FP_numero_adjetivo=None, p3_FP_contracao=None,
        ##participante realziado por circunstancia (relacionais circunstanciais)
        P_realizacaoCircunstancia=None, P_indice_preposicao_frase=None, P_dissoc_ente_nucleo=None,
        P_tem_qualificador=None, P_tipo_qualificador=None, P_indice_preposicao_qualif=None,
        P_determinacao_especificidade_beta=None, P_orientacao_beta=None, P_genero_beta=None, P_numero_beta=None,
        P_morfologia_do_pronome_beta=None, P_determinacao_especificidade_alpha=None, P_orientacao_alpha=None,
        P_genero_alpha=None, P_numero_alpha=None, P_morfologia_do_pronome_alpha=None,
        P_pessoa_da_interlocucao_possuidor=None, P_numero_obj_possuido=None, P_genero_obj_possuido=None,
        P_pessoa_da_interlocucao_proximidade=None, P_funcao_numerativo=None, P_cardinal=None, P_genero=None,
        P_tipo_precisa=None, P_tipo_real_card=None, P_milharExtenso=None, P_centenaExtenso=None, P_dezenaExtenso=None,
        P_unidadeExtenso=None, P_numIndefinido=None, P_tipo_de_ente=None, P_tipo_de_nao_consciente=None,
        P_tipo_de_nao_consciente_material=None, P_tipo_de_nao_consciente_semiotico=None, P_classe_palavra_ente=None,
        P_substantivo_lematizado=None, P_numero=None, P_tipo_feminino_ao=None, P_tipo_masc_ao=None, P_acent_tonica=None,
        P_nome_proprio=None, P_pessoa_da_interlocucao=None, P_transitividade_verbo=None, P_tonicidade=None,
        P_morfologia_do_pronome=None, P_reflexivo=None, P_adjetivo_epiteto=None, P_adjetivo_classificador=None,
        P_genero_adjetivo=None, P_numero_adjetivo=None, P_contracao=None, P_tipo_de_adverbio1=None, P_ind1=None,
        P_tipo_de_adverbio2=None, P_ind2=None, P_tipo_de_adverbio3=None, P_ind3=None, P_tipo_de_adverbio4=None,
        P_ind4=None, P_tipo_de_adverbio5=None, P_ind5=None,
        ##CIRCUNSTANCIA
        CIRC_ORACAO_realizacaoCircunstancia=None, CIRC_ORACAO_indice_preposicao_frase=None,
        CIRC_ORACAO_dissoc_ente_nucleo=None, CIRC_ORACAO_tem_qualificador=None, CIRC_ORACAO_tipo_qualificador=None,
        CIRC_ORACAO_indice_preposicao_qualif=None, CIRC_ORACAO_determinacao_especificidade_beta=None,
        CIRC_ORACAO_orientacao_beta=None, CIRC_ORACAO_genero_beta=None, CIRC_ORACAO_numero_beta=None,
        CIRC_ORACAO_morfologia_do_pronome_beta=None, CIRC_ORACAO_determinacao_especificidade_alpha=None,
        CIRC_ORACAO_orientacao_alpha=None, CIRC_ORACAO_genero_alpha=None, CIRC_ORACAO_numero_alpha=None,
        CIRC_ORACAO_morfologia_do_pronome_alpha=None, CIRC_ORACAO_pessoa_da_interlocucao_possuidor=None,
        CIRC_ORACAO_numero_obj_possuido=None, CIRC_ORACAO_genero_obj_possuido=None,
        CIRC_ORACAO_pessoa_da_interlocucao_proximidade=None, CIRC_ORACAO_funcao_numerativo=None,
        CIRC_ORACAO_cardinal=None, CIRC_ORACAO_genero=None, CIRC_ORACAO_tipo_precisa=None,
        CIRC_ORACAO_tipo_real_card=None, CIRC_ORACAO_milharExtenso=None, CIRC_ORACAO_centenaExtenso=None,
        CIRC_ORACAO_dezenaExtenso=None, CIRC_ORACAO_unidadeExtenso=None, CIRC_ORACAO_numIndefinido=None,
        CIRC_ORACAO_tipo_de_ente=None, CIRC_ORACAO_tipo_de_nao_consciente=None,
        CIRC_ORACAO_tipo_de_nao_consciente_material=None, CIRC_ORACAO_tipo_de_nao_consciente_semiotico=None,
        CIRC_ORACAO_classe_palavra_ente=None, CIRC_ORACAO_substantivo_lematizado=None, CIRC_ORACAO_numero=None,
        CIRC_ORACAO_tipo_feminino_ao=None, CIRC_ORACAO_tipo_masc_ao=None, CIRC_ORACAO_acent_tonica=None,
        CIRC_ORACAO_nome_proprio=None, CIRC_ORACAO_pessoa_da_interlocucao=None, CIRC_ORACAO_transitividade_verbo=None,
        CIRC_ORACAO_tonicidade=None, CIRC_ORACAO_morfologia_do_pronome=None, CIRC_ORACAO_reflexivo=None,
        CIRC_ORACAO_adjetivo_epiteto=None, CIRC_ORACAO_adjetivo_classificador=None, CIRC_ORACAO_genero_adjetivo=None,
        CIRC_ORACAO_numero_adjetivo=None, CIRC_ORACAO_contracao=None, CIRC_ORACAO_tipo_de_adverbio1=None,
        CIRC_ORACAO_ind1=None, CIRC_ORACAO_tipo_de_adverbio2=None, CIRC_ORACAO_ind2=None,
        CIRC_ORACAO_tipo_de_adverbio3=None, CIRC_ORACAO_ind3=None, CIRC_ORACAO_tipo_de_adverbio4=None,
        CIRC_ORACAO_ind4=None, CIRC_ORACAO_tipo_de_adverbio5=None, CIRC_ORACAO_ind5=None

):
    try:
        transitividade_ = transitividade(TIPO_DE_PROCESSO, indice_material, indice_agenciamento, indice_relacional)
        Modo = modo(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = tema_interpessoal(TIPO_TEMA_INTERPESSOAL, t_inter_tipoRealizacao, t_inter_tipo_de_adverbio1,
                                              t_inter_ind1, t_inter_tipo_de_adverbio2, t_inter_ind2,
                                              t_inter_tipo_de_adverbio3, t_inter_ind3, t_inter_tipo_de_adverbio4,
                                              t_inter_ind4, t_inter_tipo_de_adverbio5, t_inter_ind5,
                                              t_inter_fp_indice_preposicao_frase, t_inter_fp_dissoc_ente_nucleo,
                                              t_inter_fp_tem_qualificador, t_inter_fp_tipo_qualificador,
                                              t_inter_fp_indice_preposicao_qualif,
                                              t_inter_fp_determinacao_especificidade_beta, t_inter_fp_orientacao_beta,
                                              t_inter_fp_genero_beta, t_inter_fp_numero_beta,
                                              t_inter_fp_morfologia_do_pronome_beta,
                                              t_inter_fp_determinacao_especificidade_alpha, t_inter_fp_orientacao_alpha,
                                              t_inter_fp_genero_alpha, t_inter_fp_numero_alpha,
                                              t_inter_fp_morfologia_do_pronome_alpha,
                                              t_inter_fp_pessoa_da_interlocucao_possuidor,
                                              t_inter_fp_numero_obj_possuido, t_inter_fp_genero_obj_possuido,
                                              t_inter_fp_pessoa_da_interlocucao_proximidade,
                                              t_inter_fp_funcao_numerativo, t_inter_fp_cardinal, t_inter_fp_genero,
                                              t_inter_fp_tipo_precisa, t_inter_fp_tipo_real_card,
                                              t_inter_fp_milharExtenso, t_inter_fp_centenaExtenso,
                                              t_inter_fp_dezenaExtenso, t_inter_fp_unidadeExtenso,
                                              t_inter_fp_numIndefinido, t_inter_fp_tipo_de_ente,
                                              t_inter_fp_tipo_de_nao_consciente,
                                              t_inter_fp_tipo_de_nao_consciente_material,
                                              t_inter_fp_tipo_de_nao_consciente_semiotico,
                                              t_inter_fp_classe_palavra_ente, t_inter_fp_substantivo_lematizado,
                                              t_inter_fp_numero, t_inter_fp_tipo_feminino_ao, t_inter_fp_tipo_masc_ao,
                                              t_inter_fp_acent_tonica, t_inter_fp_nome_proprio,
                                              t_inter_fp_pessoa_da_interlocucao, t_inter_fp_transitividade_verbo,
                                              t_inter_fp_tonicidade, t_inter_fp_morfologia_do_pronome,
                                              t_inter_fp_reflexivo, t_inter_fp_adjetivo_epiteto,
                                              t_inter_fp_adjetivo_classificador, t_inter_fp_genero_adjetivo,
                                              t_inter_fp_numero_adjetivo, t_inter_fp_contracao, t_inter_indice_elem_qu,
                                              t_inter_indice_part_modal, t_inter_nome_proprio)
        Tema_textual = tema_textual(t_text_tem_tema_textual, t_text_tipo_insercao_cont, t_text_indiceCont,
                                    t_text_tipo_de_conjuncao_Conj, t_text_conj_extensoConj, t_text_indiceConj,
                                    t_text_tipo_insercao_Rel, t_text_pron_extenso_Rel, t_text_tipo_de_relativo,
                                    t_text_tipo_pronome_relativo, t_text_generoTemaTextual, t_text_numeroTemaTextual)

        tema_id = tema_ideacional(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        polar = polaridade(tipo_polaridade)
        Processo = grupo_verbal(tipo_de_experiencia_gv, agencia, tipo_de_experiencia_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, oi_numero_1, genero_1, oi_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, tipo_de_experiencia_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, oi_numero_2, genero_2, oi_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, tipo_de_experiencia_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, oi_numero_3, genero_3, oi_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, tipo_de_experiencia_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, oi_numero_4, genero_4, oi_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final,
                                verbo_lex, tipo_de_orientacao_lex, oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                padrao_pessoa_morfologia_lex)
        Circunstancia = circunstancia(CIRC_ORACAO_realizacaoCircunstancia, CIRC_ORACAO_indice_preposicao_frase,
                                      CIRC_ORACAO_dissoc_ente_nucleo, CIRC_ORACAO_tem_qualificador,
                                      CIRC_ORACAO_tipo_qualificador, CIRC_ORACAO_indice_preposicao_qualif,
                                      CIRC_ORACAO_determinacao_especificidade_beta, CIRC_ORACAO_orientacao_beta,
                                      CIRC_ORACAO_genero_beta, CIRC_ORACAO_numero_beta,
                                      CIRC_ORACAO_morfologia_do_pronome_beta,
                                      CIRC_ORACAO_determinacao_especificidade_alpha, CIRC_ORACAO_orientacao_alpha,
                                      CIRC_ORACAO_genero_alpha, CIRC_ORACAO_numero_alpha,
                                      CIRC_ORACAO_morfologia_do_pronome_alpha,
                                      CIRC_ORACAO_pessoa_da_interlocucao_possuidor, CIRC_ORACAO_numero_obj_possuido,
                                      CIRC_ORACAO_genero_obj_possuido, CIRC_ORACAO_pessoa_da_interlocucao_proximidade,
                                      cardinal=CIRC_ORACAO_cardinal, genero_numerativo=CIRC_ORACAO_numIndefinido,
                                      tipo_de_ente=CIRC_ORACAO_tipo_de_ente,
                                      tipo_de_nao_consciente=CIRC_ORACAO_tipo_de_nao_consciente,
                                      tipo_de_nao_consciente_material=CIRC_ORACAO_tipo_de_nao_consciente_material,
                                      tipo_de_nao_consciente_semiotico=CIRC_ORACAO_tipo_de_nao_consciente_semiotico,
                                      classe_palavra_ente=CIRC_ORACAO_classe_palavra_ente,
                                      substantivo_lematizado=CIRC_ORACAO_substantivo_lematizado,
                                      numero=CIRC_ORACAO_numero, tipo_feminino_ao=CIRC_ORACAO_tipo_feminino_ao,
                                      tipo_masc_ao=CIRC_ORACAO_tipo_masc_ao, acent_tonica=CIRC_ORACAO_acent_tonica,
                                      nome_prop=CIRC_ORACAO_nome_proprio,
                                      pessoa_da_interlocucao=CIRC_ORACAO_pessoa_da_interlocucao,
                                      transitividade_verbo=CIRC_ORACAO_transitividade_verbo,
                                      tonicidade=CIRC_ORACAO_tonicidade,
                                      morfologia_do_pronome=CIRC_ORACAO_morfologia_do_pronome,
                                      reflexivo=CIRC_ORACAO_reflexivo, adjetivo_epiteto=CIRC_ORACAO_adjetivo_epiteto,
                                      adjetivo_classificador=CIRC_ORACAO_adjetivo_classificador,
                                      genero_adjetivo=CIRC_ORACAO_genero_adjetivo,
                                      numero_adjetivo=CIRC_ORACAO_numero_adjetivo, contracao=CIRC_ORACAO_contracao,
                                      tipo_de_adverbio1=CIRC_ORACAO_tipo_de_adverbio1, ind1=CIRC_ORACAO_ind1,
                                      tipo_de_adverbio2=CIRC_ORACAO_tipo_de_adverbio2, ind2=CIRC_ORACAO_ind2,
                                      tipo_de_adverbio3=CIRC_ORACAO_tipo_de_adverbio3, ind3=CIRC_ORACAO_ind3,
                                      tipo_de_adverbio4=CIRC_ORACAO_tipo_de_adverbio4, ind4=CIRC_ORACAO_ind4,
                                      tipo_de_adverbio5=CIRC_ORACAO_tipo_de_adverbio5, ind5=CIRC_ORACAO_ind5)
        # relacional
        tipo_atribuicao = atribuicao_relacao(indice_atrib)

        # 	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
        if transitividade_ == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' and tipo_atribuicao == "sem_atribuição_de_relação":

            ####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
            ## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
            Portador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                    p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                    p1_orientacao_beta, p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                    p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                    p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                    p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido, p1_genero_obj_possuido,
                                    p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal, p1_genero,
                                    p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                    p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                    p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                    p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                    p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                    p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                    p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

            # POR ENQUANTO PARECE DESNECESSÁRIO DEIXAR TODAS AS POSSÍVILIDADES COMO ESTÃO AQUI, MAS NA HORA DE DESENVOLVER MAIS VAI SER NECESSÁRIO
            if (
                    (
                            especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                    (
                            especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                    (
                            especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                    (
                            especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')
            ):
                Atributo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                        p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                        p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                        p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                        p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                        p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                        p2_numero_obj_possuido, p2_genero_obj_possuido,
                                        p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal,
                                        p2_genero, p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso,
                                        p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido,
                                        p2_tipo_de_ente, p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                        p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                        p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                        p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                        p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)


            ## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
            # o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo.
            ##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
            elif (
                    (
                            especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                    (
                            especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                    (
                            especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                    (
                            especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')):

                Atributo = adjetivo(p2_adjetivo_epiteto, p2_genero_adjetivo, p2_numero_adjetivo)

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Portador, polar, Processo, Atributo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Portador, polar, Processo, Atributo + '?'))

        ##### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
        ##Nesse caso, a oracao é Effective (Tem Agente) e pode ser operativa ou receptiva
        # (há a possibilidade de Agente de segunda, terceira.....ordem)
        ##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
        # elementos na oracao mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA oracao

        elif transitividade_ == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo':
            Atribuidor = estrutura_gn(p3_dissoc_ente_nucleo, p3_tem_qualificador, p3_tipo_qualificador,
                                      p3_indice_preposicao_qualif, p3_determinacao_especificidade_beta,
                                      p3_orientacao_beta, p3_genero_beta, p3_numero_beta, p3_morfologia_do_pronome_beta,
                                      p3_determinacao_especificidade_alpha, p3_orientacao_alpha, p3_genero_alpha,
                                      p3_numero_alpha, p3_morfologia_do_pronome_alpha,
                                      p3_pessoa_da_interlocucao_possuidor, p3_numero_obj_possuido,
                                      p3_genero_obj_possuido, p3_pessoa_da_interlocucao_proximidade,
                                      p3_funcao_numerativo, p3_cardinal, p3_genero, p3_tipo_precisa, p3_tipo_real_card,
                                      p3_milharExtenso, p3_centenaExtenso, p3_dezenaExtenso, p3_unidadeExtenso,
                                      p3_numIndefinido, p3_tipo_de_ente, p3_tipo_de_nao_consciente,
                                      p3_tipo_de_nao_consciente_material, p3_tipo_de_nao_consciente_semiotico,
                                      p3_classe_palavra_ente, p3_substantivo_lematizado, p3_numero, p3_tipo_feminino_ao,
                                      p3_tipo_masc_ao, p3_acent_tonica, p3_nome_proprio, p3_pessoa_da_interlocucao,
                                      p3_transitividade_verbo, p3_tonicidade, p3_morfologia_do_pronome)
            Portador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                    p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                    p1_orientacao_beta, p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                    p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                    p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                    p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido, p1_genero_obj_possuido,
                                    p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal, p1_genero,
                                    p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                    p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                    p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                    p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                    p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                    p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                    p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            if ((tipo_atribuicao == 'atribuição_proj_ment_cognitiva') or
                    (tipo_atribuicao == 'atribuição_proj_ment_desiderativa') or
                    (tipo_atribuicao == 'atribuição_proj_verbal') or
                    (tipo_atribuicao == 'atribuição_expan_elaboracao') or
                    (tipo_atribuicao == 'atribuição_expan_intencificação')):
                if (
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')
                ):
                    Atributo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                            p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                            p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                            p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                            p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                            p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                            p2_numero_obj_possuido, p2_genero_obj_possuido,
                                            p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal,
                                            p2_genero, p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso,
                                            p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido,
                                            p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                            p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                            p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero,
                                            p2_tipo_feminino_ao, p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio,
                                            p2_pessoa_da_interlocucao, p2_transitividade_verbo, p2_tonicidade,
                                            p2_morfologia_do_pronome)

                if (
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')):
                    Atributo = adjetivo(p2_adjetivo_epiteto, p2_genero_adjetivo, p2_numero_adjetivo)
                #### VERIFICAR O ATRIBUIDOR---PODE SER QUE O ATRIBUTO TENHA QUE SER REALIZADO POR FRASE PREPOSICIONAL?;
                # grupo nominal com Epíteto como núcleo (checar) por enquanto vou deixar um caso basico; Possivelmente até o P1 possa
                # ser realizado por frase prep: "Eu fiz de você o presidente da cia...."
                if tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito':
                        oracao = " ".join((Atribuidor, polar, Processo, Portador, Atributo + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar':
                        oracao = " ".join((Atribuidor, polar, Processo, Portador, Atributo + '?'))

        elif transitividade_ == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo':
            ##PARA QUE O Atribuidor seja omitido é só deixar todos os parâmetros default None
            Atribuidor = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                             p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                             p3_FP_indice_preposicao_qualif, p3_FP_determinacao_especificidade_beta,
                                             p3_FP_orientacao_beta, p3_FP_genero_beta, p3_FP_numero_beta,
                                             p3_FP_morfologia_do_pronome_beta, p3_FP_determinacao_especificidade_alpha,
                                             p3_FP_orientacao_alpha, p3_FP_genero_alpha, p3_FP_numero_alpha,
                                             p3_FP_morfologia_do_pronome_alpha, p3_FP_pessoa_da_interlocucao_possuidor,
                                             p3_FP_numero_obj_possuido, p3_FP_genero_obj_possuido,
                                             p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                             p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa, p3_FP_tipo_real_card,
                                             p3_FP_milharExtenso, p3_FP_centenaExtenso, p3_FP_dezenaExtenso,
                                             p3_FP_unidadeExtenso, p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                             p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                             p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                             p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                             p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                             p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo, p3_FP_tonicidade)
            Portador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                    p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                    p1_orientacao_beta, p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                    p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                    p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                    p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido, p1_genero_obj_possuido,
                                    p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal, p1_genero,
                                    p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                    p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                    p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                    p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                    p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                    p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                    p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            if ((tipo_atribuicao == 'atribuição_proj_ment_cognitiva') or
                    (tipo_atribuicao == 'atribuição_proj_ment_desiderativa') or
                    (tipo_atribuicao == 'atribuição_proj_verbal') or
                    (tipo_atribuicao == 'atribuição_expan_elaboracao') or
                    (tipo_atribuicao == 'atribuição_expan_intencificação')):

                if (
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'entidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')
                ):
                    Atributo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                            p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                            p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                            p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                            p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                            p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                            p2_numero_obj_possuido, p2_genero_obj_possuido,
                                            p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal,
                                            p2_genero, p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso,
                                            p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido,
                                            p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                            p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                            p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero,
                                            p2_tipo_feminino_ao, p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio,
                                            p2_pessoa_da_interlocucao, p2_transitividade_verbo, p2_tonicidade,
                                            p2_morfologia_do_pronome)

                if (
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')):
                    Atributo = adjetivo(p2_adjetivo_epiteto, p2_genero_adjetivo, p2_numero_adjetivo)
            #### VERIFICAR O ATRIBUIDOR---PODE SER QUE O ATRIBUTO TENHA QUE SER REALIZADO POR FRASE PREPOSICIONAL?;
            # grupo nominal com Epíteto como núcleo (checar) por enquanto vou deixar um caso basico; Possivelmente até o P1 possa
            # ser realizado por frase prep: "Eu fiz de você o presidente da cia...."
            if tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito':
                    oracao = " ".join((Portador, polar, Processo, Atributo, Atribuidor + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar':
                    oracao = " ".join((Portador, polar, Processo, Atributo, Atribuidor + '?'))

        ####INTENSIVA_IDENTIFICATIVA
        #
        elif transitividade_ == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo':
            # 'Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            # a direcionalidade_voz do Símbolo / Valor / Sujeito;  deste tipo_pessoa de oracao determina se é operativa ou receptiva. Selecione a direcionalidade
            # 	Se Simbolo conflui com SUjeito = operativa

            Simbolo = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                   p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                   p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                   p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                   p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                   p1_numero_obj_possuido, p1_genero_obj_possuido,
                                   p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal, p1_genero,
                                   p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                   p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                   p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                   p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                   p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                   p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao, p1_transitividade_verbo,
                                   p1_tonicidade, p1_morfologia_do_pronome)
            Valor = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                 p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                 p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                 p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                 p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                 p2_numero_obj_possuido, p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                 p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                 p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                 p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                 p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                 p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                 p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                 p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)
            Designador1 = estrutura_gn(p3_dissoc_ente_nucleo, p3_tem_qualificador, p3_tipo_qualificador,
                                       p3_indice_preposicao_qualif, p3_determinacao_especificidade_beta,
                                       p3_orientacao_beta, p3_genero_beta, p3_numero_beta,
                                       p3_morfologia_do_pronome_beta, p3_determinacao_especificidade_alpha,
                                       p3_orientacao_alpha, p3_genero_alpha, p3_numero_alpha,
                                       p3_morfologia_do_pronome_alpha, p3_pessoa_da_interlocucao_possuidor,
                                       p3_numero_obj_possuido, p3_genero_obj_possuido,
                                       p3_pessoa_da_interlocucao_proximidade, p3_funcao_numerativo, p3_cardinal,
                                       p3_genero, p3_tipo_precisa, p3_tipo_real_card, p3_milharExtenso,
                                       p3_centenaExtenso, p3_dezenaExtenso, p3_unidadeExtenso, p3_numIndefinido,
                                       p3_tipo_de_ente, p3_tipo_de_nao_consciente, p3_tipo_de_nao_consciente_material,
                                       p3_tipo_de_nao_consciente_semiotico, p3_classe_palavra_ente,
                                       p3_substantivo_lematizado, p3_numero, p3_tipo_feminino_ao, p3_tipo_masc_ao,
                                       p3_acent_tonica, p3_nome_proprio, p3_pessoa_da_interlocucao,
                                       p3_transitividade_verbo, p3_tonicidade, p3_morfologia_do_pronome)

            Designador2 = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                              p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                              p3_FP_indice_preposicao_qualif, p3_FP_determinacao_especificidade_beta,
                                              p3_FP_orientacao_beta, p3_FP_genero_beta, p3_FP_numero_beta,
                                              p3_FP_morfologia_do_pronome_beta, p3_FP_determinacao_especificidade_alpha,
                                              p3_FP_orientacao_alpha, p3_FP_genero_alpha, p3_FP_numero_alpha,
                                              p3_FP_morfologia_do_pronome_alpha, p3_FP_pessoa_da_interlocucao_possuidor,
                                              p3_FP_numero_obj_possuido, p3_FP_genero_obj_possuido,
                                              p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                              p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa, p3_FP_tipo_real_card,
                                              p3_FP_milharExtenso, p3_FP_centenaExtenso, p3_FP_dezenaExtenso,
                                              p3_FP_unidadeExtenso, p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                              p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                              p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                              p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                              p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                              p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                              p3_FP_tonicidade)
            if ((tipo_atribuicao == 'atribuição_proj_ment_cognitiva') or
                    (tipo_atribuicao == 'atribuição_proj_ment_desiderativa') or
                    (tipo_atribuicao == 'atribuição_proj_verbal') or
                    (tipo_atribuicao == 'atribuição_expan_elaboracao') or
                    (tipo_atribuicao == 'atribuição_expan_intencificação')):

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo, polar, Processo, Valor, Designador2 + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo, polar, Processo, Valor, Designador2 + '?'))


                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, polar, Processo, Simbolo, Valor + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, polar, Processo, Simbolo, Valor + '?'))
            else:
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo, polar, Processo, Valor + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo, polar, Processo, Valor + '?'))

        elif transitividade_ == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo':
            ##NESTE CASO, confluência de Valor/Sujeito

            Valor = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                 p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                 p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                 p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                 p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                 p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                 p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                 p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                 p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                 p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                 p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                 p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                 p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            Simbolo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                   p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                   p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                   p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                   p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                   p2_numero_obj_possuido, p2_genero_obj_possuido,
                                   p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal, p2_genero,
                                   p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso, p2_centenaExtenso,
                                   p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido, p2_tipo_de_ente,
                                   p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                   p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                   p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                   p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao, p2_transitividade_verbo,
                                   p2_tonicidade, p2_morfologia_do_pronome)
            Designador1 = estrutura_gn(p3_dissoc_ente_nucleo, p3_tem_qualificador, p3_tipo_qualificador,
                                       p3_indice_preposicao_qualif, p3_determinacao_especificidade_beta,
                                       p3_orientacao_beta, p3_genero_beta, p3_numero_beta,
                                       p3_morfologia_do_pronome_beta, p3_determinacao_especificidade_alpha,
                                       p3_orientacao_alpha, p3_genero_alpha, p3_numero_alpha,
                                       p3_morfologia_do_pronome_alpha, p3_pessoa_da_interlocucao_possuidor,
                                       p3_numero_obj_possuido, p3_genero_obj_possuido,
                                       p3_pessoa_da_interlocucao_proximidade, p3_funcao_numerativo, p3_cardinal,
                                       p3_genero, p3_tipo_precisa, p3_tipo_real_card, p3_milharExtenso,
                                       p3_centenaExtenso, p3_dezenaExtenso, p3_unidadeExtenso, p3_numIndefinido,
                                       p3_tipo_de_ente, p3_tipo_de_nao_consciente, p3_tipo_de_nao_consciente_material,
                                       p3_tipo_de_nao_consciente_semiotico, p3_classe_palavra_ente,
                                       p3_substantivo_lematizado, p3_numero, p3_tipo_feminino_ao, p3_tipo_masc_ao,
                                       p3_acent_tonica, p3_nome_proprio, p3_pessoa_da_interlocucao,
                                       p3_transitividade_verbo, p3_tonicidade, p3_morfologia_do_pronome)

            Designador2 = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                              p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                              p3_FP_indice_preposicao_qualif, p3_FP_determinacao_especificidade_beta,
                                              p3_FP_orientacao_beta, p3_FP_genero_beta, p3_FP_numero_beta,
                                              p3_FP_morfologia_do_pronome_beta, p3_FP_determinacao_especificidade_alpha,
                                              p3_FP_orientacao_alpha, p3_FP_genero_alpha, p3_FP_numero_alpha,
                                              p3_FP_morfologia_do_pronome_alpha, p3_FP_pessoa_da_interlocucao_possuidor,
                                              p3_FP_numero_obj_possuido, p3_FP_genero_obj_possuido,
                                              p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                              p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa, p3_FP_tipo_real_card,
                                              p3_FP_milharExtenso, p3_FP_centenaExtenso, p3_FP_dezenaExtenso,
                                              p3_FP_unidadeExtenso, p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                              p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                              p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                              p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                              p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                              p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo,
                                              p3_FP_tonicidade)

            if ((tipo_atribuicao == 'atribuição_proj_ment_cognitiva') or
                    (tipo_atribuicao == 'atribuição_proj_ment_desiderativa') or
                    (tipo_atribuicao == 'atribuição_proj_verbal') or
                    (tipo_atribuicao == 'atribuição_expan_elaboracao') or
                    (tipo_atribuicao == 'atribuição_expan_intencificação')):

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, polar, Processo, Simbolo, Designador2 + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, polar, Processo, Simbolo, Designador2 + '?'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, polar, Processo, Valor, Simbolo + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, polar, Processo, Valor, Simbolo + '?'))
            else:
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, polar, Processo, Simbolo + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, polar, Processo, Simbolo + '.'))

        # 	# POSSESSIVO ATRIBUTIV0

        elif transitividade_ == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance':
            # tipo_atribuicao = choice.Menu(['posse_atributo', 'posse_processo']).ask()

            if tipo_de_realizacao_da_relacao == 'posse_atributo':

                Portador_Posse = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                              p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                              p1_orientacao_beta, p1_genero_beta, p1_numero_beta,
                                              p1_morfologia_do_pronome_beta, p1_determinacao_especificidade_alpha,
                                              p1_orientacao_alpha, p1_genero_alpha, p1_numero_alpha,
                                              p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                              p1_numero_obj_possuido, p1_genero_obj_possuido,
                                              p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal,
                                              p1_genero, p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso,
                                              p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido,
                                              p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                              p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                              p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero,
                                              p1_tipo_feminino_ao, p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio,
                                              p1_pessoa_da_interlocucao, p1_transitividade_verbo, p1_tonicidade,
                                              p1_morfologia_do_pronome)
                Atributo_Possuidor1 = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                                   p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                                   p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                                   p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                                   p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                                   p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                                   p2_numero_obj_possuido, p2_genero_obj_possuido,
                                                   p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo,
                                                   p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                                   p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso,
                                                   p2_unidadeExtenso, p2_numIndefinido, p2_tipo_de_ente,
                                                   p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                                   p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                                   p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                                   p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio,
                                                   p2_pessoa_da_interlocucao, p2_transitividade_verbo, p2_tonicidade,
                                                   p2_morfologia_do_pronome)
                Atributo_Possuidor2 = frase_preposicional(p2_FP_indice_preposicao_frase, p2_FP_dissoc_ente_nucleo,
                                                          p2_FP_tem_qualificador, p2_FP_tipo_qualificador,
                                                          p2_FP_indice_preposicao_qualif,
                                                          p2_FP_determinacao_especificidade_beta, p2_FP_orientacao_beta,
                                                          p2_FP_genero_beta, p2_FP_numero_beta,
                                                          p2_FP_morfologia_do_pronome_beta,
                                                          p2_FP_determinacao_especificidade_alpha,
                                                          p2_FP_orientacao_alpha, p2_FP_genero_alpha,
                                                          p2_FP_numero_alpha, p2_FP_morfologia_do_pronome_alpha,
                                                          p2_FP_pessoa_da_interlocucao_possuidor,
                                                          p2_FP_numero_obj_possuido, p2_FP_genero_obj_possuido,
                                                          p2_FP_pessoa_da_interlocucao_proximidade,
                                                          p2_FP_funcao_numerativo, p2_FP_cardinal, p2_FP_genero,
                                                          p2_FP_tipo_precisa, p2_FP_tipo_real_card, p2_FP_milharExtenso,
                                                          p2_FP_centenaExtenso, p2_FP_dezenaExtenso,
                                                          p2_FP_unidadeExtenso, p2_FP_numIndefinido, p2_FP_tipo_de_ente,
                                                          p2_FP_tipo_de_nao_consciente,
                                                          p2_FP_tipo_de_nao_consciente_material,
                                                          p2_FP_tipo_de_nao_consciente_semiotico,
                                                          p2_FP_classe_palavra_ente, p2_FP_substantivo_lematizado,
                                                          p2_FP_numero, p2_FP_tipo_feminino_ao, p2_FP_tipo_masc_ao,
                                                          p2_FP_acent_tonica, p2_FP_nome_proprio,
                                                          p2_FP_pessoa_da_interlocucao, p2_FP_transitividade_verbo,
                                                          p2_FP_tonicidade)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join(
                        (Portador_Posse, polar, Processo, Atributo_Possuidor1, Atributo_Possuidor2 + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join(
                        (Portador_Posse, polar, Processo, Atributo_Possuidor1, Atributo_Possuidor2 + '?'))
            # 	Ex.: O piano é meu/O piano é do João
            elif tipo_de_realizacao_da_relacao == 'posse_processo':

                # tipo_atribuicao = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask()
                if tipo_possuidor == 'possuidor_portador':
                    ##VERBO TER/POSSUIR/
                    Possuidor_Portador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                                      p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                                      p1_orientacao_beta, p1_genero_beta, p1_numero_beta,
                                                      p1_morfologia_do_pronome_beta,
                                                      p1_determinacao_especificidade_alpha, p1_orientacao_alpha,
                                                      p1_genero_alpha, p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                                      p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido,
                                                      p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                                      p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa,
                                                      p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                                      p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido,
                                                      p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                                      p1_tipo_de_nao_consciente_material,
                                                      p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                                      p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                                      p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio,
                                                      p1_pessoa_da_interlocucao, p1_transitividade_verbo, p1_tonicidade,
                                                      p1_morfologia_do_pronome)

                    Atributo_Posse = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                                  p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                                  p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                                  p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                                  p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                                  p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                                  p2_numero_obj_possuido, p2_genero_obj_possuido,
                                                  p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo,
                                                  p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                                  p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso,
                                                  p2_unidadeExtenso, p2_numIndefinido, p2_tipo_de_ente,
                                                  p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                                  p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                                  p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                                  p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio,
                                                  p2_pessoa_da_interlocucao, p2_transitividade_verbo, p2_tonicidade,
                                                  p2_morfologia_do_pronome)

                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Possuidor_Portador, polar, Processo, Atributo_Posse + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Possuidor_Portador, polar, Processo, Atributo_Posse + '?'))

                elif tipo_possuidor == 'possuidor_atributo':
                    ####VERBOS PERTENCER A/...

                    Portador_Posse = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                                  p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                                  p1_orientacao_beta, p1_genero_beta, p1_numero_beta,
                                                  p1_morfologia_do_pronome_beta, p1_determinacao_especificidade_alpha,
                                                  p1_orientacao_alpha, p1_genero_alpha, p1_numero_alpha,
                                                  p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                                  p1_numero_obj_possuido, p1_genero_obj_possuido,
                                                  p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo,
                                                  p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                                  p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso,
                                                  p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                                  p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                                  p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                                  p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                                  p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio,
                                                  p1_pessoa_da_interlocucao, p1_transitividade_verbo, p1_tonicidade,
                                                  p1_morfologia_do_pronome)

                    Atributo_Possuidor = frase_preposicional(p2_FP_indice_preposicao_frase, p2_FP_dissoc_ente_nucleo,
                                                             p2_FP_tem_qualificador, p2_FP_tipo_qualificador,
                                                             p2_FP_indice_preposicao_qualif,
                                                             p2_FP_determinacao_especificidade_beta,
                                                             p2_FP_orientacao_beta, p2_FP_genero_beta,
                                                             p2_FP_numero_beta, p2_FP_morfologia_do_pronome_beta,
                                                             p2_FP_determinacao_especificidade_alpha,
                                                             p2_FP_orientacao_alpha, p2_FP_genero_alpha,
                                                             p2_FP_numero_alpha, p2_FP_morfologia_do_pronome_alpha,
                                                             p2_FP_pessoa_da_interlocucao_possuidor,
                                                             p2_FP_numero_obj_possuido, p2_FP_genero_obj_possuido,
                                                             p2_FP_pessoa_da_interlocucao_proximidade,
                                                             p2_FP_funcao_numerativo, p2_FP_cardinal, p2_FP_genero,
                                                             p2_FP_tipo_precisa, p2_FP_tipo_real_card,
                                                             p2_FP_milharExtenso, p2_FP_centenaExtenso,
                                                             p2_FP_dezenaExtenso, p2_FP_unidadeExtenso,
                                                             p2_FP_numIndefinido, p2_FP_tipo_de_ente,
                                                             p2_FP_tipo_de_nao_consciente,
                                                             p2_FP_tipo_de_nao_consciente_material,
                                                             p2_FP_tipo_de_nao_consciente_semiotico,
                                                             p2_FP_classe_palavra_ente, p2_FP_substantivo_lematizado,
                                                             p2_FP_numero, p2_FP_tipo_feminino_ao, p2_FP_tipo_masc_ao,
                                                             p2_FP_acent_tonica, p2_FP_nome_proprio,
                                                             p2_FP_pessoa_da_interlocucao, p2_FP_transitividade_verbo,
                                                             p2_FP_tonicidade)
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Portador_Posse, polar, Processo, Atributo_Possuidor + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Portador_Posse, polar, Processo, Atributo_Possuidor + '?'))

        # POSSESSIVO IDENTIFICATIVO
        #
        elif transitividade_ == 'PR_relacional_possessivo_identificativo_AG_efetivo_operativo':
            # 'Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            # a direcionalidade_voz do Símbolo / Valor / Sujeito;  deste tipo_pessoa de oracao determina se é operativa ou receptiva. Selecione a direcionalidade
            # 	Se Simbolo conflui com SUjeito = operativa
            if tipo_de_realizacao_da_relacao == 'posse_participante' or tipo_de_realizacao_da_relacao == 'posse_processo':
                Simbolo = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                       p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                       p1_orientacao_beta, p1_genero_beta, p1_numero_beta,
                                       p1_morfologia_do_pronome_beta, p1_determinacao_especificidade_alpha,
                                       p1_orientacao_alpha, p1_genero_alpha, p1_numero_alpha,
                                       p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                       p1_numero_obj_possuido, p1_genero_obj_possuido,
                                       p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal,
                                       p1_genero, p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso,
                                       p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido,
                                       p1_tipo_de_ente, p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                       p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                       p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                       p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                       p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

                Valor1 = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                      p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                      p2_orientacao_beta, p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                      p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                      p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                      p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                      p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                      p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                      p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                      p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                      p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                      p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                      p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                      p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)
                Valor2 = frase_preposicional(p2_FP_indice_preposicao_frase, p2_FP_dissoc_ente_nucleo,
                                             p2_FP_tem_qualificador, p2_FP_tipo_qualificador,
                                             p2_FP_indice_preposicao_qualif, p2_FP_determinacao_especificidade_beta,
                                             p2_FP_orientacao_beta, p2_FP_genero_beta, p2_FP_numero_beta,
                                             p2_FP_morfologia_do_pronome_beta, p2_FP_determinacao_especificidade_alpha,
                                             p2_FP_orientacao_alpha, p2_FP_genero_alpha, p2_FP_numero_alpha,
                                             p2_FP_morfologia_do_pronome_alpha, p2_FP_pessoa_da_interlocucao_possuidor,
                                             p2_FP_numero_obj_possuido, p2_FP_genero_obj_possuido,
                                             p2_FP_pessoa_da_interlocucao_proximidade, p2_FP_funcao_numerativo,
                                             p2_FP_cardinal, p2_FP_genero, p2_FP_tipo_precisa, p2_FP_tipo_real_card,
                                             p2_FP_milharExtenso, p2_FP_centenaExtenso, p2_FP_dezenaExtenso,
                                             p2_FP_unidadeExtenso, p2_FP_numIndefinido, p2_FP_tipo_de_ente,
                                             p2_FP_tipo_de_nao_consciente, p2_FP_tipo_de_nao_consciente_material,
                                             p2_FP_tipo_de_nao_consciente_semiotico, p2_FP_classe_palavra_ente,
                                             p2_FP_substantivo_lematizado, p2_FP_numero, p2_FP_tipo_feminino_ao,
                                             p2_FP_tipo_masc_ao, p2_FP_acent_tonica, p2_FP_nome_proprio,
                                             p2_FP_pessoa_da_interlocucao, p2_FP_transitividade_verbo, p2_FP_tonicidade)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo, polar, Processo, Valor1, Valor2 + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo, polar, Processo, Valor1, Valor2 + '.'))
        # Ex.:'posse_participante'---O piano é seu/O piano é da moça?/posse_processo---***João possui o piano

        elif transitividade_ == 'PR_relacional_possessivo_identificativo_AG_efetivo_receptivo':
            Valor1 = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                  p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta, p2_orientacao_beta,
                                  p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                  p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                  p2_numero_alpha, p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                  p2_numero_obj_possuido, p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                  p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                  p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                  p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                  p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                  p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                  p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                  p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)
            Valor2 = frase_preposicional(p2_FP_indice_preposicao_frase, p2_FP_dissoc_ente_nucleo,
                                         p2_FP_tem_qualificador, p2_FP_tipo_qualificador,
                                         p2_FP_indice_preposicao_qualif, p2_FP_determinacao_especificidade_beta,
                                         p2_FP_orientacao_beta, p2_FP_genero_beta, p2_FP_numero_beta,
                                         p2_FP_morfologia_do_pronome_beta, p2_FP_determinacao_especificidade_alpha,
                                         p2_FP_orientacao_alpha, p2_FP_genero_alpha, p2_FP_numero_alpha,
                                         p2_FP_morfologia_do_pronome_alpha, p2_FP_pessoa_da_interlocucao_possuidor,
                                         p2_FP_numero_obj_possuido, p2_FP_genero_obj_possuido,
                                         p2_FP_pessoa_da_interlocucao_proximidade, p2_FP_funcao_numerativo,
                                         p2_FP_cardinal, p2_FP_genero, p2_FP_tipo_precisa, p2_FP_tipo_real_card,
                                         p2_FP_milharExtenso, p2_FP_centenaExtenso, p2_FP_dezenaExtenso,
                                         p2_FP_unidadeExtenso, p2_FP_numIndefinido, p2_FP_tipo_de_ente,
                                         p2_FP_tipo_de_nao_consciente, p2_FP_tipo_de_nao_consciente_material,
                                         p2_FP_tipo_de_nao_consciente_semiotico, p2_FP_classe_palavra_ente,
                                         p2_FP_substantivo_lematizado, p2_FP_numero, p2_FP_tipo_feminino_ao,
                                         p2_FP_tipo_masc_ao, p2_FP_acent_tonica, p2_FP_nome_proprio,
                                         p2_FP_pessoa_da_interlocucao, p2_FP_transitividade_verbo, p2_FP_tonicidade)
            Simbolo = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                   p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                                   p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                   p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                   p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                   p1_numero_obj_possuido, p1_genero_obj_possuido,
                                   p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal, p1_genero,
                                   p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                   p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                   p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                   p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                   p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                   p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao, p1_transitividade_verbo,
                                   p1_tonicidade, p1_morfologia_do_pronome)

            if tipo_de_realizacao_da_relacao == 'posse_participante' or tipo_de_realizacao_da_relacao == 'posse_processo':

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, polar, Processo, Simbolo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, polar, Processo, Simbolo + '?'))

        #####RELACIONAL CIRCUNSTANCIAL
        #
        elif transitividade_ == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance':
            # tipo_de_atributivo = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()
            Portador = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                    p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                    p1_orientacao_beta, p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                    p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                    p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                    p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido, p1_genero_obj_possuido,
                                    p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal, p1_genero,
                                    p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso, p1_centenaExtenso,
                                    p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido, p1_tipo_de_ente,
                                    p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                    p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                    p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                    p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                    p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

            if tipo_de_realizacao_da_relacao == 'atributo_circunstancial':
                Atributo_Circunstancial = circunstancia(P_realizacaoCircunstancia, P_indice_preposicao_frase,
                                                        P_dissoc_ente_nucleo, P_tem_qualificador, P_tipo_qualificador,
                                                        P_indice_preposicao_qualif, P_determinacao_especificidade_beta,
                                                        P_orientacao_beta, P_genero_beta, P_numero_beta,
                                                        P_morfologia_do_pronome_beta,
                                                        P_determinacao_especificidade_alpha, P_orientacao_alpha,
                                                        P_genero_alpha, P_numero_alpha, P_morfologia_do_pronome_alpha,
                                                        P_pessoa_da_interlocucao_possuidor, P_numero_obj_possuido,
                                                        P_genero_obj_possuido, P_pessoa_da_interlocucao_proximidade,
                                                        cardinal=P_cardinal, genero_numerativo=P_numIndefinido,
                                                        tipo_de_ente=P_tipo_de_ente,
                                                        tipo_de_nao_consciente=P_tipo_de_nao_consciente,
                                                        tipo_de_nao_consciente_material=P_tipo_de_nao_consciente_material,
                                                        tipo_de_nao_consciente_semiotico=P_tipo_de_nao_consciente_semiotico,
                                                        classe_palavra_ente=P_classe_palavra_ente,
                                                        substantivo_lematizado=P_substantivo_lematizado,
                                                        numero=P_numero, tipo_feminino_ao=P_tipo_feminino_ao,
                                                        tipo_masc_ao=P_tipo_masc_ao, acent_tonica=P_acent_tonica,
                                                        nome_prop=P_nome_proprio,
                                                        pessoa_da_interlocucao=P_pessoa_da_interlocucao,
                                                        transitividade_verbo=P_transitividade_verbo,
                                                        tonicidade=P_tonicidade,
                                                        morfologia_do_pronome=P_morfologia_do_pronome,
                                                        reflexivo=P_reflexivo, adjetivo_epiteto=P_adjetivo_epiteto,
                                                        adjetivo_classificador=P_adjetivo_classificador,
                                                        genero_adjetivo=P_genero_adjetivo,
                                                        numero_adjetivo=P_numero_adjetivo, contracao=P_contracao,
                                                        tipo_de_adverbio1=P_tipo_de_adverbio1, ind1=P_ind1,
                                                        tipo_de_adverbio2=P_tipo_de_adverbio2, ind2=P_ind2,
                                                        tipo_de_adverbio3=P_tipo_de_adverbio3, ind3=P_ind3,
                                                        tipo_de_adverbio4=P_tipo_de_adverbio4, ind4=P_ind4,
                                                        tipo_de_adverbio5=P_tipo_de_adverbio5, ind5=P_ind5)
                # Ex.: O livro é sobre a II Guerra
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Portador, polar, Processo, Atributo_Circunstancial + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Portador, polar, Processo, Atributo_Circunstancial + '?'))

            elif tipo_de_realizacao_da_relacao == 'processo_circunstancial':

                Atributo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                        p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                        p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                        p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                        p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                        p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                        p2_numero_obj_possuido, p2_genero_obj_possuido,
                                        p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal,
                                        p2_genero, p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso,
                                        p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido,
                                        p2_tipo_de_ente, p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                        p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                        p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                        p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                        p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

                # Ex.: O livro retrata a IIGuerra

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Portador, polar, Processo, Atributo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Portador, polar, Processo, Atributo + '?'))


        elif transitividade_ == 'PR_relacional_circunstancial_identificativo_AG_efetivo_operativo':

            # tipo_de_realizacao_da_relacao = choice.Menu(['participante_circunstancial', 'processo_circunstancial']).ask()

            if tipo_de_realizacao_da_relacao == 'participante_circunstancial' or tipo_de_realizacao_da_relacao == 'posse_processo':
                Simbolo1 = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                        p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                        p1_orientacao_beta, p1_genero_beta, p1_numero_beta,
                                        p1_morfologia_do_pronome_beta, p1_determinacao_especificidade_alpha,
                                        p1_orientacao_alpha, p1_genero_alpha, p1_numero_alpha,
                                        p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                        p1_numero_obj_possuido, p1_genero_obj_possuido,
                                        p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal,
                                        p1_genero, p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso,
                                        p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido,
                                        p1_tipo_de_ente, p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                        p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                        p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                        p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                        p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

                Simbolo2 = circunstancia(P_realizacaoCircunstancia, P_indice_preposicao_frase, P_dissoc_ente_nucleo,
                                         P_tem_qualificador, P_tipo_qualificador, P_indice_preposicao_qualif,
                                         P_determinacao_especificidade_beta, P_orientacao_beta, P_genero_beta,
                                         P_numero_beta, P_morfologia_do_pronome_beta,
                                         P_determinacao_especificidade_alpha, P_orientacao_alpha, P_genero_alpha,
                                         P_numero_alpha, P_morfologia_do_pronome_alpha,
                                         P_pessoa_da_interlocucao_possuidor, P_numero_obj_possuido,
                                         P_genero_obj_possuido, P_pessoa_da_interlocucao_proximidade,
                                         cardinal=P_cardinal, genero_numerativo=P_numIndefinido,
                                         tipo_de_ente=P_tipo_de_ente, tipo_de_nao_consciente=P_tipo_de_nao_consciente,
                                         tipo_de_nao_consciente_material=P_tipo_de_nao_consciente_material,
                                         tipo_de_nao_consciente_semiotico=P_tipo_de_nao_consciente_semiotico,
                                         classe_palavra_ente=P_classe_palavra_ente,
                                         substantivo_lematizado=P_substantivo_lematizado, numero=P_numero,
                                         tipo_feminino_ao=P_tipo_feminino_ao, tipo_masc_ao=P_tipo_masc_ao,
                                         acent_tonica=P_acent_tonica, nome_prop=P_nome_proprio,
                                         pessoa_da_interlocucao=P_pessoa_da_interlocucao,
                                         transitividade_verbo=P_transitividade_verbo, tonicidade=P_tonicidade,
                                         morfologia_do_pronome=P_morfologia_do_pronome, reflexivo=P_reflexivo,
                                         adjetivo_epiteto=P_adjetivo_epiteto,
                                         adjetivo_classificador=P_adjetivo_classificador,
                                         genero_adjetivo=P_genero_adjetivo, numero_adjetivo=P_numero_adjetivo,
                                         contracao=P_contracao, tipo_de_adverbio1=P_tipo_de_adverbio1, ind1=P_ind1,
                                         tipo_de_adverbio2=P_tipo_de_adverbio2, ind2=P_ind2,
                                         tipo_de_adverbio3=P_tipo_de_adverbio3, ind3=P_ind3,
                                         tipo_de_adverbio4=P_tipo_de_adverbio4, ind4=P_ind4,
                                         tipo_de_adverbio5=P_tipo_de_adverbio5, ind5=P_ind5)
                Valor = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                     p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                     p2_orientacao_beta, p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                     p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                     p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                     p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                     p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                     p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                     p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                     p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                     p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                     p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                     p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                     p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo1, Simbolo2, polar, Processo, Valor + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo1, Simbolo2, polar, Processo, Valor + '?'))

            # Ex.: Amanhã é dia 10

        elif transitividade_ == 'PR_relacional_circunstancial_identificativo_AG_efetivo_receptivo':

            if tipo_de_realizacao_da_relacao == 'posse_participante' or tipo_de_realizacao_da_relacao == 'posse_processo':
                Simbolo1 = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                        p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                        p1_orientacao_beta, p1_genero_beta, p1_numero_beta,
                                        p1_morfologia_do_pronome_beta, p1_determinacao_especificidade_alpha,
                                        p1_orientacao_alpha, p1_genero_alpha, p1_numero_alpha,
                                        p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                                        p1_numero_obj_possuido, p1_genero_obj_possuido,
                                        p1_pessoa_da_interlocucao_proximidade, p1_funcao_numerativo, p1_cardinal,
                                        p1_genero, p1_tipo_precisa, p1_tipo_real_card, p1_milharExtenso,
                                        p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso, p1_numIndefinido,
                                        p1_tipo_de_ente, p1_tipo_de_nao_consciente, p1_tipo_de_nao_consciente_material,
                                        p1_tipo_de_nao_consciente_semiotico, p1_classe_palavra_ente,
                                        p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao, p1_tipo_masc_ao,
                                        p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                        p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)

                Simbolo2 = circunstancia(P_realizacaoCircunstancia, P_indice_preposicao_frase, P_dissoc_ente_nucleo,
                                         P_tem_qualificador, P_tipo_qualificador, P_indice_preposicao_qualif,
                                         P_determinacao_especificidade_beta, P_orientacao_beta, P_genero_beta,
                                         P_numero_beta, P_morfologia_do_pronome_beta,
                                         P_determinacao_especificidade_alpha, P_orientacao_alpha, P_genero_alpha,
                                         P_numero_alpha, P_morfologia_do_pronome_alpha,
                                         P_pessoa_da_interlocucao_possuidor, P_numero_obj_possuido,
                                         P_genero_obj_possuido, P_pessoa_da_interlocucao_proximidade,
                                         cardinal=P_cardinal, genero_numerativo=P_numIndefinido,
                                         tipo_de_ente=P_tipo_de_ente, tipo_de_nao_consciente=P_tipo_de_nao_consciente,
                                         tipo_de_nao_consciente_material=P_tipo_de_nao_consciente_material,
                                         tipo_de_nao_consciente_semiotico=P_tipo_de_nao_consciente_semiotico,
                                         classe_palavra_ente=P_classe_palavra_ente,
                                         substantivo_lematizado=P_substantivo_lematizado, numero=P_numero,
                                         tipo_feminino_ao=P_tipo_feminino_ao, tipo_masc_ao=P_tipo_masc_ao,
                                         acent_tonica=P_acent_tonica, nome_prop=P_nome_proprio,
                                         pessoa_da_interlocucao=P_pessoa_da_interlocucao,
                                         transitividade_verbo=P_transitividade_verbo, tonicidade=P_tonicidade,
                                         morfologia_do_pronome=P_morfologia_do_pronome, reflexivo=P_reflexivo,
                                         adjetivo_epiteto=P_adjetivo_epiteto,
                                         adjetivo_classificador=P_adjetivo_classificador,
                                         genero_adjetivo=P_genero_adjetivo, numero_adjetivo=P_numero_adjetivo,
                                         contracao=P_contracao, tipo_de_adverbio1=P_tipo_de_adverbio1, ind1=P_ind1,
                                         tipo_de_adverbio2=P_tipo_de_adverbio2, ind2=P_ind2,
                                         tipo_de_adverbio3=P_tipo_de_adverbio3, ind3=P_ind3,
                                         tipo_de_adverbio4=P_tipo_de_adverbio4, ind4=P_ind4,
                                         tipo_de_adverbio5=P_tipo_de_adverbio5, ind5=P_ind5)
                Valor = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                     p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                     p2_orientacao_beta, p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                     p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                     p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                     p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido,
                                     p2_genero_obj_possuido, p2_pessoa_da_interlocucao_proximidade,
                                     p2_funcao_numerativo, p2_cardinal, p2_genero, p2_tipo_precisa, p2_tipo_real_card,
                                     p2_milharExtenso, p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso,
                                     p2_numIndefinido, p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                     p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                     p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao,
                                     p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                     p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, polar, Processo, Simbolo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, polar, Processo, Simbolo + '?'))
        # Ex.: Dia 10 é amanhã
        return (re.sub(' +', ' ', oracao.strip()).capitalize())
    except:
        return ""


#
# ##ORAÇÃO EXISTENCIAL
#
def oracaoExistencial(
        ##TRANSITIVIDADE
        TIPO_DE_PROCESSO=None, indice_material=None, indice_agenciamento=None, indice_relacional=None, indice_atrib=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, t_inter_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
        t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
        t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
        t_inter_fp_numero_beta=None, t_inter_fp_morfologia_do_pronome_beta=None,
        t_inter_fp_determinacao_especificidade_alpha=None, t_inter_fp_orientacao_alpha=None,
        t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
        t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
        t_inter_fp_genero_obj_possuido=None, t_inter_fp_pessoa_da_interlocucao_proximidade=None,
        t_inter_fp_funcao_numerativo=None, t_inter_fp_cardinal=None, t_inter_fp_genero=None,
        t_inter_fp_tipo_precisa=None, t_inter_fp_tipo_real_card=None, t_inter_fp_milharExtenso=None,
        t_inter_fp_centenaExtenso=None, t_inter_fp_dezenaExtenso=None, t_inter_fp_unidadeExtenso=None,
        t_inter_fp_numIndefinido=None, t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
        t_inter_fp_tipo_de_nao_consciente_material=None, t_inter_fp_tipo_de_nao_consciente_semiotico=None,
        t_inter_fp_classe_palavra_ente=None, t_inter_fp_substantivo_lematizado=None, t_inter_fp_numero=None,
        t_inter_fp_tipo_feminino_ao=None, t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
        t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
        t_inter_fp_tonicidade=None, t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None,
        t_inter_fp_adjetivo_epiteto=None, t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None,
        t_inter_fp_numero_adjetivo=None, t_inter_fp_contracao=None,
        #
        # 		#
        t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        t_text_tem_tema_textual='-', t_text_tipo_insercao_cont="inserção_menu", t_text_conj_extenso_Cont=None,
        t_text_indiceCont=None,
        t_text_tipo_insercao_Conj="inserção_menu", t_text_tipo_de_conjuncao_Conj=None, t_text_conj_extensoConj=None,
        t_text_indiceConj=None,
        t_text_tipo_insercao_Rel='inserção_menu', t_text_pron_extenso_Rel=None, t_text_tipo_de_relativo=None,
        t_text_tipo_pronome_relativo=None, t_text_generoTemaTextual=None, t_text_numeroTemaTextual=None,
        t_text_indice_relacionalativo=None,
        t_text_indice_relacionalativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,

        ##Processo
        tipo_de_experiencia_gv=None, agencia=None, tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex=None, funcao_no_grupo_verbal_pos_final=None,
        verbo_lex=None, tipo_de_orientacao_lex=None, oi_numero_lex=None, genero_lex=None, oi_tipo_de_pessoa_lex=None,
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,

        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
        p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_funcao_numerativo=None,
        p1_cardinal=None, p1_genero=None, p1_tipo_precisa=None, p1_tipo_real_card=None, p1_milharExtenso=None,
        p1_centenaExtenso=None, p1_dezenaExtenso=None, p1_unidadeExtenso=None, p1_numIndefinido=None,
        p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
        p1_numero=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None, p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
        p1_reflexivo=None, p1_adjetivo_epiteto=None, p1_adjetivo_classificador=None, p1_genero_adjetivo=None,
        p1_numero_adjetivo=None, p1_contracao=None,
        ##CIRCUNSTANCIA
        CIRC_ORACAO_realizacaoCircunstancia=None, CIRC_ORACAO_indice_preposicao_frase=None,
        CIRC_ORACAO_dissoc_ente_nucleo=None, CIRC_ORACAO_tem_qualificador=None, CIRC_ORACAO_tipo_qualificador=None,
        CIRC_ORACAO_indice_preposicao_qualif=None, CIRC_ORACAO_determinacao_especificidade_beta=None,
        CIRC_ORACAO_orientacao_beta=None, CIRC_ORACAO_genero_beta=None, CIRC_ORACAO_numero_beta=None,
        CIRC_ORACAO_morfologia_do_pronome_beta=None, CIRC_ORACAO_determinacao_especificidade_alpha=None,
        CIRC_ORACAO_orientacao_alpha=None, CIRC_ORACAO_genero_alpha=None, CIRC_ORACAO_numero_alpha=None,
        CIRC_ORACAO_morfologia_do_pronome_alpha=None, CIRC_ORACAO_pessoa_da_interlocucao_possuidor=None,
        CIRC_ORACAO_numero_obj_possuido=None, CIRC_ORACAO_genero_obj_possuido=None,
        CIRC_ORACAO_pessoa_da_interlocucao_proximidade=None, CIRC_ORACAO_funcao_numerativo=None,
        CIRC_ORACAO_cardinal=None, CIRC_ORACAO_genero=None, CIRC_ORACAO_tipo_precisa=None,
        CIRC_ORACAO_tipo_real_card=None, CIRC_ORACAO_milharExtenso=None, CIRC_ORACAO_centenaExtenso=None,
        CIRC_ORACAO_dezenaExtenso=None, CIRC_ORACAO_unidadeExtenso=None, CIRC_ORACAO_numIndefinido=None,
        CIRC_ORACAO_tipo_de_ente=None, CIRC_ORACAO_tipo_de_nao_consciente=None,
        CIRC_ORACAO_tipo_de_nao_consciente_material=None, CIRC_ORACAO_tipo_de_nao_consciente_semiotico=None,
        CIRC_ORACAO_classe_palavra_ente=None, CIRC_ORACAO_substantivo_lematizado=None, CIRC_ORACAO_numero=None,
        CIRC_ORACAO_tipo_feminino_ao=None, CIRC_ORACAO_tipo_masc_ao=None, CIRC_ORACAO_acent_tonica=None,
        CIRC_ORACAO_nome_proprio=None, CIRC_ORACAO_pessoa_da_interlocucao=None, CIRC_ORACAO_transitividade_verbo=None,
        CIRC_ORACAO_tonicidade=None, CIRC_ORACAO_morfologia_do_pronome=None, CIRC_ORACAO_reflexivo=None,
        CIRC_ORACAO_adjetivo_epiteto=None, CIRC_ORACAO_adjetivo_classificador=None, CIRC_ORACAO_genero_adjetivo=None,
        CIRC_ORACAO_numero_adjetivo=None, CIRC_ORACAO_contracao=None, CIRC_ORACAO_tipo_de_adverbio1=None,
        CIRC_ORACAO_ind1=None, CIRC_ORACAO_tipo_de_adverbio2=None, CIRC_ORACAO_ind2=None,
        CIRC_ORACAO_tipo_de_adverbio3=None, CIRC_ORACAO_ind3=None, CIRC_ORACAO_tipo_de_adverbio4=None,
        CIRC_ORACAO_ind4=None, CIRC_ORACAO_tipo_de_adverbio5=None, CIRC_ORACAO_ind5=None):
    try:
        transitividade_ = transitividade(TIPO_DE_PROCESSO, indice_material, indice_agenciamento, indice_relacional)
        Modo = modo(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = tema_interpessoal(TIPO_TEMA_INTERPESSOAL, t_inter_tipoRealizacao, t_inter_tipo_de_adverbio1,
                                              t_inter_ind1, t_inter_tipo_de_adverbio2, t_inter_ind2,
                                              t_inter_tipo_de_adverbio3, t_inter_ind3, t_inter_tipo_de_adverbio4,
                                              t_inter_ind4, t_inter_tipo_de_adverbio5, t_inter_ind5,
                                              t_inter_fp_indice_preposicao_frase, t_inter_fp_dissoc_ente_nucleo,
                                              t_inter_fp_tem_qualificador, t_inter_fp_tipo_qualificador,
                                              t_inter_fp_indice_preposicao_qualif,
                                              t_inter_fp_determinacao_especificidade_beta, t_inter_fp_orientacao_beta,
                                              t_inter_fp_genero_beta, t_inter_fp_numero_beta,
                                              t_inter_fp_morfologia_do_pronome_beta,
                                              t_inter_fp_determinacao_especificidade_alpha, t_inter_fp_orientacao_alpha,
                                              t_inter_fp_genero_alpha, t_inter_fp_numero_alpha,
                                              t_inter_fp_morfologia_do_pronome_alpha,
                                              t_inter_fp_pessoa_da_interlocucao_possuidor,
                                              t_inter_fp_numero_obj_possuido, t_inter_fp_genero_obj_possuido,
                                              t_inter_fp_pessoa_da_interlocucao_proximidade,
                                              t_inter_fp_funcao_numerativo, t_inter_fp_cardinal, t_inter_fp_genero,
                                              t_inter_fp_tipo_precisa, t_inter_fp_tipo_real_card,
                                              t_inter_fp_milharExtenso, t_inter_fp_centenaExtenso,
                                              t_inter_fp_dezenaExtenso, t_inter_fp_unidadeExtenso,
                                              t_inter_fp_numIndefinido, t_inter_fp_tipo_de_ente,
                                              t_inter_fp_tipo_de_nao_consciente,
                                              t_inter_fp_tipo_de_nao_consciente_material,
                                              t_inter_fp_tipo_de_nao_consciente_semiotico,
                                              t_inter_fp_classe_palavra_ente, t_inter_fp_substantivo_lematizado,
                                              t_inter_fp_numero, t_inter_fp_tipo_feminino_ao, t_inter_fp_tipo_masc_ao,
                                              t_inter_fp_acent_tonica, t_inter_fp_nome_proprio,
                                              t_inter_fp_pessoa_da_interlocucao, t_inter_fp_transitividade_verbo,
                                              t_inter_fp_tonicidade, t_inter_fp_morfologia_do_pronome,
                                              t_inter_fp_reflexivo, t_inter_fp_adjetivo_epiteto,
                                              t_inter_fp_adjetivo_classificador, t_inter_fp_genero_adjetivo,
                                              t_inter_fp_numero_adjetivo, t_inter_fp_contracao, t_inter_indice_elem_qu,
                                              t_inter_indice_part_modal, t_inter_nome_proprio)
        Tema_textual = tema_textual(t_text_tem_tema_textual, t_text_tipo_insercao_cont, t_text_indiceCont,
                                    t_text_tipo_de_conjuncao_Conj, t_text_conj_extensoConj, t_text_indiceConj,
                                    t_text_tipo_insercao_Rel, t_text_pron_extenso_Rel, t_text_tipo_de_relativo,
                                    t_text_tipo_pronome_relativo, t_text_generoTemaTextual, t_text_numeroTemaTextual)
        tema_id = tema_ideacional(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        polar = polaridade(tipo_polaridade)
        Processo = grupo_verbal(tipo_de_experiencia_gv, agencia, tipo_de_experiencia_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, oi_numero_1, genero_1, oi_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, tipo_de_experiencia_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, oi_numero_2, genero_2, oi_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, tipo_de_experiencia_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, oi_numero_3, genero_3, oi_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, tipo_de_experiencia_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, oi_numero_4, genero_4, oi_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final,
                                verbo_lex, tipo_de_orientacao_lex, oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                padrao_pessoa_morfologia_lex)
        Circunstancia = circunstancia(CIRC_ORACAO_realizacaoCircunstancia, CIRC_ORACAO_indice_preposicao_frase,
                                      CIRC_ORACAO_dissoc_ente_nucleo, CIRC_ORACAO_tem_qualificador,
                                      CIRC_ORACAO_tipo_qualificador, CIRC_ORACAO_indice_preposicao_qualif,
                                      CIRC_ORACAO_determinacao_especificidade_beta, CIRC_ORACAO_orientacao_beta,
                                      CIRC_ORACAO_genero_beta, CIRC_ORACAO_numero_beta,
                                      CIRC_ORACAO_morfologia_do_pronome_beta,
                                      CIRC_ORACAO_determinacao_especificidade_alpha, CIRC_ORACAO_orientacao_alpha,
                                      CIRC_ORACAO_genero_alpha, CIRC_ORACAO_numero_alpha,
                                      CIRC_ORACAO_morfologia_do_pronome_alpha,
                                      CIRC_ORACAO_pessoa_da_interlocucao_possuidor, CIRC_ORACAO_numero_obj_possuido,
                                      CIRC_ORACAO_genero_obj_possuido, CIRC_ORACAO_pessoa_da_interlocucao_proximidade,
                                      cardinal=CIRC_ORACAO_cardinal, genero_numerativo=CIRC_ORACAO_numIndefinido,
                                      tipo_de_ente=CIRC_ORACAO_tipo_de_ente,
                                      tipo_de_nao_consciente=CIRC_ORACAO_tipo_de_nao_consciente,
                                      tipo_de_nao_consciente_material=CIRC_ORACAO_tipo_de_nao_consciente_material,
                                      tipo_de_nao_consciente_semiotico=CIRC_ORACAO_tipo_de_nao_consciente_semiotico,
                                      classe_palavra_ente=CIRC_ORACAO_classe_palavra_ente,
                                      substantivo_lematizado=CIRC_ORACAO_substantivo_lematizado,
                                      numero=CIRC_ORACAO_numero, tipo_feminino_ao=CIRC_ORACAO_tipo_feminino_ao,
                                      tipo_masc_ao=CIRC_ORACAO_tipo_masc_ao, acent_tonica=CIRC_ORACAO_acent_tonica,
                                      nome_prop=CIRC_ORACAO_nome_proprio,
                                      pessoa_da_interlocucao=CIRC_ORACAO_pessoa_da_interlocucao,
                                      transitividade_verbo=CIRC_ORACAO_transitividade_verbo,
                                      tonicidade=CIRC_ORACAO_tonicidade,
                                      morfologia_do_pronome=CIRC_ORACAO_morfologia_do_pronome,
                                      reflexivo=CIRC_ORACAO_reflexivo, adjetivo_epiteto=CIRC_ORACAO_adjetivo_epiteto,
                                      adjetivo_classificador=CIRC_ORACAO_adjetivo_classificador,
                                      genero_adjetivo=CIRC_ORACAO_genero_adjetivo,
                                      numero_adjetivo=CIRC_ORACAO_numero_adjetivo, contracao=CIRC_ORACAO_contracao,
                                      tipo_de_adverbio1=CIRC_ORACAO_tipo_de_adverbio1, ind1=CIRC_ORACAO_ind1,
                                      tipo_de_adverbio2=CIRC_ORACAO_tipo_de_adverbio2, ind2=CIRC_ORACAO_ind2,
                                      tipo_de_adverbio3=CIRC_ORACAO_tipo_de_adverbio3, ind3=CIRC_ORACAO_ind3,
                                      tipo_de_adverbio4=CIRC_ORACAO_tipo_de_adverbio4, ind4=CIRC_ORACAO_ind4,
                                      tipo_de_adverbio5=CIRC_ORACAO_tipo_de_adverbio5, ind5=CIRC_ORACAO_ind5)

        if transitividade_ == 'PR_Existencial_AG_médio_sem_alcance':
            Existente = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                                     p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta,
                                     p1_orientacao_beta, p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                                     p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                                     p1_numero_alpha, p1_morfologia_do_pronome_alpha,
                                     p1_pessoa_da_interlocucao_possuidor, p1_numero_obj_possuido,
                                     p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                                     p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                                     p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                                     p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                                     p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                                     p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                                     p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                                     p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
            if (
                    Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA'):
                oracao = " ".join(polar, Processo, Existente + '.')
            elif (
                    Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'):
                oracao = " ".join((polar, Processo, Existente + '?'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((polar, Existente, Processo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((polar, Existente, Processo + '?'))
        return (re.sub(' +', ' ', oracao.strip()).capitalize())
    except:
        return ""


#
# ##ORAÇÃO verbal
# MODO_DO_DIZENTE = choice.Menu(['atividade', 'semioticidade']).ask()
# RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
# TIPO_SEMIOTICIDADE == 'não_projeção_+verbiagem',não_projeção_-verbiagem
# TIPO_PROJECAO = choice.Menu(['citativa', 'relativa']).ask()
# TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
def oracaoVerbal(

        ##TRANSITIVIDADE
        TIPO_DE_PROCESSO=None, indice_material=None, indice_agenciamento=None, indice_relacional=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, t_inter_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
        t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
        t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
        t_inter_fp_numero_beta=None, t_inter_fp_morfologia_do_pronome_beta=None,
        t_inter_fp_determinacao_especificidade_alpha=None, t_inter_fp_orientacao_alpha=None,
        t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
        t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
        t_inter_fp_genero_obj_possuido=None, t_inter_fp_pessoa_da_interlocucao_proximidade=None,
        t_inter_fp_funcao_numerativo=None, t_inter_fp_cardinal=None, t_inter_fp_genero=None,
        t_inter_fp_tipo_precisa=None, t_inter_fp_tipo_real_card=None, t_inter_fp_milharExtenso=None,
        t_inter_fp_centenaExtenso=None, t_inter_fp_dezenaExtenso=None, t_inter_fp_unidadeExtenso=None,
        t_inter_fp_numIndefinido=None, t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
        t_inter_fp_tipo_de_nao_consciente_material=None, t_inter_fp_tipo_de_nao_consciente_semiotico=None,
        t_inter_fp_classe_palavra_ente=None, t_inter_fp_substantivo_lematizado=None, t_inter_fp_numero=None,
        t_inter_fp_tipo_feminino_ao=None, t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
        t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
        t_inter_fp_tonicidade=None, t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None,
        t_inter_fp_adjetivo_epiteto=None, t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None,
        t_inter_fp_numero_adjetivo=None, t_inter_fp_contracao=None,
        #
        # 		#
        t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        t_text_tem_tema_textual='-', t_text_tipo_insercao_cont="inserção_menu", t_text_conj_extenso_Cont=None,
        t_text_indiceCont=None,
        t_text_tipo_insercao_Conj="inserção_menu", t_text_tipo_de_conjuncao_Conj=None, t_text_conj_extensoConj=None,
        t_text_indiceConj=None,
        t_text_tipo_insercao_Rel='inserção_menu', t_text_pron_extenso_Rel=None, t_text_tipo_de_relativo=None,
        t_text_tipo_pronome_relativo=None, t_text_generoTemaTextual=None, t_text_numeroTemaTextual=None,
        t_text_indice_relacionalativo=None,
        t_text_indice_relacionalativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,
        ##PARAMETROS da oracao VERBAL
        MODO_DO_DIZENTE=None, TIPO_SEMIOTICIDADE=None, TIPO_PROJECAO=None, RECEPTIVIDADE=None,
        ##Processo
        tipo_de_experiencia_gv=None, agencia=None, tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex=None, funcao_no_grupo_verbal_pos_final=None,
        verbo_lex=None, tipo_de_orientacao_lex=None, oi_numero_lex=None, genero_lex=None, oi_tipo_de_pessoa_lex=None,
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
        p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_funcao_numerativo=None,
        p1_cardinal=None, p1_genero=None, p1_tipo_precisa=None, p1_tipo_real_card=None, p1_milharExtenso=None,
        p1_centenaExtenso=None, p1_dezenaExtenso=None, p1_unidadeExtenso=None, p1_numIndefinido=None,
        p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
        p1_numero=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None, p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
        p1_reflexivo=None, p1_adjetivo_epiteto=None, p1_adjetivo_classificador=None, p1_genero_adjetivo=None,
        p1_numero_adjetivo=None, p1_contracao=None,
        ## P1 REALIZADOS POR FP
        p1_FP_indice_preposicao_frase=None, p1_FP_dissoc_ente_nucleo=None, p1_FP_tem_qualificador=None,
        p1_FP_tipo_qualificador=None, p1_FP_indice_preposicao_qualif=None, p1_FP_determinacao_especificidade_beta=None,
        p1_FP_orientacao_beta=None, p1_FP_genero_beta=None, p1_FP_numero_beta=None,
        p1_FP_morfologia_do_pronome_beta=None, p1_FP_determinacao_especificidade_alpha=None,
        p1_FP_orientacao_alpha=None, p1_FP_genero_alpha=None, p1_FP_numero_alpha=None,
        p1_FP_morfologia_do_pronome_alpha=None, p1_FP_pessoa_da_interlocucao_possuidor=None,
        p1_FP_numero_obj_possuido=None, p1_FP_genero_obj_possuido=None, p1_FP_pessoa_da_interlocucao_proximidade=None,
        p1_FP_funcao_numerativo=None, p1_FP_cardinal=None, p1_FP_genero=None, p1_FP_tipo_precisa=None,
        p1_FP_tipo_real_card=None, p1_FP_milharExtenso=None, p1_FP_centenaExtenso=None, p1_FP_dezenaExtenso=None,
        p1_FP_unidadeExtenso=None, p1_FP_numIndefinido=None, p1_FP_tipo_de_ente=None, p1_FP_tipo_de_nao_consciente=None,
        p1_FP_tipo_de_nao_consciente_material=None, p1_FP_tipo_de_nao_consciente_semiotico=None,
        p1_FP_classe_palavra_ente=None, p1_FP_substantivo_lematizado=None, p1_FP_numero=None,
        p1_FP_tipo_feminino_ao=None, p1_FP_tipo_masc_ao=None, p1_FP_acent_tonica=None, p1_FP_nome_proprio=None,
        p1_FP_pessoa_da_interlocucao=None, p1_FP_transitividade_verbo=None, p1_FP_tonicidade=None,
        p1_FP_morfologia_do_pronome=None, p1_FP_reflexivo=None, p1_FP_adjetivo_epiteto=None,
        p1_FP_adjetivo_classificador=None, p1_FP_genero_adjetivo=None, p1_FP_numero_adjetivo=None, p1_FP_contracao=None,
        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
        p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_funcao_numerativo=None,
        p2_cardinal=None, p2_genero=None, p2_tipo_precisa=None, p2_tipo_real_card=None, p2_milharExtenso=None,
        p2_centenaExtenso=None, p2_dezenaExtenso=None, p2_unidadeExtenso=None, p2_numIndefinido=None,
        p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
        p2_numero=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None, p2_nome_proprio=None,
        p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
        p2_reflexivo=None, p2_adjetivo_epiteto=None, p2_adjetivo_classificador=None, p2_genero_adjetivo=None,
        p2_numero_adjetivo=None, p2_contracao=None,
        # P2 FRASE PREP
        p2_FP_indice_preposicao_frase=None, p2_FP_dissoc_ente_nucleo=None, p2_FP_tem_qualificador=None,
        p2_FP_tipo_qualificador=None, p2_FP_indice_preposicao_qualif=None, p2_FP_determinacao_especificidade_beta=None,
        p2_FP_orientacao_beta=None, p2_FP_genero_beta=None, p2_FP_numero_beta=None,
        p2_FP_morfologia_do_pronome_beta=None, p2_FP_determinacao_especificidade_alpha=None,
        p2_FP_orientacao_alpha=None, p2_FP_genero_alpha=None, p2_FP_numero_alpha=None,
        p2_FP_morfologia_do_pronome_alpha=None, p2_FP_pessoa_da_interlocucao_possuidor=None,
        p2_FP_numero_obj_possuido=None, p2_FP_genero_obj_possuido=None, p2_FP_pessoa_da_interlocucao_proximidade=None,
        p2_FP_funcao_numerativo=None, p2_FP_cardinal=None, p2_FP_genero=None, p2_FP_tipo_precisa=None,
        p2_FP_tipo_real_card=None, p2_FP_milharExtenso=None, p2_FP_centenaExtenso=None, p2_FP_dezenaExtenso=None,
        p2_FP_unidadeExtenso=None, p2_FP_numIndefinido=None, p2_FP_tipo_de_ente=None, p2_FP_tipo_de_nao_consciente=None,
        p2_FP_tipo_de_nao_consciente_material=None, p2_FP_tipo_de_nao_consciente_semiotico=None,
        p2_FP_classe_palavra_ente=None, p2_FP_substantivo_lematizado=None, p2_FP_numero=None,
        p2_FP_tipo_feminino_ao=None, p2_FP_tipo_masc_ao=None, p2_FP_acent_tonica=None, p2_FP_nome_proprio=None,
        p2_FP_pessoa_da_interlocucao=None, p2_FP_transitividade_verbo=None, p2_FP_tonicidade=None,
        p2_FP_morfologia_do_pronome=None, p2_FP_reflexivo=None, p2_FP_adjetivo_epiteto=None,
        p2_FP_adjetivo_classificador=None, p2_FP_genero_adjetivo=None, p2_FP_numero_adjetivo=None, p2_FP_contracao=None,
        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
        p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_funcao_numerativo=None,
        p3_cardinal=None, p3_genero=None, p3_tipo_precisa=None, p3_tipo_real_card=None, p3_milharExtenso=None,
        p3_centenaExtenso=None, p3_dezenaExtenso=None, p3_unidadeExtenso=None, p3_numIndefinido=None,
        p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
        p3_numero=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None, p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None, p3_adjetivo_epiteto=None, p3_adjetivo_classificador=None, p3_genero_adjetivo=None,
        p3_numero_adjetivo=None, p3_contracao=None,
        ## P3 REALIZADOS POR FP
        p3_FP_indice_preposicao_frase=None, p3_FP_dissoc_ente_nucleo=None, p3_FP_tem_qualificador=None,
        p3_FP_tipo_qualificador=None, p3_FP_indice_preposicao_qualif=None, p3_FP_determinacao_especificidade_beta=None,
        p3_FP_orientacao_beta=None, p3_FP_genero_beta=None, p3_FP_numero_beta=None,
        p3_FP_morfologia_do_pronome_beta=None, p3_FP_determinacao_especificidade_alpha=None,
        p3_FP_orientacao_alpha=None, p3_FP_genero_alpha=None, p3_FP_numero_alpha=None,
        p3_FP_morfologia_do_pronome_alpha=None, p3_FP_pessoa_da_interlocucao_possuidor=None,
        p3_FP_numero_obj_possuido=None, p3_FP_genero_obj_possuido=None, p3_FP_pessoa_da_interlocucao_proximidade=None,
        p3_FP_funcao_numerativo=None, p3_FP_cardinal=None, p3_FP_genero=None, p3_FP_tipo_precisa=None,
        p3_FP_tipo_real_card=None, p3_FP_milharExtenso=None, p3_FP_centenaExtenso=None, p3_FP_dezenaExtenso=None,
        p3_FP_unidadeExtenso=None, p3_FP_numIndefinido=None, p3_FP_tipo_de_ente=None, p3_FP_tipo_de_nao_consciente=None,
        p3_FP_tipo_de_nao_consciente_material=None, p3_FP_tipo_de_nao_consciente_semiotico=None,
        p3_FP_classe_palavra_ente=None, p3_FP_substantivo_lematizado=None, p3_FP_numero=None,
        p3_FP_tipo_feminino_ao=None, p3_FP_tipo_masc_ao=None, p3_FP_acent_tonica=None, p3_FP_nome_proprio=None,
        p3_FP_pessoa_da_interlocucao=None, p3_FP_transitividade_verbo=None, p3_FP_tonicidade=None,
        p3_FP_morfologia_do_pronome=None, p3_FP_reflexivo=None, p3_FP_adjetivo_epiteto=None,
        p3_FP_adjetivo_classificador=None, p3_FP_genero_adjetivo=None, p3_FP_numero_adjetivo=None, p3_FP_contracao=None,
):
    try:
        transitividade_ = transitividade(TIPO_DE_PROCESSO, indice_material, indice_agenciamento, indice_relacional)
        Modo = modo(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = tema_interpessoal(TIPO_TEMA_INTERPESSOAL, t_inter_tipoRealizacao, t_inter_tipo_de_adverbio1,
                                              t_inter_ind1, t_inter_tipo_de_adverbio2, t_inter_ind2,
                                              t_inter_tipo_de_adverbio3, t_inter_ind3, t_inter_tipo_de_adverbio4,
                                              t_inter_ind4, t_inter_tipo_de_adverbio5, t_inter_ind5,
                                              t_inter_fp_indice_preposicao_frase, t_inter_fp_dissoc_ente_nucleo,
                                              t_inter_fp_tem_qualificador, t_inter_fp_tipo_qualificador,
                                              t_inter_fp_indice_preposicao_qualif,
                                              t_inter_fp_determinacao_especificidade_beta, t_inter_fp_orientacao_beta,
                                              t_inter_fp_genero_beta, t_inter_fp_numero_beta,
                                              t_inter_fp_morfologia_do_pronome_beta,
                                              t_inter_fp_determinacao_especificidade_alpha, t_inter_fp_orientacao_alpha,
                                              t_inter_fp_genero_alpha, t_inter_fp_numero_alpha,
                                              t_inter_fp_morfologia_do_pronome_alpha,
                                              t_inter_fp_pessoa_da_interlocucao_possuidor,
                                              t_inter_fp_numero_obj_possuido, t_inter_fp_genero_obj_possuido,
                                              t_inter_fp_pessoa_da_interlocucao_proximidade,
                                              t_inter_fp_funcao_numerativo, t_inter_fp_cardinal, t_inter_fp_genero,
                                              t_inter_fp_tipo_precisa, t_inter_fp_tipo_real_card,
                                              t_inter_fp_milharExtenso, t_inter_fp_centenaExtenso,
                                              t_inter_fp_dezenaExtenso, t_inter_fp_unidadeExtenso,
                                              t_inter_fp_numIndefinido, t_inter_fp_tipo_de_ente,
                                              t_inter_fp_tipo_de_nao_consciente,
                                              t_inter_fp_tipo_de_nao_consciente_material,
                                              t_inter_fp_tipo_de_nao_consciente_semiotico,
                                              t_inter_fp_classe_palavra_ente, t_inter_fp_substantivo_lematizado,
                                              t_inter_fp_numero, t_inter_fp_tipo_feminino_ao, t_inter_fp_tipo_masc_ao,
                                              t_inter_fp_acent_tonica, t_inter_fp_nome_proprio,
                                              t_inter_fp_pessoa_da_interlocucao, t_inter_fp_transitividade_verbo,
                                              t_inter_fp_tonicidade, t_inter_fp_morfologia_do_pronome,
                                              t_inter_fp_reflexivo, t_inter_fp_adjetivo_epiteto,
                                              t_inter_fp_adjetivo_classificador, t_inter_fp_genero_adjetivo,
                                              t_inter_fp_numero_adjetivo, t_inter_fp_contracao, t_inter_indice_elem_qu,
                                              t_inter_indice_part_modal, t_inter_nome_proprio)
        Tema_textual = tema_textual(t_text_tem_tema_textual, t_text_tipo_insercao_cont, t_text_indiceCont,
                                    t_text_tipo_de_conjuncao_Conj, t_text_conj_extensoConj, t_text_indiceConj,
                                    t_text_tipo_insercao_Rel, t_text_pron_extenso_Rel, t_text_tipo_de_relativo,
                                    t_text_tipo_pronome_relativo, t_text_generoTemaTextual, t_text_numeroTemaTextual)
        tema_id = tema_ideacional(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        polar = polaridade(tipo_polaridade)
        Processo = grupo_verbal(tipo_de_experiencia_gv, agencia, tipo_de_experiencia_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, oi_numero_1, genero_1, oi_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, tipo_de_experiencia_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, oi_numero_2, genero_2, oi_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, tipo_de_experiencia_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, oi_numero_3, genero_3, oi_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, tipo_de_experiencia_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, oi_numero_4, genero_4, oi_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final,
                                verbo_lex, tipo_de_orientacao_lex, oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                padrao_pessoa_morfologia_lex)
        Circunstancia = circunstancia(CIRC_ORACAO_realizacaoCircunstancia, CIRC_ORACAO_indice_preposicao_frase,
                                      CIRC_ORACAO_dissoc_ente_nucleo, CIRC_ORACAO_tem_qualificador,
                                      CIRC_ORACAO_tipo_qualificador, CIRC_ORACAO_indice_preposicao_qualif,
                                      CIRC_ORACAO_determinacao_especificidade_beta, CIRC_ORACAO_orientacao_beta,
                                      CIRC_ORACAO_genero_beta, CIRC_ORACAO_numero_beta,
                                      CIRC_ORACAO_morfologia_do_pronome_beta,
                                      CIRC_ORACAO_determinacao_especificidade_alpha, CIRC_ORACAO_orientacao_alpha,
                                      CIRC_ORACAO_genero_alpha, CIRC_ORACAO_numero_alpha,
                                      CIRC_ORACAO_morfologia_do_pronome_alpha,
                                      CIRC_ORACAO_pessoa_da_interlocucao_possuidor, CIRC_ORACAO_numero_obj_possuido,
                                      CIRC_ORACAO_genero_obj_possuido, CIRC_ORACAO_pessoa_da_interlocucao_proximidade,
                                      cardinal=CIRC_ORACAO_cardinal, genero_numerativo=CIRC_ORACAO_numIndefinido,
                                      tipo_de_ente=CIRC_ORACAO_tipo_de_ente,
                                      tipo_de_nao_consciente=CIRC_ORACAO_tipo_de_nao_consciente,
                                      tipo_de_nao_consciente_material=CIRC_ORACAO_tipo_de_nao_consciente_material,
                                      tipo_de_nao_consciente_semiotico=CIRC_ORACAO_tipo_de_nao_consciente_semiotico,
                                      classe_palavra_ente=CIRC_ORACAO_classe_palavra_ente,
                                      substantivo_lematizado=CIRC_ORACAO_substantivo_lematizado,
                                      numero=CIRC_ORACAO_numero, tipo_feminino_ao=CIRC_ORACAO_tipo_feminino_ao,
                                      tipo_masc_ao=CIRC_ORACAO_tipo_masc_ao, acent_tonica=CIRC_ORACAO_acent_tonica,
                                      nome_prop=CIRC_ORACAO_nome_proprio,
                                      pessoa_da_interlocucao=CIRC_ORACAO_pessoa_da_interlocucao,
                                      transitividade_verbo=CIRC_ORACAO_transitividade_verbo,
                                      tonicidade=CIRC_ORACAO_tonicidade,
                                      morfologia_do_pronome=CIRC_ORACAO_morfologia_do_pronome,
                                      reflexivo=CIRC_ORACAO_reflexivo, adjetivo_epiteto=CIRC_ORACAO_adjetivo_epiteto,
                                      adjetivo_classificador=CIRC_ORACAO_adjetivo_classificador,
                                      genero_adjetivo=CIRC_ORACAO_genero_adjetivo,
                                      numero_adjetivo=CIRC_ORACAO_numero_adjetivo, contracao=CIRC_ORACAO_contracao,
                                      tipo_de_adverbio1=CIRC_ORACAO_tipo_de_adverbio1, ind1=CIRC_ORACAO_ind1,
                                      tipo_de_adverbio2=CIRC_ORACAO_tipo_de_adverbio2, ind2=CIRC_ORACAO_ind2,
                                      tipo_de_adverbio3=CIRC_ORACAO_tipo_de_adverbio3, ind3=CIRC_ORACAO_ind3,
                                      tipo_de_adverbio4=CIRC_ORACAO_tipo_de_adverbio4, ind4=CIRC_ORACAO_ind4,
                                      tipo_de_adverbio5=CIRC_ORACAO_tipo_de_adverbio5, ind5=CIRC_ORACAO_ind5)
        Dizente = estrutura_gn(p1_dissoc_ente_nucleo, p1_tem_qualificador, p1_tipo_qualificador,
                               p1_indice_preposicao_qualif, p1_determinacao_especificidade_beta, p1_orientacao_beta,
                               p1_genero_beta, p1_numero_beta, p1_morfologia_do_pronome_beta,
                               p1_determinacao_especificidade_alpha, p1_orientacao_alpha, p1_genero_alpha,
                               p1_numero_alpha, p1_morfologia_do_pronome_alpha, p1_pessoa_da_interlocucao_possuidor,
                               p1_numero_obj_possuido, p1_genero_obj_possuido, p1_pessoa_da_interlocucao_proximidade,
                               p1_funcao_numerativo, p1_cardinal, p1_genero, p1_tipo_precisa, p1_tipo_real_card,
                               p1_milharExtenso, p1_centenaExtenso, p1_dezenaExtenso, p1_unidadeExtenso,
                               p1_numIndefinido, p1_tipo_de_ente, p1_tipo_de_nao_consciente,
                               p1_tipo_de_nao_consciente_material, p1_tipo_de_nao_consciente_semiotico,
                               p1_classe_palavra_ente, p1_substantivo_lematizado, p1_numero, p1_tipo_feminino_ao,
                               p1_tipo_masc_ao, p1_acent_tonica, p1_nome_proprio, p1_pessoa_da_interlocucao,
                               p1_transitividade_verbo, p1_tonicidade, p1_morfologia_do_pronome)
        if RECEPTIVIDADE == '+receptor':
            Receptor = frase_preposicional(p3_FP_indice_preposicao_frase, p3_FP_dissoc_ente_nucleo,
                                           p3_FP_tem_qualificador, p3_FP_tipo_qualificador,
                                           p3_FP_indice_preposicao_qualif, p3_FP_determinacao_especificidade_beta,
                                           p3_FP_orientacao_beta, p3_FP_genero_beta, p3_FP_numero_beta,
                                           p3_FP_morfologia_do_pronome_beta, p3_FP_determinacao_especificidade_alpha,
                                           p3_FP_orientacao_alpha, p3_FP_genero_alpha, p3_FP_numero_alpha,
                                           p3_FP_morfologia_do_pronome_alpha, p3_FP_pessoa_da_interlocucao_possuidor,
                                           p3_FP_numero_obj_possuido, p3_FP_genero_obj_possuido,
                                           p3_FP_pessoa_da_interlocucao_proximidade, p3_FP_funcao_numerativo,
                                           p3_FP_cardinal, p3_FP_genero, p3_FP_tipo_precisa, p3_FP_tipo_real_card,
                                           p3_FP_milharExtenso, p3_FP_centenaExtenso, p3_FP_dezenaExtenso,
                                           p3_FP_unidadeExtenso, p3_FP_numIndefinido, p3_FP_tipo_de_ente,
                                           p3_FP_tipo_de_nao_consciente, p3_FP_tipo_de_nao_consciente_material,
                                           p3_FP_tipo_de_nao_consciente_semiotico, p3_FP_classe_palavra_ente,
                                           p3_FP_substantivo_lematizado, p3_FP_numero, p3_FP_tipo_feminino_ao,
                                           p3_FP_tipo_masc_ao, p3_FP_acent_tonica, p3_FP_nome_proprio,
                                           p3_FP_pessoa_da_interlocucao, p3_FP_transitividade_verbo, p3_FP_tonicidade)
        else:
            Receptor = ''

        if transitividade_ == 'PR_Verbal_AG_médio_sem_alcance':
            if MODO_DO_DIZENTE == 'atividade_fala' or MODO_DO_DIZENTE == 'semioticidade':

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Dizente, polar, Processo, Receptor + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Dizente, polar, Processo, Receptor + '?'))
            # Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...
            elif MODO_DO_DIZENTE == 'semioticidade':
                TIPO_SEMIOTICIDADE == 'não_projeção_-verbiagem'
                if TIPO_SEMIOTICIDADE == 'não_projeção_-verbiagem':
                    # print('Não-projeção + médio sem alcance = -verbiagem')
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Dizente, polar, Processo, Receptor + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Dizente, polar, Processo, Receptor + '?'))

        elif transitividade_ == 'PR_Verbal_AG_médio_com_alcance':
            MODO_DO_DIZENTE = 'semioticidade'
            if MODO_DO_DIZENTE == 'semioticidade':
                if TIPO_SEMIOTICIDADE == 'projeção':
                    # REVISAR: inserir parametros para a projetada.
                    oracao_projetada = oraçãoProjetada()
                    if TIPO_PROJECAO == 'citativa':

                        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                            oracao = " ".join((Dizente, polar, Processo, Receptor, '"' + oracao_projetada + '".'))
                        elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                            oracao = " ".join((Dizente, polar, Processo, Receptor, '"' + oracao_projetada + '"?'))

                    # Ex.: Eu disse a ele "Eu comi o bolo".

                    elif TIPO_PROJECAO == 'relativa':
                        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                            oracao = " ".join(
                                (Dizente, polar, Processo, Receptor, 'que "' + oracao_projetada + '".'))
                        elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                            oracao = " ".join(
                                (Dizente, polar, Processo, Receptor, 'que "' + oracao_projetada + '"?'))

                    # Ex.: Eu disse a ele que eu havia comido o bolo.

                elif TIPO_SEMIOTICIDADE == 'não_projeção_+verbiagem':
                    Verbiagem = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                             p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                             p2_orientacao_beta, p2_genero_beta, p2_numero_beta,
                                             p2_morfologia_do_pronome_beta, p2_determinacao_especificidade_alpha,
                                             p2_orientacao_alpha, p2_genero_alpha, p2_numero_alpha,
                                             p2_morfologia_do_pronome_alpha, p2_pessoa_da_interlocucao_possuidor,
                                             p2_numero_obj_possuido, p2_genero_obj_possuido,
                                             p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal,
                                             p2_genero, p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso,
                                             p2_centenaExtenso, p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido,
                                             p2_tipo_de_ente, p2_tipo_de_nao_consciente,
                                             p2_tipo_de_nao_consciente_material, p2_tipo_de_nao_consciente_semiotico,
                                             p2_classe_palavra_ente, p2_substantivo_lematizado, p2_numero,
                                             p2_tipo_feminino_ao, p2_tipo_masc_ao, p2_acent_tonica, p2_nome_proprio,
                                             p2_pessoa_da_interlocucao, p2_transitividade_verbo, p2_tonicidade,
                                             p2_morfologia_do_pronome)
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Dizente, polar, Processo, Verbiagem, Receptor + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Dizente, polar, Processo, Verbiagem, Receptor + '?'))


        elif transitividade_ == 'PR_Verbal_AG_efetivo_operativo':
            if MODO_DO_DIZENTE == 'atividade_alvo':
                Alvo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                    p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                    p2_orientacao_beta, p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                    p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                    p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                    p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido, p2_genero_obj_possuido,
                                    p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal, p2_genero,
                                    p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso, p2_centenaExtenso,
                                    p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido, p2_tipo_de_ente,
                                    p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                    p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                    p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                    p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                    p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Dizente, polar, Processo, Alvo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Dizente, polar, Processo, Alvo + '?'))
            # Ex.: Eu acusei o padeiro

        elif transitividade_ == 'PR_Verbal_AG_efetivo_receptivo':
            if MODO_DO_DIZENTE == 'atividade_alvo':
                Dizente = frase_preposicional(p1_FP_indice_preposicao_frase, p1_FP_dissoc_ente_nucleo,
                                              p1_FP_tem_qualificador, p1_FP_tipo_qualificador,
                                              p1_FP_indice_preposicao_qualif, p1_FP_determinacao_especificidade_beta,
                                              p1_FP_orientacao_beta, p1_FP_genero_beta, p1_FP_numero_beta,
                                              p1_FP_morfologia_do_pronome_beta, p1_FP_determinacao_especificidade_alpha,
                                              p1_FP_orientacao_alpha, p1_FP_genero_alpha, p1_FP_numero_alpha,
                                              p1_FP_morfologia_do_pronome_alpha, p1_FP_pessoa_da_interlocucao_possuidor,
                                              p1_FP_numero_obj_possuido, p1_FP_genero_obj_possuido,
                                              p1_FP_pessoa_da_interlocucao_proximidade, p1_FP_funcao_numerativo,
                                              p1_FP_cardinal, p1_FP_genero, p1_FP_tipo_precisa, p1_FP_tipo_real_card,
                                              p1_FP_milharExtenso, p1_FP_centenaExtenso, p1_FP_dezenaExtenso,
                                              p1_FP_unidadeExtenso, p1_FP_numIndefinido, p1_FP_tipo_de_ente,
                                              p1_FP_tipo_de_nao_consciente, p1_FP_tipo_de_nao_consciente_material,
                                              p1_FP_tipo_de_nao_consciente_semiotico, p1_FP_classe_palavra_ente,
                                              p1_FP_substantivo_lematizado, p1_FP_numero, p1_FP_tipo_feminino_ao,
                                              p1_FP_tipo_masc_ao, p1_FP_acent_tonica, p1_FP_nome_proprio,
                                              p1_FP_pessoa_da_interlocucao, p1_FP_transitividade_verbo,
                                              p1_FP_tonicidade)
                Alvo = estrutura_gn(p2_dissoc_ente_nucleo, p2_tem_qualificador, p2_tipo_qualificador,
                                    p2_indice_preposicao_qualif, p2_determinacao_especificidade_beta,
                                    p2_orientacao_beta, p2_genero_beta, p2_numero_beta, p2_morfologia_do_pronome_beta,
                                    p2_determinacao_especificidade_alpha, p2_orientacao_alpha, p2_genero_alpha,
                                    p2_numero_alpha, p2_morfologia_do_pronome_alpha,
                                    p2_pessoa_da_interlocucao_possuidor, p2_numero_obj_possuido, p2_genero_obj_possuido,
                                    p2_pessoa_da_interlocucao_proximidade, p2_funcao_numerativo, p2_cardinal, p2_genero,
                                    p2_tipo_precisa, p2_tipo_real_card, p2_milharExtenso, p2_centenaExtenso,
                                    p2_dezenaExtenso, p2_unidadeExtenso, p2_numIndefinido, p2_tipo_de_ente,
                                    p2_tipo_de_nao_consciente, p2_tipo_de_nao_consciente_material,
                                    p2_tipo_de_nao_consciente_semiotico, p2_classe_palavra_ente,
                                    p2_substantivo_lematizado, p2_numero, p2_tipo_feminino_ao, p2_tipo_masc_ao,
                                    p2_acent_tonica, p2_nome_proprio, p2_pessoa_da_interlocucao,
                                    p2_transitividade_verbo, p2_tonicidade, p2_morfologia_do_pronome)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Alvo, polar, Processo, Dizente + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Alvo, polar, Processo, Dizente + '?'))

        return (re.sub(' +', ' ', oracao.strip()).capitalize())
    except:
        return ""


# O homem acusou o padeiro
oracaoVerbal(
    ##TRANSITIVIDADE
    'Verbal', None, 2, None,
    # MODO
    0, 0, 1,
    # TEMA IDEACIONAL
    'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA', None, None, None,
    ##PARAMETROS DO PROCESSO VERBAL
    'atividade_alvo', None, None, None,
    ##Processo
    'Sentir', 'não_agenciado', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'Sentir',
    'Evento', 'acusar',
    'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão',
    # POLARIDADE
    'positiva',
    ##PARTICIPANTES
    # P1
    None, None, None, None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None,
    None, None, None, None, None, 'não-binário', None, None, None, None, None, None, None,
    'não_consciente', 'material', 'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    ##PARTICIPANTE P1 REALIZADOS POR FP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    # P2

    None, None, None, None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None,
    None, None, None, None, None, 'masculino', None, None, None, None, None, None, None,
    'não_consciente', 'material', 'abstração_material', None, 'substantivo_comum', 'padeiro', 'singular', None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    # P2 FRASE PREP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None,

    # P3
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,
    ##PARTICIPANTE P3 REALIZADOS POR FP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None)

oracaoVerbal(
    ##TRANSITIVIDADE
    'Verbal', None, 0, None,
    # MODO
    0, 0, 1,
    # TEMA IDEACIONAL
    'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA', None, None, None,
    ##PARAMETROS DO PROCESSO VERBAL
    'semioticidade', 'não_projeção_-verbiagem', None, None,
    ##Processo
    'Sentir', 'não_agenciado', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'Sentir',
    'Evento', 'falar',
    'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão',
    # POLARIDADE
    'positiva',
    ##PARTICIPANTES
    # P1
    None, None, None, None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None,
    None, None, None, None, None, 'não-binário', None, None, None, None, None, None, None,
    'não_consciente', 'material', 'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    ##PARTICIPANTE P1 REALIZADOS POR FP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    # P2

    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    # P2 FRASE PREP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None,

    # P3
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,
    ##PARTICIPANTE P3 REALIZADOS POR FP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None)

oracaoVerbal(
    ##TRANSITIVIDADE
    'Verbal', None, 0, None,
    # MODO
    0, 0, 1,
    # TEMA IDEACIONAL
    'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA', None, None, None,
    ##PARAMETROS DO PROCESSO VERBAL
    'atividade_fala', None, None, None,
    ##Processo
    'Sentir', 'não_agenciado', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'Sentir',
    'Evento', 'falar',
    'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão',
    # POLARIDADE
    'positiva',
    ##PARTICIPANTES
    # P1
    None, None, None, None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None,
    None, None, None, None, None, 'não-binário', None, None, None, None, None, None, None,
    'não_consciente', 'material', 'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    ##PARTICIPANTE P1 REALIZADOS POR FP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    # P2

    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,

    # P2 FRASE PREP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None,

    # P3
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None,
    ##PARTICIPANTE P3 REALIZADOS POR FP
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None)
