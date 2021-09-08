# -*- coding: utf-8 -*-

import json
#
# dicionario = {
# 	"TIPO_DE_EXPERIENCIA_GV": "Fazer",
# 	"AGENCIA": "agenciado_passiva",
# 	"TIPO_DE_EXPERIENCIA_1": "Ser",
# 	"funcao_no_grupo_verbal_1": "Auxiliar",
# 	"verbo_1": "estar",
# 	"tipo_de_orientacao_1": "pretérito_imperfectivo",
# 	"padrao_de_morfologia_1": "-AR",
# 	"OI_numero_1": "singular",
# 	"genero_1": "None",
# 	"OI_tipo_de_pessoa_1": "1pessoa",
# 	"padrao_pessoa_morfologia_1": "Morfologia_padrão",
# 	"TIPO_DE_EXPERIENCIA_2": "None",
# 	"funcao_no_grupo_verbal_2": "None",
# 	"verbo_2": "None",
# 	"tipo_de_orientacao_2": "None",
# 	"padrao_de_morfologia_2": "None",
# 	"OI_numero_2": "None",
# 	"genero_2": "None",
# 	"OI_tipo_de_pessoa_2": "None",
# 	"padrao_pessoa_morfologia_2": "None",
# 	"TIPO_DE_EXPERIENCIA_3": "None",
# 	"funcao_no_grupo_verbal_3": "None",
# 	"verbo_3": "None",
# 	"tipo_de_orientacao_3": "None",
# 	"padrao_de_morfologia_3": "None",
# 	"OI_numero_3": "None",
# 	"genero_3": "None",
# 	"OI_tipo_de_pessoa_3": "None",
# 	"padrao_pessoa_morfologia_3": "None",
# 	"TIPO_DE_EXPERIENCIA_4": "Ser",
# 	"funcao_no_grupo_verbal_4": "Auxiliar",
# 	"verbo_4": "ser",
# 	"tipo_de_orientacao_4": "gerúndio",
# 	"padrao_de_morfologia_4": "-ER",
# 	"OI_numero_4": "singular",
# 	"genero_4": "None",
# 	"OI_tipo_de_pessoa_4": "1pessoa",
# 	"padrao_pessoa_morfologia_4": "Morfologia_padrão",
# 	"TIPO_DE_EXPERIENCIA_LEX": "Fazer",
# 	"funcao_no_grupo_verbal_POS_FINAL": "Evento",
# 	"verbo_LEX": "levar",
# 	"tipo_de_orientacao_LEX": "particípio",
# 	"padrao_de_morfologia_LEX": "-AR",
# 	"OI_numero_LEX": "singular",
# 	"genero_LEX": "masculino",
# 	"OI_tipo_de_pessoa_LEX": "None",
# 	"padrao_pessoa_morfologia_LEX": "Morfologia_padrão"
# }
#
# with open('parametros_GV.json', "w") as file:
# 	json.dump(dicionario, file, ensure_ascii=False)

parametros = json.load(open("./NLG_BRAZILIAN_PORTUGUESE/parametros_GV.json"))
# parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_GV"]

dicionarioSinonimos=json.load(open("./mineração_lexicon/dic_sin_cbow2.json"))
##PARAMETROS DO JSON PARA A FUNÇÃO

