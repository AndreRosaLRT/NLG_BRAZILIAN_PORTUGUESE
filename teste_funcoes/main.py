from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_nominal_frase_preposicional import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_oracao.oracao import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.frase.frase_preposicional import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_conjuntivo import *


#
# frase_preposicional(indice_preposicao_frase=0,dissoc_ente_nucleo=None,tem_qualificador=None,tipo_qualificador=None,
#     indice_preposicao_qualif=None,determinacao_especificidade_beta='específico',
#     orientacao_beta='NA',genero_beta='masculino',numero_beta=None,morfologia_do_pronome_beta=None,
#     determinacao_especificidade_alpha='específico',orientacao_alpha='NA',genero_alpha='masculino',
#     numero_alpha='singular',morfologia_do_pronome_alpha=None,pessoa_da_interlocucao_possuidor='1s',
#     numero_obj_possuido='singular',genero_obj_possuido='masculino',
#     pessoa_da_interlocucao_proximidade='próximo_ao_falante',tipo_numerativo=None,cardinal=None,
#     genero_numerativo=None,tipo_de_ente='não_consciente',tipo_de_nao_consciente='material',
#     tipo_de_nao_consciente_material='objeto_material',tipo_de_nao_consciente_semiotico=None,
#     classe_palavra_ente='substantivo_comum',substantivo_lematizado='piano',numero_subs='singular',
#     genero_subs='masculino',tipo_feminino_ao=None,tipo_masc_ao=None,acent_tonica=None,nome_proprio=None,
#     pessoa_da_interlocucao=None,transitividade_verbo=None,tonicidade=None,morfologia_do_pronome=None,
#     reflexivo=None,
#     adjetivo_classificador='importado',
#     adj_epit_exp_pre=None,
#     adj_epit_int_pre='grande',
#     adj_epit_exp_pos=None,
#     adj_epit_int_pos='bonito',
#     genero_adjetivo='não-binário',
#     numero_adjetivo='singular',
#     contracao=None)
# estrutura_gn(dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
#              indice_preposicao_qualif=None, determinacao_especificidade_beta=None,
#              orientacao_beta=None, genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#              determinacao_especificidade_alpha='específico', orientacao_alpha='NA', genero_alpha='masculino',
#              numero_alpha='singular', morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor='1s',
#              numero_obj_possuido='singular', genero_obj_possuido='masculino',
#              pessoa_da_interlocucao_proximidade='próximo_ao_falante', tipo_numerativo=None, cardinal=None,
#              genero_numerativo=None, tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
#              tipo_de_nao_consciente_material='objeto_material', tipo_de_nao_consciente_semiotico=None,
#              classe_palavra_ente='substantivo_comum', substantivo_lematizado='piano', numero_subs='singular',
#              genero_subs='masculino', tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
#              pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
#              reflexivo=None,
#              adjetivo_classificador='importado',
#              adj_epit_exp_pre=None,
#              adj_epit_int_pre='grande',
#              adj_epit_exp_pos=None,
#              adj_epit_int_pos='bonito',
#              genero_adjetivo='não-binário',
#              numero_adjetivo='singular',
#              contracao=None)
# import json
# # Exemplos de uso das funções
# # ordem do morfema
# # experiencia do verbo
# lemas_verbos = ['desmatar', 'registrar', 'detectar', 'identificar', 'atingir', 'contabilizar', 'somar', 'totalizar',
#           'alcançar', 'chegar', 'reportar', 'observar', 'ser', 'representar', 'acontecer', 'ocorrer', 'existir',
#           'ter', 'apresentar', 'possuir', 'estar', 'acumular', 'relatar', 'sofrer']
# for verb in lemas_verbos:
#     print(experiencia_do_verbo(verb))
# # desmat
# # registr
# # detect
# # identific
# # ating
# # contabiliz
# # som
# # totaliz
# # alcanç
# # cheg
# # report
# # observ
# # s
# # represent
# # acontec
# # ocorr
# # exist
# # t
# # apresent
# # possu
# # est
# # acumul
# # relat
# # sofr
# #Detecção terminação verbo infinitivo
# for verb in lemas_verbos:
#     print(deteccao_transitoriedade_do_verbo(verb))
# # ar
# # ar
# # ar
# # ar
# # ir
# # ar
# # ar
# # ar
# # ar
# # ar
# # ´ar
# # ar
# # er
# # ar
# # er
# # er
# # ir
# # er
# # ar
# # ir
# # ar
# # ar
# # ar
# # er
#
# # Detecção de padrão de morfologia
# for verb in lemas_verbos:
#     print(detecta_padrao_morfologia(verb))
# # AR
# # AR
# # AR
# # AR
# # IR
# # AR
# # AR
# # AR
# # AR
# # AR
# # AR
# # AR
# # ER
# # AR
# # ER
# # ER
# # IR
# # ER
# # AR
# # IR
# # AR
# # AR
# # AR
# # ER
#
#
# # Os morfemas interpessoas serão testados diretamente na palavra verbal_verbo
# # ORDEM DA PALAVRA
# # VERBOS: os algoritmo a seguir retorna um dicionário com todas as opções de Orientação Interpessoal de cada
# # um dos verbos na lista lema_verbos.
# #
# ####
# #
#
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# OI_INTERPESSOAIS = [ 'presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II',
#                     'pretérito_imperfectivo', 'pretérito_imperfectivo', 'passado_volitivo', 'futuro',
#                     'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
#                     'não_finito_concretizado','imperativo_I', 'imperativo_II']
# generos=['masculino','feminino']
# conjugacao = []
#
# dicionarioConjuga={}
#
# for lema in lemas_verbos:
#     dicionarioConjuga.update({lema: {}})
#     for oi in OI_INTERPESSOAIS:
#         conjugacao = []
#         for numero in OI_numeros:
#             for tipo_pessoa in OI_tipo_pessoas:
#                 verbo = verbo_geral("Fazer", 'Evento', lema, oi, numero, None, tipo_pessoa)
#                 conjugacao.append(verbo)
#                 dicionarioConjuga[lema].update({oi:conjugacao})
# # print(dicionarioConjuga)
#
# # Função que  retorna a classe do verbo, dada a função do verbo no grupo verbal
# funcao_no_grupo_verbal = ['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo','Auxiliar+Núcleo', 'Modal+Núcleo']
# for elem in funcao_no_grupo_verbal:
#     print(def_classe_de_verbo(elem))
#
# # PREPOSIÇÕES: a linha a seguir printa todas as opções disponíveis no módulo para as preposições
# [print(preposicao(i)) for i in range (17)]
#
#
#
# # CIRCUNSTANCIA:
# for i in range (26):
#     print(circunstancia(realizacao_circunstancia='grupo_adverbial',
#                   indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
#                   tipo_qualificador=None, indice_preposicao_qualif=None,
#                   determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None, numero_beta=None,
#                   morfologia_do_pronome_beta=None, determinacao_especificidade_alpha=None, orientacao_alpha=None,
#                   genero_alpha=None, numero_alpha=None, morfologia_do_pronome_alpha=None,
#                   pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None, genero_obj_possuido=None,
#                   pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None, cardinal=None,
#                   genero_numerativo=None,
#                   tipo_de_ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
#                   tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None, substantivo_lematizado=None,
#                   numero_subs=None, genero_subs=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
#                   nome_prop_fp=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#                   morfologia_do_pronome=None, reflexivo=None,
#                   # classificador
#                   adjetivo_classificador=None,
#                   # epitetos
#                   adj_epit_exp_pre=None,
#                   adj_epit_int_pre=None,
#                   adj_epit_exp_pos=None,
#                   adj_epit_int_pos=None,
#                   genero_adjetivo=None, numero_adjetivo=None,
#
#                   contracao=None,
#                   tipo_de_adverbio1='Tempo', adv_ind1=i))
#
# for i in range(16):
#     print(circunstancia(realizacao_circunstancia='frase_preposicional', indice_preposicao_frase=i,
#                         dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
#                         indice_preposicao_qualif=None, determinacao_especificidade_beta='específico',
#                         orientacao_beta='NA', genero_beta='masculino', numero_beta=None,
#                         morfologia_do_pronome_beta=None,
#                         determinacao_especificidade_alpha='específico', orientacao_alpha='NA', genero_alpha='feminino',
#                         numero_alpha='singular', morfologia_do_pronome_alpha=None,
#                         pessoa_da_interlocucao_possuidor='1s',
#                         numero_obj_possuido='singular', genero_obj_possuido='masculino',
#                         pessoa_da_interlocucao_proximidade=None, tipo_numerativo='ordinal', cardinal=2,
#                         genero_numerativo='feminino', tipo_de_ente='não_consciente', tipo_de_nao_consciente='semiótico',
#                         tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico='objeto_semiótico',
#                         classe_palavra_ente='substantivo_comum', substantivo_lematizado='guerra',
#                         numero_subs='singular',
#                         genero_subs='feminino', tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
#                         nome_prop_fp=None,
#                         pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#                         morfologia_do_pronome=None,
#                         reflexivo=None,
#                         adjetivo_classificador='mundial',
#                         adj_epit_exp_pre=None,
#                         adj_epit_int_pre=None,
#                         adj_epit_exp_pos=None,
#                         adj_epit_int_pos=None,
#                         genero_adjetivo='não-binário',
#                         numero_adjetivo='singular',
#                         contracao=None))
#
# # -> à segunda guerra mundial
# # ante a segunda guerra mundial
# # após a segunda guerra mundial
# # até a segunda guerra mundial
# # com a segunda guerra mundial
# # contra a segunda guerra mundial
# # da segunda guerra mundial
# # desde a segunda guerra mundial
# # na segunda guerra mundial
# # entre a segunda guerra mundial
# # para a segunda guerra mundial
# # pela segunda guerra mundial
# # perante a segunda guerra mundial
# # sem a segunda guerra mundial
# # sob a segunda guerra mundial
# # sobre a segunda guerra mundial
#
#
# # testes oracao:
#
# #verbal
#
#
# # O homem acusou o padeiro
# oracao_verbal('Verbal', None, 2, None, 0, 0, 1, 'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA',
#               None, None, None, 'atividade_alvo', None, None, None, 'Sentir', 'não_agenciado', None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, 'Sentir', 'Evento', 'acusar',
#               'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'positiva', None, None, None,
#               None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None, None, None,
#               None, None, None, 'não-binário', None, None, None, None, None, None, None, 'não_consciente', 'material',
#               'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               'específico', 'NA', 'masculino', 'singular', None, None, None, None, None, None, None, 'masculino', None,
#               None, None, None, None, None, None, 'não_consciente', 'material', 'abstração_material', None,
#               'substantivo_comum', 'padeiro', 'singular', None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
#
# oracao_verbal('Verbal', None, 0, None, 0, 0, 1, 'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA',
#               None, None, None, 'semioticidade', 'não_projeção_-verbiagem', None, None, 'Sentir', 'não_agenciado', None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'Sentir', 'Evento',
#               'falar', 'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'positiva', None,
#               None, None, None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None,
#               None, None, None, None, None, 'não-binário', None, None, None, None, None, None, None, 'não_consciente',
#               'material', 'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None)
#
# oracao_verbal('Verbal', None, 0, None, 0, 0, 1, 'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA',
#               None, None, None, 'atividade_fala', None, None, None, 'Sentir', 'não_agenciado', None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, 'Sentir', 'Evento', 'falar',
#               'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'positiva', None, None, None,
#               None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None, None, None,
#               None, None, None, 'não-binário', None, None, None, None, None, None, None, 'não_consciente', 'material',
#               'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#               None)
#
#
#
# # ORAÇÃO MENTAL
#
# oracao_mental(
#
#     # TRANSITIVIDADE
#     tipo_de_processo='Mental', indice_material=None, indice_agenciamento=0, indice_relacional=None,
#
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#
#     # # TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#
#     ##específico do processo_ Mental
#     fenomenalizacao='não-fenomenalização_comportamento-passivo', tipo_de_mental='inferior_perceptivo',
#
#     ##processo_
#     tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='ouvir', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='1pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade='positiva',
#
#     ##PARTICIPANTES
#
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente="consciente", p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='pronome_caso_reto',
#     p1_substantivo_lematizado=None,
#     p1_numero_subs="singular", p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao="falante", p1_transitividade_verbo=None, p1_tonicidade=None,
#     p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#     p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#
#     ##PARTICIPANTES REALIZADOS POR FP
#     part_fp_indice_preposicao_frase=None, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
#     part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
#     part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
#     part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
#     part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
#     part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
#     part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
#     part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None,
#     part_fp_tipo_numerativo=None, part_fp_cardinal=None,
#     part_fp_genero_numerativo=None, part_fp_tipo_de_ente=None,
#     part_fp_tipo_de_nao_consciente=None, part_fp_tipo_de_nao_consciente_material=None,
#     part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente=None,
#     part_fp_substantivo_lematizado=None, part_fp_numero_subs=None, part_fp_genero_subs=None,
#     part_fp_tipo_feminino_ao=None,
#     part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
#     part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
#     part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None,  # classificador
#     part_fp_adjetivo_classificador=None,
#     # epitetos
#     part_fp_adj_epit_exp_pre=None,
#     part_fp_adj_epit_int_pre=None,
#     part_fp_adj_epit_exp_pos=None,
#     part_fp_adj_epit_int_pos=None,
#     part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
#     part_fp_contracao=None,
#
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia='grupo_adverbial',
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1='Modo', circunst_adv_ind1=10,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )

# # -> 'Eu ouvi cuidadosamente.'
#
# ###########################################################################################
#
#
# oracao_mental(
#
#     # TRANSITIVIDADE
#     tipo_de_processo='Mental', indice_material=None, indice_agenciamento=1, indice_relacional=None,
#
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=4,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#
#     # # TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#
#     ##específico do processo_ Mental
#     fenomenalizacao='não-fenomenalização_assunto', tipo_de_mental='superior_cognitivo',
#
#     ##processo_
#     tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='saber', tipo_de_orientacao_lex='presente', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='1pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade='positiva',
#
#     ##PARTICIPANTES
#
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente="consciente", p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='pronome_caso_reto',
#     p1_substantivo_lematizado=None,
#     p1_numero_subs="singular", p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao="falante", p1_transitividade_verbo=None, p1_tonicidade=None,
#     p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#     p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#
#     ##PARTICIPANTES REALIZADOS POR FP
#     part_fp_indice_preposicao_frase=6, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
#     part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
#     part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
#     part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
#     part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
#     part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
#     part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
#     part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None,
#     part_fp_tipo_numerativo=None, part_fp_cardinal=None,
#     part_fp_genero_numerativo=None, part_fp_tipo_de_ente='não_consciente',
#     part_fp_tipo_de_nao_consciente='material', part_fp_tipo_de_nao_consciente_material='abstração_material',
#     part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente='substantivo_comum',
#     part_fp_substantivo_lematizado='futebol', part_fp_numero_subs='singular', part_fp_genero_subs='não-binário',
#     part_fp_tipo_feminino_ao=None,
#     part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
#     part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
#     part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None,  # classificador
#     part_fp_adjetivo_classificador=None,
#     # epitetos
#     part_fp_adj_epit_exp_pre=None,
#     part_fp_adj_epit_int_pre=None,
#     part_fp_adj_epit_exp_pos=None,
#     part_fp_adj_epit_int_pos=None,
#     part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
#     part_fp_contracao=None,
#
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia='grupo_adverbial',
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1='Modo', circunst_adv_ind1=2,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )

# # -> > 'Eu sei de futebol bem.'
#
# ##########################################
#
# oracao_mental(
#
#     # TRANSITIVIDADE
#     tipo_de_processo='Mental', indice_material=None, indice_agenciamento=1, indice_relacional=None,
#
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#
#     # # TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#
#     ##específico do processo_ Mental
#     fenomenalizacao='fenomenalização_fenômeno-simples', tipo_de_mental='superior_cognitivo',
#
#     ##processo_
#     tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='imaginar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='1pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade='positiva',
#
#     ##PARTICIPANTES
#
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente="consciente", p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='pronome_caso_reto',
#     p1_substantivo_lematizado=None,
#     p1_numero_subs="singular", p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao="falante", p1_transitividade_verbo=None, p1_tonicidade=None,
#     p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='específico', p2_orientacao_beta='NA',
#     p2_genero_beta='masculino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='específico', p2_orientacao_alpha='NA', p2_genero_alpha='masculino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='abstração_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='jogo',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#
#     ##PARTICIPANTES REALIZADOS POR FP
#     part_fp_indice_preposicao_frase=None, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
#     part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
#     part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
#     part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
#     part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
#     part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
#     part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
#     part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None,
#     part_fp_tipo_numerativo=None, part_fp_cardinal=None,
#     part_fp_genero_numerativo=None, part_fp_tipo_de_ente=None,
#     part_fp_tipo_de_nao_consciente=None, part_fp_tipo_de_nao_consciente_material=None,
#     part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente=None,
#     part_fp_substantivo_lematizado=None, part_fp_numero_subs=None, part_fp_genero_subs=None,
#     part_fp_tipo_feminino_ao=None,
#     part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
#     part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
#     part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None,  # classificador
#     part_fp_adjetivo_classificador=None,
#     # epitetos
#     part_fp_adj_epit_exp_pre=None,
#     part_fp_adj_epit_int_pre=None,
#     part_fp_adj_epit_exp_pos=None,
#     part_fp_adj_epit_int_pos=None,
#     part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
#     part_fp_contracao=None,
#
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia='grupo_adverbial',
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1='Modo', circunst_adv_ind1=1,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # --> > 'Eu imaginei o jogo.'
#
# #########################################
#
#
# oracao_mental(
#
#     # TRANSITIVIDADE
#     tipo_de_processo='Mental', indice_material=None, indice_agenciamento=1, indice_relacional=None,
#
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#
#     # # TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#
#     ##específico do processo_ Mental
#     fenomenalizacao='fenomenalização_fenômeno-simples', tipo_de_mental='inferior_emotivo',
#
#     ##processo_
#     tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='estranhar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade='positiva',
#
#     ##PARTICIPANTES
#
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente="não_consciente", p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='animal',
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='peixe',
#     p1_numero_subs="singular", p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None,
#     p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='específico', p2_orientacao_beta='NA',
#     p2_genero_beta='feminino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='específico', p2_orientacao_alpha='NA', p2_genero_alpha='feminino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='objeto_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='água',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#
#     ##PARTICIPANTES REALIZADOS POR FP
#     part_fp_indice_preposicao_frase=None, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
#     part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
#     part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
#     part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
#     part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
#     part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
#     part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
#     part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None,
#     part_fp_tipo_numerativo=None, part_fp_cardinal=None,
#     part_fp_genero_numerativo=None, part_fp_tipo_de_ente=None,
#     part_fp_tipo_de_nao_consciente=None, part_fp_tipo_de_nao_consciente_material=None,
#     part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente=None,
#     part_fp_substantivo_lematizado=None, part_fp_numero_subs=None, part_fp_genero_subs=None,
#     part_fp_tipo_feminino_ao=None,
#     part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
#     part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
#     part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None,  # classificador
#     part_fp_adjetivo_classificador=None,
#     # epitetos
#     part_fp_adj_epit_exp_pre=None,
#     part_fp_adj_epit_int_pre=None,
#     part_fp_adj_epit_exp_pos=None,
#     part_fp_adj_epit_int_pos=None,
#     part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
#     part_fp_contracao=None,
#
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia='grupo_adverbial',
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # 'O peixe estranhou a água .'
#
#
# ###################################################
#
#
#
# oracao_mental(
#
#     # TRANSITIVIDADE
#     tipo_de_processo='Mental', indice_material=None, indice_agenciamento=2, indice_relacional=None,
#
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#
#     # # TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#
#     ##específico do processo_ Mental
#     fenomenalizacao='fenomenalização_fenômeno_simples', tipo_de_mental='superior_cognitivo',
#
#     ##processo_
#     tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='impressionar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade='positiva',
#
#     ##PARTICIPANTES
#
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente="não_consciente", p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='animal',
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='peixe',
#     p1_numero_subs="singular", p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None,
#     p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='específico', p2_orientacao_beta='NA',
#     p2_genero_beta='masculino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='específico', p2_orientacao_alpha='NA', p2_genero_alpha='masculino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='consciente', p2_tipo_de_nao_consciente=None,
#     p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='homem',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#
#     ##PARTICIPANTES REALIZADOS POR FP
#     part_fp_indice_preposicao_frase=None, part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None,
#     part_fp_tipo_qualificador=None, part_fp_indice_preposicao_qualif=None,
#     part_fp_determinacao_especificidade_beta=None, part_fp_orientacao_beta=None, part_fp_genero_beta=None,
#     part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
#     part_fp_determinacao_especificidade_alpha=None, part_fp_orientacao_alpha=None, part_fp_genero_alpha=None,
#     part_fp_numero_alpha=None, part_fp_morfologia_do_pronome_alpha=None,
#     part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
#     part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None,
#     part_fp_tipo_numerativo=None, part_fp_cardinal=None,
#     part_fp_genero_numerativo=None, part_fp_tipo_de_ente=None,
#     part_fp_tipo_de_nao_consciente=None, part_fp_tipo_de_nao_consciente_material=None,
#     part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente=None,
#     part_fp_substantivo_lematizado=None, part_fp_numero_subs=None, part_fp_genero_subs=None,
#     part_fp_tipo_feminino_ao=None,
#     part_fp_tipo_masc_ao=None, part_fp_acent_tonica=None, part_fp_nome_proprio=None,
#     part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None,
#     part_fp_morfologia_do_pronome=None, part_fp_reflexivo=None,  # classificador
#     part_fp_adjetivo_classificador=None,
#     # epitetos
#     part_fp_adj_epit_exp_pre=None,
#     part_fp_adj_epit_int_pre=None,
#     part_fp_adj_epit_exp_pos=None,
#     part_fp_adj_epit_int_pos=None,
#     part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
#     part_fp_contracao=None,
#
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
# # ->>>'O peixe impressionou o homem .'
# #########################################################
#
#
# oracao_mental(
#
#     # TRANSITIVIDADE
#     tipo_de_processo='Mental', indice_material=None, indice_agenciamento=2, indice_relacional=None,
#
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal='TI_NA', t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#
#     # # TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#
#     ##específico do processo_ Mental
#     fenomenalizacao='fenomenalização_fenômeno_simples', tipo_de_mental='superior_cognitivo',
#
#     ##processo_
#     tipo_de_experiencia_gv='Sentir', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='impressionar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade='positiva',
#
#     ##PARTICIPANTES
#
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente="não_consciente", p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='animal',
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='peixe',
#     p1_numero_subs="singular", p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None,
#     p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#     p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#
#     ##PARTICIPANTES REALIZADOS POR FP
#     part_fp_indice_preposicao_frase=0,part_fp_dissoc_ente_nucleo=None, part_fp_tem_qualificador=None, part_fp_tipo_qualificador=None,
#     part_fp_indice_preposicao_qualif=None, part_fp_determinacao_especificidade_beta='específico', part_fp_orientacao_beta='NA',
#     part_fp_genero_beta='masculino', part_fp_numero_beta=None, part_fp_morfologia_do_pronome_beta=None,
#     part_fp_determinacao_especificidade_alpha='específico', part_fp_orientacao_alpha='NA', part_fp_genero_alpha='masculino',
#     part_fp_numero_alpha='singular',
#     part_fp_morfologia_do_pronome_alpha=None, part_fp_pessoa_da_interlocucao_possuidor=None, part_fp_numero_obj_possuido=None,
#     part_fp_genero_obj_possuido=None, part_fp_pessoa_da_interlocucao_proximidade=None, part_fp_tipo_numerativo=None,
#     part_fp_cardinal=None, part_fp_genero_numerativo=None,
#     part_fp_tipo_de_ente='consciente', part_fp_tipo_de_nao_consciente=None,
#     part_fp_tipo_de_nao_consciente_material=None,
#     part_fp_tipo_de_nao_consciente_semiotico=None, part_fp_classe_palavra_ente='substantivo_comum',
#     part_fp_substantivo_lematizado='homem',
#     part_fp_numero_subs='singular', part_fp_genero_subs='não-binário', part_fp_tipo_feminino_ao=None, part_fp_tipo_masc_ao=None,
#     part_fp_acent_tonica=None,
#     part_fp_nome_proprio=None,
#     part_fp_pessoa_da_interlocucao=None, part_fp_transitividade_verbo=None, part_fp_tonicidade=None, part_fp_morfologia_do_pronome=None,
#     part_fp_reflexivo=None,
#     # classificador
#     part_fp_adjetivo_classificador=None,
#     # epitetos
#     part_fp_adj_epit_exp_pre=None,
#     part_fp_adj_epit_int_pre=None,
#     part_fp_adj_epit_exp_pos=None,
#     part_fp_adj_epit_int_pos=None,
#     part_fp_genero_adjetivo=None, part_fp_numero_adjetivo=None,
#
#     part_fp_contracao=None,
#
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
# # ->>>'O peixe impressionou ao homem .'
#
#
#
# # ORACÃO MATERIAL

