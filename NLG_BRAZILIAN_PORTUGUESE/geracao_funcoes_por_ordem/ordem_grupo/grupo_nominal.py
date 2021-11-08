from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.frase_preposicional import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_nominais import *

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.frase_preposicional import *

# # ####DÊIXIS DO GN
# #


def estrutura_logica_deixis(indice: int = None) -> str:
    """

    Ex.:

    >>> estrutura_logica_deixis(2)
    'α(Dêitico_prox)'

    :param indice:
    :return: estrutura lógica da deixis
    """
    estrutura_logica_det_deixis = ''
    opcoes = ["α(Dêitico_ñ_seletivo_específico)",  # ex.: O,A
              "α(Dêitico_ñ_seletivo_ñ_específico)",  # ex.: Um,uns
              "α(Dêitico_prox)",  # Este
              "α(Dêitico_pess)",  # Meu
              "β(Dêitico_prox)^α(Dêitico_pess)",  # ex.: Este meu
              "β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)",  # ex.: O meu
              "β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)"]  # ex.: Um meu
    num = [x for x in range(len(opcoes))]
    estrutura_logica_det_deixis = dict(zip(num, opcoes))
    return estrutura_logica_det_deixis[indice]


def deitico_nao_seletivo_especifico(determinacao_espeficifidade=None, orientacao=None, numero=None, genero=None):
    """
    Ex.:

    >>> deitico_nao_seletivo_especifico('específico', 'NA','plural', 'feminino')
    'as'

    :param determinacao_espeficifidade:
     ['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
         'genérico(contável)']
    :param orientacao:
    ['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param numero:
    ['singular', 'plural']
    :param genero:
    ['masculino', 'feminino']
    :return: deitico não seletivo específico
    """

    determinante = ''
    if determinacao_espeficifidade == 'específico' and orientacao == 'NA':

        if numero == 'plural' and genero == 'masculino':
            determinante = 'os'
        elif numero == 'plural' and genero == 'feminino':
            determinante = 'as'
        elif numero == 'singular' and genero == 'masculino':
            determinante = 'o'
        elif numero == 'singular' and genero == 'feminino':
            determinante = 'a'

    return determinante


def deitico_nao_seletivo_nao_especifico(determinacao_espeficifidade, orientacao, numero, genero):
    """
    Ex.:

    >>> deitico_nao_seletivo_nao_especifico('não_específico','NA','plural','masculino')
    'uns'

    :param determinacao_espeficifidade:
     ['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
         'genérico(contável)']
    :param orientacao:
    ['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param numero:
    ['singular', 'plural']
    :param genero:
    ['masculino', 'feminino']

    :return: deitico_nao_seletivo_nao_especifico
    """

    determinante = ''
    if determinacao_espeficifidade == 'não_específico' and orientacao == 'NA':
        if numero == 'singular' and genero == 'masculino':
            determinante = 'um'
        elif numero == 'plural' and genero == 'masculino':
            determinante = 'uns'
        elif numero == 'singular' and genero == 'feminino':
            determinante = 'uma'
        elif numero == 'plural' and genero == 'feminino':
            determinante = 'umas'
    return determinante


def deitico_prox(determinacao_espeficifidade, orientacao, pessoa_da_interlocucao_proximidade, numero, genero):
    """
    Ex.:
    >>> deitico_pess('específico','orientação_específica_pessoa','2p','plural','feminino','padrão')
    'vossas'

    >>> deitico_prox('específico','orientação_específica_proximidade','próximo_ao_não_interlocutor','plural','masculino')
    'aqueles'
    :param determinacao_espeficifidade: ['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']
    :param orientacao:['NA', 'orientação_específica_pessoa','orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param pessoa_da_interlocucao_proximidade:['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']
    :param numero:['singular', 'plural']
    :param genero:['masculino', 'feminino']
    :return: deitico_prox
    """
    determinante = ""
    if determinacao_espeficifidade == 'específico' and orientacao == 'orientação_específica_proximidade':

        if pessoa_da_interlocucao_proximidade == 'próximo_ao_falante':

            if numero == 'singular' and genero == 'masculino':
                determinante = 'este'
            elif numero == 'plural' and genero == 'masculino':
                determinante = 'estes'
            elif numero == 'singular' and genero == 'feminino':
                determinante = 'esta'
            elif numero == 'plural' and genero == 'feminino':
                determinante = 'estas'

        elif pessoa_da_interlocucao_proximidade == 'próximo_ao_ouvinte':

            if numero == 'singular' and genero == 'masculino':
                determinante = 'esse'
            elif numero == 'plural' and genero == 'masculino':
                determinante = 'esses'
            elif numero == 'singular' and genero == 'feminino':
                determinante = 'essa'
            elif numero == 'plural' and genero == 'feminino':
                determinante = 'essas'

        elif pessoa_da_interlocucao_proximidade == 'próximo_ao_não_interlocutor':

            if numero == 'singular' and genero == 'masculino':
                determinante = 'aquele'
            elif numero == 'plural' and genero == 'masculino':
                determinante = 'aqueles'
            elif numero == 'singular' and genero == 'feminino':
                determinante = 'aquela'
            elif numero == 'plural' and genero == 'feminino':
                determinante = 'aquelas'

    return determinante


