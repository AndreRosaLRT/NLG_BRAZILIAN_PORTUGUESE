##A FAZERES

# Ainda não fiz a interrogativa polar da oração mental
#FAZER A PASSIVA DOS OUTROS TIPOS DE PROCESSO (SO FIZ A MATERIAL)
#REVER BENEFICIÁRIOS NAS MATERIAIS E INSERIR BENEFICIÁRIO NAS INTERROGATIVAS POLARES
#CONTINUAR MEXENDO NO VERBO SABER ABAIXO

def oraçãoTESTE():
    '''
    '''
    Transitividade = 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance'
    Modo = 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito'
    Tema_id = 'TID_default_indicativo_declarativo_TIdentif_NA'
    Tema_interpessoal = TEMA_INTERPESSOAL()
    Tema_textual = TEMA_TEXTUAL()

    if Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance'\
            and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' \
            and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        Circunstância = circunstância()
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''
        print('Há Participante Beneficiário na oração?')
        RECEPÇÃO = choice.Menu(['+beneficiário', '-beneficiário']).ask()
        if RECEPÇÃO == '+beneficiário':
            Beneficiário = frase_preposicional()
        elif RECEPÇÃO == '-beneficiário':
            Beneficiário = ''
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
             print('Qual é o Escopo?')
             tipo_Escopo = choice.Menu (['escopo(processo)','escopo(entidade)']).ask()
             if tipo_Escopo == 'escopo(processo)':
                 Escopo = estrutura_GN()
             elif tipo_Escopo == 'escopo(entidade)':
                 Escopo = estrutura_GN() #por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)

             oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade \
                      + ' ' + Processo + ' ' +  Escopo+' ' + Beneficiário+ ' '+ Circunstância +'.'

    return oração




def formação_verbo_saber_não_orientado():
    verbo_lematizado = 'saber'
    TIPO_OM_NÃO_ORIENTADA = OI_não_orientado()
    if TIPO_OM_NÃO_ORIENTADA == 'infinitivo':
        verbo=verbo_lematizado
    elif TIPO_OM_NÃO_ORIENTADA == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'endo'
        verbo= ME + MI
    elif TIPO_OM_NÃO_ORIENTADA == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ido'
        verbo= ME + MI
    return verbo


def formação_verbo_saber_finito():
    '''
    '''

    verbo_lematizado = 'saber'
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()

        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
                OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = 'sab'
            MI = 'ia'
            verbo = ME + MI


        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = 'sab'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI = 'ia'
                verbo = ME + MI

            else:
                MI = 'ias'
                verbo = ME + MI

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = 'sab'
                MI = 'ia'
                verbo = ME + MI

            else:
                ME = 'sab'
                MI = 'íamos'
                verbo = ME + MI


        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':

            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = 'sab'
                MI = 'ia'
                verbo = ME + MI

            else:
                ME = 'sab'
                MI = 'ís'
                verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
    #         ME = 'er'
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #
    #             MI = 'a'
    #             verbo = ME + MI
    #
    #         else:
    #
    #             MI = 'am'
    #             verbo = ME + MI
    #
    # elif TIPO_OM_FINITA == 'futuro':
    #     ME = verbo_lematizado[slice(-2)]
    #     MI = realização_transitoriedade_futuro()
    #     verbo = ME + MI
    #
    # elif TIPO_OM_FINITA == 'passado_volitivo':
    #     ME = verbo_lematizado[slice(-2)]
    #     MI = realização_transitoriedade_passado_volitivo()
    #     verbo = ME + MI
    #
    #
    #
    # elif TIPO_OM_FINITA == 'presente':
    #     OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
    #     OI_número = choice.Menu(['singular', 'plural']).ask()
    #
    #     if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
    #         ME = verbo_lematizado[slice(-2)]
    #         MI = 'ou'
    #         verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
    #         ME = ''
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'é'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'és'
    #             verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
    #         ME = ''
    #         MI = 'é'
    #         verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             ME = ''
    #             MI = 'é'
    #             verbo = ME + MI
    #
    #         else:
    #             ME = verbo_lematizado[slice(-2)]
    #             MI = 'omos'
    #             verbo = ME + MI
    #
    #     elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
    #         ME = verbo_lematizado[slice(-2)]
    #         MI = 'ois'
    #         verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             ME = ''
    #             MI = 'é'
    #             verbo = ME + MI
    #
    #         else:
    #             ME = verbo_lematizado[slice(-2)]
    #             MI = 'ão'
    #             verbo = ME + MI
    #
    # elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
    #     OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
    #     OI_número = choice.Menu(['singular', 'plural']).ask()
    #     ME = 'f'
    #     if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
    #
    #         MI = 'ui'
    #         verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'oi'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'oste'
    #             verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
    #
    #         MI = 'oi'
    #         verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'oi'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'omos'
    #             verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
    #
    #         MI = 'ostes'
    #         verbo = ME + MI
    #
    #     elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'oi'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'oram'
    #             verbo = ME + MI
    #
    # elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
    #     OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
    #     OI_número = choice.Menu(['singular', 'plural']).ask()
    #     ME = 'f'
    #     if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
    #             OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
    #
    #         MI = 'ora'
    #         verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'ora'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'oras'
    #             verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'ora'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'ôramos'
    #             verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'ora'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'ôreis'
    #             verbo = ME + MI
    #
    #
    #     elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
    #
    #         padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    #         if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
    #             MI = 'ora'
    #             verbo = ME + MI
    #
    #         else:
    #             MI = 'oram'
    #             verbo = ME + MI
    #
    # return verbo
    #

