from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_morfema.morf_verbais import *
import argparse
# import sys
# sys.path.append('../../..')


def preposicao(indice: int = None) -> str:
    """
    Retorna preposição dado um índice entre 0 e 16
    :param indice:
    :return: preposição
    """
    opcoes = ['a', 'ante', 'após', 'até', 'com', 'contra',
              'de', 'desde', 'em', 'entre', 'para', 'por', 'perante', 'sem',
              'sob', 'sobre', 'trás']
    try:
        nums = [x for x in range(len(opcoes))]
        preposicoes = dict(zip(nums, opcoes))
        prep = preposicoes[indice]
        return prep
    except (ValueError, KeyError):
        return ''


# print("Com ou sem contração")
# contracao = choice.Menu(['+contração', '-contração']).ask()


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
    except ValueError:
        return ''


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
                me = verbo[slice(-2)]

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'ç'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if (oi_tipo_de_pessoa == '3pessoa' or
                    oi_tipo_de_pessoa == '1pessoa'):
                me = verbo[slice(-3)] + 'ç'
            else:
                me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-3)] + 'ç'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except ValueError:
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
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'c'
            else:
                me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'c'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if oi_tipo_de_pessoa == '2pessoa':
                me = verbo[slice(-2)]
            else:
                me = verbo[slice(-3)] + 'c'
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-3)] + 'c'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except ValueError:
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
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'qu'
            else:
                me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'qu'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-3)] + 'qu'
                elif oi_tipo_de_pessoa == '1pessoa':
                    me = ''
                else:
                    me = verbo[slice(-2)]
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '3pessoa' or oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-3)] + 'qu'
                else:
                    me = verbo[slice(-2)]
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
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except ValueError:
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
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                     oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'gu'
            else:
                me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'gu'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_I':
            if (oi_tipo_de_pessoa == '3pessoa' or
                    oi_tipo_de_pessoa == '1pessoa'):
                me = verbo[slice(-3)] + 'gu'
            else:
                me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-3)] + 'gu'
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                          oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except ValueError:
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
                    me = verbo[slice(-2)]
                    mi = 'o'
                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'i'
                    else:
                        mi = 'is'
                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-2)]
                    mi = 'i'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-2)]
                        mi = 'i'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'ímos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'ís'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-2)]
                        mi = 'i'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'em'
        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
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
            me = verbo[slice(-2)]
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
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)
            mi = ''.join(('í', mi[1:]))

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            mi = ''.join(('í', mi[1:]))

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
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
                        me = verbo[slice(-2)]
                        mi = 'a'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'i'

                else:
                    me = verbo[slice(-2)]
                    mi = 'a'

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-2)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
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
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except ValueError:
        return ''


# VERBOS TERMINADOS EM : 'RUIR'


def formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                        genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """
    Ex.:


    >>> formacao_verbo_RUIR('construir', 'presente', 'IR','plural' ,None, '3pessoa')
    'constroem'

    >>> formacao_verbo_RUIR('usufruir', 'presente', 'IR','plural' ,None, '3pessoa')
    'usufruem'

    :param verbo:str
    :param tipo_de_orientacao:str
    :param padrao_de_morfologia:str
    :param oi_numero:str
    :param genero:
    :param oi_tipo_de_pessoa:str
    :param padrao_pessoa_morfologia:str
    :return:str verbo conjugado
    """
    me, mi = '', ''
    try:
        if verbo[-5:] == 'truir' and tipo_de_orientacao == 'presente':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-2)]
                    mi = 'o'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-3)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ói'
                    else:
                        mi = 'óis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-3)]
                    mi = 'ói'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-3)]
                        mi = 'ói'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'ímos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'ís'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-3)]
                        mi = 'ói'
                    else:
                        me = ''.join((verbo[slice(-3)], 'o'))
                        mi = 'em'

        elif verbo[-4:] == 'ruir' and tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-2)]
                    mi = 'o'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'i'
                    else:
                        mi = 'is'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-2)]
                    mi = 'i'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-2)]
                        mi = 'i'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'ímos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'ís'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-2)]
                        mi = 'i'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'em'
        elif verbo[-5:] == 'truir' and tipo_de_orientacao == 'imperativo_I':
            if oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)]
                mi = 'ói'
            elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
                me = verbo[slice(-2)]
                mi = 'í'
            else:
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)
        elif verbo[-4:] == 'ruir' and tipo_de_orientacao == 'imperativo_I':
            if oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
                me = verbo[slice(-1)]
                mi = ''
            elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
                me = verbo[slice(-2)]
                mi = 'í'
            else:
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif (verbo[-5:] == 'truir' or
              verbo[-4:] == 'ruir'):
            if tipo_de_orientacao == 'pretérito_imperfectivo':
                me = verbo[slice(-2)]
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
                me = verbo[slice(-2)]
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
                me = verbo[slice(-2)]
                mi = ''.join(
                    ('í', realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                             oi_tipo_de_pessoa)[1:]))

            elif tipo_de_orientacao == 'subjuntivo_condicional':
                me = verbo[slice(-2)]
                mi = ''.join(('í', realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)[1:]))

            elif tipo_de_orientacao == 'subjuntivo_optativo':
                me = verbo[slice(-2)]
                if (oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' or
                        oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'):
                    mi = ''.join(
                        ('í', (realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                              oi_tipo_de_pessoa,
                                                                              padrao_pessoa_morfologia)[1:])))
                else:
                    mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                        oi_tipo_de_pessoa,
                                                                        padrao_pessoa_morfologia)

            elif tipo_de_orientacao == 'passado_volitivo':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                                 oi_tipo_de_pessoa, padrao_pessoa_morfologia)

            elif tipo_de_orientacao == 'pretérito_imperfectivo':
                me = verbo[slice(-2)]
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
                            mi = 'ímos'

                    elif oi_tipo_de_pessoa == '2pessoa':
                        mi = 'íeis'

                    elif oi_tipo_de_pessoa == '3pessoa':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'ía'
                        else:
                            mi = 'íam'

            elif tipo_de_orientacao == 'não_finito_concretizado':
                me = verbo[slice(-2)]
                if (oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' or
                        oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'):
                    mi = ''.join(
                        ('í', (realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia,
                                                                                  oi_numero,
                                                                                  oi_tipo_de_pessoa,
                                                                                  padrao_pessoa_morfologia)[
                               1:])))
                else:
                    mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                            oi_tipo_de_pessoa,
                                                                            padrao_pessoa_morfologia)

            elif tipo_de_orientacao == 'futuro':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                       oi_tipo_de_pessoa, padrao_pessoa_morfologia)

            elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                      oi_tipo_de_pessoa,
                                                                      padrao_pessoa_morfologia)

            elif tipo_de_orientacao == 'imperativo_II':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)

            elif tipo_de_orientacao == 'gerúndio':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

            elif tipo_de_orientacao == 'particípio':
                me = verbo[slice(-2)]
                mi = ''.join(
                    ("í", realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)[1:]))

            elif tipo_de_orientacao == 'infinitivo':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))
    except ValueError:
        return ''

# formacao_verbo_RUIR('construir', 'subjuntivo_condicional', 'IR','plural' ,None, '3pessoa')
# formacao_verbo_RUIR('usufruir', 'subjuntivo_condicional', 'IR','plural' ,None, '3pessoa')
# # VERBO agredir

def formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                           genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """
    Ex.:
    >>> formacao_verbo_agredir('agredir', 'presente', 'IR', 'singular', None, '3pessoa')
    'agride'
    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:verbo conjugado
    """

    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)] + 'id'
                    mi = 'o'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)] + 'id'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'es'
                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)] + 'id'
                    mi = 'e'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-4)] + 'id'
                        mi = 'e'
                    else:
                        me = experiencia_do_verbo(verbo)
                        mi = 'imos'
                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'is'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-4)] + 'id'
                        mi = 'e'
                    else:
                        me = verbo[slice(-4)] + 'id'
                        mi = 'em'

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            if oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
                mi = 'iam'
            else:
                mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                       oi_tipo_de_pessoa,
                                                                       padrao_pessoa_morfologia)

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
            me = verbo[slice(-4)] + 'id'
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
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-4)] + "ir"
                        mi = 'a'
                    else:
                        me = verbo[slice(-4)] + "id"
                        mi = 'e'
                else:
                    me = verbo[slice(-4)] + "id"
                    mi = 'a'

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)] + 'id'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'i'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)] + 'id'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'

                    else:
                        mi = 'am'

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa':
                print('Imperativos não selecionam 1pessoa do singular')
            else:
                me = verbo[slice(-4)] + 'id'
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

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
    except ValueError:
        return ''


