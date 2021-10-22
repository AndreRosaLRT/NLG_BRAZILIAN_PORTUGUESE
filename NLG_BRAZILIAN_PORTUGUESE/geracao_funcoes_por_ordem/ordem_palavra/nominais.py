## Cardinais
teste = ("testo", "testo2", "teste3")

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
CENTENAS = ('cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos',
'novecentos')
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
# unidade_dezena_centena([2,2,2], 'feminino')
# unidade_dezena_centena([3,2,2], 'masculino')
# unidade_dezena_centena([3,2,4], 'masculino')
# unidade_dezena_centena([3,2,4], 'feminino')
# unidade_dezena_centena([3,2,2], 'masculino')
# unidade_dezena_centena([3,2,2], 'feminino')
# unidade_dezena_centena([5,2,4], 'masculino')
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


#
# if __name__ == '__main__':
#
#     while True:
#         try:
#             numero = input('Digite um número real: ')
#             extenso = monetario(numero)
#             print(numero, extenso)
#             break
#         except ValueError as erro:
#             print('ERRO!! ', erro)


def ordinal(cardinal, genero):
    """
    :param cardinal:
    :param genero:
    :return: orginal
    """
    num = str(cardinal)
    if genero == 'masculino':
        ordin = num + 'º'
    else:
        ordin = num + 'ª'
    return ordin


print(ordinal(4, 'masculino'))


# #
def porcento(cardinal):
    '''
    '''
    porcento = str(cardinal) + '%'

    return porcento


