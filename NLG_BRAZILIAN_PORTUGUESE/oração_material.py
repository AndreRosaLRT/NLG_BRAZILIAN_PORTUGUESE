
###MATERIAL
from NLG_BRAZILIAN_PORTUGUESE.GENERATION_main import grupo_verbal
import re

def oração_material_dev():
    '''(str,str,str)->str
    Retorna a formação estrutural na lexicogramática
     (oração) de uma figura específica da semântica

    >>> oração_gerar()
    'eu bebi água'
    '''
    Transitividade = TRANSITIVIDADE()
    Modo = MODO()
    Tema_id = TEMA_IDEACIONAL()

    # ORAÇÃO MATERIAL
    # Exemplo (com todas funções extrapoladas, menos P3 Iniciador):
    # Eu enfeitei o bolo(de azul) pra ela
    if (Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo'
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito'):
        Tema_id = TEMA_IDEACIONAL()
        if Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
            Polaridade = POLARIDADE()
            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Ator?')
            Ator = estrutura_GN()
            print('Qual é a Meta?')
            Meta = estrutura_GN()

        print('Selecione os resultados do processo (elaboração-atributos e extensão-beneficiários), se houver:')
        print('Há Resultado_elaboração atributo ou papel?')
        print('Qual a realização do atributo?')
        resultado_atributo = choice.Menu(['adjetivo', 'frase_preposicional', '-resultado_atributo']).ask()
        if resultado_atributo == 'adjetivo':
            Atributo = adjetivo_modificador()
        elif resultado_atributo == 'frase_preposicional':
            Atributo = frase_preposicional()
        else:
            Atributo = ''
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''

        Circunstância = circunstância()

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade \
                 + ' ' + Processo + ' ' + Meta + '  ' + Atributo + ' ' + Beneficiário + ' ' + Circunstância + '.'


    # Exemplo (com todas funções extrapoladas, Cliente em posição não temática, sem INICIADOR):
    # Eu fiz um bolo(azul) pra ela
    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()

        print('Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()
        if CLIENTE == '+cliente':
            Cliente = frase_preposicional()
        else:
            Cliente = ''

        Circunstância = circunstância()
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
                 + ' ' + Meta + ' ' + Cliente + ' ' + Circunstância + '.'
#

    # Exemplo (sem INICIADOR):
    # Eles jogaram tênis

    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()

        print('Há EXPANSÃO do processo?')
        TIPO_DE_EXPANSAO = choice.Menu(['elaboração', 'intensificação']).ask()
        if TIPO_DE_EXPANSAO == 'elaboração':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Escopo + ' ' + Circunstância + '.'

        elif TIPO_DE_EXPANSAO == 'intensificação':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se há distinção ao longo da anotação do corpus)
            print('Há resultado locativo?')
            realização_locativo = choice.Menu(['sim', 'não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
                     + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + ' ' + Circunstância + '.'

#
    # Ex: Gelo formou
    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        print('Há Participante Beneficiário na oração?')

        Circunstância = circunstância()
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade \
                 + ' ' + Processo + ' ' + ' ' + Circunstância + '.'


    # Ela cruzou (sem escopo)(Locativo=até o outro lado)
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()
        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
            print('Orações médio_sem_alcance  selecionam -escopo')

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
                     + ' ' + ' ' + Circunstância + '.'

        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Orações médio_sem_alcance selecionam -escopo')
            print('Há resultado locativo?')
            realização_locativo = choice.Menu(['sim', 'não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Ator + ' ' + Polaridade + ' ' + Processo \
                     + ' ' + Resultado_locativo + ' ' + Circunstância + '.'

        ##MATERIAL METEOROLÓGICA
        ##Segundo Halliday 2014, melhor interpreta-se que as meteorológicas
            # têm o Meio em confluência com o Processo (e podem ou não ter Alcance/escopo)
    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_processo_sem_alcance' \
            and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()
        Polaridade = POLARIDADE()
        print('Tipo de oração sem escopo',end='\n')
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''
        Circunstância = circunstância()

        oração = Tema_interpessoal + ' ' + Tema_textual + ' '  + Polaridade + ' ' + Processo \
                 + ' ' + Beneficiário + ' ' + Circunstância + '.'

    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_processo+alcance' \
         and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' \
         and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()
        Polaridade = POLARIDADE()
        print('Qual estrutura realiza o escopo?')
        realização_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
        if realização_escopo == 'frase_preposicional':
            Escopo = frase_preposicional()
        elif realização_escopo == 'grupo_nominal':
            Escopo = estrutura_GN()
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''
        Circunstância = circunstância()

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Polaridade + ' ' + Processo \
                 + ' ' + Escopo +' ' + Beneficiário+' '+ Circunstância +'.'

        return re.sub(' +', ' ', oração).strip().capitalize()
        # #
        # # # #####testado até aqui


        ##########COMEÇO DE AGENCIAMENTO PASSIVA
        ###CONSEQUENTE MUDANÇA NO TEMA(p/ PROEMINENTE_INTENSIVO_PAPEL TRANSITIVO_
        # NUCLEAR_PARTICIPANTE), sujeito continua recuperado explícito, modo declarativo

    #Ex.: (P2)O bolo foi levado por mim pra ela
    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo_agentivo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_intensivo_relativo_papel_transitivo_nuclear_participante':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual é a Meta?')
        Meta = estrutura_GN()
        print('Qual o Processo?')
        Polaridade = POLARIDADE()
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
        print('Qual é o Ator/Agente?')
        Ator = frase_preposicional()
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''

        Circunstância = circunstância()

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

            print("Qual papel transitivo é selecionado para posição temática? ")
            papel_transit_temático = choice.Menu(["Participante_2", "Participante_3"]).ask()

            if papel_transit_temático == "Participante_2":
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Meta + ' ' + Polaridade \
                         + ' ' + Processo + ' ' + Atributo + ' ' + Ator + ' ' + Beneficiário + ' ' + Circunstância + '.'
            else:
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Beneficiário + ' ' + Polaridade \
                         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Ator  + ' ' + Circunstância + '.'
################################################ PAREI AQUI#################

    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo_agentivo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_intensivo_relativo_papel_transitivo_nuclear_processo':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual é a Meta?')
        Meta = estrutura_GN()
        print('Qual o Processo?')
        Polaridade = POLARIDADE()
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
        print('Qual é o Ator/Agente?')
        Ator = frase_preposicional()
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''

        Circunstância = circunstância()

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

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Processo + ' ' + Polaridade \
                 + ' ' + Meta + ' ' + Atributo + ' ' + Ator + ' ' + Beneficiário + ' ' + Circunstância + '.'


    # Ex.: (P2)O bolo foi levado pra ela/ (P3)Pra ela o bolo foi levado
    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo_não_agentivo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_intensivo_relativo_papel_transitivo_nuclear_participante':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual é a Meta?')
        Meta = estrutura_GN()
        print('Qual o Processo?')
        Polaridade = POLARIDADE()
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''

        Circunstância = circunstância()

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

            print("Qual papel transitivo é selecionado para posição temática? ")
            papel_transit_temático = choice.Menu(["Participante_2", "Participante_3", "Processo"]).ask()

            if papel_transit_temático == "Participante_2":
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Meta + ' ' + Polaridade \
                         + ' ' + Processo + ' ' + Atributo + ' ' + Beneficiário + ' ' + Circunstância + '.'
            elif papel_transit_temático == "Participante_3":
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Beneficiário + ' ' + Polaridade \
                         + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '.'
            else:
                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Processo + ' ' + Polaridade \
                         + ' ' + Meta + ' ' + Atributo + ' ' + Beneficiário + ' ' + Circunstância + '.'





    return (re.sub(' +', ' ', oração).strip().capitalize())

























##########################################################################################################
############################################################################################################


    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE()
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''
        Circunstância = circunstância()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()  ####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''

        print('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu(['+ator/agente', '-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''

        print(
            'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

        if CLIENTE == '+cliente':
            Cliente = frase_preposicional()
        elif CLIENTE == '-cliente':
            Cliente = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' \
                 + Meta + ' ' + Polaridade + ' ' + Processo + ' ' + Cliente +\
                 ' ' + Ator + ' ' + Beneficiário + ' ' + Circunstância + '.'


    ##ORAÇÃO MATERIAL /MODO INTERROGATIVO POLAR/TEMA DEFAULT INTERROGATIVO POLAR

    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textua l =TEMA_TEXTUAL()

        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        Circunstância = circunstância()

        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador' ,'-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal(  )####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''

        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração' ,'extensão' ,'intensificação']).ask()

        if TIPO_DE_RESULTADO == 'elaboração':

            print ('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
                    RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo' ,'frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador ()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Meta + ' ' + Atributo + ' ' + Circunstância + '?'



        elif TIPO_DE_RESULTADO == 'extensão':
            print('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Meta + '  ' + Beneficiário + ' ' + Circunstância + '?'


    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
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
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''

        print(
            'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

        if CLIENTE == '+cliente':
            Cliente = frase_preposicional()
        else:
            Cliente = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                 + ' ' + Processo + ' ' + Meta + ' ' + Cliente + ' ' + Circunstância + '?'


    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''

        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Escopo + ' ' + Circunstância + '?'

        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu(['escopo(processo)', 'escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN()  # por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
            print('Há resultado locativo?')
            realização_locativo = choice.Menu(['sim', 'não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Escopo + ' ' + Resultado_locativo + ' ' + Circunstância + '?'


    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()
        print('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração', 'intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
            print('Orações médio_sem_alcance  selecionam -escopo')
            Escopo = ''

        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Orações médio_sem_alcance selecionam -escopo')

            print('Há resultado locativo?')
            realização_locativo = choice.Menu(['sim', 'não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                     + ' ' + Processo + ' ' + Resultado_locativo + ' ' + Circunstância + '?'

    ##ORAÇÃO MATERIAL, VOZ passiva(no caso de materiais, será necessariamente passivo?)/MODO INTERROGATIVA ELEMENTAL/TEMA ELEMENTAL
    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
                     and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
    and Tema_id == 'TID_complemento_elemental':
         Tema_interpessoal = TEMA_INTERPESSOAL()
         Tema_textual=TEMA_TEXTUAL()

         print ('Qual o Processo?')
         Processo = grupo_verbal() ##selecionar agenciado_passivo
         print('Qual é a Meta?')
         Meta = estrutura_GN()
         Polaridade = POLARIDADE ()
         Circunstância = circunstância()
         print('Há Participante Beneficiário na oração?')
         RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
         if RECEPÇÃO == '+beneficiário':
             Beneficiário = frase_preposicional()
         elif RECEPÇÃO == '-beneficiário':
             Beneficiário = ''
         print ('Há Participante Iniciador na oração?')
         INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
         if INICIADOR == '+iniciador':
             Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
         else:
             Iniciador = ''

         print ('O Ator/Agente é realizado na oração?')
         realização_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
         if realização_Ator == '+ator/agente':
             print('Qual é o Ator/Agente?')
             Ator = frase_preposicional()
         elif realização_Ator == '-ator/agente':
             Ator = ''
         print ('Há resultado do processo?')
         TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()

         if TIPO_DE_RESULTADO == 'elaboração':

             print ('há Resultado_elaboração atributo ou papel?')
             RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
             if (RESULTADO_QUALITATIVO == 'resultado_atributo' or
                 RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                 realização_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
                 if realização_atributo == 'adjetivo':
                     Atributo = adjetivo_modificador ()
                 elif realização_atributo == 'frase_preposicional':
                     Atributo = frase_preposicional()
             elif RESULTADO_QUALITATIVO == '-resultado':
                 Atributo = ''

             oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
                      + ' ' + Processo +' '+ Atributo+ ' ' + Ator +' ' +Beneficiário+' '+ Circunstância +'.'

         elif TIPO_DE_RESULTADO == 'extensão':
             print ('Há Participante Beneficiário na oração?')
             RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
             if RECEPÇÃO == '+beneficiário':
                 Beneficiário = frase_preposicional()
             elif RECEPÇÃO == '-beneficiário':
                 Beneficiário = ''


             oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade \
                      + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +' '+Beneficiário+' '+ Circunstância +'.'

    ##
    #
    #  elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
    #          and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
    #          and Tema_id == 'TID_complemento_elemental':
    #
    #      Tema_interpessoal = TEMA_INTERPESSOAL()
    #      Tema_textual=TEMA_TEXTUAL()
    #
    #      print ('Qual o Processo?')
    #      Processo = grupo_verbal() ##selecionar agenciado_passivo
    #      print('Qual é a Meta?')
    #      Meta = estrutura_GN()
    #      Polaridade = POLARIDADE ()
    #      print('Há Participante Beneficiário na oração?')
    #      RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
    #      if RECEPÇÃO == '+beneficiário':
    #          Beneficiário = frase_preposicional()
    #      elif RECEPÇÃO == '-beneficiário':
    #          Beneficiário = ''
    #      Circunstância = circunstância()
    #
    #
    #      print ('Há Participante Iniciador na oração?')
    #      INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
    #      if INICIADOR == '+iniciador':
    #          Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
    #      else:
    #          Iniciador = ''
    #
    #      print ('O Ator/Agente é realizado na oração?')
    #      realização_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
    #      if realização_Ator == '+ator/agente':
    #          print('Qual é o Ator/Agente?')
    #          Ator = frase_preposicional()
    #      elif realização_Ator == '-ator/agente':
    #          Ator = ''
    #
    #
    #      print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
    #      CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
    #
    #      if CLIENTE == '+cliente':
    #          Cliente = frase_preposicional()
    #      elif CLIENTE == '-cliente':
    #          Cliente=''
    #
    #      oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' \
    #               + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +' ' + Beneficiário+' '+Circunstância +'.'

    ################

    ##ORAÇÃO METEOROLÓGICA MODO INTERROGATIVO POLAR
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' \
            and Modo == 'sujeitabilidade_recuperação_NA_MOD_interrogativo_polar' \
            and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':

        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()

        tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)', 'pessoal']).ask()
        print('Qual o tipo de inTransitividade?')
        if tipo_intransitiva == 'impessoal(fenômeno_natural)':
            print('Há escopo?')
            escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
            if escopo_intransitiva == '+escopo':
                print('Qual estrutura realiza o escopo?')
                realização_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
                if realização_escopo == 'frase_preposicional':
                    Escopo = frase_preposicional()
                elif realização_escopo == 'grupo_nominal':
                    Escopo = estrutura_GN()
            elif escopo_intransitiva == '-escopo':
                Escopo = ''
        print('Qual o Processo?')
        Processo = grupo_verbal()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()

        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Polaridade + ' ' + Processo \
                 + ' ' + Escopo + ' ' + Circunstância + '?'


    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        Tema_textual = TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()
        print('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu(['+iniciador', '-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Ator + ' ' + Polaridade \
                 + ' ' + Processo + ' ' + Circunstância + '?'

        ##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)

    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_complemento_elemental':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
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

        print('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu(['+ator/agente', '-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''

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

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' + Meta \
                     + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo + ' ' + Ator + ' ' + Circunstância + '?'

        elif TIPO_DE_RESULTADO == 'extensão':
            print('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' \
                     + Meta + ' ' + Polaridade + ' ' + Processo + '  ' + Beneficiário + ' ' + Ator + ' ' + Circunstância + '?'

    ##

    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' \
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' \
            and Tema_id == 'TID_complemento_elemental':

        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()

        print('Qual o Processo?')
        Processo = grupo_verbal()  ##selecionar agenciado_passivo
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

        print('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu(['+ator/agente', '-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''

        print(
            'Há Participante Cliente na oração?')  # Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu(['+cliente', '-cliente']).ask()

        if CLIENTE == '+cliente':
            Cliente = frase_preposicional()
        elif CLIENTE == '-cliente':
            Cliente = ''

        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador + ' ' \
                 + Meta + ' ' + Polaridade + ' ' + Processo + ' ' + Cliente + ' ' + Ator + ' ' + Circunstância + '?'












