###A FAZER : CONTINUAR A ORAÇÃO VERBAL



   





def oraçãoMental():
	'''
	'''
	Transitividade = TRANSITIVIDADE()
	Modo = MODO()
	Tema_id = TEMA_IDEACIONAL()
	Tema_interpessoal = TEMA_INTERPESSOAL()
	Tema_textual=TEMA_TEXTUAL()
	
	if Transitividade == 'PR_Mental_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':

		print ('Selecione o tipo de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()
	    
		if TIPO_DE_PROCESSO == 'superior':
			TIPO_SUPERIOR = choice.Menu(['cognitivo','desiderativo',]).ask()
			print ('Qual o Experienciador (Ente:Humanizado)?')
			Experienciador = estrutura_GN()
		else:
			TIPO_INFERIOR = choice.Menu(['emotivo','perceptivo']).ask()
			print ('Qual o Experienciador (Ente:Animalizado☺)?')
			Experienciador = estrutura_GN()
			 
		print ('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE ()
	    
		print ('Em orações mentais médio sem alcance, a Fenomenalização seleciona especificamente a Não-fenomenalização:comportamento_passivo')
		
		oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Experienciador  + ' ' + Polaridade + ' ' + Processo + '.'
    
	
		
		
			
	
	    
	
	
	
	
	
	
	
	elif Transitividade == 'PR_Mental_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
		
		
		print ('Selecione o tipo de processo mental:')
		TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()
	    
		if TIPO_DE_PROCESSO == 'superior':
			TIPO_SUPERIOR = choice.Menu(['cognitivo','desiderativo',]).ask()
			print ('Qual o Experienciador (Ente:Humanizado)?')
			Experienciador = estrutura_GN()
		else:
			TIPO_INFERIOR = choice.Menu(['emotivo','perceptivo']).ask()
			print ('Qual o Experienciador (Ente:Animalizado☺)?')
			Experienciador = estrutura_GN()
			 
		print ('Qual o Processo?')
		Processo = grupo_verbal()
		Polaridade = POLARIDADE ()
        
		print ('Qual o tipo de Fenomenalizalção?')
		FENOMENALIZAÇÃO = choice.Menu(['fenomenalização', 'não-fenomenalização']).ask()
		if FENOMENALIZAÇÃO == 'fenomenalização':
			TIPO_fenomenalização = choice.Menu(['hiperfenômeno','fenômeno_simples']).ask()
            if TIPO_fenomenalização == 'hiperfenômeno':
                TIPO_hiperfenômeno = choice.Menu(['criativo','reativo']).ask()
                if TIPO_hiperfenômeno == 'criativo':
                    TIPO_criativo = choice.Menu(['pensamento','desejo']).ask()
                elif TIPO_hiperfenômeno == 'reativo':
                    TIPO_reativo = choice.Menu(['metafenômeno','macrofenômeno']).ask()
            elif TIPO_fenomenalização == 'fenômeno_simples':
                #ver qual a realização
		elif FENOMENALIZAÇÃO == 'não-fenomenalização':
			print ('Em caso de orações mentais médio com alcance e Não-fenomenalização seleciona-se a opção: assunto']).ask()
	        Assunto = frase_preposicional()
			
			oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Experienciador  + ' ' + Polaridade + ' ' + Processo + ' ' + Assunto + '.'
	return oração
		
		
		if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
			TIPO_DE_COGNITIVO = choice.Menu (['pensar','saber','sonhar']).ask()
		
	    elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
			TIPO_DE_DESIDERATIVO = choice.Menu(['querer','esperar']).ask()
			
		elif TIPO_INFERIOR == 'emotivo' and TIPO_reativo == 'metafenômeno':
			TIPO_DE_EMOTIVO = choice.Menu(['gostar','agradar']).ask()
		
		
        
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
#		op
        TIPO_DE_PROCESSO = choice.Menu(['superior','inferior']).ask()
        if TIPO_DE_PROCESSO == 'superior':
            TIPO_SUPERIOR = choice.Menu(['cognitivo','desiderativo',]).ask()
        else:
            TIPO_INFERIOR = choice.Menu(['emotivo','perceptivo']).ask()
            
        FENOMENALIZAÇÃO = choice.Menu(['fenomenalização', 'não-fenomenalização']).ask()
        if FENOMENALIZAÇÃO == 'fenomenalização':
            TIPO_fenomenalização = choice.Menu(['hiperfenômeno','fenômeno_simples']).ask()
            if TIPO_fenomenalização == 'hiperfenômeno':
                TIPO_hiperfenômeno = choice.Menu(['criativo','reativo']).ask()
                if TIPO_hiperfenômeno == 'criativo':
                    TIPO_criativo = choice.Menu(['pensamento','desejo']).ask()
                elif TIPO_hiperfenômeno == 'reativo':
                    TIPO_reativo = choice.Menu(['metafenômeno','macrofenômeno']).ask()
            elif TIPO_fenomenalização == 'fenômeno_simples':
                #ver qual a realização
		elif FENOMENALIZAÇÃO == 'não-fenomenalização':
			NÃO_FENOMENALIZAÇÃO = choice.Menu (['comportamento_passivo', 'assunto']).ask()
        
		
		
		if TIPO_SUPERIOR == 'cognitivo' and TIPO_criativo == 'pensamento':
			TIPO_DE_COGNITIVO = choice.Menu (['pensar','saber','sonhar']).ask()
		
	    elif TIPO_SUPERIOR == 'desiderativo' and TIPO_criativo == 'desejo':
			TIPO_DE_DESIDERATIVO = choice.Menu(['querer','esperar']).ask()
			
		elif TIPO_INFERIOR == 'emotivo' and TIPO_reativo == 'metafenômeno':
			TIPO_DE_EMOTIVO = choice.Menu(['gostar','agradar']).ask()
        
        
        
        
        
        
        
        
    
    
#
#
#def oração_Verbal():
#    '''(str,str,str)->str
#    Retorna a formação estrutural na lexicogramática (oração) de uma figura específica
#    da semãntica
#    
#    >>>formação_estrutura_oração ()
#    'eu bebi água'
#    '''
#    
#    
#    ##ORAÇÃO VERBAL
#    
#    Transitividade = TRANSITIVIDADE()
#    Modo = MODO()
#    Tema_id = TEMA_IDEACIONAL()        
#
#    if Transitividade == 'PR_Verbal_AG_médio_sem_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#        Tema_interpessoal = TEMA_INTERPESSOAL()
#        Tema_textual=TEMA_TEXTUAL()
#        print ('Selecione a Receptividade')
#        RECEPTIVIDADE = choice.Menu (['+receptor','-receptor']).ask()
#        print ('Qual a Ordem do Dizente?')
#        ORDEM_DO_DIZENTE = choice.Menu (['atividade','semioticidade']).ask()
#        
#        if ORDEM_DO_DIZENTE == 'atividade':    
#            TIPO_ATIVIDADE = 'fala'
#    
#            if TIPO_ATIVIDADE == 'fala' and RECEPTIVIDADE == '-receptor':
#                
#                print ('Qual o Processo?')
#                Processo = grupo_verbal()
#                print('Qual é o Dizente?')
#                Dizente = estrutura_GN()
#                Polaridade = POLARIDADE ()
#            
#                oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + '.'
#                 #Ex.: Eu conversei até anoitecer; Eu falei muito ontem; Nós discutimos...
#        
#            elif TIPO_ATIVIDADE == 'fala' and RECEPTIVIDADE == '+receptor':
#                
#                print ('Qual o Processo?')
#                Processo = grupo_verbal()
#                print('Qual é o Dizente?')
#                Dizente = estrutura_GN()
#                print ('Qual é o Receptor?')
#                Receptor = frase_preposicional ()
#                Polaridade = POLARIDADE ()
#            
#                oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + ' ' +  Receptor + '.'
#                
#                #Ex.: Eu conversei com você até anoitecer; Eu falei com você muito ontem; Nós discutimos com ela...
#            
#       
#        
#        elif ORDEM_DO_DIZENTE == 'semioticidade' and RECEPTIVIDADE == '+receptor': 
#            print ('Selecione o tipo de Semioticidade')
#            
#            TIPO_SEMIOTICIDADE = choice.Menu (['projeção','não_projeção']).ask()
#            if TIPO_SEMIOTICIDADE == 'projeção':
#                print ('Selecione o tipo de projeção')
#                TIPO_PROJEÇÃO = choice.Menu (['citativa', 'relativa']).ask()
#                
#                
#                if TIPO_PROJEÇÃO == 'citativa':
#                    print ('Qual o Processo?')
#                    Processo = grupo_verbal()
#                    print('Qual é o Dizente?')
#                    Dizente = estrutura_GN()
#                    print ('Qual é o Receptor?')
#                    Receptor = frase_preposicional ()
#                    Polaridade = POLARIDADE ()
#                    print ('Qual a oração projetada?')
#                    Oração_projetada = oraçãoProjetada()
#        
#                    oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor + '"' + Oração_projetada + '" ' + '.'
#                    #Ex.: Eu disse a ele "Eu comi o bolo". 
#                
#                elif TIPO_PROJEÇÃO == 'relativa':
#                    print ('Qual o Processo?')
#                    Processo = grupo_verbal()
#                    print('Qual é o Dizente?')
#                    Dizente = estrutura_GN()
#                    print ('Qual é o Receptor?')
#                    Receptor = frase_preposicional ()
#                    Polaridade = POLARIDADE ()
#                    print ('Qual a oração projetada?')
#                    Oração_projetada = oraçãoProjetada()
#        
#                    oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + ' ' + Receptor  + ' ' + 'que'  + ' ' + '"' + Oração_projetada + '" ' + '.'
#                    #Ex.: Eu disse a ele que "Eu comi o bolo". 
#                    
#        elif ORDEM_DO_DIZENTE == 'semioticidade' and RECEPTIVIDADE == '-receptor': 
#            print ('Selecione o tipo de Semioticidade')
#            
#            TIPO_SEMIOTICIDADE = choice.Menu (['projeção','não_projeção']).ask()
#            if TIPO_SEMIOTICIDADE == 'projeção':
#                print ('Selecione o tipo de projeção')
#                TIPO_PROJEÇÃO = choice.Menu (['citativa', 'relativa']).ask()
#                
#                
#                if TIPO_PROJEÇÃO == 'citativa':
#                    print ('Qual o Processo?')
#                    Processo = grupo_verbal()
#                    print('Qual é o Dizente?')
#                    Dizente = estrutura_GN()
#                    
#                    Polaridade = POLARIDADE ()
#                    print ('Qual a oração projetada?')
#                    Oração_projetada = oraçãoProjetada()
#        
#                    oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + '"' + Oração_projetada + '" ' + '.'
#                    #Ex.: Eu disse  "Eu comi o bolo". 
#                
#                elif TIPO_PROJEÇÃO == 'relativa':
#                    print ('Qual o Processo?')
#                    Processo = grupo_verbal()
#                    print('Qual é o Dizente?')
#                    Dizente = estrutura_GN()
#                    
#                    Polaridade = POLARIDADE ()
#                    print ('Qual a oração projetada?')
#                    Oração_projetada = oração()
#        
#                    oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo   + ' ' + 'que'  + ' ' + '"' + Oração_projetada + '" ' + '.'
#                    #Ex.: Eu disse que "Eu comi o bolo".      
#            
#           
#            
#            elif TIPO_SEMIOTICIDADE == 'não_projeção':
#                
#                TIPO_NÃO_PROJEÇÃO = '-verbiagem'
#                print ('Qual o Processo?')
#                Processo = grupo_verbal()
#                print('Qual é o Dizente?')
#                Dizente = estrutura_GN()
#                Polaridade = POLARIDADE ()
#                
#                oração =  Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + '.'
#              
#    elif Transitividade == 'PR_Verbal_AG_médio_com_alcance' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#        
#        Tema_interpessoal = TEMA_INTERPESSOAL()
#        Tema_textual=TEMA_TEXTUAL()
#        TIPO_SEMIOTICIDADE = 'não_projeção'
#        print ('Selecione a Receptividade')
#        RECEPTIVIDADE = choice.Menu (['+receptor','-receptor']).ask()
#        
#        if RECEPTIVIDADE == '+receptor':
#            print ('Qual o Processo?')
#            Processo = grupo_verbal()
#            print('Qual é o Dizente?')
#            Dizente = estrutura_GN()
#            print('Qual é a Verbiagem?')
#            Verbiagem = estrutura_GN()
#            print ('Qual é o Receptor?')
#            Receptor = frase_preposicional ()
#            Polaridade = POLARIDADE ()
#            
#            oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + ' ' + Verbiagem + ' '+ Receptor +'.' 
#            
#           
#             
#        else:
#            print ('Qual o Processo?')
#            Processo = grupo_verbal()
#            print('Qual é o Dizente?')
#            Dizente = estrutura_GN()
#            print('Qual é a Verbiagem?')
#            Verbiagem = estrutura_GN()            
#            Polaridade = POLARIDADE ()
#            
#            oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo + ' ' + Verbiagem +'.'
#    
#
#    elif   'PR_Verbal_AG_efetivo_operativo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#        
#        Tema_interpessoal = TEMA_INTERPESSOAL()
#        Tema_textual=TEMA_TEXTUAL()  
#        print ('Qual o Processo?')
#        Processo = grupo_verbal()
#        Polaridade = POLARIDADE ()
#        print('Qual é o Dizente?')
#        Dizente = estrutura_GN()
#        
#        print('O Alvo é realizado por grupo nominal ou frase preposicional?')
#        realização_alvo = choice.Menu(['GN','FP']).ask()
#        if realização_alvo == 'GN':
#            print('Qual é o Alvo?')
#            Alvo = estrutura_GN()
#            print ('Qual a localização do alvo na oração (em relação ao Processo)?')
#            localização_alvo = choice.Menu(['ante_processo','pós_processo']).ask()
#            if localização_alvo == 'ante_processo':
#                oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Alvo + ' ' + Processo +'.'
#            else:
#                oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo+ ' ' + Alvo +'.'
#           
#                
#        else:
#            print('Qual é o Alvo?')
#            Alvo = frase_preposicional()
#            
#            oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Dizente  + ' ' + Polaridade + ' ' + Processo+ ' ' + Alvo +'.'
#
#    
#    elif   'PR_Verbal_AG_efetivo_receptivo' and Modo == 'SUJ_responsável_recuperado_explícito_MOD_declarativo_-perguntafinito' and Tema_id == 'TID_default_indicativo_declarativo_TIdentif_NA':
#        
#        Tema_interpessoal = TEMA_INTERPESSOAL()
#        Tema_textual=TEMA_TEXTUAL()  
#        print ('Qual o Processo?')
#        Processo = grupo_verbal()
#        Polaridade = POLARIDADE ()
#        print('Qual é o Dizente?')
#        Dizente = frase_preposicional()
#        print('Qual é o Alvo?')
#        Alvo = estrutura_GN()
#        
#            
#            
#        oração = Tema_interpessoal + ' ' + Tema_textual  + ' ' + Alvo  + ' ' + Polaridade + ' ' + Processo+ ' ' + Dizente +'.'
#           
#        
#        
#    
#        
#           
#    return oração.capitalize() 
#     
#            
#            
#           
            
   
        
  

substantivo_lematizado= 'professor'

substantivo_lematizado[-2:] == 'or'



def formação_da_estrutura_do_substantivo_comumteste ():
    '''(str, str)-str

    Retorna a realização de um substantivo comum dados a experiência_do_substantivo
    e as flexões_desejadas.

    >>>formação_da_estrutura_do_substantivo_comum ()

    '''
    
  
    substantivo_lematizado = input ('Qual é o substantivo lematizado?')
    
    if substantivo_lematizado[-2:] == 'or':
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




























































































    