# porcento(10)
#
# ##NÚMEROS CARDINAIS ATÉ A 4 CASA(9 000) NÃOS SEI SE VOU IMPLEMENTAR ATÉ A 6 CASA.....
# def num_cardinal_1dig_extenso(unidade, genero):
#     if unidade == "zero":
#         numerativo = ''
#     else:
#         if unidade == 'dois':
#             if genero == 'feminino':
#                 numerativo = unidade[slice(-3)] + 'uas'
#             elif genero == 'masculino':
#                 numerativo = unidade
#         elif unidade == 'um':
#             if genero == 'feminino':
#                 numerativo = unidade + 'a'
#             elif genero == 'masculino':
#                 numerativo = unidade
#         else:
#             numerativo = unidade
#
#     return numerativo
#
#
# num_cardinal_1dig_extenso('um','feminino')
# #
# # def num_cardinal_2dig_extenso(dezenaExtenso, unidadeExtenso, genero):
# #     if dezenaExtenso == "zero":
# #         numerativo = num_cardinal_1dig_extenso(unidadeExtenso, genero)
# #     elif dezenaExtenso == 'dez':
# #         if unidadeExtenso == 'zero':
# #             numerativo = dezenaExtenso
# #         elif unidadeExtenso == 'um':
# #             numerativo = 'onze'
# #         elif unidadeExtenso == 'dois':
# #             numerativo = 'doze'
# #         elif unidadeExtenso == 'três':
# #             numerativo = 'treze'
# #         elif unidadeExtenso == 'quatro':
# #             numerativo = 'quatorze'
# #         elif unidadeExtenso == 'cinco':
# #             numerativo = 'quinze'
# #         elif unidadeExtenso == 'seis':
# #             numerativo = 'dezesseis'
# #         elif unidadeExtenso == 'sete':
# #             numerativo = 'dezessete'
# #         elif unidadeExtenso == 'oito':
# #             numerativo = 'dezoito'
# #         elif unidadeExtenso == 'nove':
# #             numerativo = 'dezenove'
# #     else:
# #         digito1 = num_cardinal_1dig_extenso(unidadeExtenso, genero)
# #         if digito1 == "zero":
# #             digito1 = ''
# #         if digito1 == "":
# #             numerativo = dezenaExtenso + digito1
# #         else:
# #             numerativo = dezenaExtenso + ' e ' + digito1
# #
# #     return numerativo
# #
# #
# # # num_cardinal_2dig_extenso('zero','zero','feminino')
# #
# # def num_cardinal_3dig_extenso(centenaExtenso, dezenaExtenso, unidadeExtenso, genero):
# #     if centenaExtenso == "zero":
# #         numerativo = num_cardinal_2dig_extenso(dezenaExtenso, unidadeExtenso, genero)
# #     else:
# #         digitos2 = num_cardinal_2dig_extenso(dezenaExtenso, unidadeExtenso, genero)
# #
# #         if digitos2 == '':
# #             if (centenaExtenso == 'duzentos' or centenaExtenso == 'trezentos' or
# #                     centenaExtenso == 'quatrocentos' or centenaExtenso == 'quinhentos' or
# #                     centenaExtenso == 'seiscentos' or centenaExtenso == 'setecentos' or
# #                     centenaExtenso == 'oitocentos' or centenaExtenso == 'novecentos'):
# #                 if genero == 'feminino':
# #                     centena = centenaExtenso[slice(-2)] + 'as'
# #                 elif genero == 'masculino':
# #                     centena = centenaExtenso[slice(-2)] + 'os'
# #                 numerativo = centena + digitos2
# #             else:
# #                 numerativo = centenaExtenso
# #         else:
# #             if centenaExtenso == 'cem':
# #                 centena = 'cento e '
# #
# #             elif (centenaExtenso == 'duzentos' or centenaExtenso == 'trezentos' or
# #                   centenaExtenso == 'quatrocentos' or centenaExtenso == 'quinhentos' or
# #                   centenaExtenso == 'seiscentos' or centenaExtenso == 'setecentos' or
# #                   centenaExtenso == 'oitocentos' or centenaExtenso == 'novecentos'):
# #                 if genero == 'feminino':
# #                     centena = centenaExtenso[slice(-2)] + 'as e '
# #                 elif genero == 'masculino':
# #                     centena = centenaExtenso[slice(-2)] + 'os e '
# #
# #             numerativo = centena + digitos2
# #
# #     return numerativo
# #
# #
# # # num_cardinal_3dig_extenso('duzentos','zero','zero', 'feminino')
# #
# # def num_cardinal_4dig_extenso(milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
# #                               genero):  # Número com 4 dígitos
# #     if milharExtenso == "zero":
# #         numerativo = num_cardinal_3dig_extenso(centenaExtenso, dezenaExtenso, unidadeExtenso, genero)
# #     else:
# #         digito3 = num_cardinal_3dig_extenso(centenaExtenso, dezenaExtenso, unidadeExtenso, genero)
# #         if digito3 == '':
# #             if milharExtenso == 'dois mil':
# #                 if genero == 'masculino':
# #                     milhar = milharExtenso
# #
# #                 elif genero == 'feminino':
# #                     milhar = milharExtenso[:1] + 'uas' + milharExtenso[4:]
# #             else:
# #                 milhar = milharExtenso
# #         else:
# #             milhar = milharExtenso
# #             numerativo = milhar + " e " + digito3
# #
# #     return numerativo


# num_cardinal_4dig_extenso('zero','trezentos', 'zero', 'três', 'feminino')

# tipoRealCard = choice.Menu(['extenso', 'numérico']).ask()
#
# def num_cardinal(tipoRealCard, cardNumerico, milharExtenso,
#                  centenaExtenso, dezenaExtenso, unidadeExtenso, genero):
#     if tipoRealCard == 'numérico':
#         numCardinal = cardNumerico
#
#     elif tipoRealCard == 'extenso':
#         numCardinal = num_cardinal_4dig_extenso(milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso, genero)
#
#     return numCardinal


# num_cardinal("extenso", None, 'zero','duzentos', 'zero', 'zero', 'feminino')
#
# funcaoNumerativo = choice.Menu(['quant_precisa_absoluta(cardinais)',
# 		                                 'quant_precisa_div/multi(fração/multiplicativos)',
# 		                                 'quant_imprecisa_pron_indef_numer',
# 		                                 'quant_imprecisa_pron_indef_valor_alt_baixo',
# 		                                 'ordem_lugar_preciso(ordinal)',
# 		                                 'ordem_lugar_impreciso(posição_relativa'
# 		                                 ]).ask()
# print("""
#                     'algum'
#                     'nenhum'
#                     3: 'todo'
#                     4: 'muito'
#                     5: 'pouco'
#                     6: 'vário'
#                     7: 'tanto'
#                     8: 'outro'
#                     9: 'quanto'
#                     10: 'alguma'
#                     1'nenhuma'
#                     1'toda'
#                     13: 'muita'
#                     14: 'pouca'
#                     15: 'vária'
#                     1'tanta'
#                     17:'outra'
#                     18: 'quanta'
#                     19:'alguns'
#                     20:'nenhuns'
#                     21:'todos'
#                     22:'muitos'
#                     23:'poucos'
#                     24:'vários'
#                     25:'tantos'
#                     26:'outros'
#                     27:'quantos'
#                     28:'algumas'
#                     29:'nenhumas'
#                     30:'todas'
#                     31:'muitas'
#                     32:'poucas'
#                     33:'várias'
#                     34:'tantas'
#                     35:'outras'
#                     36:'quantas'
#
#                                Escolha uma opção:""")


