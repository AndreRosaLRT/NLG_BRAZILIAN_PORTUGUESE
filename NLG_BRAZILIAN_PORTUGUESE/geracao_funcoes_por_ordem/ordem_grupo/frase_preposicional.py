from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.verbais import *


def frase_preposicional(indicePreposicaoFrase=None, dissocEnteNucleo=None, temQualificador=None,
                        tipoQualificador=None, indicePreposicaoQualif=None, DETERMINAÇÃO_espeficifidade_beta=None,
                        ORIENTAÇÃO_beta=None,
                        gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
                        DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
                        número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
                        número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
                        funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
                        milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
                        numIndefinido=None, tipo_de_Ente=None, tipo_de_nao_consciente=None,
                        tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
                        classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
                        tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
                        pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                        morfologia_do_pronome=None, reflexivo=None,
                        adjetivo_epiteto=None,
                        adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None,
                        contracao=None):
    '''
    '''
    prep = preposicao(indicePreposicaoFrase)
    grupo_nominal = (re.sub(' +', ' ',
                            estrutura_GN_downraked(dissocEnteNucleo, temQualificador, tipoQualificador,
                                                   indicePreposicaoQualif, DETERMINAÇÃO_espeficifidade_beta,
                                                   ORIENTAÇÃO_beta, gênero_beta, número_beta,
                                                   morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
                                                   ORIENTAÇÃO_alpha, gênero_alpha, número_alpha,
                                                   morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
                                                   número_obj_possuído, gênero_obj_possuído,
                                                   pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal,
                                                   genero, tipo_precisa, tipoRealCard, milharExtenso, centenaExtenso,
                                                   dezenaExtenso, unidadeExtenso, numIndefinido, tipo_de_Ente,
                                                   tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                                   tipo_de_nao_consciente_semiotico, classe_palavra_Ente,
                                                   substantivo_lematizado, numero, tipo_feminino_ÃO, tipo_masc_ÃO,
                                                   acentTonica, nomeProprio, pessoa_da_interlocucao,
                                                   transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
                                                   adjetivo_epiteto, adjetivo_classificador, generoAdjetivo,
                                                   numeroAdjetivo, contracao))).strip()
    try:
        if prep == 'por':
            if grupo_nominal[:2] == 'o ':
                frase_prep = 'pel' + grupo_nominal
            elif grupo_nominal[:2] == 'a ':
                frase_prep = 'pel' + grupo_nominal
            else:
                frase_prep = prep + ' ' + grupo_nominal
        elif prep == 'a':
            if grupo_nominal[:2] == 'a ':
                E = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
            elif grupo_nominal[:2] == 'o ':
                frase_prep = prep + grupo_nominal
            elif grupo_nominal[:5] == 'aquel':
                frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
            else:
                frase_prep = prep + ' ' + grupo_nominal
        elif prep == 'de':
            if (grupo_nominal[:2] == 'o ' or grupo_nominal[:2] == 'a ' or grupo_nominal[:3] == 'est' or
                    grupo_nominal[:3] == 'ist' or grupo_nominal[:3] == 'ess' or grupo_nominal[:3] == 'iss'
                    or grupo_nominal[:5] == 'aquel' or grupo_nominal[:5] == 'aquil'):
                frase_prep = (prep[slice(-1)]) + grupo_nominal
            elif (grupo_nominal[:2] == 'um' or grupo_nominal[:2] == 'un' or
                  grupo_nominal[:2] == 'el' or grupo_nominal[:4] == 'outr'):

                if contracao == '+contração':
                    frase_prep = (prep[slice(-1)]) + grupo_nominal
                else:
                    frase_prep = prep + ' ' + grupo_nominal
            else:
                frase_prep = prep + ' ' + grupo_nominal
        elif prep == 'em':
            if (
                    grupo_nominal[:2] == 'o ' or grupo_nominal[:2] == 'a ' or
                    grupo_nominal[:2] == 'el' or grupo_nominal[:3] == 'est' or
                    grupo_nominal[:3] == 'ist' or grupo_nominal[:3] == 'ess' or
                    grupo_nominal[:3] == 'iss' or grupo_nominal[:5] == 'aquel' or
                    grupo_nominal[:5] == 'aquil'
            ):
                frase_prep = 'n' + grupo_nominal
            else:
                if (
                        grupo_nominal[:2] == 'um' or grupo_nominal[:2] == 'un' or
                        grupo_nominal[:4] == 'outr'
                ):

                    if contracao == '+contração':
                        frase_prep = 'n' + grupo_nominal
                    else:
                        frase_prep = prep + ' ' + grupo_nominal

        elif prep == 'para':
            if (
                    grupo_nominal[:2] == 'o ' or grupo_nominal[:2] == 'a '
            ):
                if contracao == '+contração':
                    frase_prep = 'pr' + grupo_nominal
                else:
                    frase_prep = prep + ' ' + grupo_nominal
            else:
                frase_prep = prep + ' ' + grupo_nominal
        elif prep != '':
            frase_prep = prep + ' ' + grupo_nominal
        return frase_prep
    except:

        return ''


#
# #
# for i in range(12):
# 	print(frase_preposicional(indicePreposicaoFrase=i, dissocEnteNucleo=None, temQualificador=None,
# 								tipoQualificador=None,indicePreposicaoQualif=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 								gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 								DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
# 								gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
# 								pessoa_da_interlocução_possuidor=None, número_obj_possuído=None,
# 								gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
# 								funcaoNumerativo=None, cardinal=None, genero='não-binário', tipo_precisa=None,
# 								tipoRealCard=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None,
# 								unidadeExtenso=None, numIndefinido=None, tipo_de_Ente='não_consciente',
# 								tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='abstração_material',
# 								tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 								substantivo_lematizado='homem', numero='singular', tipo_feminino_ÃO=None,
# 								tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 								transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
# 								adjetivo_epiteto='alto', adjetivo_classificador=None, generoAdjetivo='masculino',
# 								numeroAdjetivo='singular', contracao=None))
frase_preposicional(10, None, None, None, None, None, None, None, None, None, 'específico',
                    'orientação_específica_proximidade', 'feminino', 'plural', 'morfologia_terceira_pessoa', '1s',
                    'plural', None, 'próximo_ao_não_interlocutor', None, None, 'feminino', None, None, None, None, None,
                    None, None, 'consciente', None, None, None, 'substantivo_comum', 'menino', 'plural', None, None,
                    None, None, None, None, None, None, None, 'alto', None, 'feminino', 'plural', '+contração')
# frase_preposicional(indicePreposicao=4,
# 					 genero='não-binário',
# 					tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 					tipo_de_nao_consciente_material='abstração_material', classe_palavra_Ente='substantivo_comum',
# 					substantivo_lematizado='certeza', numero='singular')
#
# frase_preposicional(indicePreposicao=6, dissocEnteNucleo=None, temQualificador=None,
# 						tipoQualificador=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 						gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 						DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
# 						número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
# 						número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,
# 						funcaoNumerativo=None, cardinal=None, genero='não-binário', tipo_precisa=None, tipoRealCard=None,
# 						milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None,
# 						numIndefinido=None, tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 						tipo_de_nao_consciente_material='abstração_material', tipo_de_nao_consciente_semiotico=None,
# 						classe_palavra_Ente='substantivo_comum', substantivo_lematizado='futebol', numero='singular',
# 						tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
# 						pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
# 						morfologia_do_pronome=None, reflexivo=None,
# 						adjetivo_epiteto=None,
# 						adjetivo_classificador=None,generoAdjetivo=None, numeroAdjetivo=None, contracao=None)
