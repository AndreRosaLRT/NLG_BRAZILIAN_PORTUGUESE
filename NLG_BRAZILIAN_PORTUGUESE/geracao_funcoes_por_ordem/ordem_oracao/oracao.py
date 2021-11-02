from builtins import KeyError, ValueError

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
            circ = estrutura_gn(dissoc_ente_nucleo, tem_qualificador, tipo_qualificador,
                                          indice_preposicao_qualif, determinacao_especificidade_beta,
                                          orientacao_beta,
                                          genero_beta, numero_beta, morfologia_do_pronome_beta,
                                          determinacao_especificidade_alpha, orientacao_alpha, genero_alpha,
                                          numero_alpha, morfologia_do_pronome_alpha,
                                          pessoa_da_interlocucao_possuidor, numero_obj_possuido,
                                          genero_obj_possuido, pessoa_da_interlocucao_proximidade,
                                          tipo_numerativo, cardinal, genero_numerativo, tipo_de_ente,
                                          tipo_de_nao_consciente,
                                          tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
                                          classe_palavra_ente, substantivo_lematizado, numero,
                                          tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_prop,
                                          pessoa_da_interlocucao, transitividade_verbo, tonicidade,
                                          morfologia_do_pronome, reflexivo, adjetivo_epiteto,
                                          adjetivo_classificador, genero_adjetivo, numero_adjetivo, contracao)
        elif realizacao_circunstancia == 'frase_preposicional':
            circ = frase_preposicional(indice_preposicao_frase, dissoc_ente_nucleo, tem_qualificador,
                                       tipo_qualificador, indice_preposicao_qualif, determinacao_especificidade_beta,
                                       orientacao_beta,
                                       genero_beta, numero_beta, morfologia_do_pronome_beta,
                                       determinacao_especificidade_alpha, orientacao_alpha, genero_alpha,
                                       numero_alpha, morfologia_do_pronome_alpha, pessoa_da_interlocucao_possuidor,
                                       numero_obj_possuido, genero_obj_possuido, pessoa_da_interlocucao_proximidade,
                                       tipo_numerativo, cardinal, genero_numerativo, tipo_de_ente,
                                       tipo_de_nao_consciente,
                                       tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
                                       classe_palavra_ente, substantivo_lematizado, numero,
                                       tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_prop,
                                       pessoa_da_interlocucao, transitividade_verbo, tonicidade,
                                       morfologia_do_pronome, reflexivo,
                                       adjetivo_epiteto,
                                       adjetivo_classificador, genero_adjetivo, numero_adjetivo,
                                       contracao)
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
    except (KeyError,ValueError,TypeError):
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
	    "PR_material_transformativo_IMPA_transitivo"
        "PR_material_criativo_IMPA_transitivo"
        "PR_material_transformativo_IMPA_intransitivo"
        "PR_material_criativo_IMPA_intransitivo"

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

    except (KeyError,ValueError,TypeError):
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



def tipo_de_modo(indice_modo):
    """

    :param indice_modo: 'MOD_declarativo_+perguntafinito', 'MOD_declarativo_-perguntafinito',
                       'MOD_interrogativo_elemental','MOD_interrogativo_polar',
                       'MOD_imperativo'
    :return: tipo de modo
    """
    opcoes = ['MOD_declarativo_+perguntafinito', 'MOD_declarativo_-perguntafinito',
              'MOD_interrogativo_elemental', 'MOD_interrogativo_polar',
              'MOD_imperativo']
    try:
        nums = [x for x in range(len(opcoes))]
        tiposModo = dict(zip(nums, opcoes))
        tipoModo = tiposModo[indice_modo]
    except:
        tipoModo = 'MOD_declarativo_-perguntafinito'
    return tipoModo


# TIPO_DE_MODO(3)
# #
# # ########
# #
# #
# # ######


def AVALIACAO_MODAL(AVALIACAO=None, POLARIDADE=None):
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

def TIPO_AVALIACAO_MODAL(AVALIACAO=None, POLARIDADE=None):
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

def MODO(RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None):
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
    MODO = sujeitabilidade(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO) + '_' + tipo_de_modo(TIPO_MODO)
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


def conjuncao_continuativa(tipo_insercao="inserção_menu", indice=None, conj_extenso=None):
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
            opcoes = ["e", "é", "ah", 'mas', 'sim', 'bem', 'não', 'agora', 'então', 'pois é', 'assim'
                , 'ó', 'daí', 'aí', 'aí então', 'quer dizer', 'assim', 'em seguida', 'por fim'
                , 'porque', 'porém', 'também', 'é que', 'olha']

            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]
        else:
            conjuncao = conj_extenso
        return conjuncao
    except:
        conjuncao = ''
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

def TEMA_TEXTUAL(temTemaTextual=None, tipo_insercao_Cont="inserção_menu", conj_extenso_Cont=None, indiceCont=None,
                 tipo_insercao_Conj="inserção_menu", tipo_de_conjuncao_Conj=None, conj_extensoConj=None,
                 indiceConj=None,
                 tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None, tipo_de_relativo=None,
                 tipo_pronome_relativo=None, genero=None, numero=None, indiceRelativo=None, indiceRelativoAdv=None):
    try:
        if temTemaTextual == '+':
            TEMA_CONTINUATIVO = conjuncao_continuativa(tipo_insercao_Cont, indiceCont, conj_extenso_Cont)
            TEMA_CONJUNTIVO = grupo_conjuntivo(tipo_insercao_Conj, conj_extensoConj, tipo_de_conjuncao_Conj, indiceConj)

            if tipo_de_relativo == 'nominal':
                TEMA_RELATIVO = pronome_relativo(tipo_insercao_Rel, pron_extenso_Rel, tipo_pronome_relativo, genero,
                                                 numero, indiceRelativo)
            elif tipo_de_relativo == 'adverbial':
                opcoes = ['de onde', 'quando',
                          'onde', 'de quando', 'que', 'por onde']

                nums = [x for x in range(len(opcoes))]
                relativos = dict(zip(nums, opcoes))
                TEMA_RELATIVO = relativos[indiceRelativoAdv]
            else:
                TEMA_RELATIVO = ''
        TEMA_TEXTUAL = TEMA_CONTINUATIVO + ' ' + TEMA_CONJUNTIVO + ' ' + TEMA_RELATIVO
    except:
        TEMA_TEXTUAL = ''
    return TEMA_TEXTUAL


TEMA_TEXTUAL('+', "inserção_menu", None, 3, "inserção_menu", None, None, None, 'inserção_menu', None, None, None, None,
             None, None, None)

TEMA_TEXTUAL(temTemaTextual='+',
             tipo_insercao_Cont="inserção_menu", indiceCont=3, conj_extenso_Cont=None,
             tipo_insercao_Conj="inserção_menu", tipo_de_conjuncao_Conj=None, conj_extensoConj=None, indiceConj=None,
             tipo_insercao_Rel='inserção_menu', pron_extenso_Rel=None, tipo_de_relativo=None,
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


def TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL=None, tipoRealizacao=None,
                      # grupo adverbial
                      tipo_de_adverbio1=None, ind1=None,
                      tipo_de_adverbio2=None, ind2=None,
                      tipo_de_adverbio3=None, ind3=None,
                      tipo_de_adverbio4=None, ind4=None,
                      tipo_de_adverbio5=None, ind5=None,

                      # frase prepos
                      indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
                      tipo_qualificador=None, indice_preposicao_qualif=None, determinacao_especificidade_beta=None,
                      orientacao_beta=None, genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
                      determinacao_especificidade_alpha=None, orientacao_alpha=None, genero_alpha=None,
                      numero_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
                      numero_obj_possuido=None, genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
                      funcao_numerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipo_real_card=None,
                      milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
                      numIndefinido=None, tipo_de_ente=None, tipo_de_nao_consciente=None,
                      tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
                      classe_palavra_ente=None, substantivo_lematizado=None, numero=None,
                      tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
                      pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                      morfologia_do_pronome=None, reflexivo=None,
                      adjetivo_epiteto=None,
                      adjetivo_classificador=None, genero_adjetivo=None, numero_adjetivo=None,
                      contracao=None,

                      #
                      indiceElemQu=None, indicePartModal=None,
                      nome_proprio=None):
    try:

        if (TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_modo' or TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_comentário'):
            if tipoRealizacao == 'grupo_adverbial':
                TEMA_INT = grupo_adverbial(tipo_de_adverbio1, ind1,
                                           tipo_de_adverbio2, ind2,
                                           tipo_de_adverbio3, ind3,
                                           tipo_de_adverbio4, ind4,
                                           tipo_de_adverbio5, ind5, )
            elif tipoRealizacao == 'frase_preposicional':
                TEMA_INT = frase_preposicional(indice_preposicao_frase, dissoc_ente_nucleo, tem_qualificador,
                                               tipo_qualificador, indice_preposicao_qualif,
                                               determinacao_especificidade_beta, orientacao_beta,
                                               genero_beta, numero_beta, morfologia_do_pronome_beta,
                                               determinacao_especificidade_alpha, orientacao_alpha, genero_alpha,
                                               numero_alpha, morfologia_do_pronome_alpha,
                                               pessoa_da_interlocucao_possuidor,
                                               numero_obj_possuido, genero_obj_possuido,
                                               pessoa_da_interlocucao_proximidade,
                                               funcao_numerativo, cardinal, genero, tipo_precisa, tipo_real_card,
                                               milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                               numIndefinido, tipo_de_ente, tipo_de_nao_consciente,
                                               tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
                                               classe_palavra_ente, substantivo_lematizado, numero,
                                               tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_proprio,
                                               pessoa_da_interlocucao, transitividade_verbo, tonicidade,
                                               morfologia_do_pronome, reflexivo,
                                               adjetivo_epiteto,
                                               adjetivo_classificador, genero_adjetivo, numero_adjetivo,
                                               contracao)

        elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_troca':
            TEMA_INT = elemento_qu(indiceElemQu)

        elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_falante':
            TEMA_INT = particula_modal(indicePartModal)
        elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_ouvinte':
            TEMA_INT = nome_proprio(nome_proprio)
    except:
        TEMA_INT = ''

    return TEMA_INT


#
# TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL="TI_avaliação_comentário",tipoRealizacao='frase_preposicional',
# 					  #grupo adverbial
# 					  tipo_de_adverbio1=None, ind1=None,
# 					  tipo_de_adverbio2=None, ind2=None,
# 					  tipo_de_adverbio3=None, ind3=None,
# 					  tipo_de_adverbio4=None, ind4=None,
# 					  tipo_de_adverbio5=None, ind5=None,
#
# 					#frase prepos
# 					  indice_preposicao_frase=4, dissoc_ente_nucleo=None, tem_qualificador=None,indice_preposicao_qualif=None,
# 					  tipo_qualificador=None, determinacao_especificidade_beta=None, orientacao_beta=None,
# 					  genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
# 					  determinacao_especificidade_alpha=None, orientacao_alpha=None, genero_alpha=None,
# 					  numero_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
# 					  numero_obj_possuido=None, genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
# 					  funcao_numerativo=None, cardinal=None, genero='não-binário', tipo_precisa=None, tipo_real_card=None,
# 					  milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
# 					  numIndefinido=None, tipo_de_ente='não_consciente', tipo_de_nao_consciente=None,
# 					  tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico='abstração_semiótica',
# 					  classe_palavra_ente='substantivo_comum', substantivo_lematizado='certeza', numero='singular',
# 					  tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
# 					  pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
# 					  morfologia_do_pronome=None, reflexivo=None,
# 					  adjetivo_epiteto=None,
# 					  adjetivo_classificador=None, genero_adjetivo=None, numero_adjetivo=None, contracao=None,
#
# 					#
# 					  indiceElemQu=None, indicePartModal=None,
# 					  nome_proprio=None)
# TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL="TI_avaliação_comentário", tipoRealizacao='frase_preposicional',
# 				  indice_preposicao_frase=4,
# 				  genero='não-binário',
# 				  tipo_de_ente='não_consciente', tipo_de_nao_consciente='semiótico',
# 				  tipo_de_nao_consciente_material=None, classe_palavra_ente='substantivo_comum',
# 				  substantivo_lematizado='certeza', numero='singular'
# 				  )
# #
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


def TEMA_IDEACIONAL(ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None,
                    SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
                    TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None,
                    TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
                    TEMA_PROEMINENTE=None):
    if ORIENTACAO_MODAL == 'orientado' and ORIENTACAO_TRANSITIVA == 'direcional' and SELECAO_TEMATICA == 'default':

        if TEMA_DEFAULT == 'imperativo':
            TEMA_IDEACIONAL = 'TID_default_imperativo'

        elif TEMA_DEFAULT == 'indicativo':

            if TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'NA':

                TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_NA'

            elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO == 'NA':

                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'

            elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO == 'NA':

                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_NA'

            elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':
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

    elif ORIENTACAO_MODAL == 'não_orientado' and ORIENTACAO_TRANSITIVA == 'direcional' and SELECAO_TEMATICA == 'proeminente':
        if TEMA_ANGULO == 'fonte':
            TEMA_IDEACIONAL = 'TID_angulo_fonte'
        elif TEMA_ANGULO == 'ponto_de_vista':
            TEMA_IDEACIONAL = 'TID_angulo_ponto_de_vista'
    elif ORIENTACAO_MODAL == 'orientado' and ORIENTACAO_TRANSITIVA == 'não_direcional' and SELECAO_TEMATICA == 'default':
        if TEMA_ELEMENTAL == 'complemento_elemental':
            TEMA_IDEACIONAL = 'TID_complemento_elemental'
        elif TEMA_ELEMENTAL == 'adjunto_elemental':
            TEMA_IDEACIONAL = 'TID_adjunto_elemental'
    elif ORIENTACAO_MODAL == 'não_orientado' and ORIENTACAO_TRANSITIVA == 'não_direcional' and SELECAO_TEMATICA == 'proeminente':

        TEMA_IDEACIONAL = 'TID_proeminente_' + TEMA_PROEMINENTE

    return TEMA_IDEACIONAL


# TEMA_IDEACIONAL(ORIENTACAO_MODAL='orientado',ORIENTACAO_TRANSITIVA='direcional',
# 				SELECAO_TEMATICA='default', TEMA_DEFAULT='indicativo',
# 				TEMA_DEFAULT_indicativo='declarativo', TEMA_IDENTIFICATIVO='NA',
# 				TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE=None)
# #
# TEMA_IDEACIONAL(ORIENTACAO_MODAL='não_orientado',ORIENTACAO_TRANSITIVA='não_direcional',
# 				SELECAO_TEMATICA='proeminente', TEMA_DEFAULT=None,
# 				TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO='NA',
# 				TEMA_ANGULO=None, TEMA_ELEMENTAL=None, TEMA_PROEMINENTE='intensivo_relativo_papel_transitivo_nuclear_participante')

# intensivo_relativo_papel_transitivo_nuclear_participante

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
        elemento_qu = ''

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
        particula_modal = ''
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

def TRANSITIVIDADE(TIPO_DE_PROCESSO=None, indiceMat=None,
                   indiceAgen=None, indiceRel=None):
    if TIPO_DE_PROCESSO == 'Material':
        Processo = processo_material(indiceMat)
        Agenciamento = agenciamento(indiceAgen)

    elif TIPO_DE_PROCESSO == 'Relacional':
        Processo = processo_relacional(indiceRel)
        Agenciamento = agenciamento(indiceAgen)

    elif TIPO_DE_PROCESSO == 'Existencial':
        Processo = 'PR_Existencial'
        Agenciamento = agenciamento(indiceAgen)

    elif TIPO_DE_PROCESSO == 'Verbal':
        Processo = 'PR_Verbal'
        Agenciamento = agenciamento(indiceAgen)

    elif TIPO_DE_PROCESSO == 'Mental':
        Processo = 'PR_Mental'
        Agenciamento = agenciamento(indiceAgen)

    TRANSITIVIDADE = Processo + '_' + Agenciamento
    return TRANSITIVIDADE


