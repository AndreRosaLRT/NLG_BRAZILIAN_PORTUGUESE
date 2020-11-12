import re
def Preposição():
    '''
    '''
    modo_inserção = choice.Menu(['inserção_manual',
                                 'inserção_menu']).ask()

    if modo_inserção == 'inserção_manual':
        preposição = input('Escreva a Preposição desejada:')

    else:
        print()
        i = int(input())
        switcher = {
            1: 'a',
            2: 'ante',
            3: 'após',
            4: 'até',
            5: 'com',
            6: 'contra',
            7: 'de',
            8: 'desde',
            9: 'em',
            10: 'entre',
            11: 'para',
            12: 'por',
            13: 'perante',
            14: 'sem',
            15: 'sob',
            16: 'sobre',
            17: 'trás',
        }

        preposição = switcherModo.get(i, 'Seleção nao disponível')
    return preposição












def teste_material():
    '''(str,str,str)->str
       Retorna a formação estrutural na lexicogramática
        (oração) de uma figura específica da semântica

       >>> oração_gerar()
       'eu bebi água'
       '''
    Transitividade = TRANSITIVIDADE()
    Modo = MODO()
    Tema_id = TEMA_IDEACIONAL()



    return (re.sub(' +', ' ', oração).strip().capitalize())





#####################################################################################################################
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''

        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'extensão', 'intensificação']).ask()

        if TIPO_DE_RESULTADO == 'elaboração':

            print('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu(['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
                    RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo', 'frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '.'

        elif TIPO_DE_RESULTADO == 'extensão':
            print('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + ' ' + Circunstância + '.'



# 04/09


def formacao_da_estrutura_do_verbo(verbo,tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                    genero,OI_tipo_de_pessoa, padrao_pessoa_morfologia="Morfologia_padrão" ):
    '''
    (str) -> str

    Retorna um verbo flexionado dados OE_experiência_do_verbo,
    OI_orientação_interpessoal_do_verbo.
    >>> formação_da_estrutura_do_verbo ()
    'levo'
    >>>formação_da_estrutura_do_verbo ()
    'levei'
    '''
    OE_experiência_do_verbo = experiencia_do_verbo(verbo)
    OI_orientação_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                    genero,OI_tipo_de_pessoa, padrao_pessoa_morfologia="Morfologia_padrão")
    return OE_experiência_do_verbo + OI_orientação_interpessoal_do_verbo
#






#########################################################
#Início
def formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia='Morfologia_padrão'):
    '''
    '''
    ME = verbo[slice(-2)]
    if tipo_de_orientacao == 'subjuntivo_condicional':

        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

                MI = 'esse'
                verbo = ME + 'iv' + MI

            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'esse'
                else:
                    MI = 'esses'
                verbo = ME + 'iv' + MI

        elif OI_numero == 'plural':
            if OI_tipo_de_pessoa == '1pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'esse'
                else:
                    MI = 'éssemos'
                verbo = ME + 'iv' + MI

            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'esse'
                else:
                    MI = 'ésseis'
                verbo = ME + 'iv' + MI

            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'esse'
                else:
                    MI = 'essem'
                verbo = ME + 'iv' + MI

    elif tipo_de_orientacao == 'subjuntivo_conjuntivo':
        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

                MI = 'a'
                verbo = ME + 'ej' + MI

            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'as'
                verbo = ME + 'ej' + MI

        elif OI_numero == 'plural':
            if OI_tipo_de_pessoa == '1pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'amos'
                verbo = ME + 'ej' + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'ais'
                verbo = ME + 'ej' + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'am'
                verbo = ME + 'ej' + MI


    elif tipo_de_orientacao == 'imperativo_I':

        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa':
                verbo = 'Imperativos não selecionam 1pessoa do singular'
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                    verbo = ME + 'ej' + MI
                else:
                    MI = 'á'
                    verbo = ME + MI

            elif OI_tipo_de_pessoa == '3pessoa':

                MI = 'a'
                verbo = ME + 'ej' + MI

        elif OI_numero == 'plural':
            if OI_tipo_de_pessoa == '1pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'amos'
                verbo = ME + 'ej' + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                MI = 'ai'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'am'
                verbo = ME + 'ej' + MI

    elif tipo_de_orientacao == 'imperativo_II':

        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa':
                verbo = 'Imperativos não selecionam 1pessoa do singular'
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'as'
                verbo = ME + 'ej' + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                MI = 'a'
                verbo = ME + 'ej' + MI
        if OI_numero == 'plural':
            if OI_tipo_de_pessoa == '1pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'amos'
                verbo = ME + 'ej' + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'ais'
                verbo = ME + 'ej' + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'a'
                else:
                    MI = 'am'
                verbo = ME + 'ej' + MI

    elif tipo_de_orientacao == 'subjuntivo_optativo':

        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa' or OI_tipo_de_pessoa == '3pessoa':

                MI = 'er'
                verbo = ME + 'iv' + MI

            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'er'
                else:
                    MI = 'eres'
                verbo = ME + 'iv' + MI

        elif OI_numero == 'plural':

            if OI_tipo_de_pessoa == '1pessoa':
                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'er'
                else:
                    MI = 'ermos'
                verbo = ME + 'iv' + MI

            if OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'er'
                else:
                    MI = 'erdes'
                verbo = ME + 'iv' + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'er'
                else:
                    MI = 'erem'
                verbo = ME + 'iv' + MI
    elif tipo_de_orientacao == 'pretérito_imperfectivo':

        MI = realizacao_transitoriedade_preterito_imperfectivo(padrao_de_morfologia, OI_numero,
                                                               OI_tipo_de_pessoa, padrao_pessoa_morfologia)
        verbo = ME + MI
    elif tipo_de_orientacao == 'futuro':

        MI = realizacao_transitoriedade_futuro(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
        verbo = ME + MI

    elif tipo_de_orientacao == 'passado_volitivo':

        MI = realizacao_transitoriedade_passado_volitivo(padrao_de_morfologia, OI_numero,OI_tipo_de_pessoa, padrao_pessoa_morfologia)
    elif tipo_de_orientacao == 'presente':
        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa':

                MI = 'ou'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'á'
                else:
                    MI = 'ás'

                verbo = ME + MI

            elif OI_tipo_de_pessoa == '3pessoa':

                MI = 'á'
                verbo = ME + MI
        elif OI_numero == 'plural':
            if (OI_tipo_de_pessoa == '1pessoa' or
                    OI_tipo_de_pessoa == '2pessoa'):

                MI = realizacao_transitoriedade_presente(padrao_de_morfologia, OI_numero,
                                                         OI_tipo_de_pessoa, padrao_pessoa_morfologia)

            elif OI_tipo_de_pessoa == '3pessoa':

                MI = 'ão'
            verbo = ME + MI
    elif tipo_de_orientacao == 'pretérito_perfectivo_I':
        if OI_numero == 'singular':
            if OI_tipo_de_pessoa == '1pessoa':

                MI = 'ive'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'eve'
                else:
                    MI = 'iveste'
                verbo = ME + MI

            elif OI_tipo_de_pessoa == '3pessoa':

                MI = 'eve'
                verbo = ME + MI
        if OI_numero == 'plural':
            if OI_tipo_de_pessoa == '1pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'eve'
                else:
                    MI = 'ivemos'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'eve'
                else:
                    MI = 'ivestes'
                verbo = ME + MI

            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'eve'
                else:
                    MI = 'iveram'
                verbo = ME + MI
    elif tipo_de_orientacao == 'pretérito_perfectivo_II':
        if OI_numero == 'singular':

            if OI_tipo_de_pessoa == '1pessoa':

                MI = 'ivera'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'ivera'
                else:
                    MI = 'iveras'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                MI = 'ivera'
                verbo = ME + MI
        elif OI_numero == 'plural':

            if OI_tipo_de_pessoa == '1pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'ivera'
                else:
                    MI = 'ivéramos'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '2pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'ivera'
                else:
                    MI = 'ivéreis'
                verbo = ME + MI
            elif OI_tipo_de_pessoa == '3pessoa':

                if padrao_pessoa_morfologia == '3pessoa_do_singular':
                    MI = 'ivera'
                else:
                    MI = 'iveram'

                verbo = ME + MI
    elif tipo_de_orientacao == 'não_finito_concretizado':

        MI = realizacao_transitoriedade_nao_finito_concretizado(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                                padrao_pessoa_morfologia)
        verbo = ME + MI

    elif tipo_de_orientacao == 'infinitivo':

        MI = realizacao_transitoriedade_infinitivo(padrao_de_morfologia, OI_numero, OI_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
        verbo = ME + MI

    elif tipo_de_orientacao == 'gerúndio':

        MI = realizacao_transitoriedade_gerundio(padrao_de_morfologia, genero, OI_numero, OI_tipo_de_pessoa,
                                                 padrao_pessoa_morfologia)
        verbo = ME + MI
    elif tipo_de_orientacao == 'particípio':

        MI = realizacao_transitoriedade_participio(padrao_de_morfologia, OI_numero, genero, OI_tipo_de_pessoa,  padrao_pessoa_morfologia)
        verbo = ME + MI

    return verbo

verbo = 'dizer'
verbo[slice(-3)]