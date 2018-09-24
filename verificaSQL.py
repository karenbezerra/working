import os
import sys
import string
import re

arquivo = open('./sqlteste_insert_original.sql', 'r')
texto = arquivo.read()


texto = texto.replace("\r","") #Remove o \r, facilitar a tratativa de expressões regulares 
texto = texto.replace("\n","") #Remove a quebra de linhas
texto = texto.split(';') #Separa os comandos pelo ;


for linha_texto in range(len(texto)):
    linha = re.findall('(SELECT\s[\w\*\)\(\,\s]+\sFROM\s[\w]+)|(UPDATE\s[\w]+\sSET\s[\w\,\'\=]+)|(INSERT\sINTO\s[\d\w]+[\s\w\d\)\(\,]*\sVALUES\s\([\d\w\'\,\)]+)|(DELETE\sFROM\s[\d\w\'\=]+)' , texto[linha_texto])
    print(linha)



#print 'id: %s; function: %s; method: %s; class: %s --total == %s' % \
 #  (id, function, method, class, total)

#valida = re.findall('(INSERT|CREATE|ALTER|DROP|SELECT|DECLARE|INSERT\s+INTO|UPDATE\s+\S+\s+SET|DELETE\s+FROM|EXEC(UTE){0,1}|UNION(\s+ALL){0,1})\s', texto)
