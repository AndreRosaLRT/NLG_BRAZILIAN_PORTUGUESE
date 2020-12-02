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

dicionarioSinonimos=json.load(open("./mineração_lexicon/dic_sin_cbow.json"))
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
for entrada in dicionarioSinonimos:
	print(entrada)
	for verbo in dicionarioSinonimos[entrada]:
		padraoMorfologia = detecta_padrao_morfologia(verbo)
		grupo_teste_4 = grupo_verbal(parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_GV"], parametros["GVs"][3]["AGENCIA"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_1"], parametros["GVs"][3]["funcao_no_grupo_verbal_1"], parametros["GVs"][3]["verbo_1"], parametros["GVs"][3]["tipo_de_orientacao_1"], parametros["GVs"][3]["padrao_de_morfologia_1"], parametros["GVs"][3]["OI_numero_1"], parametros["GVs"][3]["genero_1"], parametros["GVs"][3]["OI_tipo_de_pessoa_1"], parametros["GVs"][3]["padrao_pessoa_morfologia_1"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_2"], parametros["GVs"][3]["funcao_no_grupo_verbal_2"], parametros["GVs"][3]["verbo_2"], parametros["GVs"][3]["tipo_de_orientacao_2"], parametros["GVs"][3]["padrao_de_morfologia_2"], parametros["GVs"][3]["OI_numero_2"], parametros["GVs"][3]["genero_2"], parametros["GVs"][3]["OI_tipo_de_pessoa_2"], parametros["GVs"][3]["padrao_pessoa_morfologia_2"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_3"], parametros["GVs"][3]["funcao_no_grupo_verbal_3"], parametros["GVs"][3]["verbo_3"], parametros["GVs"][3]["tipo_de_orientacao_3"], parametros["GVs"][3]["padrao_de_morfologia_3"], parametros["GVs"][3]["OI_numero_3"], parametros["GVs"][3]["genero_3"], parametros["GVs"][3]["OI_tipo_de_pessoa_3"], parametros["GVs"][3]["padrao_pessoa_morfologia_3"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_4"], parametros["GVs"][3]["funcao_no_grupo_verbal_4"], parametros["GVs"][3]["verbo_4"], parametros["GVs"][3]["tipo_de_orientacao_4"], parametros["GVs"][3]["padrao_de_morfologia_4"], parametros["GVs"][3]["OI_numero_4"], parametros["GVs"][3]["genero_4"], parametros["GVs"][3]["OI_tipo_de_pessoa_4"], parametros["GVs"][3]["padrao_pessoa_morfologia_4"], parametros["GVs"][3]["TIPO_DE_EXPERIENCIA_LEX"], parametros["GVs"][3]["funcao_no_grupo_verbal_POS_FINAL"], verbo, parametros["GVs"][3]["tipo_de_orientacao_LEX"], padraoMorfologia, parametros["GVs"][3]["OI_numero_LEX"], parametros["GVs"][3]["genero_LEX"], parametros["GVs"][3]["OI_tipo_de_pessoa_LEX"], parametros["GVs"][3]["padrao_pessoa_morfologia_LEX"])
		print (grupo_teste_4)












# class GrupoVerbal:
# 	def __init__(self, TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1,
#                  tipo_de_orientacao_1, padrao_de_morfologia_1, OI_numero_1, genero_1,
#                  OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2,
#                  verbo_2, tipo_de_orientacao_2, padrao_de_morfologia_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
#                  padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
#                  tipo_de_orientacao_3, padrao_de_morfologia_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
#                  padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
#                  tipo_de_orientacao_4, padrao_de_morfologia_4,
#                  OI_numero_4, genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX,
#                  funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
#                  OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX):
# 		self.TIPO_DE_EXPERIENCIA_GV = TIPO_DE_EXPERIENCIA_GV
# 		self.AGENCIA = AGENCIA
# 		self.TIPO_DE_EXPERIENCIA_1=TIPO_DE_EXPERIENCIA_1
# 		self.funcao_no_grupo_verbal_1=funcao_no_grupo_verbal_1
# 		self.verbo_1=verbo_1
# 		self.tipo_de_orientacao_1=tipo_de_orientacao_1
# 		self.padrao_de_morfologia_1=padrao_de_morfologia_1
# 		self.OI_numero_1= OI_numero_1
# 		self.genero_1= genero_1
# 		self.OI_tipo_de_pessoa_1= OI_tipo_de_pessoa_1
# 		self.verbo_2= verbo_2
# 		self.tipo_de_orientacao_2= tipo_de_orientacao_2
# 		self.padrao_de_morfologia_2= padrao_de_morfologia_2
# 		self.OI_numero_2= OI_numero_2
# 		self.genero_2= genero_2
# 		self.OI_tipo_de_pessoa_2= OI_tipo_de_pessoa_2
# 		self.padrao_pessoa_morfologia_2= padrao_pessoa_morfologia_2
# 		self.TIPO_DE_EXPERIENCIA_3= TIPO_DE_EXPERIENCIA_3
# 		self.funcao_no_grupo_verbal_3= funcao_no_grupo_verbal_3
# 		self.verbo_3= verbo_3
# 		self.tipo_de_orientacao_3=tipo_de_orientacao_3
# 		self.padrao_de_morfologia_3= padrao_de_morfologia_3
# 		self.OI_numero_3= OI_numero_3
# 		self.genero_3= genero_3
# 		self.OI_tipo_de_pessoa_3=OI_tipo_de_pessoa_3
# 		self.padrao_pessoa_morfologia_3=padrao_pessoa_morfologia_3
# 		self.TIPO_DE_EXPERIENCIA_4=TIPO_DE_EXPERIENCIA_4
# 		self.funcao_no_grupo_verbal_4= funcao_no_grupo_verbal_4
# 		self.verbo_4= verbo_4
# 		self.tipo_de_orientacao_4= tipo_de_orientacao_4
# 		self.padrao_de_morfologia_4= padrao_de_morfologia_4
# 		self.OI_numero_4= OI_numero_4
# 		self.genero_4= genero_4
# 		self.OI_tipo_de_pessoa_4= OI_tipo_de_pessoa_4
# 		self.padrao_pessoa_morfologia_4= padrao_pessoa_morfologia_4
# 		self.TIPO_DE_EXPERIENCIA_LEX= TIPO_DE_EXPERIENCIA_LEX
# 		self.funcao_no_grupo_verbal_POS_FINAL= funcao_no_grupo_verbal_POS_FINAL
# 		self.verbo_LEX= verbo_LEX
# 		self.tipo_de_orientacao_LEX= tipo_de_orientacao_LEX
# 		self.padrao_de_morfologia_LEX= padrao_de_morfologia_LEX
# 		self.OI_numero_LEX= OI_numero_LEX
# 		self.genero_LEX= genero_LEX
# 		self.OI_tipo_de_pessoa_LEX= OI_tipo_de_pessoa_LEX
# 		self.padrao_pessoa_morfologia_LEX=padrao_pessoa_morfologia_LEX
#
# 	def grupo_verbal(self,TIPO_DE_EXPERIENCIA_GV, AGENCIA, TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1,
# 	                 tipo_de_orientacao_1, padrao_de_morfologia_1, OI_numero_1, genero_1,
# 	                 OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1, TIPO_DE_EXPERIENCIA_2, funcao_no_grupo_verbal_2,
# 	                 verbo_2, tipo_de_orientacao_2, padrao_de_morfologia_2, OI_numero_2, genero_2, OI_tipo_de_pessoa_2,
# 	                 padrao_pessoa_morfologia_2, TIPO_DE_EXPERIENCIA_3, funcao_no_grupo_verbal_3, verbo_3,
# 	                 tipo_de_orientacao_3, padrao_de_morfologia_3, OI_numero_3, genero_3, OI_tipo_de_pessoa_3,
# 	                 padrao_pessoa_morfologia_3, TIPO_DE_EXPERIENCIA_4, funcao_no_grupo_verbal_4, verbo_4,
# 	                 tipo_de_orientacao_4, padrao_de_morfologia_4,
# 	                 OI_numero_4, genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX,
# 	                 funcao_no_grupo_verbal_POS_FINAL, verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
# 	                 OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX, padrao_pessoa_morfologia_LEX):
# 		'''()->str
# 		Retorna a estrutura que realiza o grupo verbal, dadas escolhas de
# 		tipo_pessoa DE EVENTO, AGÊNCIA, TEMPO SECUNDÁRIO, FINITUDE E ASPECTO.
# 		>>>grupo_verbal()
# 		 'ando'
# 		>>>grupo_verbal()
# 		 'estou andando'
# 		>>>grupo_verbal()
# 		 'andava'
# 		'''
#
# 		if TIPO_DE_EXPERIENCIA_GV == 'Ser' or TIPO_DE_EXPERIENCIA_GV == 'Fazer' or TIPO_DE_EXPERIENCIA_GV == 'Sentir':
#
# 			if AGENCIA == 'agenciado_ativa' or AGENCIA == 'não_agenciado':
#
# 				verbo1 = verbo_geral(TIPO_DE_EXPERIENCIA_1, funcao_no_grupo_verbal_1, verbo_1,
# 				                     tipo_de_orientacao_1, padrao_de_morfologia_1, OI_numero_1, genero_1,
# 				                     OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
# 				verbo2 = verbo_geral(TIPO_DE_EXPERIENCIA_2,
# 				                     funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, padrao_de_morfologia_2,
# 				                     OI_numero_2,
# 				                     genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
# 				verbo3 = verbo_geral(TIPO_DE_EXPERIENCIA_3,
# 				                     funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, padrao_de_morfologia_3,
# 				                     OI_numero_3,
# 				                     genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)
# 				verbo4 = verbo_geral(TIPO_DE_EXPERIENCIA_4,
# 				                     funcao_no_grupo_verbal_4, verbo_4, tipo_de_orientacao_4, padrao_de_morfologia_4,
# 				                     OI_numero_4,
# 				                     genero_4, OI_tipo_de_pessoa_4, padrao_pessoa_morfologia_4)
# 				Evento = verbo_geral(TIPO_DE_EXPERIENCIA_LEX, funcao_no_grupo_verbal_POS_FINAL,
# 				                     verbo_LEX, tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
# 				                     OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX
# 				                     , padrao_pessoa_morfologia_LEX)
#
# 				grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbo4 + ' ' + Evento
#
# 			else:
# 				tipo_de_orientacao_LEX = 'particípio'
# 				verbo_4 = 'ser'
# 				verbo1 = verbo_geral(TIPO_DE_EXPERIENCIA_1,
# 				                     funcao_no_grupo_verbal_1,
# 				                     verbo_1, tipo_de_orientacao_1, padrao_de_morfologia_1, OI_numero_1,
# 				                     genero_1, OI_tipo_de_pessoa_1, padrao_pessoa_morfologia_1)
# 				verbo2 = verbo_geral(TIPO_DE_EXPERIENCIA_2,
# 				                     funcao_no_grupo_verbal_2, verbo_2, tipo_de_orientacao_2, padrao_de_morfologia_2,
# 				                     OI_numero_2,
# 				                     genero_2, OI_tipo_de_pessoa_2, padrao_pessoa_morfologia_2)
# 				verbo3 = verbo_geral(TIPO_DE_EXPERIENCIA_3,
# 				                     funcao_no_grupo_verbal_3, verbo_3, tipo_de_orientacao_3, padrao_de_morfologia_3,
# 				                     OI_numero_3,
# 				                     genero_3, OI_tipo_de_pessoa_3, padrao_pessoa_morfologia_3)
#
# 				verbos_passiva = realizacao_de_AGENCIA_passiva(verbo_4, tipo_de_orientacao_4, padrao_de_morfologia_4,
# 				                                               OI_numero_4, genero_4, OI_tipo_de_pessoa_4,
# 				                                               padrao_pessoa_morfologia_4, TIPO_DE_EXPERIENCIA_LEX,
# 				                                               funcao_no_grupo_verbal_POS_FINAL, verbo_LEX,
# 				                                               tipo_de_orientacao_LEX, padrao_de_morfologia_LEX,
# 				                                               OI_numero_LEX, genero_LEX, OI_tipo_de_pessoa_LEX,
# 				                                               padrao_pessoa_morfologia_LEX)
# 				grupo_verbal = verbo1 + ' ' + verbo2 + ' ' + verbo3 + ' ' + verbos_passiva
# 		return (re.sub(' +', ' ', grupo_verbal).strip())
#
# GrupoTeste = GrupoVerbal('Fazer', 'agenciado_passiva', None, None, None,
#                   None, None, None, None,
#                   None, None, None, None,
#                   None, None, None, None, None, None,
#                   None, None, None, None,
#                   None, None, None, None, None,
#                   None, 'Ser', 'Auxiliar', 'ser','pretérito_perfectivo_I','-ER',
#               'singular',None,'1pessoa','Morfologia_padrão','Fazer','Evento',
#               'levar','particípio','-AR','singular','masculino',None,'Morfologia_padrão')
#
#
# Grupo_teste_2 = GrupoVerbal.grupo_verbal('x','Fazer', 'agenciado_passiva', None, None, None,
#                   None, None, None, None,
#                   None, None, None, None,
#                   None, None, None, None, None, None,
#                   None, None, None, None,
#                   None, None, None, None, None,
#                   None, 'Ser', 'Auxiliar', 'ser','pretérito_perfectivo_I','-ER',
#               'singular',None,'3pessoa','Morfologia_padrão','Fazer','Evento',
#               'registrar','particípio','-AR','singular','masculino',None,'Morfologia_padrão')
#
#
