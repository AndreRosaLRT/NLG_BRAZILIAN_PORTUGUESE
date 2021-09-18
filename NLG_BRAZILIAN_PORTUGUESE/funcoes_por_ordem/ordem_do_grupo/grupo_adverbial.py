import NLG_BRAZILIAN_PORTUGUESE.funcoes_por_ordem.ordem_palavra.adverbios as adv

import re
import argparse


def grupo_adverbial(*args):
    advs = []
    for x in range(0, len(args), 2):
        advs.append(adv.adverbio(args[x], args[x + 1]))

    grupo_adv = re.sub(' +', ' ', (' '.join(advs)))

    return grupo_adv


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Retorna a realização de um grupo adverbial,"
                                                 "dados os tipos e índices dos adv (alternadamente)")
    parser.add_argument('argumentos', nargs='+')
    args = parser.parse_args()

    for i in range(1, len(args.argumentos), 2):
        args.argumentos[i] = int(args.argumentos[i])

    print(args.argumentos)
    print(grupo_adverbial(*args.argumentos))




