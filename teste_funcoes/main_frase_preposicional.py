import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_nominal_frase_preposicional import *
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

    parser = argparse.ArgumentParser(description="Retorna uma frase preposicional dados um índice e os "
                                                 "argumentos referentes ao grupo nominal encaixado")

    parser.add_argument('argumentos', nargs='+', type=none_ou_str_int)
    args = parser.parse_args()

    print(frase_preposicional(*args.argumentos))
    

#
# python3 main_frase_preposicional.py 11 None None None None None None None None None 'específico' 'NA' 'masculino' 'singular' None None None None None None None None 'consciente' None None None 'substantivo_comum' 'homem' 'singular' 'não-binário' None None None None None None None None None None None None None None None None None



