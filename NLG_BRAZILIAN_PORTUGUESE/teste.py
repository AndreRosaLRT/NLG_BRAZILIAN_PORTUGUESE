def oraçãoGeradaTeste():
    '''(str,str,str)->str
    Retorna a formação estrutural na lexicogramática (oração) de uma figura específica
    da semântica

    >>>
    'eu bebi água'
    '''

    Transitividade = TRANSITIVIDADE()
    Modo = MODO()
    Tema_id = TEMA_IDEACIONAL()

    ####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)

    if Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação':
        print ('teste1')
        print('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa', 'meio_receptiva']).ask()

        if direcionalidade_voz == 'meio_operativa':
            print('Neste caso, o Símbolo/Identificado conflui '
                  'com o Sujeito(geralmente o elemento em posição temática')

            # (confluência do Símbolo/Identificado) =

            Tema_textual = TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()

            print('Qual o Processo?')
            Processo = grupo_verbal()
            print('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE()

            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor + '?'

    return oração




a = json.load (open('json_test.json'))
Transitividade = a["dados_oracao"]["Transitividade"]
Modo = a["dados_oracao"]["Modo"]
Tema_id= a ["dados_oracao"]["Tema_id"]
Tema_interpessoal=a["dados_oracao"]["Tema_interpessoal"]
Tema_textual=a["dados_oracao"]["Tema_textual"]
RECEPTIVIDADE =a["dados_oracao"]["RECEPTIVIDADE"]
ORDEM_DO_DIZENTE=a["ORDEM_DO_DIZENTE"]
TIPO_ATIVIDADE =  a["dados_oracao"]["TIPO_ATIVIDADE"]














