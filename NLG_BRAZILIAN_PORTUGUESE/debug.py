
def formacao_da_estrutura_do_verbo(verbo, tipo_de_orientacao, padrao_de_morfologia, OI_numero,
                                       genero, OI_tipo_de_pessoa,
                                       padrao_pessoa_morfologia='Morfologia_padrão'):
	'''
    '''

	if verbo == 'estar':
		verbo = formacao_verbo_estar(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                     OI_numero,
		                                     genero, OI_tipo_de_pessoa,
		                                     padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'ter':
		verbo = formacao_verbo_ter(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                   OI_numero,
		                                   genero, OI_tipo_de_pessoa,
		                                   padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'haver':
		verbo = formacao_verbo_haver(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                     OI_numero,
		                                     genero, OI_tipo_de_pessoa,
		                                     padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'ir':
		verbo = formacao_verbo_ir(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                  OI_numero,
		                                  genero, OI_tipo_de_pessoa,
		                                  padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'vir':
		verbo = formacao_verbo_vir_invervir(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                            OI_numero,
		                                            genero, OI_tipo_de_pessoa,
		                                            padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == 'ser':
		verbo = formacao_verbo_ser(verbo, tipo_de_orientacao, padrao_de_morfologia,
		                                   OI_numero,
		                                   genero, OI_tipo_de_pessoa,
		                                   padrao_pessoa_morfologia='Morfologia_padrão')

	elif verbo == None:
		verbo = ''
	else:
		OE_experiencia_do_verbo = experiencia_do_verbo(verbo)
		OI_orientacao_interpessoal_do_verbo = realizacao_transitoriedade_do_verbo(tipo_de_orientacao,
		                                                                          padrao_de_morfologia,
		                                                                          OI_numero,
		                                                                          genero, OI_tipo_de_pessoa,
		                                                                          padrao_pessoa_morfologia)
		verbo = OE_experiencia_do_verbo + OI_orientacao_interpessoal_do_verbo
	return verbo
formacao_da_estrutura_do_verbo('ser','presente','-ER','singular',None,'1pessoa')
formacao_da_estrutura_do_verbo('expor','presente','-OR','singular',None,'1pessoa')

# ###########################################################################
# #########################################################################


formacao_da_estrutura_do_verbo('ser','presente','-AR','singular',None,'1pessoa')
formacao_da_estrutura_do_verbo('andar','pretérito_perfectivo_I','-AR','singular',None,'3pessoa')
formacao_da_estrutura_do_verbo('comer','pretérito_imperfectivo','-ER','plural',None,'1pessoa')
formacao_da_estrutura_do_verbo('expor','presente','-OR','singular',None,'1pessoa')
# formacao_da_estrutura_do_verbo('expor','gerúndio','-OR',None,None,None)
# formacao_da_estrutura_do_verbo('cortar', 'particípio', '-AR', 'singular', 'feminino', None)
#
# TIPO_DE_EXPERIENCIA = ['Ser','Fazer', 'Sentir']
#  funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
# 	                                      'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()
#
