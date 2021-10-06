from NLG_BRAZILIAN_PORTUGUESE.funcoes_por_ordem.ordem_morfema.morf_verbais import *


def def_classe_de_verbo(funcao_no_grupo_verbal: str) -> str:
    """
    Retorna a classe do verbo dada a sua função potencial no grupo verbal

    ex.:
    >>>def_classe_de_verbo ('Modal')
    >>>'modal'
    :param funcao_no_grupo_verbal:
        opções:  'Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo','Auxiliar+Núcleo', 'Modal+Núcleo'
    :return classe_verbo:
        'lexical','auxiliar','modal'


    """

    try:
        if funcao_no_grupo_verbal == 'Evento' or funcao_no_grupo_verbal == 'Evento+Núcleo':
            classe_verbo = 'lexical'
        elif funcao_no_grupo_verbal == 'Auxiliar' or funcao_no_grupo_verbal == 'Auxiliar+Núcleo':
            classe_verbo = 'auxiliar'
        elif funcao_no_grupo_verbal == 'Modal' or funcao_no_grupo_verbal == 'Modal+Núcleo':
            classe_verbo = 'modal'
        else:
            classe_verbo = None

        return classe_verbo
    except KeyError:
        return ''
"""
#     Retorna a realização dos verbos terminados em -cer, dados os parâmetros.
#
#
#     :param verbo: str
#         lema verbal - no infinitivo
#     :param tipo_de_orientacao: str
#         opções: 'infinitivo','presente','pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
#         'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo','subjuntivo_condicional', 'subjuntivo_optativo',
#         'não_finito_concretizado','imperativo_I','imperativo_II','gerúndio', 'particípio'
#     :param padrao_de_morfologia:str
#        escolhas: 'AR','ER','IR', 'OR'
#     :param oi_numero:str
#        escolhas: 'singular', 'plural'
#     :param genero:str
#         escolhas: 'feminino', 'masculino'
#     :param oi_tipo_de_pessoa:str
#         escolhas: '1pessoa','2pessoa','3pessoa'
#     :param padrao_pessoa_morfologia:str
#        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
#     :return verbo: str
#         verbo conjugado de acordo com os parâmetros
#     """


# FORMAÇÃO DOS VERBOS IRREGULARES

# VERBOS TERMINADOS EM : 'cer'
def formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:

    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            if oi_tipo_de_pessoa == '1pessoa':
                me = verbo[slice(-3)] + 'ç'
            else:
                me = experiencia_do_verbo(verbo)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'ç'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if (oi_tipo_de_pessoa == '3pessoa' or
                    oi_tipo_de_pessoa == '1pessoa'):
                me = verbo[slice(-3)] + 'ç'
            else:
                me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-3)] + 'ç'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except KeyError:
        return ''


# ###VERBOS TERMINADOS EM : 'çar'

def formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """
    >>> formacao_verbo_ÇAR('despedaçar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
    >>> formacao_verbo_ÇAR('abraçar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
    >>> formacao_verbo_ÇAR('abraçar','imperativo_I','-AR','plural',None,'3pessoa')
    >>> formacao_verbo_ÇAR('abraçar','imperativo_II','-AR','singular',None,'2pessoa')
    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """

    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'c'
            else:
                me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'c'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if oi_tipo_de_pessoa == '2pessoa':
                me = experiencia_do_verbo(verbo)
            else:
                me = verbo[slice(-3)] + 'c'
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-3)] + 'c'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except KeyError:
        return ''

# ###VERBOS TERMINADOS EM : 'Car'


def formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """
    >>>formacao_verbo_CAR('identificar','imperativo_I','-AR','singular',None,'2pessoa')
    >>>formacao_verbo_CAR('focar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
    >>>formacao_verbo_CAR('focar','imperativo_I','-AR','plural',None,'3pessoa')
    >>>formacao_verbo_CAR('focar','imperativo_II','-AR','singular',None,'2pessoa')

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'qu'
            else:
                me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'qu'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-3)] + 'qu'
                elif oi_tipo_de_pessoa == '1pessoa':
                    me = ''
                else:
                    me = experiencia_do_verbo(verbo)
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '3pessoa' or oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-3)] + 'qu'
                else:
                    me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa':
                me = ''
            else:
                me = verbo[slice(-3)] + 'qu'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)
        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except KeyError:
        return ''
#
# #
#
# ###VERBOS TERMINADOS EM : 'GAR'
#


def formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """
    Ex.:

    >>> formacao_verbo_GAR('carregar','imperativo_I','-AR','singular',None,'2pessoa')

    >>> 'carrega'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """

    me, mi = '', ''
    try:

        if tipo_de_orientacao == 'presente':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'gu'
            else:
                me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'gu'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if (oi_tipo_de_pessoa == '3pessoa' or
                    oi_tipo_de_pessoa == '1pessoa'):
                me = verbo[slice(-3)] + 'gu'
            else:
                me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-3)] + 'gu'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except KeyError:
        return ''


def formacao_verbo_possuir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                           genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """

    >>> formacao_verbo_possuir('possuir','imperativo_I','-IR','plural',None,'2pessoa')
    >>> 'possuí'
    >>> formacao_verbo_possuir('possuir','presente','-IR','singular',None,'1pessoa')
    >>> 'possuo'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:
    """
    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'o'
                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'i'
                    else:
                        mi = 'is'
                elif oi_tipo_de_pessoa == '3pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'i'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = experiencia_do_verbo(verbo)
                        mi = 'i'
                    else:
                        me = experiencia_do_verbo(verbo)
                        mi = 'ímos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'ís'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = experiencia_do_verbo(verbo)
                        mi = 'i'
                    else:
                        me = experiencia_do_verbo(verbo)
                        mi = 'em'
        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ía'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ía'
                    else:
                        mi = 'ías'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'ía'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ía'
                    else:
                        mi = 'íamos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'íeis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ía'
                    else:
                        mi = 'íam'

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'í'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iu'
                    else:
                        mi = 'íste'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'iu'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iu'

                    else:
                        mi = 'ímos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ístes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iu'
                    else:
                        mi = 'íram'

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)
            mi = ''.join(('í', mi[1:]))

        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            mi = ''.join(('í', mi[1:]))

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)

            if (oi_numero == 'singular' and oi_tipo_de_pessoa == '2pessoa' or
                    oi_numero == 'plural' and oi_tipo_de_pessoa == '3pessoa'):
                mi = ''.join(('í', mi[1:]))

        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = experiencia_do_verbo(verbo)
                        mi = 'a'
                    else:
                        me = experiencia_do_verbo(verbo)
                        mi = 'i'

                else:
                    me = experiencia_do_verbo(verbo)
                    mi = 'a'

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = experiencia_do_verbo(verbo)
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'í'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'

        elif tipo_de_orientacao == 'imperativo_II':
            me = ''.join((verbo[slice(-4)], 'id'))
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except KeyError:
        return ''


#
# ###VERBOS TERMINADOS EM : 'RUIR'
#
# def formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if verbo[-5:] == 'truir' and tipo_de_orientacao == 'presente':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'o'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-3)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ói'
#                 else:
#                     MI = 'óis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-3)]
#                 MI = 'ói'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-3)]
#                     MI = 'ói'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'ímos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'ís'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-3)]
#                     MI = 'ói'
#                 else:
#                     ME = verbo[slice(-3)] + 'o'
#                     MI = 'em'
#
#     elif verbo[-4:] == 'ruir' and tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'o'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'i'
#                 else:
#                     MI = 'is'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'i'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'i'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'ímos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'ís'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'i'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'em'
#     elif verbo[-5:] == 'truir' and tipo_de_orientacao == 'imperativo_I':
#         if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#             ME = verbo[slice(-3)]
#             MI = 'ói'
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#             ME = experiencia_do_verbo(verbo)
#             MI = 'í'
#         else:
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif verbo[-4:] == 'ruir' and tipo_de_orientacao == 'imperativo_I':
#         if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#             ME = verbo[slice(-1)]
#             MI = ''
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#             ME = experiencia_do_verbo(verbo)
#             MI = 'í'
#         else:
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif (verbo[-5:] == 'truir' or
#           verbo[-4:] == 'ruir'):
#         if tipo_de_orientacao == 'pretérito_imperfectivo':
#             ME = experiencia_do_verbo(verbo)
#             if OI_numero == 'singular':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     MI = 'ía'
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ía'
#                     else:
#                         MI = 'ías'
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     MI = 'ía'
#
#             elif OI_numero == 'plural':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ía'
#                     else:
#                         MI = 'íamos'
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     MI = 'íeis'
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ía'
#                     else:
#                         MI = 'íam'
#
#         elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#             ME = experiencia_do_verbo(verbo)
#             if OI_numero == 'singular':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     MI = 'í'
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'iu'
#                     else:
#                         MI = 'íste'
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     MI = 'iu'
#
#             elif OI_numero == 'plural':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'iu'
#
#                     else:
#                         MI = 'ímos'
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     MI = 'ístes'
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'iu'
#                     else:
#                         MI = 'íram'
#
#         elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
#                                                                     OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             MI = 'í' + MI[1:]
#
#         elif tipo_de_orientacao == 'subjuntivo_condicional':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             MI = 'í' + MI[1:]
#
#         elif tipo_de_orientacao == 'subjuntivo_optativo':
#             ME = experiencia_do_verbo(verbo)
#             if (OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' or
#                     OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
#                 MI = 'í' + (realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                                            OI_tipo_de_pessoa, padrao_pessoa_morfologia)[
#                             1:])
#             else:
#                 MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                                     OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#         elif tipo_de_orientacao == 'passado_volitivo':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                              OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#         elif tipo_de_orientacao == 'pretérito_imperfectivo':
#             ME = experiencia_do_verbo(verbo)
#             if OI_numero == 'singular':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     MI = 'ía'
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ía'
#                     else:
#                         MI = 'ías'
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     MI = 'ía'
#
#             elif OI_numero == 'plural':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ía'
#                     else:
#                         MI = 'ímos'
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     MI = 'íeis'
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ía'
#                     else:
#                         MI = 'íam'
#
#         elif tipo_de_orientacao == 'não_finito_concretizado':
#             ME = experiencia_do_verbo(verbo)
#             if (OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular' or
#                     OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural'):
#                 MI = 'í' + (realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                                OI_tipo_de_pessoa,
#                                                                                padrao_pessoa_morfologia)[1:])
#             else:
#                 MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                         OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#         elif tipo_de_orientacao == 'futuro':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#         elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                                   OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#         elif tipo_de_orientacao == 'imperativo_II':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
#                                                           OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#         elif tipo_de_orientacao == 'gerúndio':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#
#         elif tipo_de_orientacao == 'particípio':
#             ME = experiencia_do_verbo(verbo)
#             MI = "í" + realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)[1:]
#
#         elif tipo_de_orientacao == 'infinitivo':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                        padrao_pessoa_morfologia)
#
#     verbo = ME + MI
#
#     return verbo
#
#
# #
# # verbo=formacao_verbo_RUIR('construir', 'presente', '-IR','plural' ,None, '3pessoa')
# # verbo=formacao_verbo_RUIR('usufruir', 'presente', '-IR','plural' ,None, '3pessoa')
# #
# # verbo=formacao_verbo_RUIR('construir', 'subjuntivo_optativo', '-IR','plural' ,None, '3pessoa')
# # verbo=formacao_verbo_RUIR('usufruir', 'subjuntivo_condicional', '-IR','plural' ,None, '3pessoa')
# #
# formacao_verbo_RUIR('construir', 'imperativo_I', '-IR', 'singular', None, '1pessoa')
#
#
# # verbo=formacao_verbo_RUIR('usufruir', 'imperativo_I', '-IR','plural' ,None, '2pessoa')
# #
# #
# # verbo=formacao_verbo_RUIR('construir', 'não_finito_concretizado', '-IR','singular' ,None, '2pessoa')
# # verbo=formacao_verbo_RUIR('ruir', 'não_finito_concretizado', '-IR','singular' ,None, '2pessoa')
#
#
# # #
# # formacao_verbo_RUIR('construir','particípio','-IR','singular','masculino',None)
# # formacao_verbo_RUIR('focar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# # formacao_verbo_RUIR('focar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# # formacao_verbo_RUIR('focar','imperativo_I','-AR','plural',None,'3pessoa')
# # formacao_verbo_RUIR('focar','imperativo_II','-AR','singular',None,'2pessoa')
#
# # VERBO agredir
#
# def formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                            genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'o'
#                 verbo = ME + 'id' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)] + 'id'
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'es'
#                     verbo = ME + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)] + 'id'
#                 MI = 'e'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)] + 'id'
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'imos'
#                     verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'is'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)] + 'id'
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'em'
#                     verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-4)] + 'id'
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                             OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'imperativo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 print('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)]
#                     MI = 'a'
#                     verbo = ME + "ir" + MI
#                 else:
#                     ME = verbo[slice(-4)]
#                     MI = 'e'
#                     verbo = ME + "id" + MI
#             else:
#                 ME = verbo[slice(-4)]
#                 MI = 'a'
#                 verbo = ME + "id" + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'id' + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'id' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'i'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'id' + MI
#
#                 else:
#                     MI = 'am'
#                     verbo = ME + 'id' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
#                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + 'id' + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     return verbo
#
#
# #
# # formacao_verbo_agredir('agredir','particípio','plural','masculino',None)
# # formacao_verbo_agredir('agredir','particípio','plural','masculino',None)
# # formacao_verbo_agredir('agredir','particípio','singular','masculino',None)
# # formacao_verbo_agredir('agredir','gerúndio',None,None,None)
# # formacao_verbo_agredir('agredir', 'infinitivo', None, None, None)
# # formacao_verbo_agredir('agredir', 'pretérito_perfectivo_II', 'singular', None, '1pessoa')
# # formacao_verbo_agredir('agredir','pretérito_imperfectivo','singular',None,'1pessoa')
#
# # VERBO aferir
#
#
# def formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                           genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'o'
#                 verbo = ME + 'ir' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'es'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'e'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'imos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'is'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'em'
#                     verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-4)] + 'ir'
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                             OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 print('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)]
#                     MI = 'a'
#                     verbo = ME + "ir" + MI
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'e'
#                     verbo = ME + MI
#             else:
#                 ME = verbo[slice(-4)]
#                 MI = 'a'
#                 verbo = ME + "ir" + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'ir' + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'ir' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'i'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'ir' + MI
#
#                 else:
#                     MI = 'am'
#                     verbo = ME + 'ir' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
#                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + 'ir' + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#     return verbo
#
#
# #
# # formacao_verbo_aferir('aferir', 'não_finito_concretizado',  'singular', None, '2pessoa')
# # formacao_verbo_aferir('aferir', 'subjuntivo_optativo',  'singular', None, '2pessoa')
# # formacao_verbo_aferir('aferir', 'particípio',  'singular', 'masculino', None)
# # formacao_verbo_agredir('aferir','particípio','singular','feminino',None)
#
#
# # VERBO MEDIR
# def formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if tipo_de_orientacao == 'presente':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-3)]
#                 MI = 'o'
#                 verbo = ME + 'ç' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'es'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'e'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'imos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'is'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'em'
#                     verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     if tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-4)] + 'eç'
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                                      OI_tipo_de_pessoa,
#                                                                                      padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                             OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 print('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)]
#                     MI = 'a'
#                     verbo = ME + "eç" + MI
#
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'e'
#                     verbo = ME + MI
#             else:
#                 ME = verbo[slice(-4)]
#                 MI = 'a'
#                 verbo = ME + "eç" + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'eç' + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'eç' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'i'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa':
#             ME = verbo[slice(-4)]
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'a'
#                 verbo = ME + 'eç' + MI
#             else:
#                 MI = 'am'
#                 verbo = ME + 'eç' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
#                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + 'eç' + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#     return verbo
#
#
# # formacao_verbo_medir('medir','presente','-IR','singular',None,'2pessoa')
#
#
# # VERBO sentir
#
# def formacao_verbo_sentir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                           genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if tipo_de_orientacao == 'presente':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-5)] + 'int'
#                 MI = 'o'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'es'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'e'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             ME = experiencia_do_verbo(verbo)
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'imos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'is'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                     verbo = ME + MI
#                 else:
#                     MI = 'em'
#                     verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     if tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-5)] + 'int'
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                                      OI_tipo_de_pessoa,
#                                                                                      padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                             OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 print('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-5)] + "int"
#                     MI = 'a'
#                     verbo = ME + MI
#
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'e'
#                     verbo = ME + MI
#             else:
#                 ME = verbo[slice(-4)] + "int"
#                 MI = 'a'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)] + 'int'
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'i'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa':
#             ME = verbo[slice(-5)] + 'int'
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'a'
#                 verbo = ME + MI
#             else:
#                 MI = 'am'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-5)] + 'int'
#         MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
#                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#     return verbo
#
#
# #
# # formacao_verbo_sentir('sentir','subjuntivo_conjuntivo','-IR','plural',None,'1pessoa')
# # formacao_verbo_sentir('sentir','presente','-IR','singular',None,'3pessoa')
# # formacao_verbo_sentir('sentir','presente','-IR','singular',None,'1pessoa')
# # formacao_verbo_sentir('sentir', 'infinitivo','-IR',  'singular', 'masculino', None)
# # formacao_verbo_sentir('sentir','particípio','-IR','singular','feminino',None)
# # formacao_verbo_sentir('sentir','gerúndio','-IR',None,None,None)
#
# # VERBO SABER
# def formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if tipo_de_orientacao == 'infinitivo':
#         verbo = verbo
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     #
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'presente':
#
#         if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#             ME = verbo[slice(-4)]
#             MI = 'ei'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#             ME = experiencia_do_verbo(verbo)
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'e'
#                 verbo = ME + MI
#
#             else:
#                 MI = 'es'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
#             ME = experiencia_do_verbo(verbo)
#             MI = 'e'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'e'
#                 verbo = ME + MI
#
#             else:
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'emos'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#             ME = experiencia_do_verbo(verbo)
#             MI = 'eis'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'e'
#                 verbo = ME + MI
#
#             else:
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'em'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = verbo[slice(-4)]
#         if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#             MI = 'oube'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oube'
#                 verbo = ME + MI
#
#             else:
#                 MI = 'ste'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
#
#             MI = 'oube'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oube'
#                 verbo = ME + MI
#             else:
#                 MI = 'oubemos'
#                 verbo = ME + MI
#
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#
#             MI = 'oubestes'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oube'
#                 verbo = ME + MI
#
#             else:
#                 MI = 'ouberam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = verbo[slice(-4)]
#         if ((OI_tipo_de_pessoa == '1pessoa' or '3pessoa') and OI_numero == 'singular'):
#             MI = 'oubera'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubera'
#                 verbo = ME + MI
#             else:
#                 MI = 'ouberas'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubera'
#                 verbo = ME + MI
#             else:
#                 MI = 'oubéramos'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubera'
#                 verbo = ME + MI
#
#             else:
#                 MI = 'oubéreis'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubera'
#                 verbo = ME + MI
#
#             else:
#                 MI = 'ouberam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#
#         ME = verbo[slice(-4)]
#         if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular'
#                 or OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
#             MI = 'oubesse'
#             verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubesse'
#                 verbo = ME + MI
#             else:
#                 MI = 'oubesses'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubesse'
#                 verbo = ME + MI
#             else:
#                 MI = 'oubésssemos'
#                 verbo = ME + MI
#         #
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubesse'
#                 verbo = ME + MI
#             else:
#                 MI = 'oubésseis'
#                 verbo = ME + MI
#         #
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'oubesse'
#                 verbo = ME + MI
#             else:
#                 MI = 'oubessem'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + 'aib' + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + 'oub' + MI
#     #
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                             OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + 'oub' + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#
#         ME = verbo[slice(-4)]
#         if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#             return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'a'
#                 verbo = ME + "aib" + MI
#             else:
#                 MI = 'e'
#                 verbo = ME + 'ab' + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
#             MI = 'a'
#             verbo = ME + 'aib' + MI
#
#         elif OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'plural':
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'a'
#                 verbo = ME + 'aib' + MI
#             else:
#                 MI = 'amos'
#                 verbo = ME + 'aib' + MI
#
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#             MI = 'ei'
#             verbo = ME + 'ab' + MI
#
#         elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#             if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                 MI = 'a'
#                 verbo = ME + 'aib' + MI
#             else:
#                 MI = 'am'
#                 verbo = ME + 'aib' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-4)]
#         if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#             return "Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida"
#         else:
#             MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                           padrao_pessoa_morfologia)
#         verbo = ME + 'aib' + MI
#
#     return verbo
#
#
# #
# # formacao_verbo_saber('saber', 'pretérito_imperfectivo',  'plural', None, '2pessoa')
# # formacao_verbo_saber('saber', 'presente',  'singular', None, '3pessoa')
# # formacao_verbo_saber('saber', 'presente',  'singular', None, '1pessoa')
# # formacao_verbo_saber('saber', 'particípio',  'singular', 'feminino', None)
# # formacao_verbo_saber('saber', 'gerúndio',  None, None, None)
# # formacao_verbo_saber('saber', 'não_finito_concretizado',  'plural', None, '2pessoa')
# # formacao_verbo_saber('saber', 'futuro',  'singular', None, '1pessoa')
# # formacao_verbo_saber('saber', 'passado_volitivo',  'plural', None, '2pessoa')
# # formacao_verbo_saber('saber', 'pretérito_perfectivo_I',  'singular', None, '3pessoa')
# # formacao_verbo_saber('saber', 'pretérito_perfectivo_II',  'plural', None, '2pessoa')
# # formacao_verbo_saber('saber', 'subjuntivo_condicional',  'plural', None, '2pessoa')
# # formacao_verbo_saber('saber', 'subjuntivo_conjuntivo',  'plural', None, '3pessoa')
# # formacao_verbo_saber('saber', 'imperativo_II',  'singular', None, '1pessoa')
# # formacao_verbo_saber('saber', 'imperativo_I',  'singular', None, '2pessoa')
#
#
# # VERBO ESTAR
#
# def formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     ME = experiencia_do_verbo(verbo)
#     if tipo_de_orientacao == 'subjuntivo_condicional':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'esse'
#                 verbo = ME + 'iv' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'esses'
#                 verbo = ME + 'iv' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'éssemos'
#                 verbo = ME + 'iv' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'ésseis'
#                 verbo = ME + 'iv' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'essem'
#                 verbo = ME + 'iv' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'a'
#                 verbo = ME + 'ej' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'ej' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'ej' + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + 'ej' + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'ej' + MI
#
#
#     elif tipo_de_orientacao == 'imperativo_I':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = 'Imperativos não selecionam 1pessoa do singular'
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'ej' + MI
#                 else:
#                     MI = 'á'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'a'
#                 verbo = ME + 'ej' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'ej' + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 MI = 'ai'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'ej' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = 'Imperativos não selecionam 1pessoa do singular'
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'ej' + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'a'
#                 verbo = ME + 'ej' + MI
#         if OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'ej' + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + 'ej' + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'ej' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'er'
#                 verbo = ME + 'iv' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'eres'
#                 verbo = ME + 'iv' + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'ermos'
#                 verbo = ME + 'iv' + MI
#
#             if OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erdes'
#                 verbo = ME + 'iv' + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erem'
#                 verbo = ME + 'iv' + MI
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'futuro':
#
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 MI = 'ou'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ás'
#
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'á'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '2pessoa'):
#
#                 MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'ão'
#             verbo = ME + MI
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 MI = 'ive'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'iveste'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'eve'
#                 verbo = ME + MI
#         if OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'ivemos'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'ivestes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'iveram'
#                 verbo = ME + MI
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         if OI_numero == 'singular':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 MI = 'ivera'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'iveras'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 MI = 'ivera'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'ivéramos'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'ivéreis'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'iveram'
#
#                 verbo = ME + MI
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'infinitivo':
#
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     elif tipo_de_orientacao == 'particípio':
#
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#
#     return verbo
#
#
# # formacao_verbo_estar('estar','presente','singular',None,'1pessoa')
#
# # VERBO DIZER
#
# def formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#
#     if tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-3)]
#                 MI = 'go'
#                 verbo = ME + MI
#
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = ''
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'es'
#                     verbo = ME + MI
#
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = ''
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = ''
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'emos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = ''
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'eis'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = experiencia_do_verbo(verbo)
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = ''
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'em'
#                     verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'isse'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == "3pessoa_do_singular":
#                     MI = 'isse'
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'isseste'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'isse'
#                 verbo = ME + MI
#
#         elif OI_tipo_de_pessoa == '1pessoa':
#             ME = verbo[slice(-4)]
#             if padrao_pessoa_morfologia == "3pessoa_do_singular":
#                 MI = 'isse'
#                 verbo = ME + MI
#
#             else:
#                 MI = 'issemos'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == "3pessoa_do_singular":
#                     MI = 'isse'
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'issestes'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == "3pessoa_do_singular":
#                     MI = 'isse'
#                     verbo = ME + MI
#                 else:
#                     MI = 'isseram'
#                     verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'ia'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ia'
#
#                 else:
#                     MI = 'ias'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'íamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ia'
#                 else:
#                     MI = 'íeis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ia'
#                 else:
#                     MI = 'iam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'issera'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issera'
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'isseras'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'issera'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issera'
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'isséramos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issera'
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'isséreis'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issera'
#
#
#                 else:
#                     MI = 'isseram'
#
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'iria'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iria'
#                 else:
#                     MI = 'irias'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iria'
#                 else:
#                     MI = 'iríamos'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iria'
#                 else:
#                     MI = 'iríeis'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iria'
#                 else:
#                     MI = 'iriam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = verbo[slice(-3)]
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI[1:]
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'issesse'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issesse'
#                 else:
#                     MI = 'issesses'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issesse'
#                     verbo = ME + MI
#
#                 else:
#                     MI = 'isséssemos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issesse'
#                 else:
#                     MI = 'issésseis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'issesse'
#                 else:
#                     MI = 'issessem'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-3)]
#         if OI_numero == 'singular':
#
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#
#                 MI = 'a'
#                 verbo = ME + 'g' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'g' + MI
#                 else:
#                     MI = 'as'
#                     verbo = ME + 'g' + MI
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'g' + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'g' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'g' + MI
#                 else:
#                     MI = 'ais'
#                     verbo = ME + 'g' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'g' + MI
#                 else:
#                     MI = 'am'
#                     verbo = ME + 'g' + MI
#
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#
#     elif tipo_de_orientacao == 'imperativo_I':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = 'Imperativos não selecionam 1pessoa do singular'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#                     verbo = ME + MI
#                 else:
#                     MI = 'iz'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'iga'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#                 else:
#                     MI = 'igamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'izei'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#                 else:
#                     MI = 'igam'
#                 verbo = ME + MI
#
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = 'Imperativos não selecionam 1pessoa do singular'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#                 else:
#                     MI = 'igas'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'iga'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#
#                 else:
#                     MI = 'igamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#
#                 else:
#                     MI = 'igais'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iga'
#
#                 else:
#                     MI = 'igam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 ME = verbo[slice(-4)]
#                 MI = 'er'
#                 verbo = ME + 'iss' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#
#                 else:
#                     MI = 'eres'
#                     verbo = ME + 'iss' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#
#                 else:
#                     MI = 'ermos'
#                 verbo = ME + 'iss' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erdes'
#                 verbo = ME + 'iss' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#
#                 else:
#                     MI = 'erem'
#                 verbo = ME + 'iss' + MI
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if genero == 'masculino':
#                 MI = 'ito'
#             else:
#                 MI = 'ita'
#         else:
#             if genero == 'masculino':
#                 MI = 'itos'
#             else:
#                 MI = 'itas'
#
#         verbo = ME + MI
#     return verbo
#
#
# #
# formacao_verbo_dizer('maldizer', 'presente', '-ER', 'singular', None, '3pessoa')
#
#
# #
# # ##TESTE dizer
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # ###
# # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'presente',  numero, None, tipo_pessoa))
# #
# # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_I',  numero, None, tipo_pessoa))
# #
# # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'pretérito_imperfectivo',  numero, None, tipo_pessoa))
# #
# # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'pretérito_perfectivo_II',  numero, None, tipo_pessoa))
# #
# # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'passado_volitivo',  numero, None, tipo_pessoa))
# #
# # #futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'futuro',  numero, None, tipo_pessoa))
# #
# # #subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'subjuntivo_conjuntivo',  numero, None, tipo_pessoa))
# #
# # #subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'subjuntivo_condicional',  numero, None, tipo_pessoa))
# #
# #
# # #subjuntivo_optativo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'subjuntivo_optativo',  numero, None, tipo_pessoa))
# #
# #
# # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'imperativo_I',  numero, None, tipo_pessoa))
# #
# # # imperativo_II
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'imperativo_II',  numero, None, tipo_pessoa))
# #
# # # não_finito_concretizado
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_dizer('dizer', 'não_finito_concretizado',  numero, None, tipo_pessoa))
# # # infinitivo
# # print(formacao_verbo_dizer('dizer', 'infinitivo',  numero, 'feminino', None))
# #
# # # gerúndio
# # print(formacao_verbo_dizer('dizer', 'gerúndio',  None, None, None))
# #
# # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_dizer('dizer', 'particípio',  numero, genero, None))
# #
#
# # VERBO CONTER DETER
# def formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                 OI_numero, genero, OI_tipo_de_pessoa,
#                                 padrao_pessoa_morfologia='Morfologia_padrão'):
#     """
#     :return:
#     """
#
#     if tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = experiencia_do_verbo(verbo)
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'esse'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'esses'
#             verbo = ME + 'iv' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'éssemos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'ésseis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'essem'
#             verbo = ME + 'iv' + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = experiencia_do_verbo(verbo)
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#             verbo = ME + 'enh' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#             verbo = ME + 'enh' + MI
#     ###
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_I':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'enh' + MI
#                 else:
#                     MI = 'em'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'enh' + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'ende'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'enh' + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'enh' + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'er'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'eres'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'ermos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erdes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erem'
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#             verbo = ME + 'inh' + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'inh' + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'ính' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'inh' + MI
#                 else:
#                     MI = 'eis'
#                     verbo = ME + 'ính' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'inh' + MI
#                 else:
#                     MI = 'am'
#                     verbo = ME + 'inh' + MI
#     ###
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'presente':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'enho'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'ens'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'em'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'emos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'endes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'êm'
#
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ive'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'iveste'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'eve'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'ivemos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'ivestes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'iveram'
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ivera'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'iveras'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'ivera'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'ivéramos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'ivéreis'
#
#             elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'iveram'
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#
#     return verbo
#
#
# ###VERBO TRAZER
#
# def formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                           genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     if tipo_de_orientacao == 'presente':
#
#         if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#             ME = verbo[slice(-3)] + 'g'
#             MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
#                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         else:
#             if OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = ''
#             else:
#                 ME = experiencia_do_verbo(verbo)
#                 MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = verbo[slice(-4)] + 'oux'
#         if (OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular' or
#                 OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'singular'):
#             MI = 'e'
#         else:
#             MI = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, OI_numero,
#                                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = verbo[slice(-4)] + 'oux'
#         MI = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = verbo[slice(-3)] + 'r'
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = verbo[slice(-3)] + 'r'
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,
#                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-3)] + 'g'
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero,
#                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = verbo[slice(-4)] + 'oux'
#         MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = verbo[slice(-4)] + 'oux'
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, OI_numero,
#                                                             OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif tipo_de_orientacao == 'imperativo_I':
#         if OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'singular':
#             ME = experiencia_do_verbo(verbo)
#             MI = ''
#         elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#             ME = experiencia_do_verbo(verbo)
#             MI = 'ei'
#         else:
#             ME = verbo[slice(-3)] + 'g'
#             MI = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = verbo[slice(-3)] + 'g'
#         MI = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, OI_numero,
#                                                       OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#
#     verbo = ME + MI
#
#     return verbo
#     #
#     # formacao_verbo_trazer('trazer','gerúndio','-ER',None,None,None)
#     # formacao_verbo_trazer('trazer','particípio','-ER','singular','feminino',None)
#     # print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None)
#     #
#     # formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'1pessoa','Morfologia_padrão')
#     # formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'2pessoa','Morfologia_padrão')
#     # formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','singular',None,'3pessoa','Morfologia_padrão')
#     # formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'1pessoa','Morfologia_padrão')
#     # formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'2pessoa','Morfologia_padrão')
#     # formacao_verbo_trazer('trazer','não_finito_concretizado','-ER','plural',None,'3pessoa','Morfologia_padrão')
#
#     verbo = ME + MI
#
#     return verbo
#
#
# # formacao_verbo_ÇAR('despedaçar','presente','-AR','singular',None,'2pessoa','Morfologia_padrão')
# # formacao_verbo_ÇAR('abraçar','subjuntivo_conjuntivo','-AR','singular',None,'1pessoa')
# # formacao_verbo_ÇAR('abraçar','imperativo_I','-AR','plural',None,'3pessoa')
# # formacao_verbo_ÇAR('abraçar','imperativo_II','-AR','singular',None,'2pessoa')
# #
#
#
# # VERBO TER
#
# def formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                        OI_numero, genero, OI_tipo_de_pessoa,
#                        padrao_pessoa_morfologia='Morfologia_padrão'):
#     """
#     :return:
#     """
#
#     if tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = experiencia_do_verbo(verbo)
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'esse'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'esses'
#             verbo = ME + 'iv' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'éssemos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'ésseis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'essem'
#             verbo = ME + 'iv' + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = experiencia_do_verbo(verbo)
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#             verbo = ME + 'enh' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#             verbo = ME + 'enh' + MI
#     ###
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_I':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'enh' + MI
#                 else:
#                     MI = 'em'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'enh' + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'ende'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'enh' + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'enh' + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'er'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'eres'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'ermos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erdes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erem'
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#             verbo = ME + 'inh' + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'inh' + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'ính' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'inh' + MI
#                 else:
#                     MI = 'eis'
#                     verbo = ME + 'ính' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'inh' + MI
#                 else:
#                     MI = 'am'
#                     verbo = ME + 'inh' + MI
#     ###
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'presente':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'enho'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'ens'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'em'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'emos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'endes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'êm'
#
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ive'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'iveste'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'eve'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'ivemos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'ivestes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eve'
#                 else:
#                     MI = 'iveram'
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ivera'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'iveras'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'ivera'
#             verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'ivéramos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'ivéreis'
#
#             elif OI_tipo_de_pessoa == '3pessoa' and OI_numero == 'plural':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'iveram'
#             verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#
#     return verbo
#
#
# #
# # ##TESTE ter
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # #presente
# # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'presente', '-ER', numero, None, tipo_pessoa))
# #
# # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# #
# # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# #
# # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# #
# # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'futuro', '-ER', numero, None, tipo_pessoa))
# #
# # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# #
# # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # subjuntivo_optativo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# #
# # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # não_finito_concretizado
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ter('ter', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # infinitivo
# # print(formacao_verbo_ter('ter', 'infinitivo', '-ER', numero, 'feminino', None))
# #
# # # # gerúndio
# # print(formacao_verbo_ter('ter', 'gerúndio', '-ER', None, None, None))
# # #
# # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None))
#
# # ####################################################################################
#
# # VERBO SER
#
# def formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,
#                        padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     if tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         if OI_numero == 'singular':
#             ME = 'er'
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = 'er'
#                     MI = 'a'
#                 else:
#                     ME = 'ér'
#                     MI = 'amos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = 'er'
#                     MI = 'a'
#                 else:
#                     ME = 'ér'
#                     MI = 'eis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'er'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'ou'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = ''
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'é'
#                 else:
#                     MI = 'és'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = ''
#                 MI = 'é'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = ''
#                     MI = 'é'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'omos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'ois'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = ''
#                     MI = 'é'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'ão'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#
#         ME = 'f'
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ui'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                 else:
#                     MI = 'oste'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'oi'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                     verbo = ME + MI
#                 else:
#                     MI = 'omos'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'ostes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                 else:
#                     MI = 'oram'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = 'f'
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'ora'
#                 verbo = ME + MI
#
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'oras'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'ôramos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'ôreis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'oram'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#
#         ME = 'f'
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'osse'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'osses'
#                     verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'ôssemos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'ôsseis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'ossem'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                               padrao_pessoa_morfologia="Morfologia_padrão")
#         verbo = ME + 'ej' + MI
#     ###
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = 'f'
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'or'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'ores'
#                 verbo = ME + MI
#
#
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'ormos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'ordes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'orem'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_I':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'ej' + MI
#                 else:
#                     MI = 'ê'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'ej' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'ej' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'ede'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'ej' + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = experiencia_do_verbo(verbo)
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'ej' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'ej' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'ej' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa' and OI_numero == 'plural':
#                 MI = 'ais'
#                 verbo = ME + 'ej' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'ej' + MI
#
#     return verbo
#
#
# # # ##TESTE ser
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # #presente
# # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'presente', '-ER', numero, None, tipo_pessoa))
# #
# # # ###
# # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# #
# # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'futuro', '-ER', numero, None, tipo_pessoa))
# #
# # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# #
# # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# #
# # # subjuntivo_optativo
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# #
# # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# #
# # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # não_finito_concretizado
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ser('ser', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # # infinitivo
# # print(formacao_verbo_ser('ser', 'infinitivo', '-ER', numero, 'feminino', None))
# # #
# # # # # gerúndio
# # print(formacao_verbo_ser('ser', 'gerúndio', '-ER', None, None, None))
# # # #
# # # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_ser('ser', 'particípio', '-ER', numero, genero, None))
#
# # ####################################################################################
#
# # VERBO IR
#
# def formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                       genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     if tipo_de_orientacao == 'infinitivo':
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = MI
#     ###
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'v'
#                 MI = 'ou'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ai'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'v'
#                 MI = 'ai'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ai'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'i'
#                 MI = 'des'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ai'
#                 else:
#                     MI = 'am'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'f'
#                 MI = 'ui'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                 else:
#                     MI = 'oste'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'f'
#                 MI = 'oi'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                 else:
#                     MI = 'omos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                 else:
#                     MI = 'ostes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'f'
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'oi'
#                 else:
#                     MI = 'oram'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 ME = 'f'
#                 MI = 'ora'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'oras'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'ôramos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'ôreis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'f'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ora'
#                 else:
#                     MI = 'oram'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = 'f'
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'osse'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'osses'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'ôssemos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'ôsseis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'osse'
#                 else:
#                     MI = 'ossem'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 ME = 'v'
#                 MI = 'á'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ás'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ades'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ão'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia,
#                                                                 OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ai'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'v'
#                 MI = 'á'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = 'i'
#                 MI = 'de'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = 'v'
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ão'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'imperativo_II':
#         ME = 'v'
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             if OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ás'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'á'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ades'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ão'
#                 verbo = ME + MI
#     ###
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = 'f'
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'or'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'ores'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'ormos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'ordes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'or'
#                 else:
#                     MI = 'orem'
#                 verbo = ME + MI
#
#     return verbo
#
#
# # #
# # # #
# # # # # ##TESTE ir
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'presente', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # # #####pretérito_imperfectivo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # # #
# # # # # ### "pretérito_perfectivo_II"
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # ###passado_volitivo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # # futuro
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'futuro', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # # subjuntivo_conjuntivo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_ir('ir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # # imperativo_I
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # # # imperativo_II
# # #
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # # # não_finito_concretizado
# # #
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ir('ir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # # infinitivo
# # # print(formacao_verbo_ir('ir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # # #
# # # # # # # gerúndio
# # # print(formacao_verbo_ir('ir', 'gerúndio', '-IR', None, None, None))
# # # # # #
# # # # # # # particípio
# # # # generos = ['masculino', 'feminino']
# # # for numero in OI_numeros:
# # # 	for genero in generos:
# # # 		print(formacao_verbo_ir('ir', 'particípio', '-IR', numero, genero, None))
#
#
# # VERBOS VIR E INTERVIR
#
#
# def formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                 OI_numero, genero, OI_tipo_de_pessoa,
#                                 padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     ME = experiencia_do_verbo(verbo)
#
#     if tipo_de_orientacao == 'infinitivo':
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero,
#                                                    OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'inha'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'inha'
#                 else:
#                     MI = 'inhas'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'inha'
#                 else:
#                     MI = 'ínhamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'inha'
#                 else:
#                     MI = 'ínheis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'inha'
#                 else:
#                     MI = 'inham'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'particípio':
#         if OI_numero == 'singular':
#             if genero == 'masculino':
#                 MI = 'indo'
#             else:
#                 MI = 'inda'
#         else:
#             if genero == 'masculino':
#                 MI = 'indos'
#             else:
#                 MI = 'indas'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'enho'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if verbo == 'vir':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'em'
#                     else:
#                         MI = 'ens'
#                     verbo = ME + MI
#                 else:
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'ém'
#                     else:
#                         MI = 'éns'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if verbo == 'vir':
#                     MI = 'em'
#                 else:
#                     MI = 'ém'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'imos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'indes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'em'
#                 else:
#                     MI = 'êm'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'im'
#                 verbo = ME + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eio'
#                 else:
#                     MI = 'ieste'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'eio'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eio'
#                 else:
#                     MI = 'iemos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'iestes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'eio'
#                 else:
#                     MI = 'ieram'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'iera'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iera'
#                 else:
#                     MI = 'ieras'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iera'
#                 else:
#                     MI = 'iéramos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iera'
#                 else:
#                     MI = 'iéreis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iera'
#                 else:
#                     MI = 'ieram'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'iesse'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iesse'
#                 else:
#                     MI = 'iesses'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iesse'
#                 else:
#                     MI = 'iéssemos'
#                 verbo = ME + '' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'iésseis'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'iesse'
#                 else:
#                     MI = 'iessem'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'enha'
#                 else:
#                     MI = 'enhas'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'enha'
#                 else:
#                     MI = 'enhamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'enha'
#                 else:
#                     MI = 'enhais'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'enha'
#                 else:
#                     MI = 'enham'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if verbo == 'vir':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'a'
#                         verbo = ME + 'enh' + MI
#                     else:
#                         MI = 'em'
#                         verbo = ME + MI
#                 else:
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'a'
#                         verbo = ME + 'enh' + MI
#                     else:
#                         MI = 'ém'
#                         verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'enhamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'inde'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'enh' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             if OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'enh' + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#                 verbo = verbo = ME + 'enh' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = verbo = ME + 'enh' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'ier'
#                 verbo = ME + MI
#
#             if OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ier'
#                 else:
#                     MI = 'ieres'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ier'
#                 else:
#                     MI = 'iermos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ier'
#                 else:
#                     MI = 'ierdes'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ier'
#                 else:
#                     MI = 'ierem'
#                 verbo = ME + MI
#     return verbo
#
#
# #
# # # #
# # # # # ##TESTE intervir
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'presente', '-IR', numero, None, tipo_pessoa))
# #
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'futuro', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('intervir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# #
# # # # # infinitivo
# # print(formacao_verbo_vir_intervir('intervir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # #
# # # # # # # gerúndio
# # print(formacao_verbo_vir_intervir('intervir', 'gerúndio', '-IR', None, None, None))
# # # # # #
# # # # # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_vir_intervir('intervir', 'particípio', '-IR', numero, genero, None))
# #
# # ######################################
# #
# #
# # # # # ##TESTE vir
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # #presente
# # # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'presente', '-IR', numero, None, tipo_pessoa))
# #
# # # # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'pretérito_perfectivo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'pretérito_imperfectivo', '-IR', numero, None, tipo_pessoa))
# # # #
# # # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'pretérito_perfectivo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'passado_volitivo', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'futuro', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_conjuntivo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_condicional', '-IR', numero, None, tipo_pessoa))
# #
# # # # # subjuntivo_optativo
# # # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'subjuntivo_optativo', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'imperativo_I', '-IR', numero, None, tipo_pessoa))
# # #
# # # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'imperativo_II', '-IR', numero, None, tipo_pessoa))
# #
# # # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_vir_intervir('vir', 'não_finito_concretizado', '-IR', numero, None, tipo_pessoa))
# #
# # # # # infinitivo
# # print(formacao_verbo_vir_intervir('vir', 'infinitivo', '-IR', numero, 'feminino', None))
# # # #
# # # # # # # gerúndio
# # print(formacao_verbo_vir_intervir('vir', 'gerúndio', '-IR', None, None, None))
# # # # # #
# # # # # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_vir_intervir('vir', 'particípio', '-IR', numero, genero, None))
#
#
# # VERBO HAVER
# def formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                          OI_numero, genero, OI_tipo_de_pessoa,
#                          padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#
#     if tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = 'ido'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             ME = verbo[slice(-4)]
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ei'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'á'
#                 else:
#                     MI = 'ás'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'á'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)]
#                     MI = 'á'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'emos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     ME = verbo[slice(-4)]
#                     MI = 'á'
#                 else:
#                     ME = experiencia_do_verbo(verbo)
#                     MI = 'eis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'ão'
#
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'e'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                 else:
#                     MI = 'este'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'e'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                 else:
#                     MI = 'emos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                 else:
#                     MI = 'estes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'e'
#                 else:
#                     MI = 'eram'
#
#         verbo = ME + 'ouv' + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'era'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'udera'
#                 else:
#                     MI = 'eras'
#
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'era'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'era'
#                 else:
#                     MI = 'éramos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'era'
#                 else:
#                     MI = 'éreis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'era'
#                 else:
#                     MI = 'eram'
#         verbo = ME + 'ouv' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '2pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 ME = verbo[slice(-4)]
#                 MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#                 verbo = ME + 'ouv' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                     verbo = ME + 'ud' + MI
#                 else:
#                     MI = 'éssemos'
#                     verbo = ME + 'ouv' + MI
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'ésseis'
#                 verbo = ME + 'ouv' + MI
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#                 verbo = ME + 'ouv' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 ME = verbo[slice(-4)]
#                 MI = 'a'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#             verbo = ME + 'aj' + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'aj' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + 'aj' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'aj' + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero,
#                                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'aj' + MI
#                 else:
#                     MI = 'á'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'a'
#                 verbo = ME + 'aj' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'aj' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'ei'
#                 verbo = ME + 'av' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'aj' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#                 verbo = ME + 'aj' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'a'
#                 verbo = ME + 'aj' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + MI
#                 else:
#                     MI = 'amos'
#                     verbo = ME + 'aj' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#                 verbo = ME + 'aj' + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'aj' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'er'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'eres'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'ermos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erdes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erem'
#         verbo = ME + 'ouv' + MI
#
#     return verbo
#
#
# # # # # # ##TESTE haver
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # # ###
# # # # # # #presente
# # # # print("A conjugação é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'presente', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # ###
# # # # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'futuro', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # subjuntivo_optativo
# # # # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_haver('haver', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # infinitivo
# # print(formacao_verbo_haver('haver', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # #
# # # # # # # # gerúndio
# # print(formacao_verbo_haver('haver', 'gerúndio', '-ER', None, None, None))
# # # # # # #
# # # # # # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_haver('haver', 'particípio', '-ER', numero, genero, None))
#
# # VERBO PODER
#
# def formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                          OI_numero, genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     if tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,
#                                                          OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'presente':
#
#         if OI_tipo_de_pessoa == '1pessoa' and OI_numero == 'singular':
#             ME = verbo[slice(-3)]
#             MI = realizacao_transitoriedade_presente(padrao_de_morfologia,
#                                                      OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             verbo = ME + 'ss' + MI
#
#
#         else:
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_presente(padrao_de_morfologia,
#                                                      OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'ude'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ôde'
#                 else:
#                     MI = 'udeste'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'ôde'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ôde'
#                 else:
#                     MI = 'udemos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ôde'
#                 else:
#                     MI = 'udestes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ôde'
#                 else:
#                     MI = 'uderam'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'udera'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'udera'
#                 else:
#                     MI = 'uderas'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'udera'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'udera'
#                 else:
#                     MI = 'udéramos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'udera'
#                 else:
#                     MI = 'udéreis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'udera'
#                 else:
#                     MI = 'uderam'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '2pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                        OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#                 verbo = ME + 'ud' + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '3pessoa':
#                 MI = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, OI_numero,
#                                                                        OI_tipo_de_pessoa,
#                                                                        padrao_pessoa_morfologia)
#                 verbo = ME + 'ud' + MI
#
#             elif OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'éssemos'
#                 verbo = ME + 'ud' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'esse'
#                 else:
#                     MI = 'ésseis'
#                 verbo = ME + 'ud' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-4)]
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'ossa'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossas'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossamos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossais'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossam'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ode'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'ossa'
#                 verbo = ME + MI
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'odei'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = ('Imperativos não selecionam 1pessoa do singular')
#
#             if OI_tipo_de_pessoa == '2pessoa':
#
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossas'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'ossa'
#                 verbo = ME + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossamos'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossais'
#                 verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ossa'
#                 else:
#                     MI = 'ossam'
#                 verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = verbo[slice(-4)]
#         MI = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia,
#                                                             OI_numero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + 'ud' + MI
#
#     return verbo
#
#
# # # # # ##TESTE poder
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # ###
# # # # # # #presente
# # # # print("A conjugação é:")
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'presente', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # ###
# # # # print("A conjugação pretérito_perfectivo_I é:")
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # # #
# # # # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # # futuro
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'futuro', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # subjuntivo_optativo
# # # # # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_poder('poder', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # infinitivo
# # print(formacao_verbo_poder('poder', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # # #
# # # # # # # # # gerúndio
# # print(formacao_verbo_poder('poder', 'gerúndio', '-ER', None, None, None))
# # # # # # # #
# # # # # # # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_poder('poder', 'particípio', '-ER', numero, genero, None))
# #
#
#
# # VERBO FAZER
#
#
# def formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#
#     if tipo_de_orientacao == 'presente':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-3)]
#                 MI = 'ço'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = ''
#                 else:
#                     MI = 'es'
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'az'
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = 'emos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'azeis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'azem'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_I':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'iz'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ez'
#                 else:
#                     MI = 'izeste'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'ez'
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ez'
#                 else:
#                     MI = 'izemos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ez'
#                 else:
#                     MI = 'izestes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ez'
#                 else:
#                     MI = 'izeram'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_perfectivo_II':
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'izera'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izera'
#                 else:
#                     MI = 'izeras'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 MI = 'izera'
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izera'
#                 else:
#                     MI = 'izéramos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izera'
#                 else:
#                     MI = 'izéreis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 ME = verbo[slice(-4)]
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'ivera'
#                 else:
#                     MI = 'izeram'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'pretérito_imperfectivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
#                                                                OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'futuro':
#         ME = verbo[slice(-3)]
#         MI = \
#             realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                               padrao_pessoa_morfologia)[
#                 slice(1, 7)]
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'passado_volitivo':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'aria'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'aria'
#                 else:
#                     MI = 'arias'
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'aria'
#
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'aríamos'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 MI = 'aríeis'
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'ariam'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_condicional':
#         ME = verbo[slice(-4)]
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'izesse'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izesse'
#                 else:
#                     MI = 'izesses'
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izesse'
#                 else:
#                     MI = 'izéssemos'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izesse'
#                 else:
#                     MI = 'izésseis'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'izesse'
#                 else:
#                     MI = 'izessem'
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
#         ME = verbo[slice(-3)]
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'a'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'as'
#
#             elif OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 MI = 'amos'
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'ais'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#         verbo = ME + 'ç' + MI
#
#     elif tipo_de_orientacao == 'subjuntivo_optativo':
#         ME = verbo[slice(-4)]
#
#         if OI_numero == 'singular':
#             if (OI_tipo_de_pessoa == '1pessoa' or
#                     OI_tipo_de_pessoa == '3pessoa'):
#                 MI = 'er'
#             if OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'eres'
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'ermos'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erdes'
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'er'
#                 else:
#                     MI = 'erem'
#         verbo = ME + 'iz' + MI
#
#     elif tipo_de_orientacao == 'imperativo_I':
#         ME = verbo[slice(-3)]
#         if OI_numero == 'singular':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 verbo = 'Imperativos não selecionam 1pessoa do singular.'
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'ç' + MI
#                 else:
#                     MI = 'z'
#                     verbo = ME + MI
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 MI = 'a'
#                 verbo = ME + 'ç' + MI
#         elif OI_numero == 'plural':
#             if OI_tipo_de_pessoa == '1pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'amos'
#                 verbo = ME + 'ç' + MI
#
#             elif OI_tipo_de_pessoa == '2pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                     verbo = ME + 'ç' + MI
#                 else:
#                     MI = 'ei'
#                     verbo = ME + 'z' + MI
#
#
#             elif OI_tipo_de_pessoa == '3pessoa':
#                 if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                     MI = 'a'
#                 else:
#                     MI = 'am'
#                 verbo = ME + 'ç' + MI
#
#     elif tipo_de_orientacao == 'imperativo_II':
#         if tipo_de_orientacao == 'imperativo_II':
#             ME = verbo[slice(-3)]
#             if OI_numero == 'singular':
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     verbo = 'Imperativos não selecionam 1pessoa do singular. Selecione novamente:'
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'a'
#                     else:
#                         MI = 'as'
#                     verbo = ME + 'ç' + MI
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     MI = 'a'
#                     verbo = ME + 'ç' + MI
#
#             elif OI_numero == 'plural':
#
#                 if OI_tipo_de_pessoa == '1pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'a'
#                     else:
#                         MI = 'amos'
#                     verbo = ME + 'ç' + MI
#
#                 elif OI_tipo_de_pessoa == '2pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'a'
#                     else:
#                         MI = 'ais'
#                     verbo = ME + 'ç' + MI
#
#                 elif OI_tipo_de_pessoa == '3pessoa':
#                     if padrao_pessoa_morfologia == '3pessoa_do_singular':
#                         MI = 'a'
#                     else:
#                         MI = 'am'
#                     verbo = ME + 'ç' + MI
#
#     elif tipo_de_orientacao == 'não_finito_concretizado':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'infinitivo':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'gerúndio':
#         ME = experiencia_do_verbo(verbo)
#         MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
#         verbo = ME + MI
#
#     elif tipo_de_orientacao == 'particípio':
#         ME = verbo[slice(-4)]
#         if OI_numero == 'singular':
#             if genero == 'feminino':
#                 MI = 'eita'
#             elif genero == 'masculino':
#                 MI = 'eito'
#         elif OI_numero == 'plural':
#             if genero == 'feminino':
#                 MI = 'eitas'
#             elif genero == 'masculino':
#                 MI = 'eitos'
#         verbo = ME + MI
#     return verbo
#
#
# # #
# # #
# # # # # # # ##TESTE fazer
# # OI_numeros = ['singular', "plural"]
# # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # # # ###
# # # # # # # #presente
# # # # # print("A conjugação é:")
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'presente', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # ###
# # # # # print("A conjugação pretérito_perfectivo_I é:")
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # # # #####pretérito_imperfectivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # # # # # #
# # # # # # # ### "pretérito_perfectivo_II"
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # # # # ###passado_volitivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # # # futuro
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'futuro', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # subjuntivo_conjuntivo
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # # # #
# # # # # # # subjuntivo_condicional
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # # subjuntivo_optativo
# # # # # # #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # # #
# # # # # # # # imperativo_I
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # # # # # imperativo_II
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # # não_finito_concretizado
# #
# # for numero in OI_numeros:
# # 	for tipo_pessoa in OI_tipo_pessoas:
# # 		print(formacao_verbo_fazer('fazer', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# #
# # # # # # # # infinitivo
# # print(formacao_verbo_fazer('fazer', 'infinitivo', '-ER', numero, 'feminino', None))
# # # # # #
# # # # # # # # # # gerúndio
# # print(formacao_verbo_fazer('fazer', 'gerúndio', '-ER', None, None, None))
# # # # # # # # #
# # # # # # # # # # particípio
# # generos = ['masculino', 'feminino']
# # for numero in OI_numeros:
# # 	for genero in generos:
# # 		print(formacao_verbo_fazer('fazer', 'particípio', '-ER', numero, genero, None))
# #
#
# #################################################################################
#
# def formacao_da_estrutura_do_verbo_modal(TIPO_DE_EXPERIENCIA, verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                          OI_numero,
#                                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#
#     if (TIPO_DE_EXPERIENCIA == 'Ser' or
#             TIPO_DE_EXPERIENCIA == 'Fazer' or
#             TIPO_DE_EXPERIENCIA == 'Sentir'):
#
#         if verbo == 'dever':
#             ME = experiencia_do_verbo(verbo)
#             MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
#                                                      OI_tipo_de_pessoa, padrao_pessoa_morfologia="Morfologia_padrão")
#             verbo = ME + MI
#
#         elif verbo == 'poder':
#             verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                          OI_numero, genero, OI_tipo_de_pessoa,
#                                          padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'haver':
#             verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                          OI_numero, genero, OI_tipo_de_pessoa,
#                                          padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'ter':
#
#             verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                        OI_numero, genero, OI_tipo_de_pessoa,
#                                        padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
#     # elif verbo == 'ter de':
#     # 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#     # 	                           OI_numero, genero, OI_tipo_de_pessoa,
#     # 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
#     return verbo
#
#
# # formacao_da_estrutura_do_verbo_modal('Sentir','poder','presente','-ER','singular',None,'1pessoa')
#
# def formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
#                                        genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     padrao_de_morfologia = detecta_padrao_morfologia(verbo)
#     if verbo == 'estar':
#         verbo = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                      genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif verbo == 'ter':
#         verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                    genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif verbo == 'haver':
#         verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                      genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif verbo == 'ir':
#         verbo = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif verbo == 'vir':
#         verbo = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                             genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     elif verbo == 'ser':
#         verbo = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                    genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#
#     return verbo
#
#
# #
# # formacao_da_estrutura_do_verbo_AUX('estar','presente','singular',None,'1pessoa')
# # formacao_da_estrutura_do_verbo_AUX('ser','presente','singular',None,'1pessoa','Morfologia_padrão')
#
# def formacao_verbo_participio(verbo, tipo_de_orientacao, OI_numero,
#                               genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
#     ME = experiencia_do_verbo(verbo)
#     padrao_de_morfologia = detecta_padrao_morfologia(verbo)
#     MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero)
#     verbo_participio = ME + MI
#
#     return verbo_participio
#
#
# # #
# # formacao_verbo_participio("cortar",'particípio','singular','masculino',None)
#
#
# def formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
#                                    genero, OI_tipo_de_pessoa,
#                                    padrao_pessoa_morfologia='Morfologia_padrão'):
#     '''
#     '''
#     padrao_de_morfologia = detecta_padrao_morfologia(verbo)
#     if (tipo_de_orientacao == 'imperativo_I' and OI_numero == 'singular' and OI_tipo_de_pessoa == '1pessoa' or
#             tipo_de_orientacao == 'imperativo_II' and OI_numero == 'singular' and OI_tipo_de_pessoa == '1pessoa'):
#         verbo_conj = '-'
#     else:
#         if verbo == 'estar':
#             verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                               OI_numero,
#                                               genero, OI_tipo_de_pessoa,
#                                               padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'ter':
#             verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                             OI_numero,
#                                             genero, OI_tipo_de_pessoa,
#                                             padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'haver':
#             verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                               OI_numero,
#                                               genero, OI_tipo_de_pessoa,
#                                               padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'ir':
#             verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                            OI_numero,
#                                            genero, OI_tipo_de_pessoa,
#                                            padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'vir':
#             verbo_conj = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                      OI_numero,
#                                                      genero, OI_tipo_de_pessoa,
#                                                      padrao_pessoa_morfologia='Morfologia_padrão')
#
#         elif verbo == 'ser':
#             verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                             OI_numero,
#                                             genero, OI_tipo_de_pessoa,
#                                             padrao_pessoa_morfologia='Morfologia_padrão')
#         elif verbo[-5:] == 'fazer':
#             verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                               OI_numero, genero, OI_tipo_de_pessoa,
#                                               padrao_pessoa_morfologia)
#
#         elif verbo == None:
#             verbo_conj = ''
#         else:
#
#             OE_experiencia_do_verbo = experiencia_do_verbo(verbo)
#             OI_orientacao_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo(tipo_de_orientacao,
#                                                                                       padrao_de_morfologia,
#                                                                                       OI_numero,
#                                                                                       genero, OI_tipo_de_pessoa,
#                                                                                       padrao_pessoa_morfologia)
#             verbo_conj = OE_experiencia_do_verbo + OI_orientacao_interpessoal_do_verbo
#     return verbo_conj
#
#
# #
# # formacao_da_estrutura_do_verbo('andar','imperativo_I','singular',None,'3pessoa')
# # formacao_da_estrutura_do_verbo('comer','pretérito_imperfectivo','plural',None,'1pessoa')
# # formacao_da_estrutura_do_verbo('expor','presente','singular',None,'1pessoa')
# # formacao_da_estrutura_do_verbo('expor','gerúndio',None,None,None)
# # formacao_da_estrutura_do_verbo('cortar', 'particípio',  'singular', 'feminino', None)
# # verbo = formacao_verbo_sentir('sentir', 'subjuntivo_conjuntivo', '-IR', 'plural',
# # 								  None, '1pessoa')
#
# def verbo_geral(TIPO_DE_EXPERIENCIA=None, funcao_no_grupo_verbal=None, verbo=None,
#                 tipo_de_orientacao=None, OI_numero=None, genero=None, OI_tipo_de_pessoa=None,
#                 padrao_pessoa_morfologia="Morfologia_padrão"):
#     '''(str)->str
#     Retorna a estrutura que realiza os verbos no português.
#     '''
#     classe_do_verbo = def_classe_de_verbo(funcao_no_grupo_verbal)
#     padrao_de_morfologia = detecta_padrao_morfologia(verbo)
#     if classe_do_verbo == 'lexical':
#         if (TIPO_DE_EXPERIENCIA == 'Ser' or
#                 TIPO_DE_EXPERIENCIA == 'Fazer' or
#                 TIPO_DE_EXPERIENCIA == 'Sentir'):
#             if verbo == 'estar':
#                 verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                                   genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             elif verbo == 'sentir':
#                 verbo_conj = formacao_verbo_sentir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                                    genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             elif verbo == 'trazer':
#                 verbo_conj = formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                                    genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             elif verbo == 'ter':
#                 verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                 OI_numero, genero, OI_tipo_de_pessoa,
#                                                 padrao_pessoa_morfologia)
#             elif verbo == 'ser':
#                 verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
#                                                 OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             elif verbo == 'ir':
#                 verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                                genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#             elif verbo == 'haver':
#                 verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                   OI_numero, genero, OI_tipo_de_pessoa,
#                                                   padrao_pessoa_morfologia)
#             elif verbo == 'agredir':
#                 verbo_conj = formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                     OI_numero, genero, OI_tipo_de_pessoa,
#                                                     padrao_pessoa_morfologia)
#             elif verbo == 'aferir':
#                 verbo_conj = formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                    OI_numero, genero, OI_tipo_de_pessoa,
#                                                    padrao_pessoa_morfologia)
#             elif verbo == 'medir':
#                 verbo_conj = formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                   OI_numero, genero, OI_tipo_de_pessoa,
#                                                   padrao_pessoa_morfologia)
#             elif verbo == 'saber':
#                 verbo_conj = formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                   OI_numero, genero, OI_tipo_de_pessoa,
#                                                   padrao_pessoa_morfologia)
#             elif (verbo == 'vir' or verbo == 'intervir'):
#                 verbo_conj = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                          OI_numero, genero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#             elif (verbo == 'conter' or verbo == 'deter'):
#                 verbo_conj = formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                          OI_numero, genero, OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia)
#             elif verbo == 'poder':
#                 verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                   OI_numero, genero, OI_tipo_de_pessoa,
#                                                   padrao_pessoa_morfologia)
#             elif verbo == 'possuir':
#                 verbo_conj = formacao_verbo_possuir(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                     OI_numero, genero, OI_tipo_de_pessoa,
#                                                     padrao_pessoa_morfologia)
#
#             else:
#                 if verbo[-4:] == 'ruir':
#
#                     verbo_conj = formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                      OI_numero, genero, OI_tipo_de_pessoa,
#                                                      padrao_pessoa_morfologia)
#
#                 elif verbo[-3:] == 'car':
#                     verbo_conj = formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                     OI_numero, genero, OI_tipo_de_pessoa,
#                                                     padrao_pessoa_morfologia)
#                 elif verbo[-5:] == 'fazer':
#                     verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                       OI_numero, genero, OI_tipo_de_pessoa,
#                                                       padrao_pessoa_morfologia)
#                 elif verbo[-3:] == 'gar':
#                     verbo_conj = formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                     OI_numero, genero, OI_tipo_de_pessoa,
#                                                     padrao_pessoa_morfologia)
#                 elif verbo[-3:] == 'çar':
#                     verbo_conj = formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                     OI_numero, genero, OI_tipo_de_pessoa,
#                                                     padrao_pessoa_morfologia)
#
#                 elif verbo[-3:] == 'cer':
#                     verbo_conj = formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                     OI_numero, genero, OI_tipo_de_pessoa,
#                                                     padrao_pessoa_morfologia)
#
#                 elif verbo[-5:] == 'dizer':
#                     verbo_conj = formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
#                                                       genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
#                 else:
#                     verbo_conj = formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
#                                                                 genero, OI_tipo_de_pessoa,
#                                                                 padrao_pessoa_morfologia)
#     elif classe_do_verbo == 'modal':
#         if (TIPO_DE_EXPERIENCIA == 'Ser' or
#                 TIPO_DE_EXPERIENCIA == 'Fazer' or
#                 TIPO_DE_EXPERIENCIA == 'Sentir'):
#
#             if verbo == 'dever':
#                 ME = experiencia_do_verbo(verbo)
#                 MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
#                                                          OI_tipo_de_pessoa,
#                                                          padrao_pessoa_morfologia="Morfologia_padrão")
#                 verbo_conj = ME + MI
#
#             elif verbo == 'poder':
#                 verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                   OI_numero, genero, OI_tipo_de_pessoa,
#                                                   padrao_pessoa_morfologia='Morfologia_padrão')
#
#             elif verbo == 'haver':
#                 verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                   OI_numero, genero, OI_tipo_de_pessoa,
#                                                   padrao_pessoa_morfologia='Morfologia_padrão')
#
#             elif verbo == 'ter':
#
#                 verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#                                                 OI_numero, genero, OI_tipo_de_pessoa,
#                                                 padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
#     # elif verbo == 'ter de':
#     # 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
#     # 	                           OI_numero, genero, OI_tipo_de_pessoa,
#     # 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
#     elif classe_do_verbo == 'auxiliar':
#         verbo_conj = formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
#                                                         genero, OI_tipo_de_pessoa,
#                                                         padrao_pessoa_morfologia)
#     else:
#         verbo_conj = ''
#     return verbo_conj


if __name__ == "__main__":
    pass

