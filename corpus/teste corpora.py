# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:05:19 2019

@author: andre
"""

#NLTK PARA OS TEXTOS DO CORPUS DA TESE

#TESTES

lista1=["maçã", "laranja", "abacate"]

# Sintaxe: {chave : valor} 
dic1 = {
    "NN":"Substantivo",
    "VB":"Verbo",
    "JJ":"Adjetivo",
    "IN":"Preposição"}
print(dic1)

type(dic1)

print(dic1["NN"])
print(dic1["JJ"])

#SEGMENTAÇÃO EM SENTENÇAS teste

#OPENING THE FILE

f = open ('test.txt', 'r')
print (os.getcwd())

import os
os.getcwd()
os.chdir ('C:/Users/andre/Dropbox/André Rosa/FACULDADE/Doutorado/TESE_DESENVOLVIMENTO/corpus/experto_artigos')
os.listdir(os.curdir)

t1 = open ('teste.txt', 'r+')
print (t1.name)
teste1 = t1.read()
teste1
type (teste1)
type (t1)

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

sentences_t1= sent_tokenize (teste1)
sentences_t1
type (sentences_t1)
print (sentences_t1)
len (sentences_t1)
sentences_t1 [0]
sentences_t1 [1]
sentences_t1 [2]

print (sentences_t1)
with open ('output.csv','w', newline='') as outfile:
    fieldnames= ['sentence']
    wr = csv.DictWriter(outfile,fieldnames=fieldnames)
    wr.writeheader()
    sentences_t1= sent_tokenize (teste1)
    for i in sentences_t1:
        wr.writerows(sentences_t1)  
    
data= [['x', 'y'],
        ['d','dfd']]
with open ('output.csv','w', newline='') as outfile:
    a = csv.writer(outfile, delimiter=',')
    a.writerows(data)
#########################
    
    

################################## saving to csv

with open ('output.csv','w', newline='') as outfile:
    list_of_sentences = sent_tokenize(teste1.strip())
    writer = csv.DictWriter(outfile, delimiter = '|',  quotechar = None, quoting = csv.QUOTE_NONE, escapechar="\\")
    for phrase in list_of_sentences:
        phrasedict = {'phrase':phrase}
        writer.writerow(phrase)

RESULTS = [
    ['apple','cherry','orange','pineapple','strawberry']
]
with open("output.csv",'w') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerow(sentences_t1)


import csv



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