# # VERBO aferir


def formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                          genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)] + 'ir'
                    mi = 'o'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'es'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-2)]
                    mi = 'e'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-2)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'imos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'is'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-2)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'em'

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            if oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
                mi = 'iam'
            else:
                mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                       oi_tipo_de_pessoa,
                                                                       padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-4)] + 'ir'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-4)] + "ir"
                        mi = 'a'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'e'
                else:
                    me = verbo[slice(-4)] + "ir"
                    mi = 'a'

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)] + 'ir'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'i'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)] + 'ir'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa':
                print('Imperativos não selecionam 1pessoa do singular')
            else:
                me = verbo[slice(-4)] + 'ir'
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]

            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]

            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
        return ''.join((me, mi))
    except ValueError:
        return ''


# VERBO MEDIR
def formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                         genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:

    >>> formacao_verbo_medir('medir', 'presente', 'IR', 'plural', None, '3pessoa')
    'medem'
    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:verbo conjugado
    """
    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-3)] + 'ç'
                    mi = 'o'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'es'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'e'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'imos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'is'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'em'

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

        if tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'ç'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)
        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        if tipo_de_orientacao == 'imperativo_I':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-3)] + "ç"
                        mi = 'a'

                    else:
                        me = experiencia_do_verbo(verbo)
                        mi = 'e'
                else:
                    me = verbo[slice(-3)] + "ç"
                    mi = 'a'

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-3)] + 'ç'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = 'i'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-3)] + 'ç'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa':
                print('Imperativos não selecionam 1pessoa do singular')
            else:
                me = verbo[slice(-3)] + 'ç'
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        return ''.join((me, mi))
    except ValueError:
        return ''


#
# # ##TESTES
#
# OIs = ['presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
#        'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
#        'não_finito_concretizado', 'imperativo_I', 'imperativo_II']
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# generos = ['masculino', 'feminino']
#
# # TESTE GERAL:
#
# print('Conjugação geral:')
# for oi in OIs:
#     print("### ", oi, ' ###')
#     for num in OI_numeros:
#         for pessoa in OI_tipo_pessoas:
#             print(formacao_verbo_medir('medir', oi, 'IR', num, None, pessoa))
# # teste individual
# for num in OI_numeros:
#     for pessoa in OI_tipo_pessoas:
#         print(formacao_verbo_medir('medir', oi, 'IR', num, None, pessoa))
# # infinitivo
# formacao_verbo_medir('medir', 'infinitivo', 'IR', None, None, None)
#
# # gerúndio
# print(formacao_verbo_medir('medir', 'gerúndio', 'IR', None, None, None))
# #
# # # particípio
# for numero in OI_numeros:
#     for genero in generos:
#         print(formacao_verbo_medir('medir', 'particípio', 'IR', numero, genero, None))

#
# VERBO sentir


def formacao_verbo_sentir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                          genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:

    >>> formacao_verbo_sentir('sentir', 'gerúndio', 'IR', None, None, None)
    'sentindo'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:verbo conjugado
    """
    me, mi = '', ''
    try:
        if tipo_de_orientacao == 'presente':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-5)] + 'int'
                    mi = 'o'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'

                    else:
                        mi = 'es'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-2)]
                    mi = 'e'
            elif oi_numero == 'plural':
                me = verbo[slice(-2)]
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'

                    else:
                        mi = 'imos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'is'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'

                    else:
                        mi = 'em'

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        if tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-5)] + 'int'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_I':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-5)] + "int"
                        mi = 'a'

                    else:
                        me = verbo[slice(-2)]
                        mi = 'e'

                else:
                    me = verbo[slice(-4)] + "int"
                    mi = 'a'

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)] + 'int'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'

                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'i'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-5)] + 'int'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'

                    else:
                        mi = 'am'

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa':
                print('Imperativos não selecionam 1pessoa do singular')
            else:
                me = verbo[slice(-5)] + 'int'
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        return ''.join((me, mi))
    except ValueError:
        return ''