def Numerativo(funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
               milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None):
    '''
    '''
    try:
        if funcaoNumerativo == 'ordem_lugar_preciso(ordinal)':
            Numerativo = ordinal(cardinal, genero)

        elif funcaoNumerativo == 'quant_precisa_div/multi(fração/multiplicativos)':
            if tipo_precisa == 'porcentagem':
                Numerativo = porcento(cardinal)

        elif funcaoNumerativo == 'quant_precisa_absoluta(cardinais)':
            Numerativo = num_cardinal(tipoRealCard, cardinal, milharExtenso, centenaExtenso,
                                      dezenaExtenso, unidadeExtenso, genero)
        elif funcaoNumerativo == 'quant_imprecisa_pron_indef_numer':
            Numerativo = numIndefinido
        else:
            Numerativo = ''

        return Numerativo
    except:
        Numerativo = ''
        return Numerativo


#
# # ordinal
# Numerativo()
# Numerativo('ordem_lugar_preciso(ordinal)','2','feminino',None,None,
# 			   None,None,None,None,None)
# #cardinal
# Numerativo('quant_precisa_absoluta(cardinais)',None,'feminino',None,"extenso",
# 			   "zero","duzentos","zero","zero",None)
#
# def NumerativoIndefinidoSwitcher():
# 	i = int(input())
#
# 	switcherNumInd = {
# 		'algum',
# 		'nenhum',
# 		3: 'todo', \
# 		4: 'muito',
# 		5: 'pouco',
# 		6: 'vário',
# 		7: 'tanto',
# 		8: 'outro',
# 		9: 'quanto',
# 		10: 'alguma',
# 		1'nenhuma',
# 		1'toda',
# 		13: 'muita',
# 		14: 'pouca',
# 		15: 'vária',
# 		16: 'tanta',
# 		17: 'outra',
# 		18: 'quanta',
# 		19: 'alguns',
# 		20: 'nenhuns',
# 		2'todos',
# 		2'muitos',
# 		23: 'poucos',
# 		24: 'vários',
# 		25: 'tantos',
# 		26: 'outros',
# 		27: 'quantos',
# 		28: 'algumas',
# 		29: 'nenhumas',
# 		30: 'todas',
# 		3'muitas',
# 		3'poucas',
# 		33: 'várias',
# 		34: 'tantas',
# 		35: 'outras',
# 		36: 'quantas',
# 	}
#
# 	return switcherNumInd.get(i, 'Seleção nao disponível')

# #
# # #
# #
# # ###A palavra nominal que realiza o Ente no GRUPO NOMINAL- Flexiona para nos eixos:
# # #     Gênero, Número, Grau. Por enquanto, vou trabalhar apenas com Gênero e número.(ORDEM DA PALAVRA AINDA)
# # # COMECEI APENAS COM SUBSTANTIVOS QUE SÃO REGULARES NAS SUAS FLEXÕES: gato:gatos:gatas:

def detectaExpSubstantivo(substantivo, genero, numero):  ##dado o substantivo flexionado##
    '''(str,str,str)->

    Retorna o morfema que realiza a experiência em um substantivo, dados
    o substantivo flexionado, o gênero e o numero.

    >>>detectaExpSubstantivo('','masculino','plural')
    'gat'
    '''

    if genero == 'masculino' and numero == 'singular':
        raizSubs = (substantivo[slice(-1)])

    elif genero == 'feminino' and numero == 'singular':
        raizSubs = (substantivo[slice(-1)])

    elif genero == 'masculino' and numero == 'plural':
        raizSubs = (substantivo[slice(-2)])

    elif genero == 'feminino' and numero == 'plural':
        raizSubs = (substantivo[slice(-2)])
    return raizSubs


