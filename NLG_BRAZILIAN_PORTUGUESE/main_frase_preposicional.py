import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.frase_preposicional import *
import argparse


if __name__ == '__main__':
    def none_ou_str(value):
        if value == 'None':
            return None
        return value

    parser = argparse.ArgumentParser(description="Retorna uma frase preposicional dados um índice e os "
                                                 "argumentos referentes ao grupo nominal encaixado")

    parser.add_argument('argumentos', nargs='+', type=none_ou_str)
    args = parser.parse_args()

    print(frase_preposicional(*args.argumentos))
    


