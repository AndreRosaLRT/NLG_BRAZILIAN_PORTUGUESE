# Cardinais teste
import argparse
import re
# import nltk
# nltk.download('punkt')
# nltk.download('rslp')


DECIMAIS = (('décimo', 'décimos'), ('centésimo', 'centésimos'), ('milésimo', 'milésimos'),
            ('décimo de milésimo', 'décimos de milésimo'),
            ('centésimo de milésimo', 'centésimos de milésimo'), ('milionésimo', 'milionésimos'),
            ('décimo de milionésimo', 'décimos de milionésimo'),
            ('centésimo de milionésimo', 'centésimos de milionésimo'), ('bilionésimo', 'bilionésimos'),
            ('décimo de bilionésimo', 'décimos de bilionésimo'),
            ('centésimo de bilionésimo', 'centésimos de bilionésimo'), ('trilionésimo', 'trilionésimos'),
            ('quatrilionésimo', 'quatrilionésimos'),
            ('quintilionésimo', 'quintilionésimos'), ('sextilionésimo', 'sextilionésimos'),
            ('septilionésimo', 'septilionésimos'), ('octilionésimo', 'octilionésimos'),
            ('nonilionésimo', 'nonilionésimos'), ('decilionésimo', 'decilionésimos')
            )
UNIDADES = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
DEZENA_ESPECIAL = ('', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
DEZENAS = ('', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
CENTENAS = ('cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos',
            'oitocentos', 'novecentos')
MILHAR = (('milhão', 'milhões'), ('bilhão', 'bilhões'), ('trilhão', 'trilhões'), ('quatrilhão', 'quatrilhões'),
          ('quintilhão', 'quintilhões'),
          ('sextilhão', 'sextilhões'), ('septilhão', 'septilhões'), ('octilhão', 'octilhões'),
          ('nonilhão', 'nonilhões'), ('decilhão', 'decilhões'),
          ('unodecilhão', 'unodecilhões'), ('duodecilhão', 'duodecilhões'), ('tredecilhão', 'tredecilhões'),
          ('quatuordecilhão', 'quatuordecilhões'),
          ('quindecilhão', 'quindecilhões'), ('sexdecilhão', 'sexdecilhões'), ('sepdecilhão', 'sepdecilhões'),
          ('octodecilhão', 'octodecilhões'),
          ('novemdecilhão', 'novemdecilhões')
          )


UNIDADES_ORD = ('', 'primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono')
# DEZENA_ESPECIAL_ORD = ('', 'décimo primeiro', 'décimo segundo', 'décimo terceiro', 'décimo quarto', 'décimo quinto',
#                        'décimo sexto', 'décimo sétimo', 'décimo oitavo', 'décimo nono')
DEZENAS_ORD = ('', 'décimo', 'vigésimo','trigésimo', 'quadragésimo', 'quinquagésimo', 'sexagésimo', 'septuagésimo',
               'octogésimo', 'nonagésimo')
CENTENAS_ORD = ('','centésimo', 'ducentésimo', 'trecentésimo', 'quadringentésimo', 'quingentésimo', 'sexsentésimo',
                'setingentésimo', 'octingentésimo', 'nongentésimo')
MILHAR_ORD = ('', 'milésimo')


def separar_casas(numero):
    digitos = list(str(numero))
    tamanho = len(digitos)

    casa = tamanho % 3
    casas = []
    terno = []
    for i in range(tamanho):
        terno.append(int(digitos[i]))
        if (i + 1) % 3 == casa:
            casas.append(terno)
            terno = []
    return casas


def unidade_dezena_centena(terno, genero=None):

    numero_extenso = ''

    termos = len(terno)
    digito = terno[0]

    if termos == 3:
        if digito != 0:
            if terno[1:] == [0, 0]:
                if digito == 1:
                    numero_extenso += CENTENAS[0]
                else:
                    if genero == 'feminino':
                        numero_extenso += CENTENAS[digito][slice(-2)] + 'as'
                    else:
                        numero_extenso += CENTENAS[digito]

            else:
                if terno[0] == 1:
                    if genero == 'feminino':
                        numero_extenso += CENTENAS[digito] + ' e '
                        if terno[-1] == 2:
                            numero_extenso += unidade_dezena_centena(terno[1:])[slice(-3)] + "uas"
                        else:
                            numero_extenso += unidade_dezena_centena(terno[1:])
                else:

                    if genero == 'feminino':
                        numero_extenso += CENTENAS[digito][slice(-2)] + 'as e '

                        if terno[-1] == 2:
                            numero_extenso += unidade_dezena_centena(terno[1:])[slice(-3)] + "uas"
                        else:
                            numero_extenso += unidade_dezena_centena(terno[1:])
                    else:
                        numero_extenso += CENTENAS[digito] + ' e ' + unidade_dezena_centena(terno[1:])
        else:
            if genero == 'feminino':

                if terno[2] == 2:
                    numero_extenso += unidade_dezena_centena(terno[1:])[slice(-3)] + "uas"
                else:
                    numero_extenso += unidade_dezena_centena(terno[1:])

    if termos == 2:
        if digito != 0:
            if terno[1] == 0:
                numero_extenso += DEZENAS[digito]
            elif digito == 1:
                numero_extenso += DEZENA_ESPECIAL[terno[1]]
            else:
                if terno[-1] == 2 and genero == 'feminino':
                    numero_extenso += DEZENAS[digito] + ' e ' + unidade_dezena_centena(terno[1:])[slice(-3)] + "uas"
                else:
                    numero_extenso += DEZENAS[digito] + ' e ' + unidade_dezena_centena(terno[1:])

        else:
            numero_extenso += unidade_dezena_centena(terno[1:])
    elif termos == 1:
        if terno[0] == 1 and genero == 'feminino':
            numero_extenso += UNIDADES[digito] + 'a'
        elif terno[0] == 2 and genero == 'feminino':
            numero_extenso += UNIDADES[digito][slice(-3)] + 'uas'
        else:
            numero_extenso += UNIDADES[digito]

    return numero_extenso

#
# unidade_dezena_centena([3,2,4], 'masculino')
# unidade_dezena_centena([3,2,4], 'feminino')
# unidade_dezena_centena([3,2,2], 'masculino')
# unidade_dezena_centena([3,2,2], 'feminino')
# unidade_dezena_centena([5,2,4], 'feminino')


def milhares(ternos, genero=None):
    numero_extenso = ''
    termos = len(ternos)
    terno = ternos[0]

    if termos >= 3:
        if terno != [0, 0, 0]:
            if terno == [0, 0, 1] or terno == [1]:
                numero_extenso += 'um ' + MILHAR[termos - 3][0]
            else:
                numero_extenso += unidade_dezena_centena(terno, genero) + ' ' + MILHAR[termos - 3][1]

            if ternos[1:] == [[0, 0, 0], [0, 0, 0]]:
                return numero_extenso
            else:
                numero_extenso += ' ' + milhares(ternos[1:], genero)
        else:
            numero_extenso += milhares(ternos[1:], genero)

    if termos == 2:
        if terno != [0, 0, 0]:
            numero_extenso += unidade_dezena_centena(terno, genero) + ' mil'
            if ternos[1] == [0, 0, 0]:
                return numero_extenso
            elif ternos[1][0]:
                numero_extenso += ' ' + milhares(ternos[1:], genero)
            else:
                numero_extenso += ' e ' + milhares(ternos[1:], genero)
        else:
            numero_extenso += ' ' + milhares(ternos[1:], genero)

    elif termos == 1:
        if terno != [0, 0, 0]:
            numero_extenso += unidade_dezena_centena(terno, genero)

    return numero_extenso


def formatar(numero: str):
    numero = str(float(numero.replace(',', '.')))
    divisao = numero.split('.')

    if 0 < len(divisao) < 3:
        if len(divisao[0]) > 33:
            raise ValueError('Valor muito grande')
        else:
            inteiro = int(divisao[0])

        if len(divisao) == 2:
            if len(divisao[1]) > 35:
                raise ValueError('Valor decimal muito grande')
            else:
                decimal = divisao[1]
        else:
            decimal = None
    else:
        raise ValueError('Número não formatado corretamente')

    return inteiro, decimal


def real(numero: float or str, genero=None):
    inteiro, decimal = formatar(str(numero))
    extenso = milhares(separar_casas(inteiro), genero)

    if decimal is not None and int(decimal) != 0:
        ordem = len(decimal) - 1
        if ordem > 11:
            ordem = 7 + ordem // 3

        if inteiro == 0:
            extenso = ''
        elif inteiro == 1:
            extenso += ' inteiro e '
        else:
            extenso += ' inteiros e '

        decimal = int(decimal)
        if decimal == 1:
            plural = 0
        else:
            plural = 1

        extenso += milhares(separar_casas(decimal), genero) + ' ' + DECIMAIS[ordem][plural]

    return extenso


def monetario(numero: float or str):
    inteiro, decimal = formatar(str(numero))
    extenso = milhares(separar_casas(inteiro))

    if inteiro == 0:
        extenso = ''
    elif inteiro == 1:
        extenso += ' real'
    else:
        extenso += ' reais'

    if decimal is not None and int(decimal) != 0:
        ordem = len(decimal)
        if ordem == 1:
            decimal += '0'
            ordem = 2
        elif ordem > 11:
            ordem = 7 + ordem // 3

        if inteiro == 0:
            extenso = ''
        elif inteiro == 1:
            extenso += ' e '
        else:
            extenso += ' e '

        decimal = int(decimal)
        if decimal == 1:
            plural = 0
        else:
            plural = 1

        extenso += milhares(separar_casas(decimal))
        if decimal == 1:
            if ordem < 3:
                extenso += ' centavo'
            else:
                extenso += ' ' + DECIMAIS[ordem - 3][plural] + ' de centavo'
        elif decimal < 100:
            extenso += ' centavos'
        else:
            extenso += ' ' + DECIMAIS[ordem - 3][plural] + ' de centavo'

    return extenso


def ordinal(num_cardinal, genero=None):
    """
    Até 9999 - retorna os números ordinais

    Ex.:
    >>> ordinal(999999, 'masculino')
    'nongentésimo nonagésimo nono milésimo nongentésimo nonagésimo nono'

    >>> ordinal(123, 'feminino')
    'centésima vigésima terceira'

    >>> ordinal(2334,'feminino')
    'segunda milésima trecentésima trigésima quarta'

    :param num_cardinal:
    :param genero:
    :return: ordinais
    """

    numero_extenso, cent_mil, dez_mil, unid_mil, cent, dez, unid = '', '', '', '', '', '', ''
    ternos = separar_casas(num_cardinal)
    if ternos.__len__() == 2:
        if ternos[-2].__len__() > 2:
            cent_mil = CENTENAS_ORD[ternos[-2][-3]]
        else:
            cent_mil = ''
        if ternos[-2].__len__() > 1:
            dez_mil = DEZENAS_ORD[ternos[-2][-2]]
        else:
            dez_mil = ''
        unid_mil = UNIDADES_ORD[ternos[-2][-1]]
        if ternos[-1].__len__() > 2:
            cent = CENTENAS_ORD[ternos[-1][-3]]
        else:
            cent = ''
        if ternos[-1].__len__() > 1:
            dez = DEZENAS_ORD[ternos[-1][-2]]
        else:
            dez = ''
        unid = UNIDADES_ORD[ternos[-1][-1]]
        numero_extenso = ' '.join((cent_mil, dez_mil,  unid_mil,'milésimo', cent, dez, unid))

    if ternos.__len__() == 1:
        if ternos[-1].__len__() > 2:
            cent = CENTENAS_ORD[ternos[-1][-3]]
        else:
            cent = ''
        if ternos[-1].__len__() > 1:
            dez = DEZENAS_ORD[ternos[-1][-2]]
        else:
            dez = ''
        unid = UNIDADES_ORD[ternos[-1][-1]]
        numero_extenso = ' '.join((cent_mil, dez_mil, unid_mil, cent, dez, unid))

    if genero == 'feminino':
        numero_extenso = ' '.join([i[slice(-1)] + 'a' for i in numero_extenso.split()])
    return re.sub(' +', ' ', numero_extenso).strip()


# #
def porcento(cardinal):
    """
    Retorna num com símbolo de percentual
    :param cardinal:
    :return:
    """
    porc = str(cardinal) + '%'

    return porc


def porcento_extenso(numero):
    """
    Retorna uma porcentagem por extenso dada uma lista de inteiros representando cada casa do cardinal
    Ex.:

    >>>porcento_extenso(34)
    'trinta e quatro por cento'

    :param numero:
    :return: percentagem por extenso
    """
    return ' '.join((real(numero), 'por cento'))


def numerativo(tipo_numerativo=None, cardinal=None, genero_numerativo=None):
    """
    Retorna numerativos (ainda restrito a cardinal, ordinal e porcentagem, por enquanto), dada o
    tipo de numerativo, um número cardinal, genero,

    Ex.:

    >>> numerativo('cardinal',23,'feminino')
    'vinte e três'

   >>> numerativo('cardinal',202,'feminino')
    'duzentas e duas'

    >>> numerativo('ordinal',202,'feminino')
    'ducentésima segunda'

    :param tipo_numerativo:
    :param cardinal:
    :param genero_numerativo:
    :return: numerativo
    """

    try:
        if tipo_numerativo == 'ordinal':
            num_extenso = ordinal(cardinal, genero_numerativo)

        elif tipo_numerativo == 'porcentagem':
            num_extenso = porcento_extenso(cardinal)

        elif tipo_numerativo == 'cardinal':
            num_extenso = real(cardinal, genero_numerativo)
        else:
            num_extenso = ''

        return num_extenso
    except ValueError:
        return ''


# def detecta_exp_substantivo(substantivo):  ##dado o substantivo flexionado##
#     '''(str,str,str)->
#
#     Retorna o morfema que realiza a experiência em um substantivo, dados
#     o substantivo flexionado, o gênero e o numero.
#
#     >>>detecta_exp_substantivo('','masculino','plural')
#     'gat'
#     '''
#     raiz = nltk.stem.RSLPStemmer()
#
#     # if genero == 'masculino' and numero == 'singular':
#     #     raizSubs = (substantivo[slice(-1)])
#     #
#     # elif genero == 'feminino' and numero == 'singular':
#     #     raizSubs = (substantivo[slice(-1)])
#     #
#     # elif genero == 'masculino' and numero == 'plural':
#     #     raizSubs = (substantivo[slice(-2)])
#     #
#     # elif genero == 'feminino' and numero == 'plural':
#     #     raizSubs = (substantivo[slice(-2)])
#     return raiz.stem(substantivo)
# detecta_exp_substantivo('garrafa')


# genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
# lemaSubs = input('Qual é o substantivo lematizado?')

#
# def realiza_exp_substantivo(lema, genero):
#
#     """
#     Retorna o morfema que realiza a experiência em um substantivo, dado
#     o substantivo lematizado.
#
#     ##dado o substantivo_lematizado- por enquanto, apenas para
#     ##substantivos regulares, com foco em masculino-feminino, singular plural. Tenho que considerar desenvolver
#     #    com relação aos diferentes tipos de radicais (primitivo, derivado, composto, simples...)
#
#     >>>realiza_exp_substantivo('gato','feminino')
#     'gat'
#     """
#     morf_exp_subs = ''
#     if genero == 'masculino' or genero == 'feminino':
#         morf_exp_subs = lema[slice(-1)]
#
#     elif genero == 'não-binário':
#         morf_exp_subs = lema
#
#     return morf_exp_subs
#

# realizaExpSubstantivo('gata','masculino')
# #

def realizacao_flexoes_substantivo(genero, numero):
    """(str,str,str)->str

    Retorna os morfemas que realizam as flexões de genero e numero dados
    a experiência do substantivo e os genero e numeros desejados.

    genero = choice.Menu(['masculino', 'feminino', 'não-binário']).ask()
    numero = choice.Menu(['singular', 'plural']).ask()
    
    >>>realizacao_flexoes_substantivo(,
    'os'
    """
    morfema_flexao_substantivo = ''
    if genero == 'masculino' and numero == 'singular':
        morfema_flexao_substantivo = 'o'
    elif genero == 'feminino' and numero == 'singular':
        morfema_flexao_substantivo = 'a'
    elif genero == 'masculino' and numero == 'plural':
        morfema_flexao_substantivo = 'os'
    elif genero == 'feminino' and numero == 'plural':
        morfema_flexao_substantivo = 'as'
    elif genero == 'não-binário' and numero == 'singular':
        morfema_flexao_substantivo = ''
    elif genero == 'não-binário' and numero == 'plural':
        morfema_flexao_substantivo = 's'

    return morfema_flexao_substantivo


# realizacao_flexoes_substantivos("masculino",'plural')
# #
# # ###Com relação aos substantivos comuns tenho que ver a abordagem que vou tomar
# # # com relação aos substantivos não binários, ou inerentemente masculinos ou femininos. Me parece
# # # que o sistema se organiza a realizar o gênero em alguns casos na ordem da palavra, e em
# # # outros casos na ordem do grupo (mesa: não parece ter uma contrapartida masculina)
# #

def substantivo_comum(substantivo_lematizado, numero='singular',
                      genero='masculino', tipo_feminino_ao=None,
                      tipo_masc_ao=None, acent_tonica=None):
    """
    Retorna o substantivo comum flexionado em gênero e número
    Ex.:

    >>>substantivo_comum("ancião",'plural',"masculino", None,"ão",None)
    'anciãos'

    >>> substantivo_comum("artesão",'singular',"feminino", "ão",None,None)
    'artesã'

    >>> substantivo_comum("carro","plural","não-binário")
    'carros'

    >>> substantivo_comum("varal","plural", "não-binário")
    'varais'

    >>> substantivo_comum("retrós","plural", "não-binário", None, None,'oxítona')
    'retroses'

    :param substantivo_lematizado:
    :param numero:
    :param genero:
    :param tipo_feminino_ao:
        opcoes : ['oa', 'ona', 'ã', 'esa']
    :param tipo_masc_ao:
        opcoes: ['ãos', 'ões', 'ães']
    :param acent_tonica: ['oxítona', 'paroxítona', 'proparoxítona']
    :return:
    """
    subs_comum = ''
    if substantivo_lematizado[-1:] == 'm':

        if numero == 'singular':
            subs_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'ns'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'or':

        if genero == 'masculino' and numero == 'singular':

            subs_comum = substantivo_lematizado

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'a'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'masculino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'es'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'as'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = ''
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 's'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo
    elif substantivo_lematizado[-2:] == 'ão':

        if (genero == 'masculino' and numero == 'singular'
                or genero == 'não-binário' and numero == 'singular'):
            subs_comum = substantivo_lematizado

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            subs_comum = morfema_experiencial_do_substantivo + tipo_feminino_ao

        elif (genero == 'masculino' and numero == 'plural'
              or genero == 'não-binário' and numero == 'plural'):

            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            subs_comum = morfema_experiencial_do_substantivo + tipo_masc_ao + 's'

        elif genero == 'feminino' and numero == 'plural':

            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            subs_comum = morfema_experiencial_do_substantivo + tipo_feminino_ao + 's'

    elif substantivo_lematizado[-1:] == 'x':
        subs_comum = substantivo_lematizado

    elif substantivo_lematizado[-1:] == 's':
        if acent_tonica == 'paroxítona':
            subs_comum = substantivo_lematizado
        elif acent_tonica == 'oxítona':
            if substantivo_lematizado[-2] == 'ó':
                morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)] + 'os'
            else:
                morfema_experiencial_do_substantivo = substantivo_lematizado

            morfema_numero = 'es'
            subs_comum = morfema_experiencial_do_substantivo + morfema_numero

    elif substantivo_lematizado[-1:] == 'r' or substantivo_lematizado[-1:] == 'z':

        if genero == 'masculino' and numero == 'singular':
            subs_comum = substantivo_lematizado

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'a'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'masculino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'es'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'as'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = ''
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'es'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'al':
        if numero == 'singular':
            subs_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'ais'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'el':

        if numero == 'singular':
            subs_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'éis'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'il':

        if numero == 'singular':
            subs_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'is'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'ol':

        if numero == 'singular':
            subs_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'óis'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'ul':

        if numero == 'singular':
            subs_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'úis'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    else:

        if genero == 'masculino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'o'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'a'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'masculino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'os'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'as'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = ''
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 's'
            subs_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    return subs_comum