grupo_teste = grupo_verbal(parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][0]["AGENCIA"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][0]["funcao_no_grupo_verbal_1"], parametros["GVs"][0]["verbo_1"], parametros["GVs"][0]["tipo_de_orientacao_1"], parametros["GVs"][0]["padrao_de_morfologia_1"], parametros["GVs"][0]["OI_numero_1"], parametros["GVs"][0]["genero_1"], parametros["GVs"][0]["OI_tipo_de_pessoa_1"], parametros["GVs"][0]["padrao_pessoa_morfologia_1"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][0]["funcao_no_grupo_verbal_2"], parametros["GVs"][0]["verbo_2"], parametros["GVs"][0]["tipo_de_orientacao_2"], parametros["GVs"][0]["padrao_de_morfologia_2"], parametros["GVs"][0]["OI_numero_2"], parametros["GVs"][0]["genero_2"], parametros["GVs"][0]["OI_tipo_de_pessoa_2"], parametros["GVs"][0]["padrao_pessoa_morfologia_2"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][0]["funcao_no_grupo_verbal_3"], parametros["GVs"][0]["verbo_3"], parametros["GVs"][0]["tipo_de_orientacao_3"], parametros["GVs"][0]["padrao_de_morfologia_3"], parametros["GVs"][0]["OI_numero_3"], parametros["GVs"][0]["genero_3"], parametros["GVs"][0]["OI_tipo_de_pessoa_3"], parametros["GVs"][0]["padrao_pessoa_morfologia_3"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][0]["funcao_no_grupo_verbal_4"], parametros["GVs"][0]["verbo_4"], parametros["GVs"][0]["tipo_de_orientacao_4"], parametros["GVs"][0]["padrao_de_morfologia_4"], parametros["GVs"][0]["OI_numero_4"], parametros["GVs"][0]["genero_4"], parametros["GVs"][0]["OI_tipo_de_pessoa_4"], parametros["GVs"][0]["padrao_pessoa_morfologia_4"], parametros["GVs"][0]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][0]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][0]["verbo_LEX"], parametros["GVs"][0]["tipo_de_orientacao_LEX"], parametros["GVs"][0]["padrao_de_morfologia_LEX"], parametros["GVs"][0]["OI_numero_LEX"], parametros["GVs"][0]["genero_LEX"], parametros["GVs"][0]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][0]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste)

grupo_teste_2 = grupo_verbal(parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][1]["AGENCIA"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][1]["funcao_no_grupo_verbal_1"], parametros["GVs"][1]["verbo_1"], parametros["GVs"][1]["tipo_de_orientacao_1"], parametros["GVs"][1]["padrao_de_morfologia_1"], parametros["GVs"][1]["OI_numero_1"], parametros["GVs"][1]["genero_1"], parametros["GVs"][1]["OI_tipo_de_pessoa_1"], parametros["GVs"][1]["padrao_pessoa_morfologia_1"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][1]["funcao_no_grupo_verbal_2"], parametros["GVs"][1]["verbo_2"], parametros["GVs"][1]["tipo_de_orientacao_2"], parametros["GVs"][1]["padrao_de_morfologia_2"], parametros["GVs"][1]["OI_numero_2"], parametros["GVs"][1]["genero_2"], parametros["GVs"][1]["OI_tipo_de_pessoa_2"], parametros["GVs"][1]["padrao_pessoa_morfologia_2"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][1]["funcao_no_grupo_verbal_3"], parametros["GVs"][1]["verbo_3"], parametros["GVs"][1]["tipo_de_orientacao_3"], parametros["GVs"][1]["padrao_de_morfologia_3"], parametros["GVs"][1]["OI_numero_3"], parametros["GVs"][1]["genero_3"], parametros["GVs"][1]["OI_tipo_de_pessoa_3"], parametros["GVs"][1]["padrao_pessoa_morfologia_3"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][1]["funcao_no_grupo_verbal_4"], parametros["GVs"][1]["verbo_4"], parametros["GVs"][1]["tipo_de_orientacao_4"], parametros["GVs"][1]["padrao_de_morfologia_4"], parametros["GVs"][1]["OI_numero_4"], parametros["GVs"][1]["genero_4"], parametros["GVs"][1]["OI_tipo_de_pessoa_4"], parametros["GVs"][1]["padrao_pessoa_morfologia_4"], parametros["GVs"][1]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][1]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][1]["verbo_LEX"], parametros["GVs"][1]["tipo_de_orientacao_LEX"], parametros["GVs"][1]["padrao_de_morfologia_LEX"], parametros["GVs"][1]["OI_numero_LEX"], parametros["GVs"][1]["genero_LEX"], parametros["GVs"][1]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][1]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_2)