# detectaExpSubstantivo('gatos','masculino','plural')
# #
# # # OS LEMAS QUE SERVIRÃO PARA  FUNÇÃO QUE SEGUE VIRÃO DA ANOTAÇÃO NA ONTOLOGIA:
# # #        o que na ontologia tiver anotado como Thing, vai servir como um
# # ##        banco lexical do qual o operador vai selecionar(não sei ainda se
# # #        vai ser importado automaticamente ou se vou ter de inserir manualmente
# # #        )
# #
# genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
# lemaSubs = input('Qual é o substantivo lematizado?')


def realizaExpSubstantivo(lemaSubs, genero):  ##dado o substantivo_lematizado- por enquanto, apenas para
    ##substantivos regulares, com foco em masculino-feminino, singular plural. Tenho que considerar desenvolver
    #    com relação aos diferentes tipos de radicais (primitivo, derivado, composto, simples...)
    '''(str)-> str

    Retorna o morfema que realiza a experiência em um substantivo, dado
    o substantivo lematizado.

    >>>realizaExpSubstantivo()
    'gat'
    '''
    if genero == 'masculino' or genero == 'feminino':
        morfExpSubs = lemaSubs[slice(-1)]

    elif genero == 'não-binário':
        morfExpSubs = lemaSubs

    return morfExpSubs


# realizaExpSubstantivo('gata','masculino')
# #

def realizacao_flexoes_substantivos(genero, numero):
    '''(str,str,str)->

    Retorna os morfemas que realizam as flexões de genero e numero dados
    a experiência do substantivo e os genero e numeros desejados.

    genero = choice.Menu(['masculino', 'feminino', 'não-binário']).ask()
    numero = choice.Menu(['singular', 'plural']).ask()
    >>>realizacao_flexoes_substantivos()
    'os'
    '''

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
# print('Escolha o tipo_pessoa de feminino:')
# tipo_feminino_ÃO = choice.Menu(['oa', 'ona', 'ã', 'esa', 'casos_exceção']).ask()
#
# print('Escolha o tipo_pessoa de plural:')
# tipo_masc_ÃO = choice.Menu(['ãos', 'ões', 'ães']).ask()

# terminado em 's':;;;tonicidade = choice.Menu(['oxítona', 'paroxítona', 'proparoxítona']).ask()

def substantivo_comum(substantivo_lematizado, numero,
                      genero, tipo_feminino_ÃO,
                      tipo_masc_ÃO, acentTonica):
    """
    """

    if substantivo_lematizado[-1:] == 'm':

        if numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'ns'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'or':

        if genero == 'masculino' and numero == 'singular':

            substantivo_comum = substantivo_lematizado

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'masculino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo
    elif substantivo_lematizado[-2:] == 'ão':

        if (genero == 'masculino' and numero == 'singular'
                or genero == 'não-binário' and numero == 'singular'):
            substantivo_comum = substantivo_lematizado

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino_ÃO

        elif (genero == 'masculino' and numero == 'plural'
              or genero == 'não-binário' and numero == 'plural'):

            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            substantivo_comum = morfema_experiencial_do_substantivo + tipo_masc_ÃO + 's'

        elif genero == 'feminino' and numero == 'plural':

            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            substantivo_comum = morfema_experiencial_do_substantivo + tipo_feminino_ÃO + 's'

    elif substantivo_lematizado[-1:] == 'x':
        substantivo_comum = substantivo_lematizado

    elif substantivo_lematizado[-1:] == 's':
        if acentTonica == 'paroxítona':
            substantivo_comum = substantivo_lematizado
        elif acentTonica == 'oxítona':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_numero = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_numero

    elif (substantivo_lematizado[-1:] == 'r' or substantivo_lematizado[-1:] == 'z'):

        if genero == 'masculino' and numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'masculino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'al':
        if numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'ais'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'el':

        if numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'éis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'il':

        if numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'is'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'ol':

        if numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'óis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    elif substantivo_lematizado[-2:] == 'ul':

        if numero == 'singular':
            substantivo_comum = substantivo_lematizado

        elif numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexao_substantivo = 'úis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    else:

        if genero == 'masculino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'o'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'masculino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'os'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'feminino' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexao_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'singular':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

        elif genero == 'não-binário' and numero == 'plural':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexao_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexao_substantivo

    return substantivo_comum