# # # ADJETIVOS
#
# def deteccao_experiencia_do_adjetivo(adjetivo, genero, numero):  ##dado o adjetivo flexionado##
#     '''(str,str,str)->
#
#     Retorna o morfema que realiza a experiência em um adjetivo, dados
#     o adjetivo flexionado, o gênero e o número.
#
#     >>>deteccao_experiencia_do_adjetivo()
#     'esportiv'
#     '''
#
#     if numero == 'singular':
#         if genero == 'masculino':
#             raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
#
#         elif genero == 'feminino':
#             raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
#     elif numero == 'plural':
#         if genero == 'masculino':
#             raiz_experiencial_adjetivo = (adjetivo[slice(-2)])
#
#         elif genero == 'feminino':
#             raiz_experiencial_adjetivo = (adjetivo[slice(-2)])
#
#     return raiz_experiencial_adjetivo


# deteccao_experiencia_do_adjetivo("esperto","masculino","singular")
#

# def realizacao_experiencia_do_adjetivo(adjetivo_lematizado, genero):
#     """
#     genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
#     adjetivo_lematizado =
#
#     Retorna o morfema que realiza a experiência em um adjetivo, dado
#     o adjetivo lematizado.
#
#     >>>realizacao_experiencia_do_adjetivo()
#     'gat'
#     :param adjetivo_lematizado:
#     :param genero:
#     :return:
#     """
#     morfema_experiencial_do_adjetivo = ''
#     if genero == 'masculino/feminino':
#         morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
#
#     elif genero == 'não-binário':
#         morfema_experiencial_do_adjetivo = adjetivo_lematizado
#
#     return morfema_experiencial_do_adjetivo