grupo_teste_3 = grupo_verbal(parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][2]["AGENCIA"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][2]["funcao_no_grupo_verbal_1"], parametros["GVs"][2]["verbo_1"], parametros["GVs"][2]["tipo_de_orientacao_1"], parametros["GVs"][2]["padrao_de_morfologia_1"], parametros["GVs"][2]["OI_numero_1"], parametros["GVs"][2]["genero_1"], parametros["GVs"][2]["OI_tipo_de_pessoa_1"], parametros["GVs"][2]["padrao_pessoa_morfologia_1"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][2]["funcao_no_grupo_verbal_2"], parametros["GVs"][2]["verbo_2"], parametros["GVs"][2]["tipo_de_orientacao_2"], parametros["GVs"][2]["padrao_de_morfologia_2"], parametros["GVs"][2]["OI_numero_2"], parametros["GVs"][2]["genero_2"], parametros["GVs"][2]["OI_tipo_de_pessoa_2"], parametros["GVs"][2]["padrao_pessoa_morfologia_2"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][2]["funcao_no_grupo_verbal_3"], parametros["GVs"][2]["verbo_3"], parametros["GVs"][2]["tipo_de_orientacao_3"], parametros["GVs"][2]["padrao_de_morfologia_3"], parametros["GVs"][2]["OI_numero_3"], parametros["GVs"][2]["genero_3"], parametros["GVs"][2]["OI_tipo_de_pessoa_3"], parametros["GVs"][2]["padrao_pessoa_morfologia_3"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][2]["funcao_no_grupo_verbal_4"], parametros["GVs"][2]["verbo_4"], parametros["GVs"][2]["tipo_de_orientacao_4"], parametros["GVs"][2]["padrao_de_morfologia_4"], parametros["GVs"][2]["OI_numero_4"], parametros["GVs"][2]["genero_4"], parametros["GVs"][2]["OI_tipo_de_pessoa_4"], parametros["GVs"][2]["padrao_pessoa_morfologia_4"], parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][2]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][2]["verbo_LEX"], parametros["GVs"][2]["tipo_de_orientacao_LEX"], parametros["GVs"][2]["padrao_de_morfologia_LEX"], parametros["GVs"][2]["OI_numero_LEX"], parametros["GVs"][2]["genero_LEX"], parametros["GVs"][2]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][2]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_3)

