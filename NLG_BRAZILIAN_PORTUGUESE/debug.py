# -*- coding: utf-8 -*-

def verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, verbo,
                tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa,
                padrao_pessoa_morfologia="Morfologia_padrão"):
    '''(str)->str
    Retorna a estrutura que realiza os verbos no português.
    '''
    classe_do_verbo = def_classe_de_verbo(funcao_no_grupo_verbal)
    padrao_de_morfologia = detecta_padrao_morfologia(verbo)
    if classe_do_verbo == 'lexical':
        if (TIPO_DE_EXPERIENCIA == 'Ser' or
                TIPO_DE_EXPERIENCIA == 'Fazer' or
                TIPO_DE_EXPERIENCIA == 'Sentir'):

            if verbo == 'estar':
                verbo = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                             genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)

            elif verbo == 'ter':
                verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                           OI_numero, genero, OI_tipo_de_pessoa,
                                           padrao_pessoa_morfologia)
            elif verbo == 'ser':
                verbo = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
                                           OI_tipo_de_pessoa, padrao_pessoa_morfologia)
            elif verbo == 'ir':
                verbo = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                          genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
            elif verbo == 'haver':
                verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia)
            elif verbo == 'agredir':
                verbo = formacao_verbo_agredir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                               OI_numero, genero, OI_tipo_de_pessoa,
                                               padrao_pessoa_morfologia)
            elif verbo == 'aferir':
                verbo = formacao_verbo_aferir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                              OI_numero, genero, OI_tipo_de_pessoa,
                                              padrao_pessoa_morfologia)
            elif verbo == 'medir':
                verbo = formacao_verbo_medir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia)
            elif verbo == 'saber':
                verbo = formacao_verbo_saber(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia)
            elif (verbo == 'vir' or verbo == 'intervir'):
                verbo = formacao_verbo_vir_intervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                                    OI_numero, genero, OI_tipo_de_pessoa,
                                                    padrao_pessoa_morfologia)
            elif verbo == 'poder':
                verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia)
            elif verbo == 'fazer':
                verbo = formacao_verbo_fazer(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia)

            else:
                if verbo[-3:] == 'car':
                    verbo = formacao_verbo_CAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                               OI_numero, genero, OI_tipo_de_pessoa,
                                               padrao_pessoa_morfologia)
        elif verbo[-3:] == 'gar':
            verbo = formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                       OI_numero, genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia)
        elif verbo[-3:] == 'çar':
            verbo = formacao_verbo_ÇAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                       OI_numero, genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia)
        elif verbo[-3:] == 'gar':
            verbo = formacao_verbo_GAR(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                       OI_numero, genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia)
        elif verbo[-3:] == 'cer':
            verbo = formacao_verbo_CER(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                       OI_numero, genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia)

        elif verbo[-5:] == 'dizer':
            verbo = formacao_verbo_dizer(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                         genero, OI_tipo_de_pessoa, padrao_pessoa_morfologia)
        else:
            verbo = formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, OI_numero,
                                                   genero, OI_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
    #######
    elif classe_do_verbo == 'modal':
        if (TIPO_DE_EXPERIENCIA == 'Ser' or
                TIPO_DE_EXPERIENCIA == 'Fazer' or
                TIPO_DE_EXPERIENCIA == 'Sentir'):

            if verbo == 'dever':
                ME = verbo[slice(-2)]
                MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao, padrao_de_morfologia, OI_numero, genero,
                                                         OI_tipo_de_pessoa,
                                                         padrao_pessoa_morfologia="Morfologia_padrão")
                verbo = ME + MI

            elif verbo == 'poder':
                verbo = formacao_verbo_poder(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia='Morfologia_padrão')

            elif verbo == 'haver':
                verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                             OI_numero, genero, OI_tipo_de_pessoa,
                                             padrao_pessoa_morfologia='Morfologia_padrão')

            elif verbo == 'ter':

                verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
                                           OI_numero, genero, OI_tipo_de_pessoa,
                                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
    # elif verbo == 'ter de':
    # 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
    # 	                           OI_numero, genero, OI_tipo_de_pessoa,
    # 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'

    elif classe_do_verbo == 'auxiliar':
        verbo = formacao_da_estrutura_do_verbo_AUX(verbo, tipo_de_orientacao, OI_numero,
                                                   genero, OI_tipo_de_pessoa,
                                                   padrao_pessoa_morfologia)
    else:
        verbo = ''
    return verbo


verbo_geral("Fazer", 'Evento', 'enternecer', 'pretérito_perfectivo_I', 'singular', None, '1pessoa')
