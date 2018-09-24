#coding:latin1
#!/usr/bin/python3
import os
import sys
import string

texto = ""
colunas = []
valores = []
i = 0

def quebra_script (script_completo):
	global scripts
	scripts = script_completo.split(';')
	tam = len(scripts)
	tam=-1
	scripts.pop(tam)


def trata_script():
	global texto 
	texto = texto.replace('(',' inicio ')
	texto = texto.replace(')', ' fim ')
	texto = texto.replace(',', ' ')
	texto = texto.replace('\n', ' ')
	texto = texto.replace('  ', ' ')
	texto = texto.lower()


""" refatorar mC)tonome_tabelado para aproveitar a variC!vel owner quando precisar/"""

def tem_owner(nome_tabela):
	if '.' in nome_tabela: 
		ow_tb = nome_tabela.split('.')
		owner = ow_tb[0]
		nome_tabela = ow_tb[1]
		return True
	else:
		return False 

def guarda_colunas(script):
	i=+1
	while script[i] != 'fim':
		colunas.append(script[i])
		i += 1
	return len(valores)

''' Por variável valores global p/ quando precisar'''
def guarda_valores(script): 
	global i 
	if script[i] == 'values':
		i=+1
		if script[i] == 'inicio':
			i=+1
			while (script[i]!= 'fim'):
				valores.append(script[1])
				i=+1
	return len(valores)	

''' Por variável owner global p/ quando precisar'''
def checa_insert(insert):
	global i 
	script = insert.split(' ') 

	if script[0] =='insert':
		
		if script[1] =='into':
			nome_tabela = script[2]
			owner_status = tem_owner(nome_tabela)
			i=3
			if (script[i] == 'inicio'):				
				qtde_colunas = guarda_colunas(script)
				qtde_valores = guarda_valores(script)
			elif script[i] == 'values':
				qtde_valores = guarda_valores(script)	
				qtde_colunas = 0 
			if qtde_colunas == qtde_valores:
				print('O script de insert esta validado.')
			elif qtde_colunas == 0:
				print('O script de insert está validado.')
			else: 
				print ('O número de colunas especificado é diferente do número de valores passados')          
		else: print('Script com formatacao incorreta, parametro \'into\' nao encontrando.')
	else: print('Este script nao eh de insercao. Parametro ' + script[0] + ' localizado no lugar do \'insert\'.')


arq = open('./sqlteste_insert.sql', 'r')
texto = arq.read()
trata_script()
scripts = []
quebra_script(texto)
for script in scripts:
	checa_insert(script)




