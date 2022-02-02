import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_conjuntivo import *
import argparse


if __name__ == '__main__':
    def none_ou_str_int(value):
        if value == 'None':
            return None
        try:
            return int(value)
        except:
            return value

    parser = argparse.ArgumentParser(description=" Retorna um grupo conjuntivo dado o tipo de inserção,"
                                                 " a conjunção por extenso(caso a escolha seja manual), "
                                                 "o tipo de conjunção e o índice (caso a escolha de tipo de "
                                                 "inserção seja manual)")

    parser.add_argument('tipo_de_conjuncao', type=none_ou_str_int, choices=['paratática_aditiva', 'paratática_adversativa',
                                                                        'paratática_alternativa',
                                                                        'paratática_conclusiva',
                                                                        'paratática_explicativa', 'hipotática_causal',
                                                                        'hipotática_concessiva',
                                                                        'hipotática_condicional',
                                                                        'hipotática_conformativa', 'hipotátiva_final',
                                                                        'hipotática_proporcional',
                                                                        'hipotática_temporal',
                                                                        'hipotática_comparativa',
                                                                        'hipotática_consecutiva',
                                                                        'hipotática_integrante', 'hipotática_relativa'])
    parser.add_argument('indice', type=int)
    args = parser.parse_args()

    print(grupo_conjuntivo(args.tipo_de_conjuncao, args.indice))
    # python3 main_grupo_conjuntivo.py paratática_aditiva 3 - > nem