# # VERBO SABER
def formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                         genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:

    >>> formacao_verbo_saber('saber', 'pretérito_imperfectivo', 'ER', 'singular', None, '3pessoa')
    'sabia'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:verbo conjugado
    """

    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'infinitivo':
            verbo_conj = verbo

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi
        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi
        #
        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)

            verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'presente':

            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-4)]
                mi = 'ei'
                verbo_conj = me + mi

            elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
                me = experiencia_do_verbo(verbo)

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    mi = 'e'
                    verbo_conj = me + mi

                else:
                    mi = 'es'
                    verbo_conj = me + mi

            elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
                me = experiencia_do_verbo(verbo)
                mi = 'e'
                verbo_conj = me + mi

            elif oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    me = experiencia_do_verbo(verbo)
                    mi = 'e'
                    verbo_conj = me + mi

                else:
                    me = experiencia_do_verbo(verbo)
                    mi = 'emos'
                    verbo_conj = me + mi

            elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
                me = experiencia_do_verbo(verbo)
                mi = 'eis'
                verbo_conj = me + mi

            elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    me = experiencia_do_verbo(verbo)
                    mi = 'e'
                    verbo_conj = me + mi

                else:
                    me = experiencia_do_verbo(verbo)
                    mi = 'em'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'oube'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oube'
                        verbo_conj = me + mi

                    else:
                        mi = 'oubeste'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    mi = 'oube'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oube'
                        verbo_conj = me + mi
                    else:
                        mi = 'oubemos'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    mi = 'oubestes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oube'
                    else:
                        mi = 'ouberam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' or oi_tipo_de_pessoa == '3pessoa':
                    mi = 'oubera'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubera'
                        verbo_conj = me + mi

                    else:
                        mi = 'ouberas'
                        verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubera'
                        verbo_conj = me + mi
                    else:
                        mi = 'oubéramos'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubera'
                        verbo_conj = me + mi

                    else:
                        mi = 'oubéreis'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubera'

                    else:
                        mi = 'ouberam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_condicional':

            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' or oi_tipo_de_pessoa == '3pessoa':
                    mi = 'oubesse'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubesse'
                    else:
                        mi = 'oubesses'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubesse'
                    else:
                        mi = 'oubésssemos'

                #
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubesse'

                    else:
                        mi = 'oubésseis'

                #
                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oubesse'
                    else:
                        mi = 'oubessem'
                verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-4)] + 'aib'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-4)] + 'oub'
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi
        #
        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-4)] + 'oub'
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_I':

            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + "aib" + mi
                    else:
                        mi = 'e'
                        verbo_conj = me + 'ab' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'aib' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'aib' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ei'
                    verbo_conj = me + 'ab' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'aib' + mi

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa':
                print('Imperativos não selecionam 1pessoa do singular')
            else:
                me = verbo[slice(-3)] + 'ib'
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)
                verbo_conj = me + mi

        return verbo_conj
    except ValueError:
        return ''


# # VERBO ESTAR

def formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                         genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_estar('estar', 'presente', 'AR', 'singular',None, '2pessoa')
    'estás'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    verbo_conj, me = '', experiencia_do_verbo(verbo)

    try:
        if tipo_de_orientacao == 'subjuntivo_condicional':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' or oi_tipo_de_pessoa == '3pessoa':

                    mi = 'esse'
                    verbo_conj = me + 'iv' + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'esses'
                    verbo_conj = me + 'iv' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'éssemos'
                    verbo_conj = me + 'iv' + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'ésseis'
                    verbo_conj = me + 'iv' + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'essem'
                    verbo_conj = me + 'iv' + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' or oi_tipo_de_pessoa == '3pessoa':

                    mi = 'a'
                    verbo_conj = me + 'ej' + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'ej' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'ej' + mi
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'ej' + mi
                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'ej' + mi

        elif tipo_de_orientacao == 'imperativo_I':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'ej' + mi
                    else:
                        mi = 'á'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'ej' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'ej' + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ai'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'ej' + mi

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'ej' + mi
                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'ej' + mi
            if oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'ej' + mi
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'ej' + mi
                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'ej' + mi

        elif tipo_de_orientacao == 'subjuntivo_optativo':

            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' or oi_tipo_de_pessoa == '3pessoa':
                    mi = 'er'
                    verbo_conj = me + 'iv' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'eres'
                    verbo_conj = me + 'iv' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'ermos'
                    verbo_conj = me + 'iv' + mi

                if oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erdes'
                    verbo_conj = me + 'iv' + mi
                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erem'
                    verbo_conj = me + 'iv' + mi
        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi
        elif tipo_de_orientacao == 'futuro':
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi
        elif tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':

                    mi = 'ou'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ás'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'á'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '2pessoa'):

                    mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    mi = 'ão'
                    verbo_conj = me + mi
        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':

                    mi = 'ive'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'iveste'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    mi = 'eve'
                    verbo_conj = me + mi
            if oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'ivemos'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'ivestes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'iveram'
                    verbo_conj = me + mi
        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            if oi_numero == 'singular':

                if oi_tipo_de_pessoa == '1pessoa':

                    mi = 'ivera'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'iveras'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '3pessoa':

                    mi = 'ivera'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'ivéramos'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'ivéreis'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'iveram'

                    verbo_conj = me + mi
        elif tipo_de_orientacao == 'não_finito_concretizado':

            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'infinitivo':

            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'gerúndio':

            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi
        elif tipo_de_orientacao == 'particípio':

            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi

        return verbo_conj
    except ValueError:
        return ''


# # VERBO DIZER

def formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                         genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_dizer('dizer', 'pretérito_imperfectivo', 'ER', 'singular',None, '2pessoa')
    'dizias'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':

                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-3)]
                    mi = 'go'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = ''
                        verbo_conj = me + mi

                    else:
                        mi = 'es'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = experiencia_do_verbo(verbo)
                    mi = ''
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = ''
                        verbo_conj = me + mi

                    else:
                        mi = 'emos'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = ''
                        verbo_conj = me + mi

                    else:
                        mi = 'eis'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = experiencia_do_verbo(verbo)

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = ''
                        verbo_conj = me + mi

                    else:
                        mi = 'em'
                        verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    mi = 'isse'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == "3pessoa_do_singular":
                        mi = 'isse'
                        verbo_conj = me + mi

                    else:
                        mi = 'isseste'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'isse'
                    verbo_conj = me + mi

            elif oi_tipo_de_pessoa == '1pessoa':
                me = verbo[slice(-4)]
                if padrao_pessoa_morfologia == "3pessoa_do_singular":
                    mi = 'isse'
                    verbo_conj = me + mi

                else:
                    mi = 'issemos'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == "3pessoa_do_singular":
                        mi = 'isse'
                        verbo_conj = me + mi

                    else:
                        mi = 'issestes'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == "3pessoa_do_singular":
                        mi = 'isse'
                        verbo_conj = me + mi
                    else:
                        mi = 'isseram'
                        verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'ia'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ia'

                    else:
                        mi = 'ias'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'íamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ia'
                    else:
                        mi = 'íeis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ia'
                    else:
                        mi = 'iam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    mi = 'issera'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issera'
                        verbo_conj = me + mi

                    else:
                        mi = 'isseras'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'issera'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issera'
                        verbo_conj = me + mi

                    else:
                        mi = 'isséramos'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issera'
                        verbo_conj = me + mi

                    else:
                        mi = 'isséreis'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issera'
                    else:
                        mi = 'isseram'

                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'iria'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iria'
                    else:
                        mi = 'irias'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iria'
                    else:
                        mi = 'iríamos'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iria'
                    else:
                        mi = 'iríeis'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iria'
                    else:
                        mi = 'iriam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-3)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi[1:]
        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'issesse'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issesse'
                    else:
                        mi = 'issesses'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issesse'
                        verbo_conj = me + mi

                    else:
                        mi = 'isséssemos'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issesse'
                    else:
                        mi = 'issésseis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'issesse'
                    else:
                        mi = 'issessem'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)]
            if oi_numero == 'singular':

                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):

                    mi = 'a'
                    verbo_conj = me + 'g' + mi

                elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'g' + mi
                    else:
                        mi = 'as'
                        verbo_conj = me + 'g' + mi
            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'g' + mi
                    else:
                        mi = 'amos'
                        verbo_conj = me + 'g' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'g' + mi
                    else:
                        mi = 'ais'
                        verbo_conj = me + 'g' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'g' + mi
                    else:
                        mi = 'am'
                        verbo_conj = me + 'g' + mi

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_I':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':

                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'
                        verbo_conj = me + mi
                    else:
                        mi = 'iz'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'iga'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'
                    else:
                        mi = 'igamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'izei'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'
                    else:
                        mi = 'igam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'
                    else:
                        mi = 'igas'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'iga'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'

                    else:
                        mi = 'igamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'

                    else:
                        mi = 'igais'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iga'

                    else:
                        mi = 'igam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    me = verbo[slice(-4)]
                    mi = 'er'
                    verbo_conj = me + 'iss' + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'

                    else:
                        mi = 'eres'
                    verbo_conj = me + 'iss' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'

                    else:
                        mi = 'ermos'
                    verbo_conj = me + 'iss' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erdes'
                    verbo_conj = me + 'iss' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'

                    else:
                        mi = 'erem'
                    verbo_conj = me + 'iss' + mi
        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi
        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if genero == 'masculino':
                    mi = 'ito'
                else:
                    mi = 'ita'
            else:
                if genero == 'masculino':
                    mi = 'itos'
                else:
                    mi = 'itas'

            verbo_conj = me + mi
        return verbo_conj
    except ValueError:
        return ''


# VERBO TER
def formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                       oi_numero, genero, oi_tipo_de_pessoa,
                       padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_ter('ter','pretérito_imperfectivo', 'ER', 'singular',None, '2pessoa')
    'tinhas'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conugado
    """
    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-2)]

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'esse'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'esses'
                verbo_conj = me + 'iv' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'éssemos'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'ésseis'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'essem'
                verbo_conj = me + 'iv' + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-2)]

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'a'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                verbo_conj = me + 'enh' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                verbo_conj = me + 'enh' + mi
        ###
        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'imperativo_I':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'enh' + mi
                    else:
                        mi = 'em'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'enh' + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ende'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'enh' + mi
        ###
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                    print('Imperativos não selecionam 1pessoa do singular')
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'enh' + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-2)] + 'iv'
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'er'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'eres'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'ermos'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erdes'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erem'
                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'a'
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                verbo_conj = me + 'inh' + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'inh' + mi
                    else:
                        mi = 'amos'
                        verbo_conj = me + 'ính' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'inh' + mi
                    else:
                        mi = 'eis'
                        verbo_conj = me + 'ính' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'inh' + mi
                    else:
                        mi = 'am'
                        verbo_conj = me + 'inh' + mi
        ###
        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'presente':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'enho'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'ens'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'em'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'emos'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'endes'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'êm'

                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ive'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'iveste'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'eve'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'ivemos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'ivestes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'iveram'
                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ivera'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'iveras'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'ivera'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'ivéramos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'ivéreis'

                elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'iveram'
                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi

        return verbo_conj
    except ValueError:
        return ''


#
# OIs = ['presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
#        'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
#        'não_finito_concretizado', 'imperativo_I', 'imperativo_II']
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# generos = ['masculino', 'feminino']
#
# for num in OI_numeros:
#     for pessoa in OI_tipo_pessoas:
#         print(formacao_verbo_ter('ter', 'imperativo_II', 'ER', num, None, pessoa))


