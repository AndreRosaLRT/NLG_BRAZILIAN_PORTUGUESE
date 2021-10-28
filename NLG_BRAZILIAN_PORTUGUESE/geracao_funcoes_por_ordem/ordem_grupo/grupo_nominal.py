from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_nominais import *
from NLG_BRAZILIAN_PORTUGUESE.geracao_funcoes_por_ordem.ordem_palavra.pal_verbais import *

# # ####DÊIXIS DO GN
# #


def estrutura_logica_deixis():
    '''
    '''

    estrutura_lógica_det_dêixis = input("""

            α(Dêitico_ñ_seletivo_específico) # ex.: O,A
            α(Dêitico_ñ_seletivo_ñ_específico) #ex.: Um,uns
            3: α(Dêitico_prox) #Este
            4: α(Dêitico_pess) #Meu
            5: β(Dêitico_prox)^α(Dêitico_pess) # ex.: Este meu
            6: β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess) # ex.: O meu
            7: β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess) # ex.: Um meu





            Selecione uma opção:""")

    if estrutura_lógica_det_dêixis == '1':

        estrutura_lógica_det_dêixis = 'α(Dêitico_ñ_seletivo_específico)'

    elif estrutura_lógica_det_dêixis == '2':

        estrutura_lógica_det_dêixis = 'α(Dêitico_ñ_seletivo_ñ_específico)'

    elif estrutura_lógica_det_dêixis == '3':

        estrutura_lógica_det_dêixis = 'α(Dêitico_prox)'

    elif estrutura_lógica_det_dêixis == '4':

        estrutura_lógica_det_dêixis = 'α(Dêitico_pess)'

    elif estrutura_lógica_det_dêixis == '5':

        estrutura_lógica_det_dêixis = 'β(Dêitico_prox)^α(Dêitico_pess)'

    elif estrutura_lógica_det_dêixis == '6':

        estrutura_lógica_det_dêixis = 'β(Dêitico_ñ_seletivo_específico)^α(Dêitico_pess)'

    elif estrutura_lógica_det_dêixis == '7':

        estrutura_lógica_det_dêixis = 'β(Dêitico_ñ_seletivo_ñ_específico)^α(Dêitico_pess)'

    return estrutura_lógica_det_dêixis


# #
# # # a fazer: verificar as opções que coloquei para os diferentes tipos de dêixis:
# # # não preciso talvez colocar todas as opções de especificidade em cada um deles
# # # pra não ter a possibilidade de dar erro nas escolhas.
def Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade, ORIENTAÇÃO, número, gênero):
    '''
    print('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade = choice.Menu(
        ['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
         'genérico(contável)']).ask()

    print('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']).ask()
                              print('Selecione número:')
    número = choice.Menu(['singular', 'plural']).ask()
    print('Selecione o gênero')
    gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

    if (DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'NA'):

        if número == 'plural' and gênero == 'masculino':
            determinante = 'os'
        elif número == 'plural' and gênero == 'feminino':
            determinante = 'as'
        elif número == 'singular' and gênero == 'masculino':
            determinante = 'o'
        elif número == 'singular' and gênero == 'feminino':
            determinante = 'a'

    return determinante


# Dêitico_ñ_seletivo_específico('específico', 'NA','plural', 'feminino')
# #
def Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade, ORIENTAÇÃO, número, gênero):
    '''
    print('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade = choice.Menu(
        ['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)', 'genérico(de_massa)',
         'genérico(contável)']).ask()

    print('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']).ask()

    print('Selecione número:')
        número = choice.Menu(['singular', 'plural']).ask()
        print('Selecione o gênero')
        gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

    if DETERMINAÇÃO_espeficifidade == 'não_específico' and ORIENTAÇÃO == 'NA':
        if número == 'singular' and gênero == 'masculino':
            determinante = 'um'
        elif número == 'plural' and gênero == 'masculino':
            determinante = 'uns'
        elif número == 'singular' and gênero == 'feminino':
            determinante = 'uma'
        elif número == 'plural' and gênero == 'feminino':
            determinante = 'umas'
    return determinante