# Sistemas do grupo verbal
from NLG_BRAZILIAN_PORTUGUESE.GENERATION import estrutura_GN

print('Selecione a finitude:')
FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
print('Há a seleção de  tempo secundário')
TEMPO_SECUNDÁRIO = choice.Menu(['-', '1_reiteração', '2_reiterações', '3_reiterações', '4_reiterações']).ask()
print('Qual o aspecto verbal?')
ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
print('Qual a dêixis temporal?')
DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
print('Qual a dêixis modal?')
DÊIXIS_MODAL = choice.Menu(['modalizado_modulação', 'modalizado_modalização', 'não-modalizado']).ask()


def grupo_verbal_teste():
    '''()->str

    Retorna a estrutura que realiza o grupo verbal
    >>>grupo_verbal()
    'ando'
    >>>grupo_verbal()
    'estou andando'
    >>>grupo_verbal()
    'andava'
    '''
    print ('Qual o tipo de evento desejado para o grupo verbal?')
    TIPO_DE_EVENTO = choice.Menu(['Ser','Fazer','Sentir']).ask()

    if TIPO_DE_EVENTO == 'Ser' or TIPO_DE_EVENTO == 'Fazer' or TIPO_DE_EVENTO == 'Sentir':
        print ('Selecione um lema verbal que realize o tipo de evento desejado:')
        print('Qual a agência do GV?')
        AGÊNCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não_agenciado']).ask()

        if AGÊNCIA == 'agenciado_ativa' or AGÊNCIA == 'não_agenciado':
            print('Há a seleção de  tempo secundário')
            TEMPO_SECUNDÁRIO = choice.Menu(['-', '1_reiteração', '2_reiterações',
                                            '3_reiterações', '4_reiterações']).ask()

            if TEMPO_SECUNDÁRIO == '-':
                print ('Dêixis modal = não_modalizada')
                print('Selecione a finitude')
                FINITUDE = choice.Menu(['finito', 'não-finito', 'não-orientado']).ask()
                if FINITUDE == 'finito':
                    print('Qual a dêixis temporal?')
                    DÊIXIS_TEMPORAL = choice.Menu(['presente', 'passado', 'futuro']).ask()
                    if  DÊIXIS_TEMPORAL == 'presente':
                        print('Selecione morfologia de presente e aspecto perfectivo:')
                        grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                    elif  DÊIXIS_TEMPORAL == 'passado':
                        print('Qual o aspecto verbal?')
                        ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                        if ASPECTO == 'perfectivo':
                            print('Selecione morfologia de pretérito perfectivo:')
                            grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                        else:
                            print('Selecione morfologia de pretérito imperfectivo:')
                            grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()
                    elif DÊIXIS_TEMPORAL == 'futuro':
                        grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito()

                elif FINITUDE == 'não-finito':
                    grupo_verbal = formação_da_estrutura_do_verbo_lexical_não_finito()

                elif FINITUDE == 'não-orientado':
                    print('Qual o aspecto verbal?')
                    ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                    if ASPECTO == 'perfectivo':
                        grupo_verbal = formação_verbo_particípio()

                    elif ASPECTO == 'imperfectivo':
                        print('Selecione o tipo de OI não-orientação desejada')
                        não_orientado = choice.Menu(['infinitivo','gerúndio'])

                        if não_orientado == 'infinitivo':
                            verbo_lematizado = input ('Qual o verbo lematizado?')
                            grupo_verbal = verbo_lematizado
                        else:
                            verbo_lematizado = input ('Qual o verbo lematizado?')
                            if verbo_lematizado == 'vir':
                                ME = verbo_lematizado[slice(-2)]
                                MI = realização_transitoriedade_gerúndio()
                                verbo = ME + MI
                                grupo_verbal = verbo
                            elif verbo_lematizado == 'dizer':
                                ME = verbo_lematizado[slice(-2)]
                                MI = realização_transitoriedade_gerúndio()
                                verbo = ME + MI
                                grupo_verbal = verbo
                            else:
                                ME = verbo_lematizado[slice(-2)]
                                MI = realização_transitoriedade_gerúndio()
                                verbo = ME + MI
                                grupo_verbal = verbo

            elif TEMPO_SECUNDÁRIO == '1_reiteração':
                print ('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
                       'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
                       'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal :')
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia do perfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo realiza o Evento?')
                    Evento = verbo_geral2()
                else:
                    print('Selecione morfologia do imperfectivo:')
                    print ('Qual o verbo da primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual o verbo que realiza o Evento?')
                    Evento = formação_da_estrutura_do_verbo_lexical()

                    grupo_verbal = verbo1 + ' ' + Evento


            elif TEMPO_SECUNDÁRIO =='2_reiterações':
                print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
                      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
                      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia do perfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo ocupa a segunda posição no grupo?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo realiza o Evento?')
                    Evento = verbo_geral2()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + Evento

                else:
                    print('Selecione morfologia do imperfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual o verbo ocupa a segunda posição no grupo?')
                    verbo2 = verbo_geral2()
                    print('Qual o verbo realiza o Evento?')
                    Evento = verbo_geral2()

                    grupo_verbal = verbo1 + ' ' +verbo2 + ' ' + Evento

            elif TEMPO_SECUNDÁRIO =='3_reiterações':
                print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
                      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
                      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia do perfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo ocupa a segunda posição no grupo?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo ocupa a terceira posição no grupo?')
                    verbo3 = verbo_geral2()
                    print('Qual verbo realiza o Evento?')
                    Evento = verbo_geral2()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + Evento
                else:
                    print('Selecione morfologia do imperfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual o verbo ocupa a segunda posição no grupo?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo ocupa a terceira posição no grupo?')
                    verbo3 = verbo_geral2()
                    print('Qual o verbo realiza o Evento?')
                    Evento = verbo_geral2()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + Evento

            elif TEMPO_SECUNDÁRIO =='4_reiterações':
                print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
                      'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
                      'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia do perfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo ocupa a segunda posição no grupo?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo ocupa a terceira posição no grupo?')
                    verbo3 = verbo_geral2()
                    print('Qual verbo ocupa a quarta posição no grupo?')
                    verbo4 = verbo_geral2()
                    print('Qual verbo realiza o Evento?')
                    Evento = verbo_geral2()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento
                else:
                    print('Selecione morfologia do imperfectivo:')
                    print('Qual verbo ocupa a primeira posição no grupo?')
                    verbo1 = verbo_geral2()
                    print('Qual o verbo ocupa a segunda posição no grupo?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo ocupa a terceira posição no grupo?')
                    verbo3 = verbo_geral2()
                    print('Qual verbo ocupa a quarta posição no grupo?')
                    verbo4 = verbo_geral2()
                    print('Qual o verbo realiza o Evento?')
                    Evento = verbo_geral2()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento
    

        ####PASSIVA

        elif AGÊNCIA == 'agenciado_passiva':
            print('Quantas reiterações de TEMPO SECUNDÁRIO?')
            TEMPO_SECUNDÁRIO = choice.Menu(['1_reiteração', '2_reiterações','3_reiterações', '4_reiterações']).ask()
            print('Selecione a DÊIXIS_TEMPORAL e FINITUDE respectivas de acordo com as '
                  'seleções de ORIENTAÇÃO_INTERPESSOAL do verbo '
                  'e DÊIXIS_MODAL de acordo com a função dos verbos que compõem o grupo verbal:')
            
            if TEMPO_SECUNDÁRIO == '1_reiteração':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbos_passiva
                else:
                    print('Selecione morfologia de imperfectivo:')
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbos_passiva
            elif TEMPO_SECUNDÁRIO == '2_reiterações':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    print('Qual verbo ocupa a primeira posição do grupo verbal?')
                    verbo1 = verbo_geral2()
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbo1 + ' ' + verbos_passiva
                else:
                    print('Selecione morfologia de imperfectivo:')
                    print('Qual verbo ocupa a primeira posição do grupo verbal?')
                    verbo1 = verbo_geral2()
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbo1 + ' ' + verbos_passiva
            elif TEMPO_SECUNDÁRIO == '3_reiterações':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    print('Qual verbo ocupa a primeira posição do grupo verbal?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo ocupa a segunda posição do grupo verbal?')
                    verbo2 = verbo_geral2()
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' +verbos_passiva
                else:
                    print('Selecione morfologia de imperfectivo:')
                    print('Qual verbo ocupa a primeira posição do grupo verbal?')
                    verbo1 = verbo_geral2()
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' +verbos_passiva
            
            elif TEMPO_SECUNDÁRIO == '4_reiterações':
                print('Qual o aspecto verbal?')
                ASPECTO = choice.Menu(['perfectivo', 'imperfectivo']).ask()
                if ASPECTO == 'perfectivo':
                    print('Selecione morfologia de perfectivo:')
                    print('Qual verbo ocupa a primeira posição do grupo verbal?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo ocupa a segunda posição do grupo verbal?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo ocupa a terceira posição do grupo verbal?')
                    verbo3 = verbo_geral2()
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' '+verbos_passiva
                else:
                    print('Selecione morfologia de imperfectivo:')
                    print('Qual verbo ocupa a primeira posição do grupo verbal?')
                    verbo1 = verbo_geral2()
                    print('Qual verbo ocupa a segunda posição do grupo verbal?')
                    verbo2 = verbo_geral2()
                    print('Qual verbo ocupa a terceira posição do grupo verbal?')
                    verbo3 = verbo_geral2()
                    print('Selecione os verbo da passiva:')
                    verbos_passiva = realização_de_AGÊNCIA_passiva()
                    grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva

    return grupo_verbal


