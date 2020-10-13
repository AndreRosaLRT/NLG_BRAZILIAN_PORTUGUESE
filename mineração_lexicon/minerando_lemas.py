import json
# WORDNET
#WORDNET
#preparando o ambiente
import nltk
#download do wordnet no ambiente
nltk.download('wordnet')
nltk.download('omw')
#importa wordnet
from nltk.corpus import wordnet as wn
wn.langs()

##########WORDEMBEDDINGS

import gensim
print('done')
from gensim import models
from gensim.models import KeyedVectors
print('done')

model_cbow = KeyedVectors.load_word2vec_format('./mineração_lexicon/cbow_s50.txt')
print('Done')
model_skip = KeyedVectors.load_word2vec_format('./mineração_lexicon/skip_s300.txt')
print('Done')


palavras_cbow = list(model_cbow.wv.vocab)
palavras_skip = list(model_skip.wv.vocab)


####
# OS VERBOS DE INTERESSE:
arquivo = json.load(open('./mineração_lexicon/verbs.json'))
#
# type(arquivo)
chaves = arquivo.keys()
# type(chaves)
chaves = list(chaves)

lemas_verbos = []

i = 0
for entrada in chaves:
    verbo = chaves[i].split()[1]
    if verbo not in lemas_verbos:
        lemas_verbos.append(verbo)
    i += 1
lemas_verbos[4] = 'alcançar'




###########################
################################
##################################

lemas_verbos[0]

wn.synsets('registrar', lang='por', pos= wn.VERB)
for synset in wn.synsets('registrar', lang= 'por'):
    print(synset.name(), synset.definition())

for synset in wn.synsets('registrar', lang= 'por'):
    for lemma in synset.lemmas('por'):
        print(lemma.name())




dict_sinon_wn = {

}
for palavra in lemas_verbos:
    sinonimos = []
    dict_sinon_wn.update({palavra:sinonimos})
    i=0
    for synset in wn.synsets(palavra, lang='por', pos=wn.VERB):
        for lemma in synset.lemmas('por'):
            sinonimo = lemma.name()
            if sinonimo not in sinonimos:
                sinonimos.append(sinonimo)
            i+=1
    i+=1


##############################################


###dicionario co base no cbow
dict_sinon_cbow = {

}

for palavra in lemas_verbos:
    sinonimos = []
    dict_sinon_cbow.update({palavra: sinonimos})
    i=0
    for entrada in model_cbow.most_similar(palavra):
        sinonimos.append(model_cbow.most_similar(palavra)[i][0])
        i+=1
    i+=1



# Serializing json
json_object = json.dumps(dict_sinon_cbow, indent=4)

# Writing to sample.json
with open("./mineração_lexicon/dic_sin_cbow.json", "w") as outfile:
    outfile.write(json_object)

dict_sinon_cbow.items()


###dicionario co base no skipgram
dict_sinon_skip = {

}


1+1

for palavra in lemas_verbos:
    dict_sinon_skip.update({palavra: {}})
    i=0
    sinonimos = []
    for entrada in model_cbow.most_similar(palavra):
        sinonimos.append(model_cbow.most_similar(palavra)[i][0])
        i+=1
    i=0
    for sin in sinonimos:
        dict_sinon_skip[palavra].update({'sin_' + str(i): sin})
        i+=1
    i+=1

# Serializing json
json_object = json.dumps(dict_sinon, indent=4)

# Writing to sample.json
with open("dic_sin_cbow.json", "w") as outfile:
    outfile.write(json_object)

dict_sinon_skip.items()














###############################
# BANCO DE FUNÇÕES

#acessando synsets
wn.synsets('study') #no inglês como default

#no português
wn.synsets('correr', lang='por')
nltk.sent_tokenize()

#com POS
#ingles com especificação de POS
wn.synsets('knowledge', pos=wn.NOUN)

#port com especificação de POS
wn.synsets('saber', lang='por', pos= wn.VERB)

#ACESSANDO SYNSET ESPECÍFICO

wn.synset('handy.s.01').name()
wn.synset('handy.s.01').definition()
wn.synset('handy.s.01').examples()
    #acessando hipônimo e hiperônimo
wn.synsets('computador', lang= 'por')

for synset in wn.synsets('computador', lang= 'por'):
    print(synset.name(), synset.definition())

wn.synset('computer.n.01').hypernyms()
wn.synset('computer.n.01').hyponyms()

#acessando lemas:
for lemma in wn.synset('computer.n.01').lemmas():
    print (lemma.name())

wn.synset('computer.n.01').lemmas('por')

wn.synsets('discursar', lang='por')[0].lemmas()
wn.synsets('discursar', lang='por')[0].lemmas('por')

wn.lemma('discourse.v.01.discursar', lang='por')
#
wn.synsets('andar', lang='por', pos=wn.VERB)

lemma = wn.synset('good.a.01').lemmas()[0]
#antônimos
lemma.antonyms()

#teste de similaridade nos critérios da wordnet

wn.synsets('trabalho', lang= 'por')
wn.synsets('estudo', lang= 'por')

work = wn.synset('work.n.01')
study = wn.synset('study.n.02')

work.path_similarity(study)

with open('anavitoria.txt', 'r') as f:
    sample = f.read()