for entrada in dicionarioSinonimos:
	print(entrada)

	for verbo in dicionarioSinonimos[entrada]:
		padraoMorfologia = detecta_padrao_morfologia(verbo)
		grupo_teste_3 = grupo_verbal(parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][2]["AGENCIA"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_1"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_1"], parametros["GVs"][2]["verbo_1"],
		                             parametros["GVs"][2]["tipo_de_orientacao_1"],
		                             parametros["GVs"][2]["padrao_de_morfologia_1"], parametros["GVs"][2]["OI_numero_1"],
		                             parametros["GVs"][2]["genero_1"], parametros["GVs"][2]["OI_tipo_de_pessoa_1"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_1"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_2"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_2"], parametros["GVs"][2]["verbo_2"],
		                             parametros["GVs"][2]["tipo_de_orientacao_2"],
		                             parametros["GVs"][2]["padrao_de_morfologia_2"], parametros["GVs"][2]["OI_numero_2"],
		                             parametros["GVs"][2]["genero_2"], parametros["GVs"][2]["OI_tipo_de_pessoa_2"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_2"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_3"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_3"], parametros["GVs"][2]["verbo_3"],
		                             parametros["GVs"][2]["tipo_de_orientacao_3"],
		                             parametros["GVs"][2]["padrao_de_morfologia_3"], parametros["GVs"][2]["OI_numero_3"],
		                             parametros["GVs"][2]["genero_3"], parametros["GVs"][2]["OI_tipo_de_pessoa_3"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_3"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_4"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_4"], parametros["GVs"][2]["verbo_4"],
		                             parametros["GVs"][2]["tipo_de_orientacao_4"],
		                             parametros["GVs"][2]["padrao_de_morfologia_4"], parametros["GVs"][2]["OI_numero_4"],
		                             parametros["GVs"][2]["genero_4"], parametros["GVs"][2]["OI_tipo_de_pessoa_4"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_4"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_LEX"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_POS_FINAL"],
		                            verbo, parametros["GVs"][2]["tipo_de_orientacao_LEX"],
		                             padraoMorfologia,
		                             parametros["GVs"][2]["OI_numero_LEX"], parametros["GVs"][2]["genero_LEX"],
		                             parametros["GVs"][2]["OI_tipo_de_pessoa_LEX"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_LEX"])
		print(grupo_teste_3)

grupo_teste_4 = grupo_verbal(parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][3]["AGENCIA"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][3]["funcao_no_grupo_verbal_1"], parametros["GVs"][3]["verbo_1"], parametros["GVs"][3]["tipo_de_orientacao_1"], parametros["GVs"][3]["padrao_de_morfologia_1"], parametros["GVs"][3]["OI_numero_1"], parametros["GVs"][3]["genero_1"], parametros["GVs"][3]["OI_tipo_de_pessoa_1"], parametros["GVs"][3]["padrao_pessoa_morfologia_1"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][3]["funcao_no_grupo_verbal_2"], parametros["GVs"][3]["verbo_2"], parametros["GVs"][3]["tipo_de_orientacao_2"], parametros["GVs"][3]["padrao_de_morfologia_2"], parametros["GVs"][3]["OI_numero_2"], parametros["GVs"][3]["genero_2"], parametros["GVs"][3]["OI_tipo_de_pessoa_2"], parametros["GVs"][3]["padrao_pessoa_morfologia_2"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][3]["funcao_no_grupo_verbal_3"], parametros["GVs"][3]["verbo_3"], parametros["GVs"][3]["tipo_de_orientacao_3"], parametros["GVs"][3]["padrao_de_morfologia_3"], parametros["GVs"][3]["OI_numero_3"], parametros["GVs"][3]["genero_3"], parametros["GVs"][3]["OI_tipo_de_pessoa_3"], parametros["GVs"][3]["padrao_pessoa_morfologia_3"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][3]["funcao_no_grupo_verbal_4"], parametros["GVs"][3]["verbo_4"], parametros["GVs"][3]["tipo_de_orientacao_4"], parametros["GVs"][3]["padrao_de_morfologia_4"], parametros["GVs"][3]["OI_numero_4"], parametros["GVs"][3]["genero_4"], parametros["GVs"][3]["OI_tipo_de_pessoa_4"], parametros["GVs"][3]["padrao_pessoa_morfologia_4"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][3]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][3]["verbo_LEX"], parametros["GVs"][3]["tipo_de_orientacao_LEX"], parametros["GVs"][3]["padrao_de_morfologia_LEX"], parametros["GVs"][3]["OI_numero_LEX"], parametros["GVs"][3]["genero_LEX"], parametros["GVs"][3]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][3]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_4)

grupo_teste_5 = grupo_verbal(parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][4]["AGENCIA"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][4]["funcao_no_grupo_verbal_1"], parametros["GVs"][4]["verbo_1"], parametros["GVs"][4]["tipo_de_orientacao_1"], parametros["GVs"][4]["padrao_de_morfologia_1"], parametros["GVs"][4]["OI_numero_1"], parametros["GVs"][4]["genero_1"], parametros["GVs"][4]["OI_tipo_de_pessoa_1"], parametros["GVs"][4]["padrao_pessoa_morfologia_1"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][4]["funcao_no_grupo_verbal_2"], parametros["GVs"][4]["verbo_2"], parametros["GVs"][4]["tipo_de_orientacao_2"], parametros["GVs"][4]["padrao_de_morfologia_2"], parametros["GVs"][4]["OI_numero_2"], parametros["GVs"][4]["genero_2"], parametros["GVs"][4]["OI_tipo_de_pessoa_2"], parametros["GVs"][4]["padrao_pessoa_morfologia_2"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][4]["funcao_no_grupo_verbal_3"], parametros["GVs"][4]["verbo_3"], parametros["GVs"][4]["tipo_de_orientacao_3"], parametros["GVs"][4]["padrao_de_morfologia_3"], parametros["GVs"][4]["OI_numero_3"], parametros["GVs"][4]["genero_3"], parametros["GVs"][4]["OI_tipo_de_pessoa_3"], parametros["GVs"][4]["padrao_pessoa_morfologia_3"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][4]["funcao_no_grupo_verbal_4"], parametros["GVs"][4]["verbo_4"], parametros["GVs"][4]["tipo_de_orientacao_4"], parametros["GVs"][4]["padrao_de_morfologia_4"], parametros["GVs"][4]["OI_numero_4"], parametros["GVs"][4]["genero_4"], parametros["GVs"][4]["OI_tipo_de_pessoa_4"], parametros["GVs"][4]["padrao_pessoa_morfologia_4"], parametros["GVs"][4]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][4]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][4]["verbo_LEX"], parametros["GVs"][4]["tipo_de_orientacao_LEX"], parametros["GVs"][4]["padrao_de_morfologia_LEX"], parametros["GVs"][4]["OI_numero_LEX"], parametros["GVs"][4]["genero_LEX"], parametros["GVs"][4]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][4]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_5)


