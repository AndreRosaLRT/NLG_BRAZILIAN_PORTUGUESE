import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *
import argparse


def main(tipo_de_experiencia, funcao_no_grupo_verbal, lema):
    """
    Retorna a conjugação em todas as opções e Orientação Interpessoal.
    :param tipo_de_experiencia:
    :param funcao_no_grupo_verbal:
    :param lema:
    :return:
    """
    dicionario_conjuga = {}
    participios = []
    ois = ['presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
           'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
           'não_finito_concretizado', 'imperativo_I', 'imperativo_II']
    oi_numeros = ['singular', "plural"]
    oi_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
    generos = ['masculino', 'feminino']

    # TESTE GERAL:
    try:

        dicionario_conjuga.update({lema: {}})
        for oi in ois:
            conjugacao = []
            for num in oi_numeros:
                for pessoa in oi_tipo_pessoas:
                    verbo = verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, lema, oi, num, None, pessoa)
                    conjugacao.append(verbo)
                    dicionario_conjuga[lema].update({oi: conjugacao})
        dicionario_conjuga[lema].update({'gerúndio': verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, lema,
                                                                 'gerúndio', None, None, None)})

        for numero in oi_numeros:
            for genero in generos:
                participios.append(verbo_geral(tipo_de_experiencia, funcao_no_grupo_verbal, lema, 'particípio',
                                               numero, genero, None))
        dicionario_conjuga[lema].update({'participio': participios})
        return dicionario_conjuga
    except ValueError:
        return ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Retorna verbo conjugado')
    parser.add_argument('tipo_experiencia', type=str)
    parser.add_argument('funcao_verbo', type=str)
    parser.add_argument('lema', type=str)
    args = parser.parse_args()

    print(main(args.tipo_experiencia, args.funcao_verbo, args.lema))


# python3 main_pal_verbais.py Fazer Evento levar
# python3 main_pal_verbais.py Fazer Evento comer
# python3 main_pal_verbais.py Fazer Evento desmatar