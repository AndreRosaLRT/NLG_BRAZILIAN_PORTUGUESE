a = json.load (open('json_test.json'))
Transitividade = a["dados_oracao"]["Transitividade"]
Modo = a["dados_oracao"]["Modo"]
Tema_id= a ["dados_oracao"]["Tema_id"]
Tema_interpessoal=a["dados_oracao"]["Tema_interpessoal"]
Tema_textual=a["dados_oracao"]["Tema_textual"]
RECEPTIVIDADE =a["dados_oracao"]["RECEPTIVIDADE"]
ORDEM_DO_DIZENTE=a["ORDEM_DO_DIZENTE"]
TIPO_ATIVIDADE =  a["dados_oracao"]["TIPO_ATIVIDADE"]


def oraçãoVerbal():
    '''(str,str,str)->str
    Retorna a formação estrutural na lexicogramática (oração) de uma figura específica
    da semântica

    >>> oraçãoGerada()
    'eu bebi água'
    '''

    Transitividade = 'PR_Verbal_AG_médio_sem_alcance'
    Modo = 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito'
    Tema_id = 'TID_default_indicativo_declarativo_TIdentif_NA'
    ##ORAÇÃO verbal

    if Transitividade == 'PR_Verbal_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()
        print('Qual a Ordem do Dizente?')
        ORDEM_DO_DIZENTE = choice.Menu(['atividade', 'semioticidade']).ask()
        if ORDEM_DO_DIZENTE == 'atividade':
            TIPO_ATIVIDADE = 'fala'

            if TIPO_ATIVIDADE == 'fala':

                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Dizente?')
                Dizente = estrutura_GN()
                print('Há Receptor?')
                print('Selecione a Receptividade')
                RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
                if RECEPTIVIDADE == '+receptor':
                    Receptor = frase_preposicional()
                else:
                    Receptor = ''
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + '.'
                # Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...


        elif ORDEM_DO_DIZENTE == 'semioticidade':
            print('Semioticidade em Médio sem alcance = não_projeção')
            TIPO_SEMIOTICIDADE = choice.Menu(['não_projeção']).ask()

            if TIPO_SEMIOTICIDADE == 'não_projeção':
                print('Não-projeção + médio sem alcance = -verbiagem')
                TIPO_NÃO_PROJEÇÃO = '-verbiagem'
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Dizente?')
                Dizente = estrutura_GN()
                print('Há Receptor?')
                print('Selecione a Receptividade')
                RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
                if RECEPTIVIDADE == '+receptor':
                    Receptor = frase_preposicional()
                else:
                    Receptor = ''
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + '.'

    elif Transitividade == 'PR_Verbal_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual = TEMA_TEXTUAL()
        print('Qual a Ordem do Dizente?')
        ORDEM_DO_DIZENTE = choice.Menu(['semioticidade']).ask()
        print('Selecione a Receptividade')
        RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()

        if ORDEM_DO_DIZENTE == 'semioticidade':
            print('Selecione o tipo de Semioticidade')

            TIPO_SEMIOTICIDADE = choice.Menu(['projeção', 'não_projeção']).ask()
            if TIPO_SEMIOTICIDADE == 'projeção':
                print('Selecione o tipo de projeção')
                TIPO_PROJEÇÃO = choice.Menu(['citativa', 'relativa']).ask()
                if TIPO_PROJEÇÃO == 'citativa':
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Dizente?')
                    Dizente = estrutura_GN()
                    print('Há Receptor?')
                    print('Selecione a Receptividade')
                    RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
                    if RECEPTIVIDADE == '+receptor':
                        Receptor = frase_preposicional()
                    else:
                        Receptor = ''
                    Polaridade = POLARIDADE()
                    print('Qual a oração projetada?')
                    Oração_projetada = oraçãoProjetada()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + '"' + Oração_projetada + '" ' + '.'
                    # Ex.: Eu disse a ele "Eu comi o bolo".

                elif TIPO_PROJEÇÃO == 'relativa':
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual é o Dizente?')
                    Dizente = estrutura_GN()
                    print('Há Receptor?')
                    print('Selecione a Receptividade')
                    RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
                    if RECEPTIVIDADE == '+receptor':
                        Receptor = frase_preposicional()
                    else:
                        Receptor = ''
                    Polaridade = POLARIDADE()
                    Polaridade = POLARIDADE()
                    print('Qual a oração projetada?')
                    Oração_projetada = oraçãoProjetada()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + ' ' + 'que' + ' ' + '"' + Oração_projetada + '" ' + '.'
                    # Ex.: Eu disse a ele que "Eu comi o bolo".

            elif TIPO_SEMIOTICIDADE == 'não_projeção':
                print('Qual o Processo?')
                Processo = grupo_verbal()
                print('Qual é o Dizente?')
                Dizente = estrutura_GN()
                print('Qual é a Verbiagem?')
                Verbiagem = estrutura_GN()
                print('Há Receptor?')
                print('Selecione a Receptividade')
                RECEPTIVIDADE = choice.Menu(['+receptor', '-receptor']).ask()
                if RECEPTIVIDADE == '+receptor':
                    Receptor = frase_preposicional()
                else:
                    Receptor = ''
                Polaridade = POLARIDADE()

                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Dizente + ' ' + Polaridade + ' ' + Processo + ' ' + Verbiagem + ' ' + Receptor + '.'
    return oração


