grupo_teste_6 = grupo_verbal(parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][5]["AGENCIA"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][5]["funcao_no_grupo_verbal_1"], parametros["GVs"][5]["verbo_1"], parametros["GVs"][5]["tipo_de_orientacao_1"], parametros["GVs"][5]["padrao_de_morfologia_1"], parametros["GVs"][5]["OI_numero_1"], parametros["GVs"][5]["genero_1"], parametros["GVs"][5]["OI_tipo_de_pessoa_1"], parametros["GVs"][5]["padrao_pessoa_morfologia_1"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][5]["funcao_no_grupo_verbal_2"], parametros["GVs"][5]["verbo_2"], parametros["GVs"][5]["tipo_de_orientacao_2"], parametros["GVs"][5]["padrao_de_morfologia_2"], parametros["GVs"][5]["OI_numero_2"], parametros["GVs"][5]["genero_2"], parametros["GVs"][5]["OI_tipo_de_pessoa_2"], parametros["GVs"][5]["padrao_pessoa_morfologia_2"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][5]["funcao_no_grupo_verbal_3"], parametros["GVs"][5]["verbo_3"], parametros["GVs"][5]["tipo_de_orientacao_3"], parametros["GVs"][5]["padrao_de_morfologia_3"], parametros["GVs"][5]["OI_numero_3"], parametros["GVs"][5]["genero_3"], parametros["GVs"][5]["OI_tipo_de_pessoa_3"], parametros["GVs"][5]["padrao_pessoa_morfologia_3"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][5]["funcao_no_grupo_verbal_4"], parametros["GVs"][5]["verbo_4"], parametros["GVs"][5]["tipo_de_orientacao_4"], parametros["GVs"][5]["padrao_de_morfologia_4"], parametros["GVs"][5]["OI_numero_4"], parametros["GVs"][5]["genero_4"], parametros["GVs"][5]["OI_tipo_de_pessoa_4"], parametros["GVs"][5]["padrao_pessoa_morfologia_4"], parametros["GVs"][5]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][5]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][5]["verbo_LEX"], parametros["GVs"][5]["tipo_de_orientacao_LEX"], parametros["GVs"][5]["padrao_de_morfologia_LEX"], parametros["GVs"][5]["OI_numero_LEX"], parametros["GVs"][5]["genero_LEX"], parametros["GVs"][5]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][5]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_6)

