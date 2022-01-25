import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_adverbial import *
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Retorna a realização de um grupo adverbial,"
                                                 "dados os tipos e índices dos adv (alternadamente)")
    parser.add_argument('argumentos', nargs='+')
    args = parser.parse_args()

    for i in range(1, len(args.argumentos), 2):
        args.argumentos[i] = int(args.argumentos[i])

    print(grupo_adverbial(*args.argumentos))

