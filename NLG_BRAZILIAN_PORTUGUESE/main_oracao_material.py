import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_oracao.oracao import *
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

    parser = argparse.ArgumentParser()
    parser.add_argument('argumentos', nargs='+', type=none_ou_str_int)
    args = parser.parse_args()

    print(oracao_material(*args.argumentos))



# python3 main_oracao_material.py 'Material' 1 3 None None 0 0 1 None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None False None None None None None None None None None 'não_orientado' 'não_direcional' 'proeminente' None None 'NA' None None 'intensivo_relativo_papel_transitivo_nuclear_participante' None None None None None None 6 None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Fazer' 'agenciado_passiva' None None None None None None None None None None None None None None None None None None None None None None None None 'Ser' 'Auxiliar' 'ser' 'pretérito_perfectivo_I' 'singular' None '3pessoa' 'Morfologia_padrão' 'Fazer' 'Evento' 'fazer' 'particípio' 'singular' 'masculino' '3pessoa' 'Morfologia_padrão' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 11 None None None None None None None None None 'específico' 'NA' 'masculino' 'singular' None None None None None None None None 'consciente' None None None 'substantivo_comum' 'homem' 'singular' 'não-binário' None None None None None None None None None None None None None None None None None None None None None None None None None None 'específico' 'NA' 'masculino' 'singular' None None None None None None None None 'não_consciente' 'material' 'objeto_material' None 'substantivo_comum' 'bolo' 'singular' 'não-binário' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None



























