def deitico_pess(determinacao_espeficifidade, orientacao, pessoa_da_interlocucao_possuidor,
                 numero_obj_possuido, genero_obj_possuido, morfologia_do_pronome='morfologia_terceira_pessoa'):
    """
    Ex.:

    :param determinacao_espeficifidade:['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']
    :param orientacao:['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param pessoa_da_interlocucao_possuidor:['1s', '2s', '3s', '1p', '2p', '3p']
    :param numero_obj_possuido: ['singular', 'plural']
    :param genero_obj_possuido:['masculino', 'feminino']
    :param morfologia_do_pronome: padrão', 'morfologia_terceira_pessoa']
    :return: deitico_pess
    """

    determinante = ''
    if determinacao_espeficifidade == 'específico' and orientacao == 'orientação_específica_pessoa':

        if pessoa_da_interlocucao_possuidor == '1s':

            if numero_obj_possuido == 'singular' and genero_obj_possuido == 'masculino':
                determinante = 'meu'
            elif pessoa_da_interlocucao_possuidor == '1s' and numero_obj_possuido == 'plural' \
                    and genero_obj_possuido == 'masculino':
                determinante = 'meus'
            elif pessoa_da_interlocucao_possuidor == '1s' and numero_obj_possuido == 'singular' \
                    and genero_obj_possuido == 'feminino':
                determinante = 'minha'
            elif pessoa_da_interlocucao_possuidor == '1s' and numero_obj_possuido == 'plural' \
                    and genero_obj_possuido == 'feminino':
                determinante = 'minhas'

        elif pessoa_da_interlocucao_possuidor == '2s':

            if numero_obj_possuido == 'singular' and genero_obj_possuido == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'teu'
                else:
                    determinante = 'seu'

            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'teus'
                else:
                    determinante = 'seus'

            elif numero_obj_possuido == 'singular' and genero_obj_possuido == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'tua'
                else:
                    determinante = 'sua'

            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'tuas'
                else:
                    determinante = 'suas'

        elif (pessoa_da_interlocucao_possuidor == '3s' or
              pessoa_da_interlocucao_possuidor == '3p'):

            if numero_obj_possuido == 'singular' and genero_obj_possuido == 'masculino':
                determinante = 'seu'

            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'masculino':
                determinante = 'seus'

            elif numero_obj_possuido == 'singular' and genero_obj_possuido == 'feminino':
                determinante = 'sua'

            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'feminino':
                determinante = 'suas'

        elif pessoa_da_interlocucao_possuidor == '1p':

            if numero_obj_possuido == 'singular' and genero_obj_possuido == 'masculino':
                determinante = 'nosso'
            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'masculino':
                determinante = 'nossos'
            elif numero_obj_possuido == 'singular' and genero_obj_possuido == 'feminino':
                determinante = 'nossa'
            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'feminino':
                determinante = 'nossas'

        elif pessoa_da_interlocucao_possuidor == '2p':

            if numero_obj_possuido == 'singular' and genero_obj_possuido == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vosso'
                else:
                    determinante = 'seu'

            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossos'
                else:
                    determinante = 'seus'

            elif numero_obj_possuido == 'singular' and genero_obj_possuido == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossa'
                else:
                    determinante = 'sua'

            elif numero_obj_possuido == 'plural' and genero_obj_possuido == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossas'
                else:
                    determinante = 'suas'

    return determinante


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