oracao_material(
# TRANSITIVIDADE
        tipo_de_processo='Material', indice_material=2, indice_agenciamento=2, indice_relacional=None,
        indice_atrib=None,
        # MODO
        responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
        # TEMA INTERPESSOAL
        tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
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
        orientacao_modal='não_orientado', orientacao_transitiva='não_direcional',
        selecao_tematica='proeminente', tema_default=None,
        tema_default_indicativo=None, tema_identificativo='NA',
        tema_angulo=None, tema_elemental=None,
        tema_proeminente='intensivo_relativo_papel_transitivo_nuclear_participante',
        ##Parâmetors específicos do processo_ Mental
        # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
        ##Parâmetors específicos do processo material
        # iniciador
        iniciador='+iniador',

        resultado_qualitativo=None, realizacao_atributo=None,
        # realizado por adjetivo
        atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
        # realizado por frase preposicional
        atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
        atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
        atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
        atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
        atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
        atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
        atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
        atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
        atrib_tipo_numerativo=None, atrib_cardinal=None,
        atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
        atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
        atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
        atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
        atrib_tipo_feminino_ao=None,
        atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
        atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
        atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
        atrib_adjetivo_classificador=None,
        # epitetos
        atrib_adj_epit_exp_pre=None,
        atrib_adj_epit_int_pre=None,
        atrib_adj_epit_exp_pos=None,
        atrib_adj_epit_int_pos=None,
        atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
        atrib_contracao=None,
        # ESCOPO
        escopo=None,
        # locativo
        locativo=None,
        ##extensão beneficiarios
        beneficiario=None,

        ##processo_
        tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
        funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
        verbo_lex='rolar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
        oi_tipo_de_pessoa_lex='3pessoa',
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
        p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino', p1_numero_alpha='singular',
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
        p1_cardinal=None, p1_genero_numerativo=None,
        p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum', p1_substantivo_lematizado='bola',
        p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
        p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
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
        ##PARTICIPANTE P1 REALIZADOS POR FP
        p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
        p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
        p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
        p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
        p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
        p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
        p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
        p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
        p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
        p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
        p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
        p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
        p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
        p1_fp_tipo_feminino_ao=None,
        p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
        p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
        p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
        p1_fp_adjetivo_classificador=None,
        # epitetos
        p1_fp_adj_epit_exp_pre=None,
        p1_fp_adj_epit_int_pre=None,
        p1_fp_adj_epit_exp_pos=None,
        p1_fp_adj_epit_int_pos=None,
        p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
        p1_fp_contracao=None,

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
        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta='específico', p3_orientacao_beta='NA',
        p3_genero_beta='masculino', p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha='específico', p3_orientacao_alpha='NA', p3_genero_alpha='masculino',
        p3_numero_alpha='singular',
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
        p3_cardinal=None, p3_genero_numerativo=None,
        p3_tipo_de_ente='consciente', p3_tipo_de_nao_consciente=None,
        p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente='substantivo_comum',
        p3_substantivo_lematizado='homem',
        p3_numero_subs='singular', p3_genero_subs='não-binário', p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
        p3_acent_tonica=None,
        p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None,
        # classificador
        p3_adjetivo_classificador=None,
        # epitetos
        p3_adj_epit_exp_pre=None,
        p3_adj_epit_int_pre=None,
        p3_adj_epit_exp_pos=None,
        p3_adj_epit_int_pos=None,
        p3_genero_adjetivo=None, p3_numero_adjetivo=None,

        p3_contracao=None,

        ##PARTICIPANTE P3 REALIZADOS POR FP
        p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
        p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
        p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
        p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
        p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
        p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
        p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
        p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
        p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
        p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
        p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
        p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
        p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
        p3_fp_tipo_feminino_ao=None,
        p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
        p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
        p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
        p3_fp_adjetivo_classificador=None,
        # epitetos
        p3_fp_adj_epit_exp_pre=None,
        p3_fp_adj_epit_int_pre=None,
        p3_fp_adj_epit_exp_pos=None,
        p3_fp_adj_epit_int_pos=None,
        p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
        p3_fp_contracao=None,
        ##CIRCUNSTANCIA
        circunst_realizacao_circunstancia=None,
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
        circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
        circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
        circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
        circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
        circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None

)

