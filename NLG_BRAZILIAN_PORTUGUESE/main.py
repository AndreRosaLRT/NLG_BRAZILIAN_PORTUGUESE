from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.frase_preposicional import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_verbal import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_adverbial import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_conjuntivo import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_oracao.oracao import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_nominal import *
import json
# Exemplos de uso das funções
# ordem do morfema
# experiencia do verbo
lemas_verbos = ['desmatar', 'registrar', 'detectar', 'identificar', 'atingir', 'contabilizar', 'somar', 'totalizar',
          'alcançar', 'chegar', 'reportar', 'observar', 'ser', 'representar', 'acontecer', 'ocorrer', 'existir',
          'ter', 'apresentar', 'possuir', 'estar', 'acumular', 'relatar', 'sofrer']
for verb in lemas_verbos:
    print(experiencia_do_verbo(verb))
# desmat
# registr
# detect
# identific
# ating
# contabiliz
# som
# totaliz
# alcanç
# cheg
# report
# observ
# s
# represent
# acontec
# ocorr
# exist
# t
# apresent
# possu
# est
# acumul
# relat
# sofr
#Detecção terminação verbo infinitivo
for verb in lemas_verbos:
    print(deteccao_transitoriedade_do_verbo(verb))
# ar
# ar
# ar
# ar
# ir
# ar
# ar
# ar
# ar
# ar
# ar
# ar
# er
# ar
# er
# er
# ir
# er
# ar
# ir
# ar
# ar
# ar
# er

# Detecção de padrão de morfologia
for verb in lemas_verbos:
    print(detecta_padrao_morfologia(verb))
# AR
# AR
# AR
# AR
# IR
# AR
# AR
# AR
# AR
# AR
# AR
# AR
# ER
# AR
# ER
# ER
# IR
# ER
# AR
# IR
# AR
# AR
# AR
# ER


# Os morfemas interpessoas serão testados diretamente na palavra verbal_verbo
# ORDEM DA PALAVRA
# VERBOS: os algoritmo a seguir retorna um dicionário com todas as opções de Orientação Interpessoal de cada
# um dos verbos na lista lema_verbos.
#
####
#

OI_numeros = ['singular', "plural"]
OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
OI_INTERPESSOAIS = [ 'presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II',
                    'pretérito_imperfectivo', 'pretérito_imperfectivo', 'passado_volitivo', 'futuro',
                    'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
                    'não_finito_concretizado','imperativo_I', 'imperativo_II']
generos=['masculino','feminino']
conjugacao = []

dicionarioConjuga={}

for lema in lemas_verbos:
    dicionarioConjuga.update({lema: {}})
    for oi in OI_INTERPESSOAIS:
        conjugacao = []
        for numero in OI_numeros:
            for tipo_pessoa in OI_tipo_pessoas:
                verbo = verbo_geral("Fazer", 'Evento', lema, oi, numero, None, tipo_pessoa)
                conjugacao.append(verbo)
                dicionarioConjuga[lema].update({oi:conjugacao})
# print(dicionarioConjuga)

# Função que  retorna a classe do verbo, dada a função do verbo no grupo verbal
funcao_no_grupo_verbal = ['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo','Auxiliar+Núcleo', 'Modal+Núcleo']
for elem in funcao_no_grupo_verbal:
    print(def_classe_de_verbo(elem))

# PREPOSIÇÕES: a linha a seguir printa todas as opções disponíveis no módulo para as preposições
[print(preposicao(i)) for i in range (17)]



# CIRCUNSTANCIA:
for i in range (26):
    print(circunstancia(realizacao_circunstancia='grupo_adverbial',
                  indice_preposicao_frase=None, dissoc_ente_nucleo=None, tem_qualificador=None,
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
                  nome_prop_fp=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                  morfologia_do_pronome=None, reflexivo=None,
                  # classificador
                  adjetivo_classificador=None,
                  # epitetos
                  adj_epit_exp_pre=None,
                  adj_epit_int_pre=None,
                  adj_epit_exp_pos=None,
                  adj_epit_int_pos=None,
                  genero_adjetivo=None, numero_adjetivo=None,

                  contracao=None,
                  tipo_de_adverbio1='Tempo', adv_ind1=i))

