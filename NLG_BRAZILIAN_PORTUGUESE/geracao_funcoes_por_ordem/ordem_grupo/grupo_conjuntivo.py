import argparse


def grupo_conjuntivo(tipo_de_conjuncao=None, indice=None):
    """
    Retorna um grupo conjuntivo dado o tipo de inserção, a conjunção por extenso
    (caso a escolha seja manual), o tipo de conjunção e o índice (caso a escolha de tipo de
    inserção seja manual)

    Exs.:

    >>> grupo_conjuntivo('paratática_adversativa',1)

    >>> 'entretanto'

    >>> grupo_conjuntivo (tipo_de_conjuncao='hipotática_concessiva', indice=7) -> 'apesar de que'

    :param indice:
    :param tipo_de_conjuncao:'paratática_aditiva': {0: 'e', 1: 'mas ainda', 2: 'mas também', 3: 'nem'},
    'paratática_adversativa':{0: 'contudo', 1: 'entretanto', 2: 'mas', 3: 'não obstante',4: 'no entanto',
    5: 'porém', 6: 'todavia'},
    'paratática_alternativa': {0: 'já', 1: 'ou', 2: 'ora', 3: 'quer'},
    'paratática_conclusiva':{0: 'assim', 1: 'então', 2: 'logo', 3: 'por conseguinte', 4: 'por isso', 5: 'portanto'},
    'paratática_explicativa':{0: 'pois', 1: 'porquanto', 2: 'porque', 3: 'que'},
    'hipotática_causal':{0: 'porque', 1: 'pois', 2: 'porquanto', 3: 'como', 4: 'pois que', 5: 'por isso que',
    6: 'á que', 7: 'uma vez que', 8: 'visto que', 9: 'visto como', 10: 'que'},
    'hipotática_concessiva':{0: 'embora', 1: 'conquanto', 2: 'ainda que', 3: 'mesmo que', 4: 'posto que',
    5: 'bem que', 6: 'se bem que', 7: 'apesar de que', 8: 'nem que', 9: 'que'},
    'hipotática_condicional':{0: 'se', 1: 'caso', 2: 'quando', 3: 'conquanto que',  4: 'salvo se', 5: 'sem que',
    6: 'dado que', 7: 'desde que',8: 'a menos que', 9: 'a não ser que'},
    'hipotática_conformativa':{0: 'conforme', 1: 'como', 2: 'segundo', 3: 'consoante'},
    'hipotátiva_final':{0: 'para que', 1: 'a fim de que', 2: 'porque', 3: 'que'},
    'hipotática_proporcional':{0: 'à medida que', 1: 'ao passo que', 2: 'à proporção que', 3: 'enquanto',
    4: 'quanto mais', 5: 'quanto menos'},
    'hipotática_temporal':{0: 'quando', 1: 'antes que', 2: 'depois que', 3: 'até que', 4: 'logo que',
    5: 'sempre que', 6: 'assim que', 7: 'desde que', 8: 'todas as vezes que', 9: 'cada vez que', 10: 'apenas',
    11: 'mal', 12: 'desde que'},
    'hipotática_comparativa':{0: 'mais que', 1: 'mais do que', 2: 'menos que', 3: 'maior que', 4: 'menor que',
    5: 'melhor que', 6: 'pior que', 7: 'menos do que', 8: 'maior do que', 9: 'menor do que',
    10: 'melhor do que', 11: 'pior do que'},
    'hipotática_consecutiva':{0: 'De modo que', 1: 'De maneira que'},
    'hipotática_integrante':{0: 'que', 1: 'se'},
    'hipotática_relativa':{0: 'porque', 1: 'pois', 2: 'porquanto', 3: 'como', 4: 'pois que', 5: 'por isso que',
    6: 'á que', 7: 'uma vez que', 8: 'visto que', 9: 'visto como', 10: 'que'}
    :return: grupo conjuntivo
    """
    conjuncao = ''
    indice = int(indice)
    try:

        if tipo_de_conjuncao == 'paratática_aditiva':
            opcoes = ['e', 'mas ainda', 'mas também', 'nem']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'paratática_adversativa':
            opcoes = ['contudo', 'entretanto', 'mas',
                      'não obstante', 'no entanto',
                      'porém', 'todavia']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'paratática_alternativa':
            # PRECISO VER COMO IMPLEMENTAR UM COMPLEXO COM ESTE TIPO
            opcoes = ['já', 'ou', 'ora', 'quer']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'paratática_conclusiva':
            opcoes = ['assim', 'então', 'logo',
                      'por conseguinte', 'por isso',
                      'portanto']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'paratática_explicativa':
            opcoes = ['pois', 'porquanto', 'porque', 'que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_causal':
            opcoes = ['porque', 'pois', 'porquanto',
                      'como', 'pois que', 'por isso que',
                      'á que', 'uma vez que', 'visto que',
                      'visto como', 'que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_concessiva':
            opcoes = ['embora', 'conquanto', 'ainda que',
                      'mesmo que', 'posto que', 'bem que',
                      'se bem que', 'apesar de que', 'nem que',
                      'que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_condicional':
            opcoes = ['se', 'caso', 'quando',
                      'conquanto que', 'salvo se', 'sem que',
                      'dado que', 'desde que', 'a menos que',
                      'a não ser que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_conformativa':
            opcoes = ['conforme', 'como', 'segundo', 'consoante']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_final':
            opcoes = ['para que',
                      'a fim de que', 'porque',
                      'que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_proporcional':
            opcoes = ['à medida que', 'ao passo que', 'à proporção que',
                      'enquanto', 'quanto mais',
                      'quanto menos']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_temporal':
            opcoes = ['quando', 'antes que',
                      'depois que', 'até que', 'logo que',
                      'sempre que', 'assim que', 'desde que',
                      'todas as vezes que', 'cada vez que', 'apenas',
                      'mal', 'desde que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_comparativa':
            opcoes = ['mais que', 'mais do que',
                      'menos que', 'maior que', 'menor que',
                      'melhor que', 'pior que',
                      'menos do que', 'maior do que',
                      'menor do que', 'melhor do que',
                      'pior do que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_consecutiva':
            opcoes = ['De modo que', 'De maneira que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_integrante':
            opcoes = ['que', 'se']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        elif tipo_de_conjuncao == 'hipotática_relativa':
            opcoes = ['porque', 'pois', 'porquanto',
                      'como', 'pois que', 'por isso que',
                      'á que', 'uma vez que', 'visto que',
                      'visto como', 'que']
            nums = [x for x in range(len(opcoes))]
            conjuncoes = dict(zip(nums, opcoes))
            conjuncao = conjuncoes[indice]

        return conjuncao
    except:
        return ''


if __name__ == '__main__':
    def none_ou_str(value):
        if value == 'None':
            return None
        return value

    parser = argparse.ArgumentParser(description=" Retorna um grupo conjuntivo dado o tipo de inserção,"
                                                 " a conjunção por extenso(caso a escolha seja manual), "
                                                 "o tipo de conjunção e o índice (caso a escolha de tipo de "
                                                 "inserção seja manual)")

    parser.add_argument('tipo_insercao', type=none_ou_str, choices=['inserção_manual', 'inserção_menu'],
                        default='inserção_menu')
    parser.add_argument('conj_extenso', type=none_ou_str)
    parser.add_argument('tipo_de_conjuncao', type=none_ou_str, choices=['paratática_aditiva', 'paratática_adversativa',
                                                                        'paratática_alternativa',
                                                                        'paratática_conclusiva',
                                                                        'paratática_explicativa', 'hipotática_causal',
                                                                        'hipotática_concessiva',
                                                                        'hipotática_condicional',
                                                                        'hipotática_conformativa', 'hipotátiva_final',
                                                                        'hipotática_proporcional',
                                                                        'hipotática_temporal',
                                                                        'hipotática_comparativa',
                                                                        'hipotática_consecutiva',
                                                                        'hipotática_integrante', 'hipotática_relativa'])
    parser.add_argument('indice', type=int)
    args = parser.parse_args()

    print(grupo_conjuntivo(args.tipo_insercao, args.conj_extenso, args.tipo_de_conjuncao, args.indice))