# #'PR_relacional_intensivo_atributivo_sem_atribuição_de_relação_AG_médio_com_alcance':
# TRANSITIVIDADE(TIPO_DE_PROCESSO='Relacional',indiceMat=None, indiceAgen=1, indiceRel=0)

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
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, T_INTER_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        T_INTER_tipo_de_adverbio1=None, T_INTER_ind1=None,
        T_INTER_tipo_de_adverbio2=None, T_INTER_ind2=None,
        T_INTER_tipo_de_adverbio3=None, T_INTER_ind3=None,
        T_INTER_tipo_de_adverbio4=None, T_INTER_ind4=None,
        T_INTER_tipo_de_adverbio5=None, T_INTER_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        T_INTER_FP_indice_preposicao_frase=None, T_INTER_FP_dissoc_ente_nucleo=None, T_INTER_FP_tem_qualificador=None,
        T_INTER_FP_tipo_qualificador=None, T_INTER_FP_indice_preposicao_qualif=None,
        T_INTER_FP_determinacao_especificidade_beta=None, T_INTER_FP_orientacao_beta=None, T_INTER_FP_genero_beta=None,
        T_INTER_FP_numero_beta=None, T_INTER_FP_morfologia_do_pronome_beta=None,
        T_INTER_FP_determinacao_especificidade_alpha=None, T_INTER_FP_orientacao_alpha=None,
        T_INTER_FP_genero_alpha=None, T_INTER_FP_numero_alpha=None, T_INTER_FP_morfologia_do_pronome_alpha=None,
        T_INTER_FP_pessoa_da_interlocucao_possuidor=None, T_INTER_FP_numero_obj_possuido=None,
        T_INTER_FP_genero_obj_possuido=None, T_INTER_FP_pessoa_da_interlocucao_proximidade=None,
        T_INTER_FP_funcao_numerativo=None, T_INTER_FP_cardinal=None, T_INTER_FP_genero=None,
        T_INTER_FP_tipo_precisa=None, T_INTER_FP_tipo_real_card=None, T_INTER_FP_milharExtenso=None,
        T_INTER_FP_centenaExtenso=None, T_INTER_FP_dezenaExtenso=None, T_INTER_FP_unidadeExtenso=None,
        T_INTER_FP_numIndefinido=None, T_INTER_FP_tipo_de_ente=None, T_INTER_FP_tipo_de_nao_consciente=None,
        T_INTER_FP_tipo_de_nao_consciente_material=None, T_INTER_FP_tipo_de_nao_consciente_semiotico=None,
        T_INTER_FP_classe_palavra_ente=None, T_INTER_FP_substantivo_lematizado=None, T_INTER_FP_numero=None,
        T_INTER_FP_tipo_feminino_ao=None, T_INTER_FP_tipo_masc_ao=None, T_INTER_FP_acent_tonica=None,
        T_INTER_FP_nome_proprio=None, T_INTER_FP_pessoa_da_interlocucao=None, T_INTER_FP_transitividade_verbo=None,
        T_INTER_FP_tonicidade=None, T_INTER_FP_morfologia_do_pronome=None, T_INTER_FP_reflexivo=None,
        T_INTER_FP_adjetivo_epiteto=None, T_INTER_FP_adjetivo_classificador=None, T_INTER_FP_genero_adjetivo=None,
        T_INTER_FP_numero_adjetivo=None, T_INTER_FP_contracao=None,
        #
        # 		#
        T_INTER_indiceElemQu=None, T_INTER_indicePartModal=None, T_INTER_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        T_TEXT_temTemaTextual='-', T_TEXT_tipo_insercao_Cont="inserção_menu", T_TEXT_conj_extenso_Cont=None,
        T_TEXT_indiceCont=None,
        T_TEXT_tipo_insercao_Conj="inserção_menu", T_TEXT_tipo_de_conjuncao_Conj=None, T_TEXT_conj_extensoConj=None,
        T_TEXT_indiceConj=None,
        T_TEXT_tipo_insercao_Rel='inserção_menu', T_TEXT_pron_extenso_Rel=None, T_TEXT_tipo_de_relativo=None,
        T_TEXT_tipo_pronome_relativo=None, T_TEXT_generoTemaTextual=None, T_TEXT_numeroTemaTextual=None,
        T_TEXT_indiceRelativo=None,
        T_TEXT_indiceRelativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,
        ##específico do Processo Mental
        FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,

        ##Processo
        TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None,
        verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
        padrao_pessoa_morfologia_LEX='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        P1_dissoc_ente_nucleo=None, P1_tem_qualificador=None, P1_tipo_qualificador=None,
        P1_indice_preposicao_qualif=None, P1_determinacao_especificidade_beta=None, P1_orientacao_beta=None,
        P1_genero_beta=None, P1_numero_beta=None, P1_morfologia_do_pronome_beta=None,
        P1_determinacao_especificidade_alpha=None, P1_orientacao_alpha=None, P1_genero_alpha=None, P1_numero_alpha=None,
        P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocucao_possuidor=None, P1_numero_obj_possuido=None,
        P1_genero_obj_possuido=None, P1_pessoa_da_interlocucao_proximidade=None, P1_funcao_numerativo=None,
        P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipo_real_card=None, P1_milharExtenso=None,
        P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None,
        P1_tipo_de_ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None,
        P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_ente=None, P1_substantivo_lematizado=None,
        P1_numero=None, P1_tipo_feminino_ao=None, P1_tipo_masc_ao=None, P1_acent_tonica=None, P1_nome_proprio=None,
        P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None,
        P1_reflexivo=None, P1_adjetivo_epiteto=None, P1_adjetivo_classificador=None, P1_genero_adjetivo=None,
        P1_numero_adjetivo=None, P1_contracao=None,
        # P2
        P2_dissoc_ente_nucleo=None, P2_tem_qualificador=None, P2_tipo_qualificador=None,
        P2_indice_preposicao_qualif=None, P2_determinacao_especificidade_beta=None, P2_orientacao_beta=None,
        P2_genero_beta=None, P2_numero_beta=None, P2_morfologia_do_pronome_beta=None,
        P2_determinacao_especificidade_alpha=None, P2_orientacao_alpha=None, P2_genero_alpha=None, P2_numero_alpha=None,
        P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocucao_possuidor=None, P2_numero_obj_possuido=None,
        P2_genero_obj_possuido=None, P2_pessoa_da_interlocucao_proximidade=None, P2_funcao_numerativo=None,
        P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipo_real_card=None, P2_milharExtenso=None,
        P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None,
        P2_tipo_de_ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None,
        P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_ente=None, P2_substantivo_lematizado=None,
        P2_numero=None, P2_tipo_feminino_ao=None, P2_tipo_masc_ao=None, P2_acent_tonica=None, P2_nome_proprio=None,
        P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None,
        P2_reflexivo=None, P2_adjetivo_epiteto=None, P2_adjetivo_classificador=None, P2_genero_adjetivo=None,
        P2_numero_adjetivo=None, P2_contracao=None,
        ##PARTICIPANTES REALIZADOS POR FP
        PART_FP_indice_preposicao_frase=None, PART_FP_dissoc_ente_nucleo=None, PART_FP_tem_qualificador=None,
        PART_FP_tipo_qualificador=None, PART_FP_indice_preposicao_qualif=None,
        PART_FP_determinacao_especificidade_beta=None, PART_FP_orientacao_beta=None, PART_FP_genero_beta=None,
        PART_FP_numero_beta=None, PART_FP_morfologia_do_pronome_beta=None,
        PART_FP_determinacao_especificidade_alpha=None, PART_FP_orientacao_alpha=None, PART_FP_genero_alpha=None,
        PART_FP_numero_alpha=None, PART_FP_morfologia_do_pronome_alpha=None,
        PART_FP_pessoa_da_interlocucao_possuidor=None, PART_FP_numero_obj_possuido=None,
        PART_FP_genero_obj_possuido=None, PART_FP_pessoa_da_interlocucao_proximidade=None,
        PART_FP_funcao_numerativo=None, PART_FP_cardinal=None, PART_FP_genero=None, PART_FP_tipo_precisa=None,
        PART_FP_tipo_real_card=None, PART_FP_milharExtenso=None, PART_FP_centenaExtenso=None,
        PART_FP_dezenaExtenso=None, PART_FP_unidadeExtenso=None, PART_FP_numIndefinido=None, PART_FP_tipo_de_ente=None,
        PART_FP_tipo_de_nao_consciente=None, PART_FP_tipo_de_nao_consciente_material=None,
        PART_FP_tipo_de_nao_consciente_semiotico=None, PART_FP_classe_palavra_ente=None,
        PART_FP_substantivo_lematizado=None, PART_FP_numero=None, PART_FP_tipo_feminino_ao=None,
        PART_FP_tipo_masc_ao=None, PART_FP_acent_tonica=None, PART_FP_nome_proprio=None,
        PART_FP_pessoa_da_interlocucao=None, PART_FP_transitividade_verbo=None, PART_FP_tonicidade=None,
        PART_FP_morfologia_do_pronome=None, PART_FP_reflexivo=None, PART_FP_adjetivo_epiteto=None,
        PART_FP_adjetivo_classificador=None, PART_FP_genero_adjetivo=None, PART_FP_numero_adjetivo=None,
        PART_FP_contracao=None,
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
        Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel, indiceAtrib)
        Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL, T_INTER_tipoRealizacao, T_INTER_tipo_de_adverbio1,
                                              T_INTER_ind1, T_INTER_tipo_de_adverbio2, T_INTER_ind2,
                                              T_INTER_tipo_de_adverbio3, T_INTER_ind3, T_INTER_tipo_de_adverbio4,
                                              T_INTER_ind4, T_INTER_tipo_de_adverbio5, T_INTER_ind5,
                                              T_INTER_FP_indice_preposicao_frase, T_INTER_FP_dissoc_ente_nucleo,
                                              T_INTER_FP_tem_qualificador, T_INTER_FP_tipo_qualificador,
                                              T_INTER_FP_indice_preposicao_qualif,
                                              T_INTER_FP_determinacao_especificidade_beta, T_INTER_FP_orientacao_beta,
                                              T_INTER_FP_genero_beta, T_INTER_FP_numero_beta,
                                              T_INTER_FP_morfologia_do_pronome_beta,
                                              T_INTER_FP_determinacao_especificidade_alpha, T_INTER_FP_orientacao_alpha,
                                              T_INTER_FP_genero_alpha, T_INTER_FP_numero_alpha,
                                              T_INTER_FP_morfologia_do_pronome_alpha,
                                              T_INTER_FP_pessoa_da_interlocucao_possuidor,
                                              T_INTER_FP_numero_obj_possuido, T_INTER_FP_genero_obj_possuido,
                                              T_INTER_FP_pessoa_da_interlocucao_proximidade,
                                              T_INTER_FP_funcao_numerativo, T_INTER_FP_cardinal, T_INTER_FP_genero,
                                              T_INTER_FP_tipo_precisa, T_INTER_FP_tipo_real_card,
                                              T_INTER_FP_milharExtenso, T_INTER_FP_centenaExtenso,
                                              T_INTER_FP_dezenaExtenso, T_INTER_FP_unidadeExtenso,
                                              T_INTER_FP_numIndefinido, T_INTER_FP_tipo_de_ente,
                                              T_INTER_FP_tipo_de_nao_consciente,
                                              T_INTER_FP_tipo_de_nao_consciente_material,
                                              T_INTER_FP_tipo_de_nao_consciente_semiotico,
                                              T_INTER_FP_classe_palavra_ente, T_INTER_FP_substantivo_lematizado,
                                              T_INTER_FP_numero, T_INTER_FP_tipo_feminino_ao, T_INTER_FP_tipo_masc_ao,
                                              T_INTER_FP_acent_tonica, T_INTER_FP_nome_proprio,
                                              T_INTER_FP_pessoa_da_interlocucao, T_INTER_FP_transitividade_verbo,
                                              T_INTER_FP_tonicidade, T_INTER_FP_morfologia_do_pronome,
                                              T_INTER_FP_reflexivo, T_INTER_FP_adjetivo_epiteto,
                                              T_INTER_FP_adjetivo_classificador, T_INTER_FP_genero_adjetivo,
                                              T_INTER_FP_numero_adjetivo, T_INTER_FP_contracao, T_INTER_indiceElemQu,
                                              T_INTER_indicePartModal, T_INTER_nome_proprio)
        Tema_textual = TEMA_TEXTUAL(T_TEXT_temTemaTextual, T_TEXT_tipo_insercao_Cont, T_TEXT_conj_extenso_Cont,
                                    T_TEXT_indiceCont, T_TEXT_tipo_insercao_Conj, T_TEXT_tipo_de_conjuncao_Conj,
                                    T_TEXT_conj_extensoConj, T_TEXT_indiceConj, T_TEXT_tipo_insercao_Rel,
                                    T_TEXT_pron_extenso_Rel, T_TEXT_tipo_de_relativo, T_TEXT_tipo_pronome_relativo,
                                    T_TEXT_generoTemaTextual, T_TEXT_numeroTemaTextual, T_TEXT_indiceRelativo,
                                    T_TEXT_indiceRelativoAdv)
        Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        Polaridade = POLARIDADE(tipo_polaridade)
        Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
                                verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                                padrao_pessoa_morfologia_LEX)
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

        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

            if Transitividade == 'PR_Mental_AG_médio_sem_alcance':

                Experienciador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                              P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                              P1_orientacao_beta,
                                              P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                              P1_determinacao_especificidade_alpha, P1_orientacao_alpha,
                                              P1_genero_alpha,
                                              P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                              P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido,
                                              P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                              P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa,
                                              P1_tipo_real_card,
                                              P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso,
                                              P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                              P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                              P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero,
                                              P1_tipo_feminino_ao, P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                              P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                              P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                              P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                              P1_contracao)
                if FENOMENALIZACAO == 'não-fenomenalização_comportamento-passivo':

                    if (TIPO_DE_MENTAL == 'superior_cognitivo' or
                            TIPO_DE_MENTAL == 'superior_desiderativo' or
                            # Ex.: Tenho pensado; Eu pensei a noite toda;
                            TIPO_DE_MENTAL == 'inferior_emotivo' or
                            TIPO_DE_MENTAL == 'inferior_perceptivo'):
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + '.'
                    # 'Eu ouvi perfeitamente'

            elif Transitividade == 'PR_Mental_AG_médio_com_alcance':
                Experienciador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                              P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                              P1_orientacao_beta,
                                              P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                              P1_determinacao_especificidade_alpha, P1_orientacao_alpha,
                                              P1_genero_alpha,
                                              P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                              P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido,
                                              P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                              P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa,
                                              P1_tipo_real_card,
                                              P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso,
                                              P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                              P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                              P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero,
                                              P1_tipo_feminino_ao, P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                              P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                              P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                              P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                              P1_contracao)
                if FENOMENALIZACAO == 'não-fenomenalização_assunto':
                    if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo' or
                            TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
                        Assunto = frase_preposicional(PART_FP_indice_preposicao_frase, PART_FP_dissoc_ente_nucleo,
                                                      PART_FP_tem_qualificador, PART_FP_tipo_qualificador,
                                                      PART_FP_indice_preposicao_qualif,
                                                      PART_FP_determinacao_especificidade_beta, PART_FP_orientacao_beta,
                                                      PART_FP_genero_beta, PART_FP_numero_beta,
                                                      PART_FP_morfologia_do_pronome_beta,
                                                      PART_FP_determinacao_especificidade_alpha,
                                                      PART_FP_orientacao_alpha,
                                                      PART_FP_genero_alpha, PART_FP_numero_alpha,
                                                      PART_FP_morfologia_do_pronome_alpha,
                                                      PART_FP_pessoa_da_interlocucao_possuidor,
                                                      PART_FP_numero_obj_possuido,
                                                      PART_FP_genero_obj_possuido,
                                                      PART_FP_pessoa_da_interlocucao_proximidade,
                                                      PART_FP_funcao_numerativo,
                                                      PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa,
                                                      PART_FP_tipo_real_card, PART_FP_milharExtenso,
                                                      PART_FP_centenaExtenso,
                                                      PART_FP_dezenaExtenso, PART_FP_unidadeExtenso,
                                                      PART_FP_numIndefinido,
                                                      PART_FP_tipo_de_ente, PART_FP_tipo_de_nao_consciente,
                                                      PART_FP_tipo_de_nao_consciente_material,
                                                      PART_FP_tipo_de_nao_consciente_semiotico,
                                                      PART_FP_classe_palavra_ente,
                                                      PART_FP_substantivo_lematizado, PART_FP_numero,
                                                      PART_FP_tipo_feminino_ao, PART_FP_tipo_masc_ao,
                                                      PART_FP_acent_tonica,
                                                      PART_FP_nome_proprio, PART_FP_pessoa_da_interlocucao,
                                                      PART_FP_transitividade_verbo, PART_FP_tonicidade,
                                                      PART_FP_morfologia_do_pronome, PART_FP_reflexivo,
                                                      PART_FP_adjetivo_epiteto, PART_FP_adjetivo_classificador,
                                                      PART_FP_genero_adjetivo, PART_FP_numero_adjetivo,
                                                      PART_FP_contracao)
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '.'
                # Ex.: Eu sei de futebol.

                # 'Médio com alcance = mental emanente.'
                # TIPO_FENOMENALIZACAO= choice.Menu(['hiperfenômeno', 'fenômeno_simples']
                # print('Qual tipo_pessoa de Processo superior?')
                # TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                elif FENOMENALIZACAO == 'fenomenalização_fenômeno-simples':
                    if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo'):

                        Fenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                P2_cardinal,
                                                P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                P2_numIndefinido,
                                                P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                P2_contracao)

                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenomeno + '.'
                    # Ex.: Eu imaginei o jogo
                    elif (TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
                        # APESAR DE PARECER REDUNDANTE, EM UMA PRÓXIMA FASE, CADA UMA DESTAS ITERAÇÕES
                        # VAI TER OS LEXEMAS REPRESENTATIVOS DE CADA TIPO DE PROCESSO MENTAL
                        # print('Qual tipo_pessoa de Processo inferior?')
                        # TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')

                        Fenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                P2_cardinal,
                                                P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                P2_numIndefinido,
                                                P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                P2_contracao)

                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenomeno + '.'

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
                        Metafenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                    P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                    P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                    P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                    P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                    P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                    P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                    P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                    P2_cardinal,
                                                    P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                    P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                    P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                    P2_tipo_de_nao_consciente_material,
                                                    P2_tipo_de_nao_consciente_semiotico,
                                                    P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                    P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica,
                                                    P2_nome_proprio,
                                                    P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                    P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                    P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                    P2_contracao)

                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Metafenomeno + '.'

                elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-orientado_gerúndio'):
                    if TIPO_DE_MENTAL == 'inferior_perceptivo':
                        Macrofenomeno = oracaoProjetada()
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '.'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if TIPO_DE_MENTAL == 'inferior_perceptivo':
                        Macrofenomeno = 'que' + ' ' + oracaoProjetada()
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '.'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if TIPO_DE_MENTAL == 'inferior_perceptivo':
                        Macrofenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                     P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                     P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                     P2_morfologia_do_pronome_beta,
                                                     P2_determinacao_especificidade_alpha,
                                                     P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                     P2_morfologia_do_pronome_alpha,
                                                     P2_pessoa_da_interlocucao_possuidor,
                                                     P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                     P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                     P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                                     P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso,
                                                     P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                                     P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                                     P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                     P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                     P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                     P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                     P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                     P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                     P2_contracao)
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '.'

            elif Transitividade == 'PR_Mental_AG_efetivo_operativo':
                # impingente
                ExperienciadorGN = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                P2_cardinal,
                                                P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                P2_numIndefinido,
                                                P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                P2_contracao)
                ExperienciadorFP = frase_preposicional(PART_FP_indicePreposicao, PART_FP_dissoc_ente_nucleo,
                                                       PART_FP_tem_qualificador, PART_FP_tipo_qualificador,
                                                       PART_FP_determinacao_especificidade_beta,
                                                       PART_FP_orientacao_beta,
                                                       PART_FP_genero_beta, PART_FP_numero_beta,
                                                       PART_FP_morfologia_do_pronome_beta,
                                                       PART_FP_determinacao_especificidade_alpha,
                                                       PART_FP_orientacao_alpha,
                                                       PART_FP_genero_alpha, PART_FP_numero_alpha,
                                                       PART_FP_morfologia_do_pronome_alpha,
                                                       PART_FP_pessoa_da_interlocucao_possuidor,
                                                       PART_FP_numero_obj_possuido, PART_FP_genero_obj_possuido,
                                                       PART_FP_pessoa_da_interlocucao_proximidade,
                                                       PART_FP_funcao_numerativo,
                                                       PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa,
                                                       PART_FP_tipo_real_card, PART_FP_milharExtenso,
                                                       PART_FP_centenaExtenso,
                                                       PART_FP_dezenaExtenso, PART_FP_unidadeExtenso,
                                                       PART_FP_numIndefinido,
                                                       PART_FP_tipo_de_ente, PART_FP_tipo_de_nao_consciente,
                                                       PART_FP_tipo_de_nao_consciente_material,
                                                       PART_FP_tipo_de_nao_consciente_semiotico,
                                                       PART_FP_classe_palavra_ente, PART_FP_substantivo_lematizado,
                                                       PART_FP_numero, PART_FP_tipo_feminino_ao, PART_FP_tipo_masc_ao,
                                                       PART_FP_acent_tonica, PART_FP_nome_proprio,
                                                       PART_FP_pessoa_da_interlocucao, PART_FP_transitividade_verbo,
                                                       PART_FP_tonicidade, PART_FP_morfologia_do_pronome,
                                                       PART_FP_reflexivo,
                                                       PART_FP_adjetivo_epiteto, PART_FP_adjetivo_classificador,
                                                       PART_FP_genero_adjetivo, PART_FP_numero_adjetivo,
                                                       PART_FP_contracao)
                if FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
                    if TIPO_DE_MENTAL == 'inferior_emotivo':
                        MetafenomenoAgente = oracaoProjetada()
                        oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_que':
                    if TIPO_DE_MENTAL == 'inferior_emotivo':
                        MetafenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
                    if TIPO_DE_MENTAL == 'inferior_emotivo':
                        # print('Selecione o GN com oração qualificadora:')
                        MetafenomenoAgente = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador,
                                                          P2_tipo_qualificador,
                                                          P2_indice_preposicao_qualif,
                                                          P2_determinacao_especificidade_beta,
                                                          P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                          P2_morfologia_do_pronome_beta,
                                                          P2_determinacao_especificidade_alpha, P2_orientacao_alpha,
                                                          P2_genero_alpha, P2_numero_alpha,
                                                          P2_morfologia_do_pronome_alpha,
                                                          P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                                          P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                                          P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa,
                                                          P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                                          P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                                          P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                          P2_tipo_de_nao_consciente_material,
                                                          P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                          P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                          P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                          P2_pessoa_da_interlocucao, P2_transitividade_verbo,
                                                          P2_tonicidade,
                                                          P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                          P2_adjetivo_classificador, P2_genero_adjetivo,
                                                          P2_numero_adjetivo,
                                                          P2_contracao)
                        oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      FENOMENALIZACAO == 'reativo_macrofenômeno_não-orientado_gerúndio'):
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        MacrofenomenoAgente = oracaoProjetada()
                        oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        MacrofenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        MacrofenomenoAgente = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador,
                                                           P2_tipo_qualificador,
                                                           P2_indice_preposicao_qualif,
                                                           P2_determinacao_especificidade_beta,
                                                           P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                           P2_morfologia_do_pronome_beta,
                                                           P2_determinacao_especificidade_alpha, P2_orientacao_alpha,
                                                           P2_genero_alpha, P2_numero_alpha,
                                                           P2_morfologia_do_pronome_alpha,
                                                           P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                                           P2_genero_obj_possuido,
                                                           P2_pessoa_da_interlocucao_proximidade,
                                                           P2_funcao_numerativo, P2_cardinal, P2_genero,
                                                           P2_tipo_precisa,
                                                           P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                                           P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                                           P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                           P2_tipo_de_nao_consciente_material,
                                                           P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                           P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                           P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                           P2_pessoa_da_interlocucao, P2_transitividade_verbo,
                                                           P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                                           P2_adjetivo_epiteto, P2_adjetivo_classificador,
                                                           P2_genero_adjetivo, P2_numero_adjetivo, P2_contracao)
                        oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

                elif FENOMENALIZACAO == "fenomenalização_fenômeno_simples":
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')
                        FenomenoAgente = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                                      P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                                      P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                                      P1_morfologia_do_pronome_beta,
                                                      P1_determinacao_especificidade_alpha,
                                                      P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                                      P1_morfologia_do_pronome_alpha,
                                                      P1_pessoa_da_interlocucao_possuidor,
                                                      P1_numero_obj_possuido, P1_genero_obj_possuido,
                                                      P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo,
                                                      P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipo_real_card,
                                                      P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso,
                                                      P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                                      P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                                      P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                                      P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                                      P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                                      P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                                      P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                                      P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                                      P1_contracao)
                        oração = FenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + ' ' + '.'

        # comeca interrogativa polar
        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

            if Transitividade == 'PR_Mental_AG_médio_sem_alcance':

                Experienciador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                              P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                              P1_orientacao_beta,
                                              P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                              P1_determinacao_especificidade_alpha, P1_orientacao_alpha,
                                              P1_genero_alpha,
                                              P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                              P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido,
                                              P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                              P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa,
                                              P1_tipo_real_card,
                                              P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso,
                                              P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                              P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                              P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero,
                                              P1_tipo_feminino_ao, P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                              P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                              P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                              P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                              P1_contracao)
                if FENOMENALIZACAO == 'não-fenomenalização_comportamento-passivo':

                    if (TIPO_DE_MENTAL == 'superior_cognitivo' or
                            TIPO_DE_MENTAL == 'superior_desiderativo' or
                            # Ex.: Tenho pensado; Eu pensei a noite toda;
                            TIPO_DE_MENTAL == 'inferior_emotivo' or
                            TIPO_DE_MENTAL == 'inferior_perceptivo'):
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + '?'
            # 'Eu ouvi perfeitamente'

            elif Transitividade == 'PR_Mental_AG_médio_com_alcance':
                Experienciador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                              P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                              P1_orientacao_beta,
                                              P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                              P1_determinacao_especificidade_alpha, P1_orientacao_alpha,
                                              P1_genero_alpha,
                                              P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                              P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido,
                                              P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                              P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa,
                                              P1_tipo_real_card,
                                              P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso,
                                              P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                              P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                              P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero,
                                              P1_tipo_feminino_ao, P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                              P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                              P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                              P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                              P1_contracao)
                if FENOMENALIZACAO == 'não-fenomenalização_assunto':
                    if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo' or
                            TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
                        Assunto = frase_preposicional(PART_FP_indice_preposicao_frase, PART_FP_dissoc_ente_nucleo,
                                                      PART_FP_tem_qualificador, PART_FP_tipo_qualificador,
                                                      PART_FP_indice_preposicao_qualif,
                                                      PART_FP_determinacao_especificidade_beta, PART_FP_orientacao_beta,
                                                      PART_FP_genero_beta, PART_FP_numero_beta,
                                                      PART_FP_morfologia_do_pronome_beta,
                                                      PART_FP_determinacao_especificidade_alpha,
                                                      PART_FP_orientacao_alpha,
                                                      PART_FP_genero_alpha, PART_FP_numero_alpha,
                                                      PART_FP_morfologia_do_pronome_alpha,
                                                      PART_FP_pessoa_da_interlocucao_possuidor,
                                                      PART_FP_numero_obj_possuido,
                                                      PART_FP_genero_obj_possuido,
                                                      PART_FP_pessoa_da_interlocucao_proximidade,
                                                      PART_FP_funcao_numerativo,
                                                      PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa,
                                                      PART_FP_tipo_real_card, PART_FP_milharExtenso,
                                                      PART_FP_centenaExtenso,
                                                      PART_FP_dezenaExtenso, PART_FP_unidadeExtenso,
                                                      PART_FP_numIndefinido,
                                                      PART_FP_tipo_de_ente, PART_FP_tipo_de_nao_consciente,
                                                      PART_FP_tipo_de_nao_consciente_material,
                                                      PART_FP_tipo_de_nao_consciente_semiotico,
                                                      PART_FP_classe_palavra_ente,
                                                      PART_FP_substantivo_lematizado, PART_FP_numero,
                                                      PART_FP_tipo_feminino_ao, PART_FP_tipo_masc_ao,
                                                      PART_FP_acent_tonica,
                                                      PART_FP_nome_proprio, PART_FP_pessoa_da_interlocucao,
                                                      PART_FP_transitividade_verbo, PART_FP_tonicidade,
                                                      PART_FP_morfologia_do_pronome, PART_FP_reflexivo,
                                                      PART_FP_adjetivo_epiteto, PART_FP_adjetivo_classificador,
                                                      PART_FP_genero_adjetivo, PART_FP_numero_adjetivo,
                                                      PART_FP_contracao)
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '?'
                # Ex.: Eu sei de futebol.

                # 'Médio com alcance = mental emanente.'
                # TIPO_FENOMENALIZACAO= choice.Menu(['hiperfenômeno', 'fenômeno_simples']
                # print('Qual tipo_pessoa de Processo superior?')
                # TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                elif FENOMENALIZACAO == 'fenomenalização_fenômeno-simples':
                    if (TIPO_DE_MENTAL == 'superior_cognitivo' or TIPO_DE_MENTAL == 'superior_desiderativo'):

                        Fenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                P2_cardinal,
                                                P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                P2_numIndefinido,
                                                P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                P2_contracao)

                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenomeno + '?'
                    # Ex.: Eu imaginei o jogo
                    elif (TIPO_DE_MENTAL == 'inferior_emotivo' or TIPO_DE_MENTAL == 'inferior_perceptivo'):
                        # APESAR DE PARECER REDUNDANTE, EM UMA PRÓXIMA FASE, CADA UMA DESTAS ITERAÇÕES
                        # VAI TER OS LEXEMAS REPRESENTATIVOS DE CADA TIPO DE PROCESSO MENTAL
                        # print('Qual tipo_pessoa de Processo inferior?')
                        # TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')

                        Fenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                P2_cardinal,
                                                P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                P2_numIndefinido,
                                                P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                P2_contracao)

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
                        Metafenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                    P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                    P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                    P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                    P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                    P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                    P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                    P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                    P2_cardinal,
                                                    P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                    P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                    P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                    P2_tipo_de_nao_consciente_material,
                                                    P2_tipo_de_nao_consciente_semiotico,
                                                    P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                    P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica,
                                                    P2_nome_proprio,
                                                    P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                    P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                    P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                    P2_contracao)

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
                        Macrofenomeno = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                     P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                     P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                     P2_morfologia_do_pronome_beta,
                                                     P2_determinacao_especificidade_alpha,
                                                     P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                     P2_morfologia_do_pronome_alpha,
                                                     P2_pessoa_da_interlocucao_possuidor,
                                                     P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                     P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                     P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                                     P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso,
                                                     P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                                     P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                                     P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                     P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                     P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                     P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                     P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                     P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                     P2_contracao)
                        oração = Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Macrofenomeno + '?'

            elif Transitividade == 'PR_Mental_AG_efetivo_operativo':
                # impingente
                ExperienciadorGN = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                P2_cardinal,
                                                P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                                P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                                P2_numIndefinido,
                                                P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                                P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                P2_contracao)
                ExperienciadorFP = frase_preposicional(PART_FP_indice_preposicao_frase, PART_FP_dissoc_ente_nucleo,
                                                       PART_FP_tem_qualificador, PART_FP_tipo_qualificador,
                                                       PART_FP_indice_preposicao_qualif,
                                                       PART_FP_determinacao_especificidade_beta,
                                                       PART_FP_orientacao_beta,
                                                       PART_FP_genero_beta, PART_FP_numero_beta,
                                                       PART_FP_morfologia_do_pronome_beta,
                                                       PART_FP_determinacao_especificidade_alpha,
                                                       PART_FP_orientacao_alpha,
                                                       PART_FP_genero_alpha, PART_FP_numero_alpha,
                                                       PART_FP_morfologia_do_pronome_alpha,
                                                       PART_FP_pessoa_da_interlocucao_possuidor,
                                                       PART_FP_numero_obj_possuido, PART_FP_genero_obj_possuido,
                                                       PART_FP_pessoa_da_interlocucao_proximidade,
                                                       PART_FP_funcao_numerativo,
                                                       PART_FP_cardinal, PART_FP_genero, PART_FP_tipo_precisa,
                                                       PART_FP_tipo_real_card, PART_FP_milharExtenso,
                                                       PART_FP_centenaExtenso,
                                                       PART_FP_dezenaExtenso, PART_FP_unidadeExtenso,
                                                       PART_FP_numIndefinido,
                                                       PART_FP_tipo_de_ente, PART_FP_tipo_de_nao_consciente,
                                                       PART_FP_tipo_de_nao_consciente_material,
                                                       PART_FP_tipo_de_nao_consciente_semiotico,
                                                       PART_FP_classe_palavra_ente, PART_FP_substantivo_lematizado,
                                                       PART_FP_numero, PART_FP_tipo_feminino_ao, PART_FP_tipo_masc_ao,
                                                       PART_FP_acent_tonica, PART_FP_nome_proprio,
                                                       PART_FP_pessoa_da_interlocucao, PART_FP_transitividade_verbo,
                                                       PART_FP_tonicidade, PART_FP_morfologia_do_pronome,
                                                       PART_FP_reflexivo,
                                                       PART_FP_adjetivo_epiteto, PART_FP_adjetivo_classificador,
                                                       PART_FP_genero_adjetivo, PART_FP_numero_adjetivo,
                                                       PART_FP_contracao)
                if FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_mudada_ordem':
                    if TIPO_DE_MENTAL == 'inferior_emotivo':
                        MetafenomenoAgente = oracaoProjetada()
                        oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_oração_que':
                    if TIPO_DE_MENTAL == 'inferior_emotivo':
                        MetafenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_metafenômeno_GN+oração_qualificadora':
                    if TIPO_DE_MENTAL == 'inferior_emotivo':
                        # print('Selecione o GN com oração qualificadora:')
                        MetafenomenoAgente = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador,
                                                          P2_tipo_qualificador,
                                                          P2_indice_preposicao_qualif,
                                                          P2_determinacao_especificidade_beta,
                                                          P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                          P2_morfologia_do_pronome_beta,
                                                          P2_determinacao_especificidade_alpha, P2_orientacao_alpha,
                                                          P2_genero_alpha, P2_numero_alpha,
                                                          P2_morfologia_do_pronome_alpha,
                                                          P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                                          P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                                          P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa,
                                                          P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                                          P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                                          P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                          P2_tipo_de_nao_consciente_material,
                                                          P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                          P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                          P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                          P2_pessoa_da_interlocucao, P2_transitividade_verbo,
                                                          P2_tonicidade,
                                                          P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                          P2_adjetivo_classificador, P2_genero_adjetivo,
                                                          P2_numero_adjetivo,
                                                          P2_contracao)
                        oração = MetafenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif (FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_não-finito_concretizado' or
                      FENOMENALIZACAO == 'reativo_macrofenômeno_não-orientado_gerúndio'):
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        MacrofenomenoAgente = oracaoProjetada()
                        oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_oração_que':
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        MacrofenomenoAgente = 'que' + ' ' + oracaoProjetada()
                        oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif FENOMENALIZACAO == 'hiperfenômeno_reativo_macrofenômeno_GN+oração_qualificadora':
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        MacrofenomenoAgente = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador,
                                                           P2_tipo_qualificador,
                                                           P2_indice_preposicao_qualif,
                                                           P2_determinacao_especificidade_beta,
                                                           P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                           P2_morfologia_do_pronome_beta,
                                                           P2_determinacao_especificidade_alpha, P2_orientacao_alpha,
                                                           P2_genero_alpha, P2_numero_alpha,
                                                           P2_morfologia_do_pronome_alpha,
                                                           P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                                           P2_genero_obj_possuido,
                                                           P2_pessoa_da_interlocucao_proximidade,
                                                           P2_funcao_numerativo, P2_cardinal, P2_genero,
                                                           P2_tipo_precisa,
                                                           P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                                           P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                                           P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                                           P2_tipo_de_nao_consciente_material,
                                                           P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                           P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                           P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                           P2_pessoa_da_interlocucao, P2_transitividade_verbo,
                                                           P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                                           P2_adjetivo_epiteto, P2_adjetivo_classificador,
                                                           P2_genero_adjetivo, P2_numero_adjetivo, P2_contracao)
                        oração = MacrofenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

                elif FENOMENALIZACAO == "fenomenalização_fenômeno_simples":
                    if TIPO_DE_MENTAL == "superior_cognitivo":
                        # print('Selecione verbo lematizado cognitivo ou desiderativo:')
                        FenomenoAgente = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                                      P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                                      P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                                      P1_morfologia_do_pronome_beta,
                                                      P1_determinacao_especificidade_alpha,
                                                      P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                                      P1_morfologia_do_pronome_alpha,
                                                      P1_pessoa_da_interlocucao_possuidor,
                                                      P1_numero_obj_possuido, P1_genero_obj_possuido,
                                                      P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo,
                                                      P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipo_real_card,
                                                      P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso,
                                                      P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                                      P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                                      P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                                      P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                                      P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                                      P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                                      P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                                      P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                                      P1_contracao)
                        oração = FenomenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + ExperienciadorGN + ' ' + ExperienciadorFP + '?'

        return (re.sub(' +', ' ', oração).strip().capitalize())
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
        TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None, indiceAtrib=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, T_INTER_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        T_INTER_tipo_de_adverbio1=None, T_INTER_ind1=None,
        T_INTER_tipo_de_adverbio2=None, T_INTER_ind2=None,
        T_INTER_tipo_de_adverbio3=None, T_INTER_ind3=None,
        T_INTER_tipo_de_adverbio4=None, T_INTER_ind4=None,
        T_INTER_tipo_de_adverbio5=None, T_INTER_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        T_INTER_FP_indice_preposicao_frase=None, T_INTER_FP_dissoc_ente_nucleo=None, T_INTER_FP_tem_qualificador=None,
        T_INTER_FP_tipo_qualificador=None, T_INTER_FP_indice_preposicao_qualif=None,
        T_INTER_FP_determinacao_especificidade_beta=None, T_INTER_FP_orientacao_beta=None, T_INTER_FP_genero_beta=None,
        T_INTER_FP_numero_beta=None, T_INTER_FP_morfologia_do_pronome_beta=None,
        T_INTER_FP_determinacao_especificidade_alpha=None, T_INTER_FP_orientacao_alpha=None,
        T_INTER_FP_genero_alpha=None, T_INTER_FP_numero_alpha=None, T_INTER_FP_morfologia_do_pronome_alpha=None,
        T_INTER_FP_pessoa_da_interlocucao_possuidor=None, T_INTER_FP_numero_obj_possuido=None,
        T_INTER_FP_genero_obj_possuido=None, T_INTER_FP_pessoa_da_interlocucao_proximidade=None,
        T_INTER_FP_funcao_numerativo=None, T_INTER_FP_cardinal=None, T_INTER_FP_genero=None,
        T_INTER_FP_tipo_precisa=None, T_INTER_FP_tipo_real_card=None, T_INTER_FP_milharExtenso=None,
        T_INTER_FP_centenaExtenso=None, T_INTER_FP_dezenaExtenso=None, T_INTER_FP_unidadeExtenso=None,
        T_INTER_FP_numIndefinido=None, T_INTER_FP_tipo_de_ente=None, T_INTER_FP_tipo_de_nao_consciente=None,
        T_INTER_FP_tipo_de_nao_consciente_material=None, T_INTER_FP_tipo_de_nao_consciente_semiotico=None,
        T_INTER_FP_classe_palavra_ente=None, T_INTER_FP_substantivo_lematizado=None, T_INTER_FP_numero=None,
        T_INTER_FP_tipo_feminino_ao=None, T_INTER_FP_tipo_masc_ao=None, T_INTER_FP_acent_tonica=None,
        T_INTER_FP_nome_proprio=None, T_INTER_FP_pessoa_da_interlocucao=None, T_INTER_FP_transitividade_verbo=None,
        T_INTER_FP_tonicidade=None, T_INTER_FP_morfologia_do_pronome=None, T_INTER_FP_reflexivo=None,
        T_INTER_FP_adjetivo_epiteto=None, T_INTER_FP_adjetivo_classificador=None, T_INTER_FP_genero_adjetivo=None,
        T_INTER_FP_numero_adjetivo=None, T_INTER_FP_contracao=None,
        #
        # 		#
        T_INTER_indiceElemQu=None, T_INTER_indicePartModal=None, T_INTER_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        T_TEXT_temTemaTextual='-', T_TEXT_tipo_insercao_Cont="inserção_menu", T_TEXT_conj_extenso_Cont=None,
        T_TEXT_indiceCont=None,
        T_TEXT_tipo_insercao_Conj="inserção_menu", T_TEXT_tipo_de_conjuncao_Conj=None, T_TEXT_conj_extensoConj=None,
        T_TEXT_indiceConj=None,
        T_TEXT_tipo_insercao_Rel='inserção_menu', T_TEXT_pron_extenso_Rel=None, T_TEXT_tipo_de_relativo=None,
        T_TEXT_tipo_pronome_relativo=None, T_TEXT_generoTemaTextual=None, T_TEXT_numeroTemaTextual=None,
        T_TEXT_indiceRelativo=None,
        T_TEXT_indiceRelativoAdv=None,
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
        TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None,
        verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
        padrao_pessoa_morfologia_LEX='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        P1_dissoc_ente_nucleo=None, P1_tem_qualificador=None, P1_tipo_qualificador=None,
        P1_indice_preposicao_qualif=None, P1_determinacao_especificidade_beta=None, P1_orientacao_beta=None,
        P1_genero_beta=None, P1_numero_beta=None, P1_morfologia_do_pronome_beta=None,
        P1_determinacao_especificidade_alpha=None, P1_orientacao_alpha=None, P1_genero_alpha=None, P1_numero_alpha=None,
        P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocucao_possuidor=None, P1_numero_obj_possuido=None,
        P1_genero_obj_possuido=None, P1_pessoa_da_interlocucao_proximidade=None, P1_funcao_numerativo=None,
        P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipo_real_card=None, P1_milharExtenso=None,
        P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None,
        P1_tipo_de_ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None,
        P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_ente=None, P1_substantivo_lematizado=None,
        P1_numero=None, P1_tipo_feminino_ao=None, P1_tipo_masc_ao=None, P1_acent_tonica=None, P1_nome_proprio=None,
        P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None,
        P1_reflexivo=None, P1_adjetivo_epiteto=None, P1_adjetivo_classificador=None, P1_genero_adjetivo=None,
        P1_numero_adjetivo=None, P1_contracao=None,
        ##PARTICIPANTE P1 REALIZADOS POR FP
        P1_FP_indice_preposicao_frase=None, P1_FP_dissoc_ente_nucleo=None, P1_FP_tem_qualificador=None,
        P1_FP_tipo_qualificador=None, P1_FP_indice_preposicao_qualif=None, P1_FP_determinacao_especificidade_beta=None,
        P1_FP_orientacao_beta=None, P1_FP_genero_beta=None, P1_FP_numero_beta=None,
        P1_FP_morfologia_do_pronome_beta=None, P1_FP_determinacao_especificidade_alpha=None,
        P1_FP_orientacao_alpha=None, P1_FP_genero_alpha=None, P1_FP_numero_alpha=None,
        P1_FP_morfologia_do_pronome_alpha=None, P1_FP_pessoa_da_interlocucao_possuidor=None,
        P1_FP_numero_obj_possuido=None, P1_FP_genero_obj_possuido=None, P1_FP_pessoa_da_interlocucao_proximidade=None,
        P1_FP_funcao_numerativo=None, P1_FP_cardinal=None, P1_FP_genero=None, P1_FP_tipo_precisa=None,
        P1_FP_tipo_real_card=None, P1_FP_milharExtenso=None, P1_FP_centenaExtenso=None, P1_FP_dezenaExtenso=None,
        P1_FP_unidadeExtenso=None, P1_FP_numIndefinido=None, P1_FP_tipo_de_ente=None, P1_FP_tipo_de_nao_consciente=None,
        P1_FP_tipo_de_nao_consciente_material=None, P1_FP_tipo_de_nao_consciente_semiotico=None,
        P1_FP_classe_palavra_ente=None, P1_FP_substantivo_lematizado=None, P1_FP_numero=None,
        P1_FP_tipo_feminino_ao=None, P1_FP_tipo_masc_ao=None, P1_FP_acent_tonica=None, P1_FP_nome_proprio=None,
        P1_FP_pessoa_da_interlocucao=None, P1_FP_transitividade_verbo=None, P1_FP_tonicidade=None,
        P1_FP_morfologia_do_pronome=None, P1_FP_reflexivo=None, P1_FP_adjetivo_epiteto=None,
        P1_FP_adjetivo_classificador=None, P1_FP_genero_adjetivo=None, P1_FP_numero_adjetivo=None, P1_FP_contracao=None,

        # P2
        P2_dissoc_ente_nucleo=None, P2_tem_qualificador=None, P2_tipo_qualificador=None,
        P2_indice_preposicao_qualif=None, P2_determinacao_especificidade_beta=None, P2_orientacao_beta=None,
        P2_genero_beta=None, P2_numero_beta=None, P2_morfologia_do_pronome_beta=None,
        P2_determinacao_especificidade_alpha=None, P2_orientacao_alpha=None, P2_genero_alpha=None, P2_numero_alpha=None,
        P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocucao_possuidor=None, P2_numero_obj_possuido=None,
        P2_genero_obj_possuido=None, P2_pessoa_da_interlocucao_proximidade=None, P2_funcao_numerativo=None,
        P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipo_real_card=None, P2_milharExtenso=None,
        P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None,
        P2_tipo_de_ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None,
        P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_ente=None, P2_substantivo_lematizado=None,
        P2_numero=None, P2_tipo_feminino_ao=None, P2_tipo_masc_ao=None, P2_acent_tonica=None, P2_nome_proprio=None,
        P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None,
        P2_reflexivo=None, P2_adjetivo_epiteto=None, P2_adjetivo_classificador=None, P2_genero_adjetivo=None,
        P2_numero_adjetivo=None, P2_contracao=None,
        # P3
        P3_dissoc_ente_nucleo=None, P3_tem_qualificador=None, P3_tipo_qualificador=None,
        P3_indice_preposicao_qualif=None, P3_determinacao_especificidade_beta=None, P3_orientacao_beta=None,
        P3_genero_beta=None, P3_numero_beta=None, P3_morfologia_do_pronome_beta=None,
        P3_determinacao_especificidade_alpha=None, P3_orientacao_alpha=None, P3_genero_alpha=None, P3_numero_alpha=None,
        P3_morfologia_do_pronome_alpha=None, P3_pessoa_da_interlocucao_possuidor=None, P3_numero_obj_possuido=None,
        P3_genero_obj_possuido=None, P3_pessoa_da_interlocucao_proximidade=None, P3_funcao_numerativo=None,
        P3_cardinal=None, P3_genero=None, P3_tipo_precisa=None, P3_tipo_real_card=None, P3_milharExtenso=None,
        P3_centenaExtenso=None, P3_dezenaExtenso=None, P3_unidadeExtenso=None, P3_numIndefinido=None,
        P3_tipo_de_ente=None, P3_tipo_de_nao_consciente=None, P3_tipo_de_nao_consciente_material=None,
        P3_tipo_de_nao_consciente_semiotico=None, P3_classe_palavra_ente=None, P3_substantivo_lematizado=None,
        P3_numero=None, P3_tipo_feminino_ao=None, P3_tipo_masc_ao=None, P3_acent_tonica=None, P3_nome_proprio=None,
        P3_pessoa_da_interlocucao=None, P3_transitividade_verbo=None, P3_tonicidade=None, P3_morfologia_do_pronome=None,
        P3_reflexivo=None, P3_adjetivo_epiteto=None, P3_adjetivo_classificador=None, P3_genero_adjetivo=None,
        P3_numero_adjetivo=None, P3_contracao=None,

        ##PARTICIPANTE P3 REALIZADOS POR FP
        P3_FP_indice_preposicao_frase=None, P3_FP_dissoc_ente_nucleo=None, P3_FP_tem_qualificador=None,
        P3_FP_tipo_qualificador=None, P3_FP_indice_preposicao_qualif=None, P3_FP_determinacao_especificidade_beta=None,
        P3_FP_orientacao_beta=None, P3_FP_genero_beta=None, P3_FP_numero_beta=None,
        P3_FP_morfologia_do_pronome_beta=None, P3_FP_determinacao_especificidade_alpha=None,
        P3_FP_orientacao_alpha=None, P3_FP_genero_alpha=None, P3_FP_numero_alpha=None,
        P3_FP_morfologia_do_pronome_alpha=None, P3_FP_pessoa_da_interlocucao_possuidor=None,
        P3_FP_numero_obj_possuido=None, P3_FP_genero_obj_possuido=None, P3_FP_pessoa_da_interlocucao_proximidade=None,
        P3_FP_funcao_numerativo=None, P3_FP_cardinal=None, P3_FP_genero=None, P3_FP_tipo_precisa=None,
        P3_FP_tipo_real_card=None, P3_FP_milharExtenso=None, P3_FP_centenaExtenso=None, P3_FP_dezenaExtenso=None,
        P3_FP_unidadeExtenso=None, P3_FP_numIndefinido=None, P3_FP_tipo_de_ente=None, P3_FP_tipo_de_nao_consciente=None,
        P3_FP_tipo_de_nao_consciente_material=None, P3_FP_tipo_de_nao_consciente_semiotico=None,
        P3_FP_classe_palavra_ente=None, P3_FP_substantivo_lematizado=None, P3_FP_numero=None,
        P3_FP_tipo_feminino_ao=None, P3_FP_tipo_masc_ao=None, P3_FP_acent_tonica=None, P3_FP_nome_proprio=None,
        P3_FP_pessoa_da_interlocucao=None, P3_FP_transitividade_verbo=None, P3_FP_tonicidade=None,
        P3_FP_morfologia_do_pronome=None, P3_FP_reflexivo=None, P3_FP_adjetivo_epiteto=None,
        P3_FP_adjetivo_classificador=None, P3_FP_genero_adjetivo=None, P3_FP_numero_adjetivo=None, P3_FP_contracao=None,
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
        Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel, indiceAtrib)
        Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL, T_INTER_tipoRealizacao, T_INTER_tipo_de_adverbio1,
                                              T_INTER_ind1, T_INTER_tipo_de_adverbio2, T_INTER_ind2,
                                              T_INTER_tipo_de_adverbio3, T_INTER_ind3, T_INTER_tipo_de_adverbio4,
                                              T_INTER_ind4, T_INTER_tipo_de_adverbio5, T_INTER_ind5,
                                              T_INTER_FP_indice_preposicao_frase, T_INTER_FP_dissoc_ente_nucleo,
                                              T_INTER_FP_tem_qualificador, T_INTER_FP_tipo_qualificador,
                                              T_INTER_FP_indice_preposicao_qualif,
                                              T_INTER_FP_determinacao_especificidade_beta, T_INTER_FP_orientacao_beta,
                                              T_INTER_FP_genero_beta, T_INTER_FP_numero_beta,
                                              T_INTER_FP_morfologia_do_pronome_beta,
                                              T_INTER_FP_determinacao_especificidade_alpha, T_INTER_FP_orientacao_alpha,
                                              T_INTER_FP_genero_alpha, T_INTER_FP_numero_alpha,
                                              T_INTER_FP_morfologia_do_pronome_alpha,
                                              T_INTER_FP_pessoa_da_interlocucao_possuidor,
                                              T_INTER_FP_numero_obj_possuido, T_INTER_FP_genero_obj_possuido,
                                              T_INTER_FP_pessoa_da_interlocucao_proximidade,
                                              T_INTER_FP_funcao_numerativo, T_INTER_FP_cardinal, T_INTER_FP_genero,
                                              T_INTER_FP_tipo_precisa, T_INTER_FP_tipo_real_card,
                                              T_INTER_FP_milharExtenso, T_INTER_FP_centenaExtenso,
                                              T_INTER_FP_dezenaExtenso, T_INTER_FP_unidadeExtenso,
                                              T_INTER_FP_numIndefinido, T_INTER_FP_tipo_de_ente,
                                              T_INTER_FP_tipo_de_nao_consciente,
                                              T_INTER_FP_tipo_de_nao_consciente_material,
                                              T_INTER_FP_tipo_de_nao_consciente_semiotico,
                                              T_INTER_FP_classe_palavra_ente, T_INTER_FP_substantivo_lematizado,
                                              T_INTER_FP_numero, T_INTER_FP_tipo_feminino_ao, T_INTER_FP_tipo_masc_ao,
                                              T_INTER_FP_acent_tonica, T_INTER_FP_nome_proprio,
                                              T_INTER_FP_pessoa_da_interlocucao, T_INTER_FP_transitividade_verbo,
                                              T_INTER_FP_tonicidade, T_INTER_FP_morfologia_do_pronome,
                                              T_INTER_FP_reflexivo, T_INTER_FP_adjetivo_epiteto,
                                              T_INTER_FP_adjetivo_classificador, T_INTER_FP_genero_adjetivo,
                                              T_INTER_FP_numero_adjetivo, T_INTER_FP_contracao, T_INTER_indiceElemQu,
                                              T_INTER_indicePartModal, T_INTER_nome_proprio)
        Tema_textual = TEMA_TEXTUAL(T_TEXT_temTemaTextual, T_TEXT_tipo_insercao_Cont, T_TEXT_conj_extenso_Cont,
                                    T_TEXT_indiceCont, T_TEXT_tipo_insercao_Conj, T_TEXT_tipo_de_conjuncao_Conj,
                                    T_TEXT_conj_extensoConj, T_TEXT_indiceConj, T_TEXT_tipo_insercao_Rel,
                                    T_TEXT_pron_extenso_Rel, T_TEXT_tipo_de_relativo, T_TEXT_tipo_pronome_relativo,
                                    T_TEXT_generoTemaTextual, T_TEXT_numeroTemaTextual, T_TEXT_indiceRelativo,
                                    T_TEXT_indiceRelativoAdv)
        Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        Polaridade = POLARIDADE(tipo_polaridade)
        Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
                                verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                                padrao_pessoa_morfologia_LEX)
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

        if Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_efetivo_operativo':
            # NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDENS DE AGENTES
            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)

            INICIADOR = '+iniciador'
            Iniciador = estrutura_gn(P3_dissoc_ente_nucleo, P3_tem_qualificador, P3_tipo_qualificador,
                                     P3_indice_preposicao_qualif, P3_determinacao_especificidade_beta,
                                     P3_orientacao_beta, P3_genero_beta, P3_numero_beta, P3_morfologia_do_pronome_beta,
                                     P3_determinacao_especificidade_alpha, P3_orientacao_alpha, P3_genero_alpha,
                                     P3_numero_alpha, P3_morfologia_do_pronome_alpha,
                                     P3_pessoa_da_interlocucao_possuidor, P3_numero_obj_possuido,
                                     P3_genero_obj_possuido, P3_pessoa_da_interlocucao_proximidade,
                                     P3_funcao_numerativo, P3_cardinal, P3_genero, P3_tipo_precisa, P3_tipo_real_card,
                                     P3_milharExtenso, P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso,
                                     P3_numIndefinido, P3_tipo_de_ente, P3_tipo_de_nao_consciente,
                                     P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico,
                                     P3_classe_palavra_ente, P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ao,
                                     P3_tipo_masc_ao, P3_acent_tonica, P3_nome_proprio, P3_pessoa_da_interlocucao,
                                     P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo,
                                     P3_adjetivo_epiteto, P3_adjetivo_classificador, P3_genero_adjetivo,
                                     P3_numero_adjetivo, P3_contracao)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                  P3_FP_tem_qualificador,
                                                  P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                  P3_FP_determinacao_especificidade_beta,
                                                  P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                  P3_FP_morfologia_do_pronome_beta,
                                                  P3_FP_determinacao_especificidade_alpha,
                                                  P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                  P3_FP_morfologia_do_pronome_alpha,
                                                  P3_FP_pessoa_da_interlocucao_possuidor,
                                                  P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                                  P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                                  P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa,
                                                  P3_FP_tipo_real_card,
                                                  P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                                  P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                  P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                                  P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                  P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                  P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                  P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                  P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                  P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                  P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                   P3_FP_tem_qualificador,
                                                   P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                   P3_FP_determinacao_especificidade_beta,
                                                   P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                   P3_FP_morfologia_do_pronome_beta,
                                                   P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                   P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                   P3_FP_morfologia_do_pronome_alpha,
                                                   P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                   P3_FP_genero_obj_possuido, P3_FP_pessoa_da_interlocucao_proximidade,
                                                   P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                   P3_FP_tipo_precisa,
                                                   P3_FP_tipo_real_card, P3_FP_milharExtenso, P3_FP_centenaExtenso,
                                                   P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido,
                                                   P3_FP_tipo_de_ente, P3_FP_tipo_de_nao_consciente,
                                                   P3_FP_tipo_de_nao_consciente_material,
                                                   P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                   P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                   P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                   P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                   P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                   P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                   P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Iniciador, Polaridade, Processo, Ator, Locativo, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Iniciador, Polaridade, Processo, Ator, Locativo, Cliente + '?'))


        elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance':
            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)
            INICIADOR == '-iniciador'
            Iniciador = ''
            oracao = Ator + ' ' + Polaridade + ' ' + Processo
            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                  P3_FP_tem_qualificador,
                                                  P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                  P3_FP_determinacao_especificidade_beta,
                                                  P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                  P3_FP_morfologia_do_pronome_beta,
                                                  P3_FP_determinacao_especificidade_alpha,
                                                  P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                  P3_FP_morfologia_do_pronome_alpha,
                                                  P3_FP_pessoa_da_interlocucao_possuidor,
                                                  P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                                  P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                                  P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa,
                                                  P3_FP_tipo_real_card,
                                                  P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                                  P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                  P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                                  P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                  P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                  P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                  P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                  P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                  P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                  P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                   P3_FP_tem_qualificador,
                                                   P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                   P3_FP_determinacao_especificidade_beta,
                                                   P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                   P3_FP_morfologia_do_pronome_beta,
                                                   P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                   P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                   P3_FP_morfologia_do_pronome_alpha,
                                                   P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                   P3_FP_genero_obj_possuido, P3_FP_pessoa_da_interlocucao_proximidade,
                                                   P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                   P3_FP_tipo_precisa,
                                                   P3_FP_tipo_real_card, P3_FP_milharExtenso, P3_FP_centenaExtenso,
                                                   P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido,
                                                   P3_FP_tipo_de_ente, P3_FP_tipo_de_nao_consciente,
                                                   P3_FP_tipo_de_nao_consciente_material,
                                                   P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                   P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                   P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                   P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                   P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                   P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                   P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((oracao, Locativo, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((oracao, Locativo, Cliente + '?'))

        elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance':
            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)

            try:
                if ESCOPO == '+escopo':
                    Escopo = estrutura_gn(P3_dissoc_ente_nucleo, P3_tem_qualificador, P3_tipo_qualificador,
                                          P3_indice_preposicao_qualif, P3_determinacao_especificidade_beta,
                                          P3_orientacao_beta, P3_genero_beta, P3_numero_beta,
                                          P3_morfologia_do_pronome_beta, P3_determinacao_especificidade_alpha,
                                          P3_orientacao_alpha, P3_genero_alpha, P3_numero_alpha,
                                          P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocucao_possuidor,
                                          P3_numero_obj_possuido, P3_genero_obj_possuido,
                                          P3_pessoa_da_interlocucao_proximidade, P3_funcao_numerativo, P3_cardinal,
                                          P3_genero, P3_tipo_precisa, P3_tipo_real_card, P3_milharExtenso,
                                          P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso, P3_numIndefinido,
                                          P3_tipo_de_ente, P3_tipo_de_nao_consciente,
                                          P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico,
                                          P3_classe_palavra_ente, P3_substantivo_lematizado, P3_numero,
                                          P3_tipo_feminino_ao, P3_tipo_masc_ao, P3_acent_tonica, P3_nome_proprio,
                                          P3_pessoa_da_interlocucao, P3_transitividade_verbo, P3_tonicidade,
                                          P3_morfologia_do_pronome, P3_reflexivo, P3_adjetivo_epiteto,
                                          P3_adjetivo_classificador, P3_genero_adjetivo, P3_numero_adjetivo,
                                          P3_contracao)

                elif ESCOPO == '-escopo':
                    Escopo = ''
            except:
                Escopo = ''

            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                   P3_FP_tem_qualificador,
                                                   P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                   P3_FP_determinacao_especificidade_beta,
                                                   P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                   P3_FP_morfologia_do_pronome_beta,
                                                   P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                   P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                   P3_FP_morfologia_do_pronome_alpha,
                                                   P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                   P3_FP_genero_obj_possuido, P3_FP_pessoa_da_interlocucao_proximidade,
                                                   P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                   P3_FP_tipo_precisa,
                                                   P3_FP_tipo_real_card, P3_FP_milharExtenso, P3_FP_centenaExtenso,
                                                   P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido,
                                                   P3_FP_tipo_de_ente, P3_FP_tipo_de_nao_consciente,
                                                   P3_FP_tipo_de_nao_consciente_material,
                                                   P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                   P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                   P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                   P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                   P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                   P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                   P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Escopo, Locativo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Escopo, Locativo + '?'))

        elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance':

            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo + '?'))

        elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo':
            # NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDENS DE AGENTES
            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)
            Meta = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                P2_indice_preposicao_qualif,
                                P2_determinacao_especificidade_beta, P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                P2_orientacao_alpha,
                                P2_genero_alpha, P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido, P2_genero_obj_possuido,
                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                P2_dezenaExtenso,
                                P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                P2_contracao)

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
                                                       ATRIB_numero_obj_possuido,
                                                       ATRIB_genero_obj_possuido,
                                                       ATRIB_pessoa_da_interlocucao_proximidade,
                                                       ATRIB_funcao_numerativo, ATRIB_cardinal, ATRIB_genero,
                                                       ATRIB_tipo_precisa, ATRIB_tipo_real_card, ATRIB_milharExtenso,
                                                       ATRIB_centenaExtenso, ATRIB_dezenaExtenso, ATRIB_unidadeExtenso,
                                                       ATRIB_numIndefinido, ATRIB_tipo_de_ente,
                                                       ATRIB_tipo_de_nao_consciente,
                                                       ATRIB_tipo_de_nao_consciente_material,
                                                       ATRIB_tipo_de_nao_consciente_semiotico,
                                                       ATRIB_classe_palavra_ente,
                                                       ATRIB_substantivo_lematizado, ATRIB_numero,
                                                       ATRIB_tipo_feminino_ao,
                                                       ATRIB_tipo_masc_ao, ATRIB_acent_tonica, ATRIB_nome_proprio,
                                                       ATRIB_pessoa_da_interlocucao, ATRIB_transitividade_verbo,
                                                       ATRIB_tonicidade, ATRIB_morfologia_do_pronome, ATRIB_reflexivo,
                                                       ATRIB_adjetivo_epiteto, ATRIB_adjetivo_classificador,
                                                       ATRIB_genero_adjetivo, ATRIB_numero_adjetivo, ATRIB_contracao)
                elif RESULTADO_QUALITATIVO == '-resultado':
                    Atributo = ''
            except:
                Atributo = ''

            try:
                if BENEFICIARIO == '+recipiente':
                    Recipiente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                     P3_FP_tem_qualificador,
                                                     P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                     P3_FP_determinacao_especificidade_beta,
                                                     P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                     P3_FP_morfologia_do_pronome_beta,
                                                     P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                     P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                     P3_FP_morfologia_do_pronome_alpha,
                                                     P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                     P3_FP_genero_obj_possuido,
                                                     P3_FP_pessoa_da_interlocucao_proximidade,
                                                     P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                     P3_FP_tipo_precisa, P3_FP_tipo_real_card, P3_FP_milharExtenso,
                                                     P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso,
                                                     P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                     P3_FP_tipo_de_nao_consciente,
                                                     P3_FP_tipo_de_nao_consciente_material,
                                                     P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                     P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                     P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                     P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                     P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                     P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                     P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-recipiente':
                    Recipiente = ''
            except:
                Recipiente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                   P3_FP_tem_qualificador,
                                                   P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                   P3_FP_determinacao_especificidade_beta,
                                                   P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                   P3_FP_morfologia_do_pronome_beta,
                                                   P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                   P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                   P3_FP_morfologia_do_pronome_alpha,
                                                   P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                   P3_FP_genero_obj_possuido, P3_FP_pessoa_da_interlocucao_proximidade,
                                                   P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                   P3_FP_tipo_precisa,
                                                   P3_FP_tipo_real_card, P3_FP_milharExtenso, P3_FP_centenaExtenso,
                                                   P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido,
                                                   P3_FP_tipo_de_ente, P3_FP_tipo_de_nao_consciente,
                                                   P3_FP_tipo_de_nao_consciente_material,
                                                   P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                   P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                   P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                   P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                   P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                   P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                   P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Meta, Atributo, Locativo, Recipiente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Meta, Atributo, Locativo, Recipiente + '?'))

        elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo':

            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)
            Meta = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                P2_indice_preposicao_qualif,
                                P2_determinacao_especificidade_beta, P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                P2_orientacao_alpha,
                                P2_genero_alpha, P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido, P2_genero_obj_possuido,
                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                P2_dezenaExtenso,
                                P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                P2_contracao)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                  P3_FP_tem_qualificador,
                                                  P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                  P3_FP_determinacao_especificidade_beta,
                                                  P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                  P3_FP_morfologia_do_pronome_beta,
                                                  P3_FP_determinacao_especificidade_alpha,
                                                  P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                  P3_FP_morfologia_do_pronome_alpha,
                                                  P3_FP_pessoa_da_interlocucao_possuidor,
                                                  P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                                  P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                                  P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa,
                                                  P3_FP_tipo_real_card,
                                                  P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                                  P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                  P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                                  P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                  P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                  P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                  P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                  P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                  P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                  P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Meta, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Meta, Cliente + '?'))

        ##MATERIAL METEOROLÓGICA
        elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_processo_com_alcance':
            Escopo = estrutura_gn(P3_dissoc_ente_nucleo, P3_tem_qualificador, P3_tipo_qualificador,
                                  P3_indice_preposicao_qualif, P3_determinacao_especificidade_beta, P3_orientacao_beta,
                                  P3_genero_beta, P3_numero_beta, P3_morfologia_do_pronome_beta,
                                  P3_determinacao_especificidade_alpha, P3_orientacao_alpha, P3_genero_alpha,
                                  P3_numero_alpha, P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocucao_possuidor,
                                  P3_numero_obj_possuido, P3_genero_obj_possuido, P3_pessoa_da_interlocucao_proximidade,
                                  P3_funcao_numerativo, P3_cardinal, P3_genero, P3_tipo_precisa, P3_tipo_real_card,
                                  P3_milharExtenso, P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso,
                                  P3_numIndefinido, P3_tipo_de_ente, P3_tipo_de_nao_consciente,
                                  P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico,
                                  P3_classe_palavra_ente, P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ao,
                                  P3_tipo_masc_ao, P3_acent_tonica, P3_nome_proprio, P3_pessoa_da_interlocucao,
                                  P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo,
                                  P3_adjetivo_epiteto, P3_adjetivo_classificador, P3_genero_adjetivo,
                                  P3_numero_adjetivo, P3_contracao)

            if Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Processo, Escopo + '.'))
            elif Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Processo, Escopo + '?'))

        elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_processo_sem_alcance':
            if Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = Processo + '.'
            elif Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = Processo + '?'

        # 		##########COMEÇO DE AGENCIAMENTO PASSIVA
        #
        #
        elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo':

            Ator = frase_preposicional(P1_FP_indice_preposicao_frase, P1_FP_dissoc_ente_nucleo, P1_FP_tem_qualificador,
                                       P1_FP_tipo_qualificador, P1_FP_indice_preposicao_qualif,
                                       P1_FP_determinacao_especificidade_beta,
                                       P1_FP_orientacao_beta, P1_FP_genero_beta, P1_FP_numero_beta,
                                       P1_FP_morfologia_do_pronome_beta, P1_FP_determinacao_especificidade_alpha,
                                       P1_FP_orientacao_alpha, P1_FP_genero_alpha, P1_FP_numero_alpha,
                                       P1_FP_morfologia_do_pronome_alpha, P1_FP_pessoa_da_interlocucao_possuidor,
                                       P1_FP_numero_obj_possuido, P1_FP_genero_obj_possuido,
                                       P1_FP_pessoa_da_interlocucao_proximidade, P1_FP_funcao_numerativo,
                                       P1_FP_cardinal,
                                       P1_FP_genero, P1_FP_tipo_precisa, P1_FP_tipo_real_card, P1_FP_milharExtenso,
                                       P1_FP_centenaExtenso, P1_FP_dezenaExtenso, P1_FP_unidadeExtenso,
                                       P1_FP_numIndefinido,
                                       P1_FP_tipo_de_ente, P1_FP_tipo_de_nao_consciente,
                                       P1_FP_tipo_de_nao_consciente_material, P1_FP_tipo_de_nao_consciente_semiotico,
                                       P1_FP_classe_palavra_ente, P1_FP_substantivo_lematizado, P1_FP_numero,
                                       P1_FP_tipo_feminino_ao, P1_FP_tipo_masc_ao, P1_FP_acent_tonica,
                                       P1_FP_nome_proprio,
                                       P1_FP_pessoa_da_interlocucao, P1_FP_transitividade_verbo, P1_FP_tonicidade,
                                       P1_FP_morfologia_do_pronome, P1_FP_reflexivo, P1_FP_adjetivo_epiteto,
                                       P1_FP_adjetivo_classificador, P1_FP_genero_adjetivo, P1_FP_numero_adjetivo,
                                       P1_FP_contracao)
            Meta = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                P2_indice_preposicao_qualif,
                                P2_determinacao_especificidade_beta, P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                P2_orientacao_alpha,
                                P2_genero_alpha, P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido, P2_genero_obj_possuido,
                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                P2_dezenaExtenso,
                                P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                P2_contracao)

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
                                                       ATRIB_numero_obj_possuido,
                                                       ATRIB_genero_obj_possuido,
                                                       ATRIB_pessoa_da_interlocucao_proximidade,
                                                       ATRIB_funcao_numerativo, ATRIB_cardinal, ATRIB_genero,
                                                       ATRIB_tipo_precisa, ATRIB_tipo_real_card, ATRIB_milharExtenso,
                                                       ATRIB_centenaExtenso, ATRIB_dezenaExtenso, ATRIB_unidadeExtenso,
                                                       ATRIB_numIndefinido, ATRIB_tipo_de_ente,
                                                       ATRIB_tipo_de_nao_consciente,
                                                       ATRIB_tipo_de_nao_consciente_material,
                                                       ATRIB_tipo_de_nao_consciente_semiotico,
                                                       ATRIB_classe_palavra_ente,
                                                       ATRIB_substantivo_lematizado, ATRIB_numero,
                                                       ATRIB_tipo_feminino_ao,
                                                       ATRIB_tipo_masc_ao, ATRIB_acent_tonica, ATRIB_nome_proprio,
                                                       ATRIB_pessoa_da_interlocucao, ATRIB_transitividade_verbo,
                                                       ATRIB_tonicidade, ATRIB_morfologia_do_pronome, ATRIB_reflexivo,
                                                       ATRIB_adjetivo_epiteto, ATRIB_adjetivo_classificador,
                                                       ATRIB_genero_adjetivo, ATRIB_numero_adjetivo, ATRIB_contracao)
                elif RESULTADO_QUALITATIVO == '-resultado':
                    Atributo = ''
            except:
                Atributo = ''

            try:
                if BENEFICIARIO == '+recipiente':
                    Recipiente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                     P3_FP_tem_qualificador,
                                                     P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                     P3_FP_determinacao_especificidade_beta,
                                                     P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                     P3_FP_morfologia_do_pronome_beta,
                                                     P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                     P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                     P3_FP_morfologia_do_pronome_alpha,
                                                     P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                     P3_FP_genero_obj_possuido,
                                                     P3_FP_pessoa_da_interlocucao_proximidade,
                                                     P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                     P3_FP_tipo_precisa, P3_FP_tipo_real_card, P3_FP_milharExtenso,
                                                     P3_FP_centenaExtenso, P3_FP_dezenaExtenso, P3_FP_unidadeExtenso,
                                                     P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                     P3_FP_tipo_de_nao_consciente,
                                                     P3_FP_tipo_de_nao_consciente_material,
                                                     P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                     P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                     P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                     P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                     P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                     P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                     P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-recipiente':
                    Recipiente = ''
                else:
                    Recipiente = ''
            except:
                Recipiente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                   P3_FP_tem_qualificador,
                                                   P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                   P3_FP_determinacao_especificidade_beta,
                                                   P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                   P3_FP_morfologia_do_pronome_beta,
                                                   P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                   P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                   P3_FP_morfologia_do_pronome_alpha,
                                                   P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                   P3_FP_genero_obj_possuido, P3_FP_pessoa_da_interlocucao_proximidade,
                                                   P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                   P3_FP_tipo_precisa,
                                                   P3_FP_tipo_real_card, P3_FP_milharExtenso, P3_FP_centenaExtenso,
                                                   P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido,
                                                   P3_FP_tipo_de_ente, P3_FP_tipo_de_nao_consciente,
                                                   P3_FP_tipo_de_nao_consciente_material,
                                                   P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                   P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                   P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                   P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                   P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                   P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                   P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, Polaridade, Processo, Atributo, Ator, Locativo, Recipiente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, Polaridade, Processo, Atributo, Ator, Locativo, Recipiente + '?'))

        ######################################################################
        elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo':

            Ator = frase_preposicional(P1_FP_indice_preposicao_frase, P1_FP_dissoc_ente_nucleo, P1_FP_tem_qualificador,
                                       P1_FP_tipo_qualificador, P1_FP_indice_preposicao_qualif,
                                       P1_FP_determinacao_especificidade_beta,
                                       P1_FP_orientacao_beta, P1_FP_genero_beta, P1_FP_numero_beta,
                                       P1_FP_morfologia_do_pronome_beta, P1_FP_determinacao_especificidade_alpha,
                                       P1_FP_orientacao_alpha, P1_FP_genero_alpha, P1_FP_numero_alpha,
                                       P1_FP_morfologia_do_pronome_alpha, P1_FP_pessoa_da_interlocucao_possuidor,
                                       P1_FP_numero_obj_possuido, P1_FP_genero_obj_possuido,
                                       P1_FP_pessoa_da_interlocucao_proximidade, P1_FP_funcao_numerativo,
                                       P1_FP_cardinal,
                                       P1_FP_genero, P1_FP_tipo_precisa, P1_FP_tipo_real_card, P1_FP_milharExtenso,
                                       P1_FP_centenaExtenso, P1_FP_dezenaExtenso, P1_FP_unidadeExtenso,
                                       P1_FP_numIndefinido,
                                       P1_FP_tipo_de_ente, P1_FP_tipo_de_nao_consciente,
                                       P1_FP_tipo_de_nao_consciente_material, P1_FP_tipo_de_nao_consciente_semiotico,
                                       P1_FP_classe_palavra_ente, P1_FP_substantivo_lematizado, P1_FP_numero,
                                       P1_FP_tipo_feminino_ao, P1_FP_tipo_masc_ao, P1_FP_acent_tonica,
                                       P1_FP_nome_proprio,
                                       P1_FP_pessoa_da_interlocucao, P1_FP_transitividade_verbo, P1_FP_tonicidade,
                                       P1_FP_morfologia_do_pronome, P1_FP_reflexivo, P1_FP_adjetivo_epiteto,
                                       P1_FP_adjetivo_classificador, P1_FP_genero_adjetivo, P1_FP_numero_adjetivo,
                                       P1_FP_contracao)
            Meta = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                P2_indice_preposicao_qualif,
                                P2_determinacao_especificidade_beta, P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                P2_orientacao_alpha,
                                P2_genero_alpha, P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido, P2_genero_obj_possuido,
                                P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                P2_dezenaExtenso,
                                P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                P2_contracao)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                  P3_FP_tem_qualificador,
                                                  P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                  P3_FP_determinacao_especificidade_beta,
                                                  P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                  P3_FP_morfologia_do_pronome_beta,
                                                  P3_FP_determinacao_especificidade_alpha,
                                                  P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                  P3_FP_morfologia_do_pronome_alpha,
                                                  P3_FP_pessoa_da_interlocucao_possuidor,
                                                  P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                                  P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                                  P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa,
                                                  P3_FP_tipo_real_card,
                                                  P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                                  P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                  P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                                  P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                  P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                  P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                  P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                  P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                  P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                  P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, Polaridade, Processo, Ator, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Meta, Polaridade, Processo, Ator, Cliente + '?'))

        elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_efetivo_receptivo':
            # NÃO CONTEMPLO O POTENCIAL DE SEGUNDA ORDEM DE AGENTES
            Ator = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                P1_indice_preposicao_qualif,
                                P1_determinacao_especificidade_beta, P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                P1_orientacao_alpha,
                                P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                P1_dezenaExtenso,
                                P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                P1_contracao)

            INICIADOR = '+iniciador'
            Iniciador = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                            P3_FP_tem_qualificador,
                                            P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                            P3_FP_determinacao_especificidade_beta,
                                            P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                            P3_FP_morfologia_do_pronome_beta, P3_FP_determinacao_especificidade_alpha,
                                            P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                            P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocucao_possuidor,
                                            P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                            P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                            P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipo_real_card,
                                            P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                            P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                            P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                            P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                            P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                            P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                            P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade,
                                            P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_adjetivo_epiteto,
                                            P3_FP_adjetivo_classificador, P3_FP_genero_adjetivo, P3_FP_numero_adjetivo,
                                            P3_FP_contracao)

            try:
                if BENEFICIARIO == '+cliente':
                    Cliente = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                  P3_FP_tem_qualificador,
                                                  P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                  P3_FP_determinacao_especificidade_beta,
                                                  P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                  P3_FP_morfologia_do_pronome_beta,
                                                  P3_FP_determinacao_especificidade_alpha,
                                                  P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                  P3_FP_morfologia_do_pronome_alpha,
                                                  P3_FP_pessoa_da_interlocucao_possuidor,
                                                  P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                                  P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                                  P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa,
                                                  P3_FP_tipo_real_card,
                                                  P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                                  P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                                  P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                                  P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                  P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                  P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                  P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                  P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                  P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                  P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif BENEFICIARIO == '-cliente':
                    Cliente = ''
            except:
                Cliente = ''
            try:
                if LOCATIVO == '+locativo':
                    Locativo = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                                   P3_FP_tem_qualificador,
                                                   P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                                   P3_FP_determinacao_especificidade_beta,
                                                   P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                                   P3_FP_morfologia_do_pronome_beta,
                                                   P3_FP_determinacao_especificidade_alpha, P3_FP_orientacao_alpha,
                                                   P3_FP_genero_alpha, P3_FP_numero_alpha,
                                                   P3_FP_morfologia_do_pronome_alpha,
                                                   P3_FP_pessoa_da_interlocucao_possuidor, P3_FP_numero_obj_possuido,
                                                   P3_FP_genero_obj_possuido, P3_FP_pessoa_da_interlocucao_proximidade,
                                                   P3_FP_funcao_numerativo, P3_FP_cardinal, P3_FP_genero,
                                                   P3_FP_tipo_precisa,
                                                   P3_FP_tipo_real_card, P3_FP_milharExtenso, P3_FP_centenaExtenso,
                                                   P3_FP_dezenaExtenso, P3_FP_unidadeExtenso, P3_FP_numIndefinido,
                                                   P3_FP_tipo_de_ente, P3_FP_tipo_de_nao_consciente,
                                                   P3_FP_tipo_de_nao_consciente_material,
                                                   P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                                   P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                                   P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                                   P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                                   P3_FP_tonicidade, P3_FP_morfologia_do_pronome, P3_FP_reflexivo,
                                                   P3_FP_adjetivo_epiteto, P3_FP_adjetivo_classificador,
                                                   P3_FP_genero_adjetivo, P3_FP_numero_adjetivo, P3_FP_contracao)
                elif LOCATIVO == '-locativo':
                    Locativo = ''
            except:
                Locativo = ''
            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Locativo, Iniciador, Cliente + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Ator, Polaridade, Processo, Locativo, Iniciador, Cliente + '?'))

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
        TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None, indiceAtrib=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, T_INTER_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        T_INTER_tipo_de_adverbio1=None, T_INTER_ind1=None,
        T_INTER_tipo_de_adverbio2=None, T_INTER_ind2=None,
        T_INTER_tipo_de_adverbio3=None, T_INTER_ind3=None,
        T_INTER_tipo_de_adverbio4=None, T_INTER_ind4=None,
        T_INTER_tipo_de_adverbio5=None, T_INTER_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        T_INTER_FP_indice_preposicao_frase=None, T_INTER_FP_dissoc_ente_nucleo=None, T_INTER_FP_tem_qualificador=None,
        T_INTER_FP_tipo_qualificador=None, T_INTER_FP_indice_preposicao_qualif=None,
        T_INTER_FP_determinacao_especificidade_beta=None, T_INTER_FP_orientacao_beta=None, T_INTER_FP_genero_beta=None,
        T_INTER_FP_numero_beta=None, T_INTER_FP_morfologia_do_pronome_beta=None,
        T_INTER_FP_determinacao_especificidade_alpha=None, T_INTER_FP_orientacao_alpha=None,
        T_INTER_FP_genero_alpha=None, T_INTER_FP_numero_alpha=None, T_INTER_FP_morfologia_do_pronome_alpha=None,
        T_INTER_FP_pessoa_da_interlocucao_possuidor=None, T_INTER_FP_numero_obj_possuido=None,
        T_INTER_FP_genero_obj_possuido=None, T_INTER_FP_pessoa_da_interlocucao_proximidade=None,
        T_INTER_FP_funcao_numerativo=None, T_INTER_FP_cardinal=None, T_INTER_FP_genero=None,
        T_INTER_FP_tipo_precisa=None, T_INTER_FP_tipo_real_card=None, T_INTER_FP_milharExtenso=None,
        T_INTER_FP_centenaExtenso=None, T_INTER_FP_dezenaExtenso=None, T_INTER_FP_unidadeExtenso=None,
        T_INTER_FP_numIndefinido=None, T_INTER_FP_tipo_de_ente=None, T_INTER_FP_tipo_de_nao_consciente=None,
        T_INTER_FP_tipo_de_nao_consciente_material=None, T_INTER_FP_tipo_de_nao_consciente_semiotico=None,
        T_INTER_FP_classe_palavra_ente=None, T_INTER_FP_substantivo_lematizado=None, T_INTER_FP_numero=None,
        T_INTER_FP_tipo_feminino_ao=None, T_INTER_FP_tipo_masc_ao=None, T_INTER_FP_acent_tonica=None,
        T_INTER_FP_nome_proprio=None, T_INTER_FP_pessoa_da_interlocucao=None, T_INTER_FP_transitividade_verbo=None,
        T_INTER_FP_tonicidade=None, T_INTER_FP_morfologia_do_pronome=None, T_INTER_FP_reflexivo=None,
        T_INTER_FP_adjetivo_epiteto=None, T_INTER_FP_adjetivo_classificador=None, T_INTER_FP_genero_adjetivo=None,
        T_INTER_FP_numero_adjetivo=None, T_INTER_FP_contracao=None,
        #
        # 		#
        T_INTER_indiceElemQu=None, T_INTER_indicePartModal=None, T_INTER_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        T_TEXT_temTemaTextual='-', T_TEXT_tipo_insercao_Cont="inserção_menu", T_TEXT_conj_extenso_Cont=None,
        T_TEXT_indiceCont=None,
        T_TEXT_tipo_insercao_Conj="inserção_menu", T_TEXT_tipo_de_conjuncao_Conj=None, T_TEXT_conj_extensoConj=None,
        T_TEXT_indiceConj=None,
        T_TEXT_tipo_insercao_Rel='inserção_menu', T_TEXT_pron_extenso_Rel=None, T_TEXT_tipo_de_relativo=None,
        T_TEXT_tipo_pronome_relativo=None, T_TEXT_generoTemaTextual=None, T_TEXT_numeroTemaTextual=None,
        T_TEXT_indiceRelativo=None,
        T_TEXT_indiceRelativoAdv=None,
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
        TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None,
        verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
        padrao_pessoa_morfologia_LEX='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        P1_dissoc_ente_nucleo=None, P1_tem_qualificador=None, P1_tipo_qualificador=None,
        P1_indice_preposicao_qualif=None, P1_determinacao_especificidade_beta=None, P1_orientacao_beta=None,
        P1_genero_beta=None, P1_numero_beta=None, P1_morfologia_do_pronome_beta=None,
        P1_determinacao_especificidade_alpha=None, P1_orientacao_alpha=None, P1_genero_alpha=None, P1_numero_alpha=None,
        P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocucao_possuidor=None, P1_numero_obj_possuido=None,
        P1_genero_obj_possuido=None, P1_pessoa_da_interlocucao_proximidade=None, P1_funcao_numerativo=None,
        P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipo_real_card=None, P1_milharExtenso=None,
        P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None,
        P1_tipo_de_ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None,
        P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_ente=None, P1_substantivo_lematizado=None,
        P1_numero=None, P1_tipo_feminino_ao=None, P1_tipo_masc_ao=None, P1_acent_tonica=None, P1_nome_proprio=None,
        P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None,
        P1_reflexivo=None, P1_adjetivo_epiteto=None, P1_adjetivo_classificador=None, P1_genero_adjetivo=None,
        P1_numero_adjetivo=None, P1_contracao=None,
        ##PARTICIPANTE P1 REALIZADOS POR FP
        P1_FP_indice_preposicao_frase=None, P1_FP_dissoc_ente_nucleo=None, P1_FP_tem_qualificador=None,
        P1_FP_tipo_qualificador=None, P1_FP_indice_preposicao_qualif=None, P1_FP_determinacao_especificidade_beta=None,
        P1_FP_orientacao_beta=None, P1_FP_genero_beta=None, P1_FP_numero_beta=None,
        P1_FP_morfologia_do_pronome_beta=None, P1_FP_determinacao_especificidade_alpha=None,
        P1_FP_orientacao_alpha=None, P1_FP_genero_alpha=None, P1_FP_numero_alpha=None,
        P1_FP_morfologia_do_pronome_alpha=None, P1_FP_pessoa_da_interlocucao_possuidor=None,
        P1_FP_numero_obj_possuido=None, P1_FP_genero_obj_possuido=None, P1_FP_pessoa_da_interlocucao_proximidade=None,
        P1_FP_funcao_numerativo=None, P1_FP_cardinal=None, P1_FP_genero=None, P1_FP_tipo_precisa=None,
        P1_FP_tipo_real_card=None, P1_FP_milharExtenso=None, P1_FP_centenaExtenso=None, P1_FP_dezenaExtenso=None,
        P1_FP_unidadeExtenso=None, P1_FP_numIndefinido=None, P1_FP_tipo_de_ente=None, P1_FP_tipo_de_nao_consciente=None,
        P1_FP_tipo_de_nao_consciente_material=None, P1_FP_tipo_de_nao_consciente_semiotico=None,
        P1_FP_classe_palavra_ente=None, P1_FP_substantivo_lematizado=None, P1_FP_numero=None,
        P1_FP_tipo_feminino_ao=None, P1_FP_tipo_masc_ao=None, P1_FP_acent_tonica=None, P1_FP_nome_proprio=None,
        P1_FP_pessoa_da_interlocucao=None, P1_FP_transitividade_verbo=None, P1_FP_tonicidade=None,
        P1_FP_morfologia_do_pronome=None, P1_FP_reflexivo=None, P1_FP_adjetivo_epiteto=None,
        P1_FP_adjetivo_classificador=None, P1_FP_genero_adjetivo=None, P1_FP_numero_adjetivo=None, P1_FP_contracao=None,
        # P2
        P2_dissoc_ente_nucleo=None, P2_tem_qualificador=None, P2_tipo_qualificador=None,
        P2_indice_preposicao_qualif=None, P2_determinacao_especificidade_beta=None, P2_orientacao_beta=None,
        P2_genero_beta=None, P2_numero_beta=None, P2_morfologia_do_pronome_beta=None,
        P2_determinacao_especificidade_alpha=None, P2_orientacao_alpha=None, P2_genero_alpha=None, P2_numero_alpha=None,
        P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocucao_possuidor=None, P2_numero_obj_possuido=None,
        P2_genero_obj_possuido=None, P2_pessoa_da_interlocucao_proximidade=None, P2_funcao_numerativo=None,
        P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipo_real_card=None, P2_milharExtenso=None,
        P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None,
        P2_tipo_de_ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None,
        P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_ente=None, P2_substantivo_lematizado=None,
        P2_numero=None, P2_tipo_feminino_ao=None, P2_tipo_masc_ao=None, P2_acent_tonica=None, P2_nome_proprio=None,
        P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None,
        P2_reflexivo=None, P2_adjetivo_epiteto=None, P2_adjetivo_classificador=None, P2_genero_adjetivo=None,
        P2_numero_adjetivo=None, P2_contracao=None,
        # P2 FRASE PREP
        P2_FP_indice_preposicao_frase=None, P2_FP_dissoc_ente_nucleo=None, P2_FP_tem_qualificador=None,
        P2_FP_tipo_qualificador=None, P2_FP_indice_preposicao_qualif=None, P2_FP_determinacao_especificidade_beta=None,
        P2_FP_orientacao_beta=None, P2_FP_genero_beta=None, P2_FP_numero_beta=None,
        P2_FP_morfologia_do_pronome_beta=None, P2_FP_determinacao_especificidade_alpha=None,
        P2_FP_orientacao_alpha=None, P2_FP_genero_alpha=None, P2_FP_numero_alpha=None,
        P2_FP_morfologia_do_pronome_alpha=None, P2_FP_pessoa_da_interlocucao_possuidor=None,
        P2_FP_numero_obj_possuido=None, P2_FP_genero_obj_possuido=None, P2_FP_pessoa_da_interlocucao_proximidade=None,
        P2_FP_funcao_numerativo=None, P2_FP_cardinal=None, P2_FP_genero=None, P2_FP_tipo_precisa=None,
        P2_FP_tipo_real_card=None, P2_FP_milharExtenso=None, P2_FP_centenaExtenso=None, P2_FP_dezenaExtenso=None,
        P2_FP_unidadeExtenso=None, P2_FP_numIndefinido=None, P2_FP_tipo_de_ente=None, P2_FP_tipo_de_nao_consciente=None,
        P2_FP_tipo_de_nao_consciente_material=None, P2_FP_tipo_de_nao_consciente_semiotico=None,
        P2_FP_classe_palavra_ente=None, P2_FP_substantivo_lematizado=None, P2_FP_numero=None,
        P2_FP_tipo_feminino_ao=None, P2_FP_tipo_masc_ao=None, P2_FP_acent_tonica=None, P2_FP_nome_proprio=None,
        P2_FP_pessoa_da_interlocucao=None, P2_FP_transitividade_verbo=None, P2_FP_tonicidade=None,
        P2_FP_morfologia_do_pronome=None, P2_FP_reflexivo=None, P2_FP_adjetivo_epiteto=None,
        P2_FP_adjetivo_classificador=None, P2_FP_genero_adjetivo=None, P2_FP_numero_adjetivo=None, P2_FP_contracao=None,

        # P3
        P3_dissoc_ente_nucleo=None, P3_tem_qualificador=None, P3_tipo_qualificador=None,
        P3_indice_preposicao_qualif=None, P3_determinacao_especificidade_beta=None, P3_orientacao_beta=None,
        P3_genero_beta=None, P3_numero_beta=None, P3_morfologia_do_pronome_beta=None,
        P3_determinacao_especificidade_alpha=None, P3_orientacao_alpha=None, P3_genero_alpha=None, P3_numero_alpha=None,
        P3_morfologia_do_pronome_alpha=None, P3_pessoa_da_interlocucao_possuidor=None, P3_numero_obj_possuido=None,
        P3_genero_obj_possuido=None, P3_pessoa_da_interlocucao_proximidade=None, P3_funcao_numerativo=None,
        P3_cardinal=None, P3_genero=None, P3_tipo_precisa=None, P3_tipo_real_card=None, P3_milharExtenso=None,
        P3_centenaExtenso=None, P3_dezenaExtenso=None, P3_unidadeExtenso=None, P3_numIndefinido=None,
        P3_tipo_de_ente=None, P3_tipo_de_nao_consciente=None, P3_tipo_de_nao_consciente_material=None,
        P3_tipo_de_nao_consciente_semiotico=None, P3_classe_palavra_ente=None, P3_substantivo_lematizado=None,
        P3_numero=None, P3_tipo_feminino_ao=None, P3_tipo_masc_ao=None, P3_acent_tonica=None, P3_nome_proprio=None,
        P3_pessoa_da_interlocucao=None, P3_transitividade_verbo=None, P3_tonicidade=None, P3_morfologia_do_pronome=None,
        P3_reflexivo=None, P3_adjetivo_epiteto=None, P3_adjetivo_classificador=None, P3_genero_adjetivo=None,
        P3_numero_adjetivo=None, P3_contracao=None,
        ##PARTICIPANTE P3 REALIZADOS POR FP
        P3_FP_indice_preposicao_frase=None, P3_FP_dissoc_ente_nucleo=None, P3_FP_tem_qualificador=None,
        P3_FP_tipo_qualificador=None, P3_FP_indice_preposicao_qualif=None, P3_FP_determinacao_especificidade_beta=None,
        P3_FP_orientacao_beta=None, P3_FP_genero_beta=None, P3_FP_numero_beta=None,
        P3_FP_morfologia_do_pronome_beta=None, P3_FP_determinacao_especificidade_alpha=None,
        P3_FP_orientacao_alpha=None, P3_FP_genero_alpha=None, P3_FP_numero_alpha=None,
        P3_FP_morfologia_do_pronome_alpha=None, P3_FP_pessoa_da_interlocucao_possuidor=None,
        P3_FP_numero_obj_possuido=None, P3_FP_genero_obj_possuido=None, P3_FP_pessoa_da_interlocucao_proximidade=None,
        P3_FP_funcao_numerativo=None, P3_FP_cardinal=None, P3_FP_genero=None, P3_FP_tipo_precisa=None,
        P3_FP_tipo_real_card=None, P3_FP_milharExtenso=None, P3_FP_centenaExtenso=None, P3_FP_dezenaExtenso=None,
        P3_FP_unidadeExtenso=None, P3_FP_numIndefinido=None, P3_FP_tipo_de_ente=None, P3_FP_tipo_de_nao_consciente=None,
        P3_FP_tipo_de_nao_consciente_material=None, P3_FP_tipo_de_nao_consciente_semiotico=None,
        P3_FP_classe_palavra_ente=None, P3_FP_substantivo_lematizado=None, P3_FP_numero=None,
        P3_FP_tipo_feminino_ao=None, P3_FP_tipo_masc_ao=None, P3_FP_acent_tonica=None, P3_FP_nome_proprio=None,
        P3_FP_pessoa_da_interlocucao=None, P3_FP_transitividade_verbo=None, P3_FP_tonicidade=None,
        P3_FP_morfologia_do_pronome=None, P3_FP_reflexivo=None, P3_FP_adjetivo_epiteto=None,
        P3_FP_adjetivo_classificador=None, P3_FP_genero_adjetivo=None, P3_FP_numero_adjetivo=None, P3_FP_contracao=None,
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
        Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel)
        Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL, T_INTER_tipoRealizacao, T_INTER_tipo_de_adverbio1,
                                              T_INTER_ind1, T_INTER_tipo_de_adverbio2, T_INTER_ind2,
                                              T_INTER_tipo_de_adverbio3, T_INTER_ind3, T_INTER_tipo_de_adverbio4,
                                              T_INTER_ind4, T_INTER_tipo_de_adverbio5, T_INTER_ind5,
                                              T_INTER_FP_indice_preposicao_frase, T_INTER_FP_dissoc_ente_nucleo,
                                              T_INTER_FP_tem_qualificador, T_INTER_FP_tipo_qualificador,
                                              T_INTER_FP_indice_preposicao_qualif,
                                              T_INTER_FP_determinacao_especificidade_beta, T_INTER_FP_orientacao_beta,
                                              T_INTER_FP_genero_beta, T_INTER_FP_numero_beta,
                                              T_INTER_FP_morfologia_do_pronome_beta,
                                              T_INTER_FP_determinacao_especificidade_alpha, T_INTER_FP_orientacao_alpha,
                                              T_INTER_FP_genero_alpha, T_INTER_FP_numero_alpha,
                                              T_INTER_FP_morfologia_do_pronome_alpha,
                                              T_INTER_FP_pessoa_da_interlocucao_possuidor,
                                              T_INTER_FP_numero_obj_possuido, T_INTER_FP_genero_obj_possuido,
                                              T_INTER_FP_pessoa_da_interlocucao_proximidade,
                                              T_INTER_FP_funcao_numerativo, T_INTER_FP_cardinal, T_INTER_FP_genero,
                                              T_INTER_FP_tipo_precisa, T_INTER_FP_tipo_real_card,
                                              T_INTER_FP_milharExtenso, T_INTER_FP_centenaExtenso,
                                              T_INTER_FP_dezenaExtenso, T_INTER_FP_unidadeExtenso,
                                              T_INTER_FP_numIndefinido, T_INTER_FP_tipo_de_ente,
                                              T_INTER_FP_tipo_de_nao_consciente,
                                              T_INTER_FP_tipo_de_nao_consciente_material,
                                              T_INTER_FP_tipo_de_nao_consciente_semiotico,
                                              T_INTER_FP_classe_palavra_ente, T_INTER_FP_substantivo_lematizado,
                                              T_INTER_FP_numero, T_INTER_FP_tipo_feminino_ao, T_INTER_FP_tipo_masc_ao,
                                              T_INTER_FP_acent_tonica, T_INTER_FP_nome_proprio,
                                              T_INTER_FP_pessoa_da_interlocucao, T_INTER_FP_transitividade_verbo,
                                              T_INTER_FP_tonicidade, T_INTER_FP_morfologia_do_pronome,
                                              T_INTER_FP_reflexivo, T_INTER_FP_adjetivo_epiteto,
                                              T_INTER_FP_adjetivo_classificador, T_INTER_FP_genero_adjetivo,
                                              T_INTER_FP_numero_adjetivo, T_INTER_FP_contracao, T_INTER_indiceElemQu,
                                              T_INTER_indicePartModal, T_INTER_nome_proprio)
        Tema_textual = TEMA_TEXTUAL(T_TEXT_temTemaTextual, T_TEXT_tipo_insercao_Cont, T_TEXT_conj_extenso_Cont,
                                    T_TEXT_indiceCont, T_TEXT_tipo_insercao_Conj, T_TEXT_tipo_de_conjuncao_Conj,
                                    T_TEXT_conj_extensoConj, T_TEXT_indiceConj, T_TEXT_tipo_insercao_Rel,
                                    T_TEXT_pron_extenso_Rel, T_TEXT_tipo_de_relativo, T_TEXT_tipo_pronome_relativo,
                                    T_TEXT_generoTemaTextual, T_TEXT_numeroTemaTextual, T_TEXT_indiceRelativo,
                                    T_TEXT_indiceRelativoAdv)

        Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        Polaridade = POLARIDADE(tipo_polaridade)
        Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
                                verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                                padrao_pessoa_morfologia_LEX)
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
        tipo_atribuicao = atribuicao_relacao(indiceAtrib)

        # 	###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
        if Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' and tipo_atribuicao == "sem_atribuição_de_relação":

            ####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
            ## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
            Portador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                    P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                    P1_orientacao_beta, P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                    P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                    P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                    P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                    P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                    P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                    P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                    P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                    P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                    P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                    P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                    P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                    P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                    P1_numero_adjetivo, P1_contracao)

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
                Atributo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                        P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                        P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                        P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                        P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                        P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                        P2_numero_obj_possuido, P2_genero_obj_possuido,
                                        P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal,
                                        P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                        P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                        P2_tipo_de_ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                        P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                        P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao, P2_tipo_masc_ao,
                                        P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                        P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                        P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                        P2_numero_adjetivo, P2_contracao
                                        )


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

                Atributo = adjetivo(P2_adjetivo_epiteto, P2_genero_adjetivo, P2_numero_adjetivo)

            if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                oracao = " ".join((Portador, Polaridade, Processo, Atributo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                oracao = " ".join((Portador, Polaridade, Processo, Atributo + '?'))

        ##### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
        ##Nesse caso, a oracao é Effective (Tem Agente) e pode ser operativa ou receptiva
        # (há a possibilidade de Agente de segunda, terceira.....ordem)
        ##ir verificando no corpus se há diferença de realizacao para cada uma das opções a seguir e também se as ordens dos
        # elementos na oracao mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE realizacao...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA oracao

        elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo':
            Atribuidor = estrutura_gn(P3_dissoc_ente_nucleo, P3_tem_qualificador, P3_tipo_qualificador,
                                      P3_indice_preposicao_qualif, P3_determinacao_especificidade_beta,
                                      P3_orientacao_beta, P3_genero_beta, P3_numero_beta, P3_morfologia_do_pronome_beta,
                                      P3_determinacao_especificidade_alpha, P3_orientacao_alpha, P3_genero_alpha,
                                      P3_numero_alpha, P3_morfologia_do_pronome_alpha,
                                      P3_pessoa_da_interlocucao_possuidor, P3_numero_obj_possuido,
                                      P3_genero_obj_possuido, P3_pessoa_da_interlocucao_proximidade,
                                      P3_funcao_numerativo, P3_cardinal, P3_genero, P3_tipo_precisa, P3_tipo_real_card,
                                      P3_milharExtenso, P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso,
                                      P3_numIndefinido, P3_tipo_de_ente, P3_tipo_de_nao_consciente,
                                      P3_tipo_de_nao_consciente_material, P3_tipo_de_nao_consciente_semiotico,
                                      P3_classe_palavra_ente, P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ao,
                                      P3_tipo_masc_ao, P3_acent_tonica, P3_nome_proprio, P3_pessoa_da_interlocucao,
                                      P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo,
                                      P3_adjetivo_epiteto, P3_adjetivo_classificador, P3_genero_adjetivo,
                                      P3_numero_adjetivo, P3_contracao)
            Portador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                    P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                    P1_orientacao_beta, P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                    P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                    P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                    P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                    P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                    P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                    P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                    P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                    P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                    P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                    P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                    P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                    P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                    P1_numero_adjetivo, P1_contracao
                                    )
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
                    Atributo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                            P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                            P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                            P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                            P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                            P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                            P2_numero_obj_possuido, P2_genero_obj_possuido,
                                            P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal,
                                            P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                            P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                            P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                            P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                            P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                            P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                            P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                            P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                            P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                            P2_contracao
                                            )

                if (
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')):
                    Atributo = adjetivo(P2_adjetivo_epiteto, P2_genero_adjetivo, P2_numero_adjetivo)
                #### VERIFICAR O ATRIBUIDOR---PODE SER QUE O ATRIBUTO TENHA QUE SER REALIZADO POR FRASE PREPOSICIONAL?;
                # grupo nominal com Epíteto como núcleo (checar) por enquanto vou deixar um caso basico; Possivelmente até o P1 possa
                # ser realizado por frase prep: "Eu fiz de você o presidente da cia...."
                if Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito':
                        oracao = " ".join((Atribuidor, Polaridade, Processo, Portador, Atributo + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar':
                        oracao = " ".join((Atribuidor, Polaridade, Processo, Portador, Atributo + '?'))

        elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo':
            ##PARA QUE O Atribuidor seja omitido é só deixar todos os parâmetros default None
            Atribuidor = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                             P3_FP_tem_qualificador,
                                             P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                             P3_FP_determinacao_especificidade_beta,
                                             P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                             P3_FP_morfologia_do_pronome_beta, P3_FP_determinacao_especificidade_alpha,
                                             P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                             P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocucao_possuidor,
                                             P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                             P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                             P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipo_real_card,
                                             P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                             P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                             P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                             P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                             P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                             P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                             P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade,
                                             P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_adjetivo_epiteto,
                                             P3_FP_adjetivo_classificador, P3_FP_genero_adjetivo, P3_FP_numero_adjetivo,
                                             P3_FP_contracao)
            Portador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                    P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                    P1_orientacao_beta, P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                    P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                    P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                    P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                    P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                    P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                    P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                    P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                    P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                    P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                    P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                    P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                    P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                    P1_numero_adjetivo, P1_contracao
                                    )
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
                    Atributo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                            P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                            P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                            P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                            P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                            P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                            P2_numero_obj_possuido, P2_genero_obj_possuido,
                                            P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal,
                                            P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                            P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                            P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                            P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                            P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                            P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                            P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                            P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                            P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                            P2_contracao
                                            )

                if (
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'neutra' and dominio_atribuicao == 'semiótico') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'material') or
                        (
                                especificacao_tipo_modo_relacao == 'qualidade' and fase_atribuicao == 'faseada' and dominio_atribuicao == 'semiótico')):
                    Atributo = adjetivo(P2_adjetivo_epiteto, P2_genero_adjetivo, P2_numero_adjetivo)
            #### VERIFICAR O ATRIBUIDOR---PODE SER QUE O ATRIBUTO TENHA QUE SER REALIZADO POR FRASE PREPOSICIONAL?;
            # grupo nominal com Epíteto como núcleo (checar) por enquanto vou deixar um caso basico; Possivelmente até o P1 possa
            # ser realizado por frase prep: "Eu fiz de você o presidente da cia...."
            if Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito':
                    oracao = " ".join((Portador, Polaridade, Processo, Atributo, Atribuidor + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar':
                    oracao = " ".join((Portador, Polaridade, Processo, Atributo, Atribuidor + '?'))

        ####INTENSIVA_IDENTIFICATIVA
        #
        elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo':
            # 'Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            # a direcionalidade_voz do Símbolo / Valor / Sujeito;  deste tipo_pessoa de oracao determina se é operativa ou receptiva. Selecione a direcionalidade
            # 	Se Simbolo conflui com SUjeito = operativa

            Simbolo = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                   P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta, P1_orientacao_beta,
                                   P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                   P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                   P1_numero_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                   P1_numero_obj_possuido, P1_genero_obj_possuido,
                                   P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                   P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                   P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                   P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                   P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                   P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                   P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo,
                                   P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                   P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo, P1_contracao)
            Valor = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                 P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta, P2_orientacao_beta,
                                 P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                 P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                 P2_numero_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                 P2_numero_obj_possuido, P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                 P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                 P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                 P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                 P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                 P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                 P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                 P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                 P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                 P2_contracao)
            Designador1 = estrutura_gn(P3_dissoc_ente_nucleo, P3_tem_qualificador, P3_tipo_qualificador,
                                       P3_indice_preposicao_qualif, P3_determinacao_especificidade_beta,
                                       P3_orientacao_beta, P3_genero_beta, P3_numero_beta,
                                       P3_morfologia_do_pronome_beta, P3_determinacao_especificidade_alpha,
                                       P3_orientacao_alpha, P3_genero_alpha, P3_numero_alpha,
                                       P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocucao_possuidor,
                                       P3_numero_obj_possuido, P3_genero_obj_possuido,
                                       P3_pessoa_da_interlocucao_proximidade, P3_funcao_numerativo, P3_cardinal,
                                       P3_genero, P3_tipo_precisa, P3_tipo_real_card, P3_milharExtenso,
                                       P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso, P3_numIndefinido,
                                       P3_tipo_de_ente, P3_tipo_de_nao_consciente, P3_tipo_de_nao_consciente_material,
                                       P3_tipo_de_nao_consciente_semiotico, P3_classe_palavra_ente,
                                       P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ao, P3_tipo_masc_ao,
                                       P3_acent_tonica, P3_nome_proprio, P3_pessoa_da_interlocucao,
                                       P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo,
                                       P3_adjetivo_epiteto, P3_adjetivo_classificador, P3_genero_adjetivo,
                                       P3_numero_adjetivo, P3_contracao)

            Designador2 = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                              P3_FP_tem_qualificador,
                                              P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                              P3_FP_determinacao_especificidade_beta,
                                              P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                              P3_FP_morfologia_do_pronome_beta, P3_FP_determinacao_especificidade_alpha,
                                              P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                              P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocucao_possuidor,
                                              P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                              P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                              P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipo_real_card,
                                              P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                              P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                              P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                              P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                              P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                              P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                              P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                              P3_FP_tonicidade,
                                              P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_adjetivo_epiteto,
                                              P3_FP_adjetivo_classificador, P3_FP_genero_adjetivo,
                                              P3_FP_numero_adjetivo,
                                              P3_FP_contracao)
            if ((tipo_atribuicao == 'atribuição_proj_ment_cognitiva') or
                    (tipo_atribuicao == 'atribuição_proj_ment_desiderativa') or
                    (tipo_atribuicao == 'atribuição_proj_verbal') or
                    (tipo_atribuicao == 'atribuição_expan_elaboracao') or
                    (tipo_atribuicao == 'atribuição_expan_intencificação')):

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo, Polaridade, Processo, Valor, Designador2 + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo, Polaridade, Processo, Valor, Designador2 + '?'))


                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, Polaridade, Processo, Simbolo, Valor + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, Polaridade, Processo, Simbolo, Valor + '?'))
            else:
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo, Polaridade, Processo, Valor + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo, Polaridade, Processo, Valor + '?'))

        elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo':
            ##NESTE CASO, confluência de Valor/Sujeito

            Valor = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                 P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta, P1_orientacao_beta,
                                 P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                 P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                 P1_numero_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                 P1_numero_obj_possuido, P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                 P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipo_real_card,
                                 P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso,
                                 P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                 P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                 P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                 P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                 P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                 P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                 P1_contracao)
            Simbolo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                   P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta, P2_orientacao_beta,
                                   P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                   P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                   P2_numero_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                   P2_numero_obj_possuido, P2_genero_obj_possuido,
                                   P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                   P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                   P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                   P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                   P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                   P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao, P2_tipo_masc_ao,
                                   P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao, P2_transitividade_verbo,
                                   P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                   P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo, P2_contracao)
            Designador1 = estrutura_gn(P3_dissoc_ente_nucleo, P3_tem_qualificador, P3_tipo_qualificador,
                                       P3_indice_preposicao_qualif, P3_determinacao_especificidade_beta,
                                       P3_orientacao_beta, P3_genero_beta, P3_numero_beta,
                                       P3_morfologia_do_pronome_beta, P3_determinacao_especificidade_alpha,
                                       P3_orientacao_alpha, P3_genero_alpha, P3_numero_alpha,
                                       P3_morfologia_do_pronome_alpha, P3_pessoa_da_interlocucao_possuidor,
                                       P3_numero_obj_possuido, P3_genero_obj_possuido,
                                       P3_pessoa_da_interlocucao_proximidade, P3_funcao_numerativo, P3_cardinal,
                                       P3_genero, P3_tipo_precisa, P3_tipo_real_card, P3_milharExtenso,
                                       P3_centenaExtenso, P3_dezenaExtenso, P3_unidadeExtenso, P3_numIndefinido,
                                       P3_tipo_de_ente, P3_tipo_de_nao_consciente, P3_tipo_de_nao_consciente_material,
                                       P3_tipo_de_nao_consciente_semiotico, P3_classe_palavra_ente,
                                       P3_substantivo_lematizado, P3_numero, P3_tipo_feminino_ao, P3_tipo_masc_ao,
                                       P3_acent_tonica, P3_nome_proprio, P3_pessoa_da_interlocucao,
                                       P3_transitividade_verbo, P3_tonicidade, P3_morfologia_do_pronome, P3_reflexivo,
                                       P3_adjetivo_epiteto, P3_adjetivo_classificador, P3_genero_adjetivo,
                                       P3_numero_adjetivo, P3_contracao)

            Designador2 = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                              P3_FP_tem_qualificador,
                                              P3_FP_tipo_qualificador, P3_FP_indice_preposicao_qualif,
                                              P3_FP_determinacao_especificidade_beta,
                                              P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                              P3_FP_morfologia_do_pronome_beta, P3_FP_determinacao_especificidade_alpha,
                                              P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                              P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocucao_possuidor,
                                              P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                              P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                              P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipo_real_card,
                                              P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                              P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                              P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                              P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                              P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                              P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                              P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo,
                                              P3_FP_tonicidade,
                                              P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_adjetivo_epiteto,
                                              P3_FP_adjetivo_classificador, P3_FP_genero_adjetivo,
                                              P3_FP_numero_adjetivo,
                                              P3_FP_contracao)

            if ((tipo_atribuicao == 'atribuição_proj_ment_cognitiva') or
                    (tipo_atribuicao == 'atribuição_proj_ment_desiderativa') or
                    (tipo_atribuicao == 'atribuição_proj_verbal') or
                    (tipo_atribuicao == 'atribuição_expan_elaboracao') or
                    (tipo_atribuicao == 'atribuição_expan_intencificação')):

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, Polaridade, Processo, Simbolo, Designador2 + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, Polaridade, Processo, Simbolo, Designador2 + '?'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, Polaridade, Processo, Valor, Simbolo + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Designador1, Polaridade, Processo, Valor, Simbolo + '?'))
            else:
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, Polaridade, Processo, Simbolo + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor, Polaridade, Processo, Simbolo + '.'))

        # 	# POSSESSIVO ATRIBUTIV0

        elif Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance':
            # tipo_atribuicao = choice.Menu(['posse_atributo', 'posse_processo']).ask()

            if tipo_de_realizacao_da_relacao == 'posse_atributo':

                Portador_Posse = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                              P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                              P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                              P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                              P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                              P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                              P1_numero_obj_possuido, P1_genero_obj_possuido,
                                              P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal,
                                              P1_genero, P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso,
                                              P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido,
                                              P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                              P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                              P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero,
                                              P1_tipo_feminino_ao, P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                              P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                              P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                              P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                              P1_contracao)
                Atributo_Possuidor1 = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                   P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                   P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                   P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                   P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                   P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                   P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                   P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                   P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                                   P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso,
                                                   P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                                   P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                                   P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                   P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                   P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                   P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                   P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                   P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                   P2_contracao)
                Atributo_Possuidor2 = frase_preposicional(P2_FP_indice_preposicao_frase, P2_FP_dissoc_ente_nucleo,
                                                          P2_FP_tem_qualificador, P2_FP_tipo_qualificador,
                                                          P2_FP_indice_preposicao_qualif,
                                                          P2_FP_determinacao_especificidade_beta, P2_FP_orientacao_beta,
                                                          P2_FP_genero_beta, P2_FP_numero_beta,
                                                          P2_FP_morfologia_do_pronome_beta,
                                                          P2_FP_determinacao_especificidade_alpha,
                                                          P2_FP_orientacao_alpha, P2_FP_genero_alpha,
                                                          P2_FP_numero_alpha, P2_FP_morfologia_do_pronome_alpha,
                                                          P2_FP_pessoa_da_interlocucao_possuidor,
                                                          P2_FP_numero_obj_possuido, P2_FP_genero_obj_possuido,
                                                          P2_FP_pessoa_da_interlocucao_proximidade,
                                                          P2_FP_funcao_numerativo, P2_FP_cardinal, P2_FP_genero,
                                                          P2_FP_tipo_precisa, P2_FP_tipo_real_card, P2_FP_milharExtenso,
                                                          P2_FP_centenaExtenso, P2_FP_dezenaExtenso,
                                                          P2_FP_unidadeExtenso, P2_FP_numIndefinido, P2_FP_tipo_de_ente,
                                                          P2_FP_tipo_de_nao_consciente,
                                                          P2_FP_tipo_de_nao_consciente_material,
                                                          P2_FP_tipo_de_nao_consciente_semiotico,
                                                          P2_FP_classe_palavra_ente, P2_FP_substantivo_lematizado,
                                                          P2_FP_numero, P2_FP_tipo_feminino_ao, P2_FP_tipo_masc_ao,
                                                          P2_FP_acent_tonica, P2_FP_nome_proprio,
                                                          P2_FP_pessoa_da_interlocucao, P2_FP_transitividade_verbo,
                                                          P2_FP_tonicidade, P2_FP_morfologia_do_pronome,
                                                          P2_FP_reflexivo, P2_FP_adjetivo_epiteto,
                                                          P2_FP_adjetivo_classificador, P2_FP_genero_adjetivo,
                                                          P2_FP_numero_adjetivo, P2_FP_contracao)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join(
                        (Portador_Posse, Polaridade, Processo, Atributo_Possuidor1, Atributo_Possuidor2 + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join(
                        (Portador_Posse, Polaridade, Processo, Atributo_Possuidor1, Atributo_Possuidor2 + '?'))
            # 	Ex.: O piano é meu/O piano é do João
            elif tipo_de_realizacao_da_relacao == 'posse_processo':

                # tipo_atribuicao = choice.Menu(['possuidor_portador', 'possuidor_atributo']).ask()
                if tipo_possuidor == 'possuidor_portador':
                    ##VERBO TER/POSSUIR/
                    Possuidor_Portador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                                      P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                                      P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                                      P1_morfologia_do_pronome_beta,
                                                      P1_determinacao_especificidade_alpha, P1_orientacao_alpha,
                                                      P1_genero_alpha, P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                                      P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido,
                                                      P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                                      P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa,
                                                      P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                                      P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido,
                                                      P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                                      P1_tipo_de_nao_consciente_material,
                                                      P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                                      P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                                      P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                                      P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                                      P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                                      P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                                      P1_contracao)

                    Atributo_Posse = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                                  P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                                  P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                                  P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                                  P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                                  P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                                  P2_numero_obj_possuido, P2_genero_obj_possuido,
                                                  P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo,
                                                  P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                                  P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso,
                                                  P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                                  P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                                  P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                                  P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                                  P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                                  P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                                  P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                                  P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                                  P2_contracao)

                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Possuidor_Portador, Polaridade, Processo, Atributo_Posse + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Possuidor_Portador, Polaridade, Processo, Atributo_Posse + '?'))

                elif tipo_possuidor == 'possuidor_atributo':
                    ####VERBOS PERTENCER A/...

                    Portador_Posse = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                                  P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                                  P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                                  P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                                  P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                                  P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                                  P1_numero_obj_possuido, P1_genero_obj_possuido,
                                                  P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo,
                                                  P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipo_real_card,
                                                  P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso,
                                                  P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                                  P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                                  P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                                  P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                                  P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio,
                                                  P1_pessoa_da_interlocucao, P1_transitividade_verbo, P1_tonicidade,
                                                  P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                                  P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                                                  P1_contracao)

                    Atributo_Possuidor = frase_preposicional(P2_FP_indice_preposicao_frase, P2_FP_dissoc_ente_nucleo,
                                                             P2_FP_tem_qualificador, P2_FP_tipo_qualificador,
                                                             P2_FP_indice_preposicao_qualif,
                                                             P2_FP_determinacao_especificidade_beta,
                                                             P2_FP_orientacao_beta,
                                                             P2_FP_genero_beta, P2_FP_numero_beta,
                                                             P2_FP_morfologia_do_pronome_beta,
                                                             P2_FP_determinacao_especificidade_alpha,
                                                             P2_FP_orientacao_alpha, P2_FP_genero_alpha,
                                                             P2_FP_numero_alpha,
                                                             P2_FP_morfologia_do_pronome_alpha,
                                                             P2_FP_pessoa_da_interlocucao_possuidor,
                                                             P2_FP_numero_obj_possuido, P2_FP_genero_obj_possuido,
                                                             P2_FP_pessoa_da_interlocucao_proximidade,
                                                             P2_FP_funcao_numerativo, P2_FP_cardinal, P2_FP_genero,
                                                             P2_FP_tipo_precisa, P2_FP_tipo_real_card,
                                                             P2_FP_milharExtenso,
                                                             P2_FP_centenaExtenso, P2_FP_dezenaExtenso,
                                                             P2_FP_unidadeExtenso, P2_FP_numIndefinido,
                                                             P2_FP_tipo_de_ente,
                                                             P2_FP_tipo_de_nao_consciente,
                                                             P2_FP_tipo_de_nao_consciente_material,
                                                             P2_FP_tipo_de_nao_consciente_semiotico,
                                                             P2_FP_classe_palavra_ente, P2_FP_substantivo_lematizado,
                                                             P2_FP_numero, P2_FP_tipo_feminino_ao, P2_FP_tipo_masc_ao,
                                                             P2_FP_acent_tonica, P2_FP_nome_proprio,
                                                             P2_FP_pessoa_da_interlocucao, P2_FP_transitividade_verbo,
                                                             P2_FP_tonicidade, P2_FP_morfologia_do_pronome,
                                                             P2_FP_reflexivo,
                                                             P2_FP_adjetivo_epiteto, P2_FP_adjetivo_classificador,
                                                             P2_FP_genero_adjetivo, P2_FP_numero_adjetivo,
                                                             P2_FP_contracao)
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Portador_Posse, Polaridade, Processo, Atributo_Possuidor + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Portador_Posse, Polaridade, Processo, Atributo_Possuidor + '?'))

        # POSSESSIVO IDENTIFICATIVO
        #
        elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_efetivo_operativo':
            # 'Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            # a direcionalidade_voz do Símbolo / Valor / Sujeito;  deste tipo_pessoa de oracao determina se é operativa ou receptiva. Selecione a direcionalidade
            # 	Se Simbolo conflui com SUjeito = operativa
            if tipo_de_realizacao_da_relacao == 'posse_participante' or tipo_de_realizacao_da_relacao == 'posse_processo':
                Simbolo = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                       P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                       P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                       P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                       P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                       P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                       P1_numero_obj_possuido, P1_genero_obj_possuido,
                                       P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal,
                                       P1_genero, P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso,
                                       P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido,
                                       P1_tipo_de_ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                       P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                       P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                       P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                       P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                       P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                       P1_numero_adjetivo, P1_contracao)

                Valor1 = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                      P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                      P2_orientacao_beta, P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                      P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                      P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                      P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                      P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                      P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                      P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                      P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                      P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                      P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                      P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                      P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                      P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                      P2_numero_adjetivo, P2_contracao
                                      )
                Valor2 = frase_preposicional(P2_FP_indice_preposicao_frase, P2_FP_dissoc_ente_nucleo,
                                             P2_FP_tem_qualificador,
                                             P2_FP_tipo_qualificador, P2_FP_indice_preposicao_qualif,
                                             P2_FP_determinacao_especificidade_beta,
                                             P2_FP_orientacao_beta, P2_FP_genero_beta, P2_FP_numero_beta,
                                             P2_FP_morfologia_do_pronome_beta, P2_FP_determinacao_especificidade_alpha,
                                             P2_FP_orientacao_alpha, P2_FP_genero_alpha, P2_FP_numero_alpha,
                                             P2_FP_morfologia_do_pronome_alpha, P2_FP_pessoa_da_interlocucao_possuidor,
                                             P2_FP_numero_obj_possuido, P2_FP_genero_obj_possuido,
                                             P2_FP_pessoa_da_interlocucao_proximidade, P2_FP_funcao_numerativo,
                                             P2_FP_cardinal, P2_FP_genero, P2_FP_tipo_precisa, P2_FP_tipo_real_card,
                                             P2_FP_milharExtenso, P2_FP_centenaExtenso, P2_FP_dezenaExtenso,
                                             P2_FP_unidadeExtenso, P2_FP_numIndefinido, P2_FP_tipo_de_ente,
                                             P2_FP_tipo_de_nao_consciente, P2_FP_tipo_de_nao_consciente_material,
                                             P2_FP_tipo_de_nao_consciente_semiotico, P2_FP_classe_palavra_ente,
                                             P2_FP_substantivo_lematizado, P2_FP_numero, P2_FP_tipo_feminino_ao,
                                             P2_FP_tipo_masc_ao, P2_FP_acent_tonica, P2_FP_nome_proprio,
                                             P2_FP_pessoa_da_interlocucao, P2_FP_transitividade_verbo, P2_FP_tonicidade,
                                             P2_FP_morfologia_do_pronome, P2_FP_reflexivo, P2_FP_adjetivo_epiteto,
                                             P2_FP_adjetivo_classificador, P2_FP_genero_adjetivo, P2_FP_numero_adjetivo,
                                             P2_FP_contracao)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo, Polaridade, Processo, Valor1, Valor2 + '.'))

                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo, Polaridade, Processo, Valor1, Valor2 + '.'))
        # Ex.:'posse_participante'---O piano é seu/O piano é da moça?/posse_processo---***João possui o piano

        elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_efetivo_receptivo':
            Valor1 = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                  P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta, P2_orientacao_beta,
                                  P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                  P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                  P2_numero_alpha, P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                  P2_numero_obj_possuido, P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                  P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                  P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                  P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                  P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                  P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                  P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                  P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                  P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                  P2_numero_adjetivo, P2_contracao
                                  )
            Valor2 = frase_preposicional(P2_FP_indice_preposicao_frase, P2_FP_dissoc_ente_nucleo,
                                         P2_FP_tem_qualificador, P2_FP_tipo_qualificador,
                                         P2_FP_indice_preposicao_qualif, P2_FP_determinacao_especificidade_beta,
                                         P2_FP_orientacao_beta, P2_FP_genero_beta, P2_FP_numero_beta,
                                         P2_FP_morfologia_do_pronome_beta, P2_FP_determinacao_especificidade_alpha,
                                         P2_FP_orientacao_alpha, P2_FP_genero_alpha, P2_FP_numero_alpha,
                                         P2_FP_morfologia_do_pronome_alpha, P2_FP_pessoa_da_interlocucao_possuidor,
                                         P2_FP_numero_obj_possuido, P2_FP_genero_obj_possuido,
                                         P2_FP_pessoa_da_interlocucao_proximidade, P2_FP_funcao_numerativo,
                                         P2_FP_cardinal, P2_FP_genero, P2_FP_tipo_precisa, P2_FP_tipo_real_card,
                                         P2_FP_milharExtenso, P2_FP_centenaExtenso, P2_FP_dezenaExtenso,
                                         P2_FP_unidadeExtenso, P2_FP_numIndefinido, P2_FP_tipo_de_ente,
                                         P2_FP_tipo_de_nao_consciente, P2_FP_tipo_de_nao_consciente_material,
                                         P2_FP_tipo_de_nao_consciente_semiotico, P2_FP_classe_palavra_ente,
                                         P2_FP_substantivo_lematizado, P2_FP_numero, P2_FP_tipo_feminino_ao,
                                         P2_FP_tipo_masc_ao, P2_FP_acent_tonica, P2_FP_nome_proprio,
                                         P2_FP_pessoa_da_interlocucao, P2_FP_transitividade_verbo, P2_FP_tonicidade,
                                         P2_FP_morfologia_do_pronome, P2_FP_reflexivo, P2_FP_adjetivo_epiteto,
                                         P2_FP_adjetivo_classificador, P2_FP_genero_adjetivo, P2_FP_numero_adjetivo,
                                         P2_FP_contracao)
            Simbolo = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                   P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta, P1_orientacao_beta,
                                   P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                   P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                   P1_numero_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                   P1_numero_obj_possuido, P1_genero_obj_possuido,
                                   P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                   P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                   P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                   P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                   P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                   P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                   P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao, P1_transitividade_verbo,
                                   P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo, P1_adjetivo_epiteto,
                                   P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo, P1_contracao)

            if tipo_de_realizacao_da_relacao == 'posse_participante' or tipo_de_realizacao_da_relacao == 'posse_processo':

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, Polaridade, Processo, Simbolo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, Polaridade, Processo, Simbolo + '?'))

        #####RELACIONAL CIRCUNSTANCIAL
        #
        elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance':
            # tipo_de_atributivo = choice.Menu(['atributo_circunstancial', 'processo_circunstancial']).ask()
            Portador = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                    P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                    P1_orientacao_beta, P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                                    P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                                    P1_numero_alpha, P1_morfologia_do_pronome_alpha,
                                    P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido, P1_genero_obj_possuido,
                                    P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal, P1_genero,
                                    P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso,
                                    P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente,
                                    P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                    P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                    P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                    P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                    P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                    P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                    P1_numero_adjetivo, P1_contracao
                                    )

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
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Portador, Polaridade, Processo, Atributo_Circunstancial + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Portador, Polaridade, Processo, Atributo_Circunstancial + '?'))

            elif tipo_de_realizacao_da_relacao == 'processo_circunstancial':

                Atributo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                        P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                        P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                        P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                        P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                        P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                        P2_numero_obj_possuido, P2_genero_obj_possuido,
                                        P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal,
                                        P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                        P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                        P2_tipo_de_ente, P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                        P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                        P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao, P2_tipo_masc_ao,
                                        P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                        P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                        P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                        P2_numero_adjetivo, P2_contracao
                                        )

                # Ex.: O livro retrata a IIGuerra

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Portador, Polaridade, Processo, Atributo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Portador, Polaridade, Processo, Atributo + '?'))


        elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_efetivo_operativo':

            # tipo_de_realizacao_da_relacao = choice.Menu(['participante_circunstancial', 'processo_circunstancial']).ask()

            if tipo_de_realizacao_da_relacao == 'participante_circunstancial' or tipo_de_realizacao_da_relacao == 'posse_processo':
                Simbolo1 = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                        P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                        P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                        P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                        P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                        P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                        P1_numero_obj_possuido, P1_genero_obj_possuido,
                                        P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal,
                                        P1_genero, P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso,
                                        P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido,
                                        P1_tipo_de_ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                        P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                        P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                        P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                        P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                        P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                        P1_numero_adjetivo, P1_contracao)

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
                Valor = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                     P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                     P2_orientacao_beta, P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                     P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                     P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                     P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                     P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                     P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                     P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                     P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                     P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                     P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                     P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                     P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                     P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                     P2_numero_adjetivo, P2_contracao
                                     )
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Simbolo1, Simbolo2, Polaridade, Processo, Valor + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Simbolo1, Simbolo2, Polaridade, Processo, Valor + '?'))

            # Ex.: Amanhã é dia 10

        elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_efetivo_receptivo':

            if tipo_de_realizacao_da_relacao == 'posse_participante' or tipo_de_realizacao_da_relacao == 'posse_processo':
                Simbolo1 = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                        P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                        P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                        P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                        P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                        P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                                        P1_numero_obj_possuido, P1_genero_obj_possuido,
                                        P1_pessoa_da_interlocucao_proximidade, P1_funcao_numerativo, P1_cardinal,
                                        P1_genero, P1_tipo_precisa, P1_tipo_real_card, P1_milharExtenso,
                                        P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso, P1_numIndefinido,
                                        P1_tipo_de_ente, P1_tipo_de_nao_consciente, P1_tipo_de_nao_consciente_material,
                                        P1_tipo_de_nao_consciente_semiotico, P1_classe_palavra_ente,
                                        P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao, P1_tipo_masc_ao,
                                        P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                        P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                        P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                        P1_numero_adjetivo, P1_contracao)

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
                Valor = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                     P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                     P2_orientacao_beta, P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                     P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                     P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                     P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido,
                                     P2_genero_obj_possuido, P2_pessoa_da_interlocucao_proximidade,
                                     P2_funcao_numerativo, P2_cardinal, P2_genero, P2_tipo_precisa, P2_tipo_real_card,
                                     P2_milharExtenso, P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso,
                                     P2_numIndefinido, P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                     P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                     P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao,
                                     P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                     P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                     P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                     P2_numero_adjetivo, P2_contracao
                                     )

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, Polaridade, Processo, Simbolo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Valor1, Valor2, Polaridade, Processo, Simbolo + '?'))
        # Ex.: Dia 10 é amanhã
        return (re.sub(' +', ' ', oracao.strip()).capitalize())
    except:
        return ""