for i in range(16):
    print(circunstancia(realizacao_circunstancia='frase_preposicional', indice_preposicao_frase=i,
                        dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
                        indice_preposicao_qualif=None, determinacao_especificidade_beta='específico',
                        orientacao_beta='NA', genero_beta='masculino', numero_beta=None,
                        morfologia_do_pronome_beta=None,
                        determinacao_especificidade_alpha='específico', orientacao_alpha='NA', genero_alpha='feminino',
                        numero_alpha='singular', morfologia_do_pronome_alpha=None,
                        pessoa_da_interlocucao_possuidor='1s',
                        numero_obj_possuido='singular', genero_obj_possuido='masculino',
                        pessoa_da_interlocucao_proximidade=None, tipo_numerativo='ordinal', cardinal=2,
                        genero_numerativo='feminino', tipo_de_ente='não_consciente', tipo_de_nao_consciente='semiótico',
                        tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico='objeto_semiótico',
                        classe_palavra_ente='substantivo_comum', substantivo_lematizado='guerra',
                        numero_subs='singular',
                        genero_subs='feminino', tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
                        nome_prop_fp=None,
                        pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                        morfologia_do_pronome=None,
                        reflexivo=None,
                        adjetivo_classificador='mundial',
                        adj_epit_exp_pre=None,
                        adj_epit_int_pre=None,
                        adj_epit_exp_pos=None,
                        adj_epit_int_pos=None,
                        genero_adjetivo='não-binário',
                        numero_adjetivo='singular',
                        contracao=None))

# -> à segunda guerra mundial
# ante a segunda guerra mundial
# após a segunda guerra mundial
# até a segunda guerra mundial
# com a segunda guerra mundial
# contra a segunda guerra mundial
# da segunda guerra mundial
# desde a segunda guerra mundial
# na segunda guerra mundial
# entre a segunda guerra mundial
# para a segunda guerra mundial
# pela segunda guerra mundial
# perante a segunda guerra mundial
# sem a segunda guerra mundial
# sob a segunda guerra mundial
# sobre a segunda guerra mundial


# testes oracao:

#verbal


# O homem acusou o padeiro
oracao_verbal('Verbal', None, 2, None, 0, 0, 1, 'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA',
              None, None, None, 'atividade_alvo', None, None, None, 'Sentir', 'não_agenciado', None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, 'Sentir', 'Evento', 'acusar',
              'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'positiva', None, None, None,
              None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None, None, None,
              None, None, None, 'não-binário', None, None, None, None, None, None, None, 'não_consciente', 'material',
              'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              'específico', 'NA', 'masculino', 'singular', None, None, None, None, None, None, None, 'masculino', None,
              None, None, None, None, None, None, 'não_consciente', 'material', 'abstração_material', None,
              'substantivo_comum', 'padeiro', 'singular', None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)

oracao_verbal('Verbal', None, 0, None, 0, 0, 1, 'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA',
              None, None, None, 'semioticidade', 'não_projeção_-verbiagem', None, None, 'Sentir', 'não_agenciado', None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'Sentir', 'Evento',
              'falar', 'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'positiva', None,
              None, None, None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None,
              None, None, None, None, None, 'não-binário', None, None, None, None, None, None, None, 'não_consciente',
              'material', 'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None)

oracao_verbal('Verbal', None, 0, None, 0, 0, 1, 'orientado', 'direcional', 'default', 'indicativo', 'declarativo', 'NA',
              None, None, None, 'atividade_fala', None, None, None, 'Sentir', 'não_agenciado', None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, 'Sentir', 'Evento', 'falar',
              'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'positiva', None, None, None,
              None, None, None, None, None, None, 'específico', 'NA', 'masculino', 'singular', None, None, None, None,
              None, None, None, 'não-binário', None, None, None, None, None, None, None, 'não_consciente', 'material',
              'abstração_material', None, 'substantivo_comum', 'homem', 'singular', None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
              None)