###A FAZER : CONTINUAR A ORAÇÃO mental
## REVER OS PARÂMETROS PASSADAS A CADA UMA DAS FUNÇÕES PARA PODER USAR O JSON
## VER SE VAI PRECISAR SEPARAR AS ORAÇÕES POR TIPO PARA PODER ESTABELECER OS PARÂMETROS PRA CADA
	#UMA DELAS




def ler_json2(json_test):
    
    a = json.load (open('json_test_func.json'))
    return grupo_verbal(a['AGENCIA'], a['TEMPO_SECUNDARIO'], a['FINITUDE'], a['verbo_lematizado'])
	
#sistemas da orção mental
print ('Selecione o tipo de processo mental:')
TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()

print('Qual a FENOMENALIZAÇÃO?')
FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização','fenomenalização']).ask()

    print ('Qual tipo de não-fenomenalização?')
    TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['comportamento-passivo','assunto'])



def oraçãoMental():
    '''
    '''
    Transitividade = TRANSITIVIDADE()
    Modo = MODO()
    Tema_id = TEMA_IDEACIONAL()
    Tema_interpessoal = TEMA_INTERPESSOAL()
    Tema_textual = TEMA_TEXTUAL()

    if Transitividade == 'PR_Mental_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

        print('Selecione o tipo de processo mental:')
        TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
        print('Qual a FENOMENALIZAÇÃO?')
        print('Médio sem alcance: Fenomenalização = não-fenomenalização')
        FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()

        if FENOMENALIZAÇÃO == 'não-fenomenalização':
            print('Qual tipo de não-fenomenalização?')
            print('Médio sem alcance: Não-fenomenalização = comportamento-passivo')
            TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['comportamento-passivo']).ask()

            if TIPO_DE_PROCESSO == 'superior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'comportamento-passivo':
                print('Qual tipo de Processo superior?')
                TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Humanizado)?')
                    Experienciador = estrutura_GN()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + '.'
                    #Ex.: Tenho pensado; Eu pensei a noite toda;
            elif TIPO_DE_PROCESSO == 'inferior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'comportamento-passivo':
                print('Qual tipo de Processo inferior?')
                TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
                    print('Selecione verbo lematizado emotivo ou perceptivo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Animalizado)?')
                    Experienciador = estrutura_GN()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + '.'
                    #'Eu ouvi perfeitamente' - verificar se esse caso se configura como um sem alcance
                    #pois apesar de não esta instanciado, há o potencial de fenômeno

    elif Transitividade == 'PR_Mental_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('Selecione o tipo de processo mental:')
        TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
        print('Qual a FENOMENALIZAÇÃO?')
        FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
        if FENOMENALIZAÇÃO == 'não-fenomenalização':
            print('Médio com alcance, Não-fenomenalização = assunto ')
            print('Qual tipo de não-fenomenalização?')
            TIPO_NÃO_FENOMENALIZAÇÃO = choice.Menu(['assunto']).ask()

            if TIPO_DE_PROCESSO == 'superior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'assunto':
                print('Qual tipo de Processo superior?')
                TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Humanizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o Assunto?')
                    Assunto = circunstância()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '.'
                    #Ex.: Eu sei de futebol.
            elif TIPO_DE_PROCESSO == 'inferior' and TIPO_NÃO_FENOMENALIZAÇÃO == 'assunto':
                print('Qual tipo de Processo inferior?')
                TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Animalizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o Assunto?')
                    Assunto = circunstância()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '.'

        elif FENOMENALIZAÇÃO == 'fenomenalização':
            print('Médio com alcance = mental emanente.')
            print('Qual tipo de fenomenalização?')
            TIPO_FENOMENALIZAÇÃO = choice.Menu(['hiperfenômeno', 'fenômeno_simples']).ask()
            if TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
                print('Qual tipo de Processo superior?')
                TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Humanizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o Fenômeno?')
                    Fenômeno = estrutura_GN()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenômeno + '.'
            elif TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
                print('Qual tipo de Processo superior?')
                TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
                    print('Qual tipo de hiperfenômeno?')
                    print('Projeção = hiperfenômeno: criativo')
                    TIPO_HIPERFENÔMENO = choice.Menu(['criativo']).ask()

                    if TIPO_HIPERFENÔMENO == 'criativo':
                        TIPO_criativo = choice.Menu(['pensamento', 'desejo']).ask()
                        if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
                            TIPO_DE_COGNITIVO = choice.Menu(['pensar', 'saber', 'sonhar']).ask()
                            if TIPO_DE_COGNITIVO == 'pensar' or TIPO_DE_COGNITIVO == 'saber' or TIPO_DE_COGNITIVO == 'sonhar':
                                print('Selecione o verbo lexical correspondente ao Tipo de cognitivo:')
                                print('Qual o Processo?')
                                Processo = grupo_verbal()
                                print('Qual o Experienciador (Ente:Humanizado)?')
                                Experienciador = estrutura_GN()
                                print('Qual o hiperfenômeno projetado? Selecione orientado-finito')
                                Pensamento = oraçãoProjetada()
                                Polaridade = POLARIDADE()
                                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Pensamento
                        elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
                            TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar']).ask()
                            if TIPO_DE_DESIDERATIVO == 'querer' or TIPO_DE_DESIDERATIVO == 'esperar':
                                print('Selecione o verbo lexical correspondente ao Tipo de desiderativo:')
                                print('Qual o Processo?')
                                Processo = grupo_verbal()
                                print('Qual o Experienciador (Ente:Humanizado)?')
                                Experienciador = estrutura_GN()
                                print('Qual o hiperfenômeno projetado?')
                                print('Selecione grupo verbal não-finito_subjuntivo(condicional ou optativo)')
                                Desejo = oraçãoProjetada()
                                Polaridade = POLARIDADE()
                                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + 'que' + ' ' + Desejo

            elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
                print('Qual tipo de Processo inferior?')
                TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Animalizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o Fenômeno?')
                    Fenômeno = estrutura_GN()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo + ' ' + Fenômeno + '.'

            elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
                print('Qual tipo de Processo inferior?')
                TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                print('Qual tipo de hiperfenômeno?')
                TIPO_HIPERFENÔMENO = choice.Menu([ 'reativo']).ask()
                if TIPO_INFERIOR == 'emotivo' and TIPO_HIPERFENÔMENO == 'reativo':
                    print('Qual o tipo de reativo?')
                    TIPO_reativo = choice.Menu(['metafenômeno']).ask()
                    if TIPO_reativo == 'metafenômeno':
                        TIPO_DE_EMOTIVO = choice.Menu(['gostar', 'agradar']).ask()
                        print('Selecione o verbo lexical correspondente ao Tipo de emotivo:')
                        print('Qual o Processo?')
                        Processo = grupo_verbal()
                        print('Qual o Experienciador (Ente:Humanizado)?')
                        Experienciador = estrutura_GN()
                        print('Qual o metafenômeno? Metafenômenos têm natureza abstrata')
                        realização_metafenômeno = choice.Menu(['oração_mudada_ordem', 'oração_que',
                             'GN+oração_qualificadora']).ask()
                        if realização_metafenômeno == 'oração_mudada_ordem':
                            print('Selecione as orientações desejadas:')
                            Metafenômeno = oraçãoProjetada()

                        elif realização_metafenômeno == 'oração_que':
                            print('Selecione orientações desejadas')
                            Metafenômeno = 'que' + ' ' + oraçãoProjetada()
                        else:
                            print('Selecione o GN com oração qualificadora:')
                            Metafenômeno = estrutura_GN()

                        Polaridade = POLARIDADE()
                        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' + Processo +  ' ' + Metafenômeno+'.'

                elif TIPO_INFERIOR == 'perceptivo' and TIPO_HIPERFENÔMENO == 'reativo':
                    print('Qual o tipo de reativo?')
                    TIPO_reativo = choice.Menu(['macrofenômeno']).ask()
                    if TIPO_reativo == 'macrofenômeno':
                        print('Qual o Processo?')
                        Processo = grupo_verbal()
                        print('Qual o Experienciador (Ente:Humanizado)?')
                        Experienciador = estrutura_GN()
                        print('Qual o macrofenômeno? Macrofenômenos têm natureza concreta')
                        realização_macrofenômeno = choice.Menu(['não_finito_concretizado','não-orientado_gerúndio','oração_que',
                                                                'GN+oração_qualificadora']).ask()
                        if realização_macrofenômeno == 'não_finito_concretizado':
                            print('Selecione grupo verbal não-finito_concretizado')
                            Macrofenômeno = oraçãoProjetada()

                        elif realização_macrofenômeno == 'não-orientado_gerúndio':
                            print('Selecione grupo verbal não-orientado_gerúndio')
                            Macrofenômeno = oraçãoProjetada()
                        elif realização_macrofenômeno =='oração_que':
                            print('Selecione orientações desejadas')
                            Macrofenômeno = 'que' + ' '+oraçãoProjetada()
                        else:
                            print('Selecione o GN com oração qualificadora:')
                            Macrofenômeno = estrutura_GN()

                        Polaridade = POLARIDADE()
                        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Experienciador + ' ' + Polaridade + ' ' \
                                 + Processo + ' ' + Macrofenômeno

    elif Transitividade == 'PR_Mental_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print('Efetivo operativo = mental impingente.')
        print('Selecione o tipo de processo mental:')
        TIPO_DE_PROCESSO = choice.Menu(['superior', 'inferior']).ask()
        print('Qual a FENOMENALIZAÇÃO?')
        FENOMENALIZAÇÃO = choice.Menu(['não-fenomenalização', 'fenomenalização']).ask()
        if FENOMENALIZAÇÃO == 'fenomenalização':
            print('Qual tipo de fenomenalização?')
            TIPO_FENOMENALIZAÇÃO = choice.Menu(['hiperfenômeno', 'fenômeno_simples']).ask()
            if TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
                print('Qual tipo de Processo superior?')
                TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Humanizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o Fenômeno Agente?')
                    FenômenoAgente = estrutura_GN()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + FenômenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + '.'
            elif TIPO_DE_PROCESSO == 'superior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
                print('Qual tipo de Processo superior?')
                TIPO_SUPERIOR = choice.Menu(['cognitivo', 'desiderativo', ]).ask()
                if TIPO_SUPERIOR == 'cognitivo' or TIPO_SUPERIOR == 'desiderativo':
                    print('Qual tipo de hiperfenômeno?')
                    print('Projeção = hiperfenômeno: criativo')
                    TIPO_HIPERFENÔMENO = choice.Menu(['criativo']).ask()

                    if TIPO_HIPERFENÔMENO == 'criativo':
                        TIPO_criativo = choice.Menu(['pensamento', 'desejo']).ask()
                        if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
                            TIPO_DE_COGNITIVO = choice.Menu(['pensar', 'saber', 'sonhar']).ask()
                            if TIPO_DE_COGNITIVO == 'pensar' or TIPO_DE_COGNITIVO == 'saber' or TIPO_DE_COGNITIVO == 'sonhar':
                                print('Selecione o verbo lexical correspondente ao Tipo de cognitivo:')
                                print('Qual o Processo?')
                                Processo = grupo_verbal()
                                print('Qual o Experienciador (Ente:Humanizado)?')
                                Experienciador = estrutura_GN()
                                print('Qual o Pensamento Agente? Selecione orientado-finito')
                                PensamentoAgente = oraçãoProjetada()
                                Polaridade = POLARIDADE()
                                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +' ' + 'que' + ' ' + PensamentoAgente  + ' ' + Polaridade + ' ' + Processo + ' '+ Experienciador +'.'
                                #Ex.:PROBABILIDADE BAIXA DE OCORRÊNCIA: Que você não viria ocorreu me

                        elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
                            TIPO_DE_DESIDERATIVO = choice.Menu(['querer', 'esperar']).ask()
                            if TIPO_DE_DESIDERATIVO == 'querer' or TIPO_DE_DESIDERATIVO == 'esperar':
                                print('Selecione o verbo lexical correspondente ao Tipo de desiderativo:')
                                print('Qual o Processo?')
                                Processo = grupo_verbal()
                                print('Qual o Experienciador (Ente:Humanizado)?')
                                Experienciador = estrutura_GN()
                                print('Qual o Desejo Agente?')
                                print('Selecione grupo verbal não-finito_subjuntivo(condicional ou optativo)')
                                DesejoAgente = oraçãoProjetada()
                                Polaridade = POLARIDADE()
                                oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + ' ' + 'que' + ' ' + DesejoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + '.'
                                # Ex.:PROBABILIDADE BAIXA DE OCORRÊNCIA: Que você não viria ocorreu me

            elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'fenômeno_simples':
                print('Qual tipo de Processo inferior?')
                TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                if TIPO_INFERIOR == 'emotivo' or TIPO_INFERIOR == 'perceptivo':
                    print('Selecione verbo lematizado cognitivo ou desiderativo:')
                    print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Animalizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o Fenômeno/Agente?')
                    FenômenoAgente = estrutura_GN()
                    Polaridade = POLARIDADE()

                    oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + FenômenoAgente + ' ' + Polaridade + ' ' + Processo + ' ' + Experienciador + '.'
                    #Ex.: Seus modos entristecem me

            elif TIPO_DE_PROCESSO == 'inferior' and TIPO_FENOMENALIZAÇÃO == 'hiperfenômeno':
                print('Qual tipo de Processo inferior?')
                TIPO_INFERIOR = choice.Menu(['emotivo', 'perceptivo']).ask()
                print('Qual tipo de hiperfenômeno?')
                TIPO_HIPERFENÔMENO = choice.Menu(['reativo']).ask()
                if TIPO_INFERIOR == 'emotivo' and TIPO_HIPERFENÔMENO == 'reativo':
                    print('Qual o tipo de reativo?')
                    TIPO_reativo = choice.Menu(['metafenômeno']).ask()
                    if TIPO_reativo == 'metafenômeno':
                        TIPO_DE_EMOTIVO = choice.Menu(['gostar', 'agradar']).ask()
                        print('Selecione o verbo lexical correspondente ao Tipo de emotivo:')
                        print('Qual o Processo?')
                        Processo = grupo_verbal()
                        print('Qual o Experienciador (Ente:Humanizado)?')
                        Experienciador = estrutura_GN()
                        print('Qual o metafenômeno? Metafenômenos têm natureza abstrata')
                        realização_metafenômeno = choice.Menu(['oração_mudada_ordem', 'oração_que',
                                                               'GN+oração_qualificadora']).ask()
                        if realização_metafenômeno == 'oração_mudada_ordem':
                            print('Selecione as orientações desejadas:')
                            MetafenômenoAgente = oraçãoProjetada()

                        elif realização_metafenômeno == 'oração_que':
                            print('Selecione orientações desejadas')
                            MetafenômenoAgente = 'que' + ' ' + oraçãoProjetada()
                        else:
                            print('Selecione o GN com oração qualificadora:')
                            MetafenômenoAgente = estrutura_GN()

                        Polaridade = POLARIDADE()
                        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' \
                                 + MetafenômenoAgente + ' ' + Polaridade + ' ' \
                                 + Processo + ' ' + Experienciador + '.'

                elif TIPO_INFERIOR == 'perceptivo' and TIPO_HIPERFENÔMENO == 'reativo':
                    print('Qual o tipo de reativo?')
                    TIPO_reativo = choice.Menu(['macrofenômeno']).ask()
                    if TIPO_reativo == 'macrofenômeno':
                        print('Qual o Processo?')
                    Processo = grupo_verbal()
                    print('Qual o Experienciador (Ente:Humanizado)?')
                    Experienciador = estrutura_GN()
                    print('Qual o macrofenômeno? Macrofenômenos têm natureza concreta')
                    realização_macrofenômeno = choice.Menu(
                        ['não_finito_concretizado', 'não-orientado_gerúndio', 'oração_que',
                         'GN+oração_qualificadora']).ask()
                    if realização_macrofenômeno == 'não_finito_concretizado':
                        print('Selecione grupo verbal não-finito_concretizado')
                        MacrofenômenoAgente = oraçãoProjetada()

                    elif realização_macrofenômeno == 'não-orientado_gerúndio':
                        print('Selecione grupo verbal não-orientado_gerúndio')
                        MacrofenômenoAgente = oraçãoProjetada()
                    elif realização_macrofenômeno == 'oração_que':
                        print('Selecione orientações desejadas')
                        MacrofenômenoAgente = 'que' + ' ' + oraçãoProjetada()
                    else:
                        print('Selecione o GN com oração qualificadora:')
                        Macrofenômeno = estrutura_GN()

                    Polaridade = POLARIDADE()
                    oração = Tema_interpessoal + ' ' + Tema_textual \
                             + ' ' + MacrofenômenoAgente + ' ' + Polaridade + ' ' \
                             + Processo + ' ' + Experienciador + '.'


    return oração.capitalize()




                elif FENOMENALIZAÇÃO == 'não-fenomenalização':
			print ('Em caso de orações mentais médio com alcance e Não-fenomenalização seleciona-se a opção: assunto']).ask()
	        Assunto = frase_preposicional()
			
			oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Experienciador  + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '.'
	return oração
		
		

		
		




