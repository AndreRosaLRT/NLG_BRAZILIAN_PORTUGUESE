import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_adverbial import *
import argparse


if __name__ == '__main__':
    def none_ou_str_int(value):
        if value == 'None':
            return None
        elif value == 'False':
            return False
        elif value == 'True':
            return True
        try:
            return int(value)
        except:
            return value
        
    parser = argparse.ArgumentParser(description="Retorna a realização de um grupo adverbial,"
                                                 "dados os tipos e índices dos adv (alternadamente)")
    parser.add_argument('argumentos', nargs='+', type=none_ou_str_int)
    args = parser.parse_args()

    for i in range(1, len(args.argumentos), 2):
        args.argumentos[i] = int(args.argumentos[i])

    print(grupo_adverbial(*args.argumentos))


 # python3 main_grupo_adverbial.py Negação 0 Intensidade 1 'Afirmação' 2 'Tempo' 3 'Dúvida' 1
 # python3 main_grupo_adverbial.py  'Afirmação' 3
