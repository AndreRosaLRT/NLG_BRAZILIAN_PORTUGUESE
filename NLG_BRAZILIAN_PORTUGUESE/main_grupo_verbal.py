import sys
sys.path.append('../')
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_grupo.grupo_verbal import *
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Retorna o grupo verbal')
    parser.add_argument('argumentos', nargs='+', type=str)
    args = parser.parse_args()
    print(grupo_verbal(*args.argumentos))

# python3 main_grupo_verbal.py 'Fazer' 'agenciado_passiva' None None None None None None None None None None None None None None None None None None None None None None None None 'Ser' 'Auxiliar' 'ser' 'pretérito_perfectivo_I' 'singular' None '3pessoa' 'Morfologia_padrão' 'Fazer' 'Evento' 'desmatar' 'particípio' 'singular' 'masculino' None 'Morfologia_padrão'