grupo_teste_7 = grupo_verbal(parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][6]["AGENCIA"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][6]["funcao_no_grupo_verbal_1"], parametros["GVs"][6]["verbo_1"], parametros["GVs"][6]["tipo_de_orientacao_1"], parametros["GVs"][6]["padrao_de_morfologia_1"], parametros["GVs"][6]["OI_numero_1"], parametros["GVs"][6]["genero_1"], parametros["GVs"][6]["OI_tipo_de_pessoa_1"], parametros["GVs"][6]["padrao_pessoa_morfologia_1"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][6]["funcao_no_grupo_verbal_2"], parametros["GVs"][6]["verbo_2"], parametros["GVs"][6]["tipo_de_orientacao_2"], parametros["GVs"][6]["padrao_de_morfologia_2"], parametros["GVs"][6]["OI_numero_2"], parametros["GVs"][6]["genero_2"], parametros["GVs"][6]["OI_tipo_de_pessoa_2"], parametros["GVs"][6]["padrao_pessoa_morfologia_2"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][6]["funcao_no_grupo_verbal_3"], parametros["GVs"][6]["verbo_3"], parametros["GVs"][6]["tipo_de_orientacao_3"], parametros["GVs"][6]["padrao_de_morfologia_3"], parametros["GVs"][6]["OI_numero_3"], parametros["GVs"][6]["genero_3"], parametros["GVs"][6]["OI_tipo_de_pessoa_3"], parametros["GVs"][6]["padrao_pessoa_morfologia_3"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][6]["funcao_no_grupo_verbal_4"], parametros["GVs"][6]["verbo_4"], parametros["GVs"][6]["tipo_de_orientacao_4"], parametros["GVs"][6]["padrao_de_morfologia_4"], parametros["GVs"][6]["OI_numero_4"], parametros["GVs"][6]["genero_4"], parametros["GVs"][6]["OI_tipo_de_pessoa_4"], parametros["GVs"][6]["padrao_pessoa_morfologia_4"], parametros["GVs"][6]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][6]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][6]["verbo_LEX"], parametros["GVs"][6]["tipo_de_orientacao_LEX"], parametros["GVs"][6]["padrao_de_morfologia_LEX"], parametros["GVs"][6]["OI_numero_LEX"], parametros["GVs"][6]["genero_LEX"], parametros["GVs"][6]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][6]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_7)

grupo_teste_8 = grupo_verbal(parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][7]["AGENCIA"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][7]["funcao_no_grupo_verbal_1"], parametros["GVs"][7]["verbo_1"], parametros["GVs"][7]["tipo_de_orientacao_1"], parametros["GVs"][7]["padrao_de_morfologia_1"], parametros["GVs"][7]["OI_numero_1"], parametros["GVs"][7]["genero_1"], parametros["GVs"][7]["OI_tipo_de_pessoa_1"], parametros["GVs"][7]["padrao_pessoa_morfologia_1"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][7]["funcao_no_grupo_verbal_2"], parametros["GVs"][7]["verbo_2"], parametros["GVs"][7]["tipo_de_orientacao_2"], parametros["GVs"][7]["padrao_de_morfologia_2"], parametros["GVs"][7]["OI_numero_2"], parametros["GVs"][7]["genero_2"], parametros["GVs"][7]["OI_tipo_de_pessoa_2"], parametros["GVs"][7]["padrao_pessoa_morfologia_2"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][7]["funcao_no_grupo_verbal_3"], parametros["GVs"][7]["verbo_3"], parametros["GVs"][7]["tipo_de_orientacao_3"], parametros["GVs"][7]["padrao_de_morfologia_3"], parametros["GVs"][7]["OI_numero_3"], parametros["GVs"][7]["genero_3"], parametros["GVs"][7]["OI_tipo_de_pessoa_3"], parametros["GVs"][7]["padrao_pessoa_morfologia_3"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][7]["funcao_no_grupo_verbal_4"], parametros["GVs"][7]["verbo_4"], parametros["GVs"][7]["tipo_de_orientacao_4"], parametros["GVs"][7]["padrao_de_morfologia_4"], parametros["GVs"][7]["OI_numero_4"], parametros["GVs"][7]["genero_4"], parametros["GVs"][7]["OI_tipo_de_pessoa_4"], parametros["GVs"][7]["padrao_pessoa_morfologia_4"], parametros["GVs"][7]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][7]["funcao_no_grupo_verbal_POS_FINAL"], parametros["GVs"][7]["verbo_LEX"], parametros["GVs"][7]["tipo_de_orientacao_LEX"], parametros["GVs"][7]["padrao_de_morfologia_LEX"], parametros["GVs"][7]["OI_numero_LEX"], parametros["GVs"][7]["genero_LEX"], parametros["GVs"][7]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][7]["padrao_pessoa_morfologia_LEX"])
print(grupo_teste_8)
######################################
#####################################
####################################
######################################
dicionarioSinonimos["apresentar"]

