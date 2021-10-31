from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_nominais import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *


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
              "β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)"]# ex.: Um meu
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
            elif pessoa_da_interlocucao_possuidor == '1s' and numero_obj_possuido == 'plural'\
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

def deixis_geral(determinacao_espeficifidade_beta=None, orientacao_beta=None,
                 genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
                 determinacao_espeficifidade_alpha=None,
                 orientacao_alpha=None, genero_alpha=None, numero_alpha=None, morfologia_do_pronome_alpha=None,
                 pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
                 genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None):
    """

    Ex.:
    
    >>> deixis_geral(determinacao_espeficifidade_beta='específico', orientacao_beta='NA',
    ... genero_beta='masculino', numero_beta='singular', morfologia_do_pronome_beta='padrão',
    ...determinacao_espeficifidade_alpha='específico',
    ... orientacao_alpha='orientação_específica_pessoa', genero_alpha='masculino', numero_alpha='singular',
    ...morfologia_do_pronome_alpha='padrão',
    ...pessoa_da_interlocucao_possuidor='1s', numero_obj_possuido='singular',
    ... genero_obj_possuido='masculino', pessoa_da_interlocucao_proximidade=None)

    'o meu'
    
    >>> deixis_geral(None,None, None,None,None,'específico','orientação_específica_proximidade', 'masculino','singular',
             ...'morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
    'este'

    :param determinacao_espeficifidade_beta:['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']
    :param orientacao_beta:['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']
    :param pessoa_da_interlocucao_possuidor:['1s', '2s', '3s', '1p', '2p', '3p']
    :param numero_obj_possuido: ['singular', 'plural']
    :param genero_obj_possuido:['masculino', 'feminino']
    :param morfologia_do_pronome_beta: padrão', 'morfologia_terceira_pessoa']
    :param determinacao_espeficifidade_alpha:['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
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
        if determinacao_espeficifidade_alpha == 'específico':
            if orientacao_alpha == 'orientação_específica_proximidade':
                alpha = deitico_prox(determinacao_espeficifidade_alpha, orientacao_alpha,
                                     pessoa_da_interlocucao_proximidade, numero_alpha, genero_alpha)
            elif orientacao_alpha == 'orientação_específica_pessoa':
                alpha = deitico_pess(determinacao_espeficifidade_alpha, orientacao_alpha,
                                     pessoa_da_interlocucao_possuidor,
                                     numero_obj_possuido, genero_obj_possuido, morfologia_do_pronome_alpha)
            else:
                alpha = deitico_nao_seletivo_especifico(determinacao_espeficifidade_alpha,
                                                        orientacao_alpha, numero_alpha, genero_alpha)
        elif determinacao_espeficifidade_alpha == 'não_específico':
            alpha = deitico_nao_seletivo_nao_especifico(determinacao_espeficifidade_alpha,
                                                        orientacao_alpha, numero_alpha, genero_alpha)
        else:
            alpha = ''

        if determinacao_espeficifidade_beta == 'específico':

            if orientacao_beta == 'orientação_específica_proximidade':
                beta = deitico_prox(determinacao_espeficifidade_beta, orientacao_beta,
                                    pessoa_da_interlocucao_proximidade,
                                    numero_beta, genero_beta)
            elif orientacao_beta == 'orientação_específica_pessoa':
                beta = deitico_pess(determinacao_espeficifidade_beta, orientacao_beta,
                                    pessoa_da_interlocucao_possuidor,
                                    numero_obj_possuido, genero_obj_possuido, morfologia_do_pronome_beta)
            else:
                beta = deitico_nao_seletivo_especifico(determinacao_espeficifidade_beta, orientacao_beta, numero_beta,
                                                       genero_beta)
        elif determinacao_espeficifidade_beta == 'não_específico':
            beta = deitico_nao_seletivo_nao_especifico(determinacao_espeficifidade_beta,
                                                       orientacao_beta, numero_beta, genero_beta)

        else:
            beta = ''

        return re.sub(' +', ' ', " ".join((beta, alpha))).strip()
    except ValueError:
        return ''

#
#
#


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

    

#####ESTRUTURA DO GRUPO NOMINAL:

##
# print('Há Qualificador no gn?')
# tem_qualificador = choice.Menu(['sim', 'NA']).ask()
# realizacao_qualificador = choice.Menu(['frase-preposicional', 'oração']).ask()

##parei aqui
def qualificador(indicePreposicaoFrase=None, dissocEnteNucleo=None, DETERMINAÇÃO_espeficifidade_beta=None,
                 ORIENTAÇÃO_beta=None,
                 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
                 DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
                 número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
                 número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,  #
                 funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
                 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
                 tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                 tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
                 numero=None,
                 tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
                 pessoa_da_interlocucao=None,
                 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
                 temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None, adjetivo_epiteto=None,
                 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
    """

    :param indicePreposicaoFrase:
    :param dissocEnteNucleo:
    :param DETERMINAÇÃO_espeficifidade_beta:
    :param ORIENTAÇÃO_beta:
    :param gênero_beta:
    :param número_beta:
    :param morfologia_do_pronome_beta:
    :param DETERMINAÇÃO_espeficifidade_alpha:
    :param ORIENTAÇÃO_alpha:
    :param gênero_alpha:
    :param número_alpha:
    :param morfologia_do_pronome_alpha:
    :param pessoa_da_interlocução_possuidor:
    :param número_obj_possuído:
    :param gênero_obj_possuído:
    :param pessoa_da_interlocução_proximidade:
    :param funcaoNumerativo:
    :param cardinal:
    :param genero:
    :param tipo_precisa:
    :param tipoRealCard:
    :param milharExtenso:
    :param centenaExtenso:
    :param dezenaExtenso:
    :param unidadeExtenso:
    :param numIndefinido:
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
    :param nome_proprio:
    :param pessoa_da_interlocucao:
    :param transitividade_verbo:
    :param tonicidade:
    :param morfologia_do_pronome:
    :param reflexivo:
    :param temQualificador:
    :param tipoQualificador:
    :param indicePreposicaoQualif:
    :param adjetivo_epiteto:
    :param adjetivo_classificador:
    :param generoAdjetivo:
    :param numeroAdjetivo:
    :param contracao:
    :return:
    """
    try:
        if tipoQualificador == 'frase-preposicional':
            Qualificador = frase_preposicional(indicePreposicaoFrase, dissocEnteNucleo, temQualificador,
                                               tipoQualificador,
                                               indicePreposicaoQualif, DETERMINAÇÃO_espeficifidade_beta,
                                               ORIENTAÇÃO_beta, gênero_beta,
                                               número_beta, morfologia_do_pronome_beta,
                                               DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
                                               número_alpha, morfologia_do_pronome_alpha,
                                               pessoa_da_interlocução_possuidor, número_obj_possuído,
                                               gênero_obj_possuído, pessoa_da_interlocução_proximidade,
                                               funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
                                               milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                               numIndefinido, tipo_de_ente, tipo_de_nao_consciente,
                                               tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
                                               classe_palavra_ente, substantivo_lematizado, numero, tipo_feminino_ao,
                                               tipo_masc_ao, acent_tonica, nome_proprio, pessoa_da_interlocucao,
                                               transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
                                               adjetivo_epiteto, adjetivo_classificador, generoAdjetivo, numeroAdjetivo,
                                               contracao)
            # else:
            # 	Qualificador = "que" + oraçãoProjetada()
            return re.sub(' +', ' ', Qualificador).strip()
    except:
        return ''


#
# for i in range(12):
# 	print(qualificador(indicePreposicaoFrase=i,dissocEnteNucleo=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino', número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s', número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor', funcaoNumerativo=None, cardinal=None,
# 			 genero='masculino', tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
# 			 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None, tipo_de_ente='não_consciente',
# 			 tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural', tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
# 			 nome_proprio=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
# 			 morfologia_do_pronome=None, reflexivo=None, temQualificador=None, tipoQualificador='frase-preposicional',indicePreposicaoQualif=5,
# 			 adjetivo_epiteto='bonito', adjetivo_classificador=None, generoAdjetivo='masculino',
# 			 numeroAdjetivo='plural', contracao='-contração'))


def estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None,
                 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
                 morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None,
                 gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
                 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
                 pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero=None,
                 tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
                 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
                 tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                 tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
                 numero=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
                 pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
                 reflexivo=None, adjetivo_epiteto=None,
                 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
    try:
        if dissocEnteNucleo == None:

            Determinante = deixis_geral(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
                                        gênero_beta, número_beta, morfologia_do_pronome_beta,
                                        DETERMINAÇÃO_espeficifidade_alpha,
                                        ORIENTAÇÃO_alpha, gênero_alpha, número_alpha, morfologia_do_pronome_alpha,
                                        pessoa_da_interlocução_possuidor, número_obj_possuído,
                                        gênero_obj_possuído, pessoa_da_interlocução_proximidade)

            numerativo = Numerativo(funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
                                    milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso, numIndefinido)

            ente = ente(tipo_de_ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                        tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado, numero,
                        genero, tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_proprio, pessoa_da_interlocucao,
                        transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo)

            Classificador = adjetivo(adjetivo_classificador, generoAdjetivo, numeroAdjetivo)

            Epiteto = adjetivo(adjetivo_epiteto, generoAdjetivo, numeroAdjetivo)

            GN = " ".join((Determinante, numerativo, ente, Classificador, Epiteto))

        else:

            Nucleo_logico = estrutura_GN_downraked(dissocEnteNucleo, temQualificador, tipoQualificador,
                                                   indicePreposicaoQualif, DETERMINAÇÃO_espeficifidade_beta,
                                                   ORIENTAÇÃO_beta, gênero_beta, número_beta,
                                                   morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
                                                   ORIENTAÇÃO_alpha, gênero_alpha, número_alpha,
                                                   morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
                                                   número_obj_possuído, gênero_obj_possuído,
                                                   pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal,
                                                   genero, tipo_precisa, tipoRealCard, milharExtenso, centenaExtenso,
                                                   dezenaExtenso, unidadeExtenso, numIndefinido, tipo_de_ente,
                                                   tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                                   tipo_de_nao_consciente_semiotico, classe_palavra_ente,
                                                   substantivo_lematizado, numero, tipo_feminino_ao, tipo_masc_ao,
                                                   acent_tonica, nome_proprio, pessoa_da_interlocucao,
                                                   transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
                                                   adjetivo_epiteto, adjetivo_classificador, generoAdjetivo,
                                                   numeroAdjetivo, contracao)

            Qualificador = Qualificador = qualificador(indicePreposicaoQualif, dissocEnteNucleo,
                                                       DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
                                                       gênero_beta, número_beta, morfologia_do_pronome_beta,
                                                       DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
                                                       gênero_alpha,
                                                       número_alpha, morfologia_do_pronome_alpha,
                                                       pessoa_da_interlocução_possuidor,
                                                       número_obj_possuído, gênero_obj_possuído,
                                                       pessoa_da_interlocução_proximidade,  #
                                                       funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
                                                       milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                                       numIndefinido,
                                                       tipo_de_ente, tipo_de_nao_consciente,
                                                       tipo_de_nao_consciente_material,
                                                       tipo_de_nao_consciente_semiotico, classe_palavra_ente,
                                                       substantivo_lematizado, numero,
                                                       tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_proprio,
                                                       pessoa_da_interlocucao,
                                                       transitividade_verbo, tonicidade, morfologia_do_pronome,
                                                       reflexivo,  #
                                                       temQualificador, tipoQualificador, adjetivo_epiteto,
                                                       adjetivo_classificador, generoAdjetivo, numeroAdjetivo,
                                                       contracao)

            GN = " ".join((Nucleo_logico, Qualificador))
        return (re.sub(' +', ' ', GN).strip())
    except:
        GN = ''
        return GN


estrutura_GN(DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA', gênero_alpha='masculino',
             número_alpha='singular', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
             pessoa_da_interlocução_possuidor='1s', número_obj_possuído='plural', gênero_obj_possuído='masculino',
             genero='não-binário', tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
             tipo_de_nao_consciente_material='instituição', classe_palavra_ente='substantivo_comum',
             substantivo_lematizado='desmatamento', numero='singular')

estrutura_GN(None, None, None, None, DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
             gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
             pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
             genero='não-binário', tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
             tipo_de_nao_consciente_material='instituição', classe_palavra_ente='substantivo_comum',
             substantivo_lematizado='desmatamento', numero='singular',
             tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
             transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
             adjetivo_epiteto=None, adjetivo_classificador=None, generoAdjetivo=None,
             numeroAdjetivo='singular', contracao=None)

estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None,
             DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
             morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
             gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
             pessoa_da_interlocução_possuidor='1s', número_obj_possuído='singular', gênero_obj_possuído='masculino',
             pessoa_da_interlocução_proximidade='próximo_ao_falante', funcaoNumerativo=None, cardinal=None,
             genero='não-binário',
             tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None,
             unidadeExtenso=None, numIndefinido=None, tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
             tipo_de_nao_consciente_material='abstração_material', tipo_de_nao_consciente_semiotico=None,
             classe_palavra_ente='substantivo_comum', substantivo_lematizado='piano', numero='singular',
             tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
             transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
             adjetivo_epiteto=None, adjetivo_classificador=None, generoAdjetivo=None,
             numeroAdjetivo=None, contracao=None)

estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None,
             DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
             morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha='específico',
             ORIENTAÇÃO_alpha='orientação_específica_pessoa',
             gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
             pessoa_da_interlocução_possuidor='1s', número_obj_possuído='singular', gênero_obj_possuído='masculino',
             pessoa_da_interlocução_proximidade='próximo_ao_falante', funcaoNumerativo=None, cardinal=None,
             genero='não-binário',
             tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None,
             unidadeExtenso=None, numIndefinido=None, tipo_de_ente=None, tipo_de_nao_consciente=None,
             tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
             classe_palavra_ente=None, substantivo_lematizado=None, numero=None,
             tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
             transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
             adjetivo_epiteto=None, adjetivo_classificador=None, generoAdjetivo=None,
             numeroAdjetivo=None, contracao=None)

estrutura_GN(None, None, None, None,
             None, None, None, None,
             None, 'específico', 'NA',
             'masculino', 'singular', None,
             None, None, None,
             None, None, None, 'não-binário',
             None, None, None, None, None,
             None, None, 'não_consciente', 'material',
             'abstração_material', None,
             'substantivo_comum', 'moço', 'singular',
             None, None, None, None, None,
             None, None, None, None,
             None, None, None,
             None, None)


# # ########PREPOSIÇÃO
# preposicoes = ['a','ante','após','até','com','contra',
# 				   'de','desde','em','entre','para','por','perante','sem',
# 				   'sob','sobre','trás']


def estrutura_GN_downraked(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None,
                           indicePreposicaoQualif=None,
                           DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None,
                           número_beta=None,
                           morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha=None,
                           ORIENTAÇÃO_alpha=None,
                           gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
                           pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
                           pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero=None,
                           tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
                           dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
                           tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                           tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
                           numero=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
                           pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                           morfologia_do_pronome=None,
                           reflexivo=None, adjetivo_epiteto=None,
                           adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
    GN_downranked = estrutura_GN(dissocEnteNucleo, temQualificador, tipoQualificador, indicePreposicaoQualif,
                                 DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, gênero_beta, número_beta,
                                 morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
                                 gênero_alpha, número_alpha, morfologia_do_pronome_alpha,
                                 pessoa_da_interlocução_possuidor, número_obj_possuído, gênero_obj_possuído,
                                 pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal, genero, tipo_precisa,
                                 tipoRealCard, milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                 numIndefinido, tipo_de_ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                 tipo_de_nao_consciente_semiotico, classe_palavra_ente, substantivo_lematizado, numero,
                                 tipo_feminino_ao, tipo_masc_ao, acent_tonica, nome_proprio, pessoa_da_interlocucao,
                                 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo, adjetivo_epiteto,
                                 adjetivo_classificador, generoAdjetivo, numeroAdjetivo, contracao)

    return re.sub(' +', ' ', GN_downranked).strip()

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
# 			 tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			adjetivo_epiteto='bonito',
# 			 adjetivo_classificador=None,
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
# 			 tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
# 			 substantivo_lematizado='árvore', numero='plural',
# 			 tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			,adjetivo_epiteto='bonito',
# 			 adjetivo_classificador=None,
# 					   generoAdjetivo='feminino', numeroAdjetivo='plural',contracao='+contação')
# #

# # ####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
# # ##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal
# # # com função de Numerativo no GN DE PRIMEIRO NÍVEL)
# 	print('Há dissociação entre Ente e Núcleo do GN?')
# 	dissocEnteNucleo = choice.Menu(['sim', 'não']).ask()
