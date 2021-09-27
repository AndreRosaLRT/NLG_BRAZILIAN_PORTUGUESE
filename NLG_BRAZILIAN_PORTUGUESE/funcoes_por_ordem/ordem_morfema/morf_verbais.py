import importlib
import nltk as nltk
import spacy
nltk.download('punkt')
nltk.download('rslp')
import argparse

##MESMA FUNCAO COM NLTK


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retorna experiência (radical), '
                                                 'morfema inerpessoal do verbo conjugado, '
                                                 'terminação do infinitivo dado o padrão de morfologia')
    parser.add_argument('argumentos', nargs='+', type=str)
    args = parser.parse_args()

    print('O ME do verbo: ', experiencia_do_verbo(args.argumentos[0]))
    print('O MI do verbo: ', deteccao_transitoriedade_do_verbo(args.argumentos[0]))
    print('O padrão de morfologia do infinitivo:', detecta_padrao_morfologia(args.argumentos[0]))
