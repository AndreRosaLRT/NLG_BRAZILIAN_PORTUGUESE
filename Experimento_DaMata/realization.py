__author__ = 'thiagocastroferreira'
# INSERI ESTE ARQUIVO APENAS PARA APRESENTAR AS MUDANÇAS QUE REALIZEI NO PROGRAMA DO THIAGO. NÃO
# FUNCIONA SOZINHO. NÃO PUDE DISPONIBILAR O PROJETO INTEIRO POIS HÁ CREDENCIAIS SIGILOSAS DE ACESSO AO BANCO DE DADOS
# O codigo abaixo é apenas para apresentar as mudanças que realizei na class Realization para incoroporar a minha função
# flexão verbal.
import json
import os

import nlg.contractions as contractions
from nltk.tokenize.treebank import TreebankWordDetokenizer
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *


class Realization:
    def __init__(self, lexicon_path, language='pt-br'):
        self.language = language
        self.adjectives = json.load(open(os.path.join(lexicon_path, 'adjectives.json')))
        self.determiners = json.load(open(os.path.join(lexicon_path, 'determiners.json')))
        self.nouns = json.load(open(os.path.join(lexicon_path, 'nouns.json')))
        self.verbs = json.load(open(os.path.join(lexicon_path, 'verbs.json')))
        # Detokenizer
        self.detokenizer = TreebankWordDetokenizer()

    def generate(self, text):
        new_text, elements, parameters, i = [], [], [], 0
        while i < len(text):
            token = text[i]
            if 'VP[' in token:
                elements = list(token[3:-1].split(','))
                for element in elements:
                    parameter = element.split('=')[1]
                    parameters.append(parameter)
                verb = flexionar_verbo(*parameters)
                new_text.append(verb)
            # new_text, i = [], 0
            # while i < len(text):
            #     token = text[i]
            #     if 'VP[' in token:
            #         key = token + ' ' + text[i+1].lower()
            #         if key in self.verbs:
            #             new_text.extend(self.verbs[key][0].split())
            #         else:
            #             new_text.append(text[i+1])
            #         i += 2
            elif 'ADJ[' in token:
                key = token + ' ' + text[i + 1].lower()
                if key in self.adjectives:
                    new_text.extend(self.adjectives[key][0].split())
                else:
                    new_text.append(text[i + 1])
                i += 2
            elif 'DT[' in token:
                key = token + ' ' + text[i + 1].lower()
                if key in self.determiners:
                    new_text.extend(self.determiners[key][0].split())
                else:
                    new_text.append(text[i + 1])
                i += 2
            elif 'NN[' in token:
                key = token + ' ' + text[i + 1].lower()
                if key in self.nouns:
                    new_text.extend(self.nouns[key][0].split())
                else:
                    new_text.append(text[i + 1])
                i += 2
            else:
                new_text.append(token)
                i += 1
        return new_text

    def realize(self, paragraphs):
        text = ''
        for i, paragraph in enumerate(paragraphs):
            for j, sentence in enumerate(paragraph):
                snt = self.detokenizer.detokenize(self.generate(sentence.split()))
                snt = snt[0].upper() + snt[1:]
                if self.language == 'pt-br':
                    snttext = contractions.realize(snt)
                else:
                    snttext = snt
                paragraphs[i][j] = snttext.replace(' )', ')').replace(' ,', ',').replace(' .', '.')
                text += snttext
                text += ' '
            text = text.strip() + '\n\n'
        return paragraphs
