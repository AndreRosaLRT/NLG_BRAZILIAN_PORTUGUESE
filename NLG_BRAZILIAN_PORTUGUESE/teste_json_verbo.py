import json


import json


a = json.load(open('C:/Users/andre/Documents/GitHub/NLG_BRAZILIAN_PORTUGUESE_19-11/NLG_BRAZILIAN_PORTUGUESE/json_test_adverbio.json'))


for i in range(len(a["info"])):
    adv = adverbio(a["info"][i]["modo_insercao"],a["info"][i]["tipo_de_adverbio"],a["info"][i]["i"])
    print(adv)
    i+=1


###############################


def formação_da_estrutura_do_verbo_lexical(verbo_lematizado):
    '''
    '''

    # inserir verbos irregulares
    if verbo_lematizado == 'estar':
        verbo = formação_verbo_estar()
    elif verbo_lematizado == 'ser':
        verbo = formação_verbo_ser()
    elif verbo_lematizado == 'ir':
        verbo = formação_verbo_ir()
    elif (
            verbo_lematizado == 'vir'
            or verbo_lematizado == 'intervir'
    ):
        verbo = formação_verbo_vir_intervir()
    elif verbo_lematizado == 'haver':
        verbo = formação_verbo_haver()
    elif verbo_lematizado == 'ter':
        verbo = formação_verbo_ter()
    elif verbo_lematizado == 'dizer':
        verbo = formação_verbo_dizer()
    elif verbo_lematizado == 'saber':
        verbo = formação_verbo_saber()
    elif verbo_lematizado == 'fazer':
        verbo = formação_verbo_fazer()
    elif verbo_lematizado == 'medir':
        verbo = formação_verbo_medir()
    elif verbo_lematizado == 'dever':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_do_verbo()
        verbo = ME + MI
    elif verbo_lematizado == 'poder':
        verbo = formação_verbo_poder()

    else:
        ME = (verbo_lematizado[slice(-2)])
        MI = realização_transitoriedade_do_verbo_finito()
        verbo = ME + MI

    return verbo

def realização_transitoriedade_do_verbo_finito(TIPO_OM_FINITA):
    '''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realização_transitoriedade_do_verbo ()
    'o'

    '''

    # TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()

    if TIPO_OM_FINITA == 'presente':
        MI = realização_transitoriedade_presente(padrão_de_morfologia,OI_tipo_de_pessoa,OI_número)
        return MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        MI = realização_transitoriedade_pretérito_perfectivo_I()
        return MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        MI = realização_transitoriedade_pretérito_perfectivo_II()
        return MI

    elif TIPO_OM_FINITA == 'pretérito_imperfectivo':
        MI = realização_transitoriedade_pretérito_imperfectivo()
        return MI

    elif TIPO_OM_FINITA == 'passado_volitivo':
        MI = realização_transitoriedade_passado_volitivo()
        return MI

    elif TIPO_OM_FINITA == 'futuro':
        MI = realização_transitoriedade_futuro()
        return MI

def OI_ORIENTAÇÃO_MODAL_FINITO(OI_ORIENTAÇÃO_MODAL_FINITO):
    # print("Qual é a Orientação interpessoal finita desejada?")

    # print()

    # OI_ORIENTAÇÃO_MODAL_FINITO = choice.Menu(['presente',
    #                                           'pretérito_perfectivo_I',
    #                                           'pretérito_perfectivo_II',
    #                                           'pretérito_imperfectivo',
    #                                           'passado_volitivo',
    #                                           'futuro']).ask()

    return OI_ORIENTAÇÃO_MODAL_FINITO

def realização_transitoriedade_presente(padrão_de_morfologia,OI_tipo_de_pessoa,OI_número):
    '''(str,str,str,str)->str

    Retorna o morfema que realiza a transitoriedade de um verbo no presente, dados
    a o padrão de morfologia, tipo de orientação, tipo de pessoa, e número.

    >>>realização_transitoriedade_presente ()
    'o'
    '''

    # padrão_de_morfologia = choice.Menu(['-AR', '-ER', '-IR', '-OR']).ask()
    # OI_tipo_de_pessoa = choice.Menu(['1pessoa', '2pessoa', '3pessoa']).ask()
    # OI_número = choice.Menu(['singular', 'plural']).ask()
    if (
            padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
    ):
        MI = 'o'
        return MI

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):

        MI = 'onho'
        return MI

    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'as'
            return MI

    elif (
            padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
            padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'
    ):

        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'es'
            return MI


    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI = 'ões'
            return MI


    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':

        MI = 'a'
        return MI


    elif (
            padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
            padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
    ):
        MI = 'e'
        return MI


    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):

        MI = 'õe'
        return MI

    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'amos'
            return MI

    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'emos'
            return MI

    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'imos'
            return MI

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI = 'omos'
            return MI

    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'ais'
            return MI

    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'eis'
            return MI

    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'is'
            return MI

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI = 'ondes'
            return MI

    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'am'
            return MI

    elif (
            padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural' or
            padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
    ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'em'
            return MI

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()

        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI = 'õem'
            return MI




b = json.load(open('C:/Users/andre/Documents/GitHub/NLG_BRAZILIAN_PORTUGUESE_19-11/NLG_BRAZILIAN_PORTUGUESE/json_test_2.json'))
verbo_lematizado = b["verbo_lematizado"]
TIPO_OM_FINITA = b["MI"]["TIPO_OM_FINITA"]
padrão_de_morfologia = b["MI"]["realizacao_transitoriedade_presente"]["padrao_de_morfologia"]
OI_tipo_de_pessoa = b["MI"]["realizacao_transitoriedade_presente"]["OI_tipo_de_pessoa"]
OI_número = b["MI"]["realizacao_transitoriedade_presente"]["OI_numero"]

realização_transitoriedade_presente(padrão_de_morfologia, OI_tipo_de_pessoa, OI_número)

realização_transitoriedade_do_verbo_finito(TIPO_OM_FINITA)

formação_da_estrutura_do_verbo_lexical(verbo_lematizado)