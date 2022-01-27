import sys
sys.path.append('../')

import argparse
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_oracao.oracao import *

if __name__ == '__main__':

    def none_ou_str_int(value):
        if value == 'None':
            return None
        try:
            return int(value)
        except:
            return value

    parser = argparse.ArgumentParser()
    parser.add_argument('argumentos', nargs='+', type=none_ou_str_int)
    args = parser.parse_args()

    print(oracao_mental(*args.argumentos))


# Ex no terminal
# python3 main_oracao_mental.py 'Mental' None 0 None 0 0 1 'TI_NA' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None False None None None None None None None None None 'orientado' 'direcional' 'default' 'indicativo' 'declarativo' 'NA' None None None 'não-fenomenalização_comportamento-passivo' 'inferior_perceptivo' 'Sentir' 'agenciado_ativa' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Sentir' 'Evento' 'ouvir' 'pretérito_perfectivo_I' 'singular' None '1pessoa' 'Morfologia_padrão' 'positiva' None None None None None None None None None None None None None None None None None None None None None "consciente" None None None 'pronome_caso_reto' None "singular" None None None None None "falante" None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'grupo_adverbial' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Modo' 10 None None None None None None None None
# Eu ouvi




oracao_mental('Mental',None,0,None,0,0,1,'TI_NA',None, None,None,None, None,None,None,None,None,None,None,None, None, None, None, None,None, None, None, None,None,None,None,None, None,None,None,None,None,None, None, None,None,None,None,None,None,None,None,None,None, None,None, None,None, None, None,None,None, None,None,None, None, None,None,None,None,None,False, None,None,None, None,None,None, None,None,None,'orientado','direcional','default','indicativo','declarativo', 'NA',None,None,None,'não-fenomenalização_comportamento-passivo','inferior_perceptivo','Sentir', 'agenciado_ativa', None,None,None,None,None,None, None,None,None,None,None,None,None, None,None, None, None, None, None,None,None, None, None,None, None,None,None,None, None,None,None,None,'Sentir','Evento','ouvir','pretérito_perfectivo_I', 'singular',None,'1pessoa','Morfologia_padrão','positiva',None, None, None,None, None,None,None, None,None,None,None, None,None,None, None,None,None, None,None,None, None,"consciente",None,None,None,'pronome_caso_reto',None,"singular", None,None,None,None,None,"falante",None,None,None,None,None,None,None,None,None,None, None,None,None,None,None,None, None,None,None, None,None,None,None,None,None,None,None,None,None, None, None, None, None,None, None,None,None, None,None,None,None,None,None,None,None,None,None,None, None,None,None,None,None,None,None,None,None,None,None,None, None,None,None,None, None,None,None,None,None,None,None,None,None,None, None,None,None,None,None,None, None,None,None,None, None,None,None,None,None,None,None, None,None,None,None,None,None,None,None,None,None,None,None, None,None,'grupo_adverbial',None,None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None, None,None,None,None, None,None,None,None,None,None,None, None,None,'Modo',10,None,None,None, None,None,None,None,None)




