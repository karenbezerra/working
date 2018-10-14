import os
import sys
import string
import re

arquivo = open('./sqlteste_insert.sql', 'r')
texto = arquivo.read()

#texto = texto.lower() #Desativei, pois agora o re.IGNORECASE foi ativado
texto = texto.replace("\r","") #Remove o \r, facilitar a tratativa de expressões regulares 
texto = texto.replace("\n","") #Remove a quebra de linhas
texto = texto.split(';') #Separa os comandos pelo ;




for linha_texto in range(len(texto)-1): #Lê o array do arquivo e remove a ultima linha após a formatação. O split causa um linha em branco, por isso o -1
    padraoregex = re.compile(r"(INSERT INTO\s+)([\w._]+)(\s+\()([\w+,?\s*]+)(\)\s+VALUES\s+)((\(['?\w+'?,?\s*]+\)\,?;?\s*)+)", re.IGNORECASE) #Regex, o re.IGNORECASE trata /i que o python n~ão possui, além disso procura os padrões 'INSERT INTO' e 'VALUES', a partir disso ele cria os grupos de busca: $2 nome da tabela, $4 campos e $6 os valores, para melhor visualizar recomendo o https://www.debuggex.com/
    linha = re.match(padraoregex, texto[linha_texto]) #Executa o regex para cada linha
    if linha is not None: #None é o retorno padão para o Regex não encontrado, logo podemos trata-lo como marcador para o que não é um insert
        print(f'A tabela {linha.group(2)} está sendo alterada') #Imprime apenas o grupo $2
    else:
        print(f"Os seu script não contém apenas inserts ou não está formatado corretamente a linha {linha_texto+1} não foi inserida, por gentileza validar") #Resolvido o bug de multiplas linhas com o Regex
   