def deixis_geral(determinacao_especificidade_beta=None, orientacao_beta=None,
                 genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
                 determinacao_especificidade_alpha=None,
                 orientacao_alpha=None, genero_alpha=None, numero_alpha=None, morfologia_do_pronome_alpha=None,
                 pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
                 genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None):
    """

    Ex.:

    >>> deixis_geral(determinacao_especificidade_beta='específico', orientacao_beta='NA',
    ... genero_beta='masculino', numero_beta='singular', morfologia_do_pronome_beta='padrão',
    ...determinacao_especificidade_alpha='específico',
    ... orientacao_alpha='orientação_específica_pessoa', genero_alpha='masculino', numero_alpha='singular',
    ...morfologia_do_pronome_alpha='padrão',
    ...pessoa_da_interlocucao_possuidor='1s', numero_obj_possuido='singular',
    ... genero_obj_possuido='masculino', pessoa_da_interlocucao_proximidade=None)

    'o meu'

    >>> deixis_geral(None,None, None,None,None,'específico','orientação_específica_proximidade', 'masculino','singular',
             ...'morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
    'este'

    :param determinacao_especificidade_beta:['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']
    :param orientacao_beta:['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param pessoa_da_interlocucao_possuidor:['1s', '2s', '3s', '1p', '2p', '3p']
    :param numero_obj_possuido: ['singular', 'plural']
    :param genero_obj_possuido:['masculino', 'feminino']
    :param morfologia_do_pronome_beta: padrão', 'morfologia_terceira_pessoa']
    :param determinacao_especificidade_alpha:['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']
    :param orientacao_alpha:['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param pessoa_da_interlocucao_possuidor:['1s', '2s', '3s', '1p', '2p', '3p']
    :param numero_obj_possuido: ['singular', 'plural']
    :param genero_obj_possuido:['masculino', 'feminino']
    :param morfologia_do_pronome_alpha: padrão', 'morfologia_terceira_pessoa']
     :param numero_beta:['singular', 'plural']
    :param genero_beta:['masculino', 'feminino']
    :param numero_alpha:['singular', 'plural']
    :param genero_alpha:['masculino', 'feminino']
    :param genero_beta: ['masculino', 'feminino']
    :param pessoa_da_interlocucao_proximidade:['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']


    :return:
    """
    try:
        if determinacao_especificidade_alpha == 'específico':
            if orientacao_alpha == 'orientação_específica_proximidade':
                alpha = deitico_prox(determinacao_especificidade_alpha, orientacao_alpha,
                                     pessoa_da_interlocucao_proximidade, numero_alpha, genero_alpha)
            elif orientacao_alpha == 'orientação_específica_pessoa':
                alpha = deitico_pess(determinacao_especificidade_alpha, orientacao_alpha,
                                     pessoa_da_interlocucao_possuidor,
                                     numero_obj_possuido, genero_obj_possuido, morfologia_do_pronome_alpha)
            else:
                alpha = deitico_nao_seletivo_especifico(determinacao_especificidade_alpha,
                                                        orientacao_alpha, numero_alpha, genero_alpha)
        elif determinacao_especificidade_alpha == 'não_específico':
            alpha = deitico_nao_seletivo_nao_especifico(determinacao_especificidade_alpha,
                                                        orientacao_alpha, numero_alpha, genero_alpha)
        else:
            alpha = ''

        if determinacao_especificidade_beta == 'específico':

            if orientacao_beta == 'orientação_específica_proximidade':
                beta = deitico_prox(determinacao_especificidade_beta, orientacao_beta,
                                    pessoa_da_interlocucao_proximidade,
                                    numero_beta, genero_beta)
            elif orientacao_beta == 'orientação_específica_pessoa':
                beta = deitico_pess(determinacao_especificidade_beta, orientacao_beta,
                                    pessoa_da_interlocucao_possuidor,
                                    numero_obj_possuido, genero_obj_possuido, morfologia_do_pronome_beta)
            else:
                beta = deitico_nao_seletivo_especifico(determinacao_especificidade_beta, orientacao_beta, numero_beta,
                                                       genero_beta)
        elif determinacao_especificidade_beta == 'não_específico':
            beta = deitico_nao_seletivo_nao_especifico(determinacao_especificidade_beta,
                                                       orientacao_beta, numero_beta, genero_beta)

        else:
            beta = ''

        return re.sub(' +', ' ', " ".join((beta, alpha))).strip()
    except ValueError:
        return ''


