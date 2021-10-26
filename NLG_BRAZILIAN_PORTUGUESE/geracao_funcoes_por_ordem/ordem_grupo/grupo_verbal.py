import re
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.verbais import *
# grupo verbal

# print('Qual de Agência?')
# 	AGENCIA = choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não-agenciado']).ask()
#
# print('Qual o verbo auxiliar de AGÊNCIA passiva desejado?')
# 		auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()
#
# print('Qual o verbo auxiliar de AGENCIA passiva desejado?')
# 	auxiliar_da_passiva = choice.Menu(['ser', 'estar']).ask()


def realizacao_de_AGENCIA_passiva(verbo_aux, tipo_de_orientacao_aux, oi_numero_aux,
                                  genero_aux, oi_tipo_de_pessoa_aux, padrao_pessoa_morfologia_aux,
                                  tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final, verbo_lex,
                                  tipo_de_orientacao_lex, oi_numero_lex, genero_lex,
                                  oi_tipo_de_pessoa_lex, padrao_pessoa_morfologia_lex="Morfologia_padrão") -> str:
    try:
        verbo_auxiliar_passiva = formacao_da_estrutura_do_verbo_AUX(verbo_aux, tipo_de_orientacao_aux,
                                                                    oi_numero_aux,
                                                                    genero_aux, oi_tipo_de_pessoa_aux,
                                                                    padrao_pessoa_morfologia_aux)

        verbo_lexical = verbo_geral(tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final, verbo_lex,
                                    tipo_de_orientacao_lex, oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                    padrao_pessoa_morfologia_lex)

        grupo_verbal_agencia_passiva = verbo_auxiliar_passiva + ' ' + verbo_lexical
        return grupo_verbal_agencia_passiva
    except ValueError:
        return ''