# Dêitico_ñ_seletivo_ñ_específico('não_específico','NA','plural','masculino')
# # 	####
# #

def Dêitico_prox(DETERMINAÇÃO_espeficifidade, ORIENTAÇÃO, pessoa_da_interlocução_proximidade, número, gênero):
    '''
    print('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']).ask()
    print('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa',
                              'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']).ask()
    print('Selecione a pessoa da interlocução:')
        pessoa_da_interlocução_proximidade = choice.Menu(
            ['próximo_ao_falante', 'próximo_ao_ouvinte', 'próximo_ao_não_interlocutor']).ask()
    print('Selecione número:')
            número = choice.Menu(['singular', 'plural']).ask()
            print('Selecione o gênero')
            gênero = choice.Menu(['masculino', 'feminino']).ask()
    '''

    if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_proximidade':

        if pessoa_da_interlocução_proximidade == 'próximo_ao_falante':

            if número == 'singular' and gênero == 'masculino':
                determinante = 'este'
            elif número == 'plural' and gênero == 'masculino':
                determinante = 'estes'
            elif número == 'singular' and gênero == 'feminino':
                determinante = 'esta'
            elif número == 'plural' and gênero == 'feminino':
                determinante = 'estas'

        elif pessoa_da_interlocução_proximidade == 'próximo_ao_ouvinte':

            if número == 'singular' and gênero == 'masculino':
                determinante = 'esse'
            elif número == 'plural' and gênero == 'masculino':
                determinante = 'esses'
            elif número == 'singular' and gênero == 'feminino':
                determinante = 'essa'
            elif número == 'plural' and gênero == 'feminino':
                determinante = 'essas'

        elif pessoa_da_interlocução_proximidade == 'próximo_ao_não_interlocutor':

            if número == 'singular' and gênero == 'masculino':
                determinante = 'aquele'
            elif número == 'plural' and gênero == 'masculino':
                determinante = 'aqueles'
            elif número == 'singular' and gênero == 'feminino':
                determinante = 'aquela'
            elif número == 'plural' and gênero == 'feminino':
                determinante = 'aquelas'

    return determinante


# Dêitico_prox('específico','orientação_específica_proximidade','próximo_ao_não_interlocutor','plural','masculino')

def Dêitico_pess(DETERMINAÇÃO_espeficifidade, ORIENTAÇÃO, pessoa_da_interlocução_possuidor,
                 número_obj_possuído, gênero_obj_possuído, morfologia_do_pronome='morfologia_terceira_pessoa'):
    '''
    print('Selecione a especificidade:')
    DETERMINAÇÃO_espeficifidade = choice.Menu(['NA', 'específico', 'não_específico', 'genérico(=todos,quaisquer)',
                                               'genérico(de_massa)', 'genérico(contável)']).ask()

    print('Selecione a orientação:')
    ORIENTAÇÃO = choice.Menu(['NA', 'orientação_específica_pessoa', 'orientação_específica_proximidade',
                              'orientação_específica_proximidade_e_pessoa']).ask

    print('Selecione a pessoa da interlocução do possuidor')
        pessoa_da_interlocução_possuidor = choice.Menu(['1s', '2s', '3s', '1p', '2p', '3p']).ask()

    print('Selecione número do objeto possuído:')
            número_obj_possuído = choice.Menu(['singular', 'plural']).ask()
            print('Selecione o gênero do objeto possuído')
            gênero_obj_possuído = choice.Menu(['masculino', 'feminino']).ask()
    print('Selecione a morfologia do pronome:')
                morfologia_do_pronome = choice.Menu(['padrão', 'terceira_pessoa']).ask()
    '''

    if DETERMINAÇÃO_espeficifidade == 'específico' and ORIENTAÇÃO == 'orientação_específica_pessoa':

        if pessoa_da_interlocução_possuidor == '1s':

            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'meu'
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'meus'
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'minha'
            elif pessoa_da_interlocução_possuidor == '1s' and número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'minhas'

        elif pessoa_da_interlocução_possuidor == '2s':

            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'teu'
                else:
                    determinante = 'seu'

            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'teus'
                else:
                    determinante = 'seus'

            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'tua'
                else:
                    determinante = 'sua'

            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'tuas'
                else:
                    determinante = 'suas'

        elif (pessoa_da_interlocução_possuidor == '3s' or
              pessoa_da_interlocução_possuidor == '3p'):

            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'seu'

            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'seus'

            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'sua'

            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'suas'

        elif pessoa_da_interlocução_possuidor == '1p':

            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':
                determinante = 'nosso'
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':
                determinante = 'nossos'
            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':
                determinante = 'nossa'
            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':
                determinante = 'nossas'

        elif pessoa_da_interlocução_possuidor == '2p':

            if número_obj_possuído == 'singular' and gênero_obj_possuído == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vosso'
                else:
                    determinante = 'seu'

            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'masculino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossos'
                else:
                    determinante = 'seus'

            elif número_obj_possuído == 'singular' and gênero_obj_possuído == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossa'
                else:
                    determinante = 'sua'

            elif número_obj_possuído == 'plural' and gênero_obj_possuído == 'feminino':

                if morfologia_do_pronome == 'padrão':
                    determinante = 'vossas'
                else:
                    determinante = 'suas'

    return determinante