def ente(tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
         tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
         numero=None, genero=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
         nome_prop=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
         morfologia_do_pronome=None, reflexivo=None):
    """

    #
    # print('Qual tipo_pessoa de material?')
    # tipo_de_nao_consciente_material = choice.Menu(
    # 	).ask()
    #
    # print('Qual a classe de palavra que realiza o Ente?')
    # classe_palavra_ente = choice.Menu(
    # 	['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_obliquo']).ask()
    # print('Qual tipo_pessoa de semiótico?')
    # tipo_de_nao_consciente_semiotico = choice.Menu(
    # 	).ask()

    Ex.:

    >>> ente("consciente",None,None, None,
    ...'pronome_caso_reto', None, "singular",
    ...None,None, None,None,None,"falante",
    ...None,None,None,None)

    'eu'

    >>> ente(tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
    ...tipo_de_nao_consciente_material='animal',
    ...tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
    ...substantivo_lematizado='gato', numero='plural', genero='masculino',
    ...tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_prop=None, pessoa_da_interlocucao=None,
    ...transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None)
    'gatos'

    :param tipo_de_ente: ['consciente', 'não_consciente', 'NA']
    :param tipo_de_nao_consciente: ['material', 'semiótico']
    :param tipo_de_nao_consciente_material: ['animal', 'objeto_material', 'substância_material', 'abstração_material']
    :param tipo_de_nao_consciente_semiotico: ['instituição', 'objeto_semiótico', 'abstração_semiótica']
    :param classe_palavra_ente: ['substantivo_comum','substantivo_próprio','pronome_caso_reto','pronome_caso_oblíquo']
    :param substantivo_lematizado:
    :param numero: 'singular','plural'
    :param genero: 'masculino','feminino'
    :param tipo_feminino_ao:
    :param tipo_masc_ao:
    :param acent_tonica:
    :param nome_prop:
    :param pessoa_da_interlocucao:
    :param transitividade_verbo:
    :param tonicidade:
    :param morfologia_do_pronome:
    :param reflexivo:
    :return: Ente
    """
    ente_realiz = ''
    try:
        if tipo_de_ente == 'NA':
            ente_realiz = ''

        elif tipo_de_ente == 'não_consciente':

            if tipo_de_nao_consciente == 'material':

                if (tipo_de_nao_consciente_material == 'animal' or
                        tipo_de_nao_consciente_material == 'objeto_material' or
                        tipo_de_nao_consciente_material == 'substância_material' or
                        tipo_de_nao_consciente_material == 'abstração_material'):
                    if classe_palavra_ente == 'substantivo_comum':
                        ente_realiz = substantivo_comum(substantivo_lematizado, numero, genero,
                                                        tipo_feminino_ao, tipo_masc_ao, acent_tonica)

                    elif classe_palavra_ente == 'substantivo_próprio':
                        ente_realiz = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
                                                                     numero, morfologia_do_pronome)
                    elif classe_palavra_ente == 'pronome_caso_reto':
                        ente_realiz = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
                                                                     numero, morfologia_do_pronome)
                    elif classe_palavra_ente == 'pronome_caso_oblíquo':
                        ente_realiz = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
                                                                      pessoa_da_interlocucao, numero, genero,
                                                                      morfologia_do_pronome, reflexivo)

            elif tipo_de_nao_consciente == 'semiótico':
                if (tipo_de_nao_consciente_semiotico == 'instituição' or
                        tipo_de_nao_consciente_semiotico == 'objeto_semiótico' or
                        tipo_de_nao_consciente_semiotico == 'abstração_semiótica'):
                    if classe_palavra_ente == 'substantivo_comum':
                        ente_realiz = substantivo_comum(substantivo_lematizado, numero, genero,
                                                        tipo_feminino_ao, tipo_masc_ao, acent_tonica)

                    elif classe_palavra_ente == 'substantivo_próprio':
                        ente_realiz = nome_proprio(nome_prop)
                    elif classe_palavra_ente == 'pronome_caso_reto':
                        ente_realiz = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
                                                                     numero, morfologia_do_pronome)
                    elif classe_palavra_ente == 'pronome_caso_oblíquo':
                        ente_realiz = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
                                                                      pessoa_da_interlocucao, numero, genero,
                                                                      morfologia_do_pronome, reflexivo)

        elif tipo_de_ente == 'consciente':
            if classe_palavra_ente == 'substantivo_comum':
                ente_realiz = substantivo_comum(substantivo_lematizado, numero, genero,
                                                tipo_feminino_ao, tipo_masc_ao, acent_tonica)

            elif classe_palavra_ente == 'pronome_caso_reto':
                ente_realiz = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
                                                             numero, morfologia_do_pronome)

            elif classe_palavra_ente == 'substantivo_próprio':
                ente_realiz = nome_proprio(nome_prop)
            elif classe_palavra_ente == 'pronome_caso_oblíquo':
                ente_realiz = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
                                                              pessoa_da_interlocucao, numero, genero,
                                                              morfologia_do_pronome, reflexivo)
        return ente_realiz
    except ValueError:
        return ''


