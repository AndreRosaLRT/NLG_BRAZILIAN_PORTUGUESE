import sys
sys.path.append('../')

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_oracao.oracao import *
import argparse

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

    print(oracao_mental(*args.argumentos))


# Ex no terminal
# python3 main_oracao_mental.py 'Mental' None 0 None 0 0 1 'TI_NA' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None False None None None None None None None None None 'orientado' 'direcional' 'default' 'indicativo' 'declarativo' 'NA' None None None 'não-fenomenalização_comportamento-passivo' 'inferior_perceptivo' 'Sentir' 'agenciado_ativa' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Sentir' 'Evento' 'ouvir' 'pretérito_perfectivo_I' 'singular' None '1pessoa' 'Morfologia_padrão' 'positiva' None None None None None None None None None None None None None None None None None None None None None "consciente" None None None 'pronome_caso_reto' None "singular" None None None None None "falante" None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'grupo_adverbial' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Modo' 10 None None None None None None None None
# Eu ouvi

# python3 main_oracao_mental.py 'Mental' None 0 None 0 0 1 'TI_NA' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None False None None None None None None None None None 'orientado' 'direcional' 'default' 'indicativo' 'declarativo' 'NA' None None None 'não-fenomenalização_comportamento-passivo' 'inferior_perceptivo' 'Sentir' 'agenciado_ativa' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Sentir' 'Evento' 'ouvir' 'pretérito_perfectivo_I' 'singular' None '1pessoa' 'Morfologia_padrão' 'positiva' None None None None None None None None None None None None None None None None None None None None None "consciente" None None None 'pronome_caso_reto' None "singular" None None None None None "falante" None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'grupo_adverbial' None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None None 'Modo' 10 None None None None None None None None








