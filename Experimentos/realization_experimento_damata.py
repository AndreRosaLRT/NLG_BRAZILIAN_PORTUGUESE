## Demonstração de realização superficial com realização dos verbos no português brasileiro.


from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *
import json

corpus = ["No dia 18 de junho de 2019, o Instituto Nacional de Pesquisas Espaciais (INPE) VP[experience=Fazer,function_in_group=Evento,lemma=divulgar,person=3,gender=none,number=Sing,mood=Ind,tense=Past,aspect=Perf] alertas de desmatamento que VP[experience=Fazer,function_in_group=Evento,lemma=somar,person=3,gender=none,number=Plur,mood=Ind,tense=Pres,aspect=none] 3.472148256306645 km² na ÁREA DE PROTEÇÃO AMBIENTAL DO TAPAJÓS/RO, VP[experience=Fazer,function_in_group=Evento,lemma=acumular,person=none,gender=none,number=none,mood=none,tense=Pres,aspect=Prog] 8 dias com alertas no mês.", "A ÁREA DE PROTEÇÃO AMBIENTAL DO TAPAJÓS VP[experience=Fazer,function_in_group=Evento,lemma=somar,person=3,gender=none,number=Sing,mood=Ind,tense=Pres,aspect=none] 8.334555363319664 km² de desmatamento no mês analisado. O desmatamento VP[experience=Ser,function_in_group=Evento,lemma=ter,person=3,gender=none,number=Sing,mood=Ind,tense=Pres,aspect=none] como principal causa a mineração."]


corpus_2 = ["No dia 31 de julho de 2019, o Instituto Nacional de Pesquisas Espaciais (INPE) VP[experience=Sentir,function_in_group=Evento,lemma=informar,person=3,gender=none,number=Sing,mood=Ind,tense=Past,aspect=Perf] que VP[experience=Ser,function_in_group=Evento,lemma=haver,person=3,gender=none,number=Sing,mood=Ind,tense=Past,aspect=Perf] alertas de desmatamento que VP[experience=Fazer,function_in_group=Evento,lemma=somar,person=3,gender=none,number=Plur,mood=Ind,tense=Pres,aspect=none] 1.315173359776571 km² no município de Alta Floresta D'oeste/RO, VP[experience=Fazer,function_in_group=Evento,lemma=acumular,person=none,gender=none,number=none,mood=none,tense=Pres,aspect=Prog] 7 dias com alertas no mês na região. Alta Floresta D'oeste VP[experience=Ser,function_in_group=Evento,lemma=ter,person=3,gender=none,number=Sing,mood=Ind,tense=Pres,aspect=none] 12.685352175179451 km² de desmatamento em julho. A principal causa dos alertas de desmatamento VP[experience=Ser,function_in_group=Evento,lemma=ser,person=3,gender=none,number=Sing,mood=Ind,tense=Past,aspect=Perf] o desmatamento com solo exposto, que VP[experience=Ser,function_in_group=Evento,lemma=deixar,person=3,gender=none,number=Sing,mood=Ind,tense=Pres,aspect=none] a terra sem vegetação."]

def realiza_superficial(lista_corpus: list):
    new_text, elements, parameters = [], [], []
    for sentenca in lista_corpus:
        tokens = sentenca.split(" ")
        for token in tokens:
            parameters = []
            if 'VP[' in token:
                elements = list(token[3:-1].split(','))
                for element in elements:
                    parameter = element.split('=')[1]
                    parameters.append(parameter)
                verb = flexionar_verbo(*parameters)
                new_text.append(verb)

            else:
                new_text.append(token)

    return" ".join(new_text)

#
# # ##EXEMPLO TESTE NO DAMATA com sinônimos:
# #
# # ##importando sinonimos
# sinonimos = json.load(open('/home/andrerosa/PROJETO_TESE/NLG_BRAZILIAN_PORTUGUESE_19-11/Experimentos/mineracao_lexicon_pre_exp_aplicacao/dic_sin_cbow.json'))
#
# TIPO_DE_EXPERIENCIA='Fazer'
# funcao_no_grupo_verbal='Evento'
# tipo_de_orientacao='pretérito_perfectivo_I'
# OI_numero='singular'
# genero=None
# OI_tipo_de_pessoa='3pessoa'
# #
# texto="Em 25 de março de 2020, o Instituto Nacional de Pesquisas Espaciais(INPE) VP[aspect=simple,tense=past,voice=active,person=3rd,number=singular] registrar alertas de desmatamento de 5.91 km2 na RESERVA EXTRATIVISTA CHICO MENDES/AC."
# texto_token = texto.split()
# lista_oracao,texto_novo, i =[], [], 0
# for token in texto_token:
#     if 'VP[' in token:
#         indice = texto_token.index(token)
#         del texto_token[indice]
#         verbo_infinitivo = texto_token[indice]
#         if verbo_infinitivo in sinonimos:
#             for sinonimo in sinonimos[verbo_infinitivo]:
#                 texto_token[indice] = verbo_geral(TIPO_DE_EXPERIENCIA, funcao_no_grupo_verbal, sinonimo,
#                                                   tipo_de_orientacao, OI_numero, genero, OI_tipo_de_pessoa)
#                 texto_novo = ' '.join(texto_token)
#                 lista_oracao.append(texto_novo)
#
# # Serializing json
# import codecs
#
# json_object = json.dumps(lista_oracao,  ensure_ascii=False,indent=4)
#
# # Writing to sample.json
# path =r'/home/andrerosa/git_workspace/NLG_BRAZILIAN_PORTUGUESE_19-11/corpus/corpora_train_dev_test'
# with codecs.open(path + "/teste_DAMATA.json", "w",encoding='utf-8' ) as outfile:
# 	json.dump(json_object,outfile, ensure_ascii=False)
# 	outfile.write(json_object)
#


if __name__ == '__main__':
    print(realiza_superficial(corpus))

    print(realiza_superficial(corpus_2))