# ente('não_consciente', 'material', 'objeto_material', None, 'substantivo_comum', 'prédio', 'plural', 'masculino')

# Ente('consciente',None,None, None,'substantivo_comum','menina','singular', 'feminino')
# Ente(tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
#      tipo_de_nao_consciente_material='animal',
#      tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#      substantivo_lematizado='gato', numero='plural', genero='masculino',
#      tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
#      transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None)


# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "singular",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)
# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "plural",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)
# Ente(tipo_de_ente="não_consciente", tipo_de_nao_consciente="semiótico", tipo_de_nao_consciente_material=None,
# 	tipo_de_nao_consciente_semiotico='abstração_semiótica', classe_palavra_ente='pronome_caso_oblíquo',
# 	 substantivo_lematizado=None, numero='plural', genero='masculino', tipo_feminino_ao=None,
# 	 tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,pessoa_da_interlocucao='não_interlocutor',
# 	 transitividade_verbo='indireto', tonicidade='tônico', morfologia_do_pronome='não_padrão', reflexivo=False)

#####ESTRUTURA DO GRUPO NOMINAL:

##
# print('Há Qualificador no gn?')
# tem_qualificador = choice.Menu(['sim', 'NA']).ask()
# realizacao_qualificador = choice.Menu(['frase-preposicional', 'oração']).ask()


def qualificador(indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
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
                 morfologia_do_pronome=None, reflexivo=None,
                 # classificador
                 adjetivo_classificador=None,
                 # epitetos
                 adj_epit_exp_pre=None,
                 adj_epit_int_pre=None,
                 adj_epit_exp_pos=None,
                 adj_epit_int_pos=None,
                 genero_adjetivo=None, numero_adjetivo=None,

                 contracao=None):
    """
    Retorna o qualificador (por enquanto, realizado apenas pela frase preposicional)
    :param genero_subs: 
    :param indice_preposicao_frase:
    :param dissoc_ente_nucleo:
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
    :param tipo_feminino_ao:
    :param tipo_masc_ao:
    :param acent_tonica:
    :param nome_prop_fp:
    :param pessoa_da_interlocucao:
    :param transitividade_verbo:
    :param tonicidade:
    :param morfologia_do_pronome:
    :param reflexivo:
    :param tem_qualificador:
    :param tipo_qualificador:
    :param indice_preposicao_qualif:
    :param adjetivo_epiteto:
    :param adjetivo_classificador:
    :param genero_adjetivo:
    :param numero_adjetivo:
    :param contracao:
    :return:
    """
    qualif = ''
    try:
    
        qualif = frase_preposicional(indice_preposicao_frase, dissoc_ente_nucleo, tem_qualificador,
                                     tipo_qualificador, indice_preposicao_qualif,
                                     determinacao_especificidade_beta, orientacao_beta, genero_beta,
                                     numero_beta,
                                     morfologia_do_pronome_beta, determinacao_especificidade_alpha,
                                     orientacao_alpha,
                                     genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                                     pessoa_da_interlocucao_possuidor, numero_obj_possuido,
                                     genero_obj_possuido,
                                     pessoa_da_interlocucao_proximidade, tipo_numerativo, cardinal,
                                     genero_numerativo,
                                     tipo_de_ente, tipo_de_nao_consciente,
                                     tipo_de_nao_consciente_material,
                                     tipo_de_nao_consciente_semiotico, classe_palavra_ente,
                                     substantivo_lematizado,
                                     numero_subs, genero_subs, tipo_feminino_ao, tipo_masc_ao,
                                     acent_tonica,
                                     nome_prop_fp, pessoa_da_interlocucao, transitividade_verbo,
                                     tonicidade,
                                     morfologia_do_pronome, reflexivo,
                                     # classificador
                                     adjetivo_classificador,
                                     # epitetos
                                     adj_epit_exp_pre,
                                     adj_epit_int_pre,
                                     adj_epit_exp_pos,
                                     adj_epit_int_pos,
                                     genero_adjetivo, numero_adjetivo,

                                     contracao)
        # else:
            # 	Qualificador = "que" + oraçãoProjetada() (em desenvolvimento)
        return re.sub(' +', ' ', qualif).strip()
    except:
        return ''