# # O homem rolou a bola
#
#
# oracao_material(
# # TRANSITIVIDADE
#         tipo_de_processo='Material', indice_material=2, indice_agenciamento=0, indice_relacional=None,
#         indice_atrib=None,
#         # MODO
#         responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#         # TEMA INTERPESSOAL
#         tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#         # TEMA INTERP realizado por grupo adverbial
#         t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#         t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#         t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#         t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#         t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#         #
#         # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#         t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#         t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#         t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#         t_inter_fp_numero_beta=None,
#         t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#         t_inter_fp_orientacao_alpha=None,
#         t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#         t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#         t_inter_fp_genero_obj_possuido=None,
#         t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#         t_inter_fp_genero_numerativo=None,
#         t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#         t_inter_fp_tipo_de_nao_consciente_material=None,
#         t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#         t_inter_fp_substantivo_lematizado=None,
#         t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#         t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#         t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#         t_inter_fp_tonicidade=None,
#         t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#         t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#         t_inter_fp_contracao=None,
#         #
#         # 		#
#         t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#         #
#         # 	#TEMA TEXTUAL
#         t_text_tem_tema_textual=False, t_text_indice_cont=None,
#         t_text_tipo_de_conjuncao=None,
#         t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#         t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#         t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#         # TEMA IDEACIONAL
#         orientacao_modal='não_orientado', orientacao_transitiva='não_direcional',
#         selecao_tematica='proeminente', tema_default=None,
#         tema_default_indicativo=None, tema_identificativo='NA',
#         tema_angulo=None, tema_elemental=None,
#         tema_proeminente='intensivo_relativo_papel_transitivo_nuclear_participante',
#         ##Parâmetors específicos do processo_ Mental
#         # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#         ##Parâmetors específicos do processo material
#         # iniciador
#         iniciador=None,
#
#         resultado_qualitativo=None, realizacao_atributo=None,
#         # realizado por adjetivo
#         atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#         # realizado por frase preposicional
#         atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#         atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#         atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#         atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#         atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#         atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#         atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#         atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#         atrib_tipo_numerativo=None, atrib_cardinal=None,
#         atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#         atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#         atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#         atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#         atrib_tipo_feminino_ao=None,
#         atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#         atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#         atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#         atrib_adjetivo_classificador=None,
#         # epitetos
#         atrib_adj_epit_exp_pre=None,
#         atrib_adj_epit_int_pre=None,
#         atrib_adj_epit_exp_pos=None,
#         atrib_adj_epit_int_pos=None,
#         atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#         atrib_contracao=None,
#         # ESCOPO
#         escopo=None,
#         # locativo
#         locativo=None,
#         ##extensão beneficiarios
#         beneficiario=None,
#
#         ##processo_
#         tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#         funcao_no_grupo_verbal_1=None,
#         verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#         padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#         tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#         padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#         tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#         padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#         tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#         padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#         verbo_lex='rolar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#         oi_tipo_de_pessoa_lex='3pessoa',
#         padrao_pessoa_morfologia_lex='Morfologia_padrão',
#         # POLARIDADE
#         tipo_polaridade=None,
#         ##PARTICIPANTES
#         # P1
#         p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#         p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#         p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#         p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino', p1_numero_alpha='singular',
#         p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#         p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#         p1_cardinal=None, p1_genero_numerativo=None,
#         p1_tipo_de_ente='não_consciente', p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='objeto_material',
#         p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum', p1_substantivo_lematizado='bola',
#         p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
#         p1_nome_proprio=None,
#         p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#         p1_reflexivo=None,
#         # classificador
#         p1_adjetivo_classificador=None,
#         # epitetos
#         p1_adj_epit_exp_pre=None,
#         p1_adj_epit_int_pre=None,
#         p1_adj_epit_exp_pos=None,
#         p1_adj_epit_int_pos=None,
#         p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#         p1_contracao=None,
#         ##PARTICIPANTE P1 REALIZADOS POR FP
#         p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#         p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#         p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#         p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#         p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#         p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#         p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#         p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#         p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#         p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#         p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#         p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#         p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#         p1_fp_tipo_feminino_ao=None,
#         p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#         p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#         p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#         p1_fp_adjetivo_classificador=None,
#         # epitetos
#         p1_fp_adj_epit_exp_pre=None,
#         p1_fp_adj_epit_int_pre=None,
#         p1_fp_adj_epit_exp_pos=None,
#         p1_fp_adj_epit_int_pos=None,
#         p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#         p1_fp_contracao=None,
#
#         # P2
#         p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#         p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#         p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#         p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#         p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#         p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#         p2_cardinal=None, p2_genero_numerativo=None,
#         p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#         p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#         p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#         p2_nome_proprio=None,
#         p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#         p2_reflexivo=None,
#         # classificador
#         p2_adjetivo_classificador=None,
#         # epitetos
#         p2_adj_epit_exp_pre=None,
#         p2_adj_epit_int_pre=None,
#         p2_adj_epit_exp_pos=None,
#         p2_adj_epit_int_pos=None,
#         p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#         p2_contracao=None,
#         # P3
#         p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#         p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#         p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#         p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None,
#         p3_numero_alpha=None,
#         p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#         p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#         p3_cardinal=None, p3_genero_numerativo=None,
#         p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None,
#         p3_tipo_de_nao_consciente_material=None,
#         p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None,
#         p3_substantivo_lematizado=None,
#         p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
#         p3_acent_tonica=None,
#         p3_nome_proprio=None,
#         p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#         p3_reflexivo=None,
#         # classificador
#         p3_adjetivo_classificador=None,
#         # epitetos
#         p3_adj_epit_exp_pre=None,
#         p3_adj_epit_int_pre=None,
#         p3_adj_epit_exp_pos=None,
#         p3_adj_epit_int_pos=None,
#         p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#         p3_contracao=None,
#
#         ##PARTICIPANTE P3 REALIZADOS POR FP
#         p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#         p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#         p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#         p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#         p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#         p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#         p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#         p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#         p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#         p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#         p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#         p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#         p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#         p3_fp_tipo_feminino_ao=None,
#         p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#         p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#         p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#         p3_fp_adjetivo_classificador=None,
#         # epitetos
#         p3_fp_adj_epit_exp_pre=None,
#         p3_fp_adj_epit_int_pre=None,
#         p3_fp_adj_epit_exp_pos=None,
#         p3_fp_adj_epit_int_pos=None,
#         p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#         p3_fp_contracao=None,
#         ##CIRCUNSTANCIA
#         circunst_realizacao_circunstancia=None,
#         circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#         circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#         circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#         circunst_numero_beta=None,
#         circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#         circunst_orientacao_alpha=None,
#         circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#         circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#         circunst_genero_obj_possuido=None,
#         circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#         circunst_genero_numerativo=None,
#         circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#         circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#         circunst_substantivo_lematizado=None,
#         circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#         circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#         circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#         circunst_tonicidade=None,
#         circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#         # classificador
#         circunst_adjetivo_classificador=None,
#         # epitetos
#         circunst_adj_epit_exp_pre=None,
#         circunst_adj_epit_int_pre=None,
#         circunst_adj_epit_exp_pos=None,
#         circunst_adj_epit_int_pos=None,
#         circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#         circunst_contracao=None,
#         circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#         circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#         circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#         circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#         circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # A bola rolou.
#
#
#
#
# oracao_material(
# # TRANSITIVIDADE
#         tipo_de_processo='Material', indice_material=2, indice_agenciamento=0, indice_relacional=None,
#         indice_atrib=None,
#         # MODO
#         responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#         # TEMA INTERPESSOAL
#         tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#         # TEMA INTERP realizado por grupo adverbial
#         t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#         t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#         t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#         t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#         t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#         #
#         # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#         t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#         t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#         t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#         t_inter_fp_numero_beta=None,
#         t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#         t_inter_fp_orientacao_alpha=None,
#         t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#         t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#         t_inter_fp_genero_obj_possuido=None,
#         t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#         t_inter_fp_genero_numerativo=None,
#         t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#         t_inter_fp_tipo_de_nao_consciente_material=None,
#         t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#         t_inter_fp_substantivo_lematizado=None,
#         t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#         t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#         t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#         t_inter_fp_tonicidade=None,
#         t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#         t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#         t_inter_fp_contracao=None,
#         #
#         # 		#
#         t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#         #
#         # 	#TEMA TEXTUAL
#         t_text_tem_tema_textual=False, t_text_indice_cont=None,
#         t_text_tipo_de_conjuncao=None,
#         t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#         t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#         t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#         # TEMA IDEACIONAL
#         orientacao_modal='orientado', orientacao_transitiva='direcional',
#         selecao_tematica='default', tema_default='indicativo',
#         tema_default_indicativo='declarativo', tema_identificativo='NA',
#         tema_angulo=None, tema_elemental=None,
#         tema_proeminente=None,
#         ##Parâmetors específicos do processo_ Mental
#         # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#         ##Parâmetors específicos do processo material
#         # iniciador
#         iniciador=None,
#
#         resultado_qualitativo=None, realizacao_atributo=None,
#         # realizado por adjetivo
#         atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#         # realizado por frase preposicional
#         atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#         atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#         atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#         atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#         atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#         atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#         atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#         atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#         atrib_tipo_numerativo=None, atrib_cardinal=None,
#         atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#         atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#         atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#         atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#         atrib_tipo_feminino_ao=None,
#         atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#         atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#         atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#         atrib_adjetivo_classificador=None,
#         # epitetos
#         atrib_adj_epit_exp_pre=None,
#         atrib_adj_epit_int_pre=None,
#         atrib_adj_epit_exp_pos=None,
#         atrib_adj_epit_int_pos=None,
#         atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#         atrib_contracao=None,
#         # ESCOPO
#         escopo=None,
#         # locativo
#         locativo='+locativo',
#         ##extensão beneficiarios
#         beneficiario=None,
#
#         ##processo_
#         tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#         funcao_no_grupo_verbal_1=None,
#         verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#         padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#         tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#         padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#         tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#         padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#         tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#         padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#         verbo_lex='rolar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#         oi_tipo_de_pessoa_lex='3pessoa',
#         padrao_pessoa_morfologia_lex='Morfologia_padrão',
#         # POLARIDADE
#         tipo_polaridade=None,
#         ##PARTICIPANTES
#         # P1
#         p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#         p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#         p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#         p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino', p1_numero_alpha='singular',
#         p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#         p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#         p1_cardinal=None, p1_genero_numerativo=None,
#         p1_tipo_de_ente='não_consciente', p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='objeto_material',
#         p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum', p1_substantivo_lematizado='bola',
#         p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
#         p1_nome_proprio=None,
#         p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#         p1_reflexivo=None,
#         # classificador
#         p1_adjetivo_classificador=None,
#         # epitetos
#         p1_adj_epit_exp_pre=None,
#         p1_adj_epit_int_pre=None,
#         p1_adj_epit_exp_pos=None,
#         p1_adj_epit_int_pos=None,
#         p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#         p1_contracao=None,
#         ##PARTICIPANTE P1 REALIZADOS POR FP
#         p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#         p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#         p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#         p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#         p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#         p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#         p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#         p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#         p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#         p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#         p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#         p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#         p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#         p1_fp_tipo_feminino_ao=None,
#         p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#         p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#         p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#         p1_fp_adjetivo_classificador=None,
#         # epitetos
#         p1_fp_adj_epit_exp_pre=None,
#         p1_fp_adj_epit_int_pre=None,
#         p1_fp_adj_epit_exp_pos=None,
#         p1_fp_adj_epit_int_pos=None,
#         p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#         p1_fp_contracao=None,
#
#         # P2
#         p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#         p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#         p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#         p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#         p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#         p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#         p2_cardinal=None, p2_genero_numerativo=None,
#         p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#         p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#         p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#         p2_nome_proprio=None,
#         p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#         p2_reflexivo=None,
#         # classificador
#         p2_adjetivo_classificador=None,
#         # epitetos
#         p2_adj_epit_exp_pre=None,
#         p2_adj_epit_int_pre=None,
#         p2_adj_epit_exp_pos=None,
#         p2_adj_epit_int_pos=None,
#         p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#         p2_contracao=None,
#         # P3
#         p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#         p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#         p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#         p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None,
#         p3_numero_alpha=None,
#         p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#         p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#         p3_cardinal=None, p3_genero_numerativo=None,
#         p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None,
#         p3_tipo_de_nao_consciente_material=None,
#         p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None,
#         p3_substantivo_lematizado=None,
#         p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
#         p3_acent_tonica=None,
#         p3_nome_proprio=None,
#         p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#         p3_reflexivo=None,
#         # classificador
#         p3_adjetivo_classificador=None,
#         # epitetos
#         p3_adj_epit_exp_pre=None,
#         p3_adj_epit_int_pre=None,
#         p3_adj_epit_exp_pos=None,
#         p3_adj_epit_int_pos=None,
#         p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#         p3_contracao=None,
#
#         ##PARTICIPANTE P3 REALIZADOS POR FP
#
#         p3_fp_indice_preposicao_frase=8, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#         p3_fp_tipo_qualificador=None,
#         p3_fp_indice_preposicao_qualif=None, p3_fp_determinacao_especificidade_beta='específico',
#         p3_fp_orientacao_beta='NA',
#         p3_fp_genero_beta='feminino', p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#         p3_fp_determinacao_especificidade_alpha='específico', p3_fp_orientacao_alpha='NA',
#         p3_fp_genero_alpha='feminino',
#         p3_fp_numero_alpha='singular',
#         p3_fp_morfologia_do_pronome_alpha=None, p3_fp_pessoa_da_interlocucao_possuidor=None,
#         p3_fp_numero_obj_possuido=None,
#         p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None, p3_fp_tipo_numerativo=None,
#         p3_fp_cardinal=None, p3_fp_genero_numerativo=None,
#         p3_fp_tipo_de_ente='não_consciente', p3_fp_tipo_de_nao_consciente='material',
#         p3_fp_tipo_de_nao_consciente_material='objeto_material',
#         p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente='substantivo_comum',
#         p3_fp_substantivo_lematizado='rua',
#         p3_fp_numero_subs='singular', p3_fp_genero_subs='não-binário', p3_fp_tipo_feminino_ao=None,
#         p3_fp_tipo_masc_ao=None,
#         p3_fp_acent_tonica=None,
#         p3_fp_nome_proprio=None,
#         p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#         p3_fp_morfologia_do_pronome=None,
#         p3_fp_reflexivo=None,
#         # classificador
#         p3_fp_adjetivo_classificador=None,
#         # epitetos
#         p3_fp_adj_epit_exp_pre=None,
#         p3_fp_adj_epit_int_pre=None,
#         p3_fp_adj_epit_exp_pos=None,
#         p3_fp_adj_epit_int_pos=None,
#         p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#
#         p3_fp_contracao=None,
#         ##CIRCUNSTANCIA
#         circunst_realizacao_circunstancia=None,
#         circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#         circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#         circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#         circunst_numero_beta=None,
#         circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#         circunst_orientacao_alpha=None,
#         circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#         circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#         circunst_genero_obj_possuido=None,
#         circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#         circunst_genero_numerativo=None,
#         circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#         circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#         circunst_substantivo_lematizado=None,
#         circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#         circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#         circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#         circunst_tonicidade=None,
#         circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#         # classificador
#         circunst_adjetivo_classificador=None,
#         # epitetos
#         circunst_adj_epit_exp_pre=None,
#         circunst_adj_epit_int_pre=None,
#         circunst_adj_epit_exp_pos=None,
#         circunst_adj_epit_int_pos=None,
#         circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#         circunst_contracao=None,
#         circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#         circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#         circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#         circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#         circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # A bola rolou na rua.
#
#
#
# ########
#
#
# oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=2, indice_agenciamento=0, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=3,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='interrogativo_polar', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo=None, realizacao_atributo=None,
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo='+locativo',
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='rolar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#     p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente='não_consciente', p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='objeto_material',
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='bola',
#     p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#     p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None,
#     p3_numero_alpha=None,
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None,
#     p3_tipo_de_nao_consciente_material=None,
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None,
#     p3_substantivo_lematizado=None,
#     p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
#     p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#
#     p3_fp_indice_preposicao_frase=8, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None,
#     p3_fp_indice_preposicao_qualif=None, p3_fp_determinacao_especificidade_beta='específico',
#     p3_fp_orientacao_beta='NA',
#     p3_fp_genero_beta='feminino', p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha='específico', p3_fp_orientacao_alpha='NA',
#     p3_fp_genero_alpha='feminino',
#     p3_fp_numero_alpha='singular',
#     p3_fp_morfologia_do_pronome_alpha=None, p3_fp_pessoa_da_interlocucao_possuidor=None,
#     p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None, p3_fp_tipo_numerativo=None,
#     p3_fp_cardinal=None, p3_fp_genero_numerativo=None,
#     p3_fp_tipo_de_ente='não_consciente', p3_fp_tipo_de_nao_consciente='material',
#     p3_fp_tipo_de_nao_consciente_material='objeto_material',
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente='substantivo_comum',
#     p3_fp_substantivo_lematizado='rua',
#     p3_fp_numero_subs='singular', p3_fp_genero_subs='não-binário', p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None,
#     p3_fp_acent_tonica=None,
#     p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None,
#     p3_fp_reflexivo=None,
#     # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # A bola rolou na rua?
#
# ##############
#
#
# oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=2, indice_agenciamento=1, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo=None, realizacao_atributo=None,
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo='+escopo',
#     # locativo
#     locativo='+locativo',
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='subir', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#     p1_genero_beta='masculino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='homem',
#     p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#     p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta='específico', p3_orientacao_beta='NA',
#     p3_genero_beta='masculino', p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha='específico', p3_orientacao_alpha='NA', p3_genero_alpha='masculino',
#     p3_numero_alpha='singular',
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente='não_consciente', p3_tipo_de_nao_consciente='material', p3_tipo_de_nao_consciente_material='objeto_material',
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente='substantivo_comum',
#     p3_substantivo_lematizado='morro',
#     p3_numero_subs='singular', p3_genero_subs='não-binário', p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
#     p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
# # O homem subiu o morro
#
#
#
#
# oracao_material(
# # TRANSITIVIDADE
#         tipo_de_processo='Material', indice_material=3, indice_agenciamento=0, indice_relacional=None,
#         indice_atrib=None,
#         # MODO
#         responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#         # TEMA INTERPESSOAL
#         tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#         # TEMA INTERP realizado por grupo adverbial
#         t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#         t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#         t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#         t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#         t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#         #
#         # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#         t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#         t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#         t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#         t_inter_fp_numero_beta=None,
#         t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#         t_inter_fp_orientacao_alpha=None,
#         t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#         t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#         t_inter_fp_genero_obj_possuido=None,
#         t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#         t_inter_fp_genero_numerativo=None,
#         t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#         t_inter_fp_tipo_de_nao_consciente_material=None,
#         t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#         t_inter_fp_substantivo_lematizado=None,
#         t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#         t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#         t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#         t_inter_fp_tonicidade=None,
#         t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#         t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#         t_inter_fp_contracao=None,
#         #
#         # 		#
#         t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#         #
#         # 	#TEMA TEXTUAL
#         t_text_tem_tema_textual=False, t_text_indice_cont=None,
#         t_text_tipo_de_conjuncao=None,
#         t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#         t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#         t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#         # TEMA IDEACIONAL
#         orientacao_modal='orientado', orientacao_transitiva='direcional',
#         selecao_tematica='default', tema_default='indicativo',
#         tema_default_indicativo='declarativo', tema_identificativo='NA',
#         tema_angulo=None, tema_elemental=None,
#         tema_proeminente=None,
#         ##Parâmetors específicos do processo_ Mental
#         # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#         ##Parâmetors específicos do processo material
#         # iniciador
#         iniciador=None,
#
#         resultado_qualitativo=None, realizacao_atributo=None,
#         # realizado por adjetivo
#         atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#         # realizado por frase preposicional
#         atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#         atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#         atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#         atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#         atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#         atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#         atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#         atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#         atrib_tipo_numerativo=None, atrib_cardinal=None,
#         atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#         atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#         atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#         atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#         atrib_tipo_feminino_ao=None,
#         atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#         atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#         atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#         atrib_adjetivo_classificador=None,
#         # epitetos
#         atrib_adj_epit_exp_pre=None,
#         atrib_adj_epit_int_pre=None,
#         atrib_adj_epit_exp_pos=None,
#         atrib_adj_epit_int_pos=None,
#         atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#         atrib_contracao=None,
#         # ESCOPO
#         escopo=None,
#         # locativo
#         locativo=None,
#         ##extensão beneficiarios
#         beneficiario=None,
#
#         ##processo_
#         tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#         funcao_no_grupo_verbal_1=None,
#         verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#         padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#         tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#         padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#         tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#         padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#         tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#         padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Sentir', funcao_no_grupo_verbal_pos_final='Evento',
#         verbo_lex='formar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#         oi_tipo_de_pessoa_lex='3pessoa',
#         padrao_pessoa_morfologia_lex='Morfologia_padrão',
#         # POLARIDADE
#         tipo_polaridade=None,
#         ##PARTICIPANTES
#         # P1
#         p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#         p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#         p1_genero_beta='masculino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#         p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino', p1_numero_alpha='singular',
#         p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#         p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#         p1_cardinal=None, p1_genero_numerativo=None,
#         p1_tipo_de_ente='não_consciente', p1_tipo_de_nao_consciente='material', p1_tipo_de_nao_consciente_material='objeto_material',
#         p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum', p1_substantivo_lematizado='gelo',
#         p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
#         p1_nome_proprio=None,
#         p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#         p1_reflexivo=None,
#         # classificador
#         p1_adjetivo_classificador=None,
#         # epitetos
#         p1_adj_epit_exp_pre=None,
#         p1_adj_epit_int_pre=None,
#         p1_adj_epit_exp_pos=None,
#         p1_adj_epit_int_pos=None,
#         p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#         p1_contracao=None,
#         ##PARTICIPANTE P1 REALIZADOS POR FP
#         p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#         p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#         p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#         p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#         p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#         p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#         p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#         p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#         p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#         p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#         p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#         p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#         p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#         p1_fp_tipo_feminino_ao=None,
#         p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#         p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#         p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#         p1_fp_adjetivo_classificador=None,
#         # epitetos
#         p1_fp_adj_epit_exp_pre=None,
#         p1_fp_adj_epit_int_pre=None,
#         p1_fp_adj_epit_exp_pos=None,
#         p1_fp_adj_epit_int_pos=None,
#         p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#         p1_fp_contracao=None,
#
#         # P2
#         p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#         p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#         p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#         p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#         p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#         p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#         p2_cardinal=None, p2_genero_numerativo=None,
#         p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#         p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#         p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#         p2_nome_proprio=None,
#         p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#         p2_reflexivo=None,
#         # classificador
#         p2_adjetivo_classificador=None,
#         # epitetos
#         p2_adj_epit_exp_pre=None,
#         p2_adj_epit_int_pre=None,
#         p2_adj_epit_exp_pos=None,
#         p2_adj_epit_int_pos=None,
#         p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#         p2_contracao=None,
#         # P3
#         p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#         p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#         p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#         p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None,
#         p3_numero_alpha=None,
#         p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#         p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#         p3_cardinal=None, p3_genero_numerativo=None,
#         p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None,
#         p3_tipo_de_nao_consciente_material=None,
#         p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None,
#         p3_substantivo_lematizado=None,
#         p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
#         p3_acent_tonica=None,
#         p3_nome_proprio=None,
#         p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#         p3_reflexivo=None,
#         # classificador
#         p3_adjetivo_classificador=None,
#         # epitetos
#         p3_adj_epit_exp_pre=None,
#         p3_adj_epit_int_pre=None,
#         p3_adj_epit_exp_pos=None,
#         p3_adj_epit_int_pos=None,
#         p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#         p3_contracao=None,
#
#         ##PARTICIPANTE P3 REALIZADOS POR FP
#         p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#         p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#         p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#         p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#         p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#         p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#         p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#         p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#         p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#         p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#         p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#         p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#         p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#         p3_fp_tipo_feminino_ao=None,
#         p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#         p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#         p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#         p3_fp_adjetivo_classificador=None,
#         # epitetos
#         p3_fp_adj_epit_exp_pre=None,
#         p3_fp_adj_epit_int_pre=None,
#         p3_fp_adj_epit_exp_pos=None,
#         p3_fp_adj_epit_int_pos=None,
#         p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#         p3_fp_contracao=None,
#         ##CIRCUNSTANCIA
#         circunst_realizacao_circunstancia=None,
#         circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#         circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#         circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#         circunst_numero_beta=None,
#         circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#         circunst_orientacao_alpha=None,
#         circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#         circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#         circunst_genero_obj_possuido=None,
#         circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#         circunst_genero_numerativo=None,
#         circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#         circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#         circunst_substantivo_lematizado=None,
#         circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#         circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#         circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#         circunst_tonicidade=None,
#         circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#         # classificador
#         circunst_adjetivo_classificador=None,
#         # epitetos
#         circunst_adj_epit_exp_pre=None,
#         circunst_adj_epit_int_pre=None,
#         circunst_adj_epit_exp_pos=None,
#         circunst_adj_epit_int_pos=None,
#         circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#         circunst_contracao=None,
#         circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#         circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#         circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#         circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#         circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # 'O gelo formou.'
#
# #######
# oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=0, indice_agenciamento=2, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo='resultado_atributo', realizacao_atributo='atributo_adjetivo',
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado='bamba', atributo_genero='feminino', atributo_numero='singular',
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=None, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo=None,
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='fazer', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#     p1_genero_beta='masculino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None,
#     p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='homem',
#     p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='específico', p2_orientacao_beta='NA',
#     p2_genero_beta='feminino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='específico', p2_orientacao_alpha='NA', p2_genero_alpha='feminino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='objeto_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='parede',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
#     p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
# #
# # #'O homem fez a parede bamba.'
# #
# #
# #
# # #######
# oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=0, indice_agenciamento=2, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo='resultado_atributo', realizacao_atributo='atributo_frase_preposicional',
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=6, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos='verde',
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo='não-binário', atrib_numero_adjetivo='singular',
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo=None,
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='pintar', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#     p1_genero_beta='masculino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None,
#     p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='homem',
#     p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='específico', p2_orientacao_beta='NA',
#     p2_genero_beta='feminino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='específico', p2_orientacao_alpha='NA', p2_genero_alpha='feminino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='objeto_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='parede',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
#     p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # #'O homem pintou a parede de verde.'
# #
#
#

