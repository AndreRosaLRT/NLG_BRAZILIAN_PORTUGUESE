#RODA EXPERIMENTO NOS CORPORA DE DEV E TEST DO SIGMORPHON

from Experimentos.experimento_dev_test import *


if __name__ == '__main__':

    experimento('https://raw.githubusercontent.com/sigmorphon/conll2017/master/all/task1/portuguese-dev',
                'acertos_conjugação_dev.json', 'erros_conjugação_dev.json')
    experimento('https://raw.githubusercontent.com/sigmorphon/conll2017/master/answers/task1/portuguese-uncovered-test',
                'acertos_conjugação_TESTE.json', 'erros_conjugação_TESTE.json')