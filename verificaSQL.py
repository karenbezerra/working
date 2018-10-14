import os
import sys
import string
import re

arquivo = open('./sqlteste_insert.sql', 'r')
texto = arquivo.read()

texto = texto.lower()
texto = texto.replace("\r","") #Remove o \r, facilitar a tratativa de expressões regulares 
texto = texto.replace("\n","") #Remove a quebra de linhas
texto = texto.split(';') #Separa os comandos pelo ;




for linha_texto in range(len(texto)-1):
    padraoregex = re.compile(r"(INSERT INTO\s+)([\w._]+)(\s+\()([\w+,?\s*]+)(\)\s+VALUES\s+\()(['?\w+'?,?\s*]+)(\))", re.IGNORECASE)
    linha = re.match(padraoregex, texto[linha_texto])
    print(f'A tabela {linha.group(2)} está sendo alterada')

#valida = re.findall('( |CREATE|ALTER|DROP|SELECT|DECLARE|INSERT\s+INTO|UPDATE\s+\S+\s+SET|DELETE\s+FROM|EXEC(UTE){0,1}|UNION(\s+ALL){0,1})\s', texto)
#Novo teste
#Teste3