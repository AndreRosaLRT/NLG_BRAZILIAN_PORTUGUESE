# -*- coding: utf-8 -*-
"""

Created on Mon Feb 25 16:05:19 2019

@author: andre
"""

##SETTING DIRECTORY

import os
os.getcwd()
os.chdir ('C:\\Users\\andre\\Dropbox\\André Rosa\\FACULDADE\\Doutorado\\TESE\\NLG_BRAZILIAN_PORTUGUESE_19-11\\corpus\\SUBCORPORA_LIMPOS')
os.listdir(os.curdir)


#OPENING THE FILES

#     ATIVIDADE: EXPLICAR
text_sample1 = open ('revista_brasileira_de_enfermagem.txt', 'r+')#SALVAR O TEXTO EM ANSI
print (text_sample1.name)
corpus_sample1 = text_sample1.read()
corpus_sample1.rstrip('\n')
type (corpus_sample1)

    #ATIVIDADE: HABILITAR
os.chdir ('C:\\Users\\andre\\Dropbox\\André Rosa\\FACULDADE\\'
          'Doutorado\\TESE\\NLG_BRAZILIAN_PORTUGUESE_19-11\\corpus\\SUBCORPORA_LIMPOS\\HABILITAR_CARTILHA')
os.listdir(os.curdir)

text_sample_habilitar = open ('HABILITAR_CARTILHA_COMPLETO.txt', 'r+')#SALVAR O TEXTO EM ANSI
print (text_sample_habilitar.name)
corpus_sample_habilitar = text_sample_habilitar.read()
corpus_sample_habilitar.rstrip('\n')
type (corpus_sample_habilitar)

#PPREPARING TEXTS _ NLTK_ TOKENIZING SENTENCES

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize


    # ATIVIDADE: HABILITAR
sentences_habilitar= sent_tokenize (corpus_sample_habilitar)
sentences_habilitar
# print (sentences_habilitar)
# len (sentences_habilitar)

##RANDOMIZING SENTENCES FOR ANNOTATION


import secrets  # imports secure module.

# help(secrets)
#
sentence_random = secrets.SystemRandom()  # creates a secure random object.
# a sequence or set will work here. (assign a list to a variable)

import random

#     ATIVIDADE:HABILITAR

list_of_random_sentences_habilitar = sentence_random.sample(sentences_habilitar, 10)
print (list_of_random_sentences_habilitar)
print (list_of_random_sentences_habilitar [7])
len (list_of_random_sentences_habilitar)



#SAVING SENTENCES AS TXT FOR SEPARATING IN CLAUSES


# ATIVIDADE : HABILITAR
for index in range(len(list_of_random_sentences_habilitar)):
    list_of_random_sentences_habilitar[index] = list_of_random_sentences_habilitar[index].rstrip('\n')


#writing the txt with the sentences:
    
with open('sentences_output_habilitar.txt', 'w') as filehandle:
    for listitem in list_of_random_sentences_habilitar:
        filehandle.write('%s\n' % listitem)


print(list_of_random_sentences_habilitar)























#########################
    
    
##TRYING TO SAVE TO CSV
################################## saving to csv

with open ('output.csv','w', newline='') as outfile:
    list_of_sentences = sentences))
    writer = csv.DictWriter(outfile, delimiter = '|',  quotechar = None, quoting = csv.QUOTE_NONE, escapechar="\\")
    for phrase in sentences:
        phrasedict = {'phrase':phrase}
        writer.writerow(phrase)

RESULTS = [
    ['apple','cherry','orange','pineapple','strawberry']
]
with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(sentences_t1)






with open('sentence_token.txt', 'w') as fout:
    for phrase in sent_tokenize(teste1):
        print(' '.join(tokens), file=fout)

with open("output.csv", 'w'):


with open("output.csv",'w') as resultFile:
   for item in sentences_t1:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerows([item],)
    
with open('output.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(RESULT)


RESULT = ['apple','cherry','orange','pineapple','strawberry']
with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(RESULT)



from __future__ import print_function


        
with open ('myfile.txt') as fin, open('tokens.txt') as fout:
    for line in fin:
        tokens = word_tokenize(line)
        print(' '.join(tokens), end='\n', file=fout)
#saving the output to a new txt
with open ('sentence_token', 'w')as tk1:
    for i in sentences_t1:
         print (i)


with open('teste1') as in_file, open((sent_tokenize (teste)), "w") as out_file:
    for i in in_file:
        for sentence in sentences:
            out_file.write(sentence)
            out_file.write("\n")
##


t1.close()






