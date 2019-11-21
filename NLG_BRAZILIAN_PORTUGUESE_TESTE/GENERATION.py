# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:50:31 2019

@author: andre
"""






######PRELIMINARES
import os
os.getcwd()
#help(os)
#os.listdir(os.curdir)



##LEGENDA_SIGLAS
#OE (ORIENTAÇÃO EXPERIENCIAL)
#OI (ORIENTAÇÃO INTERPESSOAL)

#packages

import choice
#help (choice)
#import argparse
#help(argparse)


######



###
#Preciso determinar de maneira geral se para as funções eu vou passar
##as informações 'de cima' para que a função retorne a realização na estrutura. Me parece
#que esta é a melhor maneira até agora. Vou ir testanto
####checar stemming: https://www.nltk.org/_modules/nltk/stem/rslp.html



###############################################################################
#####################
                ###########ORDEM DA PALAVRA

###ADVÉRBIO    INÍCIO####

def advérbioModoSwitcher():
   
    i = int(input())
    
    switcherModo = {
         1:'bem',
         2:'mal',
         3:'assim',
         4:'adrede',
         5:'melhor',
         6:'pior',
         7:'depressa',
         8:'devagar',
         9:'acinte',
         10:'debalde', 
         11:'cuidadosamente', 
         12:'calmamente',
         13:'tristemente'
        }
            
    return switcherModo.get(i, 'Seleção não disponível')


def advérbioIntensidadeSwitcher():
    
    i = int(input())
    
    switcherIntensidade = {
         1:'muito', 
         2:'demais',
         3:'todo',
         4:'pouco', 
         5:'tão',
         6:'quão',
         7:'demasiado',
         8:'bastante', 
         9:'imenso',
         10:'demais',
         11:'mais', 
         12:'menos', 
         13:'quanto', 
         14:'quase', 
         15:'tanto', 
         16:'assaz', 
         17:'tudo', 
         18:'nada' 
         }
    return switcherIntensidade.get(i, 'Seleção não disponível')

        

def advérbioLugarSwitcher():
    i = int(input())
    
    switcherLugar = {
    
        1:'aí',
        2:'aqui',
        3:'acolá',
        4:'cá', 
        5:'lá',
        6:'ali',
        7:'adiante',
        8:'abaixo',
        9:'embaixo',
        10:'acima',
        11:'adentro',
        12:'dentro'
        }
    
    return switcherLugar.get(i, 'Seleção não disponível')


a= choice.Menu(['1','2']).ask()
def advérbioTempoSwitcher():
    i = int(input())
    
    switcherTempo = {
        1:'ainda',
        2:'agora',
        3:'amanhã',
        4:'à noite',
        5:'anteontem',
        6:'antes',
        7:'à tarde', 
        8:'às vezes',
        9:'atualmente',
        10:'breve', 
        11:'cedo', 
        12:'depois',
        13:'de manhã',
        14:'de repente',
        15:'de vez em quando',
        16:'hoje', 
        17:'hoje em dia',
        18:'já',  
        19:'logo', 
        20:'nunca', 
        21:'ontem', 
        22:'ora',
        23:'outrora', 
        24:'quando',
        25:'sempre', 
        26:'tarde',
        27:'jamais',
        }
    return switcherTempo.get(i, 'Seleção não disponível')

        

def advérbioNegaçãoSwitcher():
    i = int(input())
    
    switcherNegação = {1:'não',2:'nem',3:'tampouco',4:'nunca',5:'jamais'}
    return switcherNegação.get(i,'Seleção não disponível')

def advérbioAfirmaçãoSwitcher():
    
    i = int(input())
    
    switcherAfirmação = {1:'sim',
                       2:'deveras',
                       3:'indubitavelmente',
                       4:'decididamente',
                       5:'certamente',
                       6:'realmente',
                       7:'decerto',
                       8:'certo',
                       9:'efetivamente' 
                       }
    return switcherAfirmação.get (i,'Seleção não disponível')
    

def advérbioDúvidaSwitcher():
    
    i = int(input())
    
    switcherDúvida = {1:'possivelmente',
                         2:'provavelmente',   
                         3: 'acaso',
                         4:'porventura',
                         5:'quiçá',
                         6:'será',
                         7:'talvez', 
                         8:'casualmente'}
    return switcherDúvida.get(i, 'Seleção não disponível')

def advérbio():
    '''
    '''
    modo_inserção = choice.Menu(['inserção_manual','inserção_menu']).ask()
    
    if modo_inserção == 'inserção_manual':
        advérbio = input ('Escreva o advérbio desejado:')
        
    elif modo_inserção == 'inserção_menu':
        
        tipo_de_advérbio = choice.Menu(['Modo',
                                        'Intensidade',
                                        'Lugar','Tempo','Negação',
                                        'Afirmação','Dúvida','Adv_relativo']).ask()
        
        if tipo_de_advérbio == 'Modo':
            print ("""
                     1:bem
                     2:mal
                     3:assim
                     4:adrede
                     5:melhor
                     6:pior
                     7:depressa
                     8:devagar
                     9:acinte 
                     10:debalde 
                     11:cuidadosamente 
                     12:calmamente
                     13:tristemente
                    
                   Escolha uma opção:""")
            
            advérbio = advérbioModoSwitcher()
        
    

        elif tipo_de_advérbio == 'Intensidade':
            print("""
                     1:muito 
                     2:demais
                     3:todo
                     4:pouco 
                     5:tão 
                     6:quão
                     7:demasiado
                     8:bastante 
                     9:imenso
                     10:demais
                     11:mais 
                     12:menos 
                     13:quanto 
                     14:quase 
                     15:tanto 
                     16:assaz 
                     17:tudo 
                     18:nada 
                     

                   Escolha uma opção:""")

            advérbio = advérbioIntensidadeSwitcher()
        
        
        elif tipo_de_advérbio == 'Lugar':
            print("""
                 1:aí
                 2:aqui
                 3:acolá 
                 4:cá 
                 5:lá
                 6:ali
                 7:adiante
                 8:abaixo
                 9:embaixo
                 10:acima
                 11:adentro
                 12:dentro
                 Escolha uma opção:""")
            
            advérbio = advérbioLugarSwitcher()

        elif tipo_de_advérbio == 'Tempo':
            print ("""
                     1:ainda 
                     2:agora
                     3:amanhã
                     4:à noite
                     5:anteontem
                     6:antes
                     7:à tarde 
                     8:às vezes
                     9:atualmente
                     10:breve 
                     11:cedo 
                     12:depois
                     13:de manhã
                     14:de repente
                     15:de vez em quando
                     16:hoje 
                     17:hoje em dia
                     18:já  
                     19:logo 
                     20:nunca 
                     21:ontem 
                     22:ora 
                     23:outrora 
                     24:quando 
                     25:sempre 
                     26:tarde 
                     27:jamais         
                     

                   Escolha uma opção:""")
            
            advérbio = advérbioTempoSwitcher()
        
        
        elif tipo_de_advérbio == 'Negação':
            print("""
                 1:não
                 2:nem
                 3:tampouco 
                 4:nunca
                 5:jamais 
               Escolha uma opção:""")
            advérbio = advérbioNegaçãoSwitcher()
      
        elif tipo_de_advérbio == 'Afirmação':
            
            print("""
             1:sim 
             2:deveras 
             3:indubitavelmente
             4:decididamente
             5:certamente
             6:realmente
             7:decerto
             8:certo
             9:efetivamente 
             
           Escolha uma opção:""")

            advérbio= advérbioAfirmaçãoSwitcher()
            
        elif tipo_de_advérbio == 'Dúvida':
            
            print("""
                 1:possivelmente
                 2:provavelmente   
                 3: acaso
                 4:porventura
                 5:quiçá
                 6:será
                 7:talvez 
                 8:casualmente 
          
                 
               Escolha uma opção:""")
            
            advébio = advérbioDúvidaSwitcher()
        
        
        elif tipo_de_advérbio == 'Adv_relativo':
            
            advérbio = choice.Menu(['de onde', 'quando',
                                    'onde', 'de quando', 'que','por onde']).ask()
        
    return advérbio



###ADVÉRBIO    FIM####



######
    



####################################################################
##### VERBO INÍCIO####

def def_classe_de_verbo ():
    
    '''
    (str)-> str

    Retorna um str com classe de verbo dado um verbm em str.

    >>>def_classe_de_verbo ('andar')
    lexical
    >>> def_classe_de_verbo ('ir')
    auxiliar
    >>>def_classe_de_verbo ('poder')
    'modal'
    '''

    print ("Qual é a função do verbo no grupo verbal?")
    função_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal']).ask()
    

    if função_no_grupo_verbal == 'Evento':
        return ('lexical')
    elif função_no_grupo_verbal == 'Auxiliar':
        return ('auxiliar')
    elif função_no_grupo_verbal == 'Modal':
        return ('modal')
#######################################

##A próximo função precisa ir sendo atualizada e melhorada à medida que subo na escala de ordens:
        # Resolver a questão de como vou fazer para dar entrada no 'verbo'-talvez alguma
#        subfunção que pergunta ao usuário qual é a o tipo de experiência
#        ele pretende gerar. Provavelmente vai puxar do inventário de tipos de configuração
#        que vou introduzir a partir da anotação do texto na GUM- um inventário de
#        realizações de determinados significados semânticos específicos (de lá vamos puxar
#            as informações necessárias para a geração)



####ESTA FUNÇÃO DEPENDE DE FORNECIMENTO DO PARÂMETO 'VERBO'

#        A primeira função o verbo não precisa estar lematizado, ou seja, podemos entrar qualquer verbo, mesmo conjugado e
#        a função retorna o ME. Essa opção me paree um pouco redundante pois se sabemos de antemão qual é o verbo, já sabemos
##        qual é o ME. A segunda função depende de um verbo lematizado que dependerá por sua vez de escolhas dentro de opções de
#        tipos de experiências que são realizadas por verbos lematizados (esses verbos então serão realizações de opções dentro de
#            de uma estrutura em cascata de opções que ainda preciso descobrir como fazer)

def experiência_do_verbo ():

    '''(str)-> str

    Retorna um str com o morfema experiencial (ME) que realiza
    a experiência do verbo, dado um verbo lematizado.

    >>>experiência_do_verbo('levar')
    'lev'
    >>>experiência_do_verbo('levo' )
    'lev'
    >>> experiência_do_verbo('levei')
    'lev'
    >>>experiência_do_verbo('dizer')
    'diz'
    >>>experiência_do_verbo ('ter')
    't'
    '''
    
    verbo = input ("Qual o verbo?")
    
    MI = realização_transitoriedade_do_verbo ()
    ME =  (verbo[slice (-len (MI))])
 
    return ME








#    if (
#        padrão_de_morfologia == '-AR' and OI_tipo_de_orientação == 'infinitivo' and OI_tipo_de_pessoa == 'NA'or OI_número == 'NA' or
#        padrão_de_morfologia == '-ER' and  OI_tipo_de_orientação == 'infinitivo' and OI_tipo_de_pessoa == 'NA' or OI_número == 'NA'or
#        padrão_de_morfologia == '-IR' and  OI_tipo_de_orientação == 'infinitivo' and OI_tipo_de_pessoa == 'NA' or OI_número == 'NA'or
#        padrão_de_morfologia == '-OR' and  OI_tipo_de_orientação == 'infinitivo' and OI_tipo_de_pessoa == 'NA'
#        ):
#
#
#        ME = (verbo[slice (-2)])
#        return (ME)
#
#
#    elif (
#        padrão_de_morfologia == '-AR' and OI_tipo_de_orientação == 'presente'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
#        padrão_de_morfologia == '-ER' and OI_tipo_de_orientação == 'presente'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
#        padrão_de_morfologia == '-IR' and OI_tipo_de_orientação == 'presente'and OI_tipo_de_pessoa == '1pessoa'and OI_número == 'singular'
#         ):
#       ME = (verbo[slice(-1)])
#       return ME
#
#
#    elif (
#         padrão_de_morfologia == '-OR' and
#         OI_tipo_de_orientação == 'presente'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
#         ):
#
#
#        ME = (verbo[slice(-4)])
#        return ME
#
#    elif (
#         padrão_de_morfologia == '-AR'and OI_tipo_de_orientação == 'pretérito_perfectivo_I'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
#         padrão_de_morfologia == '-OR' and  OI_tipo_de_orientação == 'pretérito_perfectivo_I'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
#         ):
#
#
#        ME = (verbo[ slice(-2)])
#        return ME
#
#    elif (
#         padrão_de_morfologia == '-ER' and OI_tipo_de_orientação == 'pretérito_perfectivo_I'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
#         padrão_de_morfologia == '-IR' and OI_tipo_de_orientação == 'pretérito_perfectivo_I'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
#         ):
#
#
#        ME = (verbo[slice(-1)])
#        return ME




####Esta função depende de um parâmetro que vai vir da lista lematizada de verbos advindos da anotação na GUM
        ##TENHO AINDA QUE DESCOBRIR O JEITO PARA PUXAR ESSE VERBO A PARTIR DA LISTA DE VERBOS
#        LEMATIZADOS QUE POR SUA VEZ VÃO ESTAR ATRELADOS A UM TIPO DE EXPERIÊNCIA
##        DA GUM. TENHO QUE DESCOBRIR UM JEITO DE FAZER UM INPUT COM OPÇÕES DEPENDENTES EM CASCATA


def experiência_do_verbo2 ():

    '''(str)-> str

    Retorna um str com o morfema experiencial (ME) que realiza
    a experiência do verbo, dado um verbo lematizado

    >>>experiência_do_verbo2 ()
    'lev'
    >>>experiência_do_verbo2 ('')
    'diz'
    >>>experiência_do_verbo2 ('')
    't'
    '''
    
#    #o verbo_lematizado vai ser a saída de uma seleção de tipos de experiências
#    advindo das listas de tipos de experiências advinda da GUM

    verbo_lematizado = input ('Qual é o verbo lematizado?')
    ME = (verbo_lematizado[slice (-2)])
    return (ME)





#####testes e dúvidas


     # Implementar um jeito no qual com uma entrada de tipo de configuração da GUM
     #eu chegue nos desdobramentos aqui na ordem da palavra. Para isso, as funções
#     terão de ir mudando ao longo do trabalho. Por enquanto fica um pouco circular as coisas.



##REALIZAÇÃO DE UM ME DADO O TIPO DE EXPERIÊNCIA A PARTIR DE UMA LISTA QUE NO FUTURO VIRÁ da anotação na gum

#experiências_de_fazer_acontecer = x + y
#x = x1,x2
#x1='AffectingSimpleMotion'
#x2='AffectingOrientatioChange'
#y1='y1a'
#y2='y2a'
#y = y1,y2
#AffectingSimpleMotion = 'levar', 'pegar'
#type(AffectingSimpleMotion)
#len(AffectingSimpleMotion)
#AffectingSimpleMotion[1]
#choice.Menu([AffectingSimpleMotion[1], AffectingSimpleMotion[2]).ask()
#help(choice.Menu)
#x[1]




###

####. Suponho, pelo que estou vendo ao decorrer do trabalho, que a função de
#       experiência_do_verbo terá precedência à de transitoriedade quando
#        chegar a
#       Neste caso, as informações dadas pelo usuário são praticamente as mesmas
#        que as passadas na função de experiência do verbo. A diferença é que
##        o que ela retorna é apenas o morfema que encerra a OI. mE PARECE UM POUCO
#        circular: temos que passar sempre alguma informação para conseguir outra
#        mas isso será importante pois o verbo vai ser a concatenação dos resultados
##        destas funções (ainda vou descobrir como faz). Vou ter de ver como
#        vai ser depois, qual o tipo de informação vai ser melhor para gerar esta
#        estrutura.




##############TRANSITORIEDADE######################################################




def detecção_transitoriedade_do_verbo ():

    '''
    (str) -> str


    Retorna o morfema interpessoal que realiza a orientação interpessoal
    dados o verbo, seu padrão de morfologia, seu tipo de orientação
    e o tipo de pessoa.

    >>>detecção_transitoriedade_do_verbo ('levar')
    'ar'
    >>>detecção_transitoriedade_do_verbo ('levo')
    'o'
    >>>detecção_transitoriedade_do_verbo ('exponho')
    'onho'
    >>>detecção_transitoriedade_do_verbo ('levei')
    'ei'
    >>>detecção_transitoriedade_do_verbo ('expus')
    'us'
    >>>detecção_transitoriedade_do_verbo ('li')
    'i'
    >>>detecção_transitoriedade_do_verbo ('bebi')
    'i'

    '''
    verbo = input ("Qual o verbo?")
    ME = experiência_do_verbo ()
    MI = (verbo[len(ME):])
    return  MI


###################MENU PARA TIPOS DE OI
def OI_ORIENTAÇÃO_MODAL_NÃO_FINITO():
    print("Qual é a Orientação modal não_finita desejada?")
    #time.sleep(1)
    print()

    OI_ORIENTAÇÃO_MODAL_NÃO_FINITO = choice.Menu(['subjuntivo_conjuntivo','subjuntivo_condicional',
                                                   'subjuntivo_optativo','imperativo_I','imperativo_II',
                                                   'não_finito_concretizado']).ask()
    
    return OI_ORIENTAÇÃO_MODAL_NÃO_FINITO
    
     
           
def OI_ORIENTAÇÃO_MODAL_FINITO():
    print("Qual é a Orientação interpessoal finita desejada?")
    #time.sleep(1)
    print()

    OI_ORIENTAÇÃO_MODAL_FINITO = choice.Menu(['presente',
                                     'pretérito_perfectivo_I',
                                     'pretérito_perfectivo_II',
                                     'pretérito_imperfectivo',
                                     'passado_volitivo', 
                                     'futuro']).ask()
                                      
    return OI_ORIENTAÇÃO_MODAL_FINITO

    

def OI_não_orientado():
    print("Qual é a Orientação interpessoal desejada?")
    
    

    tipo_de_orientação = choice.Menu([
                                      'infinitivo',
                                      'gerúndio',
                                      'particípio'
                                        ]).ask()
    return tipo_de_orientação   
        
      


def OI_tipo_de_orientação():
    
    print("Qual é a Orientação interpessoal desejada?")
    print ("""
          0: infinitivo
          1: presente
          2: pretérito_perfectivo_I
          3: pretérito_perfectivo_II
          4: pretérito_imperfectivo
          5: passado_volitivo 
          6: futuro
          7: subjuntivo_conjuntivo
          8: subjuntivo_condicional 
          9: subjuntivo_optativo
          10: imperativo_I
          11: imperativo_II
          12: não_finito_concretizado 
          13: gerúndio
          14: particípio
          15: NA
          """
        )
   
    i = int(input('Selecione uma opção:'))
    switcher = {
              0: 'infinitivo',
              1: 'presente',
              2: 'pretérito_perfectivo_I',
              3: 'pretérito_perfectivo_II',
              4: 'pretérito_imperfectivo',
              5: 'passado_volitivo',
              6: 'futuro',
              7: 'subjuntivo_conjuntivo',
              8: 'subjuntivo_condicional',
              9: 'subjuntivo_optativo',
              10: 'imperativo_I',
              11: 'imperativo_II',
              12: 'não_finito_concretizado',
              13: 'gerúndio',
              14: 'particípio',
              15: 'NA'

                       }
    
    tipo_de_orientação = switcher.get(i,'Seleção não disponível.')
    
    return tipo_de_orientação
       
 #######S       
        
def realização_transitoriedade_infinitivo ():
    '''(str)->str
    
    Retorna o morfema que realiza a transitoriedade de um verbo no infinitivo, dados
    padrão de morfologia.
    
    >>>realização_transitoriedade_infinitivo ()
    'ar'
    ''' 
    
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
   
   
    
    if (padrão_de_morfologia == '-AR'):
        MI = 'ar'
        return MI
    elif (padrão_de_morfologia == '-ER'):
        MI = 'er'
        return MI
    
    elif (padrão_de_morfologia == '-IR'):
        MI = 'ir'
        return MI
    
    elif (padrão_de_morfologia == '-IR'):
        MI = 'ir'
        return MI
        
        

def realização_transitoriedade_presente ():
    '''(str,str,str,str)->str
    
    Retorna o morfema que realiza a transitoriedade de um verbo no presente, dados
    a o padrão de morfologia, tipo de orientação, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_presente ()
    'o'
    ''' 
    
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()
   
    
    if (
        padrão_de_morfologia == '-AR' and  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and  OI_tipo_de_pessoa == '1pessoa'and OI_número == 'singular'
         ):
       
        
        MI = 'o'
        return MI


    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):

        MI='onho'
        return MI

    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'as'
            return MI

    elif(
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa'and OI_número == 'singular'
         ):
        
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'es'
            return MI
      

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI = 'ões'
            return MI
        

    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
        
            MI = 'a'
            return MI
              

    elif(
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa'and OI_número == 'singular'
         ):
       MI = 'e'
       return MI


    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):

        MI='õe'
        return MI

    elif padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'amos'
            return MI  

    elif(padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'emos'
            return MI
        
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa'and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'imos'
            return MI
    
    elif (padrão_de_morfologia == '-OR'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI='omos'
            return MI
        
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'ais'
            return MI

    elif(padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
             MI = 'eis'
             return MI

    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa'and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
          MI = 'is'
          return MI

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
          MI='ondes'
          return MI
  
    elif padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'am'
            return MI

    elif(
        padrão_de_morfologia == '-ER'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa'and OI_número == 'plural'
        ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
           MI = 'em'
           return MI

    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
    
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI='õem'
            return MI



#pretérito_perfectivo_I
  
def realização_transitoriedade_pretérito_perfectivo_I ():
    
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_I, dados
    a o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    'ei'
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()
   
    if (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):

        MI ='ei'
        return MI

    elif ( padrão_de_morfologia == '-ER'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
         padrão_de_morfologia == '-IR'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
         ):

        MI = 'i'
        return MI
    
    elif  (padrão_de_morfologia == '-OR'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
        MI = 'us'
        return MI
        
    elif (padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ou'
            return MI
        else:
            MI = 'aste'
            return MI
      
        
    elif ( padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'eu'
            return MI
        else:
            MI = 'este'
            return MI
        
    elif ( padrão_de_morfologia == '-IR'and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'iu'
            return MI
        else:
            MI = 'iste'
            return MI

    elif  (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ôs'
            return MI
        else:
            MI = 'useste'
            return MI
        
    elif (padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
       
        MI ='ou'
        return MI
              
    elif ( padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
       
            MI = 'eu'
            return MI
        
    elif ( padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
            MI = 'iu'
            return MI
        
    elif  (padrão_de_morfologia == '-OR'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
            MI = 'ôs'
            return MI
          
    elif (padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ou'
            return MI
        else:
            MI = 'amos'
            return MI
              
    elif ( padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'eu'
            return MI
        else:
            MI = 'emos'
            return MI
        
    elif ( padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'iu'
            return MI
        else:
            MI = 'imos'
            return MI

    elif  (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ôs'
            return MI
        else:
            MI = 'usemos'
            return MI
    
    elif (padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ou'
            return MI
        else:
            MI = 'astes'
            return MI
              
    elif ( padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'eu'
            return MI
        else:
            MI = 'estes'
            return MI
        
    elif ( padrão_de_morfologia == '-IR'and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'iu'
            return MI
        else:
            MI = 'istes'
            return MI

    elif  (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ôs'
            return MI
        else:
            MI = 'usestes'
            return MI

    elif (padrão_de_morfologia == '-AR'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ou'
            return MI
        else:
            MI = 'aram'
            return MI
              
    elif ( padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'eu'
            return MI
        else:
            MI = 'eram'
            return MI
        
    elif ( padrão_de_morfologia == '-IR'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'iu'
            return MI
        else:
            MI = 'iram'
            return MI

    elif  (padrão_de_morfologia == '-OR'and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ôs'
            return MI
        else:
            MI = 'useram'
            return MI




###pretérito imperfectivo
            
def  realização_transitoriedade_pretérito_imperfectivo():
    
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito imperfectivo, dados
    a o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    'ei'
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()
          
        
    if (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
        MI ='ava'
        return MI
       
    
    elif (
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or 
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or 
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'         
          ):
            
        MI = 'ia'
        return MI

    elif  (padrão_de_morfologia == '-OR'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           padrão_de_morfologia == '-OR'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
           ):
           
        MI = 'unha'
        return MI
               
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ava'
            return MI
        else:
            MI = 'avas'
            return MI
      
        
    elif (
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or 
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'
         ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ia'
            return MI
        else:
            MI = 'ias'
            return MI
        
    elif  (padrão_de_morfologia == '-OR'  and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'unha'
            return MI
        else:
            MI = 'unhas'
            return MI
           
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ava'
            return MI
        else:
            MI = 'ávamos'
            return MI
         
    elif (
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or 
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'
          ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ia'
            return MI
        else:
            MI = 'íamos'
            return MI
        
    elif  (padrão_de_morfologia == '-OR'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'unha'
            return MI
        else:
            MI = 'únhamos'
            return MI
        
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ava'
            return MI
        else:
            MI = 'áveis'
            return MI
         
    elif (
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural' or 
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'
          ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ia'
            return MI
        else:
            MI = 'íeis'
            return MI
        
    elif  (padrão_de_morfologia == '-OR'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'unha'
            return MI
        else:
            MI = 'únheis'
            return MI 
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI ='ava'
            return MI
        else:
            MI = 'avam'
            return MI
         
    elif (
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural' or 
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
          ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'ia'
            return MI
        else:
            MI = 'iam'
            return MI
        
    elif  (padrão_de_morfologia == '-OR'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia ==  'Morfologia de 3pessoa do singular':
            MI = 'unha'
            return MI
        else:
            MI = 'unham'
            return MI


def realização_transitoriedade_pretérito_perfectivo_II ():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no pretérito_perfectivo_II, dados
    a o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    'ei'
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()
                
        
    if (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
        ):

        MI ='ara'
        return MI

    elif (padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
          padrão_de_morfologia == '-ER'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
        MI = 'era'
        return MI
     
    elif (padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
          padrão_de_morfologia == '-IR'  and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
        MI = 'ira'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
          padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):

        MI ='usera'
        return MI

    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):

        MI ='aras'
        return MI
    
      
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):

        MI ='eras'
        return MI 
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):

        MI ='iras'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):

        MI ='useras'
        return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):

        MI ='áramos'
        return MI
    
      
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):

        MI ='éramos'
        return MI 
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):

        MI ='íramos'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):

        MI ='úseramos'
        return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):

        MI ='áreis'
        return MI
    
      
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):

        MI ='êreis'
        return MI 
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):

        MI ='íreis'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):

        MI ='uséreis'
        return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):

        MI ='aram'
        return MI
    
      
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):

        MI ='eram'
        return MI 
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):

        MI ='iram'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):

        MI ='useram'
        return MI   


def realização_transitoriedade_passado_volitivo():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no passado volitivo, dados
    a o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    'ei'
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()
    
    
    if (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
        ):

        MI ='aria'
        return MI
          
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
        ):

        MI ='eria'
        return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
        ):

        MI ='iria'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
        ):

        MI ='oria'
        return MI
     
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'aria'
            return MI
        else:
            MI = 'arias'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'eria'
            return MI
        else:
            MI = 'erias'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'iria'
            return MI
        else:
            MI = 'irias'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'oria'
            return MI
        else:
            MI = 'orias'
            return MI
         
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'aria'
            return MI
        else:
            MI = 'aríamos'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            
            MI = 'eria'
            return MI
        else:
            MI = 'eríamos'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular': 
            MI = 'iria'
            return MI
        else:
            MI = 'iríamos'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'oria'
            return MI
        else:
            MI = 'oríamos'
            return MI 
           
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'aria'
            return MI
        else:
            MI = 'aríeis'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            
            MI = 'eria'
            return MI
        else:
            MI = 'eríeis'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular': 
            MI = 'iria'
            return MI
        else:
            MI = 'iríeis'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'oria'
            return MI
        else:
            MI = 'oríeis'
            return MI
         
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'aria'
            return MI
        else:
            MI = 'ariam'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            
            MI = 'eria'
            return MI
        else:
            MI = 'eriam'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular': 
            MI = 'iria'
            return MI
        else:
            MI = 'iriam'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'oria'
            return MI
        else:
            MI = 'oriam'
            return MI


def realização_transitoriedade_futuro():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no futuro, dados
    a o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    'ei'
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()

    if (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'arei'
       return MI
   
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'erei'
       return MI
   
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'irei'
       return MI
   
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'orei'
       return MI
   
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ará'
            return MI
        else:
            MI = 'arás'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'erá'
            return MI
        else:
            MI = 'erás'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'irá'
            return MI
        else:
            MI = 'irás'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'orá'
            return MI
        else:
            MI = 'orás'
            return MI
   
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
       MI = 'ará'
       return MI
   
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'erá'
       return MI
   
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'irá'
       return MI
   
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
       MI = 'orá'
       return MI    
     
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
       MI = 'aremos'
       return MI
   
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
       MI = 'eremos'
       return MI
   
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
       MI = 'iremos'
       return MI
   
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
       MI = 'oremos'
       return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
       MI = 'areis'
       return MI
   
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
       MI = 'ereis'
       return MI
   
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
       MI = 'ireis'
       return MI
   
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
       MI = 'oreis'
       return MI
   
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
       MI = 'arão'
       return MI
   
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
       MI = 'erão'
       return MI
   
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
       MI = 'irão'
       return MI
   
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
       MI = 'orão'
       return MI



def realização_transitoriedade_subjuntivo_conjuntivo():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo conjuntivo, dados
    o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()
    
    
    
    if (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
       MI = 'e'
       return MI
   
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
       MI = 'a'
       return MI
   
    elif (
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
       MI = 'onha'
       return MI
   
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
       else:
            MI = 'es'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'
        ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'as'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'onha'
            return MI
        else:
            MI = 'onhas'
            return MI
   
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'emos'
            return MI
    
    elif ( 
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'
           ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'amos'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'onha'
            return MI
        else:
            MI = 'onhamos'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'eis'
            return MI
    
    elif ( 
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'
           ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'ais'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'onha'
            return MI
        else:
            MI = 'onhais'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'em'
            return MI
    
    elif ( 
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
           ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'am'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'onha'
            return MI
        else:
            MI = 'onham'
            return MI
     
#######subjuntivo_condicional
def realização_transitoriedade_subjuntivo_condicional():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo condicional, dados
    o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_pretérito_perfectivo_I ()
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()       
    
    
    if (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
       MI = 'asse'
       return MI
   
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
           ):
       MI = 'esse'
       return MI
  
    elif (
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
            ):
         MI = 'isse'
         return MI
          
        
    elif (
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
       MI = 'usesse'
       return MI
   
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'asse'
            return MI
       else:
            MI = 'asses'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'esse'
            return MI
        else:
            MI = 'esses'
            return MI
    
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'isse'
            return MI
        else:
            MI = 'isses'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'usesse'
            return MI
        else:
            MI = 'usesses'
            return MI
      
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'asse'
            return MI
        else:
            MI = 'ássemos'
            return MI
    
    elif (padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'esse'
            return MI
        else:
            MI = 'êssemos'
            return MI
        
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'isse'
            return MI
        else:
            MI = 'íssemos'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'usesse'
            return MI
        else:
            MI = 'uséssemos'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'asse'
            return MI
        else:
            MI = 'ásseis'
            return MI
    
    elif ( 
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'esse'
            return MI
        else:
            MI = 'êsseis'
            return MI
        
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'onha'
            return MI
        else:
            MI = 'íssseis'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'usesse'
            return MI
        else:
            MI = 'usésseis'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'asse'
            return MI
        else:
            MI = 'assem'
            return MI
    
    elif ( 
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'esse'
            return MI
        else:
            MI = 'essem'
            return MI
    elif (padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'isse'
            return MI
        else:
            MI = 'issem'
            return MI
        
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'usesse'
            return MI
        else:
            MI = 'usessem'
            return MI



###subjuntivo_optativo 
def realização_transitoriedade_subjuntivo_optativo():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no subjuntivo_optativo , 
    dados  o padrão de morfologia, tipo de pessoa, e número.
    
    >>>
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()       
           
    
    if (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' 
        ):
       MI = 'ar'
       return MI
   
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' 
          ):
       MI = 'er'
       return MI
  
    elif (
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
         MI = 'ir'
         return MI
          
    elif (
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' 
           ):
       MI = 'user'
       return MI
   
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular': 
       
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'ares'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'eres'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'ires'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'user'
            return MI
       else:
            MI = 'useres'
            return MI
      
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'armos'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'ermos'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'irmos'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'user'
            return MI
       else:
            MI = 'usermos'
            return MI
    
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'ardes'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'erdes'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'irdes'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'user'
            return MI
       else:
            MI = 'userdes'
            return MI
    
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'arem'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'erem'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'irem'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'user'
            return MI
       else:
            MI = 'userem'
            return MI



############não_finito_concretizado
            
def realização_transitoriedade_não_finito_concretizado():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo  não_finito_concretizado, 
    dados  o padrão de morfologia, tipo de pessoa, e número.
    
    >>>
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()       
           
    
    if (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' 
        ):
       MI = 'ar'
       return MI
   
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' 
          ):
       MI = 'er'
       return MI
  
    elif (
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
         MI = 'ir'
         return MI
          
    elif (
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' 
           ):
       MI = 'or'
       return MI
   
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular': 
       
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'ares'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'eres'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'ires'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'or'
            return MI
       else:
            MI = 'ores'
            return MI
      
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'armos'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'ermos'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'irmos'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'or'
            return MI
       else:
            MI = 'ormos'
            return MI
    
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'ardes'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'erdes'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'irdes'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'or'
            return MI
       else:
            MI = 'ordes'
            return MI
    
    elif padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ar'
            return MI
        else:
            MI = 'arem'
            return MI
    
    elif padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'er'
            return MI
       else:
            MI = 'erem'
            return MI
    
    elif padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'ir'
            return MI
       else:
            MI = 'irem'
            return MI
        
    elif padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
       padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
       if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'or'
            return MI
       else:
            MI = 'orem'
            return MI
            
        
#######imperativo_I
    
def realização_transitoriedade_imperativo_I():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_I, 
    dados  o padrão de morfologia, tipo de pessoa, e número.
    
    >>>
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()       
           
    if (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'a'
            return MI
        else:
            MI = 'e'
            return MI
   
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
          ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'e'
            return MI
        else:
            MI = 'a'
            return MI
  
    elif (
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
         ):
        padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
        if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
            MI = 'õe'
            return MI
        else:
            MI = 'onha'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        
            MI = 'emos'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'
           ):
           MI = 'amos'
           return MI
   
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        
            MI = 'onhamos'
            return MI
        
    elif (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
        ):
        return 'Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida' 

 
    
#######imperativo_II (negativo)
            
def realização_transitoriedade_imperativo_II():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no imperativo_II, 
    dados  o padrão de morfologia, tipo de pessoa, e número.
    
    >>>
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()    
    
    
    if (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        
            MI = 'es'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'
            ):
        
            MI = 'a'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular'):
        
            MI = 'onha'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
            MI = 'es'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'
            ):
        
            MI = 'a'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
        
            MI = 'onha'
            return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'):
        
            MI = 'emos'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural'
            ):
        
            MI = 'amos'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'):
        
            MI = 'onhamos'
            return MI
     
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        
            MI = 'eis'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'
            ):
        
            MI = 'ais'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
        
            MI = 'onhais'
            return MI
      
    elif (padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        
            MI = 'em'
            return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
            ):
        
            MI = 'am'
            return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
        
            MI = 'onham'
            return MI
    
    elif (
        padrão_de_morfologia == '-AR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-ER' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-IR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
        padrão_de_morfologia == '-OR' and OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular'
        ):
        return 'Morfologias de imperativo não selecionam 1pessoa do singular, pois não se direcionam exclusivamente ao falante. Selecione uma opção válida' 
 
###gerúndio
def realização_transitoriedade_gerúndio():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no gerúndio, 
    dados  o padrão de morfologia.
    
    >>>
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
                
    
    
    if (padrão_de_morfologia == '-AR'):
        MI = 'ando'
        return MI
    
    elif (padrão_de_morfologia == '-ER'):
        MI = 'endo'
        return MI
    
    elif (padrão_de_morfologia == '-IR'):
        MI = 'indo'
        return MI
    
    elif (padrão_de_morfologia == '-OR'):
        MI = 'ondo'
        return MI
  
    
######particípio



def realização_transitoriedade_particípio():
    '''(str)->str
    Retorna o morfema que realiza a transitoriedade de um verbo no particípio, 
    dados  o padrão de morfologia, tipo de pessoa, e número.
    
    >>>realização_transitoriedade_particípio ()
    ''
    ''' 
    padrão_de_morfologia =  choice.Menu(['-AR','-ER','-IR', '-OR']).ask()
    OI_número = choice.Menu(['singular', 'plural']).ask()    
    gênero = choice.Menu(['masculino','feminino']).ask()
    
    if (padrão_de_morfologia == '-AR' and OI_número == 'singular' and gênero == 'feminino'):
        MI = 'ada'
        return MI
    
    elif (padrão_de_morfologia == '-AR' and OI_número == 'plural' and gênero == 'feminino'):
            MI = 'adas'
            return MI
    

    elif (padrão_de_morfologia == '-AR' and OI_número == 'singular' and gênero == 'masculino'):
        MI = 'ado'
        return MI
    

    elif (padrão_de_morfologia == '-AR' and OI_número == 'plural'and gênero == 'masculino'):
        MI = 'ados'
        return MI
     
    elif (
        padrão_de_morfologia == '-ER' and OI_número == 'singular' and gênero == 'masculino' or
        padrão_de_morfologia == '-IR' and OI_número == 'singular' and gênero == 'masculino'
          ):
        MI = 'ido'
        return MI   
    
    elif (
        padrão_de_morfologia == '-ER' and OI_número == 'plural' and gênero == 'masculino' or
        padrão_de_morfologia == '-IR' and OI_número == 'plural' and gênero == 'masculino'
          ):
        MI = 'idos'
        return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_número == 'singular' and gênero == 'feminino' or
        padrão_de_morfologia == '-IR' and OI_número == 'singular' and gênero == 'feminino'
        ):
        MI = 'ida'
        return MI
    
    elif (
        padrão_de_morfologia == '-ER' and OI_número == 'plural' and gênero == 'feminino' or
        padrão_de_morfologia == '-IR' and OI_número == 'plural' and gênero == 'feminino'
        ):
        MI = 'idas'
        return MI
    
    
    elif (padrão_de_morfologia == '-OR' and OI_número == 'singular' and gênero == 'feminino'):
        
        MI = 'osta'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_número == 'singular' and gênero == 'masculino'):
        MI = 'osto'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_número == 'plural' and gênero == 'feminino'):
        
        MI = 'ostas'
        return MI
    
    elif (padrão_de_morfologia == '-OR' and OI_número == 'plural' and gênero == 'masculino'):
        MI = 'ostos'
        return MI
    
    
            
def realização_transitoriedade_do_verbo ():
    '''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realização_transitoriedade_do_verbo ()
    'o'

    '''
    tipo_de_orientação = OI_tipo_de_orientação ()
    
    if tipo_de_orientação == 'infinitivo':
        MI = realização_transitoriedade_infinitivo ()
        return MI
    
    elif tipo_de_orientação == 'presente':
        MI = realização_transitoriedade_presente ()
        return MI

    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        MI = realização_transitoriedade_pretérito_perfectivo_I ()
        return MI
    
    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        MI = realização_transitoriedade_pretérito_perfectivo_II ()
        return MI
    
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        MI = realização_transitoriedade_pretérito_imperfectivo()
        return MI
    
    elif tipo_de_orientação == 'passado_volitivo':
        MI = realização_transitoriedade_passado_volitivo ()
        return MI

    elif tipo_de_orientação == 'futuro':
        MI = realização_transitoriedade_futuro()
        return MI
    
    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        MI = realização_transitoriedade_subjuntivo_conjuntivo()
        return MI
     
    elif tipo_de_orientação == 'subjuntivo_condicional':
        MI = realização_transitoriedade_subjuntivo_condicional()
        return MI
    
    elif tipo_de_orientação == 'subjuntivo_optativo':
        MI = realização_transitoriedade_subjuntivo_optativo()
        return MI
    
    elif tipo_de_orientação == 'não_finito_concretizado':
        MI = realização_transitoriedade_não_finito_concretizado()
        return MI
   
    elif tipo_de_orientação == 'imperativo_I':
        MI = realização_transitoriedade_imperativo_I()
        return MI
    
    elif tipo_de_orientação == 'imperativo_II':
        MI = realização_transitoriedade_imperativo_II()
        return MI
    
    elif tipo_de_orientação == 'gerúndio':
        MI = realização_transitoriedade_gerúndio()
        return MI
     
    elif tipo_de_orientação == 'particípio':
        MI = realização_transitoriedade_particípio()
        return MI


        







#FORMAÇÃO DO VERBO ###################


def formação_da_estrutura_do_verbo1 (): #O tipo_de_experiência
#aqui vai ter relação com o tipo de configuração
    '''
    (str) -> str

    Retorna um verbo flexionado dados OE_experiência_do_verbo,
    OI_orientação_interpessoal_do_verbo.

    >>> formação_da_estrutura_do_verbo ()
    'levo'
    >>>formação_da_estrutura_do_verbo ()
    'levei'
    '''




    OE_experiência_do_verbo = experiência_do_verbo ()
    OI_orientação_interpessoal_do_verbo = realização_transitoriedade_do_verbo ()

    return OE_experiência_do_verbo + OI_orientação_interpessoal_do_verbo


def formação_da_estrutura_do_verbo2 (): #O tipo_de_experiência
#aqui vai ter relação com o tipo de configuração
    '''
    (str) -> str

    Retorna um verbo flexionado dados OE_experiência_do_verbo,
    OI_orientação_interpessoal_do_verbo.

    >>> formação_da_estrutura_do_verbo ()
    'levo'
    >>>formação_da_estrutura_do_verbo ()
    'levei'
    '''




    OE_experiência_do_verbo = experiência_do_verbo2 ()
    OI_orientação_interpessoal_do_verbo = realização_transitoriedade_do_verbo ()

    return OE_experiência_do_verbo + OI_orientação_interpessoal_do_verbo




#################


def formação_verbo_estar_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'estar'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()
        
    

    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI = 'esse'
            verbo=ME + 'iv'+ MI
            return verbo
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'esses'
                verbo=ME + 'iv'+ MI
                return verbo
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'éssemos'
                verbo=ME +'iv'+ MI
                return verbo
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'ésseis'
                verbo=ME +'iv'+ MI
                return verbo

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'essem'
                verbo=ME +'iv'+ MI
                return verbo




    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                ME = verbo_lematizado[slice(-2)]
                MI = 'a'
                verbo=ME + 'ej' + MI
                return verbo
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'as'
                verbo=ME + 'ej' + MI
                return verbo
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'amos'
                verbo=ME + 'ej' + MI
                return verbo
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'ais'
                verbo=ME + 'ej' + MI
                return verbo
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'am'
                verbo=ME + 'ej' + MI
                return verbo

    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI
        return verbo

    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
                          
            else:
                MI  = 'á'
                verbo=ME + MI
                return verbo
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'a'
            verbo=ME + 'ej'+ MI
            return verbo
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                MI  = 'amos'
                verbo=ME + 'ej'+ MI
                return verbo
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI  = 'ai'
            verbo=ME + MI
            return verbo
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                MI  = 'am'
                verbo=ME + 'ej'+ MI
                return verbo



    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
                           
            else:
                MI  = 'as'
                verbo=ME + 'ej'+ MI
                return verbo
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]    
            MI  = 'a'
            verbo=ME + 'ej'+ MI
            return verbo
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                 MI = 'amos'
                 verbo=ME + 'ej'+ MI
                 return verbo
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                 MI = 'ais'
                 verbo=ME + 'ej'+ MI
                 return verbo
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                 MI = 'am'
                 verbo=ME + 'ej'+ MI
                 return verbo

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
                           
            else:
                MI  = 'eres'
                verbo=ME + 'iv'+ MI
                return verbo
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
            else:
                 MI = 'ermos'
                 verbo=ME + 'iv'+ MI
                 return verbo
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
            else:
                 MI = 'erdes'
                 verbo=ME + 'iv'+ MI
                 return verbo
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
            else:
                 MI = 'erem'
                 verbo=ME + 'iv'+ MI 
                 return verbo       
                        






    


def formação_verbo_estar_finito():
    '''            
    '''
    
    verbo_lematizado = 'estar'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()
    
    
    
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
        return verbo

    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
        return verbo
                    
    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
        return verbo

    
                
    

    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ou'
            verbo = ME + MI
            return verbo
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'á'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'ás'
               verbo=ME + MI
               return verbo
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'á'
            verbo = ME + MI
            return verbo
            

        elif (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
             OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
            ME = verbo_lematizado[slice(-2)]
            MI = realização_transitoriedade_presente()
            verbo=ME + MI
            return verbo

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ão'
            verbo = ME + MI
            return verbo
            
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ive'
           verbo=ME + MI
           return verbo
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'iveste'
               verbo=ME + MI
               return verbo
            
        
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'eve'
           verbo=ME + MI
           return verbo
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'ivemos'
               verbo=ME + MI
               return verbo
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'ivestes'
               verbo=ME + MI
               return verbo
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'iveram'
               verbo=ME + MI
               return verbo
                   



    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ivera'
           verbo=ME + MI
           return verbo
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'iveras'
               verbo=ME + MI
               return verbo
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ivera'
            verbo=ME + MI
            return verbo
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                return verbo
               
            else:
                MI  = 'ivéramos'
                verbo=ME + MI
                return verbo
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                return verbo
               
            else:
                MI  = 'ivéreis'
                verbo=ME + MI
                return verbo
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                return verbo
               
            else:
                MI  = 'iveram'
                verbo=ME + MI
                return verbo


def formação_verbo_estar():
    '''            
    '''
    
    verbo_lematizado = 'estar'
    
    
    tipo_de_orientação = OI_tipo_de_orientação()
        
    if tipo_de_orientação == 'infinitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_infinitivo()
        verbo=ME + MI
        return verbo
    
    
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
        return verbo

    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
        return verbo
                    
    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
        return verbo

    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ando'
        verbo= ME + MI
        return verbo
                
    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ado'
        verbo= ME + MI
        return verbo

    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ou'
            verbo = ME + MI
            return verbo
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'á'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'ás'
               verbo=ME + MI
               return verbo
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'á'
            verbo = ME + MI
            return verbo
            

        elif (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
             OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural'):
            ME = verbo_lematizado[slice(-2)]
            MI = realização_transitoriedade_presente()
            verbo=ME + MI
            return verbo

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ão'
            verbo = ME + MI
            return verbo
            
    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ive'
           verbo=ME + MI
           return verbo
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'iveste'
               verbo=ME + MI
               return verbo
            
        
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'eve'
           verbo=ME + MI
           return verbo
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'ivemos'
               verbo=ME + MI
               return verbo
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'ivestes'
               verbo=ME + MI
               return verbo
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'iveram'
               verbo=ME + MI
               return verbo
                   



    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ivera'
           verbo=ME + MI
           return verbo
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               return verbo
               
           else:
               MI  = 'iveras'
               verbo=ME + MI
               return verbo
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ivera'
            verbo=ME + MI
            return verbo
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                return verbo
               
            else:
                MI  = 'ivéramos'
                verbo=ME + MI
                return verbo
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                return verbo
               
            else:
                MI  = 'ivéreis'
                verbo=ME + MI
                return verbo
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                return verbo
               
            else:
                MI  = 'iveram'
                verbo=ME + MI
                return verbo


    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI = 'esse'
            verbo=ME + 'iv'+ MI
            return verbo
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'esses'
                verbo=ME + 'iv'+ MI
                return verbo
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'éssemos'
                verbo=ME +'iv'+ MI
                return verbo
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'ésseis'
                verbo=ME +'iv'+ MI
                return verbo

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'iv'+ MI
                return verbo
               
            else:
                MI  = 'essem'
                verbo=ME +'iv'+ MI
                return verbo




    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                ME = verbo_lematizado[slice(-2)]
                MI = 'a'
                verbo=ME + 'ej' + MI
                return verbo
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'as'
                verbo=ME + 'ej' + MI
                return verbo
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'amos'
                verbo=ME + 'ej' + MI
                return verbo
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'ais'
                verbo=ME + 'ej' + MI
                return verbo
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej' + MI
                return verbo
                   
            else:
                MI  = 'am'
                verbo=ME + 'ej' + MI
                return verbo

    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI
        return verbo

    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
                          
            else:
                MI  = 'á'
                verbo=ME + MI
                return verbo
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'a'
            verbo=ME + 'ej'+ MI
            return verbo
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                MI  = 'amos'
                verbo=ME + 'ej'+ MI
                return verbo
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI  = 'ai'
            verbo=ME + MI
            return verbo
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                MI  = 'am'
                verbo=ME + 'ej'+ MI
                return verbo



    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
                           
            else:
                MI  = 'as'
                verbo=ME + 'ej'+ MI
                return verbo
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]    
            MI  = 'a'
            verbo=ME + 'ej'+ MI
            return verbo
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                 MI = 'amos'
                 verbo=ME + 'ej'+ MI
                 return verbo
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                 MI = 'ais'
                 verbo=ME + 'ej'+ MI
                 return verbo
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ej'+ MI
                return verbo
            else:
                 MI = 'am'
                 verbo=ME + 'ej'+ MI
                 return verbo

    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
                           
            else:
                MI  = 'eres'
                verbo=ME + 'iv'+ MI
                return verbo
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
            else:
                 MI = 'ermos'
                 verbo=ME + 'iv'+ MI
                 return verbo
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
            else:
                 MI = 'erdes'
                 verbo=ME + 'iv'+ MI
                 return verbo
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                return verbo
            else:
                 MI = 'erem'
                 verbo=ME + 'iv'+ MI 
                 return verbo
    
   
    
  
                        



def formação_verbo_dizer_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'dizer'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()                        


    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           ME = verbo_lematizado[slice(-4)]
           MI = 'esse'
           verbo=ME + 'iss'+ MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iss'+ MI
               
           else:
               MI  = 'esses'
               verbo=ME + 'iss'+ MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iss'+ MI
               
           else:
               MI  = 'éssemos'
               verbo=ME +'iss'+ MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iss'+ MI
               
           else:
               MI  = 'ésseis'
               verbo=ME +'iss'+ MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iss'+ MI
               
           else:
               MI  = 'essem'
               verbo=ME +'iss'+ MI
               

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               ME = verbo_lematizado[slice(-3)]
               MI = 'a'
               verbo=ME + 'g' + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               ME = verbo_lematizado[slice(-3)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'a'
                   verbo=ME + 'g' + MI
                   
               else:
                   MI  = 'as'
                   verbo=ME + 'g' + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'g' + MI
                   
            else:
                MI  = 'amos'
                verbo=ME + 'g' + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'g' + MI
                 
            else:
                MI  = 'ais'
                verbo=ME + 'g' + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'g' + MI
                   
            else:
                MI  = 'am'
                verbo=ME + 'g' + MI



    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI    


    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'iga'
                verbo=ME + MI
                           
            else:
                MI  = 'iz'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'iga'
            verbo=ME + MI          
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='iga'
                verbo=ME + MI 
            else:
                MI  = 'igamos'
                verbo=ME + MI 
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'izei'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='iga'
                verbo=ME + MI 
            else:
                MI  = 'igam'
                verbo=ME +  MI    


    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'iga'
                verbo=ME + MI
                           
            else:
                MI  = 'igas'
                verbo=ME +  MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]    
            MI  = 'iga'
            verbo=ME + MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'iga'
                verbo=ME + MI
            else:
                 MI = 'amos'
                 verbo=ME + 'ig'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ig'+ MI
            else:
                 MI = 'ais'
                 verbo=ME + 'ig'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ig'+ MI
            else:
                 MI = 'am'
                 verbo=ME + 'ig'+ MI

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI  = 'er'
            verbo=ME + 'iv'+ MI
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
                           
            else:
                MI  = 'eres'
                verbo=ME + MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'ermos'
                 verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erdes'
                 verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erem'
                 verbo=ME + MI

    return verbo


def formação_verbo_dizer_finito():
    '''            
    '''
    
    verbo_lematizado = 'dizer'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()                        
    
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI = 'ia'
            verbo=ME + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ia'
                verbo=ME + MI
                   
            else:
                MI  = 'ias'
                verbo=ME + MI
              
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + MI
                   
            else:
                MI  = 'íamos'
                verbo=ME + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ia'
                verbo=ME + MI
                   
            else:
                MI  = 'íeis'
                verbo=ME + MI
                  
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ia'
                verbo=ME + MI
                   
            else:
                MI  = 'iam'
                verbo=ME + MI
        

    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-3)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + 'r' + MI
                    
    
    elif TIPO_OM_FINITA == 'passado_volitivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-4)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            MI = 'iria'
            verbo = ME  + MI
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI = 'iria'
                verbo = ME  + MI
            else:
                MI = 'irias'
                verbo = ME  + MI
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular': 
                MI = 'iria'
                verbo = ME  + MI
            else:
                MI = 'iríamos'
                verbo = ME  + MI
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular': 
                MI = 'iria'
                verbo = ME  + MI
            else:
                MI = 'iríeis'
                verbo = ME  + MI
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular': 
                MI = 'iria'
                verbo = ME  + MI
            else:
                MI = 'iriam'
                verbo = ME  + MI
             
    

    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-3)]
            MI = 'go'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = ''
               verbo=ME + MI
               
           else:
               MI  = 'es'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-3)]
            MI = 'em'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = ''
               verbo=ME + MI
               
            else:
               MI  = 'emos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = ''
               verbo=ME + MI
               
            else:
               MI  = 'eis'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = ''
               verbo=ME + MI
               
            else:
               MI  = 'em'
               verbo=ME + MI    




    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'isse'
           verbo=ME + MI
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'isse'
               verbo=ME + MI
               
           else:
               MI  = 'isseste'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'isse'
           verbo=ME + MI
           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'isse'
               verbo=ME + MI
               
           else:
               MI  = 'issemos'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'isse'
               verbo=ME + MI
               
           else:
               MI  = 'issestes'
               verbo=ME + MI
              
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'isse'
               verbo=ME + MI
               
           else:
               MI  = 'isseram'
               verbo=ME + MI
                 
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'issera'
           verbo=ME + MI
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'issera'
               verbo=ME + MI
               
           else:
               MI  = 'isseras'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'issera'
           verbo=ME + MI
           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'issera'
               verbo=ME + MI
               
           else:
               MI  = 'isséramos'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'issera'
               verbo=ME + MI
               
           else:
               MI  = 'isséreis'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'issera'
               verbo=ME + MI
               
           else:
               MI  = 'isseram'
               verbo=ME + MI

    return verbo

                        


def formação_verbo_ter_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'ter'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()                        
    
    


    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           ME = verbo_lematizado[slice(-2)]
           MI = 'esse'
           verbo=ME + 'iv'+ MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'esses'
               verbo=ME + 'iv'+ MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'éssemos'
               verbo=ME +'iv'+ MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'ésseis'
               verbo=ME +'iv'+ MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'essem'
               verbo=ME +'iv'+ MI
               

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               ME = verbo_lematizado[slice(-2)]
               MI = 'a'
               verbo=ME + 'enh' + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               ME = verbo_lematizado[slice(-2)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'a'
                   verbo=ME + 'enh' + MI
                   
               else:
                   MI  = 'as'
                   verbo=ME + 'enh' + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh' + MI
                   
            else:
                MI  = 'amos'
                verbo=ME + 'enh' + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh' + MI
                 
            else:
                MI  = 'ais'
                verbo=ME + 'enh' + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh' + MI
                   
            else:
                MI  = 'am'
                verbo=ME + 'enh' + MI



    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI    


    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'em'
                verbo=ME + MI
                           
            else:
                MI  = 'a'
                verbo=ME + 'enh'+ MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'a'
            verbo=ME + 'enh'+ MI          
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'enh'+ MI 
            else:
                MI  = 'amos'
                verbo=ME + 'enh'+ MI 
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI  = 'ende'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'enh'+ MI 
            else:
                MI  = 'am'
                verbo=ME + 'enh'+ MI    


    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME + 'enh'+ MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]    
            MI  = 'a'
            verbo=ME + 'enh'+ MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
            else:
                 MI = 'amos'
                 verbo=ME + 'enh'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
            else:
                 MI = 'ais'
                 verbo=ME + 'enh'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
            else:
                 MI = 'am'
                 verbo=ME + 'enh'+ MI

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI  = 'er'
            verbo=ME + 'iv'+ MI
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                           
            else:
                MI  = 'eres'
                verbo=ME + 'iv'+ MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
            else:
                 MI = 'ermos'
                 verbo=ME + 'iv'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
            else:
                 MI = 'erdes'
                 verbo=ME + 'iv'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
            else:
                 MI = 'erem'
                 verbo=ME + 'iv'+ MI

    return verbo
    
                        
                        
                           
 

def formação_verbo_ter_finito():
    '''            
    '''
    
    verbo_lematizado = 'ter'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()                        
    
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI = 'a'
            verbo=ME + 'inh'+ MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'as'
                verbo=ME + 'inh'+ MI
              
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'amos'
                verbo=ME + 'ính'+ MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'eis'
                verbo=ME + 'ính'+ MI
                  
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'am'
                verbo=ME + 'inh'+ MI
        

    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
                    
    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI

    

    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'enho'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
           else:
               MI  = 'ens'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'em'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'emos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'endes'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'êm'
               verbo=ME + MI    




    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ive'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'iveste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'eve'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'ivemos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'ivestes'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'iveram'
               verbo=ME + MI
               
               
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ivera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'iveras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ivera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'ivéramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'ivéreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'iveram'
               verbo=ME + MI


    

    return verbo
                            
    




def formação_verbo_ter():
    '''            
    '''
    
    verbo_lematizado = 'ter'
    
    
    tipo_de_orientação = OI_tipo_de_orientação()                        
    
    if tipo_de_orientação == 'infinitivo':
        verbo=verbo_lematizado
        
    
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-2)]
            MI = 'a'
            verbo=ME + 'inh'+ MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'as'
                verbo=ME + 'inh'+ MI
              
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'amos'
                verbo=ME + 'ính'+ MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'eis'
                verbo=ME + 'ính'+ MI
                  
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'inh'+ MI
                   
            else:
                MI  = 'am'
                verbo=ME + 'inh'+ MI
        

    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
                    
    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI

    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'endo'
        verbo= ME + MI
                
    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ido'
        verbo= ME + MI

    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'enho'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
           else:
               MI  = 'ens'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'em'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'emos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'endes'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'êm'
               verbo=ME + MI    




    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ive'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'iveste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'eve'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'ivemos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'ivestes'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eve'
               verbo=ME + MI
               
           else:
               MI  = 'iveram'
               verbo=ME + MI
               
               
    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ivera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'iveras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           MI = 'ivera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'ivéramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'ivéreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ivera'
               verbo=ME + MI
               
           else:
               MI  = 'iveram'
               verbo=ME + MI


    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           ME = verbo_lematizado[slice(-2)]
           MI = 'esse'
           verbo=ME + 'iv'+ MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'esses'
               verbo=ME + 'iv'+ MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'éssemos'
               verbo=ME +'iv'+ MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'ésseis'
               verbo=ME +'iv'+ MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'iv'+ MI
               
           else:
               MI  = 'essem'
               verbo=ME +'iv'+ MI
               

    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               ME = verbo_lematizado[slice(-2)]
               MI = 'a'
               verbo=ME + 'enh' + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               ME = verbo_lematizado[slice(-2)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'a'
                   verbo=ME + 'enh' + MI
                   
               else:
                   MI  = 'as'
                   verbo=ME + 'enh' + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh' + MI
                   
            else:
                MI  = 'amos'
                verbo=ME + 'enh' + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh' + MI
                 
            else:
                MI  = 'ais'
                verbo=ME + 'enh' + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh' + MI
                   
            else:
                MI  = 'am'
                verbo=ME + 'enh' + MI



    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI    


    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'em'
                verbo=ME + MI
                           
            else:
                MI  = 'a'
                verbo=ME + 'enh'+ MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'a'
            verbo=ME + 'enh'+ MI          
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'enh'+ MI 
            else:
                MI  = 'amos'
                verbo=ME + 'enh'+ MI 
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI  = 'ende'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'enh'+ MI 
            else:
                MI  = 'am'
                verbo=ME + 'enh'+ MI    


    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME + 'enh'+ MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]    
            MI  = 'a'
            verbo=ME + 'enh'+ MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
            else:
                 MI = 'amos'
                 verbo=ME + 'enh'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
            else:
                 MI = 'ais'
                 verbo=ME + 'enh'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'enh'+ MI
            else:
                 MI = 'am'
                 verbo=ME + 'enh'+ MI

    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
                           
            else:
                MI  = 'eres'
                verbo=ME + 'iv'+ MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
            else:
                 MI = 'ermos'
                 verbo=ME + 'iv'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
            else:
                 MI = 'erdes'
                 verbo=ME + 'iv'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iv'+ MI
            else:
                 MI = 'erem'
                 verbo=ME + 'iv'+ MI

    return verbo
    
    
    


def formação_verbo_ser_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'ser'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO() 

   
    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'osse'
           verbo=ME +  MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'osses'
               verbo=ME +  MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'ôssemos'
               verbo=ME +  MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'ôsseis'
               verbo=ME +  MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'ossem'
               verbo=ME +  MI    


    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_subjuntivo_conjuntivo()
        verbo=ME + 'ej'+ MI 
    
    
    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI    

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                MI = 'or'
                verbo=ME + MI
                                   
                               
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
                                  
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME + MI
                                       
            else:
                MI  = 'ores'
                verbo=ME + MI
                                       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
                                   
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME + MI
                                       
            else:
                MI  = 'ormos'
                verbo=ME + MI
                                      
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
                                   
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    MI  = 'or'
                    verbo=ME + MI
                                       
                else:
                    MI  = 'ordes'
                    verbo=ME + MI
                                     
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
                
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME + MI
                                       
            else:
                MI  = 'orem'
                verbo=ME + MI

    



    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]          
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
                           
            else:
                MI  = 'ê'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
            MI  = 'a'
            verbo=ME +'ej'+ MI        
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'amos'
                verbo=ME +'ej'+ MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI  = 'ede'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'am'
                verbo=ME +'ej'+ MI    

    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME +'ej'+ MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
            MI  = 'a'
            verbo=ME +'ej'+ MI        
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'amos'
                verbo=ME +'ej'+ MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI  = 'ais'
            verbo=ME +'ej'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'am'
                verbo=ME +'ej'+ MI
                        
                        
    return verbo




def formação_verbo_ser_finito():
    '''            
    '''
    
    verbo_lematizado = 'ser'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO() 

    
        
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = 'er'
            MI = 'a'
            verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = 'er'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + MI
               
            else:
               MI  = 'as'
               verbo=ME +  MI
          
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   ME = 'er'
                   MI  = 'a'
                   verbo=ME + MI
                   
            else:
                ME = 'ér'
                MI  = 'amos'
                verbo=ME + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
               
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = 'er'
                MI  = 'a'
                verbo=ME + MI
                   
            else:
                ME = 'ér'
                MI  = 'eis'
                verbo=ME +  MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'er'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                
                MI  = 'a'
                verbo=ME + MI
                   
            else:
              
                MI  = 'am'
                verbo=ME + MI    

    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI    

    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI

    

    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ou'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = ''
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'é'
               verbo=ME + MI
               
           else:
               MI  = 'és'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = ''
            MI = 'é'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = ''
                MI  = 'é'
                verbo=ME + MI
               
            else:
                ME = verbo_lematizado[slice(-2)]
                MI  = 'omos'
                verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ois'
            verbo = ME + MI
        
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = ''
                MI  = 'é'
                verbo=ME + MI
               
            else:
                ME = verbo_lematizado[slice(-2)]
                MI  = 'ão'
                verbo=ME + MI    

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           
           MI = 'ui'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'oi'
                verbo=ME + MI
               
            else:
                MI  = 'oste'
                verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            
            MI = 'oi'
            verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
          
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'oi'
                verbo=ME + MI
               
            else:
                MI  = 'omos'
                verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
          
            MI  = 'ostes'
            verbo=ME + MI
              
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'oi'
                verbo=ME + MI
               
            else:
                MI  = 'oram'
                verbo=ME + MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME= 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'ora'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oram'
               verbo=ME + MI    

                   
                        
    return verbo 




def formação_verbo_ser():
    '''            
    '''
    
    verbo_lematizado = 'ser'
    
    
    tipo_de_orientação = OI_tipo_de_orientação() 

    if tipo_de_orientação == 'infinitivo':
        verbo=verbo_lematizado
        
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = 'er'
            MI = 'a'
            verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = 'er'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + MI
               
            else:
               MI  = 'as'
               verbo=ME +  MI
          
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   ME = 'er'
                   MI  = 'a'
                   verbo=ME + MI
                   
            else:
                ME = 'ér'
                MI  = 'amos'
                verbo=ME + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
               
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = 'er'
                MI  = 'a'
                verbo=ME + MI
                   
            else:
                ME = 'ér'
                MI  = 'eis'
                verbo=ME +  MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'er'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                
                MI  = 'a'
                verbo=ME + MI
                   
            else:
              
                MI  = 'am'
                verbo=ME + MI    

    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI    

    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI

    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'endo'
        verbo= ME + MI

    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ido'
        verbo= ME + MI

    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ou'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = ''
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'é'
               verbo=ME + MI
               
           else:
               MI  = 'és'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = ''
            MI = 'é'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = ''
                MI  = 'é'
                verbo=ME + MI
               
            else:
                ME = verbo_lematizado[slice(-2)]
                MI  = 'omos'
                verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            MI = 'ois'
            verbo = ME + MI
        
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                ME = ''
                MI  = 'é'
                verbo=ME + MI
               
            else:
                ME = verbo_lematizado[slice(-2)]
                MI  = 'ão'
                verbo=ME + MI    

    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           
           MI = 'ui'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'oi'
                verbo=ME + MI
               
            else:
                MI  = 'oste'
                verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            
            MI = 'oi'
            verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
          
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'oi'
                verbo=ME + MI
               
            else:
                MI  = 'omos'
                verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
          
            MI  = 'ostes'
            verbo=ME + MI
              
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'oi'
                verbo=ME + MI
               
            else:
                MI  = 'oram'
                verbo=ME + MI

    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME= 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'ora'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oram'
               verbo=ME + MI    

    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'osse'
           verbo=ME +  MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'osses'
               verbo=ME +  MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'ôssemos'
               verbo=ME +  MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'ôsseis'
               verbo=ME +  MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'osse'
               verbo=ME +  MI
               
           else:
               MI  = 'ossem'
               verbo=ME +  MI    


    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_subjuntivo_conjuntivo()
        verbo=ME + 'ej'+ MI 
    
    
    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI    

    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                MI = 'or'
                verbo=ME + MI
                                   
                               
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
                                  
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME + MI
                                       
            else:
                MI  = 'ores'
                verbo=ME + MI
                                       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
                                   
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME + MI
                                       
            else:
                MI  = 'ormos'
                verbo=ME + MI
                                      
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
                                   
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    MI  = 'or'
                    verbo=ME + MI
                                       
                else:
                    MI  = 'ordes'
                    verbo=ME + MI
                                     
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
                
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME + MI
                                       
            else:
                MI  = 'orem'
                verbo=ME + MI

    



    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]          
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
                           
            else:
                MI  = 'ê'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
            MI  = 'a'
            verbo=ME +'ej'+ MI        
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'amos'
                verbo=ME +'ej'+ MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI  = 'ede'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'am'
                verbo=ME +'ej'+ MI    

    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME +'ej'+ MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
            MI  = 'a'
            verbo=ME +'ej'+ MI        
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'amos'
                verbo=ME +'ej'+ MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI  = 'ais'
            verbo=ME +'ej'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'ej'+ MI
            else:
                MI  = 'am'
                verbo=ME +'ej'+ MI
                        
                        
    return verbo                       
                        
                        
                        
                        
    
 

def formação_verbo_ir_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'ser'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()

      


    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
            MI = 'osse'
            verbo=ME +  MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
               
            else:
                MI  = 'osses'
                verbo=ME +  MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
               
            else:
                MI  = 'ôssemos'
                verbo=ME +  MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
               
            else:
                MI  = 'ôsseis'
                verbo=ME +  MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
                
            else:
                MI  = 'ossem'
                verbo=ME +  MI

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                ME = 'v'
                MI = 'á'
                verbo=ME + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'ás'
                verbo=ME +  MI
                  
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'amos'
                verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'ades'
                verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'ão'
                verbo=ME + MI



    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI


    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = 'v'
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                           
            else:
                MI  = 'ai'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = 'v'
            MI = 'á'
            verbo=ME + MI         
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='á'
                verbo=ME + MI
            else:
                MI  = 'amos'
                verbo=ME + MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = 'i'
            MI  = 'de'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='á'
                verbo=ME + MI 
            else:
                MI  = 'ão'
                verbo=ME + MI

    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'v'
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                           
            else:
                MI  = 'ás'
                verbo=ME +  MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
                
            MI  = 'á'
            verbo=ME +  MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME +  MI
            else:
                 MI = 'amos'
                 verbo=ME +  MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME +  MI
            else:
                 MI = 'ades'
                 verbo=ME +  MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME +  MI
            else:
                 MI = 'ão'
                 verbo=ME +  MI

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            
            MI  = 'or'
            verbo=ME+ MI
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
                           
            else:
                MI  = 'ores'
                verbo=ME+ MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
            else:
                 MI = 'ormos'
                 verbo=ME+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
            else:
                 MI = 'ordes'
                 verbo=ME+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
            else:
                 MI = 'orem'
                 verbo=ME+ MI   

    return verbo







def formação_verbo_ir_finito():
    '''            
    '''
    
    verbo_lematizado = 'ir'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()

    
        
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo= MI


    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI    
    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
    

    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = 'v'
            MI = 'ou'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = 'v'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ai'
               verbo=ME + MI
               
           else:
               MI  = 'vais'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = 'v'
            MI = 'ai'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ai'
                verbo=ME + MI
               
            else:
               MI  = 'amos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = 'i'
            MI = 'des'
            verbo = ME + MI
        
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ai'
               verbo=ME + MI
               
            else:
               MI  = 'am'
               verbo=ME + MI


    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = 'f'
           MI = 'ui'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'oste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = 'f'
           MI = 'oi'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'omos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'ostes'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'oram'
               verbo=ME + MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           ME = 'f'
           MI = 'ora'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oram'
               verbo=ME + MI   


      

    return verbo


   
    
                
    
    
    
    
def formação_verbo_ir():
    '''            
    '''
    
    verbo_lematizado = 'ir'
    
    
    tipo_de_orientação = OI_tipo_de_orientação() 

    if tipo_de_orientação == 'infinitivo':
        verbo=verbo_lematizado
        
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo= MI


    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI    
    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'indo'
        verbo= ME + MI
    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ido'
        verbo= ME + MI

    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = 'v'
            MI = 'ou'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = 'v'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ai'
               verbo=ME + MI
               
           else:
               MI  = 'vais'
               verbo=ME + MI
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = 'v'
            MI = 'ai'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ai'
                verbo=ME + MI
               
            else:
               MI  = 'amos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = 'i'
            MI = 'des'
            verbo = ME + MI
        
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ai'
               verbo=ME + MI
               
            else:
               MI  = 'am'
               verbo=ME + MI


    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = 'f'
           MI = 'ui'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'oste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = 'f'
           MI = 'oi'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'omos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'ostes'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'oi'
               verbo=ME + MI
               
           else:
               MI  = 'oram'
               verbo=ME + MI

    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           ME = 'f'
           MI = 'ora'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'ôreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = 'f'
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ora'
               verbo=ME + MI
               
           else:
               MI  = 'oram'
               verbo=ME + MI   


    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
            MI = 'osse'
            verbo=ME +  MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
               
            else:
                MI  = 'osses'
                verbo=ME +  MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
               
            else:
                MI  = 'ôssemos'
                verbo=ME +  MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
               
            else:
                MI  = 'ôsseis'
                verbo=ME +  MI    

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'osse'
                verbo=ME +  MI
                
            else:
                MI  = 'ossem'
                verbo=ME +  MI

    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                ME = 'v'
                MI = 'á'
                verbo=ME + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'ás'
                verbo=ME +  MI
                  
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'amos'
                verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'ades'
                verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                   
            else:
                MI  = 'ão'
                verbo=ME + MI



    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI


    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = 'v'
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                           
            else:
                MI  = 'ai'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = 'v'
            MI = 'á'
            verbo=ME + MI         
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='á'
                verbo=ME + MI
            else:
                MI  = 'amos'
                verbo=ME + MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = 'i'
            MI  = 'de'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = 'v'
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='á'
                verbo=ME + MI 
            else:
                MI  = 'ão'
                verbo=ME + MI

    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'v'
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                           
            else:
                MI  = 'ás'
                verbo=ME +  MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
                
            MI  = 'á'
            verbo=ME +  MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME +  MI
            else:
                 MI = 'amos'
                 verbo=ME +  MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME +  MI
            else:
                 MI = 'ades'
                 verbo=ME +  MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME +  MI
            else:
                 MI = 'ão'
                 verbo=ME +  MI

    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = 'f'
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            
            MI  = 'or'
            verbo=ME+ MI
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
                           
            else:
                MI  = 'ores'
                verbo=ME+ MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
            else:
                 MI = 'ormos'
                 verbo=ME+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
            else:
                 MI = 'ordes'
                 verbo=ME+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'or'
                verbo=ME+ MI
            else:
                 MI = 'orem'
                 verbo=ME+ MI   

    return verbo
    
    


def formação_verbo_vir_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'vir'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()
    
    
        


    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'iesse'
           verbo=ME +  MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iesse'
               verbo=ME +  MI
               
           else:
               MI  = 'iesses'
               verbo=ME +  MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iesse'
               verbo=ME +  MI
               
           else:
               MI  = 'iéssemos'
               verbo=ME +''+  MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':

               MI  = 'iésseis'
               verbo=ME +  MI
               
               

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iesse'
               verbo=ME +  MI
               
           else:
               MI  = 'iessem'
               verbo=ME +  MI


    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]    
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               
               MI = 'a'
               verbo=ME + 'enh'+ MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME + MI
                   
               else:
                   MI  = 'enhas'
                   verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME +  MI
                   
               else:
                   MI  = 'enhamos'
                   verbo=ME +  MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME + MI
                   
               else:
                   MI  = 'enhais'
                   verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME + MI
                   
               else:
                   MI  = 'enham'
                   verbo=ME + MI    



    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI



    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]          
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'em'
                verbo=ME + MI
                           
            else:
                MI  = 'a'
                verbo=ME +'enh'+ MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
            MI = 'a'
            verbo=ME + 'enh'+ MI         
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI
            else:
                MI  = 'enhamos'
                verbo=ME + MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI  = 'inde'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI 
            else:
                MI  = 'am'
                verbo=ME +'enh'+ MI    


    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME +'enh'+ MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
                
            MI  = 'a'
            verbo=ME +'enh'+ MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI
            else:
                 MI = 'amos'
                 verbo=verbo=ME +'enh'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=verbo=ME +'enh'+ MI
            else:
                 MI = 'ais'
                 verbo=verbo=ME +'enh'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=verbo=ME +'enh'+ MI
            else:
                 MI = 'am'
                 verbo=verbo=ME +'enh'+ MI


    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            
            MI  = 'ier'
            verbo=ME+ MI
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
                           
            else:
                MI  = 'ieres'
                verbo=ME+ MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
            else:
                 MI = 'iermos'
                 verbo=ME+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
            else:
                 MI = 'ierdes'
                 verbo=ME+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
            else:
                 MI = 'ierem'
                 verbo=ME+ MI
    return verbo
    






def formação_verbo_vir_finito():
    '''            
    '''
    
    verbo_lematizado = 'vir'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()
    
    
   
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            
            MI = 'inha'
            verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME +  MI
               
            else:
                MI  = 'inhas'
                verbo=ME +  MI
          
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME + MI
               
            else:
                MI  = 'ínhamos'
                verbo=ME +  MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME + MI
               
            else:
                MI  = 'ínheis'
                verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME + MI
               
            else:
                MI  = 'inham'
                verbo=ME + MI    


    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI   
    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
    
    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            
            MI = 'enho'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
           else:
               MI  = 'ens'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            
            MI = 'em'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'em'
                verbo=ME + MI
               
            else:
               MI  = 'imos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI = 'indes'
            verbo = ME + MI
        
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'êm'
               verbo=ME + MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           
           MI = 'im'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eio'
               verbo=ME + MI
               
           else:
               MI  = 'ieste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
           MI = 'eio'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eio'
               verbo=ME + MI
               
           else:
               MI  = 'iemos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           MI  = 'iestes'
           verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eio'
               verbo=ME + MI
               
           else:
               MI  = 'ieram'
               verbo=ME + MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'iera'
           verbo=ME +  MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME +  MI
               
           else:
               MI  = 'ieras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME +  MI
               
           else:
               MI  = 'iéramos'
               verbo=ME +  MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME +  MI
               
           else:
               MI  = 'iéreis'
               verbo=ME +  MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME + MI
               
           else:
               MI  = 'ieram'
               verbo=ME +  MI    


    
    return verbo
      



def formação_verbo_vir():
    '''            
    '''
    
    verbo_lematizado = 'vir'
    
    
    tipo_de_orientação = OI_tipo_de_orientação()
    if tipo_de_orientação == 'infinitivo':
        verbo=verbo_lematizado
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            
            MI = 'inha'
            verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME +  MI
               
            else:
                MI  = 'inhas'
                verbo=ME +  MI
          
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME + MI
               
            else:
                MI  = 'ínhamos'
                verbo=ME +  MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME + MI
               
            else:
                MI  = 'ínheis'
                verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'inha'
                verbo=ME + MI
               
            else:
                MI  = 'inham'
                verbo=ME + MI    


    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI   
    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'indo'
        verbo= ME + MI

    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'indo'
        verbo= ME + MI

    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            
            MI = 'enho'
            verbo = ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
           else:
               MI  = 'ens'
               verbo=ME + MI
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            
            MI = 'em'
            verbo = ME + MI 
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'em'
                verbo=ME + MI
               
            else:
               MI  = 'imos'
               verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI = 'indes'
            verbo = ME + MI
        
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'em'
               verbo=ME + MI
               
            else:
               MI  = 'êm'
               verbo=ME + MI

    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           
           MI = 'im'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eio'
               verbo=ME + MI
               
           else:
               MI  = 'ieste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
           MI = 'eio'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eio'
               verbo=ME + MI
               
           else:
               MI  = 'iemos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           MI  = 'iestes'
           verbo=ME + MI
             
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'eio'
               verbo=ME + MI
               
           else:
               MI  = 'ieram'
               verbo=ME + MI

    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'iera'
           verbo=ME +  MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME +  MI
               
           else:
               MI  = 'ieras'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME +  MI
               
           else:
               MI  = 'iéramos'
               verbo=ME +  MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME +  MI
               
           else:
               MI  = 'iéreis'
               verbo=ME +  MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iera'
               verbo=ME + MI
               
           else:
               MI  = 'ieram'
               verbo=ME +  MI    


    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
           
           MI = 'iesse'
           verbo=ME +  MI
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iesse'
               verbo=ME +  MI
               
           else:
               MI  = 'iesses'
               verbo=ME +  MI
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iesse'
               verbo=ME +  MI
               
           else:
               MI  = 'iéssemos'
               verbo=ME +''+  MI
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':

               MI  = 'iésseis'
               verbo=ME +  MI
               
               

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'iesse'
               verbo=ME +  MI
               
           else:
               MI  = 'iessem'
               verbo=ME +  MI


    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]    
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               
               MI = 'a'
               verbo=ME + 'enh'+ MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME + MI
                   
               else:
                   MI  = 'enhas'
                   verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME +  MI
                   
               else:
                   MI  = 'enhamos'
                   verbo=ME +  MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME + MI
                   
               else:
                   MI  = 'enhais'
                   verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
               
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'enha'
                   verbo=ME + MI
                   
               else:
                   MI  = 'enham'
                   verbo=ME + MI    



    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI



    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]          
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'em'
                verbo=ME + MI
                           
            else:
                MI  = 'a'
                verbo=ME +'enh'+ MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           
            MI = 'a'
            verbo=ME + 'enh'+ MI         
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI
            else:
                MI  = 'enhamos'
                verbo=ME + MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            MI  = 'inde'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI 
            else:
                MI  = 'am'
                verbo=ME +'enh'+ MI    


    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME +'enh'+ MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
                
            MI  = 'a'
            verbo=ME +'enh'+ MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME +'enh'+ MI
            else:
                 MI = 'amos'
                 verbo=verbo=ME +'enh'+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=verbo=ME +'enh'+ MI
            else:
                 MI = 'ais'
                 verbo=verbo=ME +'enh'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=verbo=ME +'enh'+ MI
            else:
                 MI = 'am'
                 verbo=verbo=ME +'enh'+ MI


    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        ME = verbo_lematizado[slice(-2)]
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            
            MI  = 'ier'
            verbo=ME+ MI
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
                           
            else:
                MI  = 'ieres'
                verbo=ME+ MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
            else:
                 MI = 'iermos'
                 verbo=ME+ MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
            else:
                 MI = 'ierdes'
                 verbo=ME+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ier'
                verbo=ME+ MI
            else:
                 MI = 'ierem'
                 verbo=ME+ MI
    return verbo
    






  
def formação_verbo_haver_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'haver'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()
    
   
    
    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
    
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
            ):
            ME = verbo_lematizado[slice(-4)]
            MI = realização_transitoriedade_subjuntivo_condicional ()
            verbo = ME + 'ouv'+ MI
              
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'ud'+ MI
                       
            else:
                MI  = 'éssemos'
                verbo=ME +'ouv'+ MI
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'ouv'+ MI
                       
            else:
                MI  = 'ésseis'
                verbo=ME +'ouv'+ MI
    
    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-4)]
            MI = 'a'
            verbo=ME + 'aj'+ MI
                       
               
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME + 'aj'+ MI
                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'amos'
                verbo=ME + 'aj'+ MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'ais'
                verbo=ME + 'aj'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'am'
                verbo=ME + 'aj'+ MI



    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI

    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()

        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'


        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI

            else:
                MI  = 'á'
                verbo=ME + MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'a'
            verbo=ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
            else:
                MI  = 'amos'
                verbo=ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'ei'
            verbo=ME + 'av'+ MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
            else:
                MI  = 'am'
                verbo=ME + 'aj'+ MI

    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()


        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI

            else:
                MI  = 'as'
                verbo=ME + 'aj'+ MI


        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'a'
            verbo=ME + 'aj'+ MI


        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + MI
            else:
                MI = 'amos'
                verbo = ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
            else:
                MI = 'ais'
                verbo = ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
            else:
                MI = 'am'
                verbo = ME + 'aj'+ MI

    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()


        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI

            else:
                MI  = 'eres'
                verbo=ME + MI


        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                MI = 'ermos'
                verbo = ME + MI

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                MI = 'erdes'
                verbo = ME + MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                MI = 'erem' 
                verbo = ME + MI
                 
    return verbo 



    
    
def formação_verbo_haver_finito():
    '''            
    '''
    
    verbo_lematizado = 'haver'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()
    
    
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
    
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
            
    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
            
    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
            
                    
   
          
    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
             
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ei'
            verbo = ME + MI
                
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                
            else:
                MI  = 'ás'
                verbo=ME + MI
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'á'
            verbo = ME + MI
            
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            padrão_morfologia = choice.Menu(['extendido','contraído']).ask()
            if padrão_morfologia == 'extendido':
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
               
                else:
                    ME = verbo_lematizado[slice(-2)]
                    MI  = 'emos'
                    verbo=ME + MI
            else:
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
                   
                else:
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'emos'
                    verbo=ME + MI
                        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            padrão_morfologia = choice.Menu(['extendido','contraído']).ask()
            if padrão_morfologia == 'extendido':
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
                   
                else:
                    ME = verbo_lematizado[slice(-2)]
                    MI  = 'eis'
                    verbo=ME + MI
            else:
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
                   
                else:
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'eis'
                    verbo=ME + MI
                
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ão'
            verbo = ME + MI
            
            
            
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'e'
            verbo=ME + 'ouv' + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'este'
                verbo=ME + 'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'e'
            verbo=ME + 'ouv' + MI
               
           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'emos'
                verbo=ME + 'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'estes'
                verbo=ME + 'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'eram'
                verbo=ME + 'ouv' + MI
        
        
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'era'
            verbo= ME +'ouv'+ MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'udera'
                verbo=ME +'ouv'+ MI
                   
            else:
               MI  = 'eras'
               verbo=ME +'ouv'+ MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'era'
            verbo=ME +'ouv'+ MI
               
           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'era'
                verbo=ME +'ouv' + MI
                
            else:
                MI  = 'éramos'
                verbo=ME +'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'era'
                verbo=ME +'ouv' + MI
                  
            else:
                MI  = 'éreis'
                verbo=ME +'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'era'
                verbo=ME +'ouv' + MI
                  
            else:
                MI  = 'eram'
                verbo=ME +'ouv' + MI
    
    
                 
    return verbo  



          
    
def formação_verbo_haver():
    '''            
    '''
    
    verbo_lematizado = 'haver'
    
    
    tipo_de_orientação = OI_tipo_de_orientação()
    if tipo_de_orientação == 'infinitivo':
        verbo=verbo_lematizado
    elif tipo_de_orientação == 'pretérito_imperfectivo':
    
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
            
    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
            
    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
            
                    
    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'endo'
        verbo= ME + MI
        
    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ido'
        verbo= ME + MI
          
    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
             
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ei'
            verbo = ME + MI
                
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'á'
                verbo=ME + MI
                
            else:
                MI  = 'ás'
                verbo=ME + MI
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'á'
            verbo = ME + MI
            
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            padrão_morfologia = choice.Menu(['extendido','contraído']).ask()
            if padrão_morfologia == 'extendido':
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
               
                else:
                    ME = verbo_lematizado[slice(-2)]
                    MI  = 'emos'
                    verbo=ME + MI
            else:
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
                   
                else:
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'emos'
                    verbo=ME + MI
                        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            padrão_morfologia = choice.Menu(['extendido','contraído']).ask()
            if padrão_morfologia == 'extendido':
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
                   
                else:
                    ME = verbo_lematizado[slice(-2)]
                    MI  = 'eis'
                    verbo=ME + MI
            else:
                padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
                if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'á'
                    verbo=ME + MI
                   
                else:
                    ME = verbo_lematizado[slice(-4)]
                    MI  = 'eis'
                    verbo=ME + MI
                
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ão'
            verbo = ME + MI
            
            
            
    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'e'
            verbo=ME + 'ouv' + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'este'
                verbo=ME + 'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'e'
            verbo=ME + 'ouv' + MI
               
           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'emos'
                verbo=ME + 'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'estes'
                verbo=ME + 'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'e'
                verbo=ME + 'ouv' + MI
                   
            else:
                MI  = 'eram'
                verbo=ME + 'ouv' + MI
        
        
    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'era'
            verbo= ME +'ouv'+ MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'udera'
                verbo=ME +'ouv'+ MI
                   
            else:
               MI  = 'eras'
               verbo=ME +'ouv'+ MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'era'
            verbo=ME +'ouv'+ MI
               
           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'era'
                verbo=ME +'ouv' + MI
                
            else:
                MI  = 'éramos'
                verbo=ME +'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'era'
                verbo=ME +'ouv' + MI
                  
            else:
                MI  = 'éreis'
                verbo=ME +'ouv' + MI
                   
            
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'era'
                verbo=ME +'ouv' + MI
                  
            else:
                MI  = 'eram'
                verbo=ME +'ouv' + MI
    
    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
    
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
            ):
            ME = verbo_lematizado[slice(-4)]
            MI = realização_transitoriedade_subjuntivo_condicional ()
            verbo = ME + 'ouv'+ MI
              
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'ud'+ MI
                       
            else:
                MI  = 'éssemos'
                verbo=ME +'ouv'+ MI
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'esse'
                verbo=ME + 'ouv'+ MI
                       
            else:
                MI  = 'ésseis'
                verbo=ME +'ouv'+ MI
    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-4)]
            MI = 'a'
            verbo=ME + 'aj'+ MI
                       
               
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'as'
                verbo=ME + 'aj'+ MI
                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'amos'
                verbo=ME + 'aj'+ MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'ais'
                verbo=ME + 'aj'+ MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
                           
            else:
                MI  = 'am'
                verbo=ME + 'aj'+ MI



    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI

    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()

        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'


        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI

            else:
                MI  = 'á'
                verbo=ME + MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'a'
            verbo=ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
            else:
                MI  = 'amos'
                verbo=ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'ei'
            verbo=ME + 'av'+ MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
            else:
                MI  = 'am'
                verbo=ME + 'aj'+ MI

    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()


        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI

            else:
                MI  = 'as'
                verbo=ME + 'aj'+ MI


        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'a'
            verbo=ME + 'aj'+ MI


        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + MI
            else:
                 MI = 'amos'
                 verbo = ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
            else:
                 MI = 'ais'
                 verbo = ME + 'aj'+ MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'aj'+ MI
            else:
                 MI = 'am'
                 verbo = ME + 'aj'+ MI

    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()


        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI

            else:
                MI  = 'eres'
                verbo=ME + MI


        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'ermos'
                 verbo = ME + MI

        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erdes'
                 verbo = ME + MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erem'
                 verbo = ME + MI
                 
    return verbo   
    


def formação_verbo_poder_não_finito():
    '''            
    '''
    
    verbo_lematizado = 'poder'
    
    
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO() 

    
               
           
    if TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
               ):
            ME = verbo_lematizado[slice(-4)]
            MI = realização_transitoriedade_subjuntivo_condicional ()
            verbo = ME + 'ud'+ MI
          
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'ud'+ MI
               
           else:
               MI  = 'éssemos'
               verbo=ME +'ud'+ MI
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'ud'+ MI
               
           else:
               MI  = 'ésseis'
               verbo=ME +'ud'+ MI
               
    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               ME = verbo_lematizado[slice(-4)]
               MI = 'ossa'
               verbo=ME + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossas'
                   verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossamos'
                   verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossais'
                   verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossam'
                   verbo=ME + MI
   
    
    
    
    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI
    
    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
                           
            else:
                MI  = 'ode'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ossa'
            verbo=ME + MI          
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='ossa'
            else:
                MI  = 'ossamos'
                verbo=ME + MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'odei'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='ossa'
            else:
                MI  = 'ossam'
                verbo=ME + MI
    
    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
                           
            else:
                MI  = 'ossas'
                verbo=ME + MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]    
            MI  = 'ossa'
            verbo=ME + MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
            else:
                 MI = 'ossamos'
                 verbo = ME + MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
            else:
                 MI = 'ossais'
                 verbo = ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
            else:
                 MI = 'ossam'
                 verbo = ME + MI        

    
    
    
    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
                           
            else:
                MI  = 'eres'
                verbo=ME + MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'ermos'
                 verbo = ME + MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erdes'
                 verbo = ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erem'
                 verbo = ME + MI


    return verbo





def formação_verbo_poder_finito():
    '''            
    '''
    
    verbo_lematizado = 'poder'
    
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO() 

    
    if TIPO_OM_FINITA == 'pretérito_imperfectivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
        
    elif TIPO_OM_FINITA == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
        
    elif TIPO_OM_FINITA == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
        
                
    
        
    elif TIPO_OM_FINITA == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            verbo = 'posso'
            
        
        elif (OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
               OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
            ME = verbo_lematizado[slice(-2)]
            MI = realização_transitoriedade_presente()
            verbo=ME + MI
            
    
    
        
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'ude'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'udeste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'ôde'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'udemos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'udestes'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'uderam'
               verbo=ME + MI
               
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'udera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'uderas'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'udera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'udéramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'udéreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'uderam'
               verbo=ME + MI
               
           
    

    return verbo        
  




def formação_verbo_poder():
    '''            
    '''
    
    verbo_lematizado = 'poder'
    
    
    tipo_de_orientação = OI_tipo_de_orientação() 

    if tipo_de_orientação == 'infinitivo':
        verbo=verbo_lematizado
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
        
    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_futuro()
        verbo=ME + MI
        
    elif tipo_de_orientação == 'passado_volitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_passado_volitivo()
        verbo=ME + MI
        
                
    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'endo'
        verbo= ME + MI
    
    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-2)]
        MI = 'ido'
        verbo= ME + MI
        
    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            verbo = 'posso'
            
        
        elif (OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural' or
               OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'):
            ME = verbo_lematizado[slice(-2)]
            MI = realização_transitoriedade_presente()
            verbo=ME + MI
            
    
    
        
    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'ude'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'udeste'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'ôde'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'udemos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'udestes'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ôde'
               verbo=ME + MI
               
           else:
               MI  = 'uderam'
               verbo=ME + MI
               
    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'udera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'uderas'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'udera'
           verbo=ME + MI
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'udéramos'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'udéreis'
               verbo=ME + MI
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'udera'
               verbo=ME + MI
               
           else:
               MI  = 'uderam'
               verbo=ME + MI
               
           
    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular' or
               OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural'
               ):
            ME = verbo_lematizado[slice(-4)]
            MI = realização_transitoriedade_subjuntivo_condicional ()
            verbo = ME + 'ud'+ MI
          
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'ud'+ MI
               
           else:
               MI  = 'éssemos'
               verbo=ME +'ud'+ MI
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'esse'
               verbo=ME + 'ud'+ MI
               
           else:
               MI  = 'ésseis'
               verbo=ME +'ud'+ MI
               
    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
           OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
               ME = verbo_lematizado[slice(-4)]
               MI = 'ossa'
               verbo=ME + MI
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossas'
                   verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossamos'
                   verbo=ME + MI
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossais'
                   verbo=ME + MI
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
               ME = verbo_lematizado[slice(-4)]
               padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
               if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                   MI  = 'ossa'
                   verbo=ME + MI
                   
               else:
                   MI  = 'ossam'
                   verbo=ME + MI
   
    
    
    
    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + MI
    
    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            return 'Imperativos não selecionam 1pessoa do singular'
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
                           
            else:
                MI  = 'ode'
                verbo=ME + MI
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ossa'
            verbo=ME + MI          
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='ossa'
            else:
                MI  = 'ossamos'
                verbo=ME + MI
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI  = 'odei'
            verbo=ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='ossa'
            else:
                MI  = 'ossam'
                verbo=ME + MI
    
    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print('Imperativos não selecionam 1pessoa do singular')
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
                           
            else:
                MI  = 'ossas'
                verbo=ME + MI
                       
                   
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]    
            MI  = 'ossa'
            verbo=ME + MI
                           
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
            else:
                 MI = 'ossamos'
                 verbo = ME + MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
            else:
                 MI = 'ossais'
                 verbo = ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ossa'
                verbo=ME + MI
            else:
                 MI = 'ossam'
                 verbo = ME + MI        

    
    
    
    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            verbo= verbo_lematizado
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-2)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
                           
            else:
                MI  = 'eres'
                verbo=ME + MI
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'ermos'
                 verbo = ME + MI
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erdes'
                 verbo = ME + MI
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-2)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + MI
            else:
                 MI = 'erem'
                 verbo = ME + MI


    return verbo



###################
def formação_verbo_fazer():
    '''            
    '''
    
    verbo_lematizado = 'fazer'
    
    
    tipo_de_orientação = OI_tipo_de_orientação()
        
    if tipo_de_orientação == 'infinitivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_infinitivo()
        verbo=ME + MI
        
    
    
    elif tipo_de_orientação == 'pretérito_imperfectivo':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_pretérito_imperfectivo()
        verbo=ME + MI
        

    elif tipo_de_orientação == 'futuro':
        ME = verbo_lematizado[slice(-3)]
        MI = realização_transitoriedade_futuro()[slice(1,5)]
        verbo=ME + MI
       
                    
    elif tipo_de_orientação == 'passado_volitivo':
        
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'aria'
            verbo = ME + MI
            
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'aria'
               verbo=ME + MI
               
               
           else:
               MI  = 'arias'
               verbo=ME + MI
               
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'aria'
            verbo = ME + MI
           
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
          
            ME = verbo_lematizado[slice(-4)]
            MI = 'aríamos'
            verbo=ME + MI
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI = 'aríeis'
            verbo=ME + MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ariam'
            verbo = ME + MI
            
        

    elif tipo_de_orientação == 'gerúndio':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_gerúndio()
        verbo= ME + MI
       
                
    elif tipo_de_orientação == 'particípio':
        ME = verbo_lematizado[slice(-4)]
        
        OI_número = choice.Menu(['singular', 'plural']).ask()    
        gênero = choice.Menu(['masculino','feminino']).ask()
        
        if OI_número == 'singular' and gênero == 'feminino':
            MI = 'eita'
            verbo = ME + MI
        
        elif OI_número == 'plural' and gênero == 'feminino':
            MI = 'eitas'
            verbo = ME + MI
        
    
        elif OI_número == 'singular' and gênero == 'masculino':
            MI = 'eito'
            verbo = ME + MI
        
    
        elif OI_número == 'plural'and gênero == 'masculino':
            MI = 'eitos'
            verbo = ME + MI
            

    elif tipo_de_orientação == 'presente':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
         
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-3)]
            MI = 'ço'
            verbo = ME + MI
            
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-2)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = ''
               verbo=ME + MI
               
               
           else:
               MI  = 'es'
               verbo=ME + MI
               
               
               
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'az'
            verbo = ME + MI
            
            

        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
          
            ME = verbo_lematizado[slice(-2)]
            MI = 'emos'
            verbo=ME + MI
            
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI = 'azeis'
            verbo=ME + MI

        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            MI = 'azem'
            verbo = ME + MI
        
      
            
    elif tipo_de_orientação == 'pretérito_perfectivo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'iz'
           verbo=ME + MI
           
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ez'
               verbo=ME + MI
               
               
           else:
               MI  = 'izeste'
               verbo=ME + MI
               
            
        
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'ez'
           verbo=ME + MI
           
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ez'
               verbo=ME + MI
               
               
           else:
               MI  = 'izemos'
               verbo=ME + MI
               
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ez'
               verbo=ME + MI
               
               
           else:
               MI  = 'izestes'
               verbo=ME + MI
               
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'ez'
               verbo=ME + MI
               
               
           else:
               MI  = 'izeram'
               verbo=ME + MI
    


    elif tipo_de_orientação == 'pretérito_perfectivo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           MI = 'izera'
           verbo=ME + MI
           
           
       
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
           ME = verbo_lematizado[slice(-4)]
           padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
           if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
               MI  = 'izera'
               verbo=ME + MI
               
               
           else:
               MI  = 'izeras'
               verbo=ME + MI
               
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            MI = 'izera'
            verbo=ME + MI
            
           
       
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'izera'
                verbo=ME + MI
                
               
            else:
                MI  = 'izéramos'
                verbo=ME + MI
                
               
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'izera'
                verbo=ME + MI
                
               
            else:
                MI  = 'izéreis'
                verbo=ME + MI
                
               
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'ivera'
                verbo=ME + MI
                
               
            else:
                MI  = 'izeram'
                verbo=ME + MI
                
    
    elif tipo_de_orientação == 'subjuntivo_condicional':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-4)]
            MI = 'izesse'
            verbo=ME + MI
            
        
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'izesse'
                verbo=ME + MI
                
               
            else:
                MI  = 'izesses'
                verbo=ME +  MI
                
                        
        
        elif  OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'izesse'
                verbo=ME + MI
                
               
            else:
                MI  = 'izéssemos'
                verbo=ME + MI
                
       
        elif  OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'izesse'
                verbo=ME + MI
                
               
            else:
                MI  = 'izésseis'
                verbo=ME + MI
                

        elif  OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'izesse'
                verbo=ME +  MI
                
               
            else:
                MI  = 'izessem'
                verbo=ME + MI
                
 
    elif tipo_de_orientação == 'subjuntivo_conjuntivo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
            
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
                ME = verbo_lematizado[slice(-3)]
                MI = 'a'
                verbo=ME + 'ç' + MI
                
               
           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ç' + MI
                
                   
            else:
                MI  = 'as'
                verbo=ME + 'ç' + MI
                
                   
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ç' + MI
                
                   
            else:
                MI  = 'amos'
                verbo=ME + 'ç' + MI
                
                   
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ç' + MI
                
                   
            else:
                MI  = 'ais'
                verbo=ME + 'ç' + MI
                
                 
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ç' + MI
                
                   
            else:
                MI  = 'am'
                verbo=ME + 'ç' + MI
   
    elif tipo_de_orientação == 'não_finito_concretizado':
        ME = verbo_lematizado[slice(-2)]
        MI = realização_transitoriedade_não_finito_concretizado()
        verbo=ME + 'az' + MI
   
 #####################   

    elif tipo_de_orientação == 'imperativo_I':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print ( 'Imperativos não selecionam 1pessoa do singular. Seleciona novamente:')
            formação_verbo_fazer()
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-3)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ç'+ MI
                
                          
            else:
                MI = 'z' 
                verbo=ME + MI
                
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-3)]
            MI = 'a'
            verbo=ME + 'ç'+ MI
            
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ç'+ MI
                
            else:
                MI  = 'amos'
                verbo=ME + 'ç'+ MI
                
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ç'+ MI
                
            else:
                MI  = 'ei'
                verbo=ME + 'z'+ MI
            
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ç'+ MI
                
            else:
                MI  = 'am'
                verbo=ME + 'ç'+ MI
                
###############
                
    elif tipo_de_orientação == 'imperativo_II':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
                  
        if OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular':
            print ( 'Imperativos não selecionam 1pessoa do singular. Selecione novamente:')
            formação_verbo_fazer()
            
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            ME = verbo_lematizado[slice(-3)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'a'
                verbo=ME + 'ç'+ MI
                
                          
            else:
                MI  = 'as'
                verbo=ME + 'ç'+ MI
                
        
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular':
            ME = verbo_lematizado[slice(-3)]
            MI = 'a'
            verbo=ME + 'ç'+ MI
            
                                                        
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ç'+ MI
                
            else:
                MI  = 'amos'
                verbo=ME + 'ç'+ MI
                
                           
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ç'+ MI
                
            else:
                MI='ais'
                verbo=ME + 'ç'+ MI
            
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-3)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI='a'
                verbo=ME + 'ç'+ MI
                
            else:
                MI  = 'am'
                verbo=ME + 'ç'+ MI   
                
    
    elif tipo_de_orientação == 'subjuntivo_optativo':
        OI_tipo_de_pessoa = choice.Menu(['1pessoa','2pessoa','3pessoa']).ask()
        OI_número = choice.Menu(['singular', 'plural']).ask()
        
        
        if (OI_tipo_de_pessoa == '1pessoa' and OI_número == 'singular' or
            OI_tipo_de_pessoa == '3pessoa' and OI_número == 'singular'):
            ME = verbo_lematizado[slice(-4)]
            MI  = 'er'
            verbo=ME + 'iz'+ MI
            
        if OI_tipo_de_pessoa == '2pessoa' and OI_número == 'singular':
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask() 
            ME = verbo_lematizado[slice(-4)]
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iz'+ MI
                
                           
            else:
                MI  = 'eres'
                verbo=ME + 'iz'+ MI
                
                       
                                                                           
        elif OI_tipo_de_pessoa == '1pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iz'+ MI
                
            else:
                 MI = 'ermos'
                 verbo=ME + 'iz'+ MI
                 
                 
        elif OI_tipo_de_pessoa == '2pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iz'+ MI
                
            else:
                 MI = 'erdes'
                 verbo=ME + 'iz'+ MI
                 
                         
        elif OI_tipo_de_pessoa == '3pessoa' and OI_número == 'plural':
            ME = verbo_lematizado[slice(-4)]
            padrão_pessoa_morfologia = choice.Menu(['Morfologia de 3pessoa do singular', 'Morfologia_padrão']).ask()
            if padrão_pessoa_morfologia == 'Morfologia de 3pessoa do singular':
                MI  = 'er'
                verbo=ME + 'iz'+ MI
                
            else:
                 MI = 'erem'
                 verbo=ME + 'iz'+ MI 
    return verbo              
    
   
    



#################################################################################
def formação_da_estrutura_do_verbo_lexical ():
    '''
    ''' 
    prompt="Qual é o verbo lematizado desejado?"
    verbo_lematizado = input(prompt)
    
    if verbo_lematizado=='estar':
        estrutura_do_verbo = formação_verbo_estar()
    elif verbo_lematizado=='ser':
        estrutura_do_verbo = formação_verbo_ser()
    elif verbo_lematizado=='ir':
        estrutura_do_verbo = formação_verbo_ir()
    elif verbo_lematizado=='vir':
        estrutura_do_verbo = formação_verbo_vir()
    elif verbo_lematizado=='haver':
        estrutura_do_verbo = formação_verbo_haver()
        
    else:
        ME =  (verbo_lematizado[slice (-2)])
        MI = realização_transitoriedade_do_verbo ()
        verbo=ME + MI
        estrutura_do_verbo = verbo
    
    return estrutura_do_verbo



def formação_da_estrutura_do_verbo_modal ():
    '''
    '''
    print("Qual é o verbo modal lematizado desejado?")
    
    tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
                                                        
    
    if tipo_de_modal == 'dever':
        ME = tipo_de_modal[slice(-2)]
        MI = realização_transitoriedade_do_verbo ()
        verbo=ME + MI
        
    
        
    elif tipo_de_modal == 'poder':
        verbo = formação_verbo_poder()


    elif tipo_de_modal == 'haver':
        verbo = formação_verbo_haver()
    
    return verbo


def formação_da_estrutura_do_verbo_auxiliar ():
    '''
    '''
    
    print("Qual é o verbo auxiliar lematizado desejado?")
    tipo_de_auxiliar = choice.Menu(['estar', 'ter','ir','vir','ser','haver']).ask()

    if tipo_de_auxiliar == 'estar':
        verbo = formação_verbo_estar()
                     
                     
    elif tipo_de_auxiliar == 'ter':
        verbo = formação_verbo_ter()


    elif tipo_de_auxiliar == 'haver':
        verbo = formação_verbo_haver()


    elif tipo_de_auxiliar == 'ir':
        verbo = formação_verbo_ir()

    elif tipo_de_auxiliar == 'vir':
       verbo = formação_verbo_vir() 

    elif tipo_de_auxiliar == 'ser':
        verbo = formação_verbo_ser()
    
    return verbo


def formação_verbo_particípio():
    prompt="Qual é o verbo lematizado desejado?"
    verbo_lematizado = input(prompt)
    
    ME = verbo_lematizado[slice(-2)]
    
    MI = realização_transitoriedade_particípio()
    verbo_particípio = ME + MI

    return verbo_particípio

def formação_verbo_gerúndio():
    prompt="Qual é o verbo lematizado desejado?"
    verbo_lematizado = input(prompt)
    
    ME = verbo_lematizado[slice(-2)]
    
    MI = realização_transitoriedade_gerúndio()
    verbo_gerúndio = ME + MI

    return verbo_gerúndio


def realização_transitoriedade_do_verbo_não_finito ():
    '''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realização_transitoriedade_do_verbo ()
    'o'

    '''
    TIPO_OM_NÃO_FINITA = OI_ORIENTAÇÃO_MODAL_NÃO_FINITO()
    
    
    
    
    
    if TIPO_OM_NÃO_FINITA == 'subjuntivo_conjuntivo':
        MI = realização_transitoriedade_subjuntivo_conjuntivo()
        return MI
     
    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_condicional':
        MI = realização_transitoriedade_subjuntivo_condicional()
        return MI
    
    elif TIPO_OM_NÃO_FINITA == 'subjuntivo_optativo':
        MI = realização_transitoriedade_subjuntivo_optativo()
        return MI
    
    elif TIPO_OM_NÃO_FINITA == 'não_finito_concretizado':
        MI = realização_transitoriedade_não_finito_concretizado()
        return MI
   
    elif TIPO_OM_NÃO_FINITA == 'imperativo_I':
        MI = realização_transitoriedade_imperativo_I()
        return MI
    
    elif TIPO_OM_NÃO_FINITA == 'imperativo_II':
        MI = realização_transitoriedade_imperativo_II()
        return MI
    
    




def realização_transitoriedade_do_verbo_finito ():
    '''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realização_transitoriedade_do_verbo ()
    'o'

    '''
    
    TIPO_OM_FINITA = OI_ORIENTAÇÃO_MODAL_FINITO()
    
    if TIPO_OM_FINITA == 'presente':
        MI = realização_transitoriedade_presente ()
        return MI

    elif TIPO_OM_FINITA == 'pretérito_perfectivo_I':
        MI = realização_transitoriedade_pretérito_perfectivo_I ()
        return MI
    
    elif TIPO_OM_FINITA == 'pretérito_perfectivo_II':
        MI = realização_transitoriedade_pretérito_perfectivo_II ()
        return MI
    
    elif TIPO_OM_FINITA == 'pretérito_imperfectivo':
        MI = realização_transitoriedade_pretérito_imperfectivo ()
        return MI
    
    elif TIPO_OM_FINITA == 'passado_volitivo':
        MI = realização_transitoriedade_passado_volitivo ()
        return MI

    elif TIPO_OM_FINITA == 'futuro':
        MI = realização_transitoriedade_futuro()
        return MI
    
    


def realização_transitoriedade_do_verbo_não_orientado ():
    '''( str)-> str

    Retorna o morfema que realiza a transitoriedade do verbo no português
    brasileiro.

    >>> realização_transitoriedade_do_verbo ()
    'o'

    '''
    tipo_de_orientação = OI_não_orientado()
    
    if tipo_de_orientação == 'infinitivo':
        MI = realização_transitoriedade_infinitivo ()
        return MI
    
        
    elif tipo_de_orientação == 'gerúndio':
        MI = realização_transitoriedade_gerúndio()
        return MI
     
    elif tipo_de_orientação == 'particípio':
        MI = realização_transitoriedade_particípio()
        return MI



def formação_da_estrutura_do_verbo_lexical_finito ():
    '''
    ''' 
    prompt="Qual é o verbo lematizado desejado?"
    verbo_lematizado = input(prompt)
    
    if verbo_lematizado=='estar':
        verbo = formação_verbo_estar_finito()
    elif verbo_lematizado=='ser':
        verbo = formação_verbo_ser_finito()
    elif verbo_lematizado=='ir':
        verbo = formação_verbo_ir_finito()
    elif verbo_lematizado=='vir':
        verbo = formação_verbo_vir_finito()
    elif verbo_lematizado=='haver':
        verbo = formação_verbo_haver_finito()
    elif verbo_lematizado == 'ter':
        verbo= formação_verbo_ter_finito()
    elif verbo_lematizado == 'dizer':
        verbo = formação_verbo_dizer_finito()
    else:
        ME = (verbo_lematizado[slice (-2)])
        MI = realização_transitoriedade_do_verbo_finito ()
        verbo=ME + MI
        
    
    return verbo


def formação_da_estrutura_do_verbo_lexical_não_finito ():
    '''
    ''' 
    prompt="Qual é o verbo lematizado desejado?"
    verbo_lematizado = input(prompt)
    
    if verbo_lematizado=='estar':
        verbo = formação_verbo_estar_não_finito()
    elif verbo_lematizado=='ser':
        verbo = formação_verbo_ser_não_finito()
    elif verbo_lematizado=='ir':
        verbo = formação_verbo_ir_não_finito()
    elif verbo_lematizado=='vir':
        verbo = formação_verbo_vir_não_finito()
    elif verbo_lematizado=='haver':
        verbo = formação_verbo_haver_não_finito()
    elif verbo_lematizado == 'ter':
        verbo = formação_verbo_ter_não_finito()
    elif verbo_lematizado == 'dizer':
        verbo = formação_verbo_dizer_não_finito()
    else:
        ME = (verbo_lematizado[slice (-2)])
        MI = realização_transitoriedade_do_verbo_não_finito ()
        verbo=ME + MI
        
    
    return verbo



def formação_da_estrutura_do_verbo_modal_não_finito ():
    '''
    '''
    print("Qual é o verbo modal lematizado desejado?")
    
    tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
                                                        
    
    if tipo_de_modal == 'dever':
        ME = tipo_de_modal[slice(-2)]
        MI = realização_transitoriedade_do_verbo_não_finito ()
        verbo=ME + MI
        
    
        
    elif tipo_de_modal == 'poder':
        verbo = formação_verbo_poder_não_finito ()


    elif tipo_de_modal == 'haver':
        verbo = formação_verbo_haver_não_finito ()
    
    return verbo


def formação_da_estrutura_do_verbo_modal_finito ():
    '''
    '''
    print("Qual é o verbo modal lematizado desejado?")
    
    tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
                                                        
    
    if tipo_de_modal == 'dever':
        ME = tipo_de_modal[slice(-2)]
        MI = realização_transitoriedade_do_verbo_finito ()
        verbo=ME + MI
        
    
        
    elif tipo_de_modal == 'poder':
        verbo = formação_verbo_poder_finito ()


    elif tipo_de_modal == 'haver':
        verbo = formação_verbo_haver_finito ()
    
    return verbo





def formação_da_estrutura_do_verbo_auxiliar_finito ():
    '''
    '''
    
    print("Qual é o verbo auxiliar lematizado desejado?")
    tipo_de_auxiliar = choice.Menu(['estar', 'ter','ir','vir','ser','haver']).ask()

    if tipo_de_auxiliar == 'estar':
        verbo = formação_verbo_estar_finito()
                     
                     
    elif tipo_de_auxiliar == 'ter':
        verbo = formação_verbo_ter_finito()


    elif tipo_de_auxiliar == 'haver':
        verbo = formação_verbo_haver_finito()


    elif tipo_de_auxiliar == 'ir':
        verbo = formação_verbo_ir_finito()

    elif tipo_de_auxiliar == 'vir':
       verbo = formação_verbo_vir_finito() 

    elif tipo_de_auxiliar == 'ser':
        verbo = formação_verbo_ser_finito()
    
    return verbo   



def formação_da_estrutura_do_verbo_auxiliar_não_finito ():
    '''
    '''
    
    print("Qual é o verbo auxiliar lematizado desejado?")
    tipo_de_auxiliar = choice.Menu(['estar', 'ter','ir','vir','ser','haver']).ask()

    if tipo_de_auxiliar == 'estar':
        verbo = formação_verbo_estar_não_finito()
                     
                     
    elif tipo_de_auxiliar == 'ter':
        verbo = formação_verbo_ter_não_finito()


    elif tipo_de_auxiliar == 'haver':
        verbo = formação_verbo_haver_não_finito()


    elif tipo_de_auxiliar == 'ir':
        verbo = formação_verbo_ir_não_finito()

    elif tipo_de_auxiliar == 'vir':
       verbo = formação_verbo_vir_não_finito() 

    elif tipo_de_auxiliar == 'ser':
        verbo = formação_verbo_ser_não_finito()
    
    return verbo           
    
     


def formação_verbo_não_orientado():
    '''            
    '''
    
    verbo_lematizado = input ('Qual é o verbo lematizado?')
    tipo_de_orientação = OI_não_orientado()
    
    if verbo_lematizado =='vir':
        
        if tipo_de_orientação == 'gerúndio':
            ME = verbo_lematizado[slice(-2)]
    
            MI = realização_transitoriedade_gerúndio()
            verbo = ME + MI
            
        
        elif tipo_de_orientação == 'particípio':
            ME = verbo_lematizado[slice(-2)]
            MI = 'indo'
            verbo= ME + MI
        
        elif tipo_de_orientação == 'infinitivo':
            verbo= verbo_lematizado
            
    elif verbo_lematizado =='dizer':
        if tipo_de_orientação == 'gerúndio':
            ME = verbo_lematizado[slice(-2)]
    
            MI = realização_transitoriedade_gerúndio()
            verbo = ME + MI
            
        
        elif tipo_de_orientação == 'particípio':
            ME = verbo_lematizado[slice(-4)]
            MI = 'ito'
            verbo= ME + MI
        
        elif tipo_de_orientação == 'infinitivo':
            verbo= verbo_lematizado
            
    else:
        if tipo_de_orientação == 'gerúndio':
            ME = verbo_lematizado[slice(-2)]
    
            MI = realização_transitoriedade_gerúndio()
            verbo = ME + MI
            
        elif tipo_de_orientação == 'particípio':
            ME = verbo_lematizado[slice(-2)]
    
            MI = realização_transitoriedade_particípio()
            verbo = ME + MI
        elif tipo_de_orientação == 'infinitivo':
            verbo= verbo_lematizado
    
    
    return verbo
         

############################################################################

            


#####VERBOS MODAIS



def verbo_modal():
    print("Qual é o verbo modal lematizado desejado?")
    
   

    tipo_de_modal = input("""
                                      0:poder
                                      1:dever
                                      2:haver
                                      

                       Escolha uma opção:""")
    
    if tipo_de_modal == '0':
        return 'poder'
    
    elif tipo_de_modal == '1':
        return 'dever'
    
    elif tipo_de_modal =='2':
        return 'haver'
        


###########################################################################
#########################################################################

def formação_da_estrutura_do_verbo_geral1 ():
    '''(str)->str
    
    Retorna a estrutura que realiza os verbos no português.
    
    '''
    
    
    classe_do_verbo = def_classe_de_verbo ()
    
    
    if classe_do_verbo == 'lexical':
        verbo = formação_da_estrutura_do_verbo_lexical ()
        
       
    elif classe_do_verbo == 'modal':
        verbo = formação_da_estrutura_do_verbo_modal ()
        
                         
    elif classe_do_verbo == 'auxiliar':
        verbo = formação_da_estrutura_do_verbo_auxiliar ()
    
    return verbo



###############


def verbo_geral2():
    '''(str)->str
    
    Retorna a estrutura que realiza os verbos no português.
    
    '''
    
    classe_do_verbo = def_classe_de_verbo ()
    print ('Qual a orientação interpessoal?')
    ORIENTAÇÃO =  choice.Menu(['orientado', 'não_orientado']).ask()
    
    if (classe_do_verbo == 'lexical' and ORIENTAÇÃO == 'não_orientado' or
        classe_do_verbo == 'modal' and ORIENTAÇÃO == 'não_orientado' or
        classe_do_verbo == 'auxiliar' and ORIENTAÇÃO == 'não_orientado'):
        
        verbo=formação_verbo_não_orientado()

    
    elif classe_do_verbo == 'lexical' and ORIENTAÇÃO == 'orientado':
        
        ORIENTAÇÃO_MODAL= choice.Menu(['finito', 'não_finito']).ask()
  
        if ORIENTAÇÃO_MODAL == 'finito':
            
            verbo = formação_da_estrutura_do_verbo_lexical_finito ()
            
        elif ORIENTAÇÃO_MODAL == 'não_finito': 
            verbo = formação_da_estrutura_do_verbo_lexical_não_finito ()
            
    
    elif classe_do_verbo == 'auxiliar' and ORIENTAÇÃO == 'orientado':
        ORIENTAÇÃO_MODAL= choice.Menu(['finito', 'não_finito']).ask()

        if ORIENTAÇÃO_MODAL == 'finito':
            
            verbo = formação_da_estrutura_do_verbo_auxiliar_finito ()
            
        elif ORIENTAÇÃO_MODAL == 'não_finito': 
            verbo = formação_da_estrutura_do_verbo_auxiliar_não_finito ()
            
    elif classe_do_verbo == 'modal' and ORIENTAÇÃO == 'orientado':
        ORIENTAÇÃO_MODAL= choice.Menu(['finito', 'não_finito']).ask()
        
        if ORIENTAÇÃO_MODAL == 'finito':
            
            verbo = formação_da_estrutura_do_verbo_modal_finito ()
            
        elif ORIENTAÇÃO_MODAL == 'não_finito': 
            verbo = formação_da_estrutura_do_verbo_modal_não_finito ()
           
    return verbo           






            




    
    
    
    


######ORDEM DO GRUPO#####
#    grupo verbal
def realização_de_TIPO_DE_EVENTO():
    '''
    '''
    print ('Qual é o tipo de evento?')
    TIPO_DE_EVENTO =  choice.Menu(['ser', 'fazer', 'sentir']).ask()
    
    if TIPO_DE_EVENTO == 'ser':
        prompt= 'Qual é o verbo lematizado?'
        verbo_lematizado = input (prompt)
        
            
    elif  TIPO_DE_EVENTO == 'fazer':
        prompt= 'Qual é o verbo lematizado?'
        verbo_lematizado = input (prompt)
    
    elif  TIPO_DE_EVENTO == 'sentir':
        prompt= 'Qual é o verbo lematizado?'
        verbo_lematizado = input (prompt)

    return verbo_lematizado

def realização_de_AGÊNCIA():
    '''
    '''
    print ('Qual de Agência?')
    AGÊNCIA =  choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não-agenciado']).ask()
    
    if AGÊNCIA == 'agenciado_passiva':
        print('Qual o verbo auxiliar de agência passiva desejado?')
        auxiliar_da_passiva =  choice.Menu(['ser', 'estar']).ask()
        if auxiliar_da_passiva == 'ser':
            verbo_auxiliar_da_passiva = formação_verbo_ser()
            verbo_lexical = formação_verbo_particípio()
        elif auxiliar_da_passiva == 'estar':
            verbo_auxiliar_da_passiva = formação_verbo_ser()
            verbo_lexical = formação_verbo_particípio()
        
        grupo_verbal_agência_passiva = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
    
        return grupo_verbal_agência_passiva
    
    elif AGÊNCIA == 'agenciado_ativa': 
    
        grupo_verbal_agência_ativa = formação_da_estrutura_do_verbo_geral() 
        return grupo_verbal_agência_ativa
    elif AGÊNCIA == 'não-agenciado':
        grupo_verbal_não_agenciado = formação_da_estrutura_do_verbo_geral()
        return grupo_verbal_não_agenciado
        
    
def realização_de_AGÊNCIA_passiva():
    '''
    '''
   
    print('Qual o verbo auxiliar de agência passiva desejado?')
    auxiliar_da_passiva =  choice.Menu(['ser', 'estar']).ask()
    if auxiliar_da_passiva == 'ser':
        verbo_auxiliar_da_passiva = formação_verbo_ser()
        verbo_lexical = formação_verbo_particípio()
    elif auxiliar_da_passiva == 'estar':
        verbo_auxiliar_da_passiva = formação_verbo_ser()
        verbo_lexical = formação_verbo_particípio()
    
    grupo_verbal_agência_passiva = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
    
    return grupo_verbal_agência_passiva
    
   
    
    
    
    
    
    
#partindo do sistema 
    
##para grupo verbal, fiz seleções nos sistemas de tempo secundário e agenciamento
    #pq as outras seleções já são feitas na ordem da palavra verba(ficaria redundante)


def grupo_verbal(): 
    '''()->str
    
    Retorna a estrutura que realiza o grupo verbal
    >>>grupo_verbal()
    'ando'
    >>>grupo_verbal()
    'estou andando'
    >>>grupo_verbal()
    'andava'
    '''

    print ('Qual a agência do GV?')
    AGÊNCIA =  choice.Menu(['agenciado_ativa', 'agenciado_passiva', 'não_agenciado', 'não_agenciado_voz_passiva']).ask()
    print ('Há a seleção de  tempo secundário')
    TEMPO_SECUNDÁRIO = choice.Menu(['-','1_reiteração', '2_reiterações','3_reiterações','4_reiterações']).ask()
    
    if (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '-' or
        AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '-'):
        print ('Selecione a finitude')
        FINITUDE = choice.Menu(['finito', 'não_finito', 'não_orientado' ]).ask()
        
        if FINITUDE == 'finito':
            grupo_verbal = formação_da_estrutura_do_verbo_lexical_finito ()
        
        elif FINITUDE == 'não_finito' :
            grupo_verbal = formação_da_estrutura_do_verbo_lexical_não_finito ()
        
        elif FINITUDE == 'não_orientado':   
            grupo_verbal = formação_verbo_não_orientado()
        
    elif (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '1_reiteração'or
          AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '1_reiteração'):
         
        grupo_verbal = verbo_geral2 () + ' ' + verbo_geral2 ()
    elif (AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '1_reiteração' or
          AGÊNCIA == 'não_agenciado_voz_passiva' and TEMPO_SECUNDÁRIO == '1_reiteração') :
        print('Qual o verbo auxiliar de agência passiva desejado?')
        auxiliar_da_passiva =  choice.Menu(['ser','estar']).ask()
        if auxiliar_da_passiva == 'ser':
            verbo_auxiliar_da_passiva = formação_verbo_ser()
            verbo_lexical = formação_verbo_particípio()
     
        elif auxiliar_da_passiva == 'estar':
            verbo_auxiliar_da_passiva = formação_verbo_estar()
            verbo_lexical = formação_verbo_particípio()
        
        grupo_verbal = verbo_auxiliar_da_passiva + ' ' + verbo_lexical
    
    elif (AGÊNCIA == 'agenciado_ativa'and TEMPO_SECUNDÁRIO == '2_reiterações' or
          AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '2_reiteração'):
        grupo_verbal = verbo_geral2 () + ' ' + verbo_geral2 () + ' ' + verbo_geral2 ()
    
    elif (AGÊNCIA == 'agenciado_passiva'and TEMPO_SECUNDÁRIO == '2_reiterações' or
          AGÊNCIA == 'não_agenciado_voz_passiva' and TEMPO_SECUNDÁRIO == '2_reiteração'):
         
        verbo1=verbo_geral2 ()
        verbos_passiva= realização_de_AGÊNCIA_passiva()
           
        grupo_verbal = verbo1 + ' ' + verbos_passiva
        
    
    elif  (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '3_reiterações' or
           AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '3_reiteração'):
         grupo_verbal = verbo_geral2 () + ' ' + verbo_geral2 () + ' ' + verbo_geral2 ()

    elif (AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '3_reiterações' or
          AGÊNCIA == 'não_agenciado_voz_passiva' and TEMPO_SECUNDÁRIO == '3_reiteração'):
         
        verbo1=verbo_geral2 ()
        verbo2=verbo_geral2 ()
        verbos_passiva= realização_de_AGÊNCIA_passiva()
        
           
        grupo_verbal = verbo1 + ' ' +  verbo2 + ' ' + verbos_passiva
    
    elif (AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '4_reiterações' or
          AGÊNCIA == 'não_agenciado' and TEMPO_SECUNDÁRIO == '4_reiteração'):
         grupo_verbal = verbo_geral2 () + ' ' + verbo_geral2 () + ' ' + verbo_geral2 ()

    elif (AGÊNCIA == 'agenciado_passiva' and TEMPO_SECUNDÁRIO == '4_reiterações' or
         AGÊNCIA == 'não_agenciado_voz_passiva' and TEMPO_SECUNDÁRIO == '4_reiteração'):
         
        verbo1=verbo_geral2 ()
        verbo2=verbo_geral2 ()
        verbo3=verbo_geral2 ()
        verbos_passiva = realização_de_AGÊNCIA_passiva()
           
        grupo_verbal = verbo1 + ' ' +  verbo2 + ' ' +  verbo3 + ' ' + verbos_passiva
    
    
    ######
    
    
    
    return grupo_verbal
        




def grupo_conjuntivo():
    '''
    '''
   
    modo_inserção = choice.Menu(['inserção_manual','inserção_menu']).ask()
    
    if modo_inserção == 'inserção_manual':
        conjunção = input ('Escreva a conjunção desejada:')
        
    elif modo_inserção == 'inserção_menu':
    
        print ('Qual o tipo de conjunção?')
        tipo_de_conjunção = choice.Menu (['paratática(linker)','hipotática(binder)']).ask()
    
        if tipo_de_conjunção == 'paratática(linker)':
            print ('Qual o tipo da conjunção paratática(linker)?')
            tipo_de_paratática = choice.Menu (['Aditiva','Adversativa','Conclusiva',
                                                 'Alternativa',
                                                 'Explicativa']).ask()
            if tipo_de_paratática == 'Aditiva':
                conjunção = choice.Menu(['e','mas ainda','mas também','nem']).ask()
           
            elif tipo_de_paratática == 'Adversativa':
                conjunção = choice.Menu(['contudo','entretanto','mas',
                                         'não obstante','no entanto',
                                         'porém','todavia']).ask()
                    
            elif tipo_de_paratática == 'Alternativa':# PRECISO VER COMO IMPLEMENTAR UM COMPLEXO COM ESTE TIPO
                conjunção = choice.Menu(['já','ou','ora',
                                         'quer']).ask()

            elif tipo_de_paratática == 'Conclusiva':
                conjunção = choice.Menu(['assim','então','logo',
                                         'por conseguinte','por isso',
                                         'portanto']).ask()
            
            elif tipo_de_paratática == 'Explicativa':
                conjunção = choice.Menu(['pois','porquanto','porque',
                                         'que']).ask()
    
        elif tipo_de_conjunção == 'hipotática(binder)':
            print ('Qual o tipo da conjunção hipotática(binder)?')
            tipo_de_hipotática = choice.Menu (['Causal','Concessiva','Condicional',
                                               'Conformativa','Final','Proporcional',
                                               'Temporal','Comparativa','Consecutiva',
                                               'Integrante', 'Relativa']).ask()
    
            if tipo_de_hipotática == 'Causal':
                conjunção = choice.Menu(['porque','pois','porquanto',
                                         'como','pois que','por isso que',
                                         'á que','uma vez que','visto que',
                                         'visto como','que']).ask()
        
        
            elif tipo_de_hipotática == 'Concessiva':
                conjunção = choice.Menu(['embora','conquanto','ainda que',
                                         'mesmo que','posto que','bem que',
                                         'se bem que','apesar de que','nem que',
                                         'que']).ask()
        
            
            elif tipo_de_hipotática == 'Condicional':
                conjunção = choice.Menu(['se','caso','quando',
                                         'conquanto que','salvo se','sem que',
                                         'dado que','desde que','a menos que',
                                         'a não ser que']).ask()
        
        
            elif tipo_de_hipotática == 'Conformativa':
                conjunção = choice.Menu(['conforme','como',''
                                         'segundo','consoante']).ask()
             
            elif tipo_de_hipotática == 'Final':
                conjunção = choice.Menu(['para que', 
                                        'a fim de que','porque', 
                                        'que']).ask()
            
        
            elif tipo_de_hipotática == 'Proporcional':
                conjunção = choice.Menu(['à medida que','ao passo que', 'à proporção que',
                                         'enquanto', 'quanto mais',
                                         'quanto menos']).ask()
            
        
            elif tipo_de_hipotática == 'Temporal':
                conjunção = choice.Menu(['quando','antes que',
                                         'depois que','até que','logo que',
                                         'sempre que','assim que','desde que',
                                         'todas as vezes que', 'cada vez que', 'apenas',
                                         'mal', 'desde que']).ask()
        
            elif tipo_de_hipotática == 'Comparativa':
                conjunção = choice.Menu(['mais que', 'mais do que',
                                         'menos que','maior que','menor que',
                                         'melhor que','pior que',
                                         'menos do que','maior do que',
                                         'menor do que','melhor do que',
                                         'pior do que']).ask()
        
            elif tipo_de_hipotática == 'Consecutiva':
                conjunção = choice.Menu(['De modo que','De maneira que']).ask()
        
            elif tipo_de_hipotática == 'Integrante':
                conjunção = choice.Menu(['que','se']).ask()
            
            elif tipo_de_hipotática == 'Relativa':
                conjunção = choice.Menu(['porque','pois','porquanto',
                                         'como','pois que','por isso que',
                                         'á que','uma vez que','visto que',
                                         'visto como','que']).ask()
        
       
        
    return conjunção

def conjunção_continuativa():
    
    '''
    '''
    print('Qual o modo de inserção da conjunção?')
    modo_inserção = choice.Menu(['inserção_manual','inserção_menu']).ask()
    
    if modo_inserção == 'inserção_manual':
        conjunção_continuativa = input ('Escreva o continuativo desejado:')
        
    elif modo_inserção == 'inserção_menu':
        print ('Escolha um continuativo:')
        conjunção_continuativa = input("""
                                 1:e 
                                 2:é 
                                 3:ah 
                                 4:mas 
                                 5:sim 
                                 6:bem 
                                 7:não 
                                 8:agora 
                                 9:então 
                                 10:pois é 
                                 11:tipo  
                                 12:tipo assim 
                                 13:ó 
                                 14:daí
                                 15:aí
                                 16:aí então  
                                 17:quer 
                                 18:dizer 
                                 19:assim
                                 20:em
                                 21:seguida 
                                 22:por fim 
                                 23:porque 
                                 24:porém 
                                 25:também
                                 26:é que 
                                 27:olha 
                                 
                                 
                                
                               Escolha uma opção:""")
            
        if conjunção_continuativa == '1':
            conjunção_continuativa = 'e'
        elif conjunção_continuativa == '2':
            conjunção_continuativa = 'é'
        elif conjunção_continuativa == '3':
            conjunção_continuativa = 'ah'
        elif conjunção_continuativa == '4':
            conjunção_continuativa = 'mas'
        elif conjunção_continuativa == '5':
            conjunção_continuativa = 'sim'
        elif conjunção_continuativa == '6':
            conjunção_continuativa = 'bem'
        elif conjunção_continuativa == '7':
            conjunção_continuativa = 'não'
        elif conjunção_continuativa == '8':
            conjunção_continuativa = 'agora'
        elif conjunção_continuativa == '9':
            conjunção_continuativa = 'então'
        elif conjunção_continuativa == '10':
            conjunção_continuativa = 'pois é'
        elif conjunção_continuativa == '11':
            conjunção_continuativa = 'tipo'
        elif conjunção_continuativa == '12':
            conjunção_continuativa = 'tipo assim '
        elif conjunção_continuativa == '13':
            conjunção_continuativa = 'ó'
        elif conjunção_continuativa == '14':
            conjunção_continuativa = 'daí'
        elif conjunção_continuativa == '15':
            conjunção_continuativa = 'aí'
        elif conjunção_continuativa == '16':
            conjunção_continuativa = 'aí então '
        elif conjunção_continuativa == '17':
            conjunção_continuativa = 'quer'
        elif conjunção_continuativa == '18':
            conjunção_continuativa = 'dizer'
        elif conjunção_continuativa == '19':
            conjunção_continuativa = 'assim'
        elif conjunção_continuativa == '20':
            conjunção_continuativa = 'em'
        elif conjunção_continuativa == '21':
            conjunção_continuativa = 'seguida'
        elif conjunção_continuativa == '22':
            conjunção_continuativa = 'por fim'
        elif conjunção_continuativa == '23':
            conjunção_continuativa = 'porque'
        elif conjunção_continuativa == '24':
            conjunção_continuativa = 'porém'
        elif conjunção_continuativa == '25':
            conjunção_continuativa = 'também'
        
        elif conjunção_continuativa == '26':
            conjunção_continuativa = 'é que'
        elif conjunção_continuativa == '27':
            conjunção_continuativa = 'olha'
    
    
    
    return conjunção_continuativa       

###ESSE TRECHO QUE SEGUE É PRA GUARDAR PRO CASO DE PRECISAR FICAR MAIS ESPECÍFICO NO GRUPO_VERBAL
#
#print ('Quais tempos secundários?')
#        TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro', 'tempo_secundário_não_orientado']).ask()
#        compilação_TEMPORAL = []
#    
#        
#        while  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'tempo_secundário_DT_presente' or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_passado'or  TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_DT_futuro' or TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL =='tempo_secundário_não_orientado':
#            compilação_TEMPORAL= [TEMPO_PRIMÁRIO,TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL]
#            TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL = choice.Menu(['NA','tempo_secundário_DT_presente','tempo_secundário_DT_passado','tempo_secundário_DT_futuro']).ask()
#            if TEMPO_SECUNDÁRIO_DÊIXIS_TEMPORAL == 'NA':
#                break
#    
#    
#        if AGÊNCIA == 'agenciado_ativa' and TEMPO_SECUNDÁRIO == '+':
#            grupo_verbal = verbo_geral2 () + ' ' + verbo_geral2 ()
#                
#    return  grupo_verbal
#    

# #####################################



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


######PALAVRAS NOMINAIS- SUBSTANTIVO



#NUMERATIVOS
    

#### A fazer para numerativos: Eu fiz apenas o de quantidade precisa absoluta ou
    #cardinais. Ainda falta fazer as outras classes de numerativos. Talvez até a
    #qualificação ainda faça os ordinais
    
  
def ordinal():
    '''
    '''
    num = str( input ('Qual o número?'))
    
    print('Qual o gênero?')
    
    gênero = choice.Menu(['M','F']).ask()
    
    if gênero == 'M':
        ordinal = num + 'º'
    else:
        ordinal = num + 'ª'
        
    
    return ordinal

def porcento():
    '''
    '''
    
    num = str( input ('Qual o número?'))
    
    porcento = num + '%'
    
    return porcento
    
    

def num_cardinal_1dig_extenso():
    
    número_extenso = input ('Escreva o número cardinal de unidade por extenso:')
    
    
    if número_extenso == 'dois' :
        gênero_do_numerativo = choice.Menu (['masculino', 'feminino']).ask()
       
        if gênero_do_numerativo== 'feminino':
        
            numerativo = número_extenso [slice (-3)] + 'uas'
        
        elif gênero_do_numerativo== 'masculino':
            numerativo = número_extenso
    elif número_extenso == 'um' :
        gênero_do_numerativo = choice.Menu (['masculino', 'feminino']).ask()
       
        if gênero_do_numerativo== 'feminino':
        
            numerativo = número_extenso + 'a'
        
        elif gênero_do_numerativo== 'masculino':
            numerativo = número_extenso
    else:
        numerativo = número_extenso
    
    return numerativo



def num_cardinal_2dig_extenso ():
    
   
    número_extenso = input ('Escreva o número cardinal de dezena por extenso:')
    
    numerativo = número_extenso
    
    return numerativo



def num_cardinal_3dig_extenso():
    
    número_extenso = input ('Escreva o número cardinal de centena por extenso:')
    
    if (número_extenso == 'duzentos' or número_extenso == 'trezentos' or
         número_extenso == 'quatrocentos' or número_extenso == 'quinhentos' or
         número_extenso == 'seiscentos' or número_extenso == 'setecentos' or 
         número_extenso == 'oitocentos' or número_extenso == 'novecentos'):
        
        gênero_do_numerativo = choice.Menu (['masculino', 'feminino']).ask()
       
        if gênero_do_numerativo== 'feminino':
        
            numerativo = número_extenso [slice (-2)] + 'as'
        
        elif gênero_do_numerativo== 'masculino':
            numerativo = número_extenso
    elif número_extenso =='cem':
        numerativo = número_extenso
    
    return numerativo


def num_cardinal_4dig_extenso (): #Número com 4 dígitos
    número_extenso = input ('Escreva o número cardinal de milhar por extenso:')
    
    if número_extenso == 'dois mil':
        gênero_do_numerativo = choice.Menu (['masculino', 'feminino']).ask()
        
        if gênero_do_numerativo == 'masculino':
            
            numerativo = número_extenso
    
        elif gênero_do_numerativo == 'feminino':
            
            numerativo = número_extenso [:1] + 'uas' + número_extenso [4:] 
        
    else:
        numerativo = número_extenso
        
    return numerativo


def num_cardinal_5dig_extenso ():  #Número com 5 dígitos
    número_extenso = input ('Escreva o número cardinal de milhar de cinco dígitos por extenso:')
    
    
    numerativo = número_extenso
        
    return numerativo
    

def num_cardinal_6dig_extenso():  #Número com 6 dígitos
    
    número_extenso = input ('Escreva o número cardinal de seis dígitos por extenso:')
    
    if (número_extenso == 'duzentos mil' or número_extenso == 'trezentos mil' or
         número_extenso == 'quatrocentos mil' or número_extenso == 'quinhentos mil' or
         número_extenso == 'seiscentos mil' or número_extenso == 'setecentos mil' or 
         número_extenso == 'oitocentos mil' or número_extenso == 'novecentos mil'):
        
        gênero_do_numerativo = choice.Menu (['masculino', 'feminino']).ask()
       
        if gênero_do_numerativo== 'feminino':
        
            numerativo = número_extenso [slice (-6)] + 'as mil'
        
        elif gênero_do_numerativo== 'masculino':
            numerativo = número_extenso
    
    
    return numerativo

def num_cardinal_extenso():
    
    print('Numeral por extenso ou numérico?')
    realização_cardinal = choice.Menu (['extenso', 'numérico']).ask()
    print ('Quantos dígitos tem o número?')
    dígitos = choice.Menu (['1', '2','3','4','5','6',]).ask()
    
    if (realização_cardinal == 'numérico' and dígitos == '1' or
        realização_cardinal == 'numérico' and dígitos == '2'  or
        realização_cardinal == 'numérico' and dígitos == '3' or
        realização_cardinal == 'numérico' and dígitos == '4') :
    
        num_cardinal_extenso = input ('Escreva o número cardinal ')
    
    elif (realização_cardinal == 'extenso' and dígitos == '1') :
    
        num_cardinal_extenso = num_cardinal_1dig_extenso()
    
    elif (realização_cardinal == 'extenso' and dígitos == '2') :
        
        print ('A dezena é inteira ou tem unidades?')
        composição_num_2dig = choice.Menu (['dezena_inteira', 'dezena+unidade']).ask()
    
        if composição_num_2dig == 'dezena_inteira':
            
            num_cardinal_extenso = num_cardinal_2dig_extenso ()
        
        else:
            
            num_cardinal_extenso = num_cardinal_2dig_extenso () + ' e ' + num_cardinal_1dig_extenso ()
         
    elif (realização_cardinal == 'extenso' and dígitos == '3'):
        
        print ('Centena inteira, centena + dezena inteira, ou centena + dezena + unidade?')
        composição_num_3dig = choice.Menu (['centena_inteira', 'centena+dezena_inteira', 'centena+dezena+unidade', 'centena+unidade']).ask()
        
        if composição_num_3dig == 'centena_inteira':
            
            num_cardinal_extenso = num_cardinal_3dig_extenso()
        
        elif composição_num_3dig == 'centena+dezena_inteira':
            
            centena = num_cardinal_3dig_extenso()
            
            if centena == 'cem':
                
                centena = centena [slice (-2)] + 'ento'
            
           
                num_cardinal_extenso = centena + ' e '+ num_cardinal_2dig_extenso()
            
            else:
                num_cardinal_extenso = centena + ' e '+ num_cardinal_2dig_extenso()
        
        elif composição_num_3dig == 'centena+dezena+unidade':
            
            centena = num_cardinal_3dig_extenso()
            if centena == 'cem':
                
                centena = centena [slice (-2)] + 'ento'
            
           
                num_cardinal_extenso = centena + ' e '+ num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()
            
            else:
                
                num_cardinal_extenso = centena + ' e '+ num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()
                
         
            
            
            
        elif composição_num_3dig == 'centena+unidade':
        
            centena = num_cardinal_3dig_extenso()
            
            if centena == 'cem':
                
                centena = centena [slice (-2)] + 'ento'
            
           
                num_cardinal_extenso = centena + ' e ' + num_cardinal_1dig_extenso()
            
            else:
                
                num_cardinal_extenso = centena +  ' e ' + num_cardinal_1dig_extenso()
            
        

    
    elif (realização_cardinal == 'extenso' and dígitos == '4'):
        
        print ('Escolha a composição do número:')
        composição_num_4dig = choice.Menu (['milhar_inteira',
                                            'milhar+unidade',
                                            'milhar+dezena_inteira',
                                            'milhar+dezena+unidade',
                                            'milhar+centena_inteira',
                                            'milhar+centena+dezena_inteira',
                                            'milhar+centena+dezena+unidade']).ask()
        
        
        if composição_num_4dig ==  'milhar_inteira':
            
            num_cardinal_extenso = num_cardinal_4dig_extenso()
        
        elif composição_num_4dig == 'milhar+unidade':
            
            num_cardinal_extenso = num_cardinal_4dig_extenso() + ' e ' + num_cardinal_1dig_extenso()
        
        elif composição_num_4dig == 'milhar+dezena_inteira':
            
            num_cardinal_extenso = num_cardinal_4dig_extenso() +' e '+ num_cardinal_2dig_extenso()
        

        
        elif composição_num_4dig == 'milhar+dezena+unidade':
            
            num_cardinal_extenso = num_cardinal_4dig_extenso() +' e '+ num_cardinal_2dig_extenso() + ' e ' + num_cardinal_1dig_extenso()
        
        elif composição_num_4dig == 'milhar+centena_inteira':
            
            num_cardinal_extenso = num_cardinal_4dig_extenso() +' e '+ num_cardinal_3dig_extenso()
         
        elif composição_num_4dig == 'milhar+centena+dezena_inteira':
            
            milhar = num_cardinal_4dig_extenso()
            centena =  num_cardinal_3dig_extenso()
            if centena == 'cem':
                centena = centena [slice (-2)] + 'ento'
            
            dezena = num_cardinal_2dig_extenso()
                        
            num_cardinal_extenso = milhar + ' ' + centena + ' e ' + dezena 

        elif composição_num_4dig == 'milhar+centena+dezena+unidade':
            
            milhar = num_cardinal_4dig_extenso()
            centena =  num_cardinal_3dig_extenso()
            if centena == 'cem':
                centena = centena [slice (-2)] + 'ento'
            
            dezena = num_cardinal_2dig_extenso()
            
            unidade = num_cardinal_1dig_extenso()
                        
            num_cardinal_extenso = milhar + ' ' + centena + ' e ' + dezena + ' e ' + unidade

    
    return num_cardinal_extenso
    
def Numerativo():
    '''
    '''
    print ('Há realização de Numerativo?')
    real_numerativo = choice.Menu(['sim', 'NA']).ask()
    
    if real_numerativo == 'NA':
        
        Numerativo = ''
        
    elif real_numerativo == 'sim':
        
        
        print ('Qual o tipo de Numerativo selecionado')
        função_Numerativo = choice.Menu (['quant_precisa_absoluta(cardinais)', 
                                           'quant_precisa_div/multi(fração/multiplicativos)', 
                                           'quant_imprecisa_pron_indef_numer',
                                           'quant_imprecisa_pron_indef_valor_alt_baixo',
                                           'ordem_lugar_preciso(ordinal)',
                                           'ordem_lugar_impreciso(posição_relativa'
                                          ]).ask()
        
        
        if função_Numerativo == 'ordem_lugar_preciso(ordinal)':
            Numerativo = ordinal()
            
        elif função_Numerativo == 'quant_precisa_div/multi(fração/multiplicativos)':
            print ('Qual o tipo?')
            tipo_precisa = choice.Menu(['porcentagem']).ask()
            
            if tipo_precisa == 'porcentagem':
                
                Numerativo = porcento()
                
        
        elif função_Numerativo == 'quant_precisa_absoluta(cardinais)':
            Numerativo = num_cardinal_extenso()
    
    return Numerativo
#    

###A palavra nominal que realiza o Ente no GRUPO NOMINAL- Flexiona para nos eixos:
#     Gênero, Número, Grau. Por enquanto, vou trabalhar apenas com Gênero e número.(ORDEM DA PALAVRA AINDA)
#COMECEI APENAS COM SUBSTANTIVOS QUE SÃO REGULARES NAS SUAS FLEXÕES: gato:gatos:gatas:

def detecção_experiência_do_substantivo (): ##dado o substantivo flexionado##
    '''(str,str,str)->

    Retorna o morfema que realiza a experiência em um substantivo, dados
    o substantivo flexionado, o gênero e o número.

    >>>detecção_experiência_do_substantivo ('', 'masculino', 'plural')
    'gat'
    '''
    raiz_experiencial_substantivo = ''
    substantivo = input ('Qual é o substantivo?')
    gênero = choice.Menu (['masculino', 'feminino']).ask()
    número = choice.Menu (['singular', 'plural']).ask()

    if gênero == 'masculino'  and número == 'singular':
        raiz_experiencial_substantivo = (substantivo[slice (-1)])
        return raiz_experiencial_substantivo

    elif gênero == 'feminino'  and número == 'singular':
        raiz_experiencial_substantivo = (substantivo[slice (-1)])
        return raiz_experiencial_substantivo

    elif gênero == 'masculino' and número == 'plural':
        raiz_experiencial_substantivo = (substantivo[slice (-2)])
        return raiz_experiencial_substantivo

    elif  gênero == 'feminino' and número == 'plural':
        raiz_experiencial_substantivo = (substantivo[slice (-2)])
        return raiz_experiencial_substantivo



#OS LEMAS QUE SERVIRÃO PARA  FUNÇÃO QUE SEGUE VIRÃO DA ANOTAÇÃO NA ONTOLOGIA: 
#        o que na ontologia tiver anotado como Thing, vai servir como um
##        banco lexical do qual o operador vai selecionar(não sei ainda se 
#        vai ser importado automaticamente ou se vou ter de inserir manualmente
#        )
        
    
def realização_experiência_do_substantivo (): ##dado o substantivo_lematizado- por enquanto, apenas para
    ##substantivos regulares, com foco em masculino-feminino, singular plural. Tenho que considerar desenvolver 
#    com relação aos diferentes tipos de radicais (primitivo, derivado, composto, simples...)
    '''(str)-> str

    Retorna o morfema que realiza a experiência em um substantivo, dado
    o substantivo lematizado.

    >>>realização_experiência_do_substantivo ()
    'gat'
    '''
    flexão_gênero_potencial = choice.Menu (['masculino/feminino', 'não_binário']).ask()
    substantivo_lematizado = input ('Qual é o substantivo lematizado?')
    
    if flexão_gênero_potencial == 'masculino/feminino':
        morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
    
    elif flexão_gênero_potencial == 'não_binário':
        morfema_experiencial_do_substantivo = substantivo_lematizado
    
    
    return  morfema_experiencial_do_substantivo





def realização_flexões_substantivos ():
    '''(str,str,str)->

    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do substantivo e os gênero e números desejados.

    >>>realização_flexões_substantivos ('', '', '')
    'os'
    '''

    
    gênero = choice.Menu (['masculino', 'feminino', 'não_binário']).ask()
    número = choice.Menu (['singular', 'plural']).ask()


    if gênero == 'masculino'  and número == 'singular':
        morfema_flexão_substantivo = 'o'
        

    elif gênero == 'feminino'  and número == 'singular':
        morfema_flexão_substantivo = 'a'
        

    elif gênero == 'masculino'  and número == 'plural':
        morfema_flexão_substantivo = 'os'
        

    elif gênero == 'feminino'  and número == 'plural':
        morfema_flexão_substantivo = 'as'
        
    
    elif gênero == 'não_binário' and número == 'singular':
       morfema_flexão_substantivo =  ''
       
    elif gênero == 'não_binário' and número == 'plural':
       morfema_flexão_substantivo =  's'
    
    return morfema_flexão_substantivo


###Com relação aos substantivos comuns tenho que ver a abordagem que vou tomar
#com relação aos substantivos não binários, ou inerentemente masculinos ou femininos. Me parece
#que o sistema se organiza a realizar o gênero em alguns casos na ordem da palavra, e em
#outros casos na ordem do grupo (mesa: não parece ter uma contrapartida masculina)


def formação_da_estrutura_do_substantivo_comum ():
    '''(str, str)-str

    Retorna a realização de um substantivo comum dados a experiência_do_substantivo
    e as flexões_desejadas.

    >>>formação_da_estrutura_do_substantivo_comum ()

    '''
    
  
    substantivo_lematizado = input ('Qual é o substantivo lematizado?')
    
    
    if substantivo_lematizado[-1:] == 'm':
        morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-1)]
        morfema_número = 'ns'
        substantivo_comum = morfema_experiencial_do_substantivo + morfema_número
          
   
    
    elif substantivo_lematizado[-2:] == 'ão':
        print ('Escolha o tipo de plural:')
        tipo_ão = choice.Menu (['ãos','ões','ães']).ask()
         
        morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
        morfema_número = tipo_ão
        substantivo_comum = morfema_experiencial_do_substantivo + morfema_número
          
        
    elif substantivo_lematizado[-1:] == 'x':
        substantivo_comum = substantivo_lematizado
        
    elif substantivo_lematizado[-1:] == 's':
        tonicidade = choice.Menu(['oxítona','paroxítona', 'proparoxítona']).ask()
        
        if tonicidade == 'paroxítona':
            substantivo_comum = substantivo_lematizado
        elif tonicidade =='oxítona':
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_número = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_número
            
            
            
    
    elif (substantivo_lematizado[-1:] == 'r' or substantivo_lematizado[-1:] == 'z') :
        print ('Qual o gênero')
        flexão_gênero_potencial = choice.Menu (['masculino' , 'feminino']).ask()
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if flexão_gênero_potencial == 'masculino' and número == 'singular': 
        
            substantivo_comum = substantivo_lematizado

        elif flexão_gênero_potencial == 'feminino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
  
            
        elif flexão_gênero_potencial == 'masculino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 'es'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo  
        
        
        elif flexão_gênero_potencial == 'não_binário'and número == 'singular' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
            
        elif flexão_gênero_potencial == 'não_binário'and número == 'plural' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
    
    
    
    elif substantivo_lematizado[-2:] == 'al':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado

        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexão_substantivo = 'ais'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
    elif substantivo_lematizado[-2:] == 'el':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-2)]
            morfema_flexão_substantivo = 'éis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo

    elif substantivo_lematizado[-2:] == 'il':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'is'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
       
    
    elif substantivo_lematizado[-2:] == 'ol':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'óis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo


    elif substantivo_lematizado[-2:] == 'ul':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'úis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
            
   
    
    elif substantivo_lematizado[-2:] == 'ul':
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        if  número == 'singular': 
        
            substantivo_comum = substantivo_lematizado 
    
        elif  número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado [slice(-2)]
            morfema_flexão_substantivo = 'úis'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    

    else:
    
        print ('Qual o gênero')
        flexão_gênero_potencial = choice.Menu (['masculino' , 'feminino', 'não_binário']).ask()
        print ('Qual o número')
        número = choice.Menu (['singular', 'plural']).ask()
        
        
        if flexão_gênero_potencial == 'masculino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'o'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'singular': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'a'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo   
            
        elif flexão_gênero_potencial == 'masculino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'os'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'plural': 
            morfema_experiencial_do_substantivo = substantivo_lematizado[slice(-1)]
            morfema_flexão_substantivo = 'as'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo  
        
        
        elif flexão_gênero_potencial == 'não_binário'and número == 'singular' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = ''
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
            
        elif flexão_gênero_potencial == 'não_binário'and número == 'plural' :
            morfema_experiencial_do_substantivo = substantivo_lematizado
            morfema_flexão_substantivo = 's'
            substantivo_comum = morfema_experiencial_do_substantivo + morfema_flexão_substantivo
        
    return substantivo_comum
        

    
    
#ADJETIVOS

def detecção_experiência_do_adjetivo (): ##dado o adjetivo flexionado##
    '''(str,str,str)->

    Retorna o morfema que realiza a experiência em um adjetivo, dados
    o adjetivo flexionado, o gênero e o número.

    >>>detecção_experiência_do_adjetivo ('', 'masculino', 'plural')
    'esportiv'
    '''
    raiz_experiencial_adjetivo= ''
    adjetivo = input ('Qual é o adjetivo?')
    gênero = choice.Menu (['masculino', 'feminino']).ask()
    número = choice.Menu (['singular', 'plural']).ask()

    if gênero == 'masculino'  and número == 'singular':
        raiz_experiencial_adjetivo = (adjetivo[slice (-1)])
        return raiz_experiencial_adjetivo

    elif gênero == 'feminino'  and número == 'singular':
        raiz_experiencial_adjetivo = (adjetivo[slice (-1)])
        return raiz_experiencial_adjetivo

    elif gênero == 'masculino' and número == 'plural':
        raiz_experiencial_adjetivo = (adjetivo[slice (-2)])
        return raiz_experiencial_adjetivo

    elif  gênero == 'feminino' and número == 'plural':
        raiz_experiencial_adjetivo = (adjetivo[slice (-2)])
        return raiz_experiencial_adjetivo

  
def realização_experiência_do_adjetivo (): 
    '''(str)-> str

    Retorna o morfema que realiza a experiência em um adjetivo, dado
    o adjetivo lematizado.

    >>>realização_experiência_do_adjetivo ()
    'gat'
    '''
    flexão_gênero_potencial = choice.Menu (['masculino/feminino', 'não_binário']).ask()
    adjetivo_lematizado = input ('Qual é o adjetivo lematizado?')
    
    if flexão_gênero_potencial == 'masculino/feminino':
        morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
    
    elif flexão_gênero_potencial == 'não_binário':
        morfema_experiencial_do_adjetivo = adjetivo_lematizado
    
    
    return  morfema_experiencial_do_adjetivo





def realização_flexões_adjetivos ():
    '''(str,str,str)->

    Retorna os morfemas que realizam as flexões de gênero e número dados
    a experiência do adjetivo e os gênero e números desejados.

    >>>realização_flexões_adjetivos ('', '', '')
    'os'
    '''

    
    gênero = choice.Menu (['masculino', 'feminino', 'não_binário']).ask()
    número = choice.Menu (['singular', 'plural']).ask()


    if gênero == 'masculino'  and número == 'singular':
        morfema_flexão_adjetivo = 'o'
        

    elif gênero == 'feminino'  and número == 'singular':
        morfema_flexão_adjetivo = 'a'
        

    elif gênero == 'masculino'  and número == 'plural':
        morfema_flexão_adjetivo = 'os'
        

    elif gênero == 'feminino'  and número == 'plural':
        morfema_flexão_adjetivo = 'as'
        
    
    elif gênero == 'não_binário' and número == 'singular':
       morfema_flexão_adjetivo =  ''
       
    elif gênero == 'não_binário' and número == 'plural':
       morfema_flexão_adjetivo =  's'
    
    return morfema_flexão_adjetivo




def adjetivo_modificador ():
    '''(str, str)-str

    Retorna a realização de um adjetivo comum dados a experiência_do_adjetivo
    e as flexões_desejadas.

    >>>estrutura_do_adjetivo ()

    '''
    print ('Há realização de adjetivo com funções de modificação (class, epítetos)?')
    real_modificadores = choice.Menu (['sim', 'NA']).ask()
    
    if real_modificadores == 'NA':
        
        modificador = ''
        
    else:    
  
        adjetivo_lematizado = input ('Qual é o adjetivo lematizado?')
        flexão_gênero_potencial = choice.Menu (['masculino' , 'feminino', 'não_binário']).ask()
        número = choice.Menu (['singular', 'plural']).ask()
        
        if flexão_gênero_potencial == 'masculino' and número == 'singular': 
            morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
            morfema_flexão_adjetivo = 'o'
            modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'singular': 
            morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
            morfema_flexão_adjetivo = 'a'
            modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo   
            
        elif flexão_gênero_potencial == 'masculino' and número == 'plural': 
            morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
            morfema_flexão_adjetivo = 'os'
            modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo
    
        elif flexão_gênero_potencial == 'feminino' and número == 'plural': 
            morfema_experiencial_do_adjetivo = adjetivo_lematizado[slice(-1)]
            morfema_flexão_adjetivo = 'as'
            modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo  
        
        
        elif flexão_gênero_potencial == 'não_binário'and número == 'singular' :
            morfema_experiencial_do_adjetivo = adjetivo_lematizado
            morfema_flexão_adjetivo = ''
            modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo
            
        elif flexão_gênero_potencial == 'não_binário'and número == 'plural' :
            morfema_experiencial_do_adjetivo = adjetivo_lematizado
            morfema_flexão_adjetivo = 's'
            modificador = morfema_experiencial_do_adjetivo + morfema_flexão_adjetivo
        
    return modificador


#PRONOMES#
    
    #PEGUEI OS PRONOMES BÁSICOS# QUANDO CHEGAR NA ORAÇÃO, A MORFOLOGIA DOS VERBOS
    #FICA UM POUCO SUBVERSIVA

def realização_pronominal_casoreto():
    '''(str)->str
    Retorna o pronome adequado dado uma pessoa da intelocução.

    >>>realização_pronominal_casoreto ('','')
    'eu'
    '''

    pessoa_da_interlocução = choice.Menu (['falante', 'ouvinte', 'não_interlocutor']).ask()

    número = choice.Menu (['singular', 'plural']).ask()

    if pessoa_da_interlocução == 'falante' and número == 'singular':
        pronome_pessoal_reto = 'eu'
        return pronome_pessoal_reto

    elif pessoa_da_interlocução == 'ouvinte' and número == 'singular':
        morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
        if morfologia_do_pronome =='padrão':
            pronome_pessoal_reto = 'tu'
        else:
            pronome_pessoal_reto = 'você'

    elif pessoa_da_interlocução == 'não_interlocutor' and número == 'singular':
        gênero = choice.Menu (['masculino', 'feminino']).ask()
        if gênero == 'masculino':
            pronome_pessoal_reto = 'ele'
            
        else:
            pronome_pessoal_reto = 'ela'
           
    elif pessoa_da_interlocução == 'falante' and número == 'plural':
        pronome_pessoal_reto = 'nós'
        

    elif pessoa_da_interlocução == 'ouvinte' and número == 'plural':
        morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
        if morfologia_do_pronome =='padrão':
            pronome_pessoal_reto = 'vós'
        else:
            pronome_pessoal_reto = 'vocês'

    elif pessoa_da_interlocução == 'não_interlocutor' and número == 'plural':
        gênero = choice.Menu (['masculino', 'feminino']).ask()
        if gênero == 'masculino':
            pronome_pessoal_reto = 'eles'
            
        else:
            pronome_pessoal_reto = 'elas'          
           
    return pronome_pessoal_reto



def realização_pronome_caso_oblíquo():
    '''(str)->str
    Retorna o pronome oblíquo adequado dado uma pessoa da intelocução.

    >>>realização_pronominal_caso_oblíquo ()
    'me'
    '''
    tonicidade = choice.Menu (['átono','tônico']).ask()
    
    pessoa_da_interlocução = choice.Menu (['falante', 'ouvinte', 'não_interlocutor']).ask()

    número = choice.Menu (['singular', 'plural']).ask()
    
    

    if pessoa_da_interlocução == 'falante' and número == 'singular' and tonicidade == 'átono':
        pronome_pessoal_oblíquo = 'me'
    
    elif pessoa_da_interlocução == 'ouvinte' and número == 'singular'and tonicidade == 'átono':
       pronome_pessoal_oblíquo = 'te'

    elif pessoa_da_interlocução == 'não_interlocutor' and número == 'singular' and tonicidade == 'átono':
        morfologia_do_pronome = choice.Menu (['padrão', 'não_padrão']).ask()
        
        
        if morfologia_do_pronome == 'padrão' :
            gênero = choice.Menu (['masculino', 'feminino','não_binário']).ask()
            
            if gênero =='masculino':
                pronome_pessoal_oblíquo = 'o'
            
            elif  gênero == 'feminino':    
                pronome_pessoal_oblíquo = 'a'
        
            else:
                pronome_pessoal_oblíquo = choice.Menu (['se','lhe']).ask()
        elif morfologia_do_pronome == 'não_padrão':
            gênero = choice.Menu (['masculino', 'feminino']).ask()
            
            if gênero == 'masculino':
                pronome_pessoal_oblíquo='ele'
            else:
                pronome_pessoal_oblíquo='ela'
                
    elif pessoa_da_interlocução == 'falante' and número == 'plural' and tonicidade == 'átono':
        pronome_pessoal_oblíquo = 'nos'
    
    elif pessoa_da_interlocução == 'ouvinte' and número == 'plural'and tonicidade == 'átono':
       pronome_pessoal_oblíquo = 'vos'

    elif pessoa_da_interlocução == 'não_interlocutor' and número == 'plural' and tonicidade == 'átono':
        morfologia_do_pronome = choice.Menu (['padrão', 'não_padrão']).ask()
        
        
        if morfologia_do_pronome == 'padrão' :
            gênero = choice.Menu (['masculino', 'feminino','não_binário']).ask()
            
            if gênero =='masculino':
                pronome_pessoal_oblíquo = 'os'
            
            elif  gênero == 'feminino':    
                pronome_pessoal_oblíquo = 'as'
        
            else:
                pronome_pessoal_oblíquo = choice.Menu (['se','lhes']).ask()
        elif morfologia_do_pronome == 'não_padrão':
            gênero = choice.Menu (['masculino', 'feminino']).ask()
            
            if gênero == 'masculino':
                pronome_pessoal_oblíquo='eles'
            else:
                pronome_pessoal_oblíquo='elas'            
         
    elif pessoa_da_interlocução == 'falante' and número == 'singular' and tonicidade == 'tônico':
        pronome_pessoal_oblíquo = 'mim'
    
    elif pessoa_da_interlocução == 'ouvinte' and número == 'singular'and tonicidade == 'tônico':
        morfologia_do_pronome = choice.Menu (['padrão', 'não_padrão']).ask()
        if morfologia_do_pronome == 'padrão':
           pronome_pessoal_oblíquo = 'ti'
        else:
            pronome_pessoal_oblíquo = 'você'

    elif pessoa_da_interlocução == 'não_interlocutor' and número == 'singular' and tonicidade == 'tônico':
       
        gênero = choice.Menu (['masculino', 'feminino','não_binário']).ask()
        
        if gênero =='masculino':
            pronome_pessoal_oblíquo = 'ele'
        
        elif  gênero == 'feminino':    
            pronome_pessoal_oblíquo = 'ela'
    
        
        elif gênero == 'não_binário':
            pronome_pessoal_oblíquo = 'si'
        
    elif pessoa_da_interlocução == 'falante' and número == 'plural' and tonicidade == 'tônico':
        pronome_pessoal_oblíquo = 'nós'
    
    elif pessoa_da_interlocução == 'ouvinte' and número == 'plural'and tonicidade == 'tônico':
        morfologia_do_pronome = choice.Menu (['padrão', 'não_padrão']).ask()
        
        if morfologia_do_pronome == 'padrão':
           pronome_pessoal_oblíquo = 'vós'
        else:
            pronome_pessoal_oblíquo = 'vocês'
        

    elif pessoa_da_interlocução == 'não_interlocutor' and número == 'plural' and tonicidade == 'tônico':
       
        gênero = choice.Menu (['masculino', 'feminino','não_binário']).ask()
        
        if gênero =='masculino':
            pronome_pessoal_oblíquo = 'eles'
        
        elif  gênero == 'feminino':    
            pronome_pessoal_oblíquo = 'elas'
    
        
        elif gênero == 'não_binário':
            pronome_pessoal_oblíquo = 'si'
                
           
    return pronome_pessoal_oblíquo 





def pronome_relativo():
    '''
    '''
    modo_inserção = choice.Menu(['inserção_manual','inserção_menu']).ask()
    
    if modo_inserção == 'inserção_manual':
        pronome_relativo = input ('Escreva o pronome desejado:')
        
    elif modo_inserção == 'inserção_menu':
       
        print('Qual tipo de relativo?')
        tipo_pronome_relativo = choice.Menu (['variável','invariável']).ask()
        if tipo_pronome_relativo == 'variável':
            
            print ('Qual o gênero?')
            gênero = choice.Menu(['masculino','feminino']).ask()
            print('Qual o número?')
            número= choice.Menu(['singular','plural']).ask()
        
        
            if gênero == 'masculino' and número =='singular':
                pronome_relativo = choice.Menu(['o qual','cujo','quanto', 'pelo quai']).ask()
            
            elif gênero == 'masculino' and número =='plural':
                pronome_relativo = choice.Menu(['os quais','cujos','quantos', 'pelos quais']).ask()
            
            elif gênero == 'feminino' and número =='singular':
                pronome_relativo = choice.Menu(['a qual','cuja','quanta', 'pela qual']).ask()
            
            elif gênero == 'feminino' and número =='plural':
                pronome_relativo = choice.Menu(['as quais','cujas','quantas', 'pelas quais']).ask()
            
        elif tipo_pronome_relativo == 'invariável':
            pronome_relativo = choice.Menu(['quem','que',
                                            'a quem','a que','porque','como']).ask()
                
    return pronome_relativo 
 
        
##PRECISO IMPLEMENTAR LETRA MAIÚSCULA NO CASO DE INICIO DE FRASE.
#SUBSTANTIVOS PRÓPRIOS VIRÃO DA LISTA DE NOMES PRÓPRIOS ANOTADOS NA GUM
#Por enquanto, vou deixar um input



def nome_próprio ():
    '''(str)->str
    Retorna o nome próprio. #Futuramente parte das listas de léxicos
    advindas da anotação na GUM.
    '''
    nome_próprio = input ('Qual é o nome próprio?')
    return nome_próprio.capitalize()







####DÊIXIS DO GN
    

def estrutura_lógica_dêixis():
    
    '''
    '''


    estrutura_lógica_dêixis = input("""
                         
            1: α(Dêitico_ñ_seletivo_específico) # ex.: O,A
            2: α(Dêitico_ñ_seletivo_ñ_específico) #ex.: Um,uns
            3: α(Dêitico_prox) #Este
            4: α(Dêitico_pess) #Meu
            5: β(Dêitico_prox)^α(Dêitico_pess) # ex.: Este meu
            6: β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess) # ex.: O meu
            7: β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess) # ex.: Um meu
                             
                             
                             
                             
                             
            Selecione uma opção:""") 
        
    if estrutura_lógica_dêixis == '1':
        
        estrutura_lógica_dêixis ='α(Dêitico_ñ_seletivo_específico)'
        
    elif estrutura_lógica_dêixis == '2':
        
        estrutura_lógica_dêixis = 'α(Dêitico_ñ_seletivo_ñ_específico)'
    
    elif estrutura_lógica_dêixis == '3':
        
        estrutura_lógica_dêixis = 'α(Dêitico_prox)'
    
    elif estrutura_lógica_dêixis == '4':
        
        estrutura_lógica_dêixis = 'α(Dêitico_pess)'
        
    elif estrutura_lógica_dêixis == '5':
        
        estrutura_lógica_dêixis = 'β(Dêitico_prox)^α(Dêitico_pess)'
    
    elif estrutura_lógica_dêixis == '6':
        
        estrutura_lógica_dêixis = 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)'
    
    elif estrutura_lógica_dêixis == '7':
        
        estrutura_lógica_dêixis = 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)'
   
    return estrutura_lógica_dêixis





        
        




#a fazer: verificar as opções que coloquei para os diferentes tipos de dêixis:
    #não preciso talvez colocar todas as opções de especificidade em cada um deles
    #pra não ter a possibilidade de dar erro nas escolhas. 
def Dêitico_ñ_seletivo_específico():
    '''
    '''
    
    
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
        
    
    
    
    
    if (DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'NA' or
        DETERMINAÇÃO_espeficifidade == 'genérico(=todos,quaisquer)' and ORIENTAÇÃO == 'NA'): 
    
        print ('Selecione número:')
        número = choice.Menu (['singular', 'plural']).ask()
        print('Selecione o gênero')
        gênero = choice.Menu (['masculino', 'feminino']).ask()
        if número == 'plural' and gênero == 'masculino':
            determinante = 'os'
            
            
        
        elif número == 'plural' and gênero == 'feminino':
            determinante = 'as'
            
            
   
        elif número == 'singular' and gênero == 'masculino':
            determinante = 'o'
            
            
        elif número == 'singular' and gênero == 'feminino':
            determinante = 'a'
            
    return determinante
            
                
    



def Dêitico_ñ_seletivo_ñ_específico():
    '''
    '''
    
    
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
        

    if DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'NA':
        print ('Selecione número:')
        número = choice.Menu (['singular', 'plural']).ask()
        print('Selecione o gênero')
        gênero = choice.Menu (['masculino', 'feminino']).ask()
        if número == 'singular' and gênero == 'masculino':
            determinante = 'um'
            
       
        elif número == 'plural' and gênero == 'masculino':
            determinante = 'uns'
            
    
        elif número == 'singular' and gênero == 'feminino':
            determinante = 'uma'
            
   
        elif número == 'plural' and gênero == 'feminino':
            determinante = 'umas'
    
    return determinante
            
    
    ####
    





def Dêitico_prox():
    '''
    '''
    
    
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
        
         
    if  DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade' :
        print ('Selecione a pessoa da interlocução:')
        pessoa_da_interlocução_proximidade = choice.Menu (['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']).ask()
        
        
        if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':
            print ('Selecione número:')
            número = choice.Menu (['singular', 'plural']).ask()
            print('Selecione o gênero')
            gênero = choice.Menu (['masculino', 'feminino']).ask()
            
            if número == 'singular' and gênero == 'masculino':
                determinante = 'este'
                
        
            elif número == 'plural' and gênero == 'masculino':
                determinante = 'estes'
                
      
            elif número == 'singular' and gênero == 'feminino':    
                determinante = 'esta'
                
        
            elif número == 'plural' and gênero == 'feminino':
                determinante = 'estas'
                
        
        elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte':
            print ('Selecione número:')
            número = choice.Menu (['singular', 'plural']).ask()
            print('Selecione o gênero')
            gênero = choice.Menu (['masculino', 'feminino']).ask()
            
            if número == 'singular' and gênero == 'masculino':
                determinante = 'esse'
                
        
            elif número == 'plural' and gênero == 'masculino':
                determinante = 'esses'
                
    
            elif número == 'singular' and gênero == 'feminino':
                determinante = 'essa'
               
            
            elif número == 'plural' and gênero == 'feminino':
                determinante = 'essas'
            
        elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor':
            print ('Selecione número:')
            número = choice.Menu (['singular', 'plural']).ask()
            print('Selecione o gênero')
            gênero = choice.Menu (['masculino', 'feminino']).ask()
            if número == 'singular' and gênero == 'masculino':
                determinante = 'aquele'
        
            elif número == 'plural' and gênero == 'masculino':
                determinante = 'aqueles'
        
            elif número == 'singular' and gênero == 'feminino':
                determinante = 'aquela'
        
            elif número == 'plural' and gênero == 'feminino':
                determinante = 'aquelas'
    
    return determinante
    

###
    
   

    

def Dêitico_pess():
    '''
    '''
        
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
        


    if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa' :
   
   
        print ('Selecione a pessoa da interlocução do possuidor')
        pessoa_da_interlocução_possuidor = choice.Menu (['1s', '2s', '3s', '1p', '2p','3p']).ask()
        
        if pessoa_da_interlocução_possuidor == '1s':
            
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
        
            
            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'meu'
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'meus'
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'minha'
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'minhas'
        
        elif pessoa_da_interlocução_possuidor == '2s': 
            
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
        
        
            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'teu'
                else:
                    determinante = 'seu'
        
            elif  número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'teus'
                else:
                    determinante = 'seus'
        
            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'tua'
                else:
                    determinante = 'sua'
        
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'tuas'
                else:
                    determinante = 'suas'
            
            
        elif (pessoa_da_interlocução_possuidor == '3s' or
              pessoa_da_interlocução_possuidor == '3p'):
            
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
                
        
            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                 determinante = 'seu'
        
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' :
                determinante = 'seus'
        
        
            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'sua'
            
            elif  número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'suas'
        
        
        elif pessoa_da_interlocução_possuidor == '1p':
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
            
            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'nosso'
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'nossos'
            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'nossa'
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'nossas'
            
        
        elif pessoa_da_interlocução_possuidor == '2p':
            print ('Selecione número do objeto  possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
        
            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'vosso'
                else:
                    determinante = 'seu'
        
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossos'
                else:
                    determinante = 'seus'
            
            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossa'
                else:
                    determinante = 'sua'
        
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossas'
                else:
                    determinante = 'suas'
    
    return determinante

 

  

def Dêitico_ñ_seletivo_específico_e_Dêitico_pess():
    '''
    '''
   
    
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
        


    if  DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa' :
   
        
        print ('Selecione a pessoa da interlocução do possuidor')
        pessoa_da_interlocução_possuidor = choice.Menu (['1s', '2s', '3s', '1p', '2p','3p']).ask()
        
        print ('Selecione número do objeto possuído:')
        número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
        print('Selecione o gênero do objeto possuído')
        gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
        
        
        if pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            determinante = 'o meu'
        elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            determinante = 'os meus'
        elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            determinante = 'a minha'
        elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            determinante = 'as minhas'
    
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome =='padrão':
                determinante = 'o teu'
            else:
                determinante = 'o seu'
        
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'os teus'
            else:
                determinante = 'os seus'
        
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'a tua'
            else:
                determinante = 'a sua'
        
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'as tuas'
            else:
                determinante = 'as suas'
        
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
              pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
            determinante = 'o seu'
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
             pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
            determinante = 'os seus'
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
              pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
            determinante = 'a sua'
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'or
              pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
            determinante = 'as suas'
        
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            determinante = 'o nosso'
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            determinante = 'os nossos'
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            determinante = 'a nossa'
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            determinante = 'as nossas'
            
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome =='padrão':
                determinante = 'o vosso'
            else:
                determinante = 'o seu'
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'os vossos'
            else:
                determinante = 'os seus'
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'a vossa'
            else:
                determinante = 'a sua'
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'as vossas'
            else:
                determinante = 'as suas'
      
    return determinante
    
    
    


def Dêitico_ñ_seletivo_ñ_específico_e_Dêitico_pess():
    '''
    '''
    
    
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
        

    if  DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':
     
        
        print ('Selecione a pessoa da interlocução do possuidor')
        pessoa_da_interlocução_possuidor = choice.Menu (['1s', '2s', '3s', '1p', '2p','3p']).ask()
        
        print ('Selecione número do objeto possuído:')
        número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
            
        print('Selecione o gênero do objeto possuído')
        gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()

        if pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            determinante = 'um meu'
            return determinante
    
        
        
        elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            determinante = 'uns meus'
            return determinante
        elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            determinante = 'uma minha'
            return determinante
        elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            determinante = 'umas minhas'
            return determinante
    
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome =='padrão':
                determinante = 'um teu'
                return determinante
            else:
                determinante = 'um seu'
                return determinante
        
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'uns teus'
                return determinante
            else:
                determinante = 'uns seus'
                return determinante
        
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'uma tua'
                return determinante
            else:
                determinante = 'uma sua'
                return determinante
        
        elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'umas tuas'
                return determinante
            else:
                determinante = 'umas suas'
                return determinante
        
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
              pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
            determinante = 'um seu'
            return determinante
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
             pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
            determinante = 'uns seus'
            return determinante
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
              pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
            determinante = 'uma sua'
            return determinante
        elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'or
              pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
            determinante = 'umas suas'
            return determinante
        
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            determinante = 'um nosso'
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            determinante = 'uns nossos'
            return determinante
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            determinante = 'uma nossa'
            return determinante
        elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            determinante = 'umas nossas'
            return determinante
            
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome =='padrão':
                determinante = 'um vosso'
                return determinante
            else:
                determinante = 'um seu'
                return determinante
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'uns vossos'
                return determinante
            else:
                determinante = 'uns seus'
                return determinante
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'uma vossa'
                return determinante
            else:
                determinante = 'uma sua'
                return determinante
        
        elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
            print( 'Selecione a morfologia do pronome:')
            morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
            if morfologia_do_pronome == 'padrão':
                determinante = 'umas vossas'
                return determinante
            else:
                determinante = 'umas suas'
                return determinante
        
        
       
      
        

def Dêitico_prox_e_Dêitico_pess():
    '''
    '''
   
    
    print ('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['NA','específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)', 'genérico(contável)']).ask()
        
         
    print ('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade', 'orientação_específica_proximidade_e_pessoa']).ask()
              
        

    if  DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade_e_pessoa':
        
        print ('Selecione a pessoa da interlocução:')
        pessoa_da_interlocução_proximidade = choice.Menu (['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']).ask()
        
        if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':
        
            print ('Selecione a pessoa da interlocução do possuidor')
            pessoa_da_interlocução_possuidor = choice.Menu (['1s', '2s', '3s', '1p', '2p','3p']).ask()
            
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
                
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
            
            if pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'este meu'
                return determinante
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'estes meus'
                return determinante
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'esta minha'
                return determinante
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'estas minhas'
                return determinante
        
            elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'este teu'
                    return determinante
                else:
                    determinante = 'este seu'
                    return determinante
            
            elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'estes teus'
                    return determinante
                else:
                    determinante = 'estes seus'
                    return determinante
            
            elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'esta tua'
                    return determinante
                else:
                    determinante = 'esta sua'
                    return determinante
            
            elif pessoa_da_interlocução_possuidor == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'estas tuas'
                    return determinante
                else:
                    determinante = 'estas suas'
                    return determinante
                    
            elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
                  pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
                determinante = 'este seu'
                return determinante
            elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
                 pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
                determinante = 'estes seus'
                return determinante
            elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
                  pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
                determinante = 'esta sua'
                return determinante
            elif (pessoa_da_interlocução_possuidor == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'or
                  pessoa_da_interlocução_possuidor == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
                determinante = 'estas suas'
                return determinante
            
            elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'este nosso'
                return determinante
            elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'estes nossos'
                return determinante
            elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'esta nossa'
                return determinante
            elif pessoa_da_interlocução_possuidor == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'estas nossas'
                return determinante
                
            elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'este vosso'
                    return determinante
                else:
                    determinante = 'este seu'
                    return determinante
            
            elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'estes vossos'
                    return determinante
                else:
                    determinante = 'estes seus'
                    return determinante
            
            elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'esta vossa'
                    return determinante
                else:
                    determinante = 'esta sua'
                    return determinante
            
            elif pessoa_da_interlocução_possuidor == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'estas vossas'
                    return determinante
                else:
                    determinante = 'estas suas' 
                    return determinante
        
    
        elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte' :
            
            print ('Selecione a pessoa da interlocução do possuidor')
            pessoa_da_interlocução_possuidor = choice.Menu (['1s', '2s', '3s', '1p', '2p','3p']).ask()
            
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
                
            print('Selecione o gênero_obj_possuído do objeto possuído')
            gênero_obj_possuído_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
        
            if pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'esse meu'
                return determinante
            elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'esses meus'
                return determinante
            elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'essa minha'
                return determinante
            elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'essas minhas'
                return determinante
        
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'esse teu'
                    return determinante
                else:
                    determinante = 'esse seu'
                    return determinante
            
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'esses teus'
                    return determinante
                else:
                    determinante = 'esses seus'
                    return determinante
            
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'essa tua'
                    return determinante
                else:
                    determinante = 'essa sua'
                    return determinante
            
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'essas tuas'
                    return determinante
                else:
                    determinante = 'essas suas'
                    return determinante
                    
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
                  pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
                determinante = 'esse seu'
                return determinante
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
                 pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
                determinante = 'esses seus'
                return determinante
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
                  pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
                determinante = 'essa sua'
                return determinante
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'or
                  pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
                determinante = 'essas suas'
                return determinante
            
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'esse nosso'
                return determinante
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'esses nossos'
                return determinante
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'essa nossa'
                return determinante
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'essas nossas'
                return determinante
                
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'esse vosso'
                    return determinante
                else:
                    determinante = 'esse seu'
                    return determinante
            
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'esses vossos'
                    return determinante
                else:
                    determinante = 'esses seus'
                    return determinante
            
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'essa vossa'
                    return determinante
                else:
                    determinante = 'essa sua'
                    return determinante
            
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'essas vossas'
                    return determinante
                else:
                    determinante = 'essas suas'
                    return determinante
        
        elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor' :
            
            print ('Selecione a pessoa da interlocução do possuidor')
            pessoa_da_interlocução_possuidor = choice.Menu (['1s', '2s', '3s', '1p', '2p','3p']).ask()
            
            print ('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu (['singular', 'plural']).ask()
                
            print('Selecione o gênero_obj_possuído do objeto possuído')
            gênero_obj_possuído_obj_possuído = choice.Menu (['masculino', 'feminino']).ask()
        
            if pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'aquele meu'
                return determinante
            elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'aqueles meus'
                return determinante
            elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'aquela minha'
                return determinante
            elif pessoa_da_interlocução == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'aquelas minhas'
                return determinante
        
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'aquele teu'
                    return determinante
                else:
                    determinante = 'aquele seu'
                    return determinante
            
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'aqueles teus'
                    return determinante
                else:
                    determinante = 'aqueles seus'
                    return determinante
            
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'aquela tua'
                    return determinante
                else:
                    determinante = 'aquela sua'
                    return determinante
            
            elif pessoa_da_interlocução == '2s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'aquelas tuas'
                    return determinante
                else:
                    determinante = 'aquelas suas'
                    return determinante
                    
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino' or
                  pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino'):
                determinante = 'aquele seu'
                return determinante
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino' or
                 pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino'):
                determinante = 'aqueles seus'
                return determinante
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino' or
                  pessoa_da_interlocução == '3p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino'):
                determinante = 'aquela sua'
                return determinante
            elif (pessoa_da_interlocução == '3s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'or
                  pessoa_da_interlocução == '3p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino'):
                determinante = 'aquelas suas'
                return determinante
            
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'aquele nosso'
                return determinante
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'aqueles nossos'
                return determinante
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'aquela nossa'
                return determinante
            elif pessoa_da_interlocução == '1p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'aquelas nossas'
                return determinante
                
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome =='padrão':
                    determinante = 'aquele vosso'
                    return determinante
                else:
                    determinante = 'aquele seu'
                    return determinante
            
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'aqueles vossos'
                    return determinante
                else:
                    determinante = 'aqueles seus'
                    return determinante
            
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'aquela vossa'
                    return determinante
                else:
                    determinante = 'aquela sua'
                    return determinante
            
            elif pessoa_da_interlocução == '2p' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                print( 'Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu (['padrão', 'de_terceira_pessoa']).ask()
                if morfologia_do_pronome == 'padrão':
                    determinante = 'aquelas vossas'
                    return determinante
                else:
                    determinante = 'aquelas suas'
                    return determinante
        
        elif DETERMINAÇÃO_espeficifidade == 'genérico(contável)' and ORIENTAÇÃO == 'NA':
            
            determinante = '' #Neste caso, o grupo nominal é realizado no plural
            return determinante
        
        elif DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' and ORIENTAÇÃO == 'NA':
           
            determinante = '' #Neste caso, o grupo nominal é realizado no singular
            return determinante
    
    


def Dêixis_geral():
    '''
    '''
    print ('Há determinante?')
    real_determinante = choice.Menu (['sim','NA']).ask()
    
    if real_determinante == 'sim':
        
        print ('Qual a sub-estrutura lógica da Dêixis?')
        estrutura_lógica = estrutura_lógica_dêixis()
        
        if (estrutura_lógica == 'α(Dêitico_ñ_seletivo_específico)' or
            estrutura_lógica == 'α(Dêitico_ñ_seletivo_específico)'):
            
            Determinante = Dêitico_ñ_seletivo_específico()
            
        elif estrutura_lógica == 'α(Dêitico_ñ_seletivo_ñ_específico)':
            Determinante = Dêitico_ñ_seletivo_ñ_específico()
            
        elif estrutura_lógica == 'α(Dêitico_prox)':
            Determinante = Dêitico_prox()
        
        elif estrutura_lógica == 'α(Dêitico_pess)':
            Determinante = Dêitico_pess()
        
        elif estrutura_lógica == 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)':
            Determinante = Dêitico_ñ_seletivo_específico_e_Dêitico_pess()
            
        elif estrutura_lógica == 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)':
            Determiante = Dêitico_ñ_seletivo_ñ_específico_e_Dêitico_pess()
        
        elif estrutura_lógica == 'β(Dêitico_prox)^α(Dêitico_pess)':
            Determinante = Dêitico_prox_e_Dêitico_pess()
        
    else:
        
        Determinante = ''
        
    
        
    return Determinante   
         
    

    


def Dêitico_genérico ():
    
    print ('Selecione tipo de dêixis genérica:')
    DETERMINAÇÃO_espeficifidade= choice.Menu(['genérico(contável)', 'genérico(de_massa)']).ask()
    
    if (DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' or
        DETERMINAÇÃO_espeficifidade == 'genérico(contável)') :
       
        determinante = '' #Neste caso, o grupo nominal CONTÁVEL é realizado no plural e o DE MASSA no singular

    return determinante




def Ente():
    '''
    '''
    
    
    print ('Qual o tipo de Ente?')
    tipo_de_Ente = choice.Menu (['consciente', 'não_consciente', 'NA']).ask()
    
    if tipo_de_Ente == 'NA':
        Ente = ''
        return Ente
    
    elif tipo_de_Ente == 'não_consciente':
        print ('Qual tipo de não_consciente?')
        tipo_de_não_consciente = choice.Menu(['material', 'semiótico']) .ask()
        
        if tipo_de_não_consciente == 'material':
            print ('Qual tipo de material?')
            tipo_de_não_consciente_material = choice.Menu (['animal', 'objeto_material', 'substância_material', 'abstração_material']).ask()
            
            if (tipo_de_não_consciente_material == 'animal' or
                tipo_de_não_consciente_material == 'objeto_material' or
                tipo_de_não_consciente_material == 'substância_material' or
                tipo_de_não_consciente_material == 'abstração_material'):
                print ('Qual a classe de palavra que realiza o Ente?')
                classe_palavra_Ente = choice.Menu (['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto','pronome_caso_oblíquo']).ask()
                
                if classe_palavra_Ente =='substantivo_comum':
                    Ente = formação_da_estrutura_do_substantivo_comum ()
                
                elif classe_palavra_Ente =='substantivo_próprio':
                    Ente = nome_próprio ()
                elif classe_palavra_Ente == 'pronome_caso_reto':
                    Ente = realização_pronominal_casoreto()
                elif classe_palavra_Ente == 'pronome_caso_oblíquo':
                    Ente = realização_pronome_caso_oblíquo()
                    
        elif tipo_de_não_consciente == 'semiótico':
            print ('Qual tipo de semiótico?')
            tipo_de_não_consciente_semiótico = choice.Menu (['instituição', 'objeto_semiótico',  'abstração_semiótica']).ask()
            
            if (tipo_de_não_consciente_semiótico == 'instituição' or
                tipo_de_não_consciente_semiótico == 'objeto_semiótico' or
                tipo_de_não_consciente_semiótico == 'abstração_semiótica'):
                print ('Qual a classe de palavra que realiza o Ente?')
                classe_palavra_Ente = choice.Menu (['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto','pronome_caso_oblíquo']).ask()
                
                if classe_palavra_Ente =='substantivo_comum':
                    Ente = formação_da_estrutura_do_substantivo_comum ()
                
                elif classe_palavra_Ente =='substantivo_próprio':
                    Ente = nome_próprio ()
                elif classe_palavra_Ente == 'pronome_caso_reto':
                    Ente = realização_pronominal_casoreto()
                elif classe_palavra_Ente == 'pronome_caso_oblíquo':
                    Ente = realização_pronome_caso_oblíquo()    
             
            
    elif tipo_de_Ente == 'consciente':
        print ('Qual a classe de palavra que realiza o Ente?')
        classe_palavra_Ente = choice.Menu (['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto','pronome_caso_oblíquo']).ask()
            
        if classe_palavra_Ente == 'substantivo_comum':
            Ente = formação_da_estrutura_do_substantivo_comum ()
            
        elif classe_palavra_Ente == 'pronome_caso_reto':
            Ente = realização_pronominal_casoreto()
            
        elif classe_palavra_Ente == 'substantivo_próprio':
            Ente =  nome_próprio ()
        elif classe_palavra_Ente == 'pronome_caso_oblíquo': 
           Ente = realização_pronome_caso_oblíquo()
           
    return Ente
        
 ###No caso do Ente, ainda tenho que modelar as opções de Ente realizados por substantivos compostos (devido ao padrão de
     # morfologia das flexões



        
     


#####ESTRUTURA DO GRUPO NOMINAL:
     
##
def qualificador_frase_prep():
    
    print('Há Qualificador no gn?')
    tem_qualificador = choice.Menu(['sim', 'NA']).ask()
    
    if tem_qualificador == 'sim':
        
        Qualificador = Preposição() +' '+ Ente( )
    else:
        Qualificador = ''
    return Qualificador 


def estrutura_GN_downraked():
    
    Determinante= Dêixis_geral()
    numerativo = Numerativo() 
    ente = Ente() 
    Classificador = adjetivo_modificador () 
    Epíteto = adjetivo_modificador () 
    Qualificador = qualificador_frase_prep()
    
    GN = Determinante + ' ' + numerativo + ' ' + ente + ' ' + Classificador + ' ' + Epíteto + ' '+ Qualificador
    
    return GN 


####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
    ##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal 
    #com função de Numerativo no GN DE PRIMEIRO NÍVEL)
def estrutura_GN():
    
    print ('Há dissociação entre Ente e Núcleo do GN?')
    dissociação_Ente_Núcleo = choice.Menu(['sim','não']).ask()
    
    if dissociação_Ente_Núcleo == 'não':
        
    
        Determinante= Dêixis_geral()
        numerativo = Numerativo() 
        ente = Ente() 
        Classificador = adjetivo_modificador () 
        Epíteto = adjetivo_modificador () 
        Qualificador = qualificador_frase_prep()
        
        GN = Determinante + ' ' + numerativo + ' ' + ente + ' ' + Classificador + ' ' + Epíteto + ' '+ Qualificador
        
    else:
        Núcleo_lógico= estrutura_GN_downraked ()
        Qualificador_Ente = frase_preposicional ()
        
        GN = Núcleo_lógico +' ' + Qualificador_Ente
    return GN 


########PREPOSIÇÃO

def Preposição():
    '''
    '''
    #Por enquanto vou deixar preposição + artigo como preposição - dos, das, do...
    Preposição = input("""
                                      
                   1:a
                   2:ante
                   3:após
                   4:até
                   5:com
                   6:contra
                   7:de
                   8:desde
                   9:em
                   10:entre
                   11:para
                   12:por
                   13:perante
                   14:sem
                   15:sob
                   16:sobre
                   17:trás
                   18:do
                   19:da
                   20:dos
                   21:das
                   22:no
                   23:na
                   24:nos
                   25:nas
                   26:pelo
                   27:pela
                   28:pelos
                   29:pelas
                                      

                       Escolha uma opção:""")
    
    if Preposição == '1':
        prepocição = 'a'
    elif Preposição == '2':
        prepocição = 'ante'
    elif Preposição == '3':
        prepocição = 'após'
    elif Preposição == '4':
        prepocição = 'até'
    elif Preposição == '5':
        prepocição = 'com'
    elif Preposição == '6':
        prepocição = 'contra'
    elif Preposição == '7':
        prepocição = 'de'
    elif Preposição == '8':
        prepocição = 'desde'
    elif Preposição == '9':
        prepocição = 'em'
    elif Preposição == '10':
        prepocição = 'entre'
    elif Preposição == '11':
        prepocição = 'para'
    elif Preposição == '12':
        prepocição = 'por'
    elif Preposição == '13':
        prepocição = 'perante'
    elif Preposição == '14':
        prepocição = 'sem'
    elif Preposição == '15':
        prepocição = 'sob'
    elif Preposição == '16':
        prepocição = 'sobre'
    elif Preposição == '17':
        prepocição = 'trás'
    elif Preposição == '18':
        prepocição = 'do'
    elif Preposição == '19':
        prepocição = 'da'
    elif Preposição == '20':
        prepocição = 'dos'
    elif Preposição == '21':
        prepocição = 'das'
    elif Preposição == '22':
        prepocição = 'no'
    elif Preposição == '23':
        prepocição = 'na'
    elif Preposição == '24':
        prepocição = 'nos'
    elif Preposição == '25':
        prepocição = 'nas'
    elif Preposição == '26':
        prepocição = 'pelo'
    elif Preposição == '27':
        prepocição = 'pela'
    elif Preposição == '28':
        prepocição = 'pelos'
    elif Preposição == '29':
        prepocição = 'pelas'
    
    return prepocição




###FRASE PREPOSICIONAL
def frase_preposicional():
    '''
    '''
    
    preposição = Preposição()
    grupo_nominal = estrutura_GN_downraked()
    
    frase_proposicional = preposição + ' ' + grupo_nominal
    
    return frase_proposicional
#A FAZERES:
############ORDEM DA ORAÇÃO

def circunstância():
    '''
    '''
    print('Selecione o tipo de grupo que realiza a circunstância:')
    realização_circunstância = choice.Menu(['grupo_nominal','frase_preposicional','grupo_adverbial']).ask()
    
    if realização_circunstância == 'grupo_nominal':
        Circunstância = estrutura_GN()
    elif realização_circunstância == 'frase_preposicional':
        Circunstância = frase_preposicional()
    elif realização_circunstância == 'grupo_adverbial':
        Circunstância = advérbio()
        
    return Circunstância

##SISTEMAS DA ORAÇÃO   

  
def AGENCIAMENTO():
    
    print ('Qual o tipo de Agenciamento?')
    AGENCIAMENTO = choice.Menu(['AG_médio_sem_alcance',
                                'AG_médio_com_alcance', 
                                'AG_efetivo_operativo',
                                'AG_efetivo_receptivo',
                                'AG_NA']).ask() 

    
    
    return AGENCIAMENTO

###tipos de processo oração
#Material
    ##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)
    
#def PROCESSO_MATERIAL():
#    Processo_material = choice.Menu(['PR_material_transformativo_transitivo',
#                                     'PR_material_criativo_transitivo',
#                                     'PR_material_transformativo_intransitivo',
#                                     'PR_material_criativo_intransitivo']).ask()
#    
#    return Processo_material




###tipos de processo oração
#Material
    ##VERIFICAR SE EXISTE DESCRIÇÃO DO PROCESSO MATERIAL (POR ENQUANTO, USANDO O SISTEMA DO INGLÊS)
    
def PROCESSO_MATERIAL(): 
    
    print ('Qual o tipo de ação realizada pelo processo?')
    TIPO_DE_AÇÃO = choice.Menu (['transformativo', 'criativo']).ask()
    
    print ('Qual o tipo de impacto?')    
    IMPACTO = choice.Menu (['IMPA_transitivo', 'IMPA_intransitivo']).ask()
    
    
    Processo_material = 'PR_material_' + TIPO_DE_AÇÃO + '_'+ IMPACTO
    
    
    
    return Processo_material

#
#
#

#relacional
    
##def atribuição_de_relação():
##    '''
##    '''
##    atribuição_de_relação = choice.Menu(['atribuição_proj_ment_cognitiva',
##                                         'atribuição_proj_ment_desiderativa',
##                                         'atribuição_proj_verbal',
##                                         'atribuição_expan_elaboração',
##                                         'atribuição_expan_intencificação',
##                                         'sem_atribuição_de_relação']).ask()
##    return atribuição_de_relação
##    
#    
#    
#    
#    
#    
#    
#def processo_relacional():
#    '''
#    '''
#    atribuição_relação = atribuição_de_relação()
#    
#    tipo_de_relacional = choice.Menu (['PR_relacional_intensivo_atributivo',
#                                       'PR_relacional_intensivo_identificativo',
#                                       'PR_relacional_possessivo_atributivo',
#                                       'PR_relacional_possessivo_identificativo',
#                                       'PR_relacional_circunstancial_atributivo',
#                                       'PR_relacional_circunstancial_identificativo']).ask()
#    
#    relacional =  tipo_de_relacional + '_' +  atribuição_relação
#    
#    return relacional
#
#
#    
    
    
#    if (atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'intensiva_atributiva'or       
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_cognitiva' and tipo_de_relacional == 'circunstancial_identificativa' or
#        
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_proj_ment_desiderativa' and tipo_de_relacional == 'circunstancial_identificativa'or
#        
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_proj_verbal' and tipo_de_relacional == 'circunstancial_identificativa'or
#        
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_expan_elaboração' and tipo_de_relacional == 'circunstancial_identificativa'or
#        
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'atribuição_expan_intencificação' and tipo_de_relacional == 'circunstancial_identificativa'or
#        
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'intensiva_atributiva' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'intensiva_identificativa' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'possessiva_atributiva' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'possessiva_identificativa' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'circunstancial_atributiva' or
#        atribuição_relação == 'não_atribuição' and tipo_de_relacional == 'circunstancial_identificativa'):
#        
#        relacional = atribuição_relação + ' ' + tipo_de_relacional    
#        
#    return relacional
#            
#        
        
                                        

        

#TRANSITIVIDADE



    
##subsistemas
    
##agenciamento oração

##MODO

#subsistemas:

#sujeitabilidade
    #coloquei aqui apenas responsabilidade e pressuposição pois
    #pessoa e número já é decidido na ordem da palavra 9tenho que ver o impacto teórico que
        ##isso tem..não sei se preciso repetir as escolhas)

def SUJEITABILIDADE():
    '''
    '''
    print ('Qual o tipo de Sujeito?')
    RESPONSABILIDADE = choice.Menu(['SUJ_responsável', 
                                  'SUJ_distante_impessoal',
                                  'SUJ_distante_não_responsável','SUJ_-sujeitabilidade']).ask() 

    PRESSUPOSIÇÃO_DO_SUJEITO = choice.Menu(['recuperado_explícito',
                                            'recuperado_implícito',
                                            'não_recuperável', 'recuperação_NA']).ask() 

    SUJEITABILIDADE =   RESPONSABILIDADE + '_' +  PRESSUPOSIÇÃO_DO_SUJEITO    
    
    return SUJEITABILIDADE


def TIPO_DE_MODO():
    
    '''
    '''
    print ('Qual o tipo de modo da oração?')
    tipo_de_modo = choice.Menu (['MOD_declarativo_+perguntafinito',
                                 'MOD_declarativo_-perguntafinito',
                                 'MOD_interrogativo_elemental',
                                 'MOD_interrogativo_polar',
                                 'MOD_imperativo']).ask()
    
    return tipo_de_modo

########


######

def AVALIAÇÃO_MODAL ():
    '''
    '''
    
    AVALIAÇÃO = choice.Menu (['+', '-']).ask()
    
    if AVALIAÇÃO == '-':
        AVALIAÇÃO_MODAL = ''
        
    else:
        POLARIDADE = choice.Menu (['positiva','negativa']).ask()
        ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada. 
        #Por enquanto vou modelar apenas a realização/ou não do adjunto-polaridade 'não'.
        
        if POLARIDADE == 'positiva':
            Adjunto_polaridade =''
        
        elif POLARIDADE == 'negativa':
            Adjunto_polaridade = 'não'
            
    return Adjunto_polaridade




###
def TIPO_POLARIDADE():
    '''
    '''
    print ('Qual o tipo de polaridade?')
    tipo_polaridade = choice.Menu (['positiva','negativa']).ask()
    ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada. 
    #Por enquanto vou modelar apenas a realização/ou não do adjunto-polaridade 'não'.
    
    return tipo_polaridade

def POLARIDADE ():
    '''
    '''
    print ('Qual o tipo de polaridade?')
    tipo_polaridade = choice.Menu (['positiva','negativa']).ask()
        ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada (em que estruturas?). 
        #Por enquanto vou modelar apenas a realização/ou não do adjunto-polaridade 'não'.
        
    if tipo_polaridade == 'positiva':
        Adjunto_polaridade = ''
    
    elif tipo_polaridade == 'negativa':
        Adjunto_polaridade = 'não'
        
    return Adjunto_polaridade


    
##############
    
## Preciso resolver como vou abordar a questão deste sistema: por enquanto vou mexer apenas com
    #polaridade, e ir incrementando as combinações.
#    
#def TIPO_AVALIAÇÃO_MODAL ():
#    '''
#    '''
#    AVALIAÇÃO = choice.Menu (['+', '-']).ask()
#    
#    if AVALIAÇÃO == '-':
#        AVALIAÇÃO_MODAL = 'AvM_sem_avaliação_modal'
#        
#    else:
#        POLARIDADE = choice.Menu (['positiva','negativa']).ask()
#        ##Preciso pesquisar mais a fundo sobre os tipos de polaridade e como ela é realizada. 
#        #Por enquanto vou modelar apenas a realização/ou não do adjunto-polaridade 'não'.
#        
#        if POLARIDADE == 'positiva':
#            Adjunto_polaridade == 'AvM_polaridade_positiva'
#        
#        elif POLARIDADE == 'negativa':
#            Adjunto_polaridade == 'AvM_polaridade_negativa'
#    

##para o sistema de modo, AINDA não considerei o subsistema de VALIDAÇÃO. (será implementado)

def MODO():
    '''
    '''
   
    print ('Faça as escolhas de MODO da oração:')
    MODO =  SUJEITABILIDADE() + '_' + TIPO_DE_MODO() 
    return MODO

# A DÊIXIS: VER, POIS ELA É DECIDIDA DESDE A ORDEM DA PALAVRA...
  

#TEMA
 

def TEMA_TEXTUAL():
    '''
    '''
   
    print ('Há TEMA TEXTUAL?')
    Tema_textual = choice.Menu(['sim','não']).ask()
    
    if Tema_textual == 'não':
        
        TEMA_TEXTUAL = ''
    else:
    
        print ('Há TEMA TEXTUAL continuativo?')
        tem_continuativo = choice.Menu(['sim','não']).ask()
        
        if tem_continuativo == 'não':
            
            TEMA_CONTINUATIVO = ''
        else:
            
            TEMA_CONTINUATIVO = conjunção_continuativa()
        
        print ('Há TEMA TEXTUAL conjuntivo?')
        
        tem_conjuntivo= choice.Menu(['sim','não']).ask()
        
        if tem_conjuntivo == 'não':
            
            TEMA_CONJUNTIVO = ''
        else:
            TEMA_CONJUNTIVO = grupo_conjuntivo()
        
        print ('Há TEMA TEXTUAL relativo?')
        tem_relativo = choice.Menu(['sim','não']).ask()
        
        if tem_relativo == 'não':
            TEMA_RELATIVO= ''
        elif tem_relativo == 'sim':
            print('Qual a tipo de relativo?')
            tipo_de_relativo = choice.Menu(['nominal', 'adverbial']).ask()
            
            if tipo_de_relativo == 'nominal':
                TEMA_RELATIVO =  pronome_relativo()
            elif tipo_de_relativo =='adverbial':
                TEMA_RELATIVO = choice.Menu(['de onde', 'quando',
                                    'onde', 'de quando', 'que','por onde']).ask()                           
                                     
        
        TEMA_TEXTUAL = TEMA_CONTINUATIVO +', '+ TEMA_CONJUNTIVO+', '+ TEMA_RELATIVO
        
    
    return TEMA_TEXTUAL


def TEMA_INTERPESSOAL():
    '''
    '''
    
    print ('Há TEMA INTERPESSOAL?')
    
    Tema_interpessoal=choice.Menu(['sim','não']).ask()
    if Tema_interpessoal == 'não':
        TEMA_INTERPESSOAL = ''
    
    elif Tema_interpessoal == 'sim':###POR ENQUANTO, TRABALHANDO COM A REALIZAÇÃO DE APENAS 1 TEMA INTERPESSOAL
        
        TIPO_TEMA_INTERPESSOAL=choice.Menu(['TI_avaliação_modo', 'TI_avaliação_comentário',
                                       'TI_encenação_troca','TI_encenação_papel_falante', 'TI_polaridade', 
                                       'TI_encenação_papel_ouvinte',
                                       'TI_NA']).ask()
        
        if (TIPO_TEMA_INTERPESSOAL == 'TI_avaliação_modo' or TIPO_TEMA_INTERPESSOAL =='TI_avaliação_comentário' or
            TIPO_TEMA_INTERPESSOAL =='TI_polaridade') :
            
            tipo_realização = choice.Menu (['grupo_adverbial','frase_preposicional']).ask()
            if tipo_realização == 'grupo_adverbial':
                 TEMA_INTERPESSOAL =  advérbio()
            else:
                TEMA_INTERPESSOAL = frase_preposicional()
        
        elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_troca':
            TEMA_INTERPESSOAL = elemento_qu()
        
        elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_falante':
            TEMA_INTERPESSOAL = partícula_modal()
        elif TIPO_TEMA_INTERPESSOAL == 'TI_encenação_papel_ouvinte':
            TEMA_INTERPESSOAL = nome_próprio () ##talvez um pronome, mas por enquanto vou deixar so o nome
            
    return TEMA_INTERPESSOAL
            
            
            


def TEMA_IDEACIONAL():
    '''
    '''
    
    print ('Qual a ORIENTAÇÃO MODAL do tema?')
    ORIENTAÇÃO_MODAL = choice.Menu(['orientado', 'não_orientado']).ask()
    
    print ('Qual a ORIENTAÇÃO TRANSITIVA do tema?')
    ORIENTAÇÃO_TRANSITIVA = choice.Menu(['direcional', 'não_direcional']).ask()
    
    print ('Qual a SELEÇÃO TEMÁTICA do tema?')
    SELEÇÃO_TEMÁTICA = choice.Menu(['default', 'proeminente']).ask()
    
    
    if ORIENTAÇÃO_MODAL == 'orientado' and ORIENTAÇÃO_TRANSITIVA == 'direcional' and SELEÇÃO_TEMÁTICA == 'default':
        print ('Qual o tipo de TEMA DEFAULT?')
        TEMA_DEFAULT = choice.Menu(['imperativo',
                                   'indicativo']).ask()
        
        if TEMA_DEFAULT == 'imperativo':
            TEMA_IDEACIONAL = 'TID_default_imperativo'
            
        elif TEMA_DEFAULT == 'indicativo':
            print ('Qual o tipo de TEMA DEFAULT INDICATIVO?')
            TEMA_DEFAULT_indicativo = choice.Menu (['declarativo',
                                                    'interrogativo_polar', 
                                                    'interrogativo_sujeito_elemental']).ask()
            
            print ('Há TEMA IDENTIFICATIVO?')
            TEMA_IDENTIFICATIVO = choice.Menu (['NA',
                                                'equativo_codificação',
                                                'equativo_decodificação']).ask()
    
            if TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'NA':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_NA'
        
            elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO =='NA':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_NA'
                
            elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO =='NA':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_NA'
             
            elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_decodificação':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação'

            elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO =='equativo_decodificação':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação'
                
            elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO =='equativo_decodificação':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_decodificação'
            
            
            elif TEMA_DEFAULT_indicativo == 'declarativo' and TEMA_IDENTIFICATIVO == 'equativo_codificação':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação'

            elif TEMA_DEFAULT_indicativo == 'interrogativo_polar' and TEMA_IDENTIFICATIVO =='equativo_codificação':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação'
                
            elif TEMA_DEFAULT_indicativo == 'interrogativo_sujeito_elemental' and TEMA_IDENTIFICATIVO =='equativo_codificação':
                
                TEMA_IDEACIONAL = 'TID_default_indicativo_interrogativo_sujeito_elemental_TIdentif_equativo_codificação'
               
    
    elif ORIENTAÇÃO_MODAL == 'não_orientado' and ORIENTAÇÃO_TRANSITIVA == 'direcional' and SELEÇÃO_TEMÁTICA == 'proeminente':
    
        TEMA_ÂNGULO = choice.Menu(['TID_fonte','TID_ponto_de_vista']).ask()
        
        TEMA_IDEACIONAL = TEMA_ÂNGULO
        
        
    
    elif ORIENTAÇÃO_MODAL == 'orientado' and ORIENTAÇÃO_TRANSITIVA == 'não_direcional' and SELEÇÃO_TEMÁTICA == 'default':
    
        TEMA_ELEMENTAL = choice.Menu(['TID_complemento_elemental','TID_adjunto_elemental']).ask()
        
        TEMA_IDEACIONAL = TEMA_ELEMENTAL
        
       
    
    elif ORIENTAÇÃO_MODAL == 'não_orientado' and ORIENTAÇÃO_TRANSITIVA == 'não_direcional' and SELEÇÃO_TEMÁTICA == 'proeminente':
        print ('Qual tipo de TEMA PROEMINENTE?')
        
        TEMA_PROEMINENTE = choice.Menu(['TID_perspectiva_intensificação',
                                        'TID_perspectiva_outro',
                                        'TID_intensivo_absoluto',
                                        'TID_intensivo_relativo_papel_transitivo_nuclear_participante',
                                        'TID_intensivo_relativo_papel_transitivo_nuclear_processo',
                                        'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_elaboração',
                                        'TID_intensivo_relativo_papel_transitivo_circunstancial_expansão_extensão',
                                        'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto',
                                        'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_reprisado',
                                        'TID_intensivo_relativo_papel_transitivo_circunstancial_projeção_assunto_estensivo_recuperável',
                                        'TID_intensivo_relativo_predicação_default_local',
                                        'TID_intensivo_relativo_predicação_proeminente_local'
                                         
                                        ]).ask()
    
        TEMA_IDEACIONAL = TEMA_PROEMINENTE
    
    
    
    
    return TEMA_IDEACIONAL






def conjunção_continuativa():
    
    '''
    '''
    print('Qual o modo de inserção da conjunção?')
    modo_inserção = choice.Menu(['inserção_manual','inserção_menu']).ask()
    
    if modo_inserção == 'inserção_manual':
        conjunção_continuativa = input ('Escreva o continuativo desejado:')
        
    elif modo_inserção == 'inserção_menu':
        print ('Escolha um continuativo:')
        conjunção_continuativa = input("""
                                 1:e 
                                 2:é 
                                 3:ah 
                                 4:mas 
                                 5:sim 
                                 6:bem 
                                 7:não 
                                 8:agora 
                                 9:então 
                                 10:pois é 
                                 11:tipo  
                                 12:tipo assim 
                                 13:ó 
                                 14:daí
                                 15:aí
                                 16:aí então  
                                 17:quer 
                                 18:dizer 
                                 19:assim
                                 20:em
                                 21:seguida 
                                 22:por fim 
                                 23:porque 
                                 24:porém 
                                 25:também
                                 26:é que 
                                 27:olha 
                                 
                                 
                                
                               Escolha uma opção:""")
            
        if conjunção_continuativa == '1':
            conjunção_continuativa = 'e'
        elif conjunção_continuativa == '2':
            conjunção_continuativa = 'é'
        elif conjunção_continuativa == '3':
            conjunção_continuativa = 'ah'
        elif conjunção_continuativa == '4':
            conjunção_continuativa = 'mas'
        elif conjunção_continuativa == '5':
            conjunção_continuativa = 'sim'
        elif conjunção_continuativa == '6':
            conjunção_continuativa = 'bem'
        elif conjunção_continuativa == '7':
            conjunção_continuativa = 'não'
        elif conjunção_continuativa == '8':
            conjunção_continuativa = 'agora'
        elif conjunção_continuativa == '9':
            conjunção_continuativa = 'então'
        elif conjunção_continuativa == '10':
            conjunção_continuativa = 'pois é'
        elif conjunção_continuativa == '11':
            conjunção_continuativa = 'tipo'
        elif conjunção_continuativa == '12':
            conjunção_continuativa = 'tipo assim '
        elif conjunção_continuativa == '13':
            conjunção_continuativa = 'ó'
        elif conjunção_continuativa == '14':
            conjunção_continuativa = 'daí'
        elif conjunção_continuativa == '15':
            conjunção_continuativa = 'aí'
        elif conjunção_continuativa == '16':
            conjunção_continuativa = 'aí então '
        elif conjunção_continuativa == '17':
            conjunção_continuativa = 'quer'
        elif conjunção_continuativa == '18':
            conjunção_continuativa = 'dizer'
        elif conjunção_continuativa == '19':
            conjunção_continuativa = 'assim'
        elif conjunção_continuativa == '20':
            conjunção_continuativa = 'em'
        elif conjunção_continuativa == '21':
            conjunção_continuativa = 'seguida'
        elif conjunção_continuativa == '22':
            conjunção_continuativa = 'por fim'
        elif conjunção_continuativa == '23':
            conjunção_continuativa = 'porque'
        elif conjunção_continuativa == '24':
            conjunção_continuativa = 'porém'
        elif conjunção_continuativa == '25':
            conjunção_continuativa = 'também'
        
        elif conjunção_continuativa == '26':
            conjunção_continuativa = 'é que'
        elif conjunção_continuativa == '27':
            conjunção_continuativa = 'olha'
    
    
    
    return conjunção_continuativa


    
def elemento_qu():
    '''
    '''
    elemento_qu = choice.Menu(['o que', 'quem', 'qual', 'quanto',
                               'quantos', 'quando', 'como', 'onde', 
                               'de quem','por quê','pra quê', 'por que']).ask()
    
    return elemento_qu


def partícula_modal():
    '''
    '''
    modo_inserção = choice.Menu(['inserção_manual','inserção_menu']).ask()
    
    if modo_inserção == 'inserção_manual':
        partícula_modal = input ('Escreva partícula modal desejada:')
        
    elif modo_inserção == 'inserção_menu':
        partícula_modal = choice.Menu(['né','ué','ó','uai','é']).ask() ##HÁ MAIS PARTÍCULAS....
        
    
    return partícula_modal
    
    




## NO CASO DO SISTEMA DE AVALIAÇÃO_MODAL EU NÃO CONTEMPLEI AINDA TODO O SISTEMA, POR ENQUANTO VOU ME 
#ATER APENAS AO SUBSISTEMA DE POLARIDADE.           

####FORMAÇÃO DA ORAÇÃO
   




   


def atribuição_de_relação():
    '''
    '''
    atribuição_de_relação = choice.Menu(['atribuição_proj_ment_cognitiva',
                                         'atribuição_proj_ment_desiderativa',
                                         'atribuição_proj_verbal',
                                         'atribuição_expan_elaboração',
                                         'atribuição_expan_intencificação'
                                         ]).ask()
    return atribuição_de_relação
  
   
    
def PROCESSO_RELACIONAL():
    '''
    '''
    
    
    tipo_de_relacional = choice.Menu (['PR_relacional_intensivo_atributivo',
                                       'PR_relacional_intensivo_identificativo',
                                       'PR_relacional_possessivo_atributivo',
                                       'PR_relacional_circunstancial_atributivo',
                                       'PR_relacional_possessivo_identificativo',
                                       'PR_relacional_circunstancial_identificativo']).ask()
    
    
    
    
    
    return tipo_de_relacional


def TRANSITIVIDADE():
    '''       
    '''
    print ('Qual o tipo de Processo?')
    TIPO_DE_PROCESSO = choice.Menu(['Material',
                                    'Relacional',
                                    'Mental',
                                    'Verbal',
                                    'Existencial']).ask()
    
    if TIPO_DE_PROCESSO == 'Material':
        print('Selecione as opções do sistema da Oração Material')
        Processo = PROCESSO_MATERIAL()
        Agenciamento = AGENCIAMENTO()
        
            
        TRANSITIVIDADE = Processo + '_' + Agenciamento
    
    elif TIPO_DE_PROCESSO == 'Relacional':
        print('Selecione as opções do sistema da Oração Relacional')
        Processo =  PROCESSO_RELACIONAL()
        Agenciamento = AGENCIAMENTO()
    
        TRANSITIVIDADE = Processo + '_' + Agenciamento
    
    elif TIPO_DE_PROCESSO ==  'Existencial':
        print('Selecione as opções do sistema da Oração Existencial')
        Processo = 'PR_Existencial'
        Agenciamento = AGENCIAMENTO()
        
        TRANSITIVIDADE = Processo + '_' + Agenciamento 
    
    elif TIPO_DE_PROCESSO == 'Verbal':
        print('Selecione as opções do sistema da Oração Verbal')
        Processo = 'PR_Verbal'
        Agenciamento = AGENCIAMENTO()
        
        TRANSITIVIDADE = Processo + '_' + Agenciamento 
    
        
    return TRANSITIVIDADE








def oração():
    '''(str,str,str)->str
    Retorna a formação estrutural na lexicogramática (oração) de uma figura específica
    da semãntica
    
    >>>formação_estrutura_oração ()
    'eu bebi água'
    '''
    
    
    ##ORAÇÃO MATERIAL
    
    Transitividade = TRANSITIVIDADE()
    Modo = MODO()
    Tema_id = TEMA_IDEACIONAL()
    
    
    if Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''
        
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
        
        if TIPO_DE_RESULTADO == 'elaboração':
            
            print ('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or 
                RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador ()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''
            
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta +' '+ Atributo+'.'
             
    
        
        elif TIPO_DE_RESULTADO == 'extensão':
            print ('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''
                
        
        
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador  + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta +'  '+ Beneficiário +'.'
    
    
      
    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL() 
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''
        
        print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
        
        if CLIENTE == '+cliente':
            Cliente = frase_preposicional() 
        else:
            Cliente=''
        
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta +' '+ Cliente +'.'
    
        
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''
        
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
             print('Qual é o Escopo?')
             tipo_Escopo = choice.Menu (['escopo(processo)','escopo(entidade)']).ask()
             if tipo_Escopo == 'escopo(processo)':
                 Escopo = estrutura_GN()
             elif tipo_Escopo == 'escopo(entidade)':
                 Escopo = estrutura_GN() #por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
            
             oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' +  Escopo+'.'
    
        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu (['escopo(processo)','escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN() #por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
            print ('Há resultado locativo?')
            realização_locativo =choice.Menu(['sim','não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo=''
    
        
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' +  Escopo+ ' ' + Resultado_locativo +'.'
    
    
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        
    
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
    
    
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
             print('Orações médio_sem_alcance  selecionam -escopo')
             Escopo = ''
             
        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Orações médio_sem_alcance selecionam -escopo')
            
            print ('Há resultado locativo?')
            realização_locativo =choice.Menu(['sim','não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo=''
    
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Resultado_locativo +'.'
    
   
    ##ORAÇÃO METEOROLÓGICA
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' and Modo == 'SUJ_-sujeitabilidade_recuperação_NA_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
       
        tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)','pessoal']).ask()
        print ('Qual o tipo de inTransitividade?')
        if tipo_intransitiva == 'impessoal(fenômeno_natural)':
            print('Há escopo?')
            escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
            if escopo_intransitiva == '+escopo':
                print('Qual estrutura realiza o escopo?')
                realização_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
                if realização_escopo == 'frase_preposicional':
                    Escopo = frase_preposicional()
                elif realização_escopo == 'grupo_nominal':
                    Escopo = estrutura_GN()
            elif escopo_intransitiva == '-escopo':
                Escopo = ''
                    
                    
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        
        
        Polaridade = POLARIDADE()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''
        
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador+' '+  Polaridade + ' ' + Processo + ' ' + Escopo +'.'
    
   
    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()   
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
           
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = '' 
        
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo +'.'
    
         
        
        ##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)
      
    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_complemento_elemental':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal() ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''
       
        print ('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''
            
          
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
        
        if TIPO_DE_RESULTADO == 'elaboração':
            
            print ('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or 
                RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador ()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''
            
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Atributo+ ' ' + Ator +'.'
        
        elif TIPO_DE_RESULTADO == 'extensão':
            print ('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''
                
        
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +'.'
          
   ##
        
    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_complemento_elemental':
        
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal() ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''
       
        print ('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''
            
          
        print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
        
        if CLIENTE == '+cliente':
            Cliente = frase_preposicional() 
        elif CLIENTE == '-cliente':
            Cliente=''
            
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +'.'
    
    
    ###RELACIONAl
    

###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
    if Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
       ####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
       ## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
       
       
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL() 
        
        print('Qual o tipo de especificação de associação?')
        tipo_especificação_associação = choice.Menu(['entidade','qualidade']).ask()
        print ('Qual a fase da atribuição?')
        fase_atribuição= choice.Menu(['neutra','faseada']).ask()##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
                                                            ###não vou especializar os tipos de fase.
        print ('Qual o domínio da atribuição')
        domínio_atribuição = choice.Menu(['material','semiótico']).ask()
        
        
        
        if (tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
            tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
            tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
            tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
                                                             
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = estrutura_GN()
            
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo +'.'
   
        elif (tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
              tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
              tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
              tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
           
            print ('Qual o Processo?')                                                 
            Processo = grupo_verbal()
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = adjetivo_modificador ()## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
                                      # o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo. 
                                      ##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo +'.'
   
    
###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
            ##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva (há a possibilidade de Agente de segunda, terceira.....ordem)
        ####para desenvolver....
    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
            
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Atribuidor?')
            Atribuidor = estrutura_GN()
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = estrutura_GN() ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar) 
            
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' +  Atribuidor+ ' ' + Polaridade + ' ' + Processo  + ' ' + Portador  + ' ' + Atributo +'.'

    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
            
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Atribuidor?')
            Atribuidor = frase_preposicional()
            
            
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = estrutura_GN() ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar) 
            
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo  + ' ' +   Atributo + ' ' +  Atribuidor +'.'

    
    ####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)
    
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_decodificação':
        
        print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
        if direcionalidade_voz == 'meio_operativa':
            print ('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            
        # (confluência do Símbolo/Identificado) =
       
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'.'
    
    
    
        elif direcionalidade_voz == 'meio_receptiva': 
            print ('Neste caso, o Valor/Identificador conflui com o Sujeito')
            ##NESTE CASO, confluência de Valor/Sujeito
           
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo+'.'
    
    
    
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_equativo_codificação':
        
        print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
        if direcionalidade_voz == 'meio_operativa':
            print ('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            
        # (confluência do Símbolo/Identificador/Sujeito) =
          #(Valor/Identificado/complemento)
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'.'
    
    
    
        elif direcionalidade_voz == 'meio_receptiva': 
            print ('Neste caso, o Valor conflui com o Sujeito')
            ##NESTE CASO, confluência de Valor/Identificado/Sujeito
            ##(Símbolo/Identificador/Complemento)
            
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo+'.'
  
    ####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)
    
#    ###TRUE_Efetiva_operativa
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        #POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
           
            
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
     
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Designador?')
            Designador = estrutura_GN()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN() ##ou frase preposicional?
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' +  Designador+ ' ' + Polaridade + ' ' + Processo  + ' ' + Símbolo  + ' ' + Valor +'.'
            ###rever possíveis estruturas para este tipo de oração(pode haver 2 processos?)
     
     ###TRUE_Efetiva_receptiva
       
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Designador?')
            Designador = frase_preposicional()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN() ##ou frase preposicional?
            Polaridade = POLARIDADE ()
    #        
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo  + ' ' + Polaridade + ' ' + Processo   + ' ' + Valor + ' ' +  Designador +'.'
    ####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realização de cada participante;
    #        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)
         
#POSSESSIVO ATRIBUTIV0
    
    if Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
       

        TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu (['posse_atributo','posse_processo']).ask()
        
        if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':       
            
            realização_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()
           
            if realização_atributo == 'grupo_nominal_possessivo':
            
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Posse?')
                Portador_Posse = estrutura_GN()
                print ('Qual é o Atributo/Possuidor?')
                Atributo_Possuidor = estrutura_GN()
                Polaridade = POLARIDADE()
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor+'.'
  
            elif realização_atributo == 'frase_preposicional':
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Posse?')
                Portador_Posse = estrutura_GN()
                print ('Qual é o Atributo/Possuidor?')
                Atributo_Possuidor = frase_preposicional()
                Polaridade = POLARIDADE()
            
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor +'.'
  
               
        elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':
            
            ##VERBO TER/POSSUIR/
            
            tipo_possuidor= choice.Menu (['possuidor_portador','possuidor_atributo']).ask()
            
            if tipo_possuidor == 'possuidor_portador':
                    
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Possuidor?')
                Portador_Possuidor = estrutura_GN()
                print ('Qual é o Atributo/Posse?')
                Atributo_Posse = estrutura_GN()
                Polaridade = POLARIDADE()
            
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Posse+'.'
      
            
            ###VERBOS PERTENCER A/...
            
            elif tipo_possuidor == 'possuidor_atributo':
                    
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Possuidor?')
                Portador_Posse = estrutura_GN()
                print ('Qual é o Atributo/Posse?')
                Atributo_Possuidor = frase_preposicional()
                Polaridade = POLARIDADE()
            
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor+'.'
      
            
        # POSSESSIVO IDENTIFICATIVO 
     
       
    elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        
        TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu (['posse_participante','posse_processo']).ask()
        
        if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':
            
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')
                
                print (
                        'Escolha o tipo de realização do Valor:')
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
           
                if realização_Valor == 'grupo_nominal':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)/Possuído?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)/Possuidor?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O piano é seu
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuidor +'.'
               
                elif realização_Valor == 'frase_preposicional':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)?')
                    Valor_Possuidor = frase_preposicional()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O piano é do André
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuidor +'.'
           
            
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')
                
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
           
                if realização_Valor == 'grupo_nominal':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)/Possuído?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)/Possuidor?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O seu é o piano
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído +'.'
               
                elif realização_Valor == 'frase_preposicional':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O do André é o piano
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído +'.'        
        
        elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
         ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
         ##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS
        
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)/Possuidor?')
                Símbolo_Possuidor = estrutura_GN()
                print ('Qual o Valor(Value)/Possuído?')
                Valor_Possuído = estrutura_GN()
                Polaridade = POLARIDADE ()
                
                #Ex.: O produto contém plástico, Eles merecem a aposentadoria
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuído +'.'
           
                
            
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')
                
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
           
                if realização_Valor == 'grupo_nominal':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()##na passiva
                    print ('Qual o Valor(Value)/Possuído?')
                    Valor_Possuído = estrutura_GN()
                    print ('Qual é o Símbolo(Token)/Possuidor?')
                    Símbolo_Possuidor = frase_preposicional()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O seu é o piano
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuidor +'.'


#####RELACIONAL CIRCUNSTANCIAL 
                    
    elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        print ('Qual o tipo de realização da Relacional Circunstancial?')
        TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu (['atributo_circunstancial','processo_circunstancial']).ask()
        
        if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Portador')
            Portador = estrutura_GN()
            print ('Qual é o Atributo Circunstancial?')
            Atributo_Circunstancial = circunstância()
            Polaridade = POLARIDADE()
            
            #Ex.: O livro é sobre a IIGuerra
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Circunstancial +'.'
        
        elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL =='processo_circunstancial':
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Portador')
            Portador = estrutura_GN()
            print ('Qual é o Atributo Circunstancial?')
            Atributo = estrutura_GN()
            Polaridade = POLARIDADE()
            
            #Ex.: O livro retrata a IIGuerra
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo +'.'
        
        
        
        
    elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        
        print ('O significado circunstancial é realixado no participante ou no processo?')
        TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu (['participante_circunstancial','processo_circunstancial']).ask()
        
        if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':
            
        
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
            
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, há confluência Símbolo/Sujeito/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print ('Qual o Valor(Value)?')
                Valor = estrutura_GN()
                Polaridade = POLARIDADE ()
                
                #Ex.: Amanhá é dia 10
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'.'
               
                
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, há confluência Valor/Sujeito/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print ('Qual o Valor(Value)?')
                Valor = estrutura_GN()
                Polaridade = POLARIDADE ()
                
                #Ex.:dia 10 é Amanhá
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo +'.'
               
    
        elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
         
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
            
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, há confluência Símbolo/Sujeito/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print ('Qual o Valor(Value)?')
                Valor = circunstância()
                Polaridade = POLARIDADE()
                
                #Ex.: A feira dura o dia todo
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'.'
               
        
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, há confluência Valor/Sujeito/Identificado')
                    
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal() ## reiterações-verbo na passiva
                print ('Qual o Valor(Value)?')
                Valor = circunstância()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
               
                Polaridade = POLARIDADE()
                
                #Ex.: O dia todo é ocupado pela feira
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo +'.'
    
   
    
    
    ##ORAÇÃO EXISTENCIAL
    
  
    elif Transitividade ==  'PR_Existencial_AG_NA' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
        
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Existente?')
        Existente = estrutura_GN()
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Processo + ' ' + Existente +'.'
               
#
##
###
######
####### ORAÇÕES INTERROGATIVAS POLARES
        
        
        
        
        
    ##ORAÇÃO MATERIAL MODO INTERROGATIVO POLAR
    
    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''
        
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
        
        if TIPO_DE_RESULTADO == 'elaboração':
            
            print ('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or 
                RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador ()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''
            
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta +' '+ Atributo+'?'
             
    
        
        elif TIPO_DE_RESULTADO == 'extensão':
            print ('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''
                
        
        
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador  + ' ' + Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta +'  '+ Beneficiário +'?'
    
    
    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL() 
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''
        
        print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
        
        if CLIENTE == '+cliente':
            Cliente = frase_preposicional() 
        else:
            Cliente=''
        
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Meta +' '+ Cliente +'?'
    
        
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = ''
        
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
             print('Qual é o Escopo?')
             tipo_Escopo = choice.Menu (['escopo(processo)','escopo(entidade)']).ask()
             if tipo_Escopo == 'escopo(processo)':
                 Escopo = estrutura_GN()
             elif tipo_Escopo == 'escopo(entidade)':
                 Escopo = estrutura_GN() #por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
            
             oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' +  Escopo+'?'
    
        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Qual é o Escopo?')
            tipo_Escopo = choice.Menu (['escopo(processo)','escopo(entidade)']).ask()
            if tipo_Escopo == 'escopo(processo)':
                Escopo = estrutura_GN()
            elif tipo_Escopo == 'escopo(entidade)':
                Escopo = estrutura_GN() #por enquanto os dois tipos de escopo são realizados pela mesma estrutura(verificar se já distinção ao longo da anotação do corpus)
            print ('Há resultado locativo?')
            realização_locativo =choice.Menu(['sim','não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo=''
    
        
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' +  Escopo+ ' ' + Resultado_locativo +'?'
    
    
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
        
    
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
    
    
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','intensificação']).ask()
        if TIPO_DE_RESULTADO == 'elaboração':
             print('Orações médio_sem_alcance  selecionam -escopo')
             Escopo = ''
             
        elif TIPO_DE_RESULTADO == 'intensificação':
            print('Orações médio_sem_alcance selecionam -escopo')
            
            print ('Há resultado locativo?')
            realização_locativo =choice.Menu(['sim','não']).ask()
            if realização_locativo == 'sim':
                Resultado_locativo = frase_preposicional()
            else:
                Resultado_locativo=''
    
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo + ' ' + Resultado_locativo +'?'
    
   
    ##ORAÇÃO METEOROLÓGICA MODO INTERROGATIVO POLAR
    elif Transitividade == 'PR_material_transformativo_IMPA_intransitivo_AG_NA' and Modo == 'sujeitabilidade_recuperação_NA_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()
       
        tipo_intransitiva = choice.Menu(['impessoal(fenômeno_natural)','pessoal']).ask()
        print ('Qual o tipo de inTransitividade?')
        if tipo_intransitiva == 'impessoal(fenômeno_natural)':
            print('Há escopo?')
            escopo_intransitiva = choice.Menu(['+escopo', '-escopo']).ask()
            if escopo_intransitiva == '+escopo':
                print('Qual estrutura realiza o escopo?')
                realização_escopo = choice.Menu(['frase_preposicional', 'grupo_nominal']).ask()
                if realização_escopo == 'frase_preposicional':
                    Escopo = frase_preposicional()
                elif realização_escopo == 'grupo_nominal':
                    Escopo = estrutura_GN()
            elif escopo_intransitiva == '-escopo':
                Escopo = ''
                    
                    
        print ('Qual o Processo?')
        Processo = grupo_verbal()
               
        Polaridade = POLARIDADE()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN()
        else:
            Iniciador = ''
        
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador+' '+  Polaridade + ' ' + Processo + ' ' + Escopo +'?'
    
   
    elif Transitividade == 'PR_material_criativo_IMPA_intransitivo_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL()   
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Ator?')
        Ator = estrutura_GN()
        Polaridade = POLARIDADE()
           
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()
        else:
            Iniciador = '' 
        
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' + Iniciador+' '+ Ator + ' ' + Polaridade + ' ' + Processo +'?'
    
         
        
        ##########COMEÇO DE AGENCIAMENTO PASSIVA(E CONSEQUENTEMENTE NO TEMA IDEACIONAL)
      
    elif Transitividade == 'PR_material_transformativo_IMPA_transitivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_complemento_elemental':
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal() ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''
       
        print ('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''
            
          
        print ('Há resultado do processo?')
        TIPO_DE_RESULTADO = choice.Menu(['elaboração','extensão','intensificação']).ask()
        
        if TIPO_DE_RESULTADO == 'elaboração':
            
            print ('há Resultado_elaboração atributo ou papel?')
            RESULTADO_QUALITATIVO = choice.Menu (['resultado_atributo', 'resultado_papel(produto)', '-resultado']).ask()
            if (RESULTADO_QUALITATIVO == 'resultado_atributo' or 
                RESULTADO_QUALITATIVO == 'resultado_papel(produto)'):
                realização_atributo = choice.Menu(['adjetivo','frase_preposicional']).ask()
                if realização_atributo == 'adjetivo':
                    Atributo = adjetivo_modificador ()
                elif realização_atributo == 'frase_preposicional':
                    Atributo = frase_preposicional()
            elif RESULTADO_QUALITATIVO == '-resultado':
                Atributo = ''
            
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Atributo+ ' ' + Ator +'?'
        
        elif TIPO_DE_RESULTADO == 'extensão':
            print ('Há Participante Beneficiário na oração?')
            RECEPÇÃO = choice.Menu (['+beneficiário','-beneficiário']).ask()
            if RECEPÇÃO == '+beneficiário':
                Beneficiário = frase_preposicional()
            elif RECEPÇÃO == '-beneficiário':
                Beneficiário = ''
                
        
            oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo  +'  '+ Beneficiário + ' ' + Ator +'?'
          
   ##
        
    elif Transitividade == 'PR_material_criativo_IMPA_transitivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_complemento_elemental':
        
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal() ##selecionar agenciado_passivo
        print('Qual é a Meta?')
        Meta = estrutura_GN()
        Polaridade = POLARIDADE ()
        
        print ('Há Participante Iniciador na oração?')
        INICIADOR = choice.Menu (['+iniciador','-iniciador']).ask()
        if INICIADOR == '+iniciador':
            Iniciador = estrutura_GN() + grupo_verbal()####TENHO QUE VER AS REALIZAÇÕES DE INICIADOR(POR enquanto apenas uma realização básica)
        else:
            Iniciador = ''
       
        print ('O Ator/Agente é realizado na oração?')
        realização_Ator = choice.Menu (['+ator/agente','-ator/agente']).ask()
        if realização_Ator == '+ator/agente':
            print('Qual é o Ator/Agente?')
            Ator = frase_preposicional()
        elif realização_Ator == '-ator/agente':
            Ator = ''
            
          
        print ('Há Participante Cliente na oração?') #Por enquanto apenas 1 cliente realizado (prevejo a possibilidade de +1)
        CLIENTE = choice.Menu (['+cliente','-cliente']).ask()
        
        if CLIENTE == '+cliente':
            Cliente = frase_preposicional() 
        elif CLIENTE == '-cliente':
            Cliente=''
            
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Iniciador + ' ' + Meta + ' ' + Polaridade + ' ' + Processo +' '+ Cliente+ ' ' + Ator +'?'
    
    
    ###RELACIONAl MODO INTERROGATIVO POLAR
    

###### INTENSIVA ATRIBUTIVA (SEM ATRIBUIDOR)
    if Transitividade == 'PR_relacional_intensivo_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
       ####Relacionais atributivas são Middle(mas selecionam necessariamente meio-operativa = por isso não são reversíveis)
       ## Selecionam sem_atribuição_de relação no sistema de ATRIBUIÇÃO DE RELAÇÃO
       
       
        Tema_textual=TEMA_TEXTUAL()
        Tema_interpessoal = TEMA_INTERPESSOAL() 
        
        print('Qual o tipo de especificação de associação?')
        tipo_especificação_associação = choice.Menu(['entidade','qualidade']).ask()
        print ('Qual a fase da atribuição?')
        fase_atribuição= choice.Menu(['neutra','faseada']).ask()##Me parece que neste caso há diferenças em termos de verbo lexical que realiza o Processo (e tempo verbal em alguns casos)
                                                            ###não vou especializar os tipos de fase.
        print ('Qual o domínio da atribuição')
        domínio_atribuição = choice.Menu(['material','semiótico']).ask()
        
        
        
        if (tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
            tipo_especificação_associação == 'entidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
            tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
            tipo_especificação_associação == 'entidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
                                                             
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = estrutura_GN()
            
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo +'?'
   
        elif (tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'material' or
              tipo_especificação_associação == 'qualidade' and fase_atribuição == 'neutra' and domínio_atribuição == 'semiótico' or
              tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'material' or
              tipo_especificação_associação == 'qualidade' and fase_atribuição == 'faseada' and domínio_atribuição == 'semiótico'):
           
            print ('Qual o Processo?')                                                 
            Processo = grupo_verbal()
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = adjetivo_modificador ()## O que diferencia os dois tipos é o que realiza o Atributo. Neste caso
                                      # o Núcleo do grupo é um EPíteto (por isso coloquei realizado pelo adjetivo. 
                                      ##Tenho que ver ainda casos metafóricos ex,:'o caso é de grande importância')
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo +'?'
   
    
###### INTENSIVA ATRIBUTIVA (COM ATRIBUIDOR)
            ##Nesse caso, a oração é Effective (Tem Agente) e pode ser operativa ou receptiva (há a possibilidade de Agente de segunda, terceira.....ordem)
        ####para desenvolver....
    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
            
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Atribuidor?')
            Atribuidor = estrutura_GN()
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = estrutura_GN() ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar) 
            
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' +  Atribuidor+ ' ' + Polaridade + ' ' + Processo  + ' ' + Portador  + ' ' + Atributo +'?'

    elif Transitividade == 'PR_relacional_intensivo_atributivo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ESTRUTURA DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
            
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Atribuidor?')
            Atribuidor = frase_preposicional()
            
            
            print ('Qual o Portador?')
            Portador = estrutura_GN()
            print ('Qual o Atributo?')
            Atributo = estrutura_GN() ##ou frase preposicional; grupo nominal com Epíteto como núcleo (checar) 
            
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' + Portador + ' ' + Polaridade + ' ' + Processo  + ' ' +   Atributo + ' ' +  Atribuidor +'?'

    
    ####INTENSIVA_IDENTIFICATIVA (sem DESIGNADOR)
    
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_decodificação':
        print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
        if direcionalidade_voz == 'meio_operativa':
            print ('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            
        # (confluência do Símbolo/Identificado) =
       
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'?'
    
    
    
        elif direcionalidade_voz == 'meio_receptiva': 
            print ('Neste caso, o Valor/Identificador conflui com o Sujeito')
            ##NESTE CASO, confluência de Valor/Sujeito
           
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo+'?'
    
    
    
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_equativo_codificação':
        
        print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor/Sujeito deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
        direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
        if direcionalidade_voz == 'meio_operativa':
            print ('Neste caso, o Símbolo/Identificado conflui com o Sujeito(geralmente o elemento em posição temática)')
            
        # (confluência do Símbolo/Identificador/Sujeito) =
          #(Valor/Identificado/complemento)
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'?'
    
    
    
        elif direcionalidade_voz == 'meio_receptiva': 
            print ('Neste caso, o Valor conflui com o Sujeito')
            ##NESTE CASO, confluência de Valor/Identificado/Sujeito
            ##(Símbolo/Identificador/Complemento)
            
       
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo+'?'
      
    
    ####INTENSIVA_IDENTIFICATIVA (COM DESIGNADOR = AGENTE)
    
#    ###TRUE_Efetiva_operativa
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        #POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
           
            
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
     
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Designador?')
            Designador = estrutura_GN()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN() ##ou frase preposicional?
            Polaridade = POLARIDADE ()
            
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' +  Designador+ ' ' + Polaridade + ' ' + Processo  + ' ' + Símbolo  + ' ' + Valor +'?'
            ###rever possíveis estruturas para este tipo de oração(pode haver 2 processos?)
     
     ###TRUE_Efetiva_receptiva
       
    elif Transitividade == 'PR_relacional_intensivo_identificativo_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        print ('Qual o tipo de atribuição de relação?')
        tipo_atribuição_relação = atribuição_de_relação()
        ##ir verificando no corpus se há diferença de realização para cada uma das opções a seguir e também se as ordens dos
        #elementos na oração mudam(e consequente adequações morfológicas precisam ser implementadas)
        ##POR ENQUANTO, VOU COLOCAR APENAS UMA POSSIBILIDADE DE REALIZAÇÃO...COM O GRUPO NOMINAL E UMA ORDEM DE ELEMENTOS NA ORAÇÃO
        
        if (tipo_atribuição_relação == 'atribuição_proj_ment_cognitiva' or
            tipo_atribuição_relação =='atribuição_proj_ment_desiderativa',
            tipo_atribuição_relação =='atribuição_proj_verbal',
            tipo_atribuição_relação =='atribuição_expan_elaboração',
            tipo_atribuição_relação =='atribuição_expan_intencificação'):
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
           
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual é o Designador?')
            Designador = frase_preposicional()
            print ('Qual é o Símbolo(Token)?')
            Símbolo = estrutura_GN()
            print ('Qual o Valor(Value)?')
            Valor = estrutura_GN() ##ou frase preposicional?
            Polaridade = POLARIDADE ()
    #        
            oração =  Tema_interpessoal + ' ' + Tema_textual + ' ' + Símbolo  + ' ' + Polaridade + ' ' + Processo   + ' ' + Valor + ' ' +  Designador +'?'
    ####NOS DOIS TIPOS DE ORAÇÃO ANTERIORES É PRECISO VERIFICAR: possibilidade de realização de cada participante;
    #        #ordem na estrutura; etc (vou fazer isso de acordo com o que for encontrando no corpus, por enquanto estao comentadas)
         
#POSSESSIVO ATRIBUTIV0
    
    if Transitividade == 'PR_relacional_possessivo_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
       

        TIPO_ATRIBUIÇÃO_POSSESSIVO = choice.Menu (['posse_atributo','posse_processo']).ask()
        
        if TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_atributo':       
            
            realização_atributo = choice.Menu(['grupo_nominal_possessivo', 'frase_preposicional']).ask()
           
            if realização_atributo == 'grupo_nominal_possessivo':
            
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Posse?')
                Portador_Posse = estrutura_GN()
                print ('Qual é o Atributo/Possuidor?')
                Atributo_Possuidor = estrutura_GN()
                Polaridade = POLARIDADE()
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor+'?'
  
            elif realização_atributo == 'frase_preposicional':
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Posse?')
                Portador_Posse = estrutura_GN()
                print ('Qual é o Atributo/Possuidor?')
                Atributo_Possuidor = frase_preposicional()
                Polaridade = POLARIDADE()
            
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor +'?'
  
               
        elif TIPO_ATRIBUIÇÃO_POSSESSIVO == 'posse_processo':
            
            ##VERBO TER/POSSUIR/
            
            tipo_possuidor= choice.Menu (['possuidor_portador','possuidor_atributo']).ask()
            
            if tipo_possuidor == 'possuidor_portador':
                    
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Possuidor?')
                Portador_Possuidor = estrutura_GN()
                print ('Qual é o Atributo/Posse?')
                Atributo_Posse = estrutura_GN()
                Polaridade = POLARIDADE()
            
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Posse+'?'
      
            
            ###VERBOS PERTENCER A/...
            
            elif tipo_possuidor == 'possuidor_atributo':
                    
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual o Portador/Possuidor?')
                Portador_Posse = estrutura_GN()
                print ('Qual é o Atributo/Posse?')
                Atributo_Possuidor = frase_preposicional()
                Polaridade = POLARIDADE()
            
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador_Posse + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Possuidor+'?'
      
            
        # POSSESSIVO IDENTIFICATIVO 
     
       
    elif Transitividade == 'PR_relacional_possessivo_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        
        TIPO_IDENTIFICATIVO_POSSESSIVO = choice.Menu (['posse_participante','posse_processo']).ask()
        
        if TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_participante':
            
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, o Símbolo conflui com o Sujeito/Possuído/Identificado')
                
                print (
                        'Escolha o tipo de realização do Valor:')
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
           
                if realização_Valor == 'grupo_nominal':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)/Possuído?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)/Possuidor?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O piano é seu
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuidor +'?'
               
                elif realização_Valor == 'frase_preposicional':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)?')
                    Valor_Possuidor = frase_preposicional()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O piano é do André
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuidor +'?'
           
            
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, o Valor conflui com Sujeito/Identificado/Possuidor')
                
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
           
                if realização_Valor == 'grupo_nominal':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)/Possuído?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)/Possuidor?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O seu é o piano
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído +'?'
               
                elif realização_Valor == 'frase_preposicional':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()
                    print ('Qual é o Símbolo(Token)?')
                    Símbolo_Possuído = estrutura_GN()
                    print ('Qual o Valor(Value)?')
                    Valor_Possuidor = estrutura_GN()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O do André é o piano
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuído +'?'        
        
        elif TIPO_IDENTIFICATIVO_POSSESSIVO == 'posse_processo':
         ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste de, providenciar
         ##NÃO SEI SE ESTA PARTE DO SISTEMA FUNCIONA BEM NO PORTUGUÊS
        
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
        
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, o Símbolo conflui com o Sujeito/Possuidor/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo? ## GERALMENTE REALIZADOS POR: incluir, envolver, conter, consiste, providenciar')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)/Possuidor?')
                Símbolo_Possuidor = estrutura_GN()
                print ('Qual o Valor(Value)/Possuído?')
                Valor_Possuído = estrutura_GN()
                Polaridade = POLARIDADE ()
                
                #Ex.: O produto contém plástico, Eles merecem a aposentadoria
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo_Possuidor + ' ' + Polaridade + ' ' + Processo + ' ' + Valor_Possuído +'?'
           
                
            
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, o Valor conflui com Sujeito/Identificado/Possuído')
                
                realização_Valor = choice.Menu(['grupo_nominal', 'frase_preposicional']).ask()
           
                if realização_Valor == 'grupo_nominal':
                
                
                    Tema_textual=TEMA_TEXTUAL()
                    Tema_interpessoal = TEMA_INTERPESSOAL() 
                   
                    print ('Qual o Processo?')
                    Processo = grupo_verbal()##na passiva
                    print ('Qual o Valor(Value)/Possuído?')
                    Valor_Possuído = estrutura_GN()
                    print ('Qual é o Símbolo(Token)/Possuidor?')
                    Símbolo_Possuidor = frase_preposicional()
                    Polaridade = POLARIDADE ()
                    
                    #Ex.: O seu é o piano
                    oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor_Possuído + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo_Possuidor +'?'


#####RELACIONAL CIRCUNSTANCIAL MODO INTERROGATIVO POLAR
                    
    elif Transitividade == 'PR_relacional_circunstancial_atributivo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        print ('Qual o tipo de realização da Relacional Circunstancial?')
        TIPO_ATRIBUTIVO_CIRCUNSTANCIAL = choice.Menu (['atributo_circunstancial','processo_circunstancial']).ask()
        
        if TIPO_ATRIBUTIVO_CIRCUNSTANCIAL == 'atributo_circunstancial':
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL() 
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Portador')
            Portador = estrutura_GN()
            print ('Qual é o Atributo Circunstancial?')
            Atributo_Circunstancial = circunstância()
            Polaridade = POLARIDADE()
            
            #Ex.: O livro é sobre a IIGuerra
            
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo_Circunstancial +'?'
        
        elif TIPO_ATRIBUTIVO_CIRCUNSTANCIAL =='processo_circunstancial':
            Tema_textual=TEMA_TEXTUAL()
            Tema_interpessoal = TEMA_INTERPESSOAL()
            print ('Qual o Processo?')
            Processo = grupo_verbal()
            print ('Qual o Portador')
            Portador = estrutura_GN()
            print ('Qual é o Atributo Circunstancial?')
            Atributo = estrutura_GN()
            Polaridade = POLARIDADE()
            
            #Ex.: O livro retrata a IIGuerra
            oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Portador + ' ' + Polaridade + ' ' + Processo + ' ' + Atributo +'?'
        
        
        
        
    elif Transitividade == 'PR_relacional_circunstancial_identificativo_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        
        print ('O significado circunstancial é realixado no participante ou no processo?')
        TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL = choice.Menu (['participante_circunstancial','processo_circunstancial']).ask()
        
        if TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'participante_circunstancial':
            
        
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
            
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, há confluência Símbolo/Sujeito/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print ('Qual o Valor(Value)?')
                Valor = estrutura_GN()
                Polaridade = POLARIDADE ()
                
                #Ex.: Amanhá é dia 10
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'?'
               
                
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, há confluência Valor/Sujeito/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print ('Qual o Valor(Value)?')
                Valor = estrutura_GN()
                Polaridade = POLARIDADE ()
                
                #Ex.:dia 10 é Amanhá
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo +'?'
               
    
        elif TIPO_IDENTIFICATIVO_CIRCUNSTANCIAL == 'processo_circunstancial':
         
            print ('Apesar de Médio(middle), a direcionalidade_voz do Símbolo/Valor deste tipo de oração determina se é operativa ou receptiva. Selecione a direcionalidade:')
            direcionalidade_voz = choice.Menu(['meio_operativa','meio_receptiva']).ask()
            
            if direcionalidade_voz == 'meio_operativa':
                print ('Neste caso, há confluência Símbolo/Sujeito/Identificado')
                
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
                print ('Qual o Valor(Value)?')
                Valor = circunstância()
                Polaridade = POLARIDADE()
                
                #Ex.: A feira dura o dia todo
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Símbolo + ' ' + Polaridade + ' ' + Processo + ' ' + Valor +'?'
               
        
            elif direcionalidade_voz == 'meio_receptiva':
                print ('Neste caso, há confluência Valor/Sujeito/Identificado')
                    
                Tema_textual=TEMA_TEXTUAL()
                Tema_interpessoal = TEMA_INTERPESSOAL() 
               
                print ('Qual o Processo?')
                Processo = grupo_verbal() ## reiterações-verbo na passiva
                print ('Qual o Valor(Value)?')
                Valor = circunstância()
                print ('Qual é o Símbolo(Token)?')
                Símbolo = circunstância()
               
                Polaridade = POLARIDADE()
                
                #Ex.: O dia todo é ocupado pela feira
                
                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Valor + ' ' + Polaridade + ' ' + Processo + ' ' + Símbolo +'?'
    
   
    
    
    ##ORAÇÃO EXISTENCIAL MODO INTERROGATIVO POLAR
    
  
    elif Transitividade ==  'PR_Existencial_AG_NA' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_interrogativo_polar' and Tema_id == 'TID_default_indicativo_interrogativo_polar_TIdentif_NA':
        
        Tema_interpessoal = TEMA_INTERPESSOAL()
        Tema_textual=TEMA_TEXTUAL()
        
        print ('Qual o Processo?')
        Processo = grupo_verbal()
        print('Qual é o Existente?')
        Existente = estrutura_GN()
        
        oração = Tema_interpessoal + ' ' + Tema_textual + ' ' +Processo + ' ' + Existente +'?'
    
    
    
    
    return oração.capitalize() 

   















####PRECISO CHECAR CASOS EM QUE HÁ A SELEÇÃO DE DOIS TIPOS DE EXPANSÃO AO MESMO TEMPO (ELABORAÇÃO + EXTENSÃO)...esses 
    #casos não parecem ter sido conteplados nem na descrição do inglês nem do português(por enquanto vou deixar como nos sistemas)

##ORAÇÃO: estou trabalhando com possibilidades restritras da ordem dos elementos na oração, uma ordem básica. À medida
    #que nos exemplos do domínio forem aparecendo ordens diferentes devo ir implementando. 

##Ainda não trabalhei com todas as opções do sistema de SUJEITABILIDADE (apenas com o explícito, recuperado)...não mexi com IMPERATIVO AINDA; Também
#não trabalhei com opções PROEMINENTES () dos sistema de TEMA IDEACIONAL (trabalhei apenas com os Defaults)
 

   

##### Para a ordem da oração, preciso pensar em como relacionar com os 
#    tipos de configuração da GUM, e além disso relacionar com o sistema
#    lexicogramatical geral da oração




#####################             A FAZERESSSS
#URGENTES
# 1-Mexer com o grupo nominal agora para conseguir implementar mais coisas na ordem da oração


#Preciso bolar um jeito para que o parâmetro que entro nas funções seja semântico
#para que daí a estrutura que realiza seja retornada pela função. Até agora,
#como tenho feito, fica circular..precisando sempre 'passar' um elemento da estrutura.

##Talvez precise de uma outra abordagem, começando da oração e descendo na escala de ordens. Mas acredito que
#este trabalho feito até agora, vá ser ''nested'' nas outras funções, acho que a realização
#vá precisar das duas etapas, uma as funções mais voltadas para a função semântica vão precisar dessas funções
#mais estruturais para funcionar a geração CALMA, ESSE TRABALHO TODO NAO SERÁ PERDIDO.








#
#
#
#####SEMÂNTICA######
#
##TENTAR UMA ABORDAGEM DIFERENTE, PARTINDO DA FIGURA NA SEMÂNTICA
#
##VOU COMEÇAR COM OS SISTEMAS BÁSICOS E COM PARADIGMAS SIMPLES COM POUCAS OPÇÕES
##PRA VER COMO A LÓGICA FUNCIONA
#
###ORGANIZAÇÃO DO SISTEMA DE FUNÇÕES DISCURSIVAS (COM BASE EM HALLIDAY E A
##DESCRIÇÃO DO GIACOMO)
#
#
#
#
# #################################################
#def função_discursiva (movimento_de_troca):
#    '''(str,str,str) -> str
#
#    Retorna uma organização semântica global necessária para a realização
#    gramatical das funções discursivas dado um objetivo geral da troca.
#
#    >>>função_discursiva ('N')
#    'declaração'
#    >>>função_discursiva (movimento de troca)
#    'pergunta'
#    '''
#
#
#
#    ARGUMENTO = choice.Menu(['inicial', 'respondeente']).ask()
#    ORIENTAÇÃO = choice.Menu(['demanda', 'fornecimento']).ask()
#    MERCADORIA = choice.Menu(['informação', 'bens&serviços']).ask()
#
#    movimento_de_troca = (ARGUMENTO, ORIENTAÇÃO, MERCADORIA)
#
#
#
#    FUNÇÃO_DISCURSIVA = ''
#    estrutura_pergunta = ''
#    estrutura_
#    if ARGUMENTO == 'inicial' and ORIENTAÇÃO == 'demanda' and MERCADORIA == 'informação':
#         FUNÇÃO_DISCURSIVA = 'pergunta'
#         return FUNÇÃO_DISCURSIVA
#
#    elif ARGUMENTO == 'inicial' and ORIENTAÇÃO == 'demanda' and MERCADORIA == 'bens&serviços':
#        FUNÇÃO_DISCURSIVA = 'comando'
#        return FUNÇÃO_DISCURSIVA
#
#    elif ARGUMENTO == 'inicial' and ORIENTAÇÃO == 'fornecimento' and MERCADORIA == 'bens&serviços':
#        FUNÇÃO_DISCURSIVA = 'oferta'
#        return  FUNÇÃO_DISCURSIVA
#
#    elif ARGUMENTO == 'inicial' and ORIENTAÇÃO == 'fornecimento' and MERCADORIA == 'informação':
#        FUNÇÃO_DISCURSIVA = 'declaração'
#        return  FUNÇÃO_DISCURSIVA
#
################
##talvez tenha de rever a questão do parâmetro para passar à função
#
#
#