#
# substantivo_comum("ancião",'plural',"masculino", None,"ão",None)
# substantivo_comum("artesão",'singular',"feminino", "ã",None,None)
#
# substantivo_comum("carro","plural","não-binário", None, None,None)
# substantivo_comum("varal","plural", "não-binário", None, None,None)

# # # ADJETIVOS

def deteccao_experiencia_do_adjetivo(adjetivo, genero, numero):  ##dado o adjetivo flexionado##
    '''(str,str,str)->

    Retorna o morfema que realiza a experiência em um adjetivo, dados
    o adjetivo flexionado, o gênero e o número.

    >>>deteccao_experiencia_do_adjetivo()
    'esportiv'
    '''

    if numero == 'singular':
        if genero == 'masculino':
            raiz_experiencial_adjetivo = (adjetivo[slice(-1)])

        elif genero == 'feminino':
            raiz_experiencial_adjetivo = (adjetivo[slice(-1)])
    elif numero == 'plural':
        if genero == 'masculino':
            raiz_experiencial_adjetivo = (adjetivo[slice(-2)])

        elif genero == 'feminino':
            raiz_experiencial_adjetivo = (adjetivo[slice(-2)])

    return raiz_experiencial_adjetivo


# deteccao_experiencia_do_adjetivo("esperto","masculino","singular")
# #


def realizacao_experiencia_do_adjetivo(adjetivo_lematizado, genero):
    '''(str)-> str
    genero = choice.Menu(['masculino/feminino', 'não-binário']).ask()
    adjetivo_lematizado =

    Retorna o morfema que realiza a experiência em um adjetivo, dado
    o adjetivo lematizado.

    >>>realizacao_experiencia_do_adjetivo()
    'gat'
    '''

    if genero == 'masculino/feminino':
        morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]

    elif genero == 'não-binário':
        morfema_experiencial_do_adjetivo = adjetivo_lematizado

    return morfema_experiencial_do_adjetivo


# realizacao_experiencia_do_adjetivo("esperto","masculino/feminino")

def realizacao_flexoes_adjetivos(genero, numero):
    """
    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do adjetivo e os gênero e números desejados.

    :param genero: 'masculino', 'feminino', 'não-binário'
    :param numero: 'singular', 'plural'
    :return: morfema_flexao_adjetivo
    """

    if numero == 'singular':
        if genero == 'masculino':
            morfema_flexao_adjetivo = 'o'

        elif genero == 'feminino':
            morfema_flexao_adjetivo = 'a'
        elif genero == 'não-binário':
            morfema_flexao_adjetivo = ''

    elif numero == 'plural':
        if genero == 'masculino':
            morfema_flexao_adjetivo = 'os'

        elif genero == 'feminino' and numero == 'plural':
            morfema_flexao_adjetivo = 'as'

        elif genero == 'não-binário':
            morfema_flexao_adjetivo = 's'

    return morfema_flexao_adjetivo


def adjetivo(adjetivo_lematizado=None, genero=None, numero=None):
    """
    Retorna a realizacao de um adjetivo comum dados a experiência_do_adjetivo
    e as flexões_desejadas.
    :param adjetivo_lematizado:
    :param genero:
    :param numero:
    :return:
    """
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
    except:
        adj = ''
        return adj


# print(adjetivo('sim','alto','feminino','singular'))
# print(adjetivo('sim','alto','feminino','singular'))


# #
# # # PRONOMES#
# #
# # # PEGUEI OS PRONOMES BÁSICOS# QUANDO CHEGAR NA ORAÇÃO, A MORFOLOGIA DOS VERBOS
# # # FICA UM POUCO SUBVERSIVA

def realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero, numero, morfologia_do_pronome="de_terceira_pessoa"):
    '''(str)->str
    Retorna o pronome adequado dado uma pessoa da intelocução.
    pessoa_da_interlocucao = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
    numero = choice.Menu(['singular', 'plural']).ask()
    morfologia_do_pronome = choice.Menu(['padrão', 'de_terceira_pessoa']).ask()
    >>>realizacao_pronominal_casoreto ('','')
    'eu'
    '''

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


# realizacao_pronominal_casoreto("não_interlocutor", "feminino", "singular", morfologia_do_pronome="de_terceira_pessoa")


def realizacao_pronome_caso_obliquo(transitividade_verbo=None, tonicidade=None, pessoa_da_interlocucao=None,
                                    numero=None,
                                    genero=None, morfologia_do_pronome=None, reflexivo=False):
    '''(str)->str
    Retorna o pronome oblíquo adequado dado uma pessoa da intelocução.
    tonicidade = choice.Menu(['átono', 'tônico']).ask()
    pessoa_da_interlocucao = choice.Menu(['falante', 'ouvinte', 'não_interlocutor']).ask()
    numero = choice.Menu(['singular', 'plural']).ask()
    morfologia_do_pronome = choice.Menu(['padrão', 'não_padrão']).ask()
    transitividade_verbo =choice.Menu(['direto','direto_preposicionado, 'indireto']).ask()
    >>>realizacao_pronominal_caso_oblíquo ()
    'me'
    '''
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

    if reflexivo == True:
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


#
# #me
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='falante', numero='singular', genero=None, morfologia_do_pronome=None, reflexivo=False)
# #te
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='ouvinte', numero='singular', genero=None, morfologia_do_pronome=None, reflexivo=False)
# #nos
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='falante', numero='plural', genero=None, morfologia_do_pronome=None, reflexivo=False)
# #vos
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='ouvinte', numero='plural', genero=None, morfologia_do_pronome=None, reflexivo=False)
#
#
# #o
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='masculino', morfologia_do_pronome='padrão', reflexivo=False)
# #ele
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='masculino', morfologia_do_pronome='não_padrão', reflexivo=False)
# #a
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='feminino', morfologia_do_pronome='padrão', reflexivo=False)
# #ela
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero='feminino', morfologia_do_pronome='não_padrão', reflexivo=False)
# #os
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='masculino', morfologia_do_pronome='padrão', reflexivo=False)
# #eles
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='masculino', morfologia_do_pronome='não_padrão', reflexivo=False)
#
# #as
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='feminino', morfologia_do_pronome='padrão', reflexivo=False)
# #elas
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='feminino', morfologia_do_pronome='não_padrão', reflexivo=False)
# #elas
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero='feminino', morfologia_do_pronome='padrão', reflexivo=False)
#
#
# #se
# realizacao_pronome_caso_obliquo(transitividade_verbo=None, tonicidade=None, pessoa_da_interlocucao=None, numero=None, genero=None, morfologia_do_pronome=None, reflexivo=True)
# #lhe
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='singular', genero=None, morfologia_do_pronome=None, reflexivo=None)
#
# #lhes
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='átono', pessoa_da_interlocucao='não_interlocutor', numero='plural', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
#
# #mim
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='falante', numero='singular', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
# #ti
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='singular', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
#
# #você
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='singular', genero=None, morfologia_do_pronome='não_padrão', reflexivo=None)
#
#
# #nós
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='falante', numero='plural', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
# #vós
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='plural', genero=None, morfologia_do_pronome='padrão', reflexivo=None)
#
# #você
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto', tonicidade='tônico', pessoa_da_interlocucao='ouvinte', numero='plural', genero=None, morfologia_do_pronome='não_padrão', reflexivo=None)
#
# ##me
# realizacao_pronome_caso_obliquo(transitividade_verbo='direto', tonicidade='átono', pessoa_da_interlocucao='falante',
# 									numero='singular',genero=None, morfologia_do_pronome=None, reflexivo=False)
#
#
# realizacao_pronome_caso_obliquo("indireto",'tônico',"não_interlocutor",'singular','feminino',"padrão")
# realizacao_pronome_caso_obliquo(transitividade_verbo='indireto',tonicidade='átono',pessoa_da_interlocucao='não_interlocutor',
# 								numero='plural',genero=None,morfologia_do_pronome='padrão',reflexivo=False)