def grupo_verbal(tipo_de_experiencia_gv=None, agencia=None, tipo_de_experiencia_1=None,
                 funcao_no_grupo_verbal_1=None, verbo_1=None, tipo_de_orientacao_1=None,
                 oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
                 padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None,
                 funcao_no_grupo_verbal_2=None, verbo_2=None, tipo_de_orientacao_2=None,
                 oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
                 padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None,
                 funcao_no_grupo_verbal_3=None, verbo_3=None, tipo_de_orientacao_3=None,
                 oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
                 padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None,
                 funcao_no_grupo_verbal_4=None, verbo_4=None, tipo_de_orientacao_4=None,
                 oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
                 padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex=None,
                 funcao_no_grupo_verbal_pos_final=None, verbo_lex=None,
                 tipo_de_orientacao_lex=None, oi_numero_lex=None,
                 genero_lex=None, oi_tipo_de_pessoa_lex=None,
                 padrao_pessoa_morfologia_lex='Morfologia_padrão') -> str:
    """
    Retorna o grupo verbal, com os verbos conjugados.

    Observação importante sobre o desenvolvimento da função de grupo verbal: Como os sistemas de
    FINITUDE,DEIXIS_TEMPORAL, ASPECTO na ordem do grupo são 'síndromes' de significados que reverberam
    desde o morfema, resolvi não repetir por uma questão de custo de desenvolvimento().
    A seleção de tipo de experiencia é indiferente (Fazer, Ser, Sentir), por enquanto.
    pois está relacionado, em certa medida, com o lema escolhido, mas principalmente
    com as escolhas da oração. A função prevê somente uma estrutura com 5 verbos - varios parâmetros como None.

    Ex.:

    >>> grupo_verbal('Fazer', 'agenciado_passiva', None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, 'Ser',
    'Auxiliar', 'ser', 'pretérito_perfectivo_I', 'singular', None, '3pessoa', 'Morfologia_padrão', 'Fazer',
    'Evento', 'desmatar', 'particípio', 'singular', 'masculino', None, 'Morfologia_padrão'):

    >>> 'foi desmatado'

    >>> grupo_verbal('Ser', 'agenciado_ativa', None, None, None, None, None, None,None, None, None,
    None, None, None, None, None, None,None, None, None, None, None, None, None, None, None, None,
    None,None, None, None, None,None,None, 'Ser', 'Evento', 'ser', 'presente', 'singular',None,
    '3pessoa', 'Morfologia_padrão')

    >>> 'é'

    >>> grupo_verbal(tipo_de_experiencia_gv='Fazer', agencia='agenciado_passiva', tipo_de_experiencia_1='Ser',
                 funcao_no_grupo_verbal_1='Auxiliar', verbo_1='estar', tipo_de_orientacao_1='pretérito_imperfectivo',
                 oi_numero_1='singular',  oi_tipo_de_pessoa_1='1pessoa',
                 padrao_pessoa_morfologia_1='Morfologia_padrão', tipo_de_experiencia_4='Ser',
                 funcao_no_grupo_verbal_4='Auxiliar', verbo_4='ser', tipo_de_orientacao_4='gerúndio',
                 tipo_de_experiencia_lex='Fazer',
                 funcao_no_grupo_verbal_pos_final='Evento', verbo_lex='levar',
                 tipo_de_orientacao_lex='particípio', oi_numero_lex='singular',
                 genero_lex='masculino',
                 padrao_pessoa_morfologia_lex='Morfologia_padrão'))

    >>> 'estava sendo levado'


    >>>
    :param tipo_de_experiencia_gv:
    :param agencia:
    :param tipo_de_experiencia_1:
    :param funcao_no_grupo_verbal_1:
    :param verbo_1:
    :param tipo_de_orientacao_1:
    :param oi_numero_1:
    :param genero_1:
    :param oi_tipo_de_pessoa_1:
    :param padrao_pessoa_morfologia_1:
    :param tipo_de_experiencia_2:
    :param funcao_no_grupo_verbal_2:
    :param verbo_2:
    :param tipo_de_orientacao_2:
    :param oi_numero_2:
    :param genero_2:
    :param oi_tipo_de_pessoa_2:
    :param padrao_pessoa_morfologia_2:
    :param tipo_de_experiencia_3:
    :param funcao_no_grupo_verbal_3:
    :param verbo_3:
    :param tipo_de_orientacao_3:
    :param oi_numero_3:
    :param genero_3:
    :param oi_tipo_de_pessoa_3:
    :param padrao_pessoa_morfologia_3:
    :param tipo_de_experiencia_4:
    :param funcao_no_grupo_verbal_4:
    :param verbo_4:
    :param tipo_de_orientacao_4:
    :param oi_numero_4:
    :param genero_4:
    :param oi_tipo_de_pessoa_4:
    :param padrao_pessoa_morfologia_4:
    :param tipo_de_experiencia_lex:
    :param funcao_no_grupo_verbal_pos_final:
    :param verbo_lex:
    :param tipo_de_orientacao_lex:
    :param oi_numero_lex:
    :param genero_lex:
    :param oi_tipo_de_pessoa_lex:
    :param padrao_pessoa_morfologia_lex:
    :return: grupo verbal
    """
    g_verbal = ''
    try:
        if tipo_de_experiencia_gv == 'Ser' or tipo_de_experiencia_gv == 'Fazer' or tipo_de_experiencia_gv == 'Sentir':

            if agencia == 'agenciado_ativa' or agencia == 'não_agenciado':

                verbo1 = verbo_geral(tipo_de_experiencia_1, funcao_no_grupo_verbal_1, verbo_1,
                                     tipo_de_orientacao_1, oi_numero_1, genero_1,
                                     oi_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
                verbo2 = verbo_geral(tipo_de_experiencia_2,
                                     funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2,
                                     oi_numero_2,
                                     genero_2, oi_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
                verbo3 = verbo_geral(tipo_de_experiencia_3,
                                     funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3,
                                     oi_numero_3,
                                     genero_3, oi_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)
                verbo4 = verbo_geral(tipo_de_experiencia_4,
                                     funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4,
                                     oi_numero_4,
                                     genero_4, oi_tipo_de_pessoa_4, padrao_pessoa_morfologia_4)
                evento = verbo_geral(tipo_de_experiencia_lex, funcao_no_grupo_verbal_pos_final,
                                     verbo_lex, tipo_de_orientacao_lex,
                                     oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex
                                     , padrao_pessoa_morfologia_lex)

                g_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + evento

            else:
                tipo_de_orientacao_lex = 'particípio'
                verbo_4 = 'ser'
                verbo1 = verbo_geral(tipo_de_experiencia_1,
                                     funcao_no_grupo_verbal_1,
                                     verbo_1, tipo_de_orientacao_1, oi_numero_1,
                                     genero_1, oi_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
                verbo2 = verbo_geral(tipo_de_experiencia_2,
                                     funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2,
                                     oi_numero_2,
                                     genero_2, oi_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
                verbo3 = verbo_geral(tipo_de_experiencia_3,
                                     funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3,
                                     oi_numero_3,
                                     genero_3, oi_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)

                verbos_passiva = realizacao_de_AGENCIA_passiva(verbo_4, tipo_de_orientacao_4,
                                                               oi_numero_4, genero_4, oi_tipo_de_pessoa_4,
                                                               padrao_pessoa_morfologia_4, tipo_de_experiencia_lex,
                                                               funcao_no_grupo_verbal_pos_final, verbo_lex,
                                                               tipo_de_orientacao_lex,
                                                               oi_numero_lex, genero_lex, oi_tipo_de_pessoa_lex,
                                                               padrao_pessoa_morfologia_lex)

                g_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva
        return re.sub(' +', ' ', g_verbal).strip()
    except ValueError:
        return ''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retorna experiência (radical), '
                                                 'morfema interpessoal do verbo conjugado, '
                                                 'terminação do infinitivo dado o padrão de morfologia')
    parser.add_argument('argumentos', nargs='+', type=str)
    args = parser.parse_args()
    print(grupo_verbal(*args.argumentos))
