

def def_classe_de_verbo(funcao_no_grupo_verbal):

   """
   :param funcao_no_grupo_verbal:
   :return: classe do verbo
   """
   # print("Qual é a função do verbo no grupo verbal?")
   # funcao_no_grupo_verbal = choice.Menu(['Evento', 'Auxiliar', 'Modal', 'Evento+Núcleo',
   #                                       'Auxiliar+Núcleo', 'Modal+Núcleo']).ask()

   if funcao_no_grupo_verbal == 'Evento' or funcao_no_grupo_verbal == 'Evento+Núcleo':
       classe_verbo = 'lexical'
   elif funcao_no_grupo_verbal == 'Auxiliar' or funcao_no_grupo_verbal == 'Auxiliar+Núcleo':
       classe_verbo = 'auxiliar'
   elif funcao_no_grupo_verbal == 'Modal' or funcao_no_grupo_verbal == 'Modal+Núcleo':
       classe_verbo = 'modal'
   else:
       classe_verbo = None

    return classe_verbo

# EXEMPLOS
# def_classe_de_verbo("Modal")
# def_classe_de_verbo("Evento+Núcleo")
# def_classe_de_verbo("Auxiliar")
# def_classe_de_verbo("Auxiliar+Núcleo")