#
# estrutura_GN(None, None, None,None,
# 				 None, None, None, None,
# 				None, None,None,
# 				 None,None, None,
# 				 None, None, None,
# 				 None, None, None, None,
# 				 None, None, None,None,
# 				 None, None,None,
# 				'consciente', None, None,
# 				 None, 'pronome_caso_oblíquo',None,
# 				 'singular',None, None, None, None,
# 				'falante','direto','átono', "padrão",
# 				None, None, None,None,
# 				 None,None, None,None)

##TENHO QUE VER SE FAZ SENTIDO MUDAR ESTA(inserir parâmetros??)
# modo_inserção = choice.Menu(['inserção_manual', 'inserção_menu']).ask()
# print('Qual tipo_pessoa de relativo?')
# tipo_pronome_relativo = choice.Menu(['variável', 'invariável']).ask()
#

def pronome_relativo(tipo_insercao="inserção_menu", pron_extenso=None, tipo_pronome_relativo=None,
                     genero=None, numero=None, indice=None):
    """

    :param tipo_insercao: 'inserção_manual', 'inserção_menu'
    :param pron_extenso: entre o pronome
    :param tipo_pronome_relativo: 'variável', 'invariável'
    :param genero: 'masculino','feminino'
    :param numero: 'singular','plural'
    :param indice: entre um integer com índice
    :return:
    """
    try:
        if tipo_insercao == 'inserção_manual':
            pronome_relativo = pron_extenso

        elif tipo_insercao == 'inserção_menu':

            if tipo_pronome_relativo == 'variável':
                if numero == "plural":
                    if genero == 'masculino':
                        opcoes = ['os quais', 'cujos', 'quantos', 'pelos quais']
                        nums = [x for x in range(len(opcoes))]
                        relativos = dict(zip(nums, opcoes))
                        pronome_relativo = relativos[indice]

                    elif genero == 'feminino':
                        opcoes = ['as quais', 'cujas', 'quantas', 'pelas quais']
                        nums = [x for x in range(len(opcoes))]
                        relativos = dict(zip(nums, opcoes))
                        pronome_relativo = relativos[indice]

                elif numero == "singular":
                    if genero == 'masculino':
                        opcoes = ['o qual', 'cujo', 'quanto', 'pelo qual']
                        nums = [x for x in range(len(opcoes))]
                        relativos = dict(zip(nums, opcoes))
                        pronome_relativo = relativos[indice]

                    elif genero == 'feminino':
                        opcoes = ['a qual', 'cuja', 'quanta', 'pela qual']
                        nums = [x for x in range(len(opcoes))]
                        relativos = dict(zip(nums, opcoes))
                        pronome_relativo = relativos[indice]

            elif tipo_pronome_relativo == 'invariável':
                opcoes = ['quem', 'que',
                          'a quem', 'a que', 'porque', 'como']
                nums = [x for x in range(len(opcoes))]
                relativos = dict(zip(nums, opcoes))
                pronome_relativo = relativos[indice]

        return pronome_relativo
    except:
        pronome_relativo = ''
        return pronome_relativo


# pronome_relativo()
# pronome_relativo(tipo_insercao="inserção_menu",pron_extenso=None,tipo_pronome_relativo='variável',genero='masculino',numero='singular', indice=3)
# pronome_relativo(tipo_insercao="inserção_menu",pron_extenso=None,tipo_pronome_relativo='variável',genero='masculino',numero='plural', indice=3)
# #
pronome_relativo(tipo_insercao="inserção_menu", pron_extenso=None, tipo_pronome_relativo='invariável', indice=3)


# #
# # ##PRECISO IMPLEMENTAR LETRA MAIÚSCULA NO CASO DE INICIO DE FRASE.
# # # SUBSTANTIVOS PRÓPRIOS VIRÃO DA LISTA DE NOMES PRÓPRIOS ANOTADOS NA GUM
# # # Por enquanto, vou deixar um input
# #

def nome_proprio(nome=None):
    '''(str)->str
    Retorna o nome próprio. #Futuramente parte das listas de léxicos
    advindas da anotação na GUM.
    '''
    resul = nome
    try:
        return resul.capitalize()
    except:
        resul = ''
        return resul

# nome_proprio('andre')