# realizacao_experiencia_do_adjetivo("esperto","masculino/feminino")
#
# def realizacao_flexoes_adjetivos(genero, numero):
#     """
#     Retorna os morfemas que realizam as flexões de gênero e número dados
#     a experiência do adjetivo e os gênero e números desejados.
#
#     :param genero: 'masculino', 'feminino', 'não-binário'
#     :param numero: 'singular', 'plural'
#     :return: morfema_flexao_adjetivo
#     """
#
#     if numero == 'singular':
#         if genero == 'masculino':
#             morfema_flexao_adjetivo = 'o'
#
#         elif genero == 'feminino':
#             morfema_flexao_adjetivo = 'a'
#         elif genero == 'não-binário':
#             morfema_flexao_adjetivo = ''
#
#     elif numero == 'plural':
#         if genero == 'masculino':
#             morfema_flexao_adjetivo = 'os'
#
#         elif genero == 'feminino' and numero == 'plural':
#             morfema_flexao_adjetivo = 'as'
#
#         elif genero == 'não-binário':
#             morfema_flexao_adjetivo = 's'
#
#     return morfema_flexao_adjetivo


def adjetivo(adjetivo_lematizado=None, genero=None, numero=None):
    """
    Retorna a realizacao de um adjetivo comum dado o adjetivo lematizado e as
    e parâmetros de genero e número.

    Ex.:

    >>> adjetivo('garrafa','não-binário','plural')
    'garrafas'

    >>> adjetivo('gato','feminino','plural')
    'gatas'

    :param adjetivo_lematizado:
    :param genero:
        opções: 'feminino', 'masculino', 'não-binário'
    :param numero:
        opções: 'singular', 'plural'
    :return: adjetivo comum flexionado em genero e numero
    """
    morfema_experiencial_do_adjetivo, morfema_flexao_adjetivo = '', ''
    try:

        if numero == 'singular':
            if genero == 'masculino':
                morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
                morfema_flexao_adjetivo = 'o'

            elif genero == 'feminino':
                morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
                morfema_flexao_adjetivo = 'a'

            elif genero == 'não-binário':
                morfema_experiencial_do_adjetivo = adjetivo_lematizado
                morfema_flexao_adjetivo = ''

        elif numero == 'plural':
            if genero == 'masculino':
                morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
                morfema_flexao_adjetivo = 'os'

            elif genero == 'feminino':
                morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
                morfema_flexao_adjetivo = 'as'

            elif genero == 'não-binário':
                morfema_experiencial_do_adjetivo = adjetivo_lematizado
                morfema_flexao_adjetivo = 's'

        adj = morfema_experiencial_do_adjetivo + morfema_flexao_adjetivo
        return adj

    except ValueError:
        return ''

