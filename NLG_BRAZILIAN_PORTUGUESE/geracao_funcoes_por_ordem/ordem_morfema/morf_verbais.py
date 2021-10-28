import importlib
# import nltk
import argparse


# nltk.download('punkt')
# nltk.download('rslp')


# MESMA FUNCAO COM NLTK


def experiencia_do_verbo(verbo) -> str:
    """
        Retorna um str com o morfema experiencial (me) que realiza
        a experiência do verbo, dado um verbo lematizado
        :param verbo
        :return: morfema experiencial
        """

    # verbo = input ('Qual é o verbo lematizado?')
    me = verbo[slice(-2)]
    return me


#
# def experiencia_do_verbo2(verbo) -> str:
#     """
#     Retorna um str com o morfema experiencial (me) que realiza
#     a experiência do verbo, dado um verbo lematizado
#     :param verbo
#     :return: morfema experiencial
#     """
#     nltk_imp = importlib.import_module('nltk')
#     rad = nltk_imp.stem.RSLPStemmer()
#     return rad.stem(verbo)


# TRANSITORIEDADE

def deteccao_transitoriedade_do_verbo(verbo):
    """
    Retorna o morfema interpessoal que realiza a orientação interpessoal
    dados o verbo, seu padrão de morfologia, seu tipo_pessoa de orientação
    e o tipo_pessoa de pessoa.

    :param verbo
    :return: morfema interpessoal
    """

    me = experiencia_do_verbo(verbo)
    mi = (verbo[len(me):])
    return mi


def realizacao_transitoriedade_infinitivo(padrao_de_morfologia) -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.

    :param padrao_de_morfologia
    :return : mi

    ex.:
    >>> realizacao_transitoriedade_infinitivo('AR')
    >>> 'ar'
    """
    mi = padrao_de_morfologia.lower()

    return mi


def detecta_padrao_morfologia(verbo) -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.

    :param verbo
    :return: Padrão de morfologia do verbo
    """
    # spc_import = importlib.import_module('spacy')
    # nlp = spc_import.load("pt_core_news_lg")

    if verbo is None:
        padrao_morfologia = None
    else:
        # txt = nlp(verbo)
        # verbo = txt[0].lemma_
        me = experiencia_do_verbo(verbo)
        mi = (verbo[len(me):])
        if mi == 'ar':
            padrao_morfologia = 'AR'
        elif mi == 'er':
            padrao_morfologia = 'ER'
        elif mi == 'ir':
            padrao_morfologia = 'IR'
        elif mi == 'or':
            padrao_morfologia = 'OR'
        else:
            padrao_morfologia = None

    return padrao_morfologia


# transitoriedade (todos os tempos verbais)


def realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                        padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no presente, dados
    o padrão de morfologia, tipo de orientação, tipo de pessoa, número e o padrão pessoa_morfologia.

    ex.:
    >>>realizacao_transitoriedade_presente('AR','singular','1pessoa')
    >>>'o'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:
        if (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == "Morfologia_padrão" or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == "Morfologia_padrão" or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == "Morfologia_padrão"
        ):
            mi = 'o'

        elif (padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and
              oi_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"):
            mi = 'onho'
        elif (padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'a'
        elif (padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'as'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'
        ):
            mi = 'e'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
        ):
            mi = 'es'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'õe'
        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'ões'
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
            mi = 'a'
        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
        ):
            mi = 'e'

        elif (padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'õe'

        elif (padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'a'

        elif (padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'amos'

        elif (padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'e'

        elif (padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'emos'

        elif (padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'e'

        elif (padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'imos'

        elif (padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'õe'
        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'omos'
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'a'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ais'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'e'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'eis'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'e'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'is'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'õe'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ondes'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'a'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'am'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == '3pessoa_do_singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'
        ):
            mi = 'e'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
        ):
            mi = 'em'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'õe'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'õem'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão"
                                                      ) -> str:
    """
     Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo de orientação, tipo de pessoa e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I('AR','singular','1pessoa')
    >>>'ei'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:
        if padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == "Morfologia_padrão":
            mi = 'ei'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == "Morfologia_padrão" or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == "Morfologia_padrão"):
            mi = 'i'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == "Morfologia_padrão"):
            mi = 'us'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'aste'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'este'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'iste'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'
        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'useste'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ou'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'eu'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'iu'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ôs'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'amos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'emos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'imos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'
        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'usemos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'astes'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'estes'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'istes'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'usestes'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'aram'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'eram'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'iram'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'
        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'useram'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """

    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa e número.

    ex.:
    >>>realizacao_transitoriedade_preterito_imperfectivo('IR', 'singular', '1pessoa')
    >>>'ia'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:
        if (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'ava'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
                or padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'ia'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'unha'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ava'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'avas'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'ia'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ias'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ias'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'unha'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'unhas'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ava'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ávamos'
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'íamos'
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ia'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ia'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'íamos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'unha'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morforlogia_padrão':
            mi = 'únhamos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ava'
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'áveis'
        #
        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ia'
            else:
                mi = 'íeis'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ía'
            else:
                mi = 'íeis'
        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'unha'
            else:
                mi = 'únheis'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ava'
            else:
                mi = 'avam'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ia'
            else:
                mi = 'iam'
        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ía'
            else:
                mi = 'íam'
        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'unha'
            else:
                mi = 'unham'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero,
                                                       oi_tipo_de_pessoa):
    """

    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    ex.:
    >>>realizacao_transitoriedade_preterito_perfectivo_II('AR', 'singular','1pessoa')
    >>>'ara'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo

    """
    mi = None
    try:
        if (padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'ara'

        elif (padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'era'

        elif (padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'ira'

        elif (padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'usera'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            mi = 'aras'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            mi = 'eras'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            mi = 'iras'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            mi = 'useras'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'áramos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'êramos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'íramos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'úseramos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'áreis'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'êreis'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'íreis'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'uséreis'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'aram'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'eram'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'iram'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'useram'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """

    Retorna o morfema que realiza a transitoriedade de um verbo no passado volitivo, dados
    a o padrão de morfologia, tipo de pessoa e número.

    ex.:
    >>>realizacao_transitoriedade_passado_volitivo('AR', 'singular', '1pessoa',
        >>>padrao_pessoa_morfologia="Morfologia_padrão")
    >>>'aria'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo

    """
    mi = None
    try:
        if (padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'aria'

        elif (padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'eria'

        elif (padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'iria'

        elif (padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'oria'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'arias'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'erias'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'irias'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'orias'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'aríamos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'eríamos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'iríamos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'oríamos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'aríeis'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'eríeis'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'iríeis'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'oríeis'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'ariam'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'eriam'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'iriam'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'oriam'

        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                      padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no futuro, dados
    o padrão de morfologia, tipo de pessoa, número e padrão de pessoa_morfologia.

    ex.:
    >>>realizacao_transitoriedade_futuro('AR', 'singular', '1pessoa')
    >>>'arei'
    '''
    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:

        if padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
            mi = 'arei'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
            mi = 'erei'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
            mi = 'irei'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular':
            mi = 'orei'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ará'
            else:
                mi = 'arás'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'erá'
            else:
                mi = 'erás'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'irá'
            else:
                mi = 'irás'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'orá'
            else:
                mi = 'orás'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
            mi = 'ará'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
            mi = 'erá'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
            mi = 'irá'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
            mi = 'orá'
        #
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'aremos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'eremos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'iremos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            mi = 'oremos'
        #
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'areis'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'ereis'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'ireis'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            mi = 'oreis'
        #
        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'arão'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'erão'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'irão'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'orão'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                     padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
     Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo conjuntivo, dados
    o padrão de morfologia, tipo de pessoa, número e padrão de pessoa_morfologia.

    ex.:
    >>>realizacao_transitoriedade_subjuntivo_conjuntivo('AR', 'singular', '2pessoa',
    padrao_pessoa_morfologia="Morfologia_padrão")
    >>>'es'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
      """
    mi = None
    try:
        if (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'e'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'a'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'onha'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'e'
            else:
                mi = 'es'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular'
        ):

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'a'
            else:
                mi = 'as'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'onha'
            else:
                mi = 'onhas'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'e'
            else:
                mi = 'emos'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'
        ):
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'a'
            else:
                mi = 'amos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'onha'
            else:
                mi = 'onhamos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'e'
            else:
                mi = 'eis'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural'
        ):
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'a'
            else:
                mi = 'ais'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'onha'
            else:
                mi = 'onhais'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'e'
            else:
                mi = 'em'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'
        ):

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'a'
            else:
                mi = 'am'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'onha'
            else:
                mi = 'onham'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                      padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo condicional, dados
    o padrão de morfologia, tipo_pessoa de pessoa, e número.

    ex.:
    >>>realizacao_transitoriedade_subjuntivo_condicional('AR','singular','1pessoa')
    >>>'asse'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = ''
    try:
        if (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'asse'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'esse'

        elif (
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'isse'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'usesse'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'asse'
            else:
                mi = 'asses'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'esse'
            else:
                mi = 'esses'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'isse'
            else:
                mi = 'isses'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'usesse'
            else:
                mi = 'usesses'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'asse'
            else:
                mi = 'ássemos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'esse'
            else:
                mi = 'êssemos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'isse'
            else:
                mi = 'íssemos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'usesse'
            else:
                mi = 'uséssemos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'asse'
            else:
                mi = 'ásseis'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'esse'
            else:
                mi = 'êsseis'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'isse'
            else:
                mi = 'ísseis'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'usesse'
            else:
                mi = 'usésseis'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'asse'
            else:
                mi = 'assem'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'esse'
            else:
                mi = 'essem'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'isse'
            else:
                mi = 'íssem'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'usesse'
            else:
                mi = 'usessem'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo_optativo,
    dados  o padrão de morfologia, tipo de pessoa, número e padrão de pessoa_morfologia.

    ex.:
    >>>realizacao_transitoriedade_subjuntivo_optativo('AR','singular','2pessoa')
    >>>'ares'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """

    mi = None
    try:
        if (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'ar'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'er'

        elif (
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'ir'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'user'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'ares'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'eres'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'ires'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'user'
            else:
                mi = 'useres'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'armos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'ermos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'irmos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'user'
            else:
                mi = 'usermos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'ardes'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'erdes'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'irdes'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'user'
            else:
                mi = 'userdes'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'arem'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'erem'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'irem'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'user'
            else:
                mi = 'userem'

        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero,
                                                       oi_tipo_de_pessoa,
                                                       padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo  não_finito_concretizado,
    dados  o padrão de morfologia, tipo de pessoa, número e padrão de pessoa_morfologia.

     ex.:
    >>>realizacao_transitoriedade_nao_finito_concretizado('OR','singular','2pessoa')
    >>>'ores'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:
        if (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'ar'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'er'

        elif (
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'ir'

        elif (
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'or'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'ares'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'eres'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'ires'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'or'
            else:
                mi = 'ores'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'armos'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'ermos'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'irmos'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'or'
            else:
                mi = 'ormos'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'ardes'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'erdes'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'irdes'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'or'
            else:
                mi = 'ordes'

        elif padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ar'
            else:
                mi = 'arem'

        elif padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'er'
            else:
                mi = 'erem'

        elif padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ir'
            else:
                mi = 'irem'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'or'
            else:
                mi = 'orem'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                            padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_I,
    dados  o padrão de morfologia, tipo de pessoa, número, padrão de pessoa da morfologia.

    ex.:
    >>>realizacao_transitoriedade_imperativo_I('AR','plural','3pessoa')
    >>>'em'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:
        if oi_numero == 'singular':
            if oi_tipo_de_pessoa == '1pessoa':
                if (padrao_de_morfologia == 'AR' or
                        padrao_de_morfologia == 'ER' or
                        padrao_de_morfologia == 'IR' or
                        padrao_de_morfologia == 'OR'):
                    mi = ''

            elif oi_tipo_de_pessoa == '2pessoa':
                if padrao_de_morfologia == 'AR':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'e'
                    else:
                        mi = 'a'
                elif padrao_de_morfologia == 'ER' or padrao_de_morfologia == 'IR':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'a'
                    else:
                        mi = 'e'
                elif padrao_de_morfologia == 'OR':
                    if padrao_pessoa_morfologia == '3pessoa_do_singular':
                        mi = 'onha'
                    else:
                        mi = 'õe'
            ####
            elif oi_tipo_de_pessoa == '3pessoa':
                if padrao_de_morfologia == 'AR':
                    mi = 'e'
                elif padrao_de_morfologia == 'ER' or padrao_de_morfologia == 'IR':
                    mi = 'a'
                elif padrao_de_morfologia == 'OR':
                    mi = 'onha'
        ####
        elif oi_numero == 'plural':
            if oi_tipo_de_pessoa == '1pessoa':
                if padrao_de_morfologia == 'AR':
                    mi = 'emos'
                elif padrao_de_morfologia == 'ER' or padrao_de_morfologia == 'IR':
                    mi = 'amos'
                elif padrao_de_morfologia == 'OR':
                    mi = 'onhamos'

            elif oi_tipo_de_pessoa == '2pessoa':
                if padrao_de_morfologia == 'AR':
                    mi = 'ai'
                elif padrao_de_morfologia == 'ER':
                    mi = 'ei'
                elif padrao_de_morfologia == 'IR':
                    mi = 'i'
                elif padrao_de_morfologia == 'OR':
                    mi = 'onde'

            elif oi_tipo_de_pessoa == '3pessoa':
                if padrao_de_morfologia == 'AR':
                    mi = 'em'
                elif (padrao_de_morfologia == 'ER' or
                      padrao_de_morfologia == 'IR'):
                    mi = 'am'
                elif padrao_de_morfologia == 'OR':
                    mi = 'onham'
        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa) -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_II,
    dados  o padrão de morfologia, tipo de pessoa, e número.
     ex.:
    >>>realizacao_transitoriedade_imperativo_II('AR','plural','2pessoa')
    >>>'eis'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:

        if padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':
            mi = 'es'

        elif (
                (padrao_de_morfologia == 'ER' or 'IR')
                and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular'
        ):
            mi = 'as'

        elif (
                padrao_de_morfologia == 'OR'
                and oi_tipo_de_pessoa == '2pessoa'
                and oi_numero == 'singular'
        ):
            mi = 'onhas'

        elif (
                padrao_de_morfologia == 'AR'
                and oi_tipo_de_pessoa == '3pessoa'
                and oi_numero == 'singular'
        ):
            mi = 'e'

        elif (
                (
                        padrao_de_morfologia == 'ER' or 'IR'
                )
                and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa'
                and oi_numero == 'singular'
        ):
            mi = 'a'

        elif (
                padrao_de_morfologia == 'OR'
                and oi_tipo_de_pessoa == '3pessoa'
                and oi_numero == 'singular'
        ):
            mi = 'onha'

        elif (
                padrao_de_morfologia == 'AR'
                and oi_tipo_de_pessoa == '1pessoa'
                and oi_numero == 'plural'
        ):
            mi = 'emos'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'
        ):
            mi = 'amos'

        elif (
                padrao_de_morfologia == 'OR'
                and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'):
            mi = 'onhamos'

        elif (
                padrao_de_morfologia == 'AR'
                and oi_tipo_de_pessoa == '2pessoa'
                and oi_numero == 'plural'
        ):
            mi = 'eis'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural'
        ):
            mi = 'ais'

        elif (
                padrao_de_morfologia == 'OR'
                and oi_tipo_de_pessoa == '2pessoa'
                and oi_numero == 'plural'
        ):
            mi = 'onhais'

        elif (
                padrao_de_morfologia == 'AR'
                and oi_tipo_de_pessoa == '3pessoa'
                and oi_numero == 'plural'
        ):
            mi = 'em'

        elif (
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'
        ):
            mi = 'am'

        elif padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            mi = 'onham'

        elif (
                padrao_de_morfologia == 'AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == 'OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
        ):
            mi = ''

        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_gerundio(padrao_de_morfologia) -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no gerúndio,
    dado o padrão de morfologia.

   ex.:
   >>>realizacao_transitoriedade_gerundio('AR')
   >>>'ando'
   :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
   :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
   """
    mi = None
    try:

        if padrao_de_morfologia == 'AR':
            mi = 'ando'

        elif padrao_de_morfologia == 'ER':
            mi = 'endo'

        elif padrao_de_morfologia == 'IR':
            mi = 'indo'

        elif padrao_de_morfologia == 'OR':
            mi = 'ondo'

        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero) -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no particípio,
    dados  o padrão de morfologia, número e gênero.

    ex.:
    >>>realizacao_transitoriedade_participio('AR', 'plural', 'masculino')
    >>>'ados'

    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
       escolhas: 'singular', 'plural'
    :param genero:str
        escolhas: 'feminino', 'masculino'
    :return:mi
       Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None

    try:
        if padrao_de_morfologia == 'AR' and oi_numero == 'singular' and genero == 'feminino':
            mi = 'ada'

        elif padrao_de_morfologia == 'AR' and oi_numero == 'plural' and genero == 'feminino':
            mi = 'adas'

        elif padrao_de_morfologia == 'AR' and oi_numero == 'singular' and genero == 'masculino':
            mi = 'ado'

        elif padrao_de_morfologia == 'AR' and oi_numero == 'plural' and genero == 'masculino':
            mi = 'ados'

        elif (
                padrao_de_morfologia == 'ER' and oi_numero == 'singular' and genero == 'masculino' or
                padrao_de_morfologia == 'IR' and oi_numero == 'singular' and genero == 'masculino'
        ):
            mi = 'ido'

        elif (
                padrao_de_morfologia == 'ER' and oi_numero == 'plural' and genero == 'masculino' or
                padrao_de_morfologia == 'IR' and oi_numero == 'plural' and genero == 'masculino'
        ):
            mi = 'idos'

        elif (
                padrao_de_morfologia == 'ER' and oi_numero == 'singular' and genero == 'feminino' or
                padrao_de_morfologia == 'IR' and oi_numero == 'singular' and genero == 'feminino'
        ):
            mi = 'ida'

        elif (
                padrao_de_morfologia == 'ER' and oi_numero == 'plural' and genero == 'feminino' or
                padrao_de_morfologia == 'IR' and oi_numero == 'plural' and genero == 'feminino'
        ):
            mi = 'idas'

        elif padrao_de_morfologia == 'OR' and oi_numero == 'singular' and genero == 'feminino':
            mi = 'osta'

        elif padrao_de_morfologia == 'OR' and oi_numero == 'singular' and genero == 'masculino':
            mi = 'osto'

        elif padrao_de_morfologia == 'OR' and oi_numero == 'plural' and genero == 'feminino':
            mi = 'ostas'

        elif padrao_de_morfologia == 'OR' and oi_numero == 'plural' and genero == 'masculino':
            mi = 'ostos'

        return mi
    except ValueError:
        return ''


def realizacao_transitoriedade_do_verbo(tipo_de_orientacao=None, padrao_de_morfologia=None,
                                        oi_numero=None, genero=None, oi_tipo_de_pessoa=None,
                                        padrao_pessoa_morfologia="Morfologia_padrão") -> str:
    """
    Função geral que retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    ex.:
    >>>realizacao_transitoriedade_do_verbo('presente','AR','singular',None,'1pessoa')
    >>>'o'
    :param tipo_de_orientacao
        opções: 'infinitivo','presente','pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
        'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo','subjuntivo_condicional', 'subjuntivo_optativo',
        'não_finito_concretizado','imperativo_I','imperativo_II','gerúndio', 'particípio'
    :param padrao_de_morfologia:str
       escolhas: 'AR','ER','IR', 'OR'
    :param oi_numero:str
       escolhas: 'singular', 'plural'
    :param genero:str
        escolhas: 'feminino', 'masculino'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
       escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
       Morfema Interpessoal que realiza a Orientação Interpessoal do verbo
    """
    mi = None
    try:
        if tipo_de_orientacao == 'infinitivo':
            mi = realizacao_transitoriedade_infinitivo(padrao_de_morfologia)

        elif tipo_de_orientacao == 'presente':
            mi = realizacao_transitoriedade_presente(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                     padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_I':
            mi = realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'pretérito_perfectivo_II':
            mi = realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'pretérito_imperfectivo':
            mi = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'passado_volitivo':
            mi = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                             padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'futuro':
            mi = realizacao_transitoriedade_futuro(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
            mi = realizacao_transitoriedade_subjuntivo_conjuntivo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                                  padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_condicional':
            mi = realizacao_transitoriedade_subjuntivo_condicional(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                                   padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'subjuntivo_optativo':
            mi = realizacao_transitoriedade_subjuntivo_optativo(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'não_finito_concretizado':
            mi = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                                    padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_I':
            mi = realizacao_transitoriedade_imperativo_I(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa,
                                                         padrao_pessoa_morfologia)

        elif tipo_de_orientacao == 'imperativo_II':
            mi = realizacao_transitoriedade_imperativo_II(padrao_de_morfologia, oi_numero, oi_tipo_de_pessoa)

        elif tipo_de_orientacao == 'gerúndio':
            mi = realizacao_transitoriedade_gerundio(padrao_de_morfologia)

        elif tipo_de_orientacao == 'particípio':
            mi = realizacao_transitoriedade_participio(padrao_de_morfologia, oi_numero, genero)
        return mi
    except ValueError:
        return ''


if __name__ == '__main__':
    def none_ou_str(value):
        if value == 'None':
            return None
        return value
    # parseamentos detecção ME e MI
    parser = argparse.ArgumentParser(description='Retorna experiência (radical), '
                                                 'morfema interpessoal do verbo conjugado, '
                                                 'terminação do infinitivo dado o padrão de morfologia')
    parser.add_argument('argumentos', nargs='+', type=none_ou_str)
    args = parser.parse_args()

    if len(args.argumentos) < 2:
        print('O ME do verbo: ', experiencia_do_verbo(args.argumentos[0]))
        print('O MI do verbo: ', deteccao_transitoriedade_do_verbo(args.argumentos[0]))
        print('O padrão de morfologia do infinitivo:', detecta_padrao_morfologia(args.argumentos[0]))
    else:
        print(realizacao_transitoriedade_do_verbo(*args.argumentos))
    # print(args.argumentos)
