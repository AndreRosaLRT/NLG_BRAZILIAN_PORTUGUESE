# -*- coding: utf-8 -*-

import os

from scipy.stats.mstats_basic import sen_seasonal_slopes

path=os.getcwd()
import json

from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *
# WORDNET
#WORDNET
#preparando o ambiente
#download do wordnet no ambiente
# nltk.download('wordnet')
# nltk.download('omw')
#importa wordnet
# from nltk.corpus import wordnet as wn
# wn.langs()

##########WORDEMBEDDINGS
#PARA REALIZAR AS ETAPAS SEGUINTES, É NECESSÁRIO BAIXAR OS MODELOS NOVAMENTE.
#http://nilc.icmc.usp.br/nilc/index.php/repositorio-de-word-embeddings-do-nilc
# import gensim
# print('done')
# from gensim import models
# from gensim.models import KeyedVectors
# print('done')

# model_cbow = KeyedVectors.load_word2vec_format('./mineração_lexicon/cbow_s50.txt', encoding="utf-8")
# print('Done')
# model_skip = KeyedVectors.load_word2vec_format('./mineração_lexicon/skip_s300.txt')
# print('Done')
# palavras_cbow = list(model_cbow.wv.vocab)
# palavras_skip = list(model_skip.wv.vocab)

####
# Carrega OS VERBOS DE INTERESSE(COM BASE NAS VERBALIZAÇÕES DO ROBÔ):
arquivo = json.load(open('./mineração_lexicon/verbs.json'))
#
# type(arquivo)
chaves = arquivo.keys() #compila as chaves do arquivo
# type(chaves)
chaves = list(chaves) #transforma a variável 'chaves' em lista

lemas_verbos = [] #lista vazia para compilar os lemas verbais da lista de chaves
i = 0
for entrada in chaves: # loop para coleção dos lemas verbais
    verbo = chaves[i].split()[1]
    if verbo not in lemas_verbos:
        lemas_verbos.append(verbo)
    i += 1



##############################################

##dicionario co base no cbow
dict_sinon_cbow = {}

for palavra in lemas_verbos:  #loop para checagem de sinonímia dos lemas verbais em comparação com o modelo cbow
    sinonimos = []
    if palavra in model_cbow.vocab: #se o lema for encontrado no dicionário cbow,
        dict_sinon_cbow.update({palavra: sinonimos})  #o dicionário de sinônimos é atualizado
    i=0
    for entrada in model_cbow.most_similar(palavra):

        sinonimos.append(model_cbow.most_similar(palavra)[i][0]) #cria lista de 10 'sinônimos', ou 'palavras similares' ao
                                                                    #lema de interesse
        i+=1
    i+=1

#Cria um jason com o dicionário de lemas de interesse e sinônimos
# # Serializing json
# json_object = json.dumps(dict_sinon_cbow, indent=4)
#
# # Writing to sample.json
# with open("./mineração_lexicon/dic_sin_cbow2.json", "w", encoding="utf-8") as outfile:
#     outfile.write(json_object)
#
# dict_sinon_cbow.items()
####O disionário de sinônimos já foi criado. Tendo o dicionário já salvo, é só carregar:
dicionario_cbow = json.load(open('./mineração_lexicon/dic_sin_cbow2.json'))


##PRE-EXPERIMENTOS APLICAÇÃO

####TOdOS OS VERBOS:

# #
# # # ##TESTE VERBOS


OI_numeros = ['singular', "plural"]
OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
OI_INTERPESSOAIS = [ 'presente', 'pretérito_perfectivo_I', 'pretérito_perfectivo_II',
                    'pretérito_imperfectivo', 'pretérito_imperfectivo', 'passado_volitivo', 'futuro',
                    'subjuntivo_conjuntivo', 'subjuntivo_condicional', 'subjuntivo_optativo',
                    'não_finito_concretizado','imperativo_I', 'imperativo_II']
generos=['masculino','feminino']
conjugacao = []
#
# for oi in OI_INTERPESSOAIS:
#     for numero in OI_numeros:
#         for tipo_pessoa in OI_tipo_pessoas:
#             try:
#                 verbo = verbo_geral("Fazer", 'Evento', 'identificar', oi, numero, None, tipo_pessoa)
#                 conjugacao.append(verbo)
#             except:
#                 conjugacao.append('ERROR_'+oi+'_'+tipo_pessoa)


dicionarioConjuga={} # dicionário para atualização dos verbos conjugados, com base na lista de lemas, para todos
                        #as Orientações Interpessoais (exceto gerúndio, particípio)

for lema in lemas_verbos: #loop nos lemas
    dicionarioConjuga.update({lema: {}}) #atualiza o dicionário
    for oi in OI_INTERPESSOAIS: #loop nos tipos de orientação interpessoal
        conjugacao = [] #lista de conjugações
        for numero in OI_numeros: #loop nos números
            for tipo_pessoa in OI_tipo_pessoas:#loop nas pessoas
                verbo = verbo_geral("Fazer", 'Evento', lema, oi, numero, None, tipo_pessoa) #função de conjugação com base nos parâmetros
                conjugacao.append(verbo) #append da conjugação
                dicionarioConjuga[lema].update({oi:conjugacao}) #atualiza o dicionário de conjugações