# Dêitico_pess('específico','orientação_específica_pessoa','2p','plural','feminino','padrão')


# ##talvez não use
# def Dêitico_genérico(DETERMINAÇÃO_espeficifidade):
#
# 	'''
#
# 	DETERMINAÇÃO_espeficifidade = choice.Menu(['genérico(contável)', 'genérico(de_massa)']).ask()
#
# 	:return:
# 	'''
#
#
# 	if (DETERMINAÇÃO_espeficifidade == 'genérico(de_massa)' or
# 			DETERMINAÇÃO_espeficifidade == 'genérico(contável)'):
# 		determinante = ''  # Neste caso, o grupo nominal CONTÁVEL é realizado no plural e o DE MASSA no singular
#
# 	return determinante
# #

def Deixis_geral(DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
                 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
                 DETERMINAÇÃO_espeficifidade_alpha=None,
                 ORIENTAÇÃO_alpha=None, gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
                 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None,
                 gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None):
    try:
        if DETERMINAÇÃO_espeficifidade_alpha == 'específico':
            if ORIENTAÇÃO_alpha == 'orientação_específica_proximidade':
                alpha = Dêitico_prox(DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
                                     pessoa_da_interlocução_proximidade, número_alpha, gênero_alpha)
            elif ORIENTAÇÃO_alpha == 'orientação_específica_pessoa':
                alpha = Dêitico_pess(DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
                                     pessoa_da_interlocução_possuidor,
                                     número_obj_possuído, gênero_obj_possuído, morfologia_do_pronome_alpha)
            else:
                alpha = Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade_alpha,
                                                      ORIENTAÇÃO_alpha, número_alpha, gênero_alpha)
        elif DETERMINAÇÃO_espeficifidade_alpha == 'não_específico':
            alpha = Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade_alpha,
                                                    ORIENTAÇÃO_alpha, número_alpha, gênero_alpha)
        else:
            alpha = ''

        if DETERMINAÇÃO_espeficifidade_beta == 'específico':

            if ORIENTAÇÃO_beta == 'orientação_específica_proximidade':
                beta = Dêitico_prox(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
                                    pessoa_da_interlocução_proximidade,
                                    número_beta, gênero_beta)
            elif ORIENTAÇÃO_beta == 'orientação_específica_pessoa':
                beta = Dêitico_pess(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
                                    pessoa_da_interlocução_possuidor,
                                    número_obj_possuído, gênero_obj_possuído, morfologia_do_pronome_beta)
            else:
                beta = Dêitico_ñ_seletivo_específico(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, número_beta,
                                                     gênero_beta)
        elif DETERMINAÇÃO_espeficifidade_beta == 'não_específico':
            beta = Dêitico_ñ_seletivo_ñ_específico(DETERMINAÇÃO_espeficifidade_beta,
                                                   ORIENTAÇÃO_beta, número_beta, gênero_beta)

        else:
            beta = ''

        return " ".join((beta, alpha))
    except:
        return ''