# # VERBO CONTER DETER
def formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                oi_numero, genero, oi_tipo_de_pessoa,
                                padrao_pessoa_morfologia='Morfologia_padrão') -> str:
    """
    Ex.:
    >>> formacao_verbo_conter_deter('deter', 'subjuntivo_conjuntivo', 'ER','singular', None, '2pessoa')
    'detenhas'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'subjuntivo_condicional':
            me = experiencia_do_verbo(verbo)

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'esse'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'esses'
                verbo_conj = me + 'iv' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'éssemos'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'ésseis'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'essem'
                verbo_conj = me + 'iv' + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = experiencia_do_verbo(verbo)

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'a'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                verbo_conj = me + 'enh' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                verbo_conj = me + 'enh' + mi
        ###
        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'imperativo_I':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')
                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'enh' + mi
                    else:
                        mi = 'em'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'enh' + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ende'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'enh' + mi
        ###
        elif tipo_de_orientacao == 'imperativo_II':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                    print('Imperativos não selecionam 1pessoa do singular')
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'enh' + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'iver'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iver'
                    else:
                        mi = 'iveres'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iver'
                    else:
                        mi = 'ivermos'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iver'
                    else:
                        mi = 'iverdes'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iver'
                    else:
                        mi = 'iverem'
                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = experiencia_do_verbo(verbo)

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'a'
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                verbo_conj = me + 'inh' + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'inh' + mi
                    else:
                        mi = 'amos'
                        verbo_conj = me + 'ính' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'inh' + mi
                    else:
                        mi = 'eis'
                        verbo_conj = me + 'ính' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'inh' + mi
                    else:
                        mi = 'am'
                        verbo_conj = me + 'inh' + mi
        ###
        elif tipo_de_orientacao == 'futuro':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'passado_volitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'presente':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'enho'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'éns'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'em'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'emos'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'endes'

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'êm'

                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ive'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'iveste'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'eve'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'ivemos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'ivestes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eve'
                    else:
                        mi = 'iveram'
                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = experiencia_do_verbo(verbo)
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ivera'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'iveras'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'ivera'
                verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'ivéramos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'ivéreis'

                elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'iveram'
                verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'infinitivo':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'gerúndio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'particípio':
            me = experiencia_do_verbo(verbo)
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi

        return verbo_conj
    except ValueError:
        return ''


# ###VERBO TRAZER

def formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                          genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_trazer('trazer', 'subjuntivo_conjuntivo', 'ER','singular', None, '2pessoa')
    'tragas'

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

            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)] + 'g'
                mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            else:
                if oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
                    me = verbo[slice(-2)]
                    mi = ''
                else:
                    me = verbo[slice(-2)]
                    mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-4)] + 'oux'
            if (oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                    oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
                mi = 'e'
            else:
                mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero,
                                                                       oi_tipo_de_pessoa,
                                                                       padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-4)] + 'oux'
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'era'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'eras'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'era'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'éramos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'éreis'

                elif oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'eram'

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-3)] + 'r'
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-3)] + 'r'
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero,
                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)[2:]

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)] + 'g'
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-4)] + 'oux'
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-4)] + 'oux'
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero,
                                                                oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_I':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                print('Imperativos não selecionam 1 pessoa do singular')
            elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
                me = verbo[slice(-2)]
                mi = ''
            elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
                me = verbo[slice(-2)]
                mi = 'ei'
            else:
                me = verbo[slice(-3)] + 'g'
                mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                return ''
            else:
                me = verbo[slice(-3)] + 'g'
                mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero,
                                                              oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        return ''.join((me, mi))

    except ValueError:
        return ''


# # VERBO SER

def formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero, genero, oi_tipo_de_pessoa,
                       padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_ser('ser', 'presente', 'ER','singular', None, '1pessoa')
    'sou'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:
    """
    verbo_conj = ''
    try:
        if tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            if oi_numero == 'singular':
                me = 'er'
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'a'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':

                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = 'er'
                        mi = 'a'
                    else:
                        me = 'ér'
                        mi = 'amos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = 'er'
                        mi = 'a'
                    else:
                        me = 'ér'
                        mi = 'eis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'er'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]

            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-2)]
                    mi = 'ou'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = ''
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'é'
                    else:
                        mi = 'és'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = ''
                    mi = 'é'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = ''
                        mi = 'é'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'omos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    mi = 'ois'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = ''
                        mi = 'é'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'ão'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_I':

            me = 'f'
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ui'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                    else:
                        mi = 'oste'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'oi'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                        verbo_conj = me + mi
                    else:
                        mi = 'omos'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ostes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                    else:
                        mi = 'oram'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = 'f'
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'ora'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'oras'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'ôramos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'ôreis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'oram'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_condicional':

            me = 'f'
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'osse'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'osses'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'ôssemos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'ôsseis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'ossem'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero,
                                                                  oi_tipo_de_pessoa,
                                                                  padrao_pessoa_morfologia="Morfologia_padrão")
            verbo_conj = me + 'ej' + mi
        ###
        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = 'f'
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'or'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'ores'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'ormos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'ordes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'orem'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'imperativo_I':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'ej' + mi
                    else:
                        mi = 'ê'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'ej' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'ej' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'ede'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'ej' + mi
        ###
        elif tipo_de_orientacao == 'imperativo_II':
            me = verbo[slice(-2)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'ej' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'ej' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'ej' + mi

                elif oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
                    mi = 'ais'
                    verbo_conj = me + 'ej' + mi

                elif oi_tipo_de_pessoa == '3pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'ej' + mi

        return verbo_conj
    except ValueError:
        return ''


# # VERBO IR


def formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                      genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_ir('ir', 'presente', 'IR','singular', None, '1pessoa')
    'vou'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    verbo_conj = ''
    try:
        if tipo_de_orientacao == 'infinitivo':
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = mi
        ###
        elif tipo_de_orientacao == 'pretérito_imperfectivo':

            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = mi
        ###
        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'v'
                    mi = 'ou'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ai'
                    else:
                        mi = 'ais'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'v'
                    mi = 'ai'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ai'
                    else:
                        mi = 'amos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'i'
                    mi = 'des'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ai'
                    else:
                        mi = 'ão'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'f'
                    mi = 'ui'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                    else:
                        mi = 'oste'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'f'
                    mi = 'oi'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                    else:
                        mi = 'omos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                    else:
                        mi = 'ostes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'f'

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'oi'
                    else:
                        mi = 'oram'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    me = 'f'
                    mi = 'ora'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'oras'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'ôramos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'ôreis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'f'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ora'
                    else:
                        mi = 'oram'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = 'f'
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'osse'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'osses'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'ôssemos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'ôsseis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'osse'
                    else:
                        mi = 'ossem'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    me = 'v'
                    mi = 'á'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ás'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'amos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ades'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ão'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia,
                                                                    oi_numero, oi_tipo_de_pessoa)
            verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ai'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'v'
                    mi = 'á'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'amos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = 'i'
                    mi = 'de'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = 'v'
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ão'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'imperativo_II':
            me = 'v'
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                if oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ás'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'á'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'amos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ades'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ão'
                    verbo_conj = me + mi
        ###
        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = 'f'
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'or'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'ores'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'ormos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'ordes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'or'
                    else:
                        mi = 'orem'
                    verbo_conj = me + mi

        return verbo_conj
    except ValueError:
        return ''


# # VERBOS VIR E INTERVIR

def formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                oi_numero, genero, oi_tipo_de_pessoa,
                                padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_vir_intervir('vir', 'passado_volitivo', 'IR','singular', None, '1pessoa')
    'venho'
    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, verbo_conj = verbo[slice(-2)], ''
    try:
        if tipo_de_orientacao == 'infinitivo':
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'inha'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'inha'
                    else:
                        mi = 'inhas'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'inha'
                    else:
                        mi = 'ínhamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'inha'
                    else:
                        mi = 'ínheis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'inha'
                    else:
                        mi = 'inham'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'futuro':
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'gerúndio':
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'particípio':
            if oi_numero == 'singular':
                if genero == 'masculino':
                    mi = 'indo'
                else:
                    mi = 'inda'
            else:
                if genero == 'masculino':
                    mi = 'indos'
                else:
                    mi = 'indas'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'enho'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if verbo == 'vir':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'em'
                        else:
                            mi = 'ens'
                        verbo_conj = me + mi
                    else:
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'ém'
                        else:
                            mi = 'éns'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if verbo == 'vir':
                        mi = 'em'
                    else:
                        mi = 'ém'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'imos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'indes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'em'
                    else:
                        mi = 'êm'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'im'
                    verbo_conj = me + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eio'
                    else:
                        mi = 'ieste'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'eio'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eio'
                    else:
                        mi = 'iemos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'iestes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'eio'
                    else:
                        mi = 'ieram'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'iera'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iera'
                    else:
                        mi = 'ieras'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iera'
                    else:
                        mi = 'iéramos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iera'
                    else:
                        mi = 'iéreis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iera'
                    else:
                        mi = 'ieram'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'iesse'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iesse'
                    else:
                        mi = 'iesses'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iesse'
                    else:
                        mi = 'iéssemos'
                    verbo_conj = me + '' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'iésseis'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'iesse'
                    else:
                        mi = 'iessem'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'enha'
                    else:
                        mi = 'enhas'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'enha'
                    else:
                        mi = 'enhamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'enha'
                    else:
                        mi = 'enhais'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'enha'
                    else:
                        mi = 'enham'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'não_finito_concretizado':
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if verbo == 'vir':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'a'
                            verbo_conj = me + 'enh' + mi
                        else:
                            mi = 'em'
                            verbo_conj = me + mi
                    else:
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'a'
                            verbo_conj = me + 'enh' + mi
                        else:
                            mi = 'ém'
                            verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'enhamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'inde'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'enh' + mi

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                if oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'enh' + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'enh' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'enh' + mi

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'ier'
                    verbo_conj = me + mi

                if oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ier'
                    else:
                        mi = 'ieres'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ier'
                    else:
                        mi = 'iermos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ier'
                    else:
                        mi = 'ierdes'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ier'
                    else:
                        mi = 'ierem'
                    verbo_conj = me + mi
        return verbo_conj
    except ValueError:
        return ''