#
# # #######
# oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=1, indice_agenciamento=2, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo=None, realizacao_atributo=None,
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=6, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo=None,
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='fazer', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#     p1_genero_beta='masculino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None,
#     p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='homem',
#     p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='não_específico', p2_orientacao_alpha='NA', p2_genero_alpha='masculino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='objeto_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='bolo',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
#     p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )

#'O homem fez um bolo.'

###
#
# oracao_material_teste(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=2, indice_agenciamento=6, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=3, pressuposicao_do_sujeito=3, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo=None, realizacao_atributo=None,
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=6, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo=None,
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='não_agenciado', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='chover', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
#     p1_numero_subs=None, p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha=None, p2_orientacao_alpha=None, p2_genero_alpha=None, p2_numero_alpha=None,
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente=None, p2_tipo_de_nao_consciente=None, p2_tipo_de_nao_consciente_material=None,
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente=None, p2_substantivo_lematizado=None,
#     p2_numero_subs=None, p2_genero_subs=None, p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None, p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta='NA',
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha='NA', p3_genero_alpha='não-binário',
#     p3_numero_alpha='singular',
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo='cardinal',
#     p3_cardinal=83000, p3_genero_numerativo='masculino',
#     p3_tipo_de_ente='não_consciente', p3_tipo_de_nao_consciente='material',
#     p3_tipo_de_nao_consciente_material='objeto_material',
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente='substantivo_comum',
#     p3_substantivo_lematizado='milímetro',
#     p3_numero_subs='plural', p3_genero_subs='não-binário', p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
#     p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None
#     ,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )

# 'Choveu oitenta e três mil milímetros.'