#
# Deixis_geral( None,None, None,None,None,'específico','orientação_específica_proximidade', 'masculino','singular','morfologia_terceira_pessoa','1s','singular','masculino','próximo_ao_falante')
# Deixis_geral(None,None, None,None,None, 'específico', 'NA','masculino','singular','morfologia_terceira_pessoa', None,None, None,None)
# Deixis_geral('específico','NA','masculino','singular','morfologia_terceira_pessoa',
# 			 'específico','orientação_específica_pessoa', 'masculino','singular','morfologia_terceira_pessoa','1s',
# 			 'singular','masculino','próximo_ao_falante')
# Deixis_geral()


#
#
# print('Qual o tipo_pessoa de Ente?')
# tipo_de_Ente = choice.Menu(['consciente', 'não_consciente', 'NA']).ask()
#
# print('Qual tipo_pessoa de não_consciente?')
# tipo_de_nao_consciente = choice.Menu(['material', 'semiótico']).ask()
#
# print('Qual tipo_pessoa de material?')
# tipo_de_nao_consciente_material = choice.Menu(
# 	['animal', 'objeto_material', 'substância_material', 'abstração_material']).ask()
#
# print('Qual a classe de palavra que realiza o Ente?')
# classe_palavra_Ente = choice.Menu(
# 	['substantivo_comum', 'substantivo_próprio', 'pronome_caso_reto', 'pronome_caso_obliquo']).ask()
# print('Qual tipo_pessoa de semiótico?')
# tipo_de_nao_consciente_semiotico = choice.Menu(
# 	['instituição', 'objeto_semiótico', 'abstração_semiótica']).ask()


def Ente(tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
         tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
         numero=None, genero=None, tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None,
         nomeProprio=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
         morfologia_do_pronome=None, reflexivo=None):
    """"""
    try:
        if tipo_de_Ente == 'NA':
            Ente = ''
        else:
            if classe_palavra_Ente == 'substantivo_comum':
                Ente = substantivo_comum(substantivo_lematizado, numero, genero,
                                         tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica)

            elif classe_palavra_Ente == 'substantivo_próprio':
                Ente = nomeProprio
            elif classe_palavra_Ente == 'pronome_caso_reto':
                Ente = realizacao_pronominal_casoreto(pessoa_da_interlocucao, genero,
                                                      numero, morfologia_do_pronome)
            elif classe_palavra_Ente == 'pronome_caso_oblíquo':
                Ente = realizacao_pronome_caso_obliquo(transitividade_verbo, tonicidade,
                                                       pessoa_da_interlocucao, numero, genero,
                                                       morfologia_do_pronome, reflexivo)

        return Ente
    except:
        return ''


#
# #
Ente('não_consciente', 'material', 'animal', None, 'substantivo_comum', 'gato', 'singular', 'feminino')
# Ente('consciente',None,None, None,'substantivo_comum','menina','singular', 'feminino')
Ente(tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
     tipo_de_nao_consciente_material='animal',
     tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
     substantivo_lematizado='gato', numero='plural', genero='masculino',
     tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
     transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None)


# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "singular",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)
# Ente("não_consciente", "semiótico",None, 'abstração_semiótica',
#      'pronome_caso_reto', None, "plural",
#      "feminino",None, None,None,None,"falante",
#      None,None,None,None)
# Ente(tipo_de_Ente="não_consciente", tipo_de_nao_consciente="semiótico", tipo_de_nao_consciente_material=None,
# 	tipo_de_nao_consciente_semiotico='abstração_semiótica', classe_palavra_Ente='pronome_caso_oblíquo',
# 	 substantivo_lematizado=None, numero='plural', genero='masculino', tipo_feminino_ÃO=None,
# 	 tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,pessoa_da_interlocucao='não_interlocutor',
# 	 transitividade_verbo='indireto', tonicidade='tônico', morfologia_do_pronome='não_padrão', reflexivo=False)