oracao_mental(

    # TRANSITIVIDADE
    tipo_de_processo='Mental', indice_material=None, indice_agenciamento=0, indice_relacional=None,

    # MODO
    responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
    # TEMA INTERPESSOAL
    tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
    # TEMA INTERP realizado por grupo adverbial
    t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
    t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
    t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
    t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
    t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
    #

    # # TEMA INTERPESSOAL realiziado por frase preposicional
    t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
    t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
    t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
    t_inter_fp_numero_beta=None,
    t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
    t_inter_fp_orientacao_alpha=None,
    t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
    t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
    t_inter_fp_genero_obj_possuido=None,
    t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
    t_inter_fp_genero_numerativo=None,
    t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
    t_inter_fp_tipo_de_nao_consciente_material=None,
    t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
    t_inter_fp_substantivo_lematizado=None,
    t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
    t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
    t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
    t_inter_fp_tonicidade=None,
    t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
    t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
    t_inter_fp_contracao=None,
    #
    # 		#
    t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
    #

    # 	#TEMA TEXTUAL
    t_text_tem_tema_textual=False, t_text_indice_cont=None,
    t_text_tipo_de_conjuncao=None,
    t_text_indice_conj=None, t_text_tipo_de_relativo=None,
    t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
    t_text_indice_relativo=None, t_text_indice_relativo_adv=None,

    # TEMA IDEACIONAL

    orientacao_modal='orientado', orientacao_transitiva='direcional',
    selecao_tematica='default', tema_default='indicativo',
    tema_default_indicativo='declarativo', tema_identificativo='NA',
    tema_angulo=None, tema_elemental=None,
    tema_proeminente=None,

    ##específico do processo_ Mental
    fenomenalizacao='não-fenomenalização_comportamento-passivo', tipo_de_mental='inferior_perceptivo',

    ##processo_
    tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
    funcao_no_grupo_verbal_1=None,
    verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
    padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
    tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
    padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
    tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
    padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
    tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
    padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
    verbo_lex='ouvir', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
    oi_tipo_de_pessoa_lex='1pessoa',
    padrao_pessoa_morfologia_lex='Morfologia_padrão',
    # POLARIDADE
    tipo_polaridade='positiva',

    ##PARTICIPANTES

    # P1
    p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
    p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
    p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
    p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
    p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
    p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
    p1_cardinal=None, p1_genero_numerativo=None,
    p1_tipo_de_ente="consciente", p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
    p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='pronome_caso_reto',
    p1_substantivo_lematizado=None,
    p1_numero_subs="singular", p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
    p1_acent_tonica=None,
    p1_nome_proprio=None,
    p1_pessoa_da_interlocucao="falante", p1_transitividade_verbo=None, p1_tonicidade=None,
    p1_morfologia_do_pronome=None,
    p1_reflexivo=None,
    # classificador
    p1_adjetivo_classificador=None,
    # epitetos
    p1_adj_epit_exp_pre=None,
    p1_adj_epit_int_pre=None,
    p1_adj_epit_exp_pos=None,
    p1_adj_epit_int_pos=None,
    p1_genero_adjetivo=None, p1_numero_adjetivo=None,

    p1_contracao=None,

    # P2
    p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
    p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
    p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
    p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
    p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
    p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
    p2_cardinal=None, p2_genero_numerativo=None,
    p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
    p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
    p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
    p2_nome_proprio=None,
    p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
    p2_reflexivo=None,
    # classificador
    p2_adjetivo_classificador=None,
    # epitetos
    p2_adj_epit_exp_pre=None,
    p2_adj_epit_int_pre=None,
    p2_adj_epit_exp_pos=None,
    p2_adj_epit_int_pos=None,
    p2_genero_adjetivo=None, p2_numero_adjetivo=None,

    p2_contracao=None,

    ##PARTICIPANTES REALIZADOS POR FP
    part_fp_indice_preposicao_frase=None, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
    part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
    part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
    part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
    part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
    part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
    part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
    part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None,
    part_fp_tipo_numerativo=None, part_fp_cardinal=None,
    part_fp_genero_numerativo=None, part_fp_tipo_de_ente=None,
    part_fp_tipo_de_nao_consciente=None, part_fp_tipo_de_nao_consciente_material=None,
    part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente=None,
    part_fp_substantivo_lematizado=None, part_fp_numero_subs=None, part_fp_genero_subs=None,
    part_fp_tipo_feminino_ao=None,
    part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
    part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
    part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None,  # classificador
    part_fp_adjetivo_classificador=None,
    # epitetos
    part_fp_adj_epit_exp_pre=None,
    part_fp_adj_epit_int_pre=None,
    part_fp_adj_epit_exp_pos=None,
    part_fp_adj_epit_int_pos=None,
    part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
    part_fp_contracao=None,

    ##CIRCUNSTANCIA
    circunst_realizacao_circunstancia='grupo_adverbial',
    circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
    circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
    circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
    circunst_numero_beta=None,
    circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
    circunst_orientacao_alpha=None,
    circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
    circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
    circunst_genero_obj_possuido=None,
    circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
    circunst_genero_numerativo=None,
    circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
    circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
    circunst_substantivo_lematizado=None,
    circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
    circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
    circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
    circunst_tonicidade=None,
    circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
    # classificador
    circunst_adjetivo_classificador=None,
    # epitetos
    circunst_adj_epit_exp_pre=None,
    circunst_adj_epit_int_pre=None,
    circunst_adj_epit_exp_pos=None,
    circunst_adj_epit_int_pos=None,
    circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,

    circunst_contracao=None,
    circunst_tipo_de_adverbio1='Modo', circunst_adv_ind1=10,
    circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
    circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
    circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
    circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None

)