oracao_material(
    # TRANSITIVIDADE
    tipo_de_processo='Material', indice_material=2, indice_agenciamento=5, indice_relacional=None,
    indice_atrib=None,
    # MODO
    responsabilidade=3, pressuposicao_do_sujeito=3, tipo_modo=1,
    # TEMA INTERPESSOAL
    tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
    # TEMA INTERP realizado por grupo adverbial
    t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
    t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
    t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
    t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
    t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
    #
    # 		# TEMA INTERPESSOAL realiziado por frase preposicional
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
    ##Parâmetors específicos do processo_ Mental
    # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
    ##Parâmetors específicos do processo material
    # iniciador
    iniciador=None,

    resultado_qualitativo=None, realizacao_atributo=None,
    # realizado por adjetivo
    atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
    # realizado por frase preposicional
    atrib_indice_preposicao_frase=6, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
    atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
    atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
    atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
    atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
    atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
    atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
    atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
    atrib_tipo_numerativo=None, atrib_cardinal=None,
    atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
    atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
    atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
    atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
    atrib_tipo_feminino_ao=None,
    atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
    atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
    atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
    atrib_adjetivo_classificador=None,
    # epitetos
    atrib_adj_epit_exp_pre=None,
    atrib_adj_epit_int_pre=None,
    atrib_adj_epit_exp_pos=None,
    atrib_adj_epit_int_pos=None,
    atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
    atrib_contracao=None,
    # ESCOPO
    escopo=None,
    # locativo
    locativo=None,
    ##extensão beneficiarios
    beneficiario=None,

    ##processo_
    tipo_de_experiencia_gv='Fazer', agencia='não_agenciado', tipo_de_experiencia_1=None,
    funcao_no_grupo_verbal_1=None,
    verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
    padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
    tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
    padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
    tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
    padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
    tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
    padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
    verbo_lex='chover', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
    oi_tipo_de_pessoa_lex='3pessoa',
    padrao_pessoa_morfologia_lex='Morfologia_padrão',
    # POLARIDADE
    tipo_polaridade=None,
    ##PARTICIPANTES
    # P1
    p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
    p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
    p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
    p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
    p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
    p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
    p1_cardinal=None, p1_genero_numerativo=None,
    p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
    p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
    p1_numero_subs=None, p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
    p1_nome_proprio=None,
    p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
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
    ##PARTICIPANTE P1 REALIZADOS POR FP
    p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
    p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
    p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
    p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
    p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
    p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
    p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
    p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
    p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
    p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
    p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
    p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
    p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
    p1_fp_tipo_feminino_ao=None,
    p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
    p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
    p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
    p1_fp_adjetivo_classificador=None,
    # epitetos
    p1_fp_adj_epit_exp_pre=None,
    p1_fp_adj_epit_int_pre=None,
    p1_fp_adj_epit_exp_pos=None,
    p1_fp_adj_epit_int_pos=None,
    p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
    p1_fp_contracao=None,

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
    # P3
    p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
    p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
    p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
    p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
    p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
    p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
    p3_cardinal=None, p3_genero_numerativo=None,
    p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
    p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
    p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
    p3_nome_proprio=None,
    p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
    p3_reflexivo=None,
    # classificador
    p3_adjetivo_classificador=None,
    # epitetos
    p3_adj_epit_exp_pre=None,
    p3_adj_epit_int_pre=None,
    p3_adj_epit_exp_pos=None,
    p3_adj_epit_int_pos=None,
    p3_genero_adjetivo=None, p3_numero_adjetivo=None,

    p3_contracao=None
    ,

    ##PARTICIPANTE P3 REALIZADOS POR FP
    p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
    p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
    p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
    p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
    p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
    p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
    p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
    p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
    p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
    p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
    p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
    p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
    p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
    p3_fp_tipo_feminino_ao=None,
    p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
    p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
    p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
    p3_fp_adjetivo_classificador=None,
    # epitetos
    p3_fp_adj_epit_exp_pre=None,
    p3_fp_adj_epit_int_pre=None,
    p3_fp_adj_epit_exp_pos=None,
    p3_fp_adj_epit_int_pos=None,
    p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
    p3_fp_contracao=None,
    ##CIRCUNSTANCIA
    circunst_realizacao_circunstancia=None,
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
    circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
    circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
    circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
    circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
    circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None

)
#

# 'Choveu.'
#
#
# oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=1, indice_agenciamento=3, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='não_orientado', orientacao_transitiva='não_direcional',
#     selecao_tematica='proeminente', tema_default=None,
#     tema_default_indicativo=None, tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente='intensivo_relativo_papel_transitivo_nuclear_participante',
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo=None, realizacao_atributo=None,
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=6, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo=None,
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_passiva', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4='Ser', funcao_no_grupo_verbal_4='Auxiliar', verbo_4='ser',
#     tipo_de_orientacao_4='pretérito_perfectivo_I', oi_numero_4='singular', genero_4=None, oi_tipo_de_pessoa_4='3pessoa',
#         padrao_pessoa_morfologia_4='Morfologia_padrão', tipo_de_experiencia_lex='Fazer',
#     funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='fazer', tipo_de_orientacao_lex='particípio', oi_numero_lex='singular', genero_lex='masculino',
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta=None, p1_orientacao_beta=None,
#     p1_genero_beta=None, p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha=None, p1_orientacao_alpha=None, p1_genero_alpha=None, p1_numero_alpha=None,
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente=None, p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente=None, p1_substantivo_lematizado=None,
#     p1_numero_subs=None, p1_genero_subs=None, p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None, p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=11, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha='específico', p1_fp_orientacao_alpha='NA', p1_fp_genero_alpha='masculino',
#     p1_fp_numero_alpha='singular', p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente='consciente',
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente='substantivo_comum',
#     p1_fp_substantivo_lematizado='homem', p1_fp_numero_subs='singular', p1_fp_genero_subs='não-binário',
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='específico', p2_orientacao_alpha='NA', p2_genero_alpha='masculino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='objeto_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='bolo',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
#     p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# # O bolo foi feito pelo homem.'
#
#



#RELACIONAIS



estrutura_gn(dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
        indice_preposicao_qualif=None, determinacao_especificidade_beta='não_específico', orientacao_beta='NA',
        genero_beta='feminino', numero_beta=None, morfologia_do_pronome_beta=None,
        determinacao_especificidade_alpha='não_específico', orientacao_alpha='NA', genero_alpha='feminino',
        numero_alpha='singular',
        morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
        genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None,
        cardinal=None, genero_numerativo=None,
        tipo_de_ente='consciente', tipo_de_nao_consciente=None,
        tipo_de_nao_consciente_material=None,
        tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
        substantivo_lematizado='arquiteta',
        numero_subs='singular', genero_subs='feminino', tipo_feminino_ao=None, tipo_masc_ao=None,
        acent_tonica=None,
        nome_proprio=None,
        pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
        reflexivo=None)

oracao_relacional(
    # TRANSITIVIDADE
        tipo_de_processo='Relacional',indice_material=None, indice_agenciamento=1, indice_relacional=0,
        indice_atrib=5,
        # MODO
        responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
        # TEMA INTERPESSOAL
        tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
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
        # PARÂMETROS ESPEĆIFICOS DA RELACIONAL
        # ATRIBUTIVAS
        especificacao_tipo_modo_relacao='entidade', fase_atribuicao='neutra',
        dominio_atribuicao='semiótico', tipo_de_realizacao_da_relacao=None,

        ##atributivas possessivas
        tipo_possuidor=None,

        ##processo_
        tipo_de_experiencia_gv='Ser', agencia='não_agenciado', tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Ser', funcao_no_grupo_verbal_pos_final='Evento',
        verbo_lex='ser', tipo_de_orientacao_lex='pretérito_imperfectivo',
        oi_numero_lex='singular', genero_lex=None, oi_tipo_de_pessoa_lex='3pessoa',
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
        p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino',
        p1_numero_alpha='singular',
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
        p1_cardinal=None, p1_genero_numerativo=None,
        p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
        p1_substantivo_lematizado='mulher',
        p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
        p1_acent_tonica=None,
        p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
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
        ##PARTICIPANTE P1 REALIZADOS POR FP
        ##PARTICIPANTE P1 REALIZADOS POR FP
        p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
        p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
        p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
        p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
        p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
        p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
        p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
        p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
        p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
        p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
        p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
        p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
        p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
        p1_fp_tipo_feminino_ao=None,
        p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
        p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
        p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
        p1_fp_adjetivo_classificador=None,
        # epitetos
        p1_fp_adj_epit_exp_pre=None,
        p1_fp_adj_epit_int_pre=None,
        p1_fp_adj_epit_exp_pos=None,
        p1_fp_adj_epit_int_pos=None,
        p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
        p1_fp_contracao=None,
        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='não_específico', p2_orientacao_beta='NA',
        p2_genero_beta='feminino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha='não_específico', p2_orientacao_alpha='NA', p2_genero_alpha='feminino',
        p2_numero_alpha='singular',
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
        p2_cardinal=None, p2_genero_numerativo=None,
        p2_tipo_de_ente='consciente', p2_tipo_de_nao_consciente=None,
        p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
        p2_substantivo_lematizado='arquiteta',
        p2_numero_subs='singular', p2_genero_subs='feminino', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
        p2_acent_tonica=None,
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
        # P2 FRASE PREP
        p2_fp_indice_preposicao_frase=None, p2_fp_dissoc_ente_nucleo=None, p2_fp_tem_qualificador=None,
        p2_fp_tipo_qualificador=None, p2_fp_indice_preposicao_qualif=None,
        p2_fp_determinacao_especificidade_beta=None, p2_fp_orientacao_beta=None, p2_fp_genero_beta=None,
        p2_fp_numero_beta=None, p2_fp_morfologia_do_pronome_beta=None,
        p2_fp_determinacao_especificidade_alpha=None, p2_fp_orientacao_alpha=None, p2_fp_genero_alpha=None,
        p2_fp_numero_alpha=None, p2_fp_morfologia_do_pronome_alpha=None,
        p2_fp_pessoa_da_interlocucao_possuidor=None, p2_fp_numero_obj_possuido=None,
        p2_fp_genero_obj_possuido=None, p2_fp_pessoa_da_interlocucao_proximidade=None,
        p2_fp_tipo_numerativo=None, p2_fp_cardinal=None,
        p2_fp_genero_numerativo=None, p2_fp_tipo_de_ente=None,
        p2_fp_tipo_de_nao_consciente=None, p2_fp_tipo_de_nao_consciente_material=None,
        p2_fp_tipo_de_nao_consciente_semiotico=None, p2_fp_classe_palavra_ente=None,
        p2_fp_substantivo_lematizado=None, p2_fp_numero_subs=None, p2_fp_genero_subs=None,
        p2_fp_tipo_feminino_ao=None,
        p2_fp_tipo_masc_ao=None, p2_fp_acent_tonica=None, p2_fp_nome_proprio=None,
        p2_fp_pessoa_da_interlocucao=None, p2_fp_transitividade_verbo=None, p2_fp_tonicidade=None,
        p2_fp_morfologia_do_pronome=None, p2_fp_reflexivo=None,  # classificador
        p2_fp_adjetivo_classificador=None,
        # epitetos
        p2_fp_adj_epit_exp_pre=None,
        p2_fp_adj_epit_int_pre=None,
        p2_fp_adj_epit_exp_pos=None,
        p2_fp_adj_epit_int_pos=None,
        p2_fp_genero_adjetivo=None, p2_fp_numero_adjetivo=None,
        p2_fp_contracao=None,

        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
        p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
        p3_cardinal=None, p3_genero_numerativo=None,
        p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
        p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
        p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None,
        # classificador
        p3_adjetivo_classificador=None,
        # epitetos
        p3_adj_epit_exp_pre=None,
        p3_adj_epit_int_pre=None,
        p3_adj_epit_exp_pos=None,
        p3_adj_epit_int_pos=None,
        p3_genero_adjetivo=None, p3_numero_adjetivo=None,

        p3_contracao=None,
        ##PARTICIPANTE P3 REALIZADOS POR FP
        p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
        p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
        p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
        p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
        p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
        p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
        p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
        p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
        p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
        p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
        p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
        p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
        p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
        p3_fp_tipo_feminino_ao=None,
        p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
        p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
        p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
        p3_fp_adjetivo_classificador=None,
        # epitetos
        p3_fp_adj_epit_exp_pre=None,
        p3_fp_adj_epit_int_pre=None,
        p3_fp_adj_epit_exp_pos=None,
        p3_fp_adj_epit_int_pos=None,
        p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
        p3_fp_contracao=None,

        ##participante realziado por circunstancia (relacionais circunstanciais)
        p_circ_realizacao_circunstancia=None,
        p_circ_indice_preposicao_frase=None, p_circ_dissoc_ente_nucleo=None, p_circ_tem_qualificador=None,
        p_circ_tipo_qualificador=None, p_circ_indice_preposicao_qualif=None,
        p_circ_determinacao_especificidade_beta=None, p_circ_orientacao_beta=None, p_circ_genero_beta=None,
        p_circ_numero_beta=None,
        p_circ_morfologia_do_pronome_beta=None, p_circ_determinacao_especificidade_alpha=None,
        p_circ_orientacao_alpha=None,
        p_circ_genero_alpha=None, p_circ_numero_alpha=None, p_circ_morfologia_do_pronome_alpha=None,
        p_circ_pessoa_da_interlocucao_possuidor=None, p_circ_numero_obj_possuido=None,
        p_circ_genero_obj_possuido=None,
        p_circ_pessoa_da_interlocucao_proximidade=None, p_circ_tipo_numerativo=None, p_circ_cardinal=None,
        p_circ_genero_numerativo=None,
        p_circ_tipo_de_ente=None, p_circ_tipo_de_nao_consciente=None, p_circ_tipo_de_nao_consciente_material=None,
        p_circ_tipo_de_nao_consciente_semiotico=None, p_circ_classe_palavra_ente=None,
        p_circ_substantivo_lematizado=None,
        p_circ_numero_subs=None, p_circ_genero_subs=None, p_circ_tipo_feminino_ao=None,
        p_circ_tipo_masc_ao=None, p_circ_acent_tonica=None,
        p_circ_nome_proprio=None, p_circ_pessoa_da_interlocucao=None, p_circ_transitividade_verbo=None,
        p_circ_tonicidade=None,
        p_circ_morfologia_do_pronome=None, p_circ_reflexivo=None,
        # classificador
        p_circ_adjetivo_classificador=None,
        # epitetos
        p_circ_adj_epit_exp_pre=None,
        p_circ_adj_epit_int_pre=None,
        p_circ_adj_epit_exp_pos=None,
        p_circ_adj_epit_int_pos=None,
        p_circ_genero_adjetivo=None, p_circ_numero_adjetivo=None,

        p_circ_contracao=None,
        p_circ_tipo_de_adverbio1=None, p_circ_adv_ind1=None,
        p_circ_tipo_de_adverbio2=None, p_circ_adv_ind2=None,
        p_circ_tipo_de_adverbio3=None, p_circ_adv_ind3=None,
        p_circ_tipo_de_adverbio4=None, p_circ_adv_ind4=None,
        p_circ_tipo_de_adverbio5=None, p_circ_adv_ind5=None,

        ##CIRCUNSTANCIA
        circunst_realizacao_circunstancia=None,
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
        circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
        circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
        circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
        circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
        circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None

)