#
# ##ORAÇÃO EXISTENCIAL
#
def oracaoExistencial(
        ##TRANSITIVIDADE
        TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None, indiceAtrib=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, T_INTER_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        T_INTER_tipo_de_adverbio1=None, T_INTER_ind1=None,
        T_INTER_tipo_de_adverbio2=None, T_INTER_ind2=None,
        T_INTER_tipo_de_adverbio3=None, T_INTER_ind3=None,
        T_INTER_tipo_de_adverbio4=None, T_INTER_ind4=None,
        T_INTER_tipo_de_adverbio5=None, T_INTER_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        T_INTER_FP_indice_preposicao_frase=None, T_INTER_FP_dissoc_ente_nucleo=None, T_INTER_FP_tem_qualificador=None,
        T_INTER_FP_tipo_qualificador=None, T_INTER_FP_indice_preposicao_qualif=None,
        T_INTER_FP_determinacao_especificidade_beta=None, T_INTER_FP_orientacao_beta=None, T_INTER_FP_genero_beta=None,
        T_INTER_FP_numero_beta=None, T_INTER_FP_morfologia_do_pronome_beta=None,
        T_INTER_FP_determinacao_especificidade_alpha=None, T_INTER_FP_orientacao_alpha=None,
        T_INTER_FP_genero_alpha=None, T_INTER_FP_numero_alpha=None, T_INTER_FP_morfologia_do_pronome_alpha=None,
        T_INTER_FP_pessoa_da_interlocucao_possuidor=None, T_INTER_FP_numero_obj_possuido=None,
        T_INTER_FP_genero_obj_possuido=None, T_INTER_FP_pessoa_da_interlocucao_proximidade=None,
        T_INTER_FP_funcao_numerativo=None, T_INTER_FP_cardinal=None, T_INTER_FP_genero=None,
        T_INTER_FP_tipo_precisa=None, T_INTER_FP_tipo_real_card=None, T_INTER_FP_milharExtenso=None,
        T_INTER_FP_centenaExtenso=None, T_INTER_FP_dezenaExtenso=None, T_INTER_FP_unidadeExtenso=None,
        T_INTER_FP_numIndefinido=None, T_INTER_FP_tipo_de_ente=None, T_INTER_FP_tipo_de_nao_consciente=None,
        T_INTER_FP_tipo_de_nao_consciente_material=None, T_INTER_FP_tipo_de_nao_consciente_semiotico=None,
        T_INTER_FP_classe_palavra_ente=None, T_INTER_FP_substantivo_lematizado=None, T_INTER_FP_numero=None,
        T_INTER_FP_tipo_feminino_ao=None, T_INTER_FP_tipo_masc_ao=None, T_INTER_FP_acent_tonica=None,
        T_INTER_FP_nome_proprio=None, T_INTER_FP_pessoa_da_interlocucao=None, T_INTER_FP_transitividade_verbo=None,
        T_INTER_FP_tonicidade=None, T_INTER_FP_morfologia_do_pronome=None, T_INTER_FP_reflexivo=None,
        T_INTER_FP_adjetivo_epiteto=None, T_INTER_FP_adjetivo_classificador=None, T_INTER_FP_genero_adjetivo=None,
        T_INTER_FP_numero_adjetivo=None, T_INTER_FP_contracao=None,
        #
        # 		#
        T_INTER_indiceElemQu=None, T_INTER_indicePartModal=None, T_INTER_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        T_TEXT_temTemaTextual='-', T_TEXT_tipo_insercao_Cont="inserção_menu", T_TEXT_conj_extenso_Cont=None,
        T_TEXT_indiceCont=None,
        T_TEXT_tipo_insercao_Conj="inserção_menu", T_TEXT_tipo_de_conjuncao_Conj=None, T_TEXT_conj_extensoConj=None,
        T_TEXT_indiceConj=None,
        T_TEXT_tipo_insercao_Rel='inserção_menu', T_TEXT_pron_extenso_Rel=None, T_TEXT_tipo_de_relativo=None,
        T_TEXT_tipo_pronome_relativo=None, T_TEXT_generoTemaTextual=None, T_TEXT_numeroTemaTextual=None,
        T_TEXT_indiceRelativo=None,
        T_TEXT_indiceRelativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,

        ##Processo
        TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None,
        verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
        padrao_pessoa_morfologia_LEX='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,

        # P1
        P1_dissoc_ente_nucleo=None, P1_tem_qualificador=None, P1_tipo_qualificador=None,
        P1_indice_preposicao_qualif=None, P1_determinacao_especificidade_beta=None, P1_orientacao_beta=None,
        P1_genero_beta=None, P1_numero_beta=None, P1_morfologia_do_pronome_beta=None,
        P1_determinacao_especificidade_alpha=None, P1_orientacao_alpha=None, P1_genero_alpha=None, P1_numero_alpha=None,
        P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocucao_possuidor=None, P1_numero_obj_possuido=None,
        P1_genero_obj_possuido=None, P1_pessoa_da_interlocucao_proximidade=None, P1_funcao_numerativo=None,
        P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipo_real_card=None, P1_milharExtenso=None,
        P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None,
        P1_tipo_de_ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None,
        P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_ente=None, P1_substantivo_lematizado=None,
        P1_numero=None, P1_tipo_feminino_ao=None, P1_tipo_masc_ao=None, P1_acent_tonica=None, P1_nome_proprio=None,
        P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None,
        P1_reflexivo=None, P1_adjetivo_epiteto=None, P1_adjetivo_classificador=None, P1_genero_adjetivo=None,
        P1_numero_adjetivo=None, P1_contracao=None,
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
        Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel)
        Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL, T_INTER_tipoRealizacao, T_INTER_tipo_de_adverbio1,
                                              T_INTER_ind1, T_INTER_tipo_de_adverbio2, T_INTER_ind2,
                                              T_INTER_tipo_de_adverbio3, T_INTER_ind3, T_INTER_tipo_de_adverbio4,
                                              T_INTER_ind4, T_INTER_tipo_de_adverbio5, T_INTER_ind5,
                                              T_INTER_FP_indice_preposicao_frase, T_INTER_FP_dissoc_ente_nucleo,
                                              T_INTER_FP_tem_qualificador, T_INTER_FP_tipo_qualificador,
                                              T_INTER_FP_indice_preposicao_qualif,
                                              T_INTER_FP_determinacao_especificidade_beta, T_INTER_FP_orientacao_beta,
                                              T_INTER_FP_genero_beta, T_INTER_FP_numero_beta,
                                              T_INTER_FP_morfologia_do_pronome_beta,
                                              T_INTER_FP_determinacao_especificidade_alpha, T_INTER_FP_orientacao_alpha,
                                              T_INTER_FP_genero_alpha, T_INTER_FP_numero_alpha,
                                              T_INTER_FP_morfologia_do_pronome_alpha,
                                              T_INTER_FP_pessoa_da_interlocucao_possuidor,
                                              T_INTER_FP_numero_obj_possuido, T_INTER_FP_genero_obj_possuido,
                                              T_INTER_FP_pessoa_da_interlocucao_proximidade,
                                              T_INTER_FP_funcao_numerativo, T_INTER_FP_cardinal, T_INTER_FP_genero,
                                              T_INTER_FP_tipo_precisa, T_INTER_FP_tipo_real_card,
                                              T_INTER_FP_milharExtenso, T_INTER_FP_centenaExtenso,
                                              T_INTER_FP_dezenaExtenso, T_INTER_FP_unidadeExtenso,
                                              T_INTER_FP_numIndefinido, T_INTER_FP_tipo_de_ente,
                                              T_INTER_FP_tipo_de_nao_consciente,
                                              T_INTER_FP_tipo_de_nao_consciente_material,
                                              T_INTER_FP_tipo_de_nao_consciente_semiotico,
                                              T_INTER_FP_classe_palavra_ente, T_INTER_FP_substantivo_lematizado,
                                              T_INTER_FP_numero, T_INTER_FP_tipo_feminino_ao, T_INTER_FP_tipo_masc_ao,
                                              T_INTER_FP_acent_tonica, T_INTER_FP_nome_proprio,
                                              T_INTER_FP_pessoa_da_interlocucao, T_INTER_FP_transitividade_verbo,
                                              T_INTER_FP_tonicidade, T_INTER_FP_morfologia_do_pronome,
                                              T_INTER_FP_reflexivo, T_INTER_FP_adjetivo_epiteto,
                                              T_INTER_FP_adjetivo_classificador, T_INTER_FP_genero_adjetivo,
                                              T_INTER_FP_numero_adjetivo, T_INTER_FP_contracao, T_INTER_indiceElemQu,
                                              T_INTER_indicePartModal, T_INTER_nome_proprio)
        Tema_textual = TEMA_TEXTUAL(T_TEXT_temTemaTextual, T_TEXT_tipo_insercao_Cont, T_TEXT_conj_extenso_Cont,
                                    T_TEXT_indiceCont, T_TEXT_tipo_insercao_Conj, T_TEXT_tipo_de_conjuncao_Conj,
                                    T_TEXT_conj_extensoConj, T_TEXT_indiceConj, T_TEXT_tipo_insercao_Rel,
                                    T_TEXT_pron_extenso_Rel, T_TEXT_tipo_de_relativo, T_TEXT_tipo_pronome_relativo,
                                    T_TEXT_generoTemaTextual, T_TEXT_numeroTemaTextual, T_TEXT_indiceRelativo,
                                    T_TEXT_indiceRelativoAdv)
        Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        Polaridade = POLARIDADE(tipo_polaridade)
        Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
                                verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                                padrao_pessoa_morfologia_LEX)
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

        if Transitividade == 'PR_Existencial_AG_médio_sem_alcance':
            Existente = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                                     P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta,
                                     P1_orientacao_beta, P1_genero_beta, P1_numero_beta,
                                     P1_morfologia_do_pronome_beta, P1_determinacao_especificidade_alpha,
                                     P1_orientacao_alpha, P1_genero_alpha, P1_numero_alpha,
                                     P1_morfologia_do_pronome_alpha,
                                     P1_pessoa_da_interlocucao_possuidor, P1_numero_obj_possuido,
                                     P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                                     P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa,
                                     P1_tipo_real_card, P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso,
                                     P1_unidadeExtenso, P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                                     P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                                     P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                                     P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                                     P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                                     P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo,
                                     P1_numero_adjetivo, P1_contracao)
            if (
                    Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA'):
                oracao = " ".join(Polaridade, Processo, Existente + '.')
            elif (
                    Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'):
                oracao = " ".join((Polaridade, Processo, Existente + '?'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Polaridade, Existente, Processo + '.'))
            elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                oracao = " ".join((Polaridade, Existente, Processo + '?'))
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
        TIPO_DE_PROCESSO=None, indiceMat=None, indiceAgen=None, indiceRel=None,
        # MODO
        RESPONSABILIDADE=None, PRESSUPOSICAO_DO_SUJEITO=None, TIPO_MODO=None,
        # TEMA INTERPESSOAL
        TIPO_TEMA_INTERPESSOAL=None, T_INTER_tipoRealizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        T_INTER_tipo_de_adverbio1=None, T_INTER_ind1=None,
        T_INTER_tipo_de_adverbio2=None, T_INTER_ind2=None,
        T_INTER_tipo_de_adverbio3=None, T_INTER_ind3=None,
        T_INTER_tipo_de_adverbio4=None, T_INTER_ind4=None,
        T_INTER_tipo_de_adverbio5=None, T_INTER_ind5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
        T_INTER_FP_indice_preposicao_frase=None, T_INTER_FP_dissoc_ente_nucleo=None, T_INTER_FP_tem_qualificador=None,
        T_INTER_FP_tipo_qualificador=None, T_INTER_FP_indice_preposicao_qualif=None,
        T_INTER_FP_determinacao_especificidade_beta=None, T_INTER_FP_orientacao_beta=None, T_INTER_FP_genero_beta=None,
        T_INTER_FP_numero_beta=None, T_INTER_FP_morfologia_do_pronome_beta=None,
        T_INTER_FP_determinacao_especificidade_alpha=None, T_INTER_FP_orientacao_alpha=None,
        T_INTER_FP_genero_alpha=None, T_INTER_FP_numero_alpha=None, T_INTER_FP_morfologia_do_pronome_alpha=None,
        T_INTER_FP_pessoa_da_interlocucao_possuidor=None, T_INTER_FP_numero_obj_possuido=None,
        T_INTER_FP_genero_obj_possuido=None, T_INTER_FP_pessoa_da_interlocucao_proximidade=None,
        T_INTER_FP_funcao_numerativo=None, T_INTER_FP_cardinal=None, T_INTER_FP_genero=None,
        T_INTER_FP_tipo_precisa=None, T_INTER_FP_tipo_real_card=None, T_INTER_FP_milharExtenso=None,
        T_INTER_FP_centenaExtenso=None, T_INTER_FP_dezenaExtenso=None, T_INTER_FP_unidadeExtenso=None,
        T_INTER_FP_numIndefinido=None, T_INTER_FP_tipo_de_ente=None, T_INTER_FP_tipo_de_nao_consciente=None,
        T_INTER_FP_tipo_de_nao_consciente_material=None, T_INTER_FP_tipo_de_nao_consciente_semiotico=None,
        T_INTER_FP_classe_palavra_ente=None, T_INTER_FP_substantivo_lematizado=None, T_INTER_FP_numero=None,
        T_INTER_FP_tipo_feminino_ao=None, T_INTER_FP_tipo_masc_ao=None, T_INTER_FP_acent_tonica=None,
        T_INTER_FP_nome_proprio=None, T_INTER_FP_pessoa_da_interlocucao=None, T_INTER_FP_transitividade_verbo=None,
        T_INTER_FP_tonicidade=None, T_INTER_FP_morfologia_do_pronome=None, T_INTER_FP_reflexivo=None,
        T_INTER_FP_adjetivo_epiteto=None, T_INTER_FP_adjetivo_classificador=None, T_INTER_FP_genero_adjetivo=None,
        T_INTER_FP_numero_adjetivo=None, T_INTER_FP_contracao=None,
        #
        # 		#
        T_INTER_indiceElemQu=None, T_INTER_indicePartModal=None, T_INTER_nome_proprio=None,
        #
        # 	#TEMA TEXTUAL
        T_TEXT_temTemaTextual='-', T_TEXT_tipo_insercao_Cont="inserção_menu", T_TEXT_conj_extenso_Cont=None,
        T_TEXT_indiceCont=None,
        T_TEXT_tipo_insercao_Conj="inserção_menu", T_TEXT_tipo_de_conjuncao_Conj=None, T_TEXT_conj_extensoConj=None,
        T_TEXT_indiceConj=None,
        T_TEXT_tipo_insercao_Rel='inserção_menu', T_TEXT_pron_extenso_Rel=None, T_TEXT_tipo_de_relativo=None,
        T_TEXT_tipo_pronome_relativo=None, T_TEXT_generoTemaTextual=None, T_TEXT_numeroTemaTextual=None,
        T_TEXT_indiceRelativo=None,
        T_TEXT_indiceRelativoAdv=None,
        # TEMA IDEACIONAL
        ORIENTACAO_MODAL=None, ORIENTACAO_TRANSITIVA=None, SELECAO_TEMATICA=None, TEMA_DEFAULT=None,
        TEMA_DEFAULT_indicativo=None, TEMA_IDENTIFICATIVO=None, TEMA_ANGULO=None, TEMA_ELEMENTAL=None,
        TEMA_PROEMINENTE=None,
        ##PARAMETROS da oracao VERBAL
        MODO_DO_DIZENTE=None, TIPO_SEMIOTICIDADE=None, TIPO_PROJECAO=None, RECEPTIVIDADE=None,
        ##Processo
        TIPO_DE_EXPERIENCIA_GV=None, AGENCIA=None, TIPO_DE_EXPERIENCIA_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, OI_numero_1=None, genero_1=None, OI_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, TIPO_DE_EXPERIENCIA_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, OI_numero_2=None, genero_2=None, OI_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, TIPO_DE_EXPERIENCIA_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, OI_numero_3=None, genero_3=None, OI_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, TIPO_DE_EXPERIENCIA_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, OI_numero_4=None, genero_4=None, OI_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, TIPO_DE_EXPERIENCIA_LEX=None, funcao_no_grupo_verbal_POS_FINAL=None,
        verbo_LEX=None, tipo_de_orientacao_LEX=None, OI_numero_LEX=None, genero_LEX=None, OI_tipo_de_pessoa_LEX=None,
        padrao_pessoa_morfologia_LEX='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        # P1
        P1_dissoc_ente_nucleo=None, P1_tem_qualificador=None, P1_tipo_qualificador=None,
        P1_indice_preposicao_qualif=None, P1_determinacao_especificidade_beta=None, P1_orientacao_beta=None,
        P1_genero_beta=None, P1_numero_beta=None, P1_morfologia_do_pronome_beta=None,
        P1_determinacao_especificidade_alpha=None, P1_orientacao_alpha=None, P1_genero_alpha=None, P1_numero_alpha=None,
        P1_morfologia_do_pronome_alpha=None, P1_pessoa_da_interlocucao_possuidor=None, P1_numero_obj_possuido=None,
        P1_genero_obj_possuido=None, P1_pessoa_da_interlocucao_proximidade=None, P1_funcao_numerativo=None,
        P1_cardinal=None, P1_genero=None, P1_tipo_precisa=None, P1_tipo_real_card=None, P1_milharExtenso=None,
        P1_centenaExtenso=None, P1_dezenaExtenso=None, P1_unidadeExtenso=None, P1_numIndefinido=None,
        P1_tipo_de_ente=None, P1_tipo_de_nao_consciente=None, P1_tipo_de_nao_consciente_material=None,
        P1_tipo_de_nao_consciente_semiotico=None, P1_classe_palavra_ente=None, P1_substantivo_lematizado=None,
        P1_numero=None, P1_tipo_feminino_ao=None, P1_tipo_masc_ao=None, P1_acent_tonica=None, P1_nome_proprio=None,
        P1_pessoa_da_interlocucao=None, P1_transitividade_verbo=None, P1_tonicidade=None, P1_morfologia_do_pronome=None,
        P1_reflexivo=None, P1_adjetivo_epiteto=None, P1_adjetivo_classificador=None, P1_genero_adjetivo=None,
        P1_numero_adjetivo=None, P1_contracao=None,
        ## P1 REALIZADOS POR FP
        P1_FP_indice_preposicao_frase=None, P1_FP_dissoc_ente_nucleo=None, P1_FP_tem_qualificador=None,
        P1_FP_tipo_qualificador=None, P1_FP_indice_preposicao_qualif=None, P1_FP_determinacao_especificidade_beta=None,
        P1_FP_orientacao_beta=None, P1_FP_genero_beta=None, P1_FP_numero_beta=None,
        P1_FP_morfologia_do_pronome_beta=None, P1_FP_determinacao_especificidade_alpha=None,
        P1_FP_orientacao_alpha=None, P1_FP_genero_alpha=None, P1_FP_numero_alpha=None,
        P1_FP_morfologia_do_pronome_alpha=None, P1_FP_pessoa_da_interlocucao_possuidor=None,
        P1_FP_numero_obj_possuido=None, P1_FP_genero_obj_possuido=None, P1_FP_pessoa_da_interlocucao_proximidade=None,
        P1_FP_funcao_numerativo=None, P1_FP_cardinal=None, P1_FP_genero=None, P1_FP_tipo_precisa=None,
        P1_FP_tipo_real_card=None, P1_FP_milharExtenso=None, P1_FP_centenaExtenso=None, P1_FP_dezenaExtenso=None,
        P1_FP_unidadeExtenso=None, P1_FP_numIndefinido=None, P1_FP_tipo_de_ente=None, P1_FP_tipo_de_nao_consciente=None,
        P1_FP_tipo_de_nao_consciente_material=None, P1_FP_tipo_de_nao_consciente_semiotico=None,
        P1_FP_classe_palavra_ente=None, P1_FP_substantivo_lematizado=None, P1_FP_numero=None,
        P1_FP_tipo_feminino_ao=None, P1_FP_tipo_masc_ao=None, P1_FP_acent_tonica=None, P1_FP_nome_proprio=None,
        P1_FP_pessoa_da_interlocucao=None, P1_FP_transitividade_verbo=None, P1_FP_tonicidade=None,
        P1_FP_morfologia_do_pronome=None, P1_FP_reflexivo=None, P1_FP_adjetivo_epiteto=None,
        P1_FP_adjetivo_classificador=None, P1_FP_genero_adjetivo=None, P1_FP_numero_adjetivo=None, P1_FP_contracao=None,
        # P2
        P2_dissoc_ente_nucleo=None, P2_tem_qualificador=None, P2_tipo_qualificador=None,
        P2_indice_preposicao_qualif=None, P2_determinacao_especificidade_beta=None, P2_orientacao_beta=None,
        P2_genero_beta=None, P2_numero_beta=None, P2_morfologia_do_pronome_beta=None,
        P2_determinacao_especificidade_alpha=None, P2_orientacao_alpha=None, P2_genero_alpha=None, P2_numero_alpha=None,
        P2_morfologia_do_pronome_alpha=None, P2_pessoa_da_interlocucao_possuidor=None, P2_numero_obj_possuido=None,
        P2_genero_obj_possuido=None, P2_pessoa_da_interlocucao_proximidade=None, P2_funcao_numerativo=None,
        P2_cardinal=None, P2_genero=None, P2_tipo_precisa=None, P2_tipo_real_card=None, P2_milharExtenso=None,
        P2_centenaExtenso=None, P2_dezenaExtenso=None, P2_unidadeExtenso=None, P2_numIndefinido=None,
        P2_tipo_de_ente=None, P2_tipo_de_nao_consciente=None, P2_tipo_de_nao_consciente_material=None,
        P2_tipo_de_nao_consciente_semiotico=None, P2_classe_palavra_ente=None, P2_substantivo_lematizado=None,
        P2_numero=None, P2_tipo_feminino_ao=None, P2_tipo_masc_ao=None, P2_acent_tonica=None, P2_nome_proprio=None,
        P2_pessoa_da_interlocucao=None, P2_transitividade_verbo=None, P2_tonicidade=None, P2_morfologia_do_pronome=None,
        P2_reflexivo=None, P2_adjetivo_epiteto=None, P2_adjetivo_classificador=None, P2_genero_adjetivo=None,
        P2_numero_adjetivo=None, P2_contracao=None,
        # P2 FRASE PREP
        P2_FP_indice_preposicao_frase=None, P2_FP_dissoc_ente_nucleo=None, P2_FP_tem_qualificador=None,
        P2_FP_tipo_qualificador=None, P2_FP_indice_preposicao_qualif=None, P2_FP_determinacao_especificidade_beta=None,
        P2_FP_orientacao_beta=None, P2_FP_genero_beta=None, P2_FP_numero_beta=None,
        P2_FP_morfologia_do_pronome_beta=None, P2_FP_determinacao_especificidade_alpha=None,
        P2_FP_orientacao_alpha=None, P2_FP_genero_alpha=None, P2_FP_numero_alpha=None,
        P2_FP_morfologia_do_pronome_alpha=None, P2_FP_pessoa_da_interlocucao_possuidor=None,
        P2_FP_numero_obj_possuido=None, P2_FP_genero_obj_possuido=None, P2_FP_pessoa_da_interlocucao_proximidade=None,
        P2_FP_funcao_numerativo=None, P2_FP_cardinal=None, P2_FP_genero=None, P2_FP_tipo_precisa=None,
        P2_FP_tipo_real_card=None, P2_FP_milharExtenso=None, P2_FP_centenaExtenso=None, P2_FP_dezenaExtenso=None,
        P2_FP_unidadeExtenso=None, P2_FP_numIndefinido=None, P2_FP_tipo_de_ente=None, P2_FP_tipo_de_nao_consciente=None,
        P2_FP_tipo_de_nao_consciente_material=None, P2_FP_tipo_de_nao_consciente_semiotico=None,
        P2_FP_classe_palavra_ente=None, P2_FP_substantivo_lematizado=None, P2_FP_numero=None,
        P2_FP_tipo_feminino_ao=None, P2_FP_tipo_masc_ao=None, P2_FP_acent_tonica=None, P2_FP_nome_proprio=None,
        P2_FP_pessoa_da_interlocucao=None, P2_FP_transitividade_verbo=None, P2_FP_tonicidade=None,
        P2_FP_morfologia_do_pronome=None, P2_FP_reflexivo=None, P2_FP_adjetivo_epiteto=None,
        P2_FP_adjetivo_classificador=None, P2_FP_genero_adjetivo=None, P2_FP_numero_adjetivo=None, P2_FP_contracao=None,
        # P3
        P3_dissoc_ente_nucleo=None, P3_tem_qualificador=None, P3_tipo_qualificador=None,
        P3_indice_preposicao_qualif=None, P3_determinacao_especificidade_beta=None, P3_orientacao_beta=None,
        P3_genero_beta=None, P3_numero_beta=None, P3_morfologia_do_pronome_beta=None,
        P3_determinacao_especificidade_alpha=None, P3_orientacao_alpha=None, P3_genero_alpha=None, P3_numero_alpha=None,
        P3_morfologia_do_pronome_alpha=None, P3_pessoa_da_interlocucao_possuidor=None, P3_numero_obj_possuido=None,
        P3_genero_obj_possuido=None, P3_pessoa_da_interlocucao_proximidade=None, P3_funcao_numerativo=None,
        P3_cardinal=None, P3_genero=None, P3_tipo_precisa=None, P3_tipo_real_card=None, P3_milharExtenso=None,
        P3_centenaExtenso=None, P3_dezenaExtenso=None, P3_unidadeExtenso=None, P3_numIndefinido=None,
        P3_tipo_de_ente=None, P3_tipo_de_nao_consciente=None, P3_tipo_de_nao_consciente_material=None,
        P3_tipo_de_nao_consciente_semiotico=None, P3_classe_palavra_ente=None, P3_substantivo_lematizado=None,
        P3_numero=None, P3_tipo_feminino_ao=None, P3_tipo_masc_ao=None, P3_acent_tonica=None, P3_nome_proprio=None,
        P3_pessoa_da_interlocucao=None, P3_transitividade_verbo=None, P3_tonicidade=None, P3_morfologia_do_pronome=None,
        P3_reflexivo=None, P3_adjetivo_epiteto=None, P3_adjetivo_classificador=None, P3_genero_adjetivo=None,
        P3_numero_adjetivo=None, P3_contracao=None,
        ## P3 REALIZADOS POR FP
        P3_FP_indice_preposicao_frase=None, P3_FP_dissoc_ente_nucleo=None, P3_FP_tem_qualificador=None,
        P3_FP_tipo_qualificador=None, P3_FP_indice_preposicao_qualif=None, P3_FP_determinacao_especificidade_beta=None,
        P3_FP_orientacao_beta=None, P3_FP_genero_beta=None, P3_FP_numero_beta=None,
        P3_FP_morfologia_do_pronome_beta=None, P3_FP_determinacao_especificidade_alpha=None,
        P3_FP_orientacao_alpha=None, P3_FP_genero_alpha=None, P3_FP_numero_alpha=None,
        P3_FP_morfologia_do_pronome_alpha=None, P3_FP_pessoa_da_interlocucao_possuidor=None,
        P3_FP_numero_obj_possuido=None, P3_FP_genero_obj_possuido=None, P3_FP_pessoa_da_interlocucao_proximidade=None,
        P3_FP_funcao_numerativo=None, P3_FP_cardinal=None, P3_FP_genero=None, P3_FP_tipo_precisa=None,
        P3_FP_tipo_real_card=None, P3_FP_milharExtenso=None, P3_FP_centenaExtenso=None, P3_FP_dezenaExtenso=None,
        P3_FP_unidadeExtenso=None, P3_FP_numIndefinido=None, P3_FP_tipo_de_ente=None, P3_FP_tipo_de_nao_consciente=None,
        P3_FP_tipo_de_nao_consciente_material=None, P3_FP_tipo_de_nao_consciente_semiotico=None,
        P3_FP_classe_palavra_ente=None, P3_FP_substantivo_lematizado=None, P3_FP_numero=None,
        P3_FP_tipo_feminino_ao=None, P3_FP_tipo_masc_ao=None, P3_FP_acent_tonica=None, P3_FP_nome_proprio=None,
        P3_FP_pessoa_da_interlocucao=None, P3_FP_transitividade_verbo=None, P3_FP_tonicidade=None,
        P3_FP_morfologia_do_pronome=None, P3_FP_reflexivo=None, P3_FP_adjetivo_epiteto=None,
        P3_FP_adjetivo_classificador=None, P3_FP_genero_adjetivo=None, P3_FP_numero_adjetivo=None, P3_FP_contracao=None,
):
    try:
        Transitividade = TRANSITIVIDADE(TIPO_DE_PROCESSO, indiceMat, indiceAgen, indiceRel)
        Modo = MODO(RESPONSABILIDADE, PRESSUPOSICAO_DO_SUJEITO, TIPO_MODO)
        Tema_interpessoal = TEMA_INTERPESSOAL(TIPO_TEMA_INTERPESSOAL, T_INTER_tipoRealizacao, T_INTER_tipo_de_adverbio1,
                                              T_INTER_ind1, T_INTER_tipo_de_adverbio2, T_INTER_ind2,
                                              T_INTER_tipo_de_adverbio3, T_INTER_ind3, T_INTER_tipo_de_adverbio4,
                                              T_INTER_ind4, T_INTER_tipo_de_adverbio5, T_INTER_ind5,
                                              T_INTER_FP_indice_preposicao_frase, T_INTER_FP_dissoc_ente_nucleo,
                                              T_INTER_FP_tem_qualificador, T_INTER_FP_tipo_qualificador,
                                              T_INTER_FP_indice_preposicao_qualif,
                                              T_INTER_FP_determinacao_especificidade_beta, T_INTER_FP_orientacao_beta,
                                              T_INTER_FP_genero_beta, T_INTER_FP_numero_beta,
                                              T_INTER_FP_morfologia_do_pronome_beta,
                                              T_INTER_FP_determinacao_especificidade_alpha, T_INTER_FP_orientacao_alpha,
                                              T_INTER_FP_genero_alpha, T_INTER_FP_numero_alpha,
                                              T_INTER_FP_morfologia_do_pronome_alpha,
                                              T_INTER_FP_pessoa_da_interlocucao_possuidor,
                                              T_INTER_FP_numero_obj_possuido, T_INTER_FP_genero_obj_possuido,
                                              T_INTER_FP_pessoa_da_interlocucao_proximidade,
                                              T_INTER_FP_funcao_numerativo, T_INTER_FP_cardinal, T_INTER_FP_genero,
                                              T_INTER_FP_tipo_precisa, T_INTER_FP_tipo_real_card,
                                              T_INTER_FP_milharExtenso, T_INTER_FP_centenaExtenso,
                                              T_INTER_FP_dezenaExtenso, T_INTER_FP_unidadeExtenso,
                                              T_INTER_FP_numIndefinido, T_INTER_FP_tipo_de_ente,
                                              T_INTER_FP_tipo_de_nao_consciente,
                                              T_INTER_FP_tipo_de_nao_consciente_material,
                                              T_INTER_FP_tipo_de_nao_consciente_semiotico,
                                              T_INTER_FP_classe_palavra_ente, T_INTER_FP_substantivo_lematizado,
                                              T_INTER_FP_numero, T_INTER_FP_tipo_feminino_ao, T_INTER_FP_tipo_masc_ao,
                                              T_INTER_FP_acent_tonica, T_INTER_FP_nome_proprio,
                                              T_INTER_FP_pessoa_da_interlocucao, T_INTER_FP_transitividade_verbo,
                                              T_INTER_FP_tonicidade, T_INTER_FP_morfologia_do_pronome,
                                              T_INTER_FP_reflexivo, T_INTER_FP_adjetivo_epiteto,
                                              T_INTER_FP_adjetivo_classificador, T_INTER_FP_genero_adjetivo,
                                              T_INTER_FP_numero_adjetivo, T_INTER_FP_contracao, T_INTER_indiceElemQu,
                                              T_INTER_indicePartModal, T_INTER_nome_proprio)
        Tema_textual = TEMA_TEXTUAL(T_TEXT_temTemaTextual, T_TEXT_tipo_insercao_Cont, T_TEXT_conj_extenso_Cont,
                                    T_TEXT_indiceCont, T_TEXT_tipo_insercao_Conj, T_TEXT_tipo_de_conjuncao_Conj,
                                    T_TEXT_conj_extensoConj, T_TEXT_indiceConj, T_TEXT_tipo_insercao_Rel,
                                    T_TEXT_pron_extenso_Rel, T_TEXT_tipo_de_relativo, T_TEXT_tipo_pronome_relativo,
                                    T_TEXT_generoTemaTextual, T_TEXT_numeroTemaTextual, T_TEXT_indiceRelativo,
                                    T_TEXT_indiceRelativoAdv)
        Tema_id = TEMA_IDEACIONAL(ORIENTACAO_MODAL, ORIENTACAO_TRANSITIVA, SELECAO_TEMATICA, TEMA_DEFAULT,
                                  TEMA_DEFAULT_indicativo, TEMA_IDENTIFICATIVO, TEMA_ANGULO, TEMA_ELEMENTAL,
                                  TEMA_PROEMINENTE)
        Polaridade = POLARIDADE(tipo_polaridade)
        Processo = grupo_verbal(TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1,
                                verbo_1, tipo_de_orientacao_1, OI_numero_1, genero_1, OI_tipo_de_pessoa_1,
                                padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2, verbo_2,
                                tipo_de_orientacao_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
                                padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
                                tipo_de_orientacao_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
                                padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
                                tipo_de_orientacao_4, OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
                                padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
                                verbo_LEX, tipo_de_orientacao_LEX, OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
                                padrao_pessoa_morfologia_LEX)
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
        Dizente = estrutura_gn(P1_dissoc_ente_nucleo, P1_tem_qualificador, P1_tipo_qualificador,
                               P1_indice_preposicao_qualif, P1_determinacao_especificidade_beta, P1_orientacao_beta,
                               P1_genero_beta, P1_numero_beta, P1_morfologia_do_pronome_beta,
                               P1_determinacao_especificidade_alpha, P1_orientacao_alpha, P1_genero_alpha,
                               P1_numero_alpha, P1_morfologia_do_pronome_alpha, P1_pessoa_da_interlocucao_possuidor,
                               P1_numero_obj_possuido, P1_genero_obj_possuido, P1_pessoa_da_interlocucao_proximidade,
                               P1_funcao_numerativo, P1_cardinal, P1_genero, P1_tipo_precisa, P1_tipo_real_card,
                               P1_milharExtenso, P1_centenaExtenso, P1_dezenaExtenso, P1_unidadeExtenso,
                               P1_numIndefinido, P1_tipo_de_ente, P1_tipo_de_nao_consciente,
                               P1_tipo_de_nao_consciente_material, P1_tipo_de_nao_consciente_semiotico,
                               P1_classe_palavra_ente, P1_substantivo_lematizado, P1_numero, P1_tipo_feminino_ao,
                               P1_tipo_masc_ao, P1_acent_tonica, P1_nome_proprio, P1_pessoa_da_interlocucao,
                               P1_transitividade_verbo, P1_tonicidade, P1_morfologia_do_pronome, P1_reflexivo,
                               P1_adjetivo_epiteto, P1_adjetivo_classificador, P1_genero_adjetivo, P1_numero_adjetivo,
                               P1_contracao)
        if RECEPTIVIDADE == '+receptor':
            Receptor = frase_preposicional(P3_FP_indice_preposicao_frase, P3_FP_dissoc_ente_nucleo,
                                           P3_FP_tem_qualificador, P3_FP_tipo_qualificador,
                                           P3_FP_indice_preposicao_qualif, P3_FP_determinacao_especificidade_beta,
                                           P3_FP_orientacao_beta, P3_FP_genero_beta, P3_FP_numero_beta,
                                           P3_FP_morfologia_do_pronome_beta, P3_FP_determinacao_especificidade_alpha,
                                           P3_FP_orientacao_alpha, P3_FP_genero_alpha, P3_FP_numero_alpha,
                                           P3_FP_morfologia_do_pronome_alpha, P3_FP_pessoa_da_interlocucao_possuidor,
                                           P3_FP_numero_obj_possuido, P3_FP_genero_obj_possuido,
                                           P3_FP_pessoa_da_interlocucao_proximidade, P3_FP_funcao_numerativo,
                                           P3_FP_cardinal, P3_FP_genero, P3_FP_tipo_precisa, P3_FP_tipo_real_card,
                                           P3_FP_milharExtenso, P3_FP_centenaExtenso, P3_FP_dezenaExtenso,
                                           P3_FP_unidadeExtenso, P3_FP_numIndefinido, P3_FP_tipo_de_ente,
                                           P3_FP_tipo_de_nao_consciente, P3_FP_tipo_de_nao_consciente_material,
                                           P3_FP_tipo_de_nao_consciente_semiotico, P3_FP_classe_palavra_ente,
                                           P3_FP_substantivo_lematizado, P3_FP_numero, P3_FP_tipo_feminino_ao,
                                           P3_FP_tipo_masc_ao, P3_FP_acent_tonica, P3_FP_nome_proprio,
                                           P3_FP_pessoa_da_interlocucao, P3_FP_transitividade_verbo, P3_FP_tonicidade,
                                           P3_FP_morfologia_do_pronome, P3_FP_reflexivo, P3_FP_adjetivo_epiteto,
                                           P3_FP_adjetivo_classificador, P3_FP_genero_adjetivo, P3_FP_numero_adjetivo,
                                           P3_FP_contracao)
        else:
            Receptor = ''

        if Transitividade == 'PR_Verbal_AG_médio_sem_alcance':
            if MODO_DO_DIZENTE == 'atividade_fala' or MODO_DO_DIZENTE == 'semioticidade':

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Dizente, Polaridade, Processo, Receptor + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Dizente, Polaridade, Processo, Receptor + '?'))
            # Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...
            elif MODO_DO_DIZENTE == 'semioticidade':
                TIPO_SEMIOTICIDADE == 'não_projeção_-verbiagem'
                if TIPO_SEMIOTICIDADE == 'não_projeção_-verbiagem':
                    # print('Não-projeção + médio sem alcance = -verbiagem')
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Dizente, Polaridade, Processo, Receptor + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Dizente, Polaridade, Processo, Receptor + '?'))

        elif Transitividade == 'PR_Verbal_AG_médio_com_alcance':
            MODO_DO_DIZENTE = 'semioticidade'
            if MODO_DO_DIZENTE == 'semioticidade':
                if TIPO_SEMIOTICIDADE == 'projeção':
                    # REVISAR: inserir parametros para a projetada.
                    oracao_projetada = oraçãoProjetada()
                    if TIPO_PROJECAO == 'citativa':

                        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                            oracao = " ".join((Dizente, Polaridade, Processo, Receptor, '"' + oracao_projetada + '".'))
                        elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                            oracao = " ".join((Dizente, Polaridade, Processo, Receptor, '"' + oracao_projetada + '"?'))

                    # Ex.: Eu disse a ele "Eu comi o bolo".

                    elif TIPO_PROJECAO == 'relativa':
                        if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                            oracao = " ".join(
                                (Dizente, Polaridade, Processo, Receptor, 'que "' + oracao_projetada + '".'))
                        elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                            oracao = " ".join(
                                (Dizente, Polaridade, Processo, Receptor, 'que "' + oracao_projetada + '"?'))

                    # Ex.: Eu disse a ele que eu havia comido o bolo.

                elif TIPO_SEMIOTICIDADE == 'não_projeção_+verbiagem':
                    Verbiagem = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                             P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                             P2_orientacao_beta, P2_genero_beta, P2_numero_beta,
                                             P2_morfologia_do_pronome_beta, P2_determinacao_especificidade_alpha,
                                             P2_orientacao_alpha, P2_genero_alpha, P2_numero_alpha,
                                             P2_morfologia_do_pronome_alpha, P2_pessoa_da_interlocucao_possuidor,
                                             P2_numero_obj_possuido, P2_genero_obj_possuido,
                                             P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal,
                                             P2_genero, P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso,
                                             P2_centenaExtenso, P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido,
                                             P2_tipo_de_ente, P2_tipo_de_nao_consciente,
                                             P2_tipo_de_nao_consciente_material, P2_tipo_de_nao_consciente_semiotico,
                                             P2_classe_palavra_ente, P2_substantivo_lematizado, P2_numero,
                                             P2_tipo_feminino_ao, P2_tipo_masc_ao, P2_acent_tonica, P2_nome_proprio,
                                             P2_pessoa_da_interlocucao, P2_transitividade_verbo, P2_tonicidade,
                                             P2_morfologia_do_pronome, P2_reflexivo, P2_adjetivo_epiteto,
                                             P2_adjetivo_classificador, P2_genero_adjetivo, P2_numero_adjetivo,
                                             P2_contracao)
                    if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                        oracao = " ".join((Dizente, Polaridade, Processo, Verbiagem, Receptor + '.'))
                    elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                        oracao = " ".join((Dizente, Polaridade, Processo, Verbiagem, Receptor + '?'))


        elif Transitividade == 'PR_Verbal_AG_efetivo_operativo':
            if MODO_DO_DIZENTE == 'atividade_alvo':
                Alvo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                    P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                    P2_orientacao_beta, P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                    P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                    P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                    P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido, P2_genero_obj_possuido,
                                    P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                    P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                    P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                    P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                    P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                    P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao, P2_tipo_masc_ao,
                                    P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                    P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                    P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                    P2_numero_adjetivo, P2_contracao)
                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
                    oracao = " ".join((Dizente, Polaridade, Processo, Alvo + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
                    oracao = " ".join((Dizente, Polaridade, Processo, Alvo + '?'))
            # Ex.: Eu acusei o padeiro

        elif Transitividade == 'PR_Verbal_AG_efetivo_receptivo':
            if MODO_DO_DIZENTE == 'atividade_alvo':
                Dizente = frase_preposicional(P1_FP_indice_preposicao_frase, P1_FP_dissoc_ente_nucleo,
                                              P1_FP_tem_qualificador, P1_FP_tipo_qualificador,
                                              P1_FP_indice_preposicao_qualif, P1_FP_determinacao_especificidade_beta,
                                              P1_FP_orientacao_beta, P1_FP_genero_beta, P1_FP_numero_beta,
                                              P1_FP_morfologia_do_pronome_beta, P1_FP_determinacao_especificidade_alpha,
                                              P1_FP_orientacao_alpha, P1_FP_genero_alpha, P1_FP_numero_alpha,
                                              P1_FP_morfologia_do_pronome_alpha, P1_FP_pessoa_da_interlocucao_possuidor,
                                              P1_FP_numero_obj_possuido, P1_FP_genero_obj_possuido,
                                              P1_FP_pessoa_da_interlocucao_proximidade, P1_FP_funcao_numerativo,
                                              P1_FP_cardinal, P1_FP_genero, P1_FP_tipo_precisa, P1_FP_tipo_real_card,
                                              P1_FP_milharExtenso, P1_FP_centenaExtenso, P1_FP_dezenaExtenso,
                                              P1_FP_unidadeExtenso, P1_FP_numIndefinido, P1_FP_tipo_de_ente,
                                              P1_FP_tipo_de_nao_consciente, P1_FP_tipo_de_nao_consciente_material,
                                              P1_FP_tipo_de_nao_consciente_semiotico, P1_FP_classe_palavra_ente,
                                              P1_FP_substantivo_lematizado, P1_FP_numero, P1_FP_tipo_feminino_ao,
                                              P1_FP_tipo_masc_ao, P1_FP_acent_tonica, P1_FP_nome_proprio,
                                              P1_FP_pessoa_da_interlocucao, P1_FP_transitividade_verbo,
                                              P1_FP_tonicidade, P1_FP_morfologia_do_pronome, P1_FP_reflexivo,
                                              P1_FP_adjetivo_epiteto, P1_FP_adjetivo_classificador,
                                              P1_FP_genero_adjetivo, P1_FP_numero_adjetivo, P1_FP_contracao)
                Alvo = estrutura_gn(P2_dissoc_ente_nucleo, P2_tem_qualificador, P2_tipo_qualificador,
                                    P2_indice_preposicao_qualif, P2_determinacao_especificidade_beta,
                                    P2_orientacao_beta, P2_genero_beta, P2_numero_beta, P2_morfologia_do_pronome_beta,
                                    P2_determinacao_especificidade_alpha, P2_orientacao_alpha, P2_genero_alpha,
                                    P2_numero_alpha, P2_morfologia_do_pronome_alpha,
                                    P2_pessoa_da_interlocucao_possuidor, P2_numero_obj_possuido, P2_genero_obj_possuido,
                                    P2_pessoa_da_interlocucao_proximidade, P2_funcao_numerativo, P2_cardinal, P2_genero,
                                    P2_tipo_precisa, P2_tipo_real_card, P2_milharExtenso, P2_centenaExtenso,
                                    P2_dezenaExtenso, P2_unidadeExtenso, P2_numIndefinido, P2_tipo_de_ente,
                                    P2_tipo_de_nao_consciente, P2_tipo_de_nao_consciente_material,
                                    P2_tipo_de_nao_consciente_semiotico, P2_classe_palavra_ente,
                                    P2_substantivo_lematizado, P2_numero, P2_tipo_feminino_ao, P2_tipo_masc_ao,
                                    P2_acent_tonica, P2_nome_proprio, P2_pessoa_da_interlocucao,
                                    P2_transitividade_verbo, P2_tonicidade, P2_morfologia_do_pronome, P2_reflexivo,
                                    P2_adjetivo_epiteto, P2_adjetivo_classificador, P2_genero_adjetivo,
                                    P2_numero_adjetivo, P2_contracao)

                if Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Alvo, Polaridade, Processo, Dizente + '.'))
                elif Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_proeminente_intensivo_relativo_papel_transitivo_nuclear_participante':
                    oracao = " ".join((Alvo, Polaridade, Processo, Dizente + '?'))

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