# #
# # ###No caso do Ente, ainda tenho que modelar as opções de Ente realizados por substantivos compostos (devido ao padrão de
# # # morfologia das flexões
# #

#####ESTRUTURA DO GRUPO NOMINAL:

##
# print('Há Qualificador no gn?')
# tem_qualificador = choice.Menu(['sim', 'NA']).ask()
# realizacao_qualificador = choice.Menu(['frase-preposicional', 'oração']).ask()


def qualificador(indicePreposicaoFrase=None, dissocEnteNucleo=None, DETERMINAÇÃO_espeficifidade_beta=None,
                 ORIENTAÇÃO_beta=None,
                 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
                 DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None, gênero_alpha=None,
                 número_alpha=None, morfologia_do_pronome_alpha=None, pessoa_da_interlocução_possuidor=None,
                 número_obj_possuído=None, gênero_obj_possuído=None, pessoa_da_interlocução_proximidade=None,  #
                 funcaoNumerativo=None, cardinal=None, genero=None, tipo_precisa=None, tipoRealCard=None,
                 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
                 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
                 numero=None,
                 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
                 pessoa_da_interlocucao=None,
                 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
                 temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None, adjetivo_epiteto=None,
                 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
    try:
        if tipoQualificador == 'frase-preposicional':
            Qualificador = frase_preposicional(indicePreposicaoFrase, dissocEnteNucleo, temQualificador,
                                               tipoQualificador,
                                               indicePreposicaoQualif, DETERMINAÇÃO_espeficifidade_beta,
                                               ORIENTAÇÃO_beta, gênero_beta,
                                               número_beta, morfologia_do_pronome_beta,
                                               DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha, gênero_alpha,
                                               número_alpha, morfologia_do_pronome_alpha,
                                               pessoa_da_interlocução_possuidor, número_obj_possuído,
                                               gênero_obj_possuído, pessoa_da_interlocução_proximidade,
                                               funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
                                               milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                               numIndefinido, tipo_de_Ente, tipo_de_nao_consciente,
                                               tipo_de_nao_consciente_material, tipo_de_nao_consciente_semiotico,
                                               classe_palavra_Ente, substantivo_lematizado, numero, tipo_feminino_ÃO,
                                               tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
                                               transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
                                               adjetivo_epiteto, adjetivo_classificador, generoAdjetivo, numeroAdjetivo,
                                               contracao)
            # else:
            # 	Qualificador = "que" + oraçãoProjetada()
            return re.sub(' +', ' ', Qualificador).strip()
    except:
        return ''


#
# for i in range(12):
# 	print(qualificador(indicePreposicaoFrase=i,dissocEnteNucleo=None, DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino', número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s', número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor', funcaoNumerativo=None, cardinal=None,
# 			 genero='masculino', tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
# 			 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None, tipo_de_Ente='não_consciente',
# 			 tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural', tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None,
# 			 nomeProprio=None, pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
# 			 morfologia_do_pronome=None, reflexivo=None, temQualificador=None, tipoQualificador='frase-preposicional',indicePreposicaoQualif=5,
# 			 adjetivo_epiteto='bonito', adjetivo_classificador=None, generoAdjetivo='masculino',
# 			 numeroAdjetivo='plural', contracao='-contração'))


def estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None,
                 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
                 morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha=None, ORIENTAÇÃO_alpha=None,
                 gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
                 pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
                 pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero=None,
                 tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
                 dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
                 tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
                 numero=None, tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
                 pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
                 reflexivo=None, adjetivo_epiteto=None,
                 adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
    try:
        if dissocEnteNucleo == None:

            Determinante = Deixis_geral(DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
                                        gênero_beta, número_beta, morfologia_do_pronome_beta,
                                        DETERMINAÇÃO_espeficifidade_alpha,
                                        ORIENTAÇÃO_alpha, gênero_alpha, número_alpha, morfologia_do_pronome_alpha,
                                        pessoa_da_interlocução_possuidor, número_obj_possuído,
                                        gênero_obj_possuído, pessoa_da_interlocução_proximidade)

            numerativo = Numerativo(funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
                                    milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso, numIndefinido)

            ente = Ente(tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                        tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
                        genero, tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
                        transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo)

            Classificador = adjetivo(adjetivo_classificador, generoAdjetivo, numeroAdjetivo)

            Epiteto = adjetivo(adjetivo_epiteto, generoAdjetivo, numeroAdjetivo)

            GN = " ".join((Determinante, numerativo, ente, Classificador, Epiteto))

        else:

            Nucleo_logico = estrutura_GN_downraked(dissocEnteNucleo, temQualificador, tipoQualificador,
                                                   indicePreposicaoQualif, DETERMINAÇÃO_espeficifidade_beta,
                                                   ORIENTAÇÃO_beta, gênero_beta, número_beta,
                                                   morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha,
                                                   ORIENTAÇÃO_alpha, gênero_alpha, número_alpha,
                                                   morfologia_do_pronome_alpha, pessoa_da_interlocução_possuidor,
                                                   número_obj_possuído, gênero_obj_possuído,
                                                   pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal,
                                                   genero, tipo_precisa, tipoRealCard, milharExtenso, centenaExtenso,
                                                   dezenaExtenso, unidadeExtenso, numIndefinido, tipo_de_Ente,
                                                   tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                                   tipo_de_nao_consciente_semiotico, classe_palavra_Ente,
                                                   substantivo_lematizado, numero, tipo_feminino_ÃO, tipo_masc_ÃO,
                                                   acentTonica, nomeProprio, pessoa_da_interlocucao,
                                                   transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo,
                                                   adjetivo_epiteto, adjetivo_classificador, generoAdjetivo,
                                                   numeroAdjetivo, contracao)

            Qualificador = Qualificador = qualificador(indicePreposicaoQualif, dissocEnteNucleo,
                                                       DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta,
                                                       gênero_beta, número_beta, morfologia_do_pronome_beta,
                                                       DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
                                                       gênero_alpha,
                                                       número_alpha, morfologia_do_pronome_alpha,
                                                       pessoa_da_interlocução_possuidor,
                                                       número_obj_possuído, gênero_obj_possuído,
                                                       pessoa_da_interlocução_proximidade,  #
                                                       funcaoNumerativo, cardinal, genero, tipo_precisa, tipoRealCard,
                                                       milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                                       numIndefinido,
                                                       tipo_de_Ente, tipo_de_nao_consciente,
                                                       tipo_de_nao_consciente_material,
                                                       tipo_de_nao_consciente_semiotico, classe_palavra_Ente,
                                                       substantivo_lematizado, numero,
                                                       tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio,
                                                       pessoa_da_interlocucao,
                                                       transitividade_verbo, tonicidade, morfologia_do_pronome,
                                                       reflexivo,  #
                                                       temQualificador, tipoQualificador, adjetivo_epiteto,
                                                       adjetivo_classificador, generoAdjetivo, numeroAdjetivo,
                                                       contracao)

            GN = " ".join((Nucleo_logico, Qualificador))
        return (re.sub(' +', ' ', GN).strip())
    except:
        GN = ''
        return GN


estrutura_GN(DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA', gênero_alpha='masculino',
             número_alpha='singular', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
             pessoa_da_interlocução_possuidor='1s', número_obj_possuído='plural', gênero_obj_possuído='masculino',
             genero='não-binário', tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
             tipo_de_nao_consciente_material='instituição', classe_palavra_Ente='substantivo_comum',
             substantivo_lematizado='desmatamento', numero='singular')

estrutura_GN(None, None, None, None, DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
             gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
             pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
             genero='não-binário', tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
             tipo_de_nao_consciente_material='instituição', classe_palavra_Ente='substantivo_comum',
             substantivo_lematizado='desmatamento', numero='singular',
             tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
             transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
             adjetivo_epiteto=None, adjetivo_classificador=None, generoAdjetivo=None,
             numeroAdjetivo='singular', contracao=None)

estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None,
             DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
             morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='NA',
             gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
             pessoa_da_interlocução_possuidor='1s', número_obj_possuído='singular', gênero_obj_possuído='masculino',
             pessoa_da_interlocução_proximidade='próximo_ao_falante', funcaoNumerativo=None, cardinal=None,
             genero='não-binário',
             tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None,
             unidadeExtenso=None, numIndefinido=None, tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
             tipo_de_nao_consciente_material='abstração_material', tipo_de_nao_consciente_semiotico=None,
             classe_palavra_Ente='substantivo_comum', substantivo_lematizado='piano', numero='singular',
             tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
             transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
             adjetivo_epiteto=None, adjetivo_classificador=None, generoAdjetivo=None,
             numeroAdjetivo=None, contracao=None)