# Ex.: A mulher era uma arquiteta


oracao_relacional(
    # TRANSITIVIDADE
        tipo_de_processo='Relacional',indice_material=None, indice_agenciamento=1, indice_relacional=0,
        indice_atrib=5,
        # MODO
        responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
        # TEMA INTERPESSOAL
        tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
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
        # PARÂMETROS ESPEĆIFICOS DA RELACIONAL
        # ATRIBUTIVAS
        especificacao_tipo_modo_relacao='entidade', fase_atribuicao='neutra',
        dominio_atribuicao='semiótico', tipo_de_realizacao_da_relacao=None,

        ##atributivas possessivas
        tipo_possuidor=None,

        ##processo_
        tipo_de_experiencia_gv='Ser', agencia='não_agenciado', tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Ser', funcao_no_grupo_verbal_pos_final='Evento',
        verbo_lex='ser', tipo_de_orientacao_lex='pretérito_imperfectivo',
        oi_numero_lex='singular', genero_lex=None, oi_tipo_de_pessoa_lex='3pessoa',
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
        p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino',
        p1_numero_alpha='singular',
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
        p1_cardinal=None, p1_genero_numerativo=None,
        p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
        p1_substantivo_lematizado='mulher',
        p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
        p1_acent_tonica=None,
        p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
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
        ##PARTICIPANTE P1 REALIZADOS POR FP
        ##PARTICIPANTE P1 REALIZADOS POR FP
        p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
        p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
        p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
        p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
        p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
        p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
        p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
        p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
        p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
        p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
        p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
        p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
        p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
        p1_fp_tipo_feminino_ao=None,
        p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
        p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
        p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
        p1_fp_adjetivo_classificador=None,
        # epitetos
        p1_fp_adj_epit_exp_pre=None,
        p1_fp_adj_epit_int_pre=None,
        p1_fp_adj_epit_exp_pos=None,
        p1_fp_adj_epit_int_pos=None,
        p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
        p1_fp_contracao=None,
        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='não_específico', p2_orientacao_beta='NA',
        p2_genero_beta='feminino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha='não_específico', p2_orientacao_alpha='NA', p2_genero_alpha='feminino',
        p2_numero_alpha='singular',
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
        p2_cardinal=None, p2_genero_numerativo=None,
        p2_tipo_de_ente='consciente', p2_tipo_de_nao_consciente=None,
        p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
        p2_substantivo_lematizado='arquiteta',
        p2_numero_subs='singular', p2_genero_subs='feminino', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
        p2_acent_tonica=None,
        p2_nome_proprio=None,
        p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
        p2_reflexivo=None,
        # classificador
        p2_adjetivo_classificador=None,
        # epitetos
        p2_adj_epit_exp_pre=None,
        p2_adj_epit_int_pre='grande',
        p2_adj_epit_exp_pos=None,
        p2_adj_epit_int_pos='inteligente',
        p2_genero_adjetivo='não-binário', p2_numero_adjetivo='singular',

        p2_contracao=None,
        # P2 FRASE PREP
        p2_fp_indice_preposicao_frase=None, p2_fp_dissoc_ente_nucleo=None, p2_fp_tem_qualificador=None,
        p2_fp_tipo_qualificador=None, p2_fp_indice_preposicao_qualif=None,
        p2_fp_determinacao_especificidade_beta=None, p2_fp_orientacao_beta=None, p2_fp_genero_beta=None,
        p2_fp_numero_beta=None, p2_fp_morfologia_do_pronome_beta=None,
        p2_fp_determinacao_especificidade_alpha=None, p2_fp_orientacao_alpha=None, p2_fp_genero_alpha=None,
        p2_fp_numero_alpha=None, p2_fp_morfologia_do_pronome_alpha=None,
        p2_fp_pessoa_da_interlocucao_possuidor=None, p2_fp_numero_obj_possuido=None,
        p2_fp_genero_obj_possuido=None, p2_fp_pessoa_da_interlocucao_proximidade=None,
        p2_fp_tipo_numerativo=None, p2_fp_cardinal=None,
        p2_fp_genero_numerativo=None, p2_fp_tipo_de_ente=None,
        p2_fp_tipo_de_nao_consciente=None, p2_fp_tipo_de_nao_consciente_material=None,
        p2_fp_tipo_de_nao_consciente_semiotico=None, p2_fp_classe_palavra_ente=None,
        p2_fp_substantivo_lematizado=None, p2_fp_numero_subs=None, p2_fp_genero_subs=None,
        p2_fp_tipo_feminino_ao=None,
        p2_fp_tipo_masc_ao=None, p2_fp_acent_tonica=None, p2_fp_nome_proprio=None,
        p2_fp_pessoa_da_interlocucao=None, p2_fp_transitividade_verbo=None, p2_fp_tonicidade=None,
        p2_fp_morfologia_do_pronome=None, p2_fp_reflexivo=None,  # classificador
        p2_fp_adjetivo_classificador=None,
        # epitetos
        p2_fp_adj_epit_exp_pre=None,
        p2_fp_adj_epit_int_pre=None,
        p2_fp_adj_epit_exp_pos=None,
        p2_fp_adj_epit_int_pos=None,
        p2_fp_genero_adjetivo=None, p2_fp_numero_adjetivo=None,
        p2_fp_contracao=None,

        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
        p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
        p3_cardinal=None, p3_genero_numerativo=None,
        p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
        p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
        p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None,
        # classificador
        p3_adjetivo_classificador=None,
        # epitetos
        p3_adj_epit_exp_pre=None,
        p3_adj_epit_int_pre=None,
        p3_adj_epit_exp_pos=None,
        p3_adj_epit_int_pos=None,
        p3_genero_adjetivo=None, p3_numero_adjetivo=None,

        p3_contracao=None,
        ##PARTICIPANTE P3 REALIZADOS POR FP
        p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
        p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
        p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
        p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
        p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
        p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
        p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
        p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
        p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
        p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
        p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
        p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
        p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
        p3_fp_tipo_feminino_ao=None,
        p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
        p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
        p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
        p3_fp_adjetivo_classificador=None,
        # epitetos
        p3_fp_adj_epit_exp_pre=None,
        p3_fp_adj_epit_int_pre=None,
        p3_fp_adj_epit_exp_pos=None,
        p3_fp_adj_epit_int_pos=None,
        p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
        p3_fp_contracao=None,

        ##participante realziado por circunstancia (relacionais circunstanciais)
        p_circ_realizacao_circunstancia=None,
        p_circ_indice_preposicao_frase=None, p_circ_dissoc_ente_nucleo=None, p_circ_tem_qualificador=None,
        p_circ_tipo_qualificador=None, p_circ_indice_preposicao_qualif=None,
        p_circ_determinacao_especificidade_beta=None, p_circ_orientacao_beta=None, p_circ_genero_beta=None,
        p_circ_numero_beta=None,
        p_circ_morfologia_do_pronome_beta=None, p_circ_determinacao_especificidade_alpha=None,
        p_circ_orientacao_alpha=None,
        p_circ_genero_alpha=None, p_circ_numero_alpha=None, p_circ_morfologia_do_pronome_alpha=None,
        p_circ_pessoa_da_interlocucao_possuidor=None, p_circ_numero_obj_possuido=None,
        p_circ_genero_obj_possuido=None,
        p_circ_pessoa_da_interlocucao_proximidade=None, p_circ_tipo_numerativo=None, p_circ_cardinal=None,
        p_circ_genero_numerativo=None,
        p_circ_tipo_de_ente=None, p_circ_tipo_de_nao_consciente=None, p_circ_tipo_de_nao_consciente_material=None,
        p_circ_tipo_de_nao_consciente_semiotico=None, p_circ_classe_palavra_ente=None,
        p_circ_substantivo_lematizado=None,
        p_circ_numero_subs=None, p_circ_genero_subs=None, p_circ_tipo_feminino_ao=None,
        p_circ_tipo_masc_ao=None, p_circ_acent_tonica=None,
        p_circ_nome_proprio=None, p_circ_pessoa_da_interlocucao=None, p_circ_transitividade_verbo=None,
        p_circ_tonicidade=None,
        p_circ_morfologia_do_pronome=None, p_circ_reflexivo=None,
        # classificador
        p_circ_adjetivo_classificador=None,
        # epitetos
        p_circ_adj_epit_exp_pre=None,
        p_circ_adj_epit_int_pre=None,
        p_circ_adj_epit_exp_pos=None,
        p_circ_adj_epit_int_pos=None,
        p_circ_genero_adjetivo=None, p_circ_numero_adjetivo=None,

        p_circ_contracao=None,
        p_circ_tipo_de_adverbio1=None, p_circ_adv_ind1=None,
        p_circ_tipo_de_adverbio2=None, p_circ_adv_ind2=None,
        p_circ_tipo_de_adverbio3=None, p_circ_adv_ind3=None,
        p_circ_tipo_de_adverbio4=None, p_circ_adv_ind4=None,
        p_circ_tipo_de_adverbio5=None, p_circ_adv_ind5=None,

        ##CIRCUNSTANCIA
        circunst_realizacao_circunstancia=None,
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
        circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
        circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
        circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
        circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
        circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None

)
# 'A mulher era uma grande arquiteta inteligente.'




