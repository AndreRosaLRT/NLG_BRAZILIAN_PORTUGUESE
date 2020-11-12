###VERBO MODAL

#
# def formação_da_estrutura_do_verbo_modal_não_finito():
# 	'''
#     '''
# 	print("Qual é o verbo modal lematizado desejado?")
#
# 	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
#
# 	if tipo_de_modal == 'dever':
# 		ME = tipo_de_modal[slice(-2)]
# 		MI = realizacao_transitoriedade_do_verbo_não_finito(
#
#
#
# 	elif tipo_de_modal == 'haver':
# 		verbo = formação_verbo_haver_não_finito()
#
# 	return verbo
#
#
# def formação_da_estrutura_do_verbo_modal_finito():
# 	'''
#     '''
# 	print("Qual é o verbo modal lematizado desejado?")
#
# 	tipo_de_modal = choice.Menu(['poder', 'dever', 'haver']).ask()
#
# 	if tipo_de_modal == 'dever':
# 		ME = tipo_de_modal[slice(-2)]
# 		MI = realizacao_transitoriedade_do_verbo_finito()
# 		verbo = ME + MI
#
#
#
# 	elif tipo_de_modal == 'poder':
# 		verbo = formação_verbo_poder_finito()
#
#
# 	elif tipo_de_modal == 'haver':
# 		verbo = formação_verbo_haver_finito()
#
# 	return verbo
#

#####verboS MODAIS


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

	elif tipo_de_modal == '2':
		return 'haver'

def formacao_da_estrutura_do_verbo_modal(TIPO_DE_EXPERIENCIA_MODAL,verbo_MODAL, tipo_de_orientacao_MODAL, padrao_de_morfologia_MODAL, OI_numero_MODAL,
                                         genero_MODAL, OI_tipo_de_pessoa_MODAL, padrao_pessoa_morfologia_MODAL='Morfologia_padrão'):
	'''
    '''

	if (TIPO_DE_EXPERIENCIA_MODAL == 'Ser' or
			TIPO_DE_EXPERIENCIA_MODAL == 'Fazer' or
			TIPO_DE_EXPERIENCIA_MODAL == 'Sentir'):

		if verbo_MODAL == 'dever':
			ME = verbo_MODAL[slice(-2)]
			MI = realizacao_transitoriedade_do_verbo(tipo_de_orientacao_MODAL, padrao_de_morfologia_MODAL, OI_numero_MODAL, genero_MODAL,
			                                         OI_tipo_de_pessoa_MODAL, padrao_pessoa_morfologia="Morfologia_padrão")
			verbo_MODAL = ME + MI

		elif verbo_MODAL == 'poder':
			verbo_MODAL = formacao_verbo_poder(verbo_MODAL, tipo_de_orientacao_MODAL, padrao_de_morfologia_MODAL,
			                                   OI_numero_MODAL, genero_MODAL, OI_tipo_de_pessoa_MODAL,
			                                   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo_MODAL == 'haver':
			verbo_MODAL = formacao_verbo_haver(verbo_MODAL, tipo_de_orientacao_MODAL, padrao_de_morfologia_MODAL,
			                                   OI_numero_MODAL, genero_MODAL, OI_tipo_de_pessoa_MODAL,
			                                   padrao_pessoa_morfologia='Morfologia_padrão')

		elif verbo_MODAL == 'ter':

			verbo_MODAL = formacao_verbo_ter(verbo_MODAL, tipo_de_orientacao_MODAL, padrao_de_morfologia_MODAL,
			                                 OI_numero_MODAL, genero_MODAL, OI_tipo_de_pessoa_MODAL,
			                                 padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'que'
	# elif verbo == 'ter de':
	# 	verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
	# 	                           OI_numero, genero, OI_tipo_de_pessoa,
	# 	                           padrao_pessoa_morfologia='Morfologia_padrão') + ' ' + 'de'
	return verbo_MODAL


formacao_da_estrutura_do_verbo_modal('Sentir','poder','presente','-ER','singular',None,'1pessoa')