estrutura_GN(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None, indicePreposicaoQualif=None,
             DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None, número_beta=None,
             morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha='específico',
             ORIENTAÇÃO_alpha='orientação_específica_pessoa',
             gênero_alpha='masculino', número_alpha='singular', morfologia_do_pronome_alpha=None,
             pessoa_da_interlocução_possuidor='1s', número_obj_possuído='singular', gênero_obj_possuído='masculino',
             pessoa_da_interlocução_proximidade='próximo_ao_falante', funcaoNumerativo=None, cardinal=None,
             genero='não-binário',
             tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None, dezenaExtenso=None,
             unidadeExtenso=None, numIndefinido=None, tipo_de_Ente=None, tipo_de_nao_consciente=None,
             tipo_de_nao_consciente_material=None, tipo_de_nao_consciente_semiotico=None,
             classe_palavra_Ente=None, substantivo_lematizado=None, numero=None,
             tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
             transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,
             adjetivo_epiteto=None, adjetivo_classificador=None, generoAdjetivo=None,
             numeroAdjetivo=None, contracao=None)

estrutura_GN(None, None, None, None,
             None, None, None, None,
             None, 'específico', 'NA',
             'masculino', 'singular', None,
             None, None, None,
             None, None, None, 'não-binário',
             None, None, None, None, None,
             None, None, 'não_consciente', 'material',
             'abstração_material', None,
             'substantivo_comum', 'moço', 'singular',
             None, None, None, None, None,
             None, None, None, None,
             None, None, None,
             None, None)