# # VERBO HAVER
def formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                         oi_numero, genero, oi_tipo_de_pessoa,
                         padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_haver('haver', 'presente', 'ER','singular', None, '1pessoa')
    'hei'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                me = verbo[slice(-4)]
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ei'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'á'
                    else:
                        mi = 'ás'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'á'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-4)]
                        mi = 'á'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'emos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        me = verbo[slice(-4)]
                        mi = 'á'
                    else:
                        me = verbo[slice(-2)]
                        mi = 'eis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'ão'

            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    mi = 'e'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'este'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'e'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'emos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'estes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'eram'

            verbo_conj = me + 'ouv' + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    mi = 'era'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'udera'
                    else:
                        mi = 'eras'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'era'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'éramos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'éreis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'era'
                    else:
                        mi = 'eram'
            verbo_conj = me + 'ouv' + mi

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '2pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    me = verbo[slice(-4)]
                    mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                           oi_tipo_de_pessoa,
                                                                           padrao_pessoa_morfologia)
                    verbo_conj = me + 'ouv' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                        verbo_conj = me + 'ud' + mi
                    else:
                        mi = 'éssemos'
                        verbo_conj = me + 'ouv' + mi
                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'ésseis'
                    verbo_conj = me + 'ouv' + mi
                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                           oi_tipo_de_pessoa,
                                                                           padrao_pessoa_morfologia)
                    verbo_conj = me + 'ouv' + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    me = verbo[slice(-4)]
                    mi = 'a'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                verbo_conj = me + 'aj' + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'aj' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'aj' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'aj' + mi

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'aj' + mi
                    else:
                        mi = 'á'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'a'
                    verbo_conj = me + 'aj' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'aj' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    mi = 'ei'
                    verbo_conj = me + 'av' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'aj' + mi

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'
                    verbo_conj = me + 'aj' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'a'
                    verbo_conj = me + 'aj' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + mi
                    else:
                        mi = 'amos'
                        verbo_conj = me + 'aj' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'
                    verbo_conj = me + 'aj' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'aj' + mi

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'er'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'eres'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'ermos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erdes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erem'
            verbo_conj = me + 'ouv' + mi

        return verbo_conj
    except ValueError:
        return ''


# # VERBO PODER

def formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                         oi_numero, genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_poder('poder', 'presente', 'ER','singular', None, '1pessoa')
    'posso'
    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero,
                                                             oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'presente':

            if oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
                me = verbo[slice(-3)]
                mi = realizacao_transitoriedade_presente(padrao_de_morfologia,
                                                         oi_numero, oi_tipo_de_pessoa,
                                                         padrao_pessoa_morfologia)
                verbo_conj = me + 'ss' + mi

            else:
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_presente(padrao_de_morfologia,
                                                         oi_numero, oi_tipo_de_pessoa,
                                                         padrao_pessoa_morfologia)
                verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'ude'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ôde'
                    else:
                        mi = 'udeste'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'ôde'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ôde'
                    else:
                        mi = 'udemos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ôde'
                    else:
                        mi = 'udestes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ôde'
                    else:
                        mi = 'uderam'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'udera'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'udera'
                    else:
                        mi = 'uderas'

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'udera'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'udera'
                    else:
                        mi = 'udéramos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'udera'
                    else:
                        mi = 'udéreis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'udera'
                    else:
                        mi = 'uderam'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '2pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                           oi_tipo_de_pessoa,
                                                                           padrao_pessoa_morfologia)
                    verbo_conj = me + 'ud' + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '3pessoa':
                    mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero,
                                                                           oi_tipo_de_pessoa,
                                                                           padrao_pessoa_morfologia)
                    verbo_conj = me + 'ud' + mi

                elif oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'éssemos'
                    verbo_conj = me + 'ud' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'esse'
                    else:
                        mi = 'ésseis'
                    verbo_conj = me + 'ud' + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-4)]

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'ossa'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossas'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossamos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossais'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossam'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_I':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ode'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'ossa'
                    verbo_conj = me + mi

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'odei'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'imperativo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    print('Imperativos não selecionam 1pessoa do singular')

                if oi_tipo_de_pessoa == '2pessoa':

                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossas'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'ossa'
                    verbo_conj = me + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossamos'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossais'
                    verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ossa'
                    else:
                        mi = 'ossam'
                    verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-4)]
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia,
                                                                oi_numero, oi_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)
            verbo_conj = me + 'ud' + mi

        return verbo_conj
    except ValueError:
        return ''


# # VERBO FAZER

def formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                         genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_verbo_fazer('fazer', 'presente', 'ER','singular', None, '1pessoa')
    'faço'

    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo conjugado
    """
    me, mi, verbo_conj = '', '', ''
    try:
        if tipo_de_orientacao == 'presente':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-3)]
                    mi = 'ço'
                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-2)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = ''
                    else:
                        mi = 'es'
                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'az'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-2)]
                    mi = 'emos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    mi = 'azeis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'azem'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    mi = 'iz'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ez'
                    else:
                        mi = 'izeste'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'ez'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ez'
                    else:
                        mi = 'izemos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ez'
                    else:
                        mi = 'izestes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ez'
                    else:
                        mi = 'izeram'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    mi = 'izera'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izera'
                    else:
                        mi = 'izeras'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    mi = 'izera'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izera'
                    else:
                        mi = 'izéramos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izera'
                    else:
                        mi = 'izéreis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    me = verbo[slice(-4)]
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'ivera'
                    else:
                        mi = 'izeram'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero,
                                                                   oi_tipo_de_pessoa, padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'futuro':
            me = verbo[slice(-3)]
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)[slice(1, 7)]
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'passado_volitivo':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'aria'
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'aria'
                    else:
                        mi = 'arias'
                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'aria'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'aríamos'
                elif oi_tipo_de_pessoa == '2pessoa':
                    mi = 'aríeis'
                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'ariam'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            me = verbo[slice(-4)]

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'izesse'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izesse'
                    else:
                        mi = 'izesses'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izesse'
                    else:
                        mi = 'izéssemos'
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izesse'
                    else:
                        mi = 'izésseis'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'izesse'
                    else:
                        mi = 'izessem'
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            me = verbo[slice(-3)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa' or oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'as'

                elif oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'

            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    mi = 'amos'
                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'ais'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
            verbo_conj = me + 'ç' + mi

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            me = verbo[slice(-4)]

            if oi_numero == 'singular':
                if (oi_tipo_de_pessoa == '1pessoa' or
                        oi_tipo_de_pessoa == '3pessoa'):
                    mi = 'er'
                if oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'eres'
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'ermos'

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erdes'

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'er'
                    else:
                        mi = 'erem'
            verbo_conj = me + 'iz' + mi

        elif tipo_de_orientacao == 'imperativo_I':
            me = verbo[slice(-3)]
            if oi_numero == 'singular':
                if oi_tipo_de_pessoa == '1pessoa':
                    verbo_conj = 'Imperativos não selecionam 1pessoa do singular.'

                elif oi_tipo_de_pessoa == '2pessoa':

                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'ç' + mi
                    else:
                        mi = 'z'
                        verbo_conj = me + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    mi = 'a'
                    verbo_conj = me + 'ç' + mi
            elif oi_numero == 'plural':
                if oi_tipo_de_pessoa == '1pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'amos'
                    verbo_conj = me + 'ç' + mi

                elif oi_tipo_de_pessoa == '2pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                        verbo_conj = me + 'ç' + mi
                    else:
                        mi = 'ei'
                        verbo_conj = me + 'z' + mi

                elif oi_tipo_de_pessoa == '3pessoa':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'am'
                    verbo_conj = me + 'ç' + mi

        elif tipo_de_orientacao == 'imperativo_II':
            if tipo_de_orientacao == 'imperativo_II':
                me = verbo[slice(-3)]
                if oi_numero == 'singular':
                    if oi_tipo_de_pessoa == '1pessoa':
                        verbo_conj = 'Imperativos não selecionam 1pessoa do singular. Selecione novamente:'
                    elif oi_tipo_de_pessoa == '2pessoa':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'a'
                        else:
                            mi = 'as'
                        verbo_conj = me + 'ç' + mi

                    elif oi_tipo_de_pessoa == '3pessoa':
                        mi = 'a'
                        verbo_conj = me + 'ç' + mi

                elif oi_numero == 'plural':

                    if oi_tipo_de_pessoa == '1pessoa':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'a'
                        else:
                            mi = 'amos'
                        verbo_conj = me + 'ç' + mi

                    elif oi_tipo_de_pessoa == '2pessoa':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'a'
                        else:
                            mi = 'ais'
                        verbo_conj = me + 'ç' + mi

                    elif oi_tipo_de_pessoa == '3pessoa':
                        if padrao_pessoa_morfologia == '3pessoa_do_singular':
                            mi = 'a'
                        else:
                            mi = 'am'
                        verbo_conj = me + 'ç' + mi

        elif tipo_de_orientacao == 'não_finito_concretizado':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                                    oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'infinitivo':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'gerúndio':
            me = verbo[slice(-2)]
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)
            verbo_conj = me + mi

        elif tipo_de_orientacao == 'particípio':
            me = verbo[slice(-4)]
            if oi_numero == 'singular':
                if genero == 'feminino':
                    mi = 'eita'
                elif genero == 'masculino':
                    mi = 'eito'
            elif oi_numero == 'plural':
                if genero == 'feminino':
                    mi = 'eitas'
                elif genero == 'masculino':
                    mi = 'eitos'
            verbo_conj = me + mi
        return verbo_conj
    except ValueError:
        return ''


def formacao_da_estrutura_do_verbo_modal(tipo_de_experiencia, verbo, tipo_de_orientacao, padrao_de_morfologia,
                                         oi_numero,
                                         genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_da_estrutura_do_verbo_modal('Sentir','ter','presente','ER','singular',None,'1pessoa')
    'tenho que'
    :param tipo_de_experiencia:
    :param verbo:
    :param tipo_de_orientacao:
    :param padrao_de_morfologia:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo modal conjugado
    """
    verbo_conj = ''
    try:
        if (tipo_de_experiencia == 'Ser' or
                tipo_de_experiencia == 'Fazer' or
                tipo_de_experiencia == 'Sentir'):

            if verbo == 'dever':
                me = verbo[slice(-2)]
                mi = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                         genero,
                                                         oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                verbo_conj = me + mi

            elif verbo == 'poder':
                verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                  oi_numero, genero, oi_tipo_de_pessoa,
                                                  padrao_pessoa_morfologia)

            elif verbo == 'haver':
                verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                  oi_numero, genero, oi_tipo_de_pessoa,
                                                  padrao_pessoa_morfologia)

            elif verbo == 'ter':

                verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                oi_numero, genero, oi_tipo_de_pessoa,
                                                padrao_pessoa_morfologia) + ' ' + 'que'
        # elif verbo == 'ter de':
        # 	verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
        # 	                           OI_numero, genero, OI_tipo_de_pessoa,
        # 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
        return verbo_conj
    except ValueError:
        return ''


def formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, oi_numero,
                                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_da_estrutura_do_verbo_AUX('estar','presente','singular',None,'1pessoa')

    :param verbo:
    :param tipo_de_orientacao:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return: verbo auxiliar conjugado
    """
    verbo_conj, padrao_de_morfologia = '', detecta_padrao_morfologia(verbo)
    try:
        if verbo == 'estar':
            verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                              genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif verbo == 'ter':
            verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                            genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif verbo == 'haver':
            verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                              genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif verbo == 'ir':
            verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                           genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif verbo == 'vir':
            verbo_conj = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                     genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        elif verbo == 'ser':
            verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                            genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)

        return verbo_conj
    except ValueError:
        return ''


def formacao_verbo_participio(verbo, oi_numero, genero) -> str:
    """
    Retorna verbo no particípio dado um lema verbal, número e gênero.
    Ex.:
    >>> formacao_verbo_participio("cortar",'singular','masculino')
    'cortado'

    :param verbo:
    :param oi_numero:
    :param genero:
    :return: verbo no particípio
    """
    me = verbo[slice(-2)]
    padrao_de_morfologia = detecta_padrao_morfologia(verbo)
    mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
    verbo_participio = me + mi

    return verbo_participio


def formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, oi_numero,
                                   genero, oi_tipo_de_pessoa,
                                   padrao_pessoa_morfologia='Morfologia_padrão'):
    """
    Ex.:
    >>> formacao_da_estrutura_do_verbo('andar','presente','singular',None,'3pessoa')
        'anda'

    :param verbo:
    :param tipo_de_orientacao:
    :param oi_numero:
    :param genero:
    :param oi_tipo_de_pessoa:
    :param padrao_pessoa_morfologia:
    :return:
    """
    padrao_de_morfologia = detecta_padrao_morfologia(verbo)
    try:
        if (tipo_de_orientacao == 'imperativo_I' and oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa' or
                tipo_de_orientacao == 'imperativo_II' and oi_numero == 'singular' and oi_tipo_de_pessoa == '1pessoa'):
            verbo_conj = ''
        else:
            if verbo == 'estar':
                verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                  oi_numero,
                                                  genero, oi_tipo_de_pessoa,
                                                  padrao_pessoa_morfologia)

            elif verbo == 'ter':
                verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                oi_numero,
                                                genero, oi_tipo_de_pessoa,
                                                padrao_pessoa_morfologia)

            elif verbo == 'haver':
                verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                  oi_numero,
                                                  genero, oi_tipo_de_pessoa,
                                                  padrao_pessoa_morfologia)

            elif verbo == 'ir':
                verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                               oi_numero,
                                               genero, oi_tipo_de_pessoa,
                                               padrao_pessoa_morfologia)

            elif verbo == 'vir':
                verbo_conj = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                         oi_numero,
                                                         genero, oi_tipo_de_pessoa,
                                                         padrao_pessoa_morfologia)

            elif verbo == 'ser':
                verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                oi_numero,
                                                genero, oi_tipo_de_pessoa,
                                                padrao_pessoa_morfologia)
            elif verbo[-5:] == 'fazer':
                verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                  oi_numero, genero, oi_tipo_de_pessoa,
                                                  padrao_pessoa_morfologia)

            elif verbo is None:
                verbo_conj = ''
            else:

                oe_experiencia_do_verbo = verbo[slice(-2)]
                oi_orientacao_interpessoal_do_verbo = \
                    realizacao_transitoriedade_do_verbo(tipo_de_orientacao,
                                                        padrao_de_morfologia,
                                                        oi_numero,
                                                        genero,
                                                        oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)
                verbo_conj = ''.join((oe_experiencia_do_verbo, oi_orientacao_interpessoal_do_verbo))
        return verbo_conj
    except ValueError:
        return ''


def verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, verbo,
                tipo_de_orientacao, oi_numero, genero, oi_tipo_de_pessoa,
                padrao_pessoa_morfologia="Morfologia_padrão"):
    """
    Retorna a estrutura que realiza os verbos no português.

    Ex.:
    >>> verbo_geral('Fazer','Evento','vir','passado_volitivo','singular',None,'1pessoa')
    'viria'

    :param tipo_de_experiencia:
        opções: 'Fazer','Ser', 'Sentir'
    :param funcao_no_grupo_verbal:
        opções:'Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo','Auxiliar+Núcleo', 'Modal+Núcleo'
    :param verbo: str
        lema verbal - no infinitivo
    :param tipo_de_orientacao: str
        opções: 'infinitivo','presente','pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
        'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo','subjuntivo_condicional', 'subjuntivo_optativo',
        'não_finito_concretizado','imperativo_I','imperativo_II','gerúndio', 'particípio'
    :param oi_numero:str
       escolhas: 'singular', 'plural'
    :param genero:str
        escolhas: 'feminino', 'masculino'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
       escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return verbo: str
        verbo conjugado de acordo com os parâmetros
    """
    classe_do_verbo = def_classe_de_verbo(funcao_no_grupo_verbal)
    padrao_de_morfologia = detecta_padrao_morfologia(verbo)
    verbo_conj = ''
    try:
        if classe_do_verbo == 'lexical':
            if (tipo_de_experiencia == 'Ser' or
                    tipo_de_experiencia == 'Fazer' or
                    tipo_de_experiencia == 'Sentir'):
                if verbo == 'estar':
                    verbo_conj = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                      genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                elif verbo == 'sentir':
                    verbo_conj = formacao_verbo_sentir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                elif verbo == 'trazer':
                    verbo_conj = formacao_verbo_trazer(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                       genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                elif verbo == 'ter':
                    verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                    oi_numero, genero, oi_tipo_de_pessoa,
                                                    padrao_pessoa_morfologia)
                elif verbo == 'ser':
                    verbo_conj = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero, genero,
                                                    oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                elif verbo == 'ir':
                    verbo_conj = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                   genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                elif verbo == 'haver':
                    verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                      oi_numero, genero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia)
                elif verbo == 'agredir':
                    verbo_conj = formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                        oi_numero, genero, oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)
                elif verbo == 'aferir':
                    verbo_conj = formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                       oi_numero, genero, oi_tipo_de_pessoa,
                                                       padrao_pessoa_morfologia)
                elif verbo == 'medir':
                    verbo_conj = formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                      oi_numero, genero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia)
                elif verbo == 'saber':
                    verbo_conj = formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                      oi_numero, genero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia)
                elif verbo == 'vir' or verbo == 'intervir':
                    verbo_conj = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                             oi_numero, genero, oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
                elif verbo == 'conter' or verbo == 'deter':
                    verbo_conj = formacao_verbo_conter_deter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                             oi_numero, genero, oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)
                elif verbo == 'poder':
                    verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                      oi_numero, genero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia)
                elif verbo == 'possuir':
                    verbo_conj = formacao_verbo_possuir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                        oi_numero, genero, oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)

                else:
                    if verbo[-4:] == 'ruir':

                        verbo_conj = formacao_verbo_RUIR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                         oi_numero, genero, oi_tipo_de_pessoa,
                                                         padrao_pessoa_morfologia)

                    elif verbo[-3:] == 'car':
                        verbo_conj = formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                        oi_numero, genero, oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)
                    elif verbo[-5:] == 'fazer':
                        verbo_conj = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                          oi_numero, genero, oi_tipo_de_pessoa,
                                                          padrao_pessoa_morfologia)
                    elif verbo[-3:] == 'gar':
                        verbo_conj = formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                        oi_numero, genero, oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)
                    elif verbo[-3:] == 'çar':
                        verbo_conj = formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                        oi_numero, genero, oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)

                    elif verbo[-3:] == 'cer':
                        verbo_conj = formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                        oi_numero, genero, oi_tipo_de_pessoa,
                                                        padrao_pessoa_morfologia)

                    elif verbo[-5:] == 'dizer':
                        verbo_conj = formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, oi_numero,
                                                          genero, oi_tipo_de_pessoa, padrao_pessoa_morfologia)
                    else:
                        verbo_conj = formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, oi_numero,
                                                                    genero, oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)
        elif classe_do_verbo == 'modal':
            if (tipo_de_experiencia == 'Ser' or
                    tipo_de_experiencia == 'Fazer' or
                    tipo_de_experiencia == 'Sentir'):

                if verbo == 'dever':
                    me = verbo[slice(-2)]
                    mi = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia,
                                                             oi_numero, genero,
                                                             oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia="Morfologia_padrão")
                    verbo_conj = me + mi

                elif verbo == 'poder':
                    verbo_conj = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                      oi_numero, genero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia='Morfologia_padrão')

                elif verbo == 'haver':
                    verbo_conj = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                      oi_numero, genero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia='Morfologia_padrão')

                elif verbo == 'ter':

                    verbo_conj = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                    oi_numero, genero, oi_tipo_de_pessoa,
                                                    padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
        # elif verbo == 'ter de':
        # 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
        # 	                           OI_numero, genero, OI_tipo_de_pessoa,
        # 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
        elif classe_do_verbo == 'auxiliar':
            verbo_conj = formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, oi_numero,
                                                            genero, oi_tipo_de_pessoa,
                                                            padrao_pessoa_morfologia)
        else:
            verbo_conj = ''
        return verbo_conj
    except ValueError:
        return ''


def main(tipo_de_experiencia, funcao_no_grupo_verbal, lema):
    """
    Retorna a conjugação em todas as opções e Orientação Interpessoal.
    :param tipo_de_experiencia:
    :param funcao_no_grupo_verbal:
    :param lema:
    :return:
    """
    dicionario_conjuga = {}
    participios = []
    ois = ['presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
           'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
           'não_finito_concretizado', 'imperativo_I', 'imperativo_II']
    oi_numeros = ['singular', "plural"]
    oi_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
    generos = ['masculino', 'feminino']

    # TESTE GERAL:
    try:

        dicionario_conjuga.update({lema: {}})
        for oi in ois:
            conjugacao = []
            for num in oi_numeros:
                for pessoa in oi_tipo_pessoas:
                    verbo = verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, lema, oi, num, None, pessoa)
                    conjugacao.append(verbo)
                    dicionario_conjuga[lema].update({oi: conjugacao})
        dicionario_conjuga[lema].update({'gerúndio': verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, lema,
                                                                 'gerúndio', None, None, None)})

        for numero in oi_numeros:
            for genero in generos:
                participios.append(verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, lema, 'particípio',
                                               numero, genero, None))
        dicionario_conjuga[lema].update({'participio': participios})
        return dicionario_conjuga
    except ValueError:
        return ''


def flexionar_verbo(experience='none', function_in_group='none',
                    lemma='none', person='none', gender='none', number='none',
                    mood='none', tense='none', aspect='none'):


    if number == 'Plur' or number == 'PL':
        oi_numero = 'plural'
    elif number == 'Sing' or number == 'SG':
        oi_numero = 'singular'
    else:
        oi_numero = None

    if person == '1':
        oi_tipo_de_pessoa = '1pessoa'

    elif person == '2':
        oi_tipo_de_pessoa = '2pessoa'

    elif person == '3':
        oi_tipo_de_pessoa = '3pessoa'
    else:
        oi_tipo_de_pessoa = None

    if gender == 'Masc' or gender == 'MASC':
        genero = 'masculino'

    elif gender == 'Fem' or gender == 'FEM':
        genero = 'feminino'

    else:
        genero = None

    if person == 'PRS' or person == 'NFIN':
        genero = None
        oi_tipo_de_pessoa = None
        oi_numero = None

    ####
    if (mood + '_' + tense + '_' + aspect == 'Ind_Past_Perf' or
            mood + '_' + tense + '_' + aspect == 'IND_PST_PFV'):
        tipo_de_orientacao = 'pretérito_perfectivo_I'
    elif (mood + '_' + tense + '_' + aspect == 'Ind_Past_Mais_Perf' or
          mood + '_' + tense + '_' + aspect == 'IND_PST_PRF'):
        tipo_de_orientacao = 'pretérito_perfectivo_II'
    elif (mood + '_' + tense + '_' + aspect == 'Ind_Past_Imp' or
          mood + '_' + tense + '_' + aspect == 'IND_PST_IPFV'):
        tipo_de_orientacao = 'pretérito_imperfectivo'
    elif (mood + '_' + tense + '_' + aspect == 'Ind_Fut_none' or
          mood + '_' + tense + '_' + aspect == 'IND_FUT_none'):
        tipo_de_orientacao = 'futuro'
    elif (mood + '_' + tense + '_' + aspect == 'Ind_Pres_none' or
          mood + '_' + tense + '_' + aspect == 'IND_PRS_none'):
        tipo_de_orientacao = 'presente'
    elif (mood + '_' + tense + '_' + aspect == 'Sub_Pres_none' or
          mood + '_' + tense + '_' + aspect == 'SBJV_PRS_none'):
        tipo_de_orientacao = 'subjuntivo_conjuntivo'
    elif (mood + '_' + tense + '_' + aspect == 'Sub_Past_Imp' or
          mood + '_' + tense + '_' + aspect == 'SBJV_PST_IPFV'):
        tipo_de_orientacao = 'subjuntivo_condicional'
    elif (mood + '_' + tense + '_' + aspect == 'Sub_Fut_none' or
          mood + '_' + tense + '_' + aspect == 'SBJV_FUT_none'):
        tipo_de_orientacao = 'subjuntivo_optativo'
    elif (mood + '_' + tense + '_' + aspect == 'none_Past_Perf' or
          mood + '_' + tense + '_' + aspect == 'PST_none_none'):
        tipo_de_orientacao = 'particípio'
    elif (mood == 'Imp_POS_none' or
          mood + '_' + tense + '_' + aspect == 'IMP_POS_none'):
        tipo_de_orientacao = 'imperativo_I'
    elif (mood == 'Imp_NEG_none' or
          mood + '_' + tense + '_' + aspect == 'IMP_NEG_none'):
        tipo_de_orientacao = 'imperativo_II'
    elif (mood + '_' + tense + '_' + aspect == 'Cnd_Past_none' or
          mood + '_' + tense + '_' + aspect == 'COND_none_none'):
        tipo_de_orientacao = 'passado_volitivo'
    elif (mood + '_' + tense + '_' + aspect == 'none_Inf_none' or
          mood + '_' + tense + '_' + aspect == 'NFIN_none_none'):
        tipo_de_orientacao = 'não_finito_concretizado'
    elif (
            person + '_' + gender + '_' + number + '_' + mood + '_' + tense + '_' + aspect == 'none_none_none_none_Pres_Prog' or
            person + '_' + number + '_' + mood + '_' + tense + '_' + aspect == 'PRS_none_none_none_none'):
        tipo_de_orientacao = 'gerúndio'
    elif (
            person + '_' + gender + '_' + number + '_' + mood + '_' + tense + '_' + aspect == 'none_none_none_none_Inf_none' or
            person + '_' + number + '_' + mood + '_' + tense + '_' + aspect == 'NFIN_none_none_none_none'):
        tipo_de_orientacao = 'infinitivo'
    verb = verbo_geral(experience, function_in_group, lemma, tipo_de_orientacao, oi_numero, genero, oi_tipo_de_pessoa)
    return verb

#
# lemma = verbo
# person = pessoa_genero
# number = numero
# mood = modo
# tense = tempo
# aspect = aspecto
# gender = None
#
# experience = "Fazer"
# function_in_group = 'Evento'
# flexionar_verbo("Fazer", 'Evento', verbo, pessoa_genero, numero, modo, tempo, aspecto)
flexionar_verbo("Fazer", 'Evento','sorver','2',None,'PL','IMP','NEG','none')
# verbo_geral("Fazer", 'Evento','sorver','imperativo_II','plural',None,'2pessoa')
# token = 'VP[experience=Ser,function_in_group=Evento,lemma=ser,person=3,gender=none,number=Sing,mood=Ind,tense=Past,aspect=Perf]'
# #
# import re
# #
# parametros = []
# #
# text = 'tentamos fazer VP[experience=Ser,function_in_group=Evento,lemma=ser,person=3,gender=none,number=Sing,mood=Ind,tense=Past,aspect=Perf]'
# new_text = []
# tokens = text.split()
# for token in tokens:
#     if re.findall(r'VP\[',token):
#         elementos = list(token[3:-1].split(','))
#         for elemento in elementos:
#             parametro = elemento.split('=')[1]
#             parametros.append(parametro)
#         verb = flexionar_verbo(*parametros)
#         new_text.extend([verb])
#     else:
#         new_text.append(token)

# def generate(text):
#     new_text, elements, parameters, i = [], [], [], 0
#     # while i < len(text):
#     #     token = text[i]
#     tokens = text.split()
#     for token in tokens:
#         if 'VP[' in token:
#             elements = list(token[3:-1].split(','))
#             for element in elements:
#                 parameter = element.split('=')[1]
#                 parameters.append(parameter)
#             verb = flexionar_verbo(*parameters)
#             new_text.append(verb)
#         else:
#             new_text.append(token)
#     return new_text
# generate(texto)
#
#
# #
# flexionar_verbo(experience="Fazer", function_in_group='Evento', lemma="registrar", person='none', gender='none',
#                number='none', mood='none', tense='Pres', aspect='Prog')
#
# flexionar_verbo(experience="Fazer", function_in_group='Evento', lemma="registrar", person='none', gender='Masc',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
#
# flexionar_verbo(experience="Fazer", function_in_group='Evento', lemma="registrar", person='1', gender='none',
#                number='Plur', mood='none', tense='Inf', aspect='none')
#
# #
# # ######verbos exemplos para o robô
# # TEVE
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='ter', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')

# # REGISTROU
# flexionar_verbo(experience="Fazer", function_in_group='Evento', lemma="registrar", person='3', gender='none',
#                number='Sing', mood='Ind', tense='Past', aspect='Perf')
#
# # reportou
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='reportar', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
# # DIVULGOU
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='divulgar', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
# # identificou
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='identificar', person='3', gender='none',
#                number='Sing', mood='Ind', tense='Past', aspect='Perf')
# # #mostrou
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='mostrar', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
# # #foram (auxiliar)
# flexionar_verbo(experience='Ser', function_in_group='Auxiliar', lemma='ser', person='3', gender='none', number='Plur',
#                mood='Ind', tense='Past', aspect='Perf')
# # #desmatados
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='desmatar', person='none', gender='Masc',
#                number='Plur', mood='none', tense='Past', aspect='Perf')
# # #foi (EVENTO)
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='ser', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
#
# # #teve
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='ter', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
# #
# # #atingido
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='atingir', person='none', gender='Masc',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
# #
# # #foi (auxiliar)
# flexionar_verbo(experience='Ser', function_in_group='Auxiliar', lemma='ser', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
# #
# # #devastada
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='devastar', person='none', gender='Fem',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
# #
# # #devastado
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='devastar', person='none', gender='Masc',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
# # #deixa
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='deixar', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Pres', aspect='none')
# # #SOMANDO
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='somar', person='none', gender='none', number='none',
#                mood='none', tense='Pres', aspect='Prog')
# # #somam
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='somar', person='3', gender='none', number='Plur',
#                mood='Ind', tense='Pres', aspect='none')
# # soma
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='somar', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Pres', aspect='none')
# # somaram
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='somar', person='3', gender='none', number='Plur',
#                mood='Ind', tense='Past', aspect='Perf')
# # TEM
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='ter', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Pres', aspect='none')
# # acumulando
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='acumular', person='none', gender='none',
#                number='none', mood='none', tense='Pres', aspect='Prog')
#
# # #ACUMULOU
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='acumular', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
# # ACUMULA
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='acumular', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Pres', aspect='none')
# # atingindo
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='atingir', person='none', gender='none', number='none',
#                mood='none', tense='Pres', aspect='Prog')
# #
# # 'analisado'
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='analisar', person='none', gender='Masc',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
#
# # 'desmatados'
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='desmatar', person='none', gender='Masc',
#                number='Plur', mood='none', tense='Past', aspect='Perf')
#
# # 'desmatado'
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='desmatar', person='none', gender='Masc',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
#
# # 'desmatada'
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='desmatar', person='none', gender='Fem',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
# # AFETADO
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='afetar', person='none', gender='Masc',
#                number='Sing', mood='none', tense='Past', aspect='Perf')
# # GERADO
# flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='gerar', person='none', gender='Masc', number='Sing',
#                mood='none', tense='Past', aspect='Perf')
#
# # RASTREOU
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='rastrear', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')
#
# # alertou
# flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='alertar', person='3', gender='none', number='Sing',
#                mood='Ind', tense='Past', aspect='Perf')

#
# for lema in lemas_verbos:
#     dicionarioConjuga.update({lema: {}})
#     for oi in OI_INTERPESSOAIS:
#         conjugacao = []
#         for numero in OI_numeros:
#             for tipo_pessoa in OI_tipo_pessoas:
#                 verbo = verbo_geral("Fazer", 'Evento', lema, oi, numero, None, tipo_pessoa)
#                 conjugacao.append(verbo)
#                 dicionarioConjuga[lema].update({oi:conjugacao})

# main('Fazer', 'Evento', 'ser')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retorna verbo conjugado')
    parser.add_argument('tipo_experiencia', type=str)
    parser.add_argument('funcao_verbo', type=str)
    parser.add_argument('lema', type=str)
    args = parser.parse_args()

    main(args.tipo_experiencia, args.funcao_verbo, args.lema)