json_object=json.dumps(dicionarioConjuga, ensure_ascii=False) #cria um objto json com o dump do dicionário
# Writing to sample.json
with open('./mineração_lexicon/dicionarioVerbosDaMata.json', "w",) as outfile:
    outfile.write(json_object) #salva o dicionário de conjugações em arquivo json

####GERUNDIO (o algoritmo segue a lógica do algoritmo anterior)

dicionarioConjugaGerundio={}

for lema in lemas_verbos:
    verbo = verbo_geral("Fazer", 'Evento', lema, 'gerúndio', None, None, None)
    dicionarioConjugaGerundio.update({lema: verbo})

json_object=json.dumps(dicionarioConjugaGerundio, ensure_ascii=False)
# Writing to sample.json
with open('./mineração_lexicon/dicionarioVerbosDaMataGerundio.json', "w",) as outfile:
    outfile.write(json_object)

####PARTICÍPIO (o algoritmo segue a lógica do algoritmo anterior)

dicionarioConjugaParticipio={}

for lema in lemas_verbos:
    listaConjugados = []
    for numero in OI_numeros:
        for genero in generos:
            verbo = verbo_geral("Fazer", 'Evento', lema, 'particípio',numero, genero, None)
            listaConjugados.append(verbo)
    dicionarioConjugaParticipio.update({lema: listaConjugados})

json_object=json.dumps(dicionarioConjugaParticipio, ensure_ascii=False)
# Writing to sample.json
with open('./mineração_lexicon/dicionarioVerbosDaMataParticipio.json', "w") as outfile:
    outfile.write(json_object)


# Algoritmo pra realização de sentença com sinônimos de lemas de interesse (pré-teste da função de realização do verbo nas sentenças do robô jornalista)
listaSentencas = [] #cria lista vazia de sentenças

for lema in dicionario_cbow['registrar']: #loop pelo dicionário de sinônimos, lema 'registrar'
    verbo = verbo_geral("Fazer", 'Evento', dicionario_cbow['registrar'][lema], 'pretérito_perfectivo_I',
                        'singular', None, '3pessoa') #realização do verbo
    sentenca = "Em 25 de março de 2020, o Instituto Nacional de Pesquisas Espaciais(INPE) " \
               + verbo + " alertas de desmatamento de 5.91 km2 na RESERVA EXTRATIVISTA CHICO MENDES/AC."
    listaSentencas.append(sentenca) #append de sentenças com o verbo sinônimo conjugado
senten_object= json.dumps(listaSentencas, ensure_ascii=False)
with open ('/home/andrerosa/PROJETO_TESE/NLG_BRAZILIAN_PORTUGUESE_19-11/mineração_lexicon/listaSentencas.json', 'w') as outfile:
    outfile.write(senten_object) #salva lista de sentenças em arquivo json

###DICIONARIOS QUE ACABEI NÃO USANDO NO EXPERIMENTO:
# ###dicionario co base no skipgram
# dict_sinon_skip = {}
#
# for palavra in lemas_verbos:
#     sinonimos = []
#     if palavra in model_skip.vocab:
#         dict_sinon_skip.update({palavra: sinonimos})
#     i=0
#     for entrada in model_skip.most_similar(palavra):
#         sinonimos.append(model_skip.most_similar(palavra)[i][0])
#         i+=1
#     i+=1
#
# model_skip.sinonym("registrar")
# model_skip.most_similar("registrar")[0][1]
# # Serializing json
# json_object = json.dumps(dict_sinon_skip, indent=4)
#
# # Writing to sample.json
# with open("C:/Users/andre/Documents/GitHub/NLG_BRAZILIAN_PORTUGUESE_19-11/mineração_lexicon/dic_sin_cbow2.json", "w") as outfile:
#     outfile.write(json_object)
#
# dict_sinon_skip.items()

####DICIONARIOS COM BASE NA WORD NET. NÃO RETORNARAM SINÔNIMOS INTERESSANTES PARA USAR

###########################
################################
##################################
# wn.synsets('registrar', lang='por', pos= wn.VERB)
# for synset in wn.synsets('registrar', lang= 'por'):
#     print(synset.name(), synset.definition())
#
# for synset in wn.synsets('registrar', lang= 'por'):
#     for lemma in synset.lemmas('por'):
# #         print(lemma.name())
#
# dict_sinon_wn = {}
#
# for palavra in lemas_verbos:
#     sinonimos = []
#     dict_sinon_wn.update({palavra: sinonimos})
#     i=0
#     for synset in wn.synsets(palavra, lang='por', pos=wn.VERB):
#         for lemma in synset.lemmas('por'):
#             sinonimo = lemma.name()
#             if sinonimo not in sinonimos:
#                 sinonimos.append(sinonimo)
#             i+=1
#     i+=1
#
#
# # Serializing json
# json_object = json.dumps(dict, indent=4)
#
# # Writing to sample.json
# with open("C:/Users/andre/Documents/GitHub/NLG_BRAZILIAN_PORTUGUESE_19-11/mineração_lexicon/dic_sin_wn.json", "w", encoding="utf-8") as outfile:
#     outfile.write(json_object)
#