# # ########PREPOSIÇÃO
# preposicoes = ['a','ante','após','até','com','contra',
# 				   'de','desde','em','entre','para','por','perante','sem',
# 				   'sob','sobre','trás']


def estrutura_GN_downraked(dissocEnteNucleo=None, temQualificador=None, tipoQualificador=None,
                           indicePreposicaoQualif=None,
                           DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None, gênero_beta=None,
                           número_beta=None,
                           morfologia_do_pronome_beta=None, DETERMINAÇÃO_espeficifidade_alpha=None,
                           ORIENTAÇÃO_alpha=None,
                           gênero_alpha=None, número_alpha=None, morfologia_do_pronome_alpha=None,
                           pessoa_da_interlocução_possuidor=None, número_obj_possuído=None, gênero_obj_possuído=None,
                           pessoa_da_interlocução_proximidade=None, funcaoNumerativo=None, cardinal=None, genero=None,
                           tipo_precisa=None, tipoRealCard=None, milharExtenso=None, centenaExtenso=None,
                           dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
                           tipo_de_Ente=None, tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
                           tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente=None, substantivo_lematizado=None,
                           numero=None, tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None,
                           pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
                           morfologia_do_pronome=None,
                           reflexivo=None, adjetivo_epiteto=None,
                           adjetivo_classificador=None, generoAdjetivo=None, numeroAdjetivo=None, contracao=None):
    GN_downranked = estrutura_GN(dissocEnteNucleo, temQualificador, tipoQualificador, indicePreposicaoQualif,
                                 DETERMINAÇÃO_espeficifidade_beta, ORIENTAÇÃO_beta, gênero_beta, número_beta,
                                 morfologia_do_pronome_beta, DETERMINAÇÃO_espeficifidade_alpha, ORIENTAÇÃO_alpha,
                                 gênero_alpha, número_alpha, morfologia_do_pronome_alpha,
                                 pessoa_da_interlocução_possuidor, número_obj_possuído, gênero_obj_possuído,
                                 pessoa_da_interlocução_proximidade, funcaoNumerativo, cardinal, genero, tipo_precisa,
                                 tipoRealCard, milharExtenso, centenaExtenso, dezenaExtenso, unidadeExtenso,
                                 numIndefinido, tipo_de_Ente, tipo_de_nao_consciente, tipo_de_nao_consciente_material,
                                 tipo_de_nao_consciente_semiotico, classe_palavra_Ente, substantivo_lematizado, numero,
                                 tipo_feminino_ÃO, tipo_masc_ÃO, acentTonica, nomeProprio, pessoa_da_interlocucao,
                                 transitividade_verbo, tonicidade, morfologia_do_pronome, reflexivo, adjetivo_epiteto,
                                 adjetivo_classificador, generoAdjetivo, numeroAdjetivo, contracao)

    return re.sub(' +', ' ', GN_downranked).strip()

