import sys
sys.path.append('../')

import argparse
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_nominal import *

if __name__ == '__main__':
    def none_ou_str_int(value):
        if value == 'None':
            return None
        try:
            return int(value)
        except:
            return value


    parser = argparse.ArgumentParser()
    parser.add_argument('argumentos', nargs='+', type=none_ou_str_int)
    args = parser.parse_args()
    print(estrutura_gn(*args.argumentos))

# python3 main_grupo_nominal.py None None None None None None None None None 'específico' 'NA' 'masculino' 'singular' None '1s' 'singular' 'masculino' 'próximo_ao_falante' None None None 'não_consciente' 'material' 'objeto_material' None 'substantivo_comum' 'piano' 'singular' 'masculino' None None None None None None None None None 'importado' None 'grande' None 'bonito' 'não-binário' 'singular' None
