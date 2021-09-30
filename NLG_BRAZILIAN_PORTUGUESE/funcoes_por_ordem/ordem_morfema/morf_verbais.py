import importlib
import nltk
import argparse

nltk.download('punkt')
nltk.download('rslp')


# MESMA FUNCAO COM NLTK


def experiencia_do_verbo(verbo):
    """
    Retorna um str com o morfema experiencial (me) que realiza
    a experiência do verbo, dado um verbo lematizado
    :param:verbo no infinitivo (str)
    :return: morfema experiencial (str)
    """
    nltk_imp = importlib.import_module('nltk')
    rad = nltk_imp.stem.RSLPStemmer()
    return rad.stem(verbo)


# TRANSITORIEDADE

def deteccao_transitoriedade_do_verbo(verbo):
    """
    (str) -> str

    Retorna o morfema interpessoal que realiza a orientação interpessoal
    dados o verbo, seu padrão de morfologia, seu tipo_pessoa de orientação
    e o tipo_pessoa de pessoa.

    :param: verbo
    :return: morfema interpessoal
    """

    me = experiencia_do_verbo(verbo)
    mi = (verbo[len(me):])
    return mi


def realizacao_transitoriedade_infinitivo(padrao_de_morfologia):
    """
    (str)->str
    :param padrao_de_morfologia:
    :return: Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.
    """
    mi = None
    if padrao_de_morfologia == '-AR':
        mi = 'ar'
    elif padrao_de_morfologia == '-ER':
        mi = 'er'
    elif padrao_de_morfologia == '-IR':
        mi = 'ir'
    elif padrao_de_morfologia == '-OR':
        mi = 'or'
    return mi


def detecta_padrao_morfologia(verbo):
    """
    (str)->str
    :param verbo:
    :return:Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dado
    padrão de morfologia.
    """
    spc_import = importlib.import_module('spacy')
    nlp = spc_import.load("pt_core_news_lg")

    if verbo is None:
        padrao_morfologia = None
    else:
        txt = nlp(verbo)
        verbo = txt[0].lemma_
        me = experiencia_do_verbo(verbo)
        mi = (verbo[len(me):])
        if mi == 'ar':
            padrao_morfologia = '-AR'
        elif mi == 'er':
            padrao_morfologia = '-ER'
        elif mi == 'ir':
            padrao_morfologia = '-IR'
        elif mi == 'or':
            padrao_morfologia = '-OR'
        else:
            padrao_morfologia = None

    return padrao_morfologia


# transitoriedade (todos os tempos verbais)


def realizacao_transitoriedade_presente(padrao_de_morfologia: str, oi_numero: str, oi_tipo_de_pessoa: str,
                                        padrao_pessoa_morfologia: str = "Morfologia_padrão") -> str:
    """
    Retorna o morfema que realiza a transitoriedade de um verbo no presente, dados
    o padrão de morfologia, tipo de orientação, tipo de pessoa, número e o padrão pessoa_morfologia.

    ex.:
    >>>realizacao_transitoriedade_presente('-AR','singular','1pessoa')
    >>>'o'
    :param padrao_de_morfologia:str
       escolhas: '-AR','-ER','-IR', '-OR'
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
                padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == "Morfologia_padrão" or
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == "Morfologia_padrão" or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == "Morfologia_padrão"
        ):
            mi = 'o'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and
              oi_numero == 'singular' and padrao_pessoa_morfologia == "Morfologia_padrão"):
            mi = 'onho'
        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'a'
        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'as'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'
        ):
            mi = 'e'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
        ):
            mi = 'es'

        elif (
                padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'õe'
        elif (
                padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'ões'
        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular':
            mi = 'a'
        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
        ):
            mi = 'e'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'õe'

        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'a'

        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'amos'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'e'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'emos'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'e'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'imos'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and
              padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'õe'
        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'omos'
        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'a'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ais'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'e'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'eis'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'e'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'is'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'õe'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ondes'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'a'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'am'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == '3pessoa_do_singular' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'
        ):
            mi = 'e'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
        ):
            mi = 'em'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'õe'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'õem'
        return mi
    except KeyError:
        return ''


def realizacao_transitoriedade_preterito_perfectivo_I(padrao_de_morfologia: str, oi_numero: str, oi_tipo_de_pessoa: str,
                                                      padrao_pessoa_morfologia: str = "Morfologia_padrão"
                                                      ) -> str:
    """
     Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo de orientação, tipo de pessoa e número.

    >>>realizacao_transitoriedade_preterito_perfectivo_I('-AR','singular','1pessoa')
    >>>'ei'
    :param padrao_de_morfologia:str
       escolhas: '-AR','-ER','-IR', '-OR'
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
        if padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == "Morfologia_padrão":
            mi = 'ei'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == "Morfologia_padrão" or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == "Morfologia_padrão"):
            mi = 'i'

        elif (
                padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == "Morfologia_padrão"):
            mi = 'us'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'
        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'aste'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'este'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'iste'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'
        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'useste'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ou'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'eu'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'iu'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ôs'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'
        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'amos'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'emos'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'imos'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'
        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'usemos'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'astes'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'estes'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'istes'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'usestes'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ou'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'aram'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'eu'
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'eram'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'iu'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'iram'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ôs'
        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'useram'
        return mi
    except KeyError:
        return ''


def realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia: str, oi_numero: str, oi_tipo_de_pessoa: str,
                                                      padrao_pessoa_morfologia: str = "Morfologia_padrão") -> str:
    """

    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo_pessoa de pessoa e número.

    ex.:
    >>>realizacao_transitoriedade_preterito_imperfectivo('-IR', 'singular', '1pessoa')
    >>>'ia'

    :param padrao_de_morfologia:str
       escolhas: '-AR','-ER','-IR', '-OR'
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
                padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
                and padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'ava'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'
                or padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'ia'

        elif (
                padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão' or
                padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == 'Morfologia_padrão'):
            mi = 'unha'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ava'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'avas'

        elif (
                padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular' or
                padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and
                padrao_pessoa_morfologia == '3pessoa_do_singular'):
            mi = 'ia'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ias'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ias'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'unha'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'unhas'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ava'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'ávamos'
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'íamos'
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ia'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ia'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'íamos'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'unha'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morforlogia_padrão':
            mi = 'únhamos'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == '3pessoa_do_singular':
            mi = 'ava'
        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural' and \
                padrao_pessoa_morfologia == 'Morfologia_padrão':
            mi = 'áveis'
        #
        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ia'
            else:
                mi = 'íeis'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ía'
            else:
                mi = 'íeis'
        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'unha'
            else:
                mi = 'únheis'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ava'
            else:
                mi = 'avam'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ia'
            else:
                mi = 'iam'
        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'ía'
            else:
                mi = 'íam'
        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':
            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'unha'
            else:
                mi = 'unham'
        return mi
    except KeyError:
        return ''


def realizacao_transitoriedade_preterito_perfectivo_II(padrao_de_morfologia: str, oi_numero: str,
                                                       oi_tipo_de_pessoa: str, padrao_pessoa_morfologia: str = "Morfologia_padrão"):
    """

    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo_pessoa de pessoa, e número.

    ex.:
    >>>realizacao_transitoriedade_preterito_perfectivo_II('-AR', 'singular','1pessoa')
    >>>'ara'

    :param padrao_de_morfologia:str
       escolhas: '-AR','-ER','-IR', '-OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo

    """
    try:
        if (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'
        ):
            mi = 'ara'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'era'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'ira'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'usera'

        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular'):
            mi = 'aras'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular'):
            mi = 'eras'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular'):
            mi = 'iras'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular'):
            mi = 'useras'

        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'):
            mi = 'áramos'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'):
            mi = 'êramos'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'):
            mi = 'íramos'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural'):
            mi = 'úseramos'

        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural'):
            mi = 'áreis'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural'):
            mi = 'êreis'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural'):
            mi = 'íreis'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural'):
            mi = 'uséreis'

        elif (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'):
            mi = 'aram'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'):
            mi = 'eram'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'):
            mi = 'iram'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural'):
            mi = 'useram'
        return mi
    except KeyError:
        return ''


def realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia: str, oi_numero: str, oi_tipo_de_pessoa: str,
                                                padrao_pessoa_morfologia: str = "Morfologia_padrão") -> str:
    """

    Retorna o morfema que realiza a transitoriedade de um verbo no passado volitivo, dados
    a o padrão de morfologia, tipo de pessoa e número.

    ex.:
    >>>realizacao_transitoriedade_passado_volitivo('-AR', 'singular', '1pessoa',padrao_pessoa_morfologia="Morfologia_padrão")
    >>>'aria'

    :param padrao_de_morfologia:str
       escolhas: '-AR','-ER','-IR', '-OR'
    :param oi_numero:str
        escolhas: 'singular', 'plural'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
        escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return:mi
        Morfema Interpessoal que realiza a Orientação Interpessoal do verbo

    """
    try:
        if (padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
                padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'aria'

        elif (padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'eria'

        elif (padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'iria'

        elif (padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'singular' or
              padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'singular'):
            mi = 'oria'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'arias'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'erias'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'irias'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'singular':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'orias'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'aríamos'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'eríamos'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'iríamos'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'oríamos'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'aríeis'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'eríeis'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '2pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'iríeis'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '1pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'oríeis'

        elif padrao_de_morfologia == '-AR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'aria'
            else:
                mi = 'ariam'

        elif padrao_de_morfologia == '-ER' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'eria'
            else:
                mi = 'eriam'

        elif padrao_de_morfologia == '-IR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'iria'
            else:
                mi = 'iriam'

        elif padrao_de_morfologia == '-OR' and oi_tipo_de_pessoa == '3pessoa' and oi_numero == 'plural':

            if padrao_pessoa_morfologia == '3pessoa_do_singular':
                mi = 'oria'
            else:
                mi = 'oriam'

        return mi
    except KeyError:
        return ''


if __name__ == '__main__':
    # parseamentos detecção ME e MI
    parser_me_mi = argparse.ArgumentParser(description='Retorna experiência (radical), '
                                                       'morfema interpessoal do verbo conjugado, '
                                                       'terminação do infinitivo dado o padrão de morfologia')
    parser_me_mi.add_argument('argumentos', nargs='+', type=str)
    args = parser_me_mi.parse_args()

    print('O ME do verbo: ', experiencia_do_verbo(args.argumentos[0]))
    print('O MI do verbo: ', deteccao_transitoriedade_do_verbo(args.argumentos[0]))
    print('O padrão de morfologia do infinitivo:', detecta_padrao_morfologia(args.argumentos[0]))

# parseamento realização de transitoriedade
