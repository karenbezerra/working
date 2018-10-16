<Padrão regex> 
		
 G1	->  
 
 G2	-> (Insert Into) +  (espaço)
 	 >  'Insert Into' + ' '
 	 >  (palavra chave para inserção) + (espaço -- diff representacoes)
 
 G3 -> (caracteres) [pode ter ou não]+ ('.') + (qualquer outra coisa)
	 >   'Owner' + '.' + 'tabela' 
	 > ( P ou A) # 'Owner tem que tratar condição 
 
 G4 -> (espaço) + ('(')
 	 > ' ' + 'marcação_de_inicio'
 
 G5 -> (conjunto_caracteres) + (',') (pode ter ou não) x [indeterminadas vezes]
 	 > 'nome_das_colunas' + virgula [null] # - caso de não tem mais colunas, não haverá mais vírgula
 	 > ( P ou A) # Grupo não obrigatório-  Presente ou Ausente -- Podem estar presente ou não 
 
 G6 -> (')') + (espaço) +  (Values) + (espaço)
 	 > 'marcação_de_fim' + ' ' + ' values' + ' '
 	 >   

 G7 -> 		('(')       +      (' \'')  + (conjunto_caracteres)  + ('\'') [null] + (',') + (espaço)  
 	 > 'marcação_de_inicio' + 'aspas' + 'valor_coluna' + 'aspas' + 'virgula' + ' '
 	 > 


<Pendências>

	
	--> no caso das colunas quando não tiver  # tem que tratar  
		=> DAR UM JEITO AVISAR PARA COLETA DE VARIÁVEIS
		 	-> irá pegar os valores inseridos direto
	
	--> Tratar caso do owner que pode ter ou não
		=> Se tiver => deve ser guardado  
	
	--> Separar Grupo 6 
		- marcação_de_fim => deve estar separada 
		- 	
	--> 
