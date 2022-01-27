# # # -*- coding: utf-8 -*-
#
#
# # import json
# # #
# # # dicionario = {
# # # 	"TIPO_DE_EXPERIENCIA_GV": "Fazer",
# # # 	"AGENCIA": "agenciado_passiva",
# # # 	"TIPO_DE_EXPERIENCIA_1": "Ser",
# # # 	"funcao_no_grupo_verbal_1": "Auxiliar",
# # # 	"verbo_1": "estar",
# # # 	"tipo_de_orientacao_1": "pretérito_imperfectivo",
# # # 	"padrao_de_morfologia_1": "-AR",
# # # 	"OI_numero_1": "singular",
# # # 	"genero_1": "None",
# # # 	"OI_tipo_de_pessoa_1": "1pessoa",
# # # 	"padrao_pessoa_morfologia_1": "Morfologia_padrão",
# # # 	"TIPO_DE_EXPERIENCIA_2": "None",
# # # 	"funcao_no_grupo_verbal_2": "None",
# # # 	"verbo_2": "None",
# # # 	"tipo_de_orientacao_2": "None",
# # # 	"padrao_de_morfologia_2": "None",
# # # 	"OI_numero_2": "None",
# # # 	"genero_2": "None",
# # # 	"OI_tipo_de_pessoa_2": "None",
# # # 	"padrao_pessoa_morfologia_2": "None",
# # # 	"TIPO_DE_EXPERIENCIA_3": "None",
# # # 	"funcao_no_grupo_verbal_3": "None",
# # # 	"verbo_3": "None",
# # # 	"tipo_de_orientacao_3": "None",
# # # 	"padrao_de_morfologia_3": "None",
# # # 	"OI_numero_3": "None",
# # # 	"genero_3": "None",
# # # 	"OI_tipo_de_pessoa_3": "None",
# # # 	"padrao_pessoa_morfologia_3": "None",
# # # 	"TIPO_DE_EXPERIENCIA_4": "Ser",
# # # 	"funcao_no_grupo_verbal_4": "Auxiliar",
# # # 	"verbo_4": "ser",
# # # 	"tipo_de_orientacao_4": "gerúndio",
# # # 	"padrao_de_morfologia_4": "-ER",
# # # 	"OI_numero_4": "singular",
# # # 	"genero_4": "None",
# # # 	"OI_tipo_de_pessoa_4": "1pessoa",
# # # 	"padrao_pessoa_morfologia_4": "Morfologia_padrão",
# # # 	"TIPO_DE_EXPERIENCIA_LEX": "Fazer",
# # # 	"funcao_no_grupo_verbal_POS_FINAL": "Evento",
# # # 	"verbo_LEX": "levar",
# # # 	"tipo_de_orientacao_LEX": "particípio",
# # # 	"padrao_de_morfologia_LEX": "-AR",
# # # 	"OI_numero_LEX": "singular",
# # # 	"genero_LEX": "masculino",
# # # 	"OI_tipo_de_pessoa_LEX": "None",
# # # 	"padrao_pessoa_morfologia_LEX": "Morfologia_padrão"
# # # }
# # #
# # # with open('parametros_GV.json', "w") as file:
# # # 	json.dump(dicionario, file, ensure_ascii=False)
# #
# # parametros = json.load(open("./NLG_BRAZILIAN_PORTUGUESE/parametros_GV.json"))
# # # parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_GV"]
# #
# # dicionarioSinonimos=json.load(open("./mineracao_lexicon_pre_exp_aplicacao/dic_sin_cbow2.json"))
# # ##PARAMETROS DO JSON PARA A FUNÇÃO
# #
# # grupo_teste = grupo_verbal(parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][0]["AGENCIA"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][0]["funcao_no_grupo_verbal_1"], parametros["GVs"][0]["verbo_1"], parametros["GVs"][0]["tipo_de_orientacao_1"], parametros["GVs"][0]["padrao_de_morfologia_1"], parametros["GVs"][0]["OI_numero_1"], parametros["GVs"][0]["genero_1"], parametros["GVs"][0]["OI_tipo_de_pessoa_1"], parametros["GVs"][0]["padrao_pessoa_morfologia_1"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][0]["funcao_no_grupo_verbal_2"], parametros["GVs"][0]["verbo_2"], parametros["GVs"][0]["tipo_de_orientacao_2"], parametros["GVs"][0]["padrao_de_morfologia_2"], parametros["GVs"][0]["OI_numero_2"], parametros["GVs"][0]["genero_2"], parametros["GVs"][0]["OI_tipo_de_pessoa_2"], parametros["GVs"][0]["padrao_pessoa_morfologia_2"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][0]["funcao_no_grupo_verbal_3"], parametros["GVs"][0]["verbo_3"], parametros["GVs"][0]["tipo_de_orientacao_3"], parametros["GVs"][0]["padrao_de_morfologia_3"], parametros["GVs"][0]["OI_numero_3"], parametros["GVs"][0]["genero_3"], parametros["GVs"][0]["OI_tipo_de_pessoa_3"], parametros["GVs"][0]["padrao_pessoa_morfologia_3"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][0]["funcao_no_grupo_verbal_4"], parametros["GVs"][0]["verbo_4"], parametros["GVs"][0]["tipo_de_orientacao_4"], parametros["GVs"][0]["padrao_de_morfologia_4"], parametros["GVs"][0]["OI_numero_4"], parametros["GVs"][0]["genero_4"], parametros["GVs"][0]["OI_tipo_de_pessoa_4"], parametros["GVs"][0]["padrao_pessoa_morfologia_4"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][0]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][0]["verbo_LEX"], parametros["GVs"][0]["tipo_de_orientacao_LEX"], parametros["GVs"][0]["padrao_de_morfologia_LEX"], parametros["GVs"][0]["OI_numero_LEX"], parametros["GVs"][0]["genero_LEX"], parametros["GVs"][0]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][0]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste)
# #
# # grupo_teste_2 = grupo_verbal(parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][1]["AGENCIA"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][1]["funcao_no_grupo_verbal_1"], parametros["GVs"][1]["verbo_1"], parametros["GVs"][1]["tipo_de_orientacao_1"], parametros["GVs"][1]["padrao_de_morfologia_1"], parametros["GVs"][1]["OI_numero_1"], parametros["GVs"][1]["genero_1"], parametros["GVs"][1]["OI_tipo_de_pessoa_1"], parametros["GVs"][1]["padrao_pessoa_morfologia_1"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][1]["funcao_no_grupo_verbal_2"], parametros["GVs"][1]["verbo_2"], parametros["GVs"][1]["tipo_de_orientacao_2"], parametros["GVs"][1]["padrao_de_morfologia_2"], parametros["GVs"][1]["OI_numero_2"], parametros["GVs"][1]["genero_2"], parametros["GVs"][1]["OI_tipo_de_pessoa_2"], parametros["GVs"][1]["padrao_pessoa_morfologia_2"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][1]["funcao_no_grupo_verbal_3"], parametros["GVs"][1]["verbo_3"], parametros["GVs"][1]["tipo_de_orientacao_3"], parametros["GVs"][1]["padrao_de_morfologia_3"], parametros["GVs"][1]["OI_numero_3"], parametros["GVs"][1]["genero_3"], parametros["GVs"][1]["OI_tipo_de_pessoa_3"], parametros["GVs"][1]["padrao_pessoa_morfologia_3"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][1]["funcao_no_grupo_verbal_4"], parametros["GVs"][1]["verbo_4"], parametros["GVs"][1]["tipo_de_orientacao_4"], parametros["GVs"][1]["padrao_de_morfologia_4"], parametros["GVs"][1]["OI_numero_4"], parametros["GVs"][1]["genero_4"], parametros["GVs"][1]["OI_tipo_de_pessoa_4"], parametros["GVs"][1]["padrao_pessoa_morfologia_4"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][1]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][1]["verbo_LEX"], parametros["GVs"][1]["tipo_de_orientacao_LEX"], parametros["GVs"][1]["padrao_de_morfologia_LEX"], parametros["GVs"][1]["OI_numero_LEX"], parametros["GVs"][1]["genero_LEX"], parametros["GVs"][1]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][1]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_2)
# #
# # grupo_teste_3 = grupo_verbal(parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][2]["AGENCIA"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][2]["funcao_no_grupo_verbal_1"], parametros["GVs"][2]["verbo_1"], parametros["GVs"][2]["tipo_de_orientacao_1"], parametros["GVs"][2]["padrao_de_morfologia_1"], parametros["GVs"][2]["OI_numero_1"], parametros["GVs"][2]["genero_1"], parametros["GVs"][2]["OI_tipo_de_pessoa_1"], parametros["GVs"][2]["padrao_pessoa_morfologia_1"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][2]["funcao_no_grupo_verbal_2"], parametros["GVs"][2]["verbo_2"], parametros["GVs"][2]["tipo_de_orientacao_2"], parametros["GVs"][2]["padrao_de_morfologia_2"], parametros["GVs"][2]["OI_numero_2"], parametros["GVs"][2]["genero_2"], parametros["GVs"][2]["OI_tipo_de_pessoa_2"], parametros["GVs"][2]["padrao_pessoa_morfologia_2"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][2]["funcao_no_grupo_verbal_3"], parametros["GVs"][2]["verbo_3"], parametros["GVs"][2]["tipo_de_orientacao_3"], parametros["GVs"][2]["padrao_de_morfologia_3"], parametros["GVs"][2]["OI_numero_3"], parametros["GVs"][2]["genero_3"], parametros["GVs"][2]["OI_tipo_de_pessoa_3"], parametros["GVs"][2]["padrao_pessoa_morfologia_3"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][2]["funcao_no_grupo_verbal_4"], parametros["GVs"][2]["verbo_4"], parametros["GVs"][2]["tipo_de_orientacao_4"], parametros["GVs"][2]["padrao_de_morfologia_4"], parametros["GVs"][2]["OI_numero_4"], parametros["GVs"][2]["genero_4"], parametros["GVs"][2]["OI_tipo_de_pessoa_4"], parametros["GVs"][2]["padrao_pessoa_morfologia_4"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][2]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][2]["verbo_LEX"], parametros["GVs"][2]["tipo_de_orientacao_LEX"], parametros["GVs"][2]["padrao_de_morfologia_LEX"], parametros["GVs"][2]["OI_numero_LEX"], parametros["GVs"][2]["genero_LEX"], parametros["GVs"][2]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][2]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_3)
# #
# # for entrada in dicionarioSinonimos:
# # 	print(entrada)
# #
# # 	for verbo in dicionarioSinonimos[entrada]:
# # 		padraoMorfologia = detecta_padrao_morfologia(verbo)
# # 		grupo_teste_3 = grupo_verbal(parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][2]["AGENCIA"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_1"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_1"], parametros["GVs"][2]["verbo_1"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_1"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_1"], parametros["GVs"][2]["OI_numero_1"],
# # 		                             parametros["GVs"][2]["genero_1"], parametros["GVs"][2]["OI_tipo_de_pessoa_1"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_1"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_2"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_2"], parametros["GVs"][2]["verbo_2"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_2"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_2"], parametros["GVs"][2]["OI_numero_2"],
# # 		                             parametros["GVs"][2]["genero_2"], parametros["GVs"][2]["OI_tipo_de_pessoa_2"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_2"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_3"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_3"], parametros["GVs"][2]["verbo_3"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_3"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_3"], parametros["GVs"][2]["OI_numero_3"],
# # 		                             parametros["GVs"][2]["genero_3"], parametros["GVs"][2]["OI_tipo_de_pessoa_3"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_3"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_4"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_4"], parametros["GVs"][2]["verbo_4"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_4"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_4"], parametros["GVs"][2]["OI_numero_4"],
# # 		                             parametros["GVs"][2]["genero_4"], parametros["GVs"][2]["OI_tipo_de_pessoa_4"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_4"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_LEX"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_POS_FINAL"],
# # 		                            verbo, parametros["GVs"][2]["tipo_de_orientacao_LEX"],
# # 		                             padraoMorfologia,
# # 		                             parametros["GVs"][2]["OI_numero_LEX"], parametros["GVs"][2]["genero_LEX"],
# # 		                             parametros["GVs"][2]["OI_tipo_de_pessoa_LEX"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_LEX"])
# # 		print(grupo_teste_3)
# #
# # grupo_teste_4 = grupo_verbal(parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][3]["AGENCIA"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][3]["funcao_no_grupo_verbal_1"], parametros["GVs"][3]["verbo_1"], parametros["GVs"][3]["tipo_de_orientacao_1"], parametros["GVs"][3]["padrao_de_morfologia_1"], parametros["GVs"][3]["OI_numero_1"], parametros["GVs"][3]["genero_1"], parametros["GVs"][3]["OI_tipo_de_pessoa_1"], parametros["GVs"][3]["padrao_pessoa_morfologia_1"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][3]["funcao_no_grupo_verbal_2"], parametros["GVs"][3]["verbo_2"], parametros["GVs"][3]["tipo_de_orientacao_2"], parametros["GVs"][3]["padrao_de_morfologia_2"], parametros["GVs"][3]["OI_numero_2"], parametros["GVs"][3]["genero_2"], parametros["GVs"][3]["OI_tipo_de_pessoa_2"], parametros["GVs"][3]["padrao_pessoa_morfologia_2"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][3]["funcao_no_grupo_verbal_3"], parametros["GVs"][3]["verbo_3"], parametros["GVs"][3]["tipo_de_orientacao_3"], parametros["GVs"][3]["padrao_de_morfologia_3"], parametros["GVs"][3]["OI_numero_3"], parametros["GVs"][3]["genero_3"], parametros["GVs"][3]["OI_tipo_de_pessoa_3"], parametros["GVs"][3]["padrao_pessoa_morfologia_3"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][3]["funcao_no_grupo_verbal_4"], parametros["GVs"][3]["verbo_4"], parametros["GVs"][3]["tipo_de_orientacao_4"], parametros["GVs"][3]["padrao_de_morfologia_4"], parametros["GVs"][3]["OI_numero_4"], parametros["GVs"][3]["genero_4"], parametros["GVs"][3]["OI_tipo_de_pessoa_4"], parametros["GVs"][3]["padrao_pessoa_morfologia_4"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][3]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][3]["verbo_LEX"], parametros["GVs"][3]["tipo_de_orientacao_LEX"], parametros["GVs"][3]["padrao_de_morfologia_LEX"], parametros["GVs"][3]["OI_numero_LEX"], parametros["GVs"][3]["genero_LEX"], parametros["GVs"][3]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][3]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_4)
# #
# # grupo_teste_5 = grupo_verbal(parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][4]["AGENCIA"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][4]["funcao_no_grupo_verbal_1"], parametros["GVs"][4]["verbo_1"], parametros["GVs"][4]["tipo_de_orientacao_1"], parametros["GVs"][4]["padrao_de_morfologia_1"], parametros["GVs"][4]["OI_numero_1"], parametros["GVs"][4]["genero_1"], parametros["GVs"][4]["OI_tipo_de_pessoa_1"], parametros["GVs"][4]["padrao_pessoa_morfologia_1"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][4]["funcao_no_grupo_verbal_2"], parametros["GVs"][4]["verbo_2"], parametros["GVs"][4]["tipo_de_orientacao_2"], parametros["GVs"][4]["padrao_de_morfologia_2"], parametros["GVs"][4]["OI_numero_2"], parametros["GVs"][4]["genero_2"], parametros["GVs"][4]["OI_tipo_de_pessoa_2"], parametros["GVs"][4]["padrao_pessoa_morfologia_2"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][4]["funcao_no_grupo_verbal_3"], parametros["GVs"][4]["verbo_3"], parametros["GVs"][4]["tipo_de_orientacao_3"], parametros["GVs"][4]["padrao_de_morfologia_3"], parametros["GVs"][4]["OI_numero_3"], parametros["GVs"][4]["genero_3"], parametros["GVs"][4]["OI_tipo_de_pessoa_3"], parametros["GVs"][4]["padrao_pessoa_morfologia_3"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][4]["funcao_no_grupo_verbal_4"], parametros["GVs"][4]["verbo_4"], parametros["GVs"][4]["tipo_de_orientacao_4"], parametros["GVs"][4]["padrao_de_morfologia_4"], parametros["GVs"][4]["OI_numero_4"], parametros["GVs"][4]["genero_4"], parametros["GVs"][4]["OI_tipo_de_pessoa_4"], parametros["GVs"][4]["padrao_pessoa_morfologia_4"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][4]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][4]["verbo_LEX"], parametros["GVs"][4]["tipo_de_orientacao_LEX"], parametros["GVs"][4]["padrao_de_morfologia_LEX"], parametros["GVs"][4]["OI_numero_LEX"], parametros["GVs"][4]["genero_LEX"], parametros["GVs"][4]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][4]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_5)
# #
# #
# # grupo_teste_6 = grupo_verbal(parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][5]["AGENCIA"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][5]["funcao_no_grupo_verbal_1"], parametros["GVs"][5]["verbo_1"], parametros["GVs"][5]["tipo_de_orientacao_1"], parametros["GVs"][5]["padrao_de_morfologia_1"], parametros["GVs"][5]["OI_numero_1"], parametros["GVs"][5]["genero_1"], parametros["GVs"][5]["OI_tipo_de_pessoa_1"], parametros["GVs"][5]["padrao_pessoa_morfologia_1"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][5]["funcao_no_grupo_verbal_2"], parametros["GVs"][5]["verbo_2"], parametros["GVs"][5]["tipo_de_orientacao_2"], parametros["GVs"][5]["padrao_de_morfologia_2"], parametros["GVs"][5]["OI_numero_2"], parametros["GVs"][5]["genero_2"], parametros["GVs"][5]["OI_tipo_de_pessoa_2"], parametros["GVs"][5]["padrao_pessoa_morfologia_2"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][5]["funcao_no_grupo_verbal_3"], parametros["GVs"][5]["verbo_3"], parametros["GVs"][5]["tipo_de_orientacao_3"], parametros["GVs"][5]["padrao_de_morfologia_3"], parametros["GVs"][5]["OI_numero_3"], parametros["GVs"][5]["genero_3"], parametros["GVs"][5]["OI_tipo_de_pessoa_3"], parametros["GVs"][5]["padrao_pessoa_morfologia_3"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][5]["funcao_no_grupo_verbal_4"], parametros["GVs"][5]["verbo_4"], parametros["GVs"][5]["tipo_de_orientacao_4"], parametros["GVs"][5]["padrao_de_morfologia_4"], parametros["GVs"][5]["OI_numero_4"], parametros["GVs"][5]["genero_4"], parametros["GVs"][5]["OI_tipo_de_pessoa_4"], parametros["GVs"][5]["padrao_pessoa_morfologia_4"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][5]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][5]["verbo_LEX"], parametros["GVs"][5]["tipo_de_orientacao_LEX"], parametros["GVs"][5]["padrao_de_morfologia_LEX"], parametros["GVs"][5]["OI_numero_LEX"], parametros["GVs"][5]["genero_LEX"], parametros["GVs"][5]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][5]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_6)
# #
# # grupo_teste_7 = grupo_verbal(parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][6]["AGENCIA"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][6]["funcao_no_grupo_verbal_1"], parametros["GVs"][6]["verbo_1"], parametros["GVs"][6]["tipo_de_orientacao_1"], parametros["GVs"][6]["padrao_de_morfologia_1"], parametros["GVs"][6]["OI_numero_1"], parametros["GVs"][6]["genero_1"], parametros["GVs"][6]["OI_tipo_de_pessoa_1"], parametros["GVs"][6]["padrao_pessoa_morfologia_1"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][6]["funcao_no_grupo_verbal_2"], parametros["GVs"][6]["verbo_2"], parametros["GVs"][6]["tipo_de_orientacao_2"], parametros["GVs"][6]["padrao_de_morfologia_2"], parametros["GVs"][6]["OI_numero_2"], parametros["GVs"][6]["genero_2"], parametros["GVs"][6]["OI_tipo_de_pessoa_2"], parametros["GVs"][6]["padrao_pessoa_morfologia_2"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][6]["funcao_no_grupo_verbal_3"], parametros["GVs"][6]["verbo_3"], parametros["GVs"][6]["tipo_de_orientacao_3"], parametros["GVs"][6]["padrao_de_morfologia_3"], parametros["GVs"][6]["OI_numero_3"], parametros["GVs"][6]["genero_3"], parametros["GVs"][6]["OI_tipo_de_pessoa_3"], parametros["GVs"][6]["padrao_pessoa_morfologia_3"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][6]["funcao_no_grupo_verbal_4"], parametros["GVs"][6]["verbo_4"], parametros["GVs"][6]["tipo_de_orientacao_4"], parametros["GVs"][6]["padrao_de_morfologia_4"], parametros["GVs"][6]["OI_numero_4"], parametros["GVs"][6]["genero_4"], parametros["GVs"][6]["OI_tipo_de_pessoa_4"], parametros["GVs"][6]["padrao_pessoa_morfologia_4"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][6]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][6]["verbo_LEX"], parametros["GVs"][6]["tipo_de_orientacao_LEX"], parametros["GVs"][6]["padrao_de_morfologia_LEX"], parametros["GVs"][6]["OI_numero_LEX"], parametros["GVs"][6]["genero_LEX"], parametros["GVs"][6]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][6]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_7)
# #
# # grupo_teste_8 = grupo_verbal(parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][7]["AGENCIA"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][7]["funcao_no_grupo_verbal_1"], parametros["GVs"][7]["verbo_1"], parametros["GVs"][7]["tipo_de_orientacao_1"], parametros["GVs"][7]["padrao_de_morfologia_1"], parametros["GVs"][7]["OI_numero_1"], parametros["GVs"][7]["genero_1"], parametros["GVs"][7]["OI_tipo_de_pessoa_1"], parametros["GVs"][7]["padrao_pessoa_morfologia_1"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][7]["funcao_no_grupo_verbal_2"], parametros["GVs"][7]["verbo_2"], parametros["GVs"][7]["tipo_de_orientacao_2"], parametros["GVs"][7]["padrao_de_morfologia_2"], parametros["GVs"][7]["OI_numero_2"], parametros["GVs"][7]["genero_2"], parametros["GVs"][7]["OI_tipo_de_pessoa_2"], parametros["GVs"][7]["padrao_pessoa_morfologia_2"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][7]["funcao_no_grupo_verbal_3"], parametros["GVs"][7]["verbo_3"], parametros["GVs"][7]["tipo_de_orientacao_3"], parametros["GVs"][7]["padrao_de_morfologia_3"], parametros["GVs"][7]["OI_numero_3"], parametros["GVs"][7]["genero_3"], parametros["GVs"][7]["OI_tipo_de_pessoa_3"], parametros["GVs"][7]["padrao_pessoa_morfologia_3"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][7]["funcao_no_grupo_verbal_4"], parametros["GVs"][7]["verbo_4"], parametros["GVs"][7]["tipo_de_orientacao_4"], parametros["GVs"][7]["padrao_de_morfologia_4"], parametros["GVs"][7]["OI_numero_4"], parametros["GVs"][7]["genero_4"], parametros["GVs"][7]["OI_tipo_de_pessoa_4"], parametros["GVs"][7]["padrao_pessoa_morfologia_4"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][7]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][7]["verbo_LEX"], parametros["GVs"][7]["tipo_de_orientacao_LEX"], parametros["GVs"][7]["padrao_de_morfologia_LEX"], parametros["GVs"][7]["OI_numero_LEX"], parametros["GVs"][7]["genero_LEX"], parametros["GVs"][7]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][7]["padrao_pessoa_morfologia_LEX"])
# # print(grupo_teste_8)
# # ######################################
# # #####################################
# # ####################################
# # ######################################
# # dicionarioSinonimos["apresentar"]
# #
# # ##exemplo passiva
# # for entrada in dicionarioSinonimos:
# # 	print(entrada)
# #
# # 	for verbo in dicionarioSinonimos[entrada]:
# # 		padraoMorfologia = detecta_padrao_morfologia(verbo)
# # 		grupo_teste = grupo_verbal(parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][2]["AGENCIA"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_1"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_1"], parametros["GVs"][2]["verbo_1"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_1"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_1"],
# # 		                             parametros["GVs"][2]["OI_numero_1"],
# # 		                             parametros["GVs"][2]["genero_1"], parametros["GVs"][2]["OI_tipo_de_pessoa_1"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_1"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_2"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_2"], parametros["GVs"][2]["verbo_2"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_2"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_2"],
# # 		                             parametros["GVs"][2]["OI_numero_2"],
# # 		                             parametros["GVs"][2]["genero_2"], parametros["GVs"][2]["OI_tipo_de_pessoa_2"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_2"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_3"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_3"], parametros["GVs"][2]["verbo_3"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_3"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_3"],
# # 		                             parametros["GVs"][2]["OI_numero_3"],
# # 		                             parametros["GVs"][2]["genero_3"], parametros["GVs"][2]["OI_tipo_de_pessoa_3"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_3"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_4"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_4"], parametros["GVs"][2]["verbo_4"],
# # 		                             parametros["GVs"][2]["tipo_de_orientacao_4"],
# # 		                             parametros["GVs"][2]["padrao_de_morfologia_4"],
# # 		                             parametros["GVs"][2]["OI_numero_4"],
# # 		                             parametros["GVs"][2]["genero_4"], parametros["GVs"][2]["OI_tipo_de_pessoa_4"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_4"],
# # 		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_LEX"],
# # 		                             parametros["GVs"][2]["funcao_no_grupo_verbal_POS_FINAL"],
# # 		                             verbo, parametros["GVs"][2]["tipo_de_orientacao_LEX"],
# # 		                             padraoMorfologia,
# # 		                             parametros["GVs"][2]["OI_numero_LEX"], parametros["GVs"][2]["genero_LEX"],
# # 		                             parametros["GVs"][2]["OI_tipo_de_pessoa_LEX"],
# # 		                             parametros["GVs"][2]["padrao_pessoa_morfologia_LEX"])
# # 		print(grupo_teste)
# #
# #
# # #exemplos ativo
# # # for entrada in dicionarioSinonimos:
# # # 	print(entrada)
# # # 	for verbo in dicionarioSinonimos[entrada]:
# # # 		padraoMorfologia = detecta_padrao_morfologia(verbo)
# # # 		grupo_teste_4 = grupo_verbal(parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][3]["AGENCIA"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][3]["funcao_no_grupo_verbal_1"], parametros["GVs"][3]["verbo_1"], parametros["GVs"][3]["tipo_de_orientacao_1"], parametros["GVs"][3]["padrao_de_morfologia_1"], parametros["GVs"][3]["OI_numero_1"], parametros["GVs"][3]["genero_1"], parametros["GVs"][3]["OI_tipo_de_pessoa_1"], parametros["GVs"][3]["padrao_pessoa_morfologia_1"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][3]["funcao_no_grupo_verbal_2"], parametros["GVs"][3]["verbo_2"], parametros["GVs"][3]["tipo_de_orientacao_2"], parametros["GVs"][3]["padrao_de_morfologia_2"], parametros["GVs"][3]["OI_numero_2"], parametros["GVs"][3]["genero_2"], parametros["GVs"][3]["OI_tipo_de_pessoa_2"], parametros["GVs"][3]["padrao_pessoa_morfologia_2"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][3]["funcao_no_grupo_verbal_3"], parametros["GVs"][3]["verbo_3"], parametros["GVs"][3]["tipo_de_orientacao_3"], parametros["GVs"][3]["padrao_de_morfologia_3"], parametros["GVs"][3]["OI_numero_3"], parametros["GVs"][3]["genero_3"], parametros["GVs"][3]["OI_tipo_de_pessoa_3"], parametros["GVs"][3]["padrao_pessoa_morfologia_3"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][3]["funcao_no_grupo_verbal_4"], parametros["GVs"][3]["verbo_4"], parametros["GVs"][3]["tipo_de_orientacao_4"], parametros["GVs"][3]["padrao_de_morfologia_4"], parametros["GVs"][3]["OI_numero_4"], parametros["GVs"][3]["genero_4"], parametros["GVs"][3]["OI_tipo_de_pessoa_4"], parametros["GVs"][3]["padrao_pessoa_morfologia_4"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][3]["funcao_no_grupo_verbal_POS_FINAL"], verbo, parametros["GVs"][3]["tipo_de_orientacao_LEX"], padraoMorfologia, parametros["GVs"][3]["OI_numero_LEX"], parametros["GVs"][3]["genero_LEX"], parametros["GVs"][3]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][3]["padrao_pessoa_morfologia_LEX"])
# # # 		print (grupo_teste_4)
# #
# #
# #
# #
# # ##################################
# #
# #
# #
# # # # ##TESTE
# # # OI_numeros = ['singular', "plural"]
# # # OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# # # generos=["masculino","feminino"]
# # # conjugacoes=["presente","pretérito_perfectivo_I","pretérito_perfectivo_II","pretérito_imperfectivo","passado_volitivo","futuro","subjuntivo_conjuntivo","subjuntivo_condicional","subjuntivo_optativo","imperativo_I","imperativo_II","não_finito_concretizado","infinitivo","gerúndio","particípio"]
# # # lemaTeste="levar"
# # #
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		for conj in conjugacoes:
# # # 				for genero in generos:
# # # 					print(verbo_geral("Fazer",'Evento','levar',conj,numero,genero,tipo_pessoa))
# #
# # #presente
# # # print("A conjugação é:")
# #
# # for lema in lemas:
# # 	print("LEMA: " + lema)
# # 	for numero in OI_numeros:
# # 		for tipo_pessoa in OI_tipo_pessoas:
# # 			print(verbo_geral("Fazer",'Evento',lema,"presente",numero,None,tipo_pessoa))
# #
# #
# #
# # # # ###
# # # #presente
# # # print("A conjugação é:")
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'presente', '-ER', numero, None, tipo_pessoa))
# # #
# # # ###
# # # print("A conjugação pretérito_perfectivo_I é:")
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # #####pretérito_imperfectivo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # ### "pretérito_perfectivo_II"
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
# # #
# # # ###passado_volitivo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # futuro
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'futuro', '-ER', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_conjuntivo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_condicional
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
# # #
# # # # subjuntivo_optativo
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
# # #
# # # # imperativo_I
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
# # #
# # # # imperativo_II
# # #
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
# # #
# # # # # não_finito_concretizado
# # # for numero in OI_numeros:
# # # 	for tipo_pessoa in OI_tipo_pessoas:
# # # 		print(formacao_verbo_ter('ter', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # # # infinitivo
# # # print(formacao_verbo_ter('ter', 'infinitivo', '-ER', numero, 'feminino', None))
# # #
# # # # # gerúndio
# # # print(formacao_verbo_ter('ter', 'gerúndio', '-ER', None, None, None))
# # # #
# # # # # particípio
# # # generos = ['masculino', 'feminino']
# # # for numero in OI_numeros:
# # # 	for genero in generos:
# # # 		print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None))
# #
# #
# estrutura_gn(dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
#         indice_preposicao_qualif=None, determinacao_especificidade_beta=None, orientacao_beta=None,
#         genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#         determinacao_especificidade_alpha=None, orientacao_alpha=None, genero_alpha=None,numero_alpha=None,
#         morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
#         genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None,
#         cardinal=None, genero_numerativo=None,
#         tipo_de_ente="consciente", tipo_de_nao_consciente=None, tipo_de_nao_consciente_material=None,
#         tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='pronome_caso_reto', substantivo_lematizado=None,
#         numero_subs="singular", genero_subs=None, tipo_feminino_ao=None, tipo_masc_ao=None, acent_tonica=None,
#         nome_proprio=None,
#         pessoa_da_interlocucao="falante", transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
#         reflexivo=None,
#         # classificador
#         adjetivo_classificador=None,
#         # epitetos
#         adj_epit_exp_pre=None,
#         adj_epit_int_pre=None,
#         adj_epit_exp_pos=None,
#         adj_epit_int_pos=None,
#         genero_adjetivo=None, numero_adjetivo=None,
#
#         contracao=None)
#
#
#
#
#
# frase_preposicional(
# indice_preposicao_frase=6, dissoc_ente_nucleo=None, tem_qualificador=None,
#         tipo_qualificador=None, indice_preposicao_qualif=None,
#         determinacao_especificidade_beta=None, orientacao_beta=None, genero_beta=None,
#         numero_beta=None, morfologia_do_pronome_beta=None,
#         determinacao_especificidade_alpha=None, orientacao_alpha=None, genero_alpha=None,
#         numero_alpha=None, morfologia_do_pronome_alpha=None,
#         pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
#         genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None,
#         tipo_numerativo=None, cardinal=None,
#         genero_numerativo=None, tipo_de_ente='não_consciente',
#         tipo_de_nao_consciente='material', tipo_de_nao_consciente_material='abstração_material',
#         tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#         substantivo_lematizado='futebol', numero_subs='singular', genero_subs='não-binário',
#         tipo_feminino_ao=None,
#         tipo_masc_ao=None, acent_tonica=None, nome_proprio=None,
#         pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#         morfologia_do_pronome=None, reflexivo=None,  # classificador
#         adjetivo_classificador=None,
#         # epitetos
#         adj_epit_exp_pre=None,
#         adj_epit_int_pre=None,
#         adj_epit_exp_pos=None,
#         adj_epit_int_pos=None,
#         genero_adjetivo=None, numero_adjetivo=None,
#         contracao=None
# )
#
# estrutura_gn(dissoc_ente_nucleo=None,tem_qualificador=None,tipo_qualificador=None,
#     indice_preposicao_qualif=None,determinacao_especificidade_beta='específico',
#     orientacao_beta='NA',genero_beta='masculino',numero_beta=None,morfologia_do_pronome_beta=None,
#     determinacao_especificidade_alpha='específico',orientacao_alpha='NA',genero_alpha='masculino',
#     numero_alpha='singular',morfologia_do_pronome_alpha=None,pessoa_da_interlocucao_possuidor=None,
#     numero_obj_possuido=None,genero_obj_possuido=None,
#     pessoa_da_interlocucao_proximidade=None,tipo_numerativo=None,cardinal=None,
#     genero_numerativo=None,tipo_de_ente='não_consciente',tipo_de_nao_consciente='material',
#             tipo_de_nao_consciente_material='abstração_material',tipo_de_nao_consciente_semiotico=None,
#             classe_palavra_ente='substantivo_comum',substantivo_lematizado='jogo',numero_subs='singular',
#     genero_subs='masculino',tipo_feminino_ao=None,tipo_masc_ao=None,acent_tonica=None,nome_proprio=None,
#     pessoa_da_interlocucao=None,transitividade_verbo=None,tonicidade=None,morfologia_do_pronome=None,
#     reflexivo=None,
#     adjetivo_classificador=None,
#     adj_epit_exp_pre=None,
#     adj_epit_int_pre=None,
#     adj_epit_exp_pos=None,
#     adj_epit_int_pos=None,
#     genero_adjetivo=None,
#     numero_adjetivo=None,
#     contracao=None)
#
#
# estrutura_gn(dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
#     indice_preposicao_qualif=None, determinacao_especificidade_beta=None, orientacao_beta=None,
#     genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#     determinacao_especificidade_alpha='não_específico', orientacao_alpha='NA', genero_alpha='masculino',
#     numero_alpha='singular',
#     morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
#     genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None,
#     cardinal=None, genero_numerativo=None,
#     tipo_de_ente='consciente', tipo_de_nao_consciente=None,
#     tipo_de_nao_consciente_material=None,
#     tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#     substantivo_lematizado='homem',
#     numero_subs='singular', genero_subs='não-binário', tipo_feminino_ao=None, tipo_masc_ao=None,
#     acent_tonica=None,
#     nome_proprio=None,
#     pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
#     reflexivo=None,
#     # classificador
#     adjetivo_classificador=None,
#     # epitetos
#     adj_epit_exp_pre=None,
#     adj_epit_int_pre=None,
#     adj_epit_exp_pos=None,
#     adj_epit_int_pos=None,
#     genero_adjetivo=None, numero_adjetivo=None,
#
#     contracao=None)
#
# frase_preposicional(indice_preposicao_frase=1, dissoc_ente_nucleo=None, tem_qualificador=None,
#         tipo_qualificador=None,
#         indice_preposicao_qualif=None, determinacao_especificidade_beta='específico',
#         orientacao_beta='NA',
#         genero_beta='masculino', numero_beta=None, morfologia_do_pronome_beta=None,
#         determinacao_especificidade_alpha='específico', orientacao_alpha='NA',
#         genero_alpha='masculino',
#         numero_alpha='singular',
#         morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
#         numero_obj_possuido=None,
#         genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None,
#         cardinal=None, genero_numerativo=None,
#         tipo_de_ente='consciente', tipo_de_nao_consciente=None,
#         tipo_de_nao_consciente_material=None,
#         tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#         substantivo_lematizado='homem',
#         numero_subs='singular', genero_subs='não-binário', tipo_feminino_ao=None,
#         tipo_masc_ao=None,
#         acent_tonica=None,
#         nome_proprio=None,
#         pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#         morfologia_do_pronome=None,
#         reflexivo=None,
#         # classificador
#         adjetivo_classificador=None,
#         # epitetos
#         adj_epit_exp_pre=None,
#         adj_epit_int_pre=None,
#         adj_epit_exp_pos=None,
#         adj_epit_int_pos=None,
#         genero_adjetivo=None, numero_adjetivo=None,
#
#         contracao=None)
#
# for i in range(12):
#     print(frase_preposicional(indice_preposicao_frase=i, dissoc_ente_nucleo=None, tem_qualificador=None,
#                     tipo_qualificador=None,
#                     indice_preposicao_qualif=None, determinacao_especificidade_beta='específico',
#                     orientacao_beta='NA',
#                     genero_beta='feminino', numero_beta=None, morfologia_do_pronome_beta=None,
#                     determinacao_especificidade_alpha='específico', orientacao_alpha='NA',
#                     genero_alpha='feminino',
#                     numero_alpha='singular',
#                     morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
#                     numero_obj_possuido=None,
#                     genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None,
#                     cardinal=None, genero_numerativo=None,
#                     tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
#                     tipo_de_nao_consciente_material='objeto_material',
#                     tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#                     substantivo_lematizado='rua',
#                     numero_subs='singular', genero_subs='não-binário', tipo_feminino_ao=None,
#                     tipo_masc_ao=None,
#                     acent_tonica=None,
#                     nome_proprio=None,
#                     pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#                     morfologia_do_pronome=None,
#                     reflexivo=None,
#                     # classificador
#                     adjetivo_classificador=None,
#                     # epitetos
#                     adj_epit_exp_pre=None,
#                     adj_epit_int_pre=None,
#                     adj_epit_exp_pos=None,
#                     adj_epit_int_pos=None,
#                     genero_adjetivo=None, numero_adjetivo=None,
#
#                     contracao=None))
#
#
#
# frase_preposicional(indice_preposicao_frase=6, dissoc_ente_nucleo=None, tem_qualificador=None,
#                     tipo_qualificador=None,
#                     indice_preposicao_qualif=None, determinacao_especificidade_beta=None,
#                     orientacao_beta='NA',
#                     genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#                     determinacao_especificidade_alpha=None, orientacao_alpha='NA',
#                     genero_alpha=None,
#                     numero_alpha=None,
#                     morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None,
#                     numero_obj_possuido=None,
#                     genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo=None,
#                     cardinal=None, genero_numerativo=None,
#                     tipo_de_ente=None, tipo_de_nao_consciente=None,
#                     tipo_de_nao_consciente_material=None,
#                     tipo_de_nao_consciente_semiotico=None, classe_palavra_ente=None,
#                     substantivo_lematizado=None,
#                     numero_subs=None, genero_subs=None, tipo_feminino_ao=None,
#                     tipo_masc_ao=None,
#                     acent_tonica=None,
#                     nome_proprio=None,
#                     pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None,
#                     morfologia_do_pronome=None,
#                     reflexivo=None,
#                     # classificador
#                     adjetivo_classificador=None,
#                     # epitetos
#                     adj_epit_exp_pre=None,
#                     adj_epit_int_pre=None,
#                     adj_epit_exp_pos='verde',
#                     adj_epit_int_pos=None,
#                     genero_adjetivo='não-binário', numero_adjetivo='singular',
#
#                     contracao=None)
#
#
# teste = oracao_material(
#     # TRANSITIVIDADE
#     tipo_de_processo='Material', indice_material=1, indice_agenciamento=2, indice_relacional=None,
#     indice_atrib=None,
#     # MODO
#     responsabilidade=0, pressuposicao_do_sujeito=0, tipo_modo=1,
#     # TEMA INTERPESSOAL
#     tipo_tema_interpessoal=None, t_inter_tipo_realizacao=None,
#     # TEMA INTERP realizado por grupo adverbial
#     t_inter_tipo_de_adverbio1=None, t_inter_ind_adv_1=None,
#     t_inter_tipo_de_adverbio2=None, t_inter_ind_adv_2=None,
#     t_inter_tipo_de_adverbio3=None, t_inter_ind_adv_3=None,
#     t_inter_tipo_de_adverbio4=None, t_inter_ind_adv_4=None,
#     t_inter_tipo_de_adverbio5=None, t_inter_ind_adv_5=None,
#     #
#     # 		# TEMA INTERPESSOAL realiziado por frase preposicional
#     t_inter_fp_indice_preposicao_frase=None, t_inter_fp_dissoc_ente_nucleo=None, t_inter_fp_tem_qualificador=None,
#     t_inter_fp_tipo_qualificador=None, t_inter_fp_indice_preposicao_qualif=None,
#     t_inter_fp_determinacao_especificidade_beta=None, t_inter_fp_orientacao_beta=None, t_inter_fp_genero_beta=None,
#     t_inter_fp_numero_beta=None,
#     t_inter_fp_morfologia_do_pronome_beta=None, t_inter_fp_determinacao_especificidade_alpha=None,
#     t_inter_fp_orientacao_alpha=None,
#     t_inter_fp_genero_alpha=None, t_inter_fp_numero_alpha=None, t_inter_fp_morfologia_do_pronome_alpha=None,
#     t_inter_fp_pessoa_da_interlocucao_possuidor=None, t_inter_fp_numero_obj_possuido=None,
#     t_inter_fp_genero_obj_possuido=None,
#     t_inter_fp_pessoa_da_interlocucao_proximidade=None, t_inter_fp_tipo_numerativo=None, t_inter_fp_cardinal=None,
#     t_inter_fp_genero_numerativo=None,
#     t_inter_fp_tipo_de_ente=None, t_inter_fp_tipo_de_nao_consciente=None,
#     t_inter_fp_tipo_de_nao_consciente_material=None,
#     t_inter_fp_tipo_de_nao_consciente_semiotico=None, t_inter_fp_classe_palavra_ente=None,
#     t_inter_fp_substantivo_lematizado=None,
#     t_inter_fp_numero_subs=None, t_inter_fp_genero_subs=None, t_inter_fp_tipo_feminino_ao=None,
#     t_inter_fp_tipo_masc_ao=None, t_inter_fp_acent_tonica=None,
#     t_inter_fp_nome_proprio=None, t_inter_fp_pessoa_da_interlocucao=None, t_inter_fp_transitividade_verbo=None,
#     t_inter_fp_tonicidade=None,
#     t_inter_fp_morfologia_do_pronome=None, t_inter_fp_reflexivo=None, t_inter_fp_adjetivo_epiteto=None,
#     t_inter_fp_adjetivo_classificador=None, t_inter_fp_genero_adjetivo=None, t_inter_fp_numero_adjetivo=None,
#     t_inter_fp_contracao=None,
#     #
#     # 		#
#     t_inter_indice_elem_qu=None, t_inter_indice_part_modal=None, t_inter_nome_proprio=None,
#     #
#     # 	#TEMA TEXTUAL
#     t_text_tem_tema_textual=False, t_text_indice_cont=None,
#     t_text_tipo_de_conjuncao=None,
#     t_text_indice_conj=None, t_text_tipo_de_relativo=None,
#     t_text_tipo_pronome_relativo=None, t_text_genero=None, t_text_numero=None,
#     t_text_indice_relativo=None, t_text_indice_relativo_adv=None,
#
#     # TEMA IDEACIONAL
#     orientacao_modal='orientado', orientacao_transitiva='direcional',
#     selecao_tematica='default', tema_default='indicativo',
#     tema_default_indicativo='declarativo', tema_identificativo='NA',
#     tema_angulo=None, tema_elemental=None,
#     tema_proeminente=None,
#     ##Parâmetors específicos do processo_ Mental
#     # FENOMENALIZACAO=None, TIPO_DE_MENTAL=None,
#     ##Parâmetors específicos do processo material
#     # iniciador
#     iniciador=None,
#
#     resultado_qualitativo=None, realizacao_atributo=None,
#     # realizado por adjetivo
#     atributo_adjetivo_lematizado=None, atributo_genero=None, atributo_numero=None,
#     # realizado por frase preposicional
#     atrib_indice_preposicao_frase=6, atrib_dissoc_ente_nucleo=None, atrib_tem_qualificador=None,
#     atrib_tipo_qualificador=None, atrib_indice_preposicao_qualif=None,
#     atrib_determinacao_especificidade_beta=None, atrib_orientacao_beta=None, atrib_genero_beta=None,
#     atrib_numero_beta=None, atrib_morfologia_do_pronome_beta=None,
#     atrib_determinacao_especificidade_alpha=None, atrib_orientacao_alpha=None, atrib_genero_alpha=None,
#     atrib_numero_alpha=None, atrib_morfologia_do_pronome_alpha=None,
#     atrib_pessoa_da_interlocucao_possuidor=None, atrib_numero_obj_possuido=None,
#     atrib_genero_obj_possuido=None, atrib_pessoa_da_interlocucao_proximidade=None,
#     atrib_tipo_numerativo=None, atrib_cardinal=None,
#     atrib_genero_numerativo=None, atrib_tipo_de_ente=None,
#     atrib_tipo_de_nao_consciente=None, atrib_tipo_de_nao_consciente_material=None,
#     atrib_tipo_de_nao_consciente_semiotico=None, atrib_classe_palavra_ente=None,
#     atrib_substantivo_lematizado=None, atrib_numero_subs=None, atrib_genero_subs=None,
#     atrib_tipo_feminino_ao=None,
#     atrib_tipo_masc_ao=None, atrib_acent_tonica=None, atrib_nome_proprio=None,
#     atrib_pessoa_da_interlocucao=None, atrib_transitividade_verbo=None, atrib_tonicidade=None,
#     atrib_morfologia_do_pronome=None, atrib_reflexivo=None,  # classificador
#     atrib_adjetivo_classificador=None,
#     # epitetos
#     atrib_adj_epit_exp_pre=None,
#     atrib_adj_epit_int_pre=None,
#     atrib_adj_epit_exp_pos=None,
#     atrib_adj_epit_int_pos=None,
#     atrib_genero_adjetivo=None, atrib_numero_adjetivo=None,
#     atrib_contracao=None,
#     # ESCOPO
#     escopo=None,
#     # locativo
#     locativo=None,
#     ##extensão beneficiarios
#     beneficiario=None,
#
#     ##processo_
#     tipo_de_experiencia_gv='Fazer', agencia='agenciado_ativa', tipo_de_experiencia_1=None,
#     funcao_no_grupo_verbal_1=None,
#     verbo_1=None, tipo_de_orientacao_1=None, oi_numero_1=None, genero_1=None, oi_tipo_de_pessoa_1=None,
#     padrao_pessoa_morfologia_1=None, tipo_de_experiencia_2=None, funcao_no_grupo_verbal_2=None, verbo_2=None,
#     tipo_de_orientacao_2=None, oi_numero_2=None, genero_2=None, oi_tipo_de_pessoa_2=None,
#     padrao_pessoa_morfologia_2=None, tipo_de_experiencia_3=None, funcao_no_grupo_verbal_3=None, verbo_3=None,
#     tipo_de_orientacao_3=None, oi_numero_3=None, genero_3=None, oi_tipo_de_pessoa_3=None,
#     padrao_pessoa_morfologia_3=None, tipo_de_experiencia_4=None, funcao_no_grupo_verbal_4=None, verbo_4=None,
#     tipo_de_orientacao_4=None, oi_numero_4=None, genero_4=None, oi_tipo_de_pessoa_4=None,
#     padrao_pessoa_morfologia_4=None, tipo_de_experiencia_lex='Fazer', funcao_no_grupo_verbal_pos_final='Evento',
#     verbo_lex='fazer', tipo_de_orientacao_lex='pretérito_perfectivo_I', oi_numero_lex='singular', genero_lex=None,
#     oi_tipo_de_pessoa_lex='3pessoa',
#     padrao_pessoa_morfologia_lex='Morfologia_padrão',
#     # POLARIDADE
#     tipo_polaridade=None,
#     ##PARTICIPANTES
#     # P1
#     p1_dissoc_ente_nucleo=None, p1_tem_qualificador=None, p1_tipo_qualificador=None,
#     p1_indice_preposicao_qualif=None, p1_determinacao_especificidade_beta='específico', p1_orientacao_beta='NA',
#     p1_genero_beta='masculino', p1_numero_beta=None, p1_morfologia_do_pronome_beta=None,
#     p1_determinacao_especificidade_alpha='específico', p1_orientacao_alpha='NA', p1_genero_alpha='masculino',
#     p1_numero_alpha='singular',
#     p1_morfologia_do_pronome_alpha=None, p1_pessoa_da_interlocucao_possuidor=None, p1_numero_obj_possuido=None,
#     p1_genero_obj_possuido=None, p1_pessoa_da_interlocucao_proximidade=None, p1_tipo_numerativo=None,
#     p1_cardinal=None, p1_genero_numerativo=None,
#     p1_tipo_de_ente='consciente', p1_tipo_de_nao_consciente=None,
#     p1_tipo_de_nao_consciente_material=None,
#     p1_tipo_de_nao_consciente_semiotico=None, p1_classe_palavra_ente='substantivo_comum',
#     p1_substantivo_lematizado='homem',
#     p1_numero_subs='singular', p1_genero_subs='não-binário', p1_tipo_feminino_ao=None, p1_tipo_masc_ao=None,
#     p1_acent_tonica=None,
#     p1_nome_proprio=None,
#     p1_pessoa_da_interlocucao=None, p1_transitividade_verbo=None, p1_tonicidade=None, p1_morfologia_do_pronome=None,
#     p1_reflexivo=None,
#     # classificador
#     p1_adjetivo_classificador=None,
#     # epitetos
#     p1_adj_epit_exp_pre=None,
#     p1_adj_epit_int_pre=None,
#     p1_adj_epit_exp_pos=None,
#     p1_adj_epit_int_pos=None,
#     p1_genero_adjetivo=None, p1_numero_adjetivo=None,
#
#     p1_contracao=None,
#     ##PARTICIPANTE P1 REALIZADOS POR FP
#     p1_fp_indice_preposicao_frase=None, p1_fp_dissoc_ente_nucleo=None, p1_fp_tem_qualificador=None,
#     p1_fp_tipo_qualificador=None, p1_fp_indice_preposicao_qualif=None,
#     p1_fp_determinacao_especificidade_beta=None, p1_fp_orientacao_beta=None, p1_fp_genero_beta=None,
#     p1_fp_numero_beta=None, p1_fp_morfologia_do_pronome_beta=None,
#     p1_fp_determinacao_especificidade_alpha=None, p1_fp_orientacao_alpha=None, p1_fp_genero_alpha=None,
#     p1_fp_numero_alpha=None, p1_fp_morfologia_do_pronome_alpha=None,
#     p1_fp_pessoa_da_interlocucao_possuidor=None, p1_fp_numero_obj_possuido=None,
#     p1_fp_genero_obj_possuido=None, p1_fp_pessoa_da_interlocucao_proximidade=None,
#     p1_fp_tipo_numerativo=None, p1_fp_cardinal=None,
#     p1_fp_genero_numerativo=None, p1_fp_tipo_de_ente=None,
#     p1_fp_tipo_de_nao_consciente=None, p1_fp_tipo_de_nao_consciente_material=None,
#     p1_fp_tipo_de_nao_consciente_semiotico=None, p1_fp_classe_palavra_ente=None,
#     p1_fp_substantivo_lematizado=None, p1_fp_numero_subs=None, p1_fp_genero_subs=None,
#     p1_fp_tipo_feminino_ao=None,
#     p1_fp_tipo_masc_ao=None, p1_fp_acent_tonica=None, p1_fp_nome_proprio=None,
#     p1_fp_pessoa_da_interlocucao=None, p1_fp_transitividade_verbo=None, p1_fp_tonicidade=None,
#     p1_fp_morfologia_do_pronome=None, p1_fp_reflexivo=None,  # classificador
#     p1_fp_adjetivo_classificador=None,
#     # epitetos
#     p1_fp_adj_epit_exp_pre=None,
#     p1_fp_adj_epit_int_pre=None,
#     p1_fp_adj_epit_exp_pos=None,
#     p1_fp_adj_epit_int_pos=None,
#     p1_fp_genero_adjetivo=None, p1_fp_numero_adjetivo=None,
#     p1_fp_contracao=None,
#
#     # P2
#     p2_dissoc_ente_nucleo=None, p2_tem_qualificador=None, p2_tipo_qualificador=None,
#     p2_indice_preposicao_qualif=None, p2_determinacao_especificidade_beta=None, p2_orientacao_beta=None,
#     p2_genero_beta=None, p2_numero_beta=None, p2_morfologia_do_pronome_beta=None,
#     p2_determinacao_especificidade_alpha='não_específico', p2_orientacao_alpha='NA', p2_genero_alpha='masculino',
#     p2_numero_alpha='singular',
#     p2_morfologia_do_pronome_alpha=None, p2_pessoa_da_interlocucao_possuidor=None, p2_numero_obj_possuido=None,
#     p2_genero_obj_possuido=None, p2_pessoa_da_interlocucao_proximidade=None, p2_tipo_numerativo=None,
#     p2_cardinal=None, p2_genero_numerativo=None,
#     p2_tipo_de_ente='não_consciente', p2_tipo_de_nao_consciente='material',
#     p2_tipo_de_nao_consciente_material='objeto_material',
#     p2_tipo_de_nao_consciente_semiotico=None, p2_classe_palavra_ente='substantivo_comum',
#     p2_substantivo_lematizado='bolo',
#     p2_numero_subs='singular', p2_genero_subs='não-binário', p2_tipo_feminino_ao=None, p2_tipo_masc_ao=None,
#     p2_acent_tonica=None,
#     p2_nome_proprio=None,
#     p2_pessoa_da_interlocucao=None, p2_transitividade_verbo=None, p2_tonicidade=None, p2_morfologia_do_pronome=None,
#     p2_reflexivo=None,
#     # classificador
#     p2_adjetivo_classificador=None,
#     # epitetos
#     p2_adj_epit_exp_pre=None,
#     p2_adj_epit_int_pre=None,
#     p2_adj_epit_exp_pos=None,
#     p2_adj_epit_int_pos=None,
#     p2_genero_adjetivo=None, p2_numero_adjetivo=None,
#
#     p2_contracao=None,
#     # P3
#     p3_dissoc_ente_nucleo=None, p3_tem_qualificador=None, p3_tipo_qualificador=None,
#     p3_indice_preposicao_qualif=None, p3_determinacao_especificidade_beta=None, p3_orientacao_beta=None,
#     p3_genero_beta=None, p3_numero_beta=None, p3_morfologia_do_pronome_beta=None,
#     p3_determinacao_especificidade_alpha=None, p3_orientacao_alpha=None, p3_genero_alpha=None, p3_numero_alpha=None,
#     p3_morfologia_do_pronome_alpha=None, p3_pessoa_da_interlocucao_possuidor=None, p3_numero_obj_possuido=None,
#     p3_genero_obj_possuido=None, p3_pessoa_da_interlocucao_proximidade=None, p3_tipo_numerativo=None,
#     p3_cardinal=None, p3_genero_numerativo=None,
#     p3_tipo_de_ente=None, p3_tipo_de_nao_consciente=None, p3_tipo_de_nao_consciente_material=None,
#     p3_tipo_de_nao_consciente_semiotico=None, p3_classe_palavra_ente=None, p3_substantivo_lematizado=None,
#     p3_numero_subs=None, p3_genero_subs=None, p3_tipo_feminino_ao=None, p3_tipo_masc_ao=None, p3_acent_tonica=None,
#     p3_nome_proprio=None,
#     p3_pessoa_da_interlocucao=None, p3_transitividade_verbo=None, p3_tonicidade=None, p3_morfologia_do_pronome=None,
#     p3_reflexivo=None,
#     # classificador
#     p3_adjetivo_classificador=None,
#     # epitetos
#     p3_adj_epit_exp_pre=None,
#     p3_adj_epit_int_pre=None,
#     p3_adj_epit_exp_pos=None,
#     p3_adj_epit_int_pos=None,
#     p3_genero_adjetivo=None, p3_numero_adjetivo=None,
#
#     p3_contracao=None,
#
#     ##PARTICIPANTE P3 REALIZADOS POR FP
#     p3_fp_indice_preposicao_frase=None, p3_fp_dissoc_ente_nucleo=None, p3_fp_tem_qualificador=None,
#     p3_fp_tipo_qualificador=None, p3_fp_indice_preposicao_qualif=None,
#     p3_fp_determinacao_especificidade_beta=None, p3_fp_orientacao_beta=None, p3_fp_genero_beta=None,
#     p3_fp_numero_beta=None, p3_fp_morfologia_do_pronome_beta=None,
#     p3_fp_determinacao_especificidade_alpha=None, p3_fp_orientacao_alpha=None, p3_fp_genero_alpha=None,
#     p3_fp_numero_alpha=None, p3_fp_morfologia_do_pronome_alpha=None,
#     p3_fp_pessoa_da_interlocucao_possuidor=None, p3_fp_numero_obj_possuido=None,
#     p3_fp_genero_obj_possuido=None, p3_fp_pessoa_da_interlocucao_proximidade=None,
#     p3_fp_tipo_numerativo=None, p3_fp_cardinal=None,
#     p3_fp_genero_numerativo=None, p3_fp_tipo_de_ente=None,
#     p3_fp_tipo_de_nao_consciente=None, p3_fp_tipo_de_nao_consciente_material=None,
#     p3_fp_tipo_de_nao_consciente_semiotico=None, p3_fp_classe_palavra_ente=None,
#     p3_fp_substantivo_lematizado=None, p3_fp_numero_subs=None, p3_fp_genero_subs=None,
#     p3_fp_tipo_feminino_ao=None,
#     p3_fp_tipo_masc_ao=None, p3_fp_acent_tonica=None, p3_fp_nome_proprio=None,
#     p3_fp_pessoa_da_interlocucao=None, p3_fp_transitividade_verbo=None, p3_fp_tonicidade=None,
#     p3_fp_morfologia_do_pronome=None, p3_fp_reflexivo=None,  # classificador
#     p3_fp_adjetivo_classificador=None,
#     # epitetos
#     p3_fp_adj_epit_exp_pre=None,
#     p3_fp_adj_epit_int_pre=None,
#     p3_fp_adj_epit_exp_pos=None,
#     p3_fp_adj_epit_int_pos=None,
#     p3_fp_genero_adjetivo=None, p3_fp_numero_adjetivo=None,
#     p3_fp_contracao=None,
#     ##CIRCUNSTANCIA
#     circunst_realizacao_circunstancia=None,
#     circunst_indice_preposicao_frase=None, circunst_dissoc_ente_nucleo=None, circunst_tem_qualificador=None,
#     circunst_tipo_qualificador=None, circunst_indice_preposicao_qualif=None,
#     circunst_determinacao_especificidade_beta=None, circunst_orientacao_beta=None, circunst_genero_beta=None,
#     circunst_numero_beta=None,
#     circunst_morfologia_do_pronome_beta=None, circunst_determinacao_especificidade_alpha=None,
#     circunst_orientacao_alpha=None,
#     circunst_genero_alpha=None, circunst_numero_alpha=None, circunst_morfologia_do_pronome_alpha=None,
#     circunst_pessoa_da_interlocucao_possuidor=None, circunst_numero_obj_possuido=None,
#     circunst_genero_obj_possuido=None,
#     circunst_pessoa_da_interlocucao_proximidade=None, circunst_tipo_numerativo=None, circunst_cardinal=None,
#     circunst_genero_numerativo=None,
#     circunst_tipo_de_ente=None, circunst_tipo_de_nao_consciente=None, circunst_tipo_de_nao_consciente_material=None,
#     circunst_tipo_de_nao_consciente_semiotico=None, circunst_classe_palavra_ente=None,
#     circunst_substantivo_lematizado=None,
#     circunst_numero_subs=None, circunst_genero_subs=None, circunst_tipo_feminino_ao=None,
#     circunst_tipo_masc_ao=None, circunst_acent_tonica=None,
#     circunst_nome_proprio=None, circunst_pessoa_da_interlocucao=None, circunst_transitividade_verbo=None,
#     circunst_tonicidade=None,
#     circunst_morfologia_do_pronome=None, circunst_reflexivo=None,
#     # classificador
#     circunst_adjetivo_classificador=None,
#     # epitetos
#     circunst_adj_epit_exp_pre=None,
#     circunst_adj_epit_int_pre=None,
#     circunst_adj_epit_exp_pos=None,
#     circunst_adj_epit_int_pos=None,
#     circunst_genero_adjetivo=None, circunst_numero_adjetivo=None,
#
#     circunst_contracao=None,
#     circunst_tipo_de_adverbio1=None, circunst_adv_ind1=None,
#     circunst_tipo_de_adverbio2=None, circunst_adv_ind2=None,
#     circunst_tipo_de_adverbio3=None, circunst_adv_ind3=None,
#     circunst_tipo_de_adverbio4=None, circunst_adv_ind4=None,
#     circunst_tipo_de_adverbio5=None, circunst_adv_ind5=None
#
# )
#
# estrutura_gn(dissoc_ente_nucleo=None, tem_qualificador=None, tipo_qualificador=None,
#     indice_preposicao_qualif=None, determinacao_especificidade_beta=None, orientacao_beta='NA',
#     genero_beta=None, numero_beta=None, morfologia_do_pronome_beta=None,
#     determinacao_especificidade_alpha=None, orientacao_alpha='NA', genero_alpha='não-binário',
#     numero_alpha='singular',
#     morfologia_do_pronome_alpha=None, pessoa_da_interlocucao_possuidor=None, numero_obj_possuido=None,
#     genero_obj_possuido=None, pessoa_da_interlocucao_proximidade=None, tipo_numerativo='cardinal',
#     cardinal=89000, genero_numerativo='masculino',
#     tipo_de_ente='não_consciente', tipo_de_nao_consciente='material',
#     tipo_de_nao_consciente_material='objeto_material',
#     tipo_de_nao_consciente_semiotico=None, classe_palavra_ente='substantivo_comum',
#     substantivo_lematizado='milímetro',
#     numero_subs='plural', genero_subs='não-binário', tipo_feminino_ao=None, tipo_masc_ao=None,
#     acent_tonica=None,
#     nome_proprio=None,
#     pessoa_da_interlocucao=None, transitividade_verbo=None, tonicidade=None, morfologia_do_pronome=None,
#     reflexivo=None,
#     # classificador
#     adjetivo_classificador=None,
#     # epitetos
#     adj_epit_exp_pre=None,
#     adj_epit_int_pre=None,
#     adj_epit_exp_pos=None,
#     adj_epit_int_pos=None,
#     genero_adjetivo=None, numero_adjetivo=None,
#
#     contracao=None)
#




































# Choveu

