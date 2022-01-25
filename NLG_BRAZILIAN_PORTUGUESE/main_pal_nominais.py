import sys
sys.path.append("../")

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_nominais import *
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Retorna pronomes no caso reto')
    parser.add_argument('pessoa_da_interlocucao', type=str)
    parser.add_argument('genero', type=str)
    parser.add_argument('numero', type=str)
    parser.add_argument('morfologia_do_pronome', type=str)
    args = parser.parse_args()

    print(realizacao_pronominal_casoreto(args.pessoa_da_interlocucao,
                                         args.genero, args.numero, args.morfologia_do_pronome))