##exemplo passiva
for entrada in dicionarioSinonimos:
	print(entrada)

	for verbo in dicionarioSinonimos[entrada]:
		padraoMorfologia = detecta_padrao_morfologia(verbo)
		grupo_teste = grupo_verbal(parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][2]["AGENCIA"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_1"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_1"], parametros["GVs"][2]["verbo_1"],
		                             parametros["GVs"][2]["tipo_de_orientacao_1"],
		                             parametros["GVs"][2]["padrao_de_morfologia_1"],
		                             parametros["GVs"][2]["OI_numero_1"],
		                             parametros["GVs"][2]["genero_1"], parametros["GVs"][2]["OI_tipo_de_pessoa_1"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_1"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_2"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_2"], parametros["GVs"][2]["verbo_2"],
		                             parametros["GVs"][2]["tipo_de_orientacao_2"],
		                             parametros["GVs"][2]["padrao_de_morfologia_2"],
		                             parametros["GVs"][2]["OI_numero_2"],
		                             parametros["GVs"][2]["genero_2"], parametros["GVs"][2]["OI_tipo_de_pessoa_2"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_2"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_3"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_3"], parametros["GVs"][2]["verbo_3"],
		                             parametros["GVs"][2]["tipo_de_orientacao_3"],
		                             parametros["GVs"][2]["padrao_de_morfologia_3"],
		                             parametros["GVs"][2]["OI_numero_3"],
		                             parametros["GVs"][2]["genero_3"], parametros["GVs"][2]["OI_tipo_de_pessoa_3"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_3"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_4"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_4"], parametros["GVs"][2]["verbo_4"],
		                             parametros["GVs"][2]["tipo_de_orientacao_4"],
		                             parametros["GVs"][2]["padrao_de_morfologia_4"],
		                             parametros["GVs"][2]["OI_numero_4"],
		                             parametros["GVs"][2]["genero_4"], parametros["GVs"][2]["OI_tipo_de_pessoa_4"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_4"],
		                             parametros["GVs"][2]["TIPO_DE_EXPERIENCIA_LEX"],
		                             parametros["GVs"][2]["funcao_no_grupo_verbal_POS_FINAL"],
		                             verbo, parametros["GVs"][2]["tipo_de_orientacao_LEX"],
		                             padraoMorfologia,
		                             parametros["GVs"][2]["OI_numero_LEX"], parametros["GVs"][2]["genero_LEX"],
		                             parametros["GVs"][2]["OI_tipo_de_pessoa_LEX"],
		                             parametros["GVs"][2]["padrao_pessoa_morfologia_LEX"])
		print(grupo_teste)


#exemplos ativo
# for entrada in dicionarioSinonimos:
# 	print(entrada)
# 	for verbo in dicionarioSinonimos[entrada]:
# 		padraoMorfologia = detecta_padrao_morfologia(verbo)
# 		grupo_teste_4 = grupo_verbal(parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][3]["AGENCIA"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][3]["funcao_no_grupo_verbal_1"], parametros["GVs"][3]["verbo_1"], parametros["GVs"][3]["tipo_de_orientacao_1"], parametros["GVs"][3]["padrao_de_morfologia_1"], parametros["GVs"][3]["OI_numero_1"], parametros["GVs"][3]["genero_1"], parametros["GVs"][3]["OI_tipo_de_pessoa_1"], parametros["GVs"][3]["padrao_pessoa_morfologia_1"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][3]["funcao_no_grupo_verbal_2"], parametros["GVs"][3]["verbo_2"], parametros["GVs"][3]["tipo_de_orientacao_2"], parametros["GVs"][3]["padrao_de_morfologia_2"], parametros["GVs"][3]["OI_numero_2"], parametros["GVs"][3]["genero_2"], parametros["GVs"][3]["OI_tipo_de_pessoa_2"], parametros["GVs"][3]["padrao_pessoa_morfologia_2"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][3]["funcao_no_grupo_verbal_3"], parametros["GVs"][3]["verbo_3"], parametros["GVs"][3]["tipo_de_orientacao_3"], parametros["GVs"][3]["padrao_de_morfologia_3"], parametros["GVs"][3]["OI_numero_3"], parametros["GVs"][3]["genero_3"], parametros["GVs"][3]["OI_tipo_de_pessoa_3"], parametros["GVs"][3]["padrao_pessoa_morfologia_3"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][3]["funcao_no_grupo_verbal_4"], parametros["GVs"][3]["verbo_4"], parametros["GVs"][3]["tipo_de_orientacao_4"], parametros["GVs"][3]["padrao_de_morfologia_4"], parametros["GVs"][3]["OI_numero_4"], parametros["GVs"][3]["genero_4"], parametros["GVs"][3]["OI_tipo_de_pessoa_4"], parametros["GVs"][3]["padrao_pessoa_morfologia_4"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][3]["funcao_no_grupo_verbal_POS_FINAL"], verbo, parametros["GVs"][3]["tipo_de_orientacao_LEX"], padraoMorfologia, parametros["GVs"][3]["OI_numero_LEX"], parametros["GVs"][3]["genero_LEX"], parametros["GVs"][3]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][3]["padrao_pessoa_morfologia_LEX"])
# 		print (grupo_teste_4)




##################################



# # ##TESTE
# OI_numeros = ['singular', "plural"]
# OI_tipo_pessoas = ["1pessoa", '2pessoa', '3pessoa']
# generos=["masculino","feminino"]
# conjugacoes=["presente","pretérito_perfectivo_I","pretérito_perfectivo_II","pretérito_imperfectivo","passado_volitivo","futuro","subjuntivo_conjuntivo","subjuntivo_condicional","subjuntivo_optativo","imperativo_I","imperativo_II","não_finito_concretizado","infinitivo","gerúndio","particípio"]
# lemaTeste="levar"
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		for conj in conjugacoes:
# 				for genero in generos:
# 					print(verbo_geral("Fazer",'Evento','levar',conj,numero,genero,tipo_pessoa))

#presente
# print("A conjugação é:")

for lema in lemas:
	print("LEMA: " + lema)
	for numero in OI_numeros:
		for tipo_pessoa in OI_tipo_pessoas:
			print(verbo_geral("Fazer",'Evento',lema,"presente",numero,None,tipo_pessoa))



# # ###
# #presente
# print("A conjugação é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'presente', '-ER', numero, None, tipo_pessoa))
#
# ###
# print("A conjugação pretérito_perfectivo_I é:")
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_I', '-ER', numero, None, tipo_pessoa))
#
# #####pretérito_imperfectivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_imperfectivo', '-ER', numero, None, tipo_pessoa))
#
# ### "pretérito_perfectivo_II"
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'pretérito_perfectivo_II', '-ER', numero, None, tipo_pessoa))
#
# ###passado_volitivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'passado_volitivo', '-ER', numero, None, tipo_pessoa))
#
# # futuro
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'futuro', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_conjuntivo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_conjuntivo', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_condicional
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_condicional', '-ER', numero, None, tipo_pessoa))
#
# # subjuntivo_optativo
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'subjuntivo_optativo', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_I
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'imperativo_I', '-ER', numero, None, tipo_pessoa))
#
# # imperativo_II
#
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'imperativo_II', '-ER', numero, None, tipo_pessoa))
#
# # # não_finito_concretizado
# for numero in OI_numeros:
# 	for tipo_pessoa in OI_tipo_pessoas:
# 		print(formacao_verbo_ter('ter', 'não_finito_concretizado', '-ER', numero, None, tipo_pessoa))
# # infinitivo
# print(formacao_verbo_ter('ter', 'infinitivo', '-ER', numero, 'feminino', None))
#
# # # gerúndio
# print(formacao_verbo_ter('ter', 'gerúndio', '-ER', None, None, None))
# #
# # # particípio
# generos = ['masculino', 'feminino']
# for numero in OI_numeros:
# 	for genero in generos:
# 		print(formacao_verbo_ter('ter', 'particípio', '-ER', numero, genero, None))


