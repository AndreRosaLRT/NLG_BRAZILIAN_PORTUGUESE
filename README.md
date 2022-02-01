# Repositório geral

Repositório contendo arquivos de corpora, experimento e os módulos lexicogramaticais para
realização superficial do português brasileiro independente de domínio.

##Conteúdo
Este repositório geral contém os seguintes diretórios:

1 - 


##Utilizando a função de realização do verbo no português brasileiro

A função de realização das palavras verbais_verbos encontra-se no caminho 
NLG_BRAZILIAN_PORTUGUESE/geracao_funcoes_por_ordem/ordem_palavra/pal_verbais.py.

No módulo, foi desenvolvida a função _verbo_geral_, que aceita os seguintes parâmetros e retorna a estrutura que realiza os verbos no português.

    :param tipo_de_experiencia:
        opções: 'Fazer','Ser', 'Sentir'
    :param funcao_no_grupo_verbal:
        opções:'Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo','Auxiliar+Núcleo', 'Modal+Núcleo'
    :param verbo: str
        lema verbal - no infinitivo
    :param tipo_de_orientacao: str
        opções: 'infinitivo','presente','pretérito_perfectivo_I', 'pretérito_perfectivo_II', 'pretérito_imperfectivo',
        'passado_volitivo', 'futuro', 'subjuntivo_conjuntivo','subjuntivo_condicional', 'subjuntivo_optativo',
        'não_finito_concretizado','imperativo_I','imperativo_II','gerúndio', 'particípio'
    :param oi_numero:str
       escolhas: 'singular', 'plural'
    :param genero:str
        escolhas: 'feminino', 'masculino'
    :param oi_tipo_de_pessoa:str
        escolhas: '1pessoa','2pessoa','3pessoa'
    :param padrao_pessoa_morfologia:str
       escolhas: "Morfologia_padrão", "3pessoa_do_singular"
    :return verbo: str
        verbo conjugado de acordo com os parâmetros

Seguem alguns exemplos de utilização da função de realização dos verbos:

Ex.:
    >>> verbo_geral('Fazer','Evento','vir','passado_volitivo','singular',None,'1pessoa')
    'viria'
    >>> verbo_geral('Fazer','Evento','sentir','subjuntivo_conjuntivo','plural',None,'1pessoa')
    'sintamos'

Foi desenvolvida uma função _flexionar_verbo_ para a conversão dos parâmetros utilizados no 
robô-jornalista e utilização da fução _verbo_geral_, para a realização do experimento de aplicação 
na instância local do robô:

Ex.:


_TEVE_

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='ter', person='3', gender='none', number='Sing',
mood='Ind', tense='Past', aspect='Perf')

_REGISTROU_

flexionar_verbo(experience="Fazer", function_in_group='Evento', lemma="registrar", person='3', gender='none',
number='Sing', mood='Ind', tense='Past', aspect='Perf')

_REPORTOU_

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='reportar', person='3', gender='none', number='Sing',
mood='Ind', tense='Past', aspect='Perf')

_DIVULGOU_

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='divulgar', person='3', gender='none', number='Sing',
mood='Ind', tense='Past', aspect='Perf')

_IDENTIFICOU_

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='identificar', person='3', gender='none',
number='Sing', mood='Ind', tense='Past', aspect='Perf')

_FORAM_ (auxiliar)

flexionar_verbo(experience='Ser', function_in_group='Auxiliar', lemma='ser', person='3', gender='none', number='Plur',
mood='Ind', tense='Past', aspect='Perf')

_DESMATADOS_

flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='desmatar', person='none', gender='Masc',
number='Plur', mood='none', tense='Past', aspect='Perf')

_FOI_ (evento)

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='ser', person='3', gender='none', number='Sing',
mood='Ind', tense='Past', aspect='Perf')

_ATINGIDO_

flexionar_verbo(experience='Fazer', function_in_group='Evento', lemma='atingir', person='none', gender='Masc',
number='Sing', mood='none', tense='Past', aspect='Perf')

_DEIXA_

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='deixar', person='3', gender='none', number='Sing',
mood='Ind', tense='Pres', aspect='none')

_SOMARAM_

flexionar_verbo(experience='Ser', function_in_group='Evento', lemma='somar', person='3', gender='none', number='Plur',
mood='Ind', tense='Past', aspect='Perf')