# estrutura_GN_downraked()
# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='masculino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='masculino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='masculino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='gato', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			adjetivo_epiteto='bonito',
# 			 adjetivo_classificador=None,
# 					   generoAdjetivo='masculino', numeroAdjetivo='singular',contracao='+contação')
#
# estrutura_GN_downraked(dissocEnteNucleo=None,temQualificador=None,tipoQualificador=None,indicePreposicao=0,
# 			 DETERMINAÇÃO_espeficifidade_beta=None, ORIENTAÇÃO_beta=None,
# 			 gênero_beta=None, número_beta=None, morfologia_do_pronome_beta=None,
# 			 DETERMINAÇÃO_espeficifidade_alpha='específico', ORIENTAÇÃO_alpha='orientação_específica_proximidade',
# 			 gênero_alpha='feminino',
# 			 número_alpha='plural', morfologia_do_pronome_alpha='morfologia_terceira_pessoa',
# 			 pessoa_da_interlocução_possuidor='1s',
# 			 número_obj_possuído='plural', gênero_obj_possuído='feminino',
# 			 pessoa_da_interlocução_proximidade='próximo_ao_não_interlocutor',  #
# 			 funcaoNumerativo=None, cardinal=None, genero='feminino', tipo_precisa=None, tipoRealCard=None,
# 			 milharExtenso=None, centenaExtenso=None, dezenaExtenso=None, unidadeExtenso=None, numIndefinido=None,
# 			 tipo_de_Ente='não_consciente', tipo_de_nao_consciente='material',
# 			 tipo_de_nao_consciente_material='animal',
# 			 tipo_de_nao_consciente_semiotico=None, classe_palavra_Ente='substantivo_comum',
# 			 substantivo_lematizado='árvore', numero='plural',
# 			 tipo_feminino_ÃO=None, tipo_masc_ÃO=None, acentTonica=None, nomeProprio=None, pessoa_da_interlocucao=None,
# 			 transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None, reflexivo=None,  #
# 			,adjetivo_epiteto='bonito',
# 			 adjetivo_classificador=None,
# 					   generoAdjetivo='feminino', numeroAdjetivo='plural',contracao='+contação')
# #

# # ####NO CASO A SEGUIR, PODE ACONTECER DE UM GRUPO NOMINAL DESCER DE ORDEM E REALIZAR, POR SUA VEZ,
# # ##ALGUMA FUNÇÃO DENTRO NO GN DO QUAL FAZ PARTE('XÍCARA DE CAFÉ',no qual 'xícara' é um grupo nominal
# # # com função de Numerativo no GN DE PRIMEIRO NÍVEL)
# 	print('Há dissociação entre Ente e Núcleo do GN?')
# 	dissocEnteNucleo = choice.Menu(['sim', 'não']).ask()