oracao_relacional(
    # TRANSITIVIDADE
        tipo_de_processo='Relacional',indice_material=None, indice_agenciamento=2, indice_relacional=0,
        indice_atrib=5,
        # MODO
        responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
        # TEMA INTERPESSOAL
        tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
        # TEMA INTERP realizado por grupo adverbial
        t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
        t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
        t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
        t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
        t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
        #
        # 		# TEMA INTERPESSOAL realiziado por frase preposicional
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
        # PARÂMETROS ESPEĆIFICOS DA RELACIONAL
        # ATRIBUTIVAS
        especificacao_tipo_modo_relacao='entidade', fase_atribuicao='neutra',
        dominio_atribuicao='semiótico', tipo_de_realizacao_da_relacao=None,

        ##atributivas possessivas
        tipo_possuidor=None,

        ##processo_
        tipo_de_experiencia_gv='Ser', agencia='não_agenciado', tipo_de_experiencia_1=None, funcao_no_grupo_verbal_1=None,
        verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
        padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
        tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
        padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
        tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
        padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
        tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
        padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Ser', funcao_no_grupo_verbal_pos_final='Evento',
        verbo_lex='ser', tipo_de_orientacao_lex='pretérito_imperfectivo',
        oi_numero_lex='singular', genero_lex=None, oi_tipo_de_pessoa_lex='3pessoa',
        padrao_pessoa_morfologia_lex='Morfologia_padrão',
        # POLARIDADE
        tipo_polaridade=None,
        ##PARTICIPANTES
        # P1
        p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
        p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
        p1_genero_beta='feminino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
        p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='feminino',
        p1_numero_alpha='singular',
        p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
        p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
        p1_cardinal=None, p1_genero_numerativo=None,
        p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None, p1_tipo_de_nao_consciente_material=None,
        p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
        p1_substantivo_lematizado='mulher',
        p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
        p1_acent_tonica=None,
        p1_nome_proprio=None,
        p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
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

        ##PARTICIPANTE P1 REALIZADOS POR FP
        p1_fp_indice_preposicao_frase=6, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None, p1_fp_tipo_qualificador=None,
        p1_fp_indice_preposicao_qualif=None, p1_fp_determinacao_especificidade_beta='específico',
        p1_fp_orientacao_beta='NA', p1_fp_genero_beta=None, p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
        p1_fp_determinacao_especificidade_alpha='NA', p1_fp_orientacao_alpha='NA', p1_fp_genero_alpha=None,
        p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None, p1_fp_pessoa_da_interlocucao_possuidor=None,
        p1_fp_numero_obj_possuido=None, p1_fp_genero_obj_possuido=None,
        p1_fp_pessoa_da_interlocucao_proximidade=None, p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
        p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente='consciente', p1_fp_tipo_de_nao_consciente=None,
        p1_fp_tipo_de_nao_consciente_material=None, p1_fp_tipo_de_nao_consciente_semiotico=None,
        p1_fp_classe_palavra_ente='pronome_caso_reto', p1_fp_substantivo_lematizado=None, p1_fp_numero_subs='singular',
        p1_fp_genero_subs='feminino', p1_fp_tipo_feminino_ao=None, p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
        p1_fp_pessoa_da_interlocucao='ouvinte', p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None, p1_fp_morfologia_do_pronome=None,
        p1_fp_reflexivo=None,
        p1_fp_adjetivo_classificador=None,
        p1_fp_adj_epit_exp_pre=None,
        p1_fp_adj_epit_int_pre=None,
        p1_fp_adj_epit_exp_pos=None,
        p1_fp_adj_epit_int_pos=None,
        p1_fp_genero_adjetivo=None,
        p1_fp_numero_adjetivo=None,
        p1_fp_contracao=None,
        # P2
        p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
        p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta='não_específico', p2_orientacao_beta='NA',
        p2_genero_beta='feminino', p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
        p2_determinacao_especificidade_alpha='não_específico', p2_orientacao_alpha='NA', p2_genero_alpha='feminino',
        p2_numero_alpha='singular',
        p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
        p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
        p2_cardinal=None, p2_genero_numerativo=None,
        p2_tipo_de_ente='consciente', p2_tipo_de_nao_consciente=None,
        p2_tipo_de_nao_consciente_material=None,
        p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
        p2_substantivo_lematizado='arquiteta',
        p2_numero_subs='singular', p2_genero_subs='feminino', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
        p2_acent_tonica=None,
        p2_nome_proprio=None,
        p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
        p2_reflexivo=None,
        # classificador
        p2_adjetivo_classificador=None,
        # epitetos
        p2_adj_epit_exp_pre=None,
        p2_adj_epit_int_pre='grande',
        p2_adj_epit_exp_pos=None,
        p2_adj_epit_int_pos=None,
        p2_genero_adjetivo='não-binário', p2_numero_adjetivo='singular',

        p2_contracao=None,
        # P2 FRASE PREP
        p2_fp_indice_preposicao_frase=None, p2_fp_dissoc_ente_nucleo=None, p2_fp_tem_qualificador=None,
        p2_fp_tipo_qualificador=None, p2_fp_indice_preposicao_qualif=None,
        p2_fp_determinacao_especificidade_beta=None, p2_fp_orientacao_beta=None, p2_fp_genero_beta=None,
        p2_fp_numero_beta=None, p2_fp_morfologia_do_pronome_beta=None,
        p2_fp_determinacao_especificidade_alpha=None, p2_fp_orientacao_alpha=None, p2_fp_genero_alpha=None,
        p2_fp_numero_alpha=None, p2_fp_morfologia_do_pronome_alpha=None,
        p2_fp_pessoa_da_interlocucao_possuidor=None, p2_fp_numero_obj_possuido=None,
        p2_fp_genero_obj_possuido=None, p2_fp_pessoa_da_interlocucao_proximidade=None,
        p2_fp_tipo_numerativo=None, p2_fp_cardinal=None,
        p2_fp_genero_numerativo=None, p2_fp_tipo_de_ente=None,
        p2_fp_tipo_de_nao_consciente=None, p2_fp_tipo_de_nao_consciente_material=None,
        p2_fp_tipo_de_nao_consciente_semiotico=None, p2_fp_classe_palavra_ente=None,
        p2_fp_substantivo_lematizado=None, p2_fp_numero_subs=None, p2_fp_genero_subs=None,
        p2_fp_tipo_feminino_ao=None,
        p2_fp_tipo_masc_ao=None, p2_fp_acent_tonica=None, p2_fp_nome_proprio=None,
        p2_fp_pessoa_da_interlocucao=None, p2_fp_transitividade_verbo=None, p2_fp_tonicidade=None,
        p2_fp_morfologia_do_pronome=None, p2_fp_reflexivo=None,  # classificador
        p2_fp_adjetivo_classificador=None,
        # epitetos
        p2_fp_adj_epit_exp_pre=None,
        p2_fp_adj_epit_int_pre=None,
        p2_fp_adj_epit_exp_pos=None,
        p2_fp_adj_epit_int_pos=None,
        p2_fp_genero_adjetivo=None, p2_fp_numero_adjetivo=None,
        p2_fp_contracao=None,

        # P3
        p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
        p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta='específico', p3_orientacao_beta='NA',
        p3_genero_beta='feminino', p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
        p3_determinacao_especificidade_alpha='específico', p3_orientacao_alpha='NA', p3_genero_alpha='feminino',
        p3_numero_alpha='singular',
        p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
        p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
        p3_cardinal=None, p3_genero_numerativo=None,
        p3_tipo_de_ente='consciente', p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
        p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente='substantivo_comum',
        p3_substantivo_lematizado='mulher',
        p3_numero_subs='singular', p3_genero_subs='não-binário', p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None,
        p3_acent_tonica=None,
        p3_nome_proprio=None,
        p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
        p3_reflexivo=None,
        # classificador
        p3_adjetivo_classificador=None,
        # epitetos
        p3_adj_epit_exp_pre=None,
        p3_adj_epit_int_pre=None,
        p3_adj_epit_exp_pos=None,
        p3_adj_epit_int_pos=None,
        p3_genero_adjetivo=None, p3_numero_adjetivo=None,

        p3_contracao=None,
        ##PARTICIPANTE P3 REALIZADOS POR FP
        p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
        p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
        p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
        p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
        p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
        p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
        p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
        p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
        p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
        p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
        p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
        p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
        p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
        p3_fp_tipo_feminino_ao=None,
        p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
        p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
        p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
        p3_fp_adjetivo_classificador=None,
        # epitetos
        p3_fp_adj_epit_exp_pre=None,
        p3_fp_adj_epit_int_pre=None,
        p3_fp_adj_epit_exp_pos=None,
        p3_fp_adj_epit_int_pos=None,
        p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
        p3_fp_contracao=None,

        ##participante realziado por circunstancia (relacionais circunstanciais)
        p_circ_realizacao_circunstancia=None,
        p_circ_indice_preposicao_frase=None, p_circ_dissoc_ente_nucleo=None, p_circ_tem_qualificador=None,
        p_circ_tipo_qualificador=None, p_circ_indice_preposicao_qualif=None,
        p_circ_determinacao_especificidade_beta=None, p_circ_orientacao_beta=None, p_circ_genero_beta=None,
        p_circ_numero_beta=None,
        p_circ_morfologia_do_pronome_beta=None, p_circ_determinacao_especificidade_alpha=None,
        p_circ_orientacao_alpha=None,
        p_circ_genero_alpha=None, p_circ_numero_alpha=None, p_circ_morfologia_do_pronome_alpha=None,
        p_circ_pessoa_da_interlocucao_possuidor=None, p_circ_numero_obj_possuido=None,
        p_circ_genero_obj_possuido=None,
        p_circ_pessoa_da_interlocucao_proximidade=None, p_circ_tipo_numerativo=None, p_circ_cardinal=None,
        p_circ_genero_numerativo=None,
        p_circ_tipo_de_ente=None, p_circ_tipo_de_nao_consciente=None, p_circ_tipo_de_nao_consciente_material=None,
        p_circ_tipo_de_nao_consciente_semiotico=None, p_circ_classe_palavra_ente=None,
        p_circ_substantivo_lematizado=None,
        p_circ_numero_subs=None, p_circ_genero_subs=None, p_circ_tipo_feminino_ao=None,
        p_circ_tipo_masc_ao=None, p_circ_acent_tonica=None,
        p_circ_nome_proprio=None, p_circ_pessoa_da_interlocucao=None, p_circ_transitividade_verbo=None,
        p_circ_tonicidade=None,
        p_circ_morfologia_do_pronome=None, p_circ_reflexivo=None,
        # classificador
        p_circ_adjetivo_classificador=None,
        # epitetos
        p_circ_adj_epit_exp_pre=None,
        p_circ_adj_epit_int_pre=None,
        p_circ_adj_epit_exp_pos=None,
        p_circ_adj_epit_int_pos=None,
        p_circ_genero_adjetivo=None, p_circ_numero_adjetivo=None,

        p_circ_contracao=None,
        p_circ_tipo_de_adverbio1=None, p_circ_adv_ind1=None,
        p_circ_tipo_de_adverbio2=None, p_circ_adv_ind2=None,
        p_circ_tipo_de_adverbio3=None, p_circ_adv_ind3=None,
        p_circ_tipo_de_adverbio4=None, p_circ_adv_ind4=None,
        p_circ_tipo_de_adverbio5=None, p_circ_adv_ind5=None,

        ##CIRCUNSTANCIA
        circunst_realizacao_circunstancia=None,
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
        circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
        circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
        circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
        circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
        circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None

)

#A professora fez de você um ótimo arquiteto


grupo_verbal('Ser', 'não_agenciado', None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, 'Ser', 'Evento', 'ser', 'pretérito_imperfectivo', 'singular', None,
             '3pessoa', 'Morfologia_padrão')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retorna verbo conjugado')
    parser.add_argument('tipo_experiencia', type=str)
    parser.add_argument('funcao_verbo', type=str)
    parser.add_argument('lema', type=str)
    args = parser.parse_args()

    print(main(args.tipo_experiencia, args.funcao_verbo, args.lema))