#
# for i in range(12):
#     print(
#         qualificador(indice_preposicao_frase=i, dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
#                      indice_preposicao_qualif=None, determinacao_especificidade_beta=None, orientacao_beta=None,
#                      genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#                      determinacao_especificidade_alpha='específico', orientacao_alpha='NA', genero_alpha='masculino',
#                      numero_alpha='singular', morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
#                      numero_obj_possuido=None, genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
#                      tipo_numerativo=None, cardinal=None, genero_numerativo='não-binário',
#                      tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
#                      tipo_de_nao_consciente_material='abstração_material', tipo_de_nao_consciente_semiotico=None,
#                      classe_palavra_ente='substantivo_comum', substantivo_lematizado='café', numero_subs='singular',
#                      genero_subs='não-binário',
#                      tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_prop_fp=None,
#                      pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#                      morfologia_do_pronome=None, reflexivo=None, adjetivo_epiteto='alto', adjetivo_classificador=None,
#                      genero_adjetivo='masculino', numero_adjetivo='singular', contracao=None))
#
#
#


def estrutura_gn(dissoc_ente_nucleo=None, tem_qualificador=None,
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
                 morfologia_do_pronome=None, reflexivo=None,
                 # classificador
                 adjetivo_classificador=None,
                 # epitetos
                 adj_epit_exp_pre=None,
                 adj_epit_int_pre=None,
                 adj_epit_exp_pos=None,
                 adj_epit_int_pos=None,
                 genero_adjetivo=None, numero_adjetivo=None,

                 contracao=None):
    """
    Ex.:

    >>> estrutura_gn(dissoc_ente_nucleo=None,tem_qualificador=None,tipo_qualificador=None,
    indice_preposicao_qualif=None,determinacao_especificidade_beta='específico',
    orientacao_beta='NA',genero_beta='masculino',numero_beta=None,morfologia_do_pronome_beta=None,
    determinacao_especificidade_alpha='específico',orientacao_alpha='NA',genero_alpha='masculino',
    numero_alpha='singular',morfologia_do_pronome_alpha=None,pessoa_da_interlocucao_possuidor='1s',
    numero_obj_possuido='singular',genero_obj_possuido='masculino',
    pessoa_da_interlocucao_proximidade='próximo_ao_falante',tipo_numerativo=None,cardinal=None,
    genero_numerativo=None,tipo_de_ente='não_consciente',tipo_de_nao_consciente='material',
    tipo_de_nao_consciente_material='objeto_material',tipo_de_nao_consciente_semiotico=None,
    classe_palavra_ente='substantivo_comum',substantivo_lematizado='piano',numero_subs='singular',
    genero_subs='masculino',tipo_feminino_ao=None,tipo_masc_ao=None,acent_tonica=None,nome_prop_fp=None,
    pessoa_da_interlocucao=None,transitividade_verbo=None,tonicidade=None,morfologia_do_pronome=None,
    reflexivo=None,
    adjetivo_classificador='importado',
    adj_epit_exp_pre=None,
    adj_epit_int_pre='grande',
    adj_epit_exp_pos=None,
    adj_epit_int_pos='bonito',
    genero_adjetivo='não-binário',
    numero_adjetivo='singular',
    contracao=None)
    -> 'o grande piano importado bonito'

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
    :return:
    """
    try:
        if dissoc_ente_nucleo is None:

            determinante = deixis_geral(determinacao_especificidade_beta, orientacao_beta,
                                        genero_beta, numero_beta, morfologia_do_pronome_beta,
                                        determinacao_especificidade_alpha,
                                        orientacao_alpha, genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                                        pessoa_da_interlocucao_possuidor, numero_obj_possuido,
                                        genero_obj_possuido, pessoa_da_interlocucao_proximidade)

            num = numerativo(tipo_numerativo, cardinal, genero_numerativo)

            ente_ = ente(tipo_de_ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                         tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado, numero_subs,
                         genero_subs, tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_prop_fp, pessoa_da_interlocucao,
                         transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo)

            classificador_adj = adjetivo(adjetivo_classificador, genero_adjetivo, numero_adjetivo)

            # (Deit, Num, Epit Inter, Epit Exp, Ente, Classificador, Epit Exp, Epit Inter)
            epiteto_int_pre = adjetivo(adj_epit_int_pre, genero_adjetivo, numero_adjetivo)
            epiteto_exp_pre = adjetivo(adj_epit_exp_pre, genero_adjetivo, numero_adjetivo)

            epiteto_exp_pos = adjetivo(adj_epit_exp_pos, genero_adjetivo, numero_adjetivo)
            epiteto_int_pos = adjetivo(adj_epit_int_pos, genero_adjetivo, numero_adjetivo)

            gn = re.sub(' +', ' ', " ".join((determinante, num, epiteto_int_pre,epiteto_exp_pre,
                                             ente_, classificador_adj, epiteto_exp_pos,epiteto_int_pos))).strip()

        else:

            nucleo_logico = estrutura_gn(dissoc_ente_nucleo, tem_qualificador,
                                         tipo_qualificador, indice_preposicao_qualif,
                                         determinacao_especificidade_beta, orientacao_beta, genero_beta,
                                         numero_beta,
                                         morfologia_do_pronome_beta, determinacao_especificidade_alpha,
                                         orientacao_alpha,
                                         genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                                         pessoa_da_interlocucao_possuidor, numero_obj_possuido,
                                         genero_obj_possuido,
                                         pessoa_da_interlocucao_proximidade, tipo_numerativo, cardinal,
                                         genero_numerativo,
                                         tipo_de_ente, tipo_de_nao_consciente,
                                         tipo_de_nao_consciente_material,
                                         tipo_de_nao_consciente_semiotico, classe_palavra_ente,
                                         substantivo_lematizado,
                                         numero_subs, genero_subs, tipo_feminino_ao, tipo_masc_ao,
                                         acent_tonica,
                                         nome_prop_fp, pessoa_da_interlocucao, transitividade_verbo,
                                         tonicidade,
                                         morfologia_do_pronome, reflexivo,
                                         # classificador
                                         adjetivo_classificador,
                                         # epitetos
                                         adj_epit_exp_pre,
                                         adj_epit_int_pre,
                                         adj_epit_exp_pos,
                                         adj_epit_int_pos,
                                         genero_adjetivo, numero_adjetivo,

                                         contracao)

            qualif = qualificador(indice_preposicao_qualif, dissoc_ente_nucleo, tem_qualificador,
                                  tipo_qualificador, indice_preposicao_qualif,
                                  determinacao_especificidade_beta, orientacao_beta, genero_beta, numero_beta,
                                  morfologia_do_pronome_beta, determinacao_especificidade_alpha, orientacao_alpha,
                                  genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                                  pessoa_da_interlocucao_possuidor, numero_obj_possuido, genero_obj_possuido,
                                  pessoa_da_interlocucao_proximidade, tipo_numerativo, cardinal,
                                  genero_numerativo, tipo_de_ente, tipo_de_nao_consciente,
                                  tipo_de_nao_consciente_material,
                                  tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado,
                                  numero_subs, genero_subs, tipo_feminino_ao, tipo_masc_ao, acent_tonica,
                                  nome_prop_fp, pessoa_da_interlocucao, transitividade_verbo, tonicidade,
                                  morfologia_do_pronome, reflexivo,  # classificador
                                  adjetivo_classificador,
                                  # epitetos
                                  adj_epit_exp_pre,
                                  adj_epit_int_pre,
                                  adj_epit_exp_pos,
                                  adj_epit_int_pos,
                                  genero_adjetivo, numero_adjetivo,
                                  contracao=None)

            gn = " ".join((nucleo_logico, qualif))
        return re.sub(' +', ' ', gn).strip()
    except ValueError:
        return ''


