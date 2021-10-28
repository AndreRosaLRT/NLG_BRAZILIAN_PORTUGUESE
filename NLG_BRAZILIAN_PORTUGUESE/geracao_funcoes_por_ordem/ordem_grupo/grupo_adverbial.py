from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_adverbiais import *
import re
import argparse


def grupo_adverbial(*argums):
    advs = []
    for x in range(0, len(argums), 2):
        advs.append(adverbio(argums[x], argums[x + 1]))

    grupo_adv = re.sub(' +', ' ', (' '.join(advs)))

    return grupo_adv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Retorna a realização de um grupo adverbial,"
                                                 "dados os tipos e índices dos adv (alternadamente)")
    parser.add_argument('argumentos', nargs='+')
    args = parser.parse_args()

    for i in range(1, len(args.argumentos), 2):
        args.argumentos[i] = int(args.argumentos[i])

    print(grupo_adverbial(*args.argumentos))