#
#
#
#
#
# substantivo_lematizado= 'professor'

substantivo_lematizado[-2:] == 'or'



def formação_da_estrutura_do_substantivo_comumteste ():
    '''(str, str)-str
    Retorna a realização de um substantivo comum dados a experiência_do_substantivo
    e as flexões_desejadas.
    >>>formação_da_estrutura_do_substantivo_comum ()
    '''
    substantivo_lematizado = input ('Qual é o substantivo lematizado?')




    if substantivo_lematizado[-1:] == 'x':
        substantivo_comum = substantivo_lematizado

    elif substantivo_lematizado[-1:] == 's':
        tonicidade = choice.Menu(['oxítona', 'paroxítona', 'proparoxítona']).ask()

        if tonicidade == 'paroxítona':
            substantivo_comum = substantivo_lematizado
        elif tonicidade == 'oxítona':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_número = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_número










    elif substantivo_lematizado[-2:] == 'al':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado

        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexão_substantivo = 'ais'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
    elif substantivo_lematizado[-2:] == 'el':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexão_substantivo = 'éis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

    elif substantivo_lematizado[-2:] == 'il':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'is'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
       
    
    elif substantivo_lematizado[-2:] == 'ol':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'óis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


    elif substantivo_lematizado[-2:] == 'ul':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'úis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

    else:
    
        print ('Qual o gênero')
        flexão_gênero_potencial = choice.Menu (['masculino' , 'feminino', 'não_binário']).ask()
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        
        if flexão_gênero_potencial == 'masculino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'o'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo   
            
        elif flexão_gênero_potencial == 'masculino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'os'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo  
        
        
        elif flexão_gênero_potencial == 'não_binário'and número == 'singular' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
            
        elif flexão_gênero_potencial == 'não_binário'and número == 'plural' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
        
    return substantivo_comum










































































































    