# #
# # # PRONOMES#
# # # PEGUEI OS PRONOMES BÁSICOS# QUANDO CHEGAR NA ORAÇÃO, A MORFOLOGIA DOS VERBOS
# # # FICA UM POUCO SUBVERSIVA


def realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero, numero,
                                   morfologia_do_pronome="morfologia_terceira_pessoa"):
    """
    Retorna a realização de pronomes de caso reto, dados a pessoa da interlocução,
    o gênero, o número e, opcionalmente, o tipo de morfologia do pronome.
    Ex.:
    >>> realizacao_pronominal_casoreto("não_interlocutor", "feminino", "singular")
    'ela'

    >>> realizacao_pronominal_casoreto("ouvinte", "feminino", "singular",'padrão')
    'tu'

    :param pessoa_da_interlocucao:
    :param genero:
        opções: 'feminino', 'masculino', 'não-binário'
    :param numero:
        opções: 'singular', 'plural'
    :param morfologia_do_pronome:
        opções:  "morfologia_terceira_pessoa", 'padrão'
    :return:
    """
    pronome_pessoal_reto = ''

    try:
        if pessoa_da_interlocucao == 'falante' and numero == 'singular':
            pronome_pessoal_reto = 'eu'

        elif pessoa_da_interlocucao == 'ouvinte' and numero == 'singular':

            if morfologia_do_pronome == 'padrão':
                pronome_pessoal_reto = 'tu'
            else:
                pronome_pessoal_reto = 'você'

        elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'singular':
            if genero == 'masculino':
                pronome_pessoal_reto = 'ele'
            else:
                pronome_pessoal_reto = 'ela'

        elif pessoa_da_interlocucao == 'falante' and numero == 'plural':
            pronome_pessoal_reto = 'nós'

        elif pessoa_da_interlocucao == 'ouvinte' and numero == 'plural':

            if morfologia_do_pronome == 'padrão':
                pronome_pessoal_reto = 'vós'
            else:
                pronome_pessoal_reto = 'vocês'

        elif pessoa_da_interlocucao == 'não_interlocutor' and numero == 'plural':

            if genero == 'masculino':
                pronome_pessoal_reto = 'eles'
            else:
                pronome_pessoal_reto = 'elas'

        return pronome_pessoal_reto
    except ValueError:
        return ''


def realizacao_pronome_caso_obliquo(transitividade_verbo: str = None, tonicidade: str = None,
                                    pessoa_da_interlocucao: str = None,
                                    numero: str = None, genero: str = None,
                                    morfologia_do_pronome: str = None, reflexivo: bool = False):
    """
    Retorna o pronome oblíquo.


    >>> realizacao_pronome_caso_obliquo('direto', 'átono','falante', 'singular', None, None, False)
    'me'

    >>> realizacao_pronome_caso_obliquo('direto', 'átono','falante', 'singular', None, None, True)
    'se'
    :param transitividade_verbo: 'direto','direto_preposicionado, 'indireto'
    :param tonicidade: 'átono', 'tônico'
    :param pessoa_da_interlocucao: 'falante', 'ouvinte', 'não_interlocutor'
    :param numero: 'singular', 'plural'
    :param genero: 'masculino', 'feminino'
    :param morfologia_do_pronome: 'padrão', 'não_padrão'
    :param reflexivo: bool
    :return: pronome oblíquo
    """
    pronome_pessoal_obliquo = ''
    try:
        if tonicidade == 'átono' and transitividade_verbo == "direto":
            if numero == 'singular':
                if pessoa_da_interlocucao == 'falante':
                    pronome_pessoal_obliquo = 'me'
                elif pessoa_da_interlocucao == 'ouvinte':
                    pronome_pessoal_obliquo = 'te'
            elif numero == 'plural':
                if pessoa_da_interlocucao == 'falante':
                    pronome_pessoal_obliquo = 'nos'
                elif pessoa_da_interlocucao == 'ouvinte':
                    pronome_pessoal_obliquo = 'vos'

            if pessoa_da_interlocucao == 'não_interlocutor':
                if numero == 'singular':
                    if genero == 'masculino':
                        if morfologia_do_pronome == 'padrão':
                            pronome_pessoal_obliquo = 'o'

                    if genero == 'feminino':
                        if morfologia_do_pronome == 'padrão':
                            pronome_pessoal_obliquo = 'a'

                elif numero == 'plural':
                    if genero == 'masculino':
                        if morfologia_do_pronome == 'padrão':
                            pronome_pessoal_obliquo = 'os'

                    if genero == 'feminino':
                        if morfologia_do_pronome == 'padrão':
                            pronome_pessoal_obliquo = 'as'

        if reflexivo:
            pronome_pessoal_obliquo = 'se'

        if pessoa_da_interlocucao == 'não_interlocutor' and transitividade_verbo == "indireto":
            if tonicidade == 'átono':
                if numero == 'singular':
                    pronome_pessoal_obliquo = 'lhe'

                elif numero == 'plural':
                    if morfologia_do_pronome == 'padrão':
                        pronome_pessoal_obliquo = 'lhes'

            elif tonicidade == 'tônico':
                if morfologia_do_pronome == 'não_padrão':
                    if genero == 'masculino':
                        if numero == 'singular':
                            pronome_pessoal_obliquo = 'ele'
                        elif numero == 'plural':
                            pronome_pessoal_obliquo = 'eles'

                    elif genero == 'feminino':
                        if numero == 'singular':
                            pronome_pessoal_obliquo = 'ela'
                        elif numero == 'plural':
                            pronome_pessoal_obliquo = 'elas'
                elif morfologia_do_pronome == 'padrão':
                    pronome_pessoal_obliquo = 'si'

        if transitividade_verbo == 'indireto' and tonicidade == 'tônico':
            if numero == 'singular':
                if pessoa_da_interlocucao == 'falante':
                    pronome_pessoal_obliquo = 'mim'
                elif pessoa_da_interlocucao == 'ouvinte':
                    if morfologia_do_pronome == 'padrão':
                        pronome_pessoal_obliquo = 'ti'
                    else:
                        pronome_pessoal_obliquo = 'você'
            elif numero == 'plural':
                if pessoa_da_interlocucao == 'falante':
                    pronome_pessoal_obliquo = 'nós'
                elif pessoa_da_interlocucao == 'ouvinte':
                    if morfologia_do_pronome == 'padrão':
                        pronome_pessoal_obliquo = 'vós'
                    else:
                        pronome_pessoal_obliquo = 'vocês'

        return pronome_pessoal_obliquo
    except ValueError:
        return ''


