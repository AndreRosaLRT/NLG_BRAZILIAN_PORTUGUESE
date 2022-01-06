from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_nominal import *
import re


def frase_preposicional(indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
                        tipo_qualificador=None, indice_preposicao_qualif=None,
                        determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None, numero_beta=None,
                        morfologia_do_pronome_beta=None, determinacao_especificidade_alpha=None, orientacao_alpha=None,
                        genero_alpha=None, numero_alpha=None, morfologia_do_pronome_alpha=None,
                        pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None, genero_obj_possuido=None,
                        pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None, cardinal=None,
                        genero_numerativo=None,
                        tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                        tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
                        numero_subs=None, genero_subs=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
                        nome_proprio=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                        morfologia_do_pronome=None, reflexivo=None,
                        # classificador
                        adjetivo_classificador=None,
                        # epitetos
                        adj_epit_exp_pre=None,
                        adj_epit_int_pre=None,
                        adj_epit_exp_pos=None,
                        adj_epit_int_pos=None,
                        genero_adjetivo=None, numero_adjetivo=None,

                        contracao=None):
    """
    Ex.:

    >>> frase_preposicional(indice_preposicao_frase=0,dissoc_ente_nucleo=None,tem_qualificador=None,tipo_qualificador=None,
    indice_preposicao_qualif=None,determinacao_especificidade_beta='específico',
    orientacao_beta='NA',genero_beta='masculino',numero_beta=None,morfologia_do_pronome_beta=None,
    determinacao_especificidade_alpha='específico',orientacao_alpha='NA',genero_alpha='masculino',
    numero_alpha='singular',morfologia_do_pronome_alpha=None,pessoa_da_interlocucao_possuidor='1s',
    numero_obj_possuido='singular',genero_obj_possuido='masculino',
    pessoa_da_interlocucao_proximidade='próximo_ao_falante',tipo_numerativo=None,cardinal=None,
    genero_numerativo=None,tipo_de_ente='não_consciente',tipo_de_nao_consciente='material',
    tipo_de_nao_consciente_material='objeto_material',tipo_de_nao_consciente_semiotico=None,
    classe_palavra_ente='substantivo_comum',substantivo_lematizado='piano',numero_subs='singular',
    genero_subs='masculino',tipo_feminino_ao=None,tipo_masc_ao=None,acent_tonica=None,nome_proprio=None,
    pessoa_da_interlocucao=None,transitividade_verbo=None,tonicidade=None,morfologia_do_pronome=None,
    reflexivo=None,
    adjetivo_classificador='importado',
    adj_epit_exp_pre=None,
    adj_epit_int_pre='grande',
    adj_epit_exp_pos=None,
    adj_epit_int_pos='bonito',
    genero_adjetivo='não-binário',
    numero_adjetivo='singular',
    contracao=None) -> 'ao grande piano importado bonito'


    """
    frase_prep = ''
    prep = preposicao(indice_preposicao_frase)
    grupo_nominal = (re.sub(' +', ' ',
                            estrutura_gn_downranked(dissoc_ente_nucleo, tem_qualificador,
                                                    tipo_qualificador, indice_preposicao_qualif,
                                                    determinacao_especificidade_beta, orientacao_beta,
                                                    genero_beta, numero_beta,
                                                    morfologia_do_pronome_beta,
                                                    determinacao_especificidade_alpha, orientacao_alpha,
                                                    genero_alpha, numero_alpha,
                                                    morfologia_do_pronome_alpha,
                                                    pessoa_da_interlocucao_possuidor, numero_obj_possuido,
                                                    genero_obj_possuido,
                                                    pessoa_da_interlocucao_proximidade, tipo_numerativo,
                                                    cardinal,
                                                    genero_numerativo,
                                                    tipo_de_ente, tipo_de_nao_consciente,
                                                    tipo_de_nao_consciente_material,
                                                    tipo_de_nao_consciente_semiotico, classe_palavra_ente,
                                                    substantivo_lematizado,
                                                    numero_subs, genero_subs, tipo_feminino_ao,
                                                    tipo_masc_ao, acent_tonica,
                                                    nome_proprio, pessoa_da_interlocucao,
                                                    transitividade_verbo, tonicidade,
                                                    morfologia_do_pronome, reflexivo,
                                                    # classificador
                                                    adjetivo_classificador,
                                                    # epitetos
                                                    adj_epit_exp_pre,
                                                    adj_epit_int_pre,
                                                    adj_epit_exp_pos,
                                                    adj_epit_int_pos,
                                                    genero_adjetivo, numero_adjetivo,

                                                    contracao))).strip()
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
                frase_prep = 'à' + grupo_nominal[(-(len(grupo_nominal) - 1)):]
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

    except ValueError:
        return ''
#
# for i in range(12):
#     print(frase_preposicional(indice_preposicao_frase=i, dissoc_ente_nucleo=None, tem_qualificador=None,
#                           tipo_qualificador=None, indice_preposicao_qualif=None,
#                           determinacao_especificidade_beta=None,
#                           orientacao_beta=None,
#                           genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#                           determinacao_especificidade_alpha='específico', orientacao_alpha='NA',
#                           genero_alpha='masculino', numero_alpha='singular', morfologia_do_pronome_alpha=None,
#                           pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
#                           genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
#                           tipo_numerativo=None, cardinal=None, genero_numerativo='não-binário',
#                           tipo_de_ente='não_consciente',tipo_de_nao_consciente='material',
#                           tipo_de_nao_consciente_material='abstração_material',
#                           tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#                           substantivo_lematizado='homem', numero_subs='singular',genero_subs='masculino',
#                           tipo_feminino_ao=None,tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
#                           pessoa_da_interlocucao=None,transitividade_verbo=None, tonicidade=None,
#                           morfologia_do_pronome=None, reflexivo=None,adjetivo_epiteto='alto',
#                           adjetivo_classificador=None, genero_adjetivo='masculino',
#                           numero_adjetivo='singular', contracao=None))
