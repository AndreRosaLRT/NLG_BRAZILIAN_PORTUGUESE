import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.frase.frase_preposicional import *
import argparse


if __name__ == '__main__':
    def none_ou_str(value):
        if value == 'None':
            return None
        return value

    parser = argparse.ArgumentParser(description="Retorna uma frase preposicional dados um índice e os "
                                                 "argumentos referentes ao grupo nominal encaixado")

    parser.add_argument('argumentos', nargs='+', type=none_ou_str)
    args = parser.parse_args()

    print(frase_preposicional(*args.argumentos))
    

#
# frase_preposicional(indice_preposicao_frase=11, dissoc_ente_nucleo=None, tem_qualificador=None,
#     tipo_qualificador=None, indice_preposicao_qualif=None,
#     determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None,
#     numero_beta=None, morfologia_do_pronome_beta=None,
#     determinacao_especificidade_alpha='específico', orientacao_alpha='NA', genero_alpha='masculino',
#     numero_alpha='singular', morfologia_do_pronome_alpha=None,
#     pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
#     genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
#     tipo_numerativo=None, cardinal=None,
#     genero_numerativo=None, tipo_de_ente='consciente',
#     tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
#     tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#     substantivo_lematizado='homem', numero_subs='singular', genero_subs='não-binário',
#     tipo_feminino_ao=None,
#     tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
#     pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#     morfologia_do_pronome=None, reflexivo=None,  # classificador
#     adjetivo_classificador=None,
#     # epitetos
#     adj_epit_exp_pre=None,
#     adj_epit_int_pre=None,
#     adj_epit_exp_pos=None,
#     adj_epit_int_pos=None,
#     genero_adjetivo=None, numero_adjetivo=None,
#     contracao=None)