def pronome_relativo(tipo_pronome_relativo=None,
                     genero=None, numero=None, indice=None):
    """
    REVISAR: lembrar de operar mudanças nas funções nas quais esta está aninhada

    Retorna o pronome relativo  dados os parâmetros:

    Ex.:
    >>> pronome_relativo(tipo_pronome_relativo='variável',genero='masculino',numero='singular', indice=3)
    'pelo qual'

    >>> pronome_relativo(tipo_pronome_relativo='variável',genero='masculino',numero='plural', indice=3)
    'pelos quais'

    :param tipo_pronome_relativo: 'variável' ('os quais', 'cujos', 'quantos', 'pelos quais'),
                                'invariável' ('quem', 'que', 'a quem', 'a que', 'porque', 'como')
    :param genero: 'masculino','feminino'
    :param numero: 'singular','plural'
    :param indice: entre um integer com índice
    :return:
    """
    pron_relativo = ''
    try:
        if tipo_pronome_relativo == 'variável':
            if numero == "plural":
                if genero == 'masculino':
                    opcoes = ['os quais', 'cujos', 'quantos', 'pelos quais']
                    nums = [x for x in range(len(opcoes))]
                    relativos = dict(zip(nums, opcoes))
                    try:
                        pron_relativo = relativos[indice]
                    except KeyError:
                        pron_relativo = ''

                elif genero == 'feminino':
                    opcoes = ['as quais', 'cujas', 'quantas', 'pelas quais']
                    nums = [x for x in range(len(opcoes))]
                    relativos = dict(zip(nums, opcoes))
                    try:
                        pron_relativo = relativos[indice]
                    except KeyError:
                        pron_relativo = ''

            elif numero == "singular":
                if genero == 'masculino':
                    opcoes = ['o qual', 'cujo', 'quanto', 'pelo qual']
                    nums = [x for x in range(len(opcoes))]
                    relativos = dict(zip(nums, opcoes))
                    try:
                        pron_relativo = relativos[indice]
                    except KeyError:
                        pron_relativo = ''

                elif genero == 'feminino':
                    opcoes = ['a qual', 'cuja', 'quanta', 'pela qual']
                    nums = [x for x in range(len(opcoes))]
                    relativos = dict(zip(nums, opcoes))
                    try:
                        pron_relativo = relativos[indice]
                    except KeyError:
                        pron_relativo = ''

        elif tipo_pronome_relativo == 'invariável':
            opcoes = ['quem', 'que',
                      'a quem', 'a que', 'porque', 'como']
            nums = [x for x in range(len(opcoes))]
            relativos = dict(zip(nums, opcoes))
            try:
                pron_relativo = relativos[indice]
            except KeyError:
                pron_relativo = ''

        return pron_relativo
    except ValueError:
        return ''


def nome_proprio(nome: str = ''):
    """
    Retorna o nome próprio. #Futuramente parte das listas de léxicos
    advindas da anotação na GUM.

    Ex.:
    >>> nome_proprio('andré')
    'André'
    :param nome:
    :return:
    """
    resul = nome
    try:
        return resul.capitalize()
    except ValueError:
        return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retorna palavras nominais')
    pass