def estrutura_gn_downranked(dissoc_ente_nucleo=None, tem_qualificador=None,
                           tipo_qualificador=None, indice_preposicao_qualif=None,
                           determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None,
                           numero_beta=None,
                           morfologia_do_pronome_beta=None, determinacao_especificidade_alpha=None,
                           orientacao_alpha=None,
                           genero_alpha=None, numero_alpha=None, morfologia_do_pronome_alpha=None,
                           pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None, genero_obj_possuido=None,
                           pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None, cardinal=None,
                           genero_numerativo=None,
                           tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                           tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
                           numero_subs=None, genero_subs=None, tipo_feminino_ao=None, tipo_masc_ao=None,
                           acent_tonica=None,
                           nome_prop_fp=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                           morfologia_do_pronome=None, reflexivo=None,
                           # classificador
                           adjetivo_classificador=None,
                           # epitetos
                           adj_epit_exp_pre=None,
                           adj_epit_int_pre=None,
                           adj_epit_exp_pos=None,
                           adj_epit_int_pos=None,
                           genero_adjetivo=None, numero_adjetivo=None,

                           contracao=None):
    """
    Ex.:
    >>>  estrutura_gn_downraked(dissoc_ente_nucleo=None,tem_qualificador=None,tipo_qualificador=None,
    indice_preposicao_qualif=None,determinacao_especificidade_beta='específico',
    orientacao_beta='NA',genero_beta='masculino',numero_beta=None,morfologia_do_pronome_beta=None,
    determinacao_especificidade_alpha='específico',orientacao_alpha='NA',genero_alpha='masculino',
    numero_alpha='singular',morfologia_do_pronome_alpha=None,pessoa_da_interlocucao_possuidor='1s',
    numero_obj_possuido='singular',genero_obj_possuido='masculino',
    pessoa_da_interlocucao_proximidade='próximo_ao_falante',tipo_numerativo=None,cardinal=None,
    genero_numerativo=None,tipo_de_ente='não_consciente',tipo_de_nao_consciente='material',
    tipo_de_nao_consciente_material='objeto_material',tipo_de_nao_consciente_semiotico=None,
    classe_palavra_ente='substantivo_comum',substantivo_lematizado='piano',numero_subs='singular',
    genero_subs='masculino',tipo_feminino_ao=None,tipo_masc_ao=None,acent_tonica=None,nome_prop_fp=None,
    pessoa_da_interlocucao=None,transitividade_verbo=None,tonicidade=None,morfologia_do_pronome=None,
    reflexivo=None,
    adjetivo_classificador='importado',
    adj_epit_exp_pre=None,
    adj_epit_int_pre='grande',
    adj_epit_exp_pos=None,
    adj_epit_int_pos='bonito',
    genero_adjetivo='masculino',
    numero_adjetivo='singular',
    contracao=None)

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
    :return:
    """
    gn_downranked = estrutura_gn(dissoc_ente_nucleo, tem_qualificador,
                 tipo_qualificador, indice_preposicao_qualif,
                 determinacao_especificidade_beta, orientacao_beta, genero_beta, numero_beta,
                 morfologia_do_pronome_beta, determinacao_especificidade_alpha, orientacao_alpha,
                 genero_alpha, numero_alpha, morfologia_do_pronome_alpha,
                 pessoa_da_interlocucao_possuidor, numero_obj_possuido, genero_obj_possuido,
                 pessoa_da_interlocucao_proximidade, tipo_numerativo, cardinal,
                 genero_numerativo,
                 tipo_de_ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                 tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado,
                 numero_subs, genero_subs, tipo_feminino_ao, tipo_masc_ao, acent_tonica,
                 nome_prop_fp, pessoa_da_interlocucao, transitividade_verbo, tonicidade,
                 morfologia_do_pronome, reflexivo,
                 # classificador
                 adjetivo_classificador,
                 # epitetos
                 adj_epit_exp_pre,
                 adj_epit_int_pre,
                 adj_epit_exp_pos,
                 adj_epit_int_pos,
                 genero_adjetivo, numero_adjetivo,

                 contracao)

    return re.sub(' +', ' ', gn_downranked).strip()

# # ####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
# # ##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal
# # # com função de Numerativo no GN DE PRIMEIRO NÍVEL)