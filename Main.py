__author__='AlVictor'

import datetime
import time
import os
from datetime import timedelta
from acesso_API   import AcessoAPI
from grava_banco  import GravaBanco


#string_date = input("Insira a Data Inicial: ")
string_date = "2018-08-30 17:00:00"
format = "%Y-%m-%d %H:%M:%S"
datainicio = datetime.datetime.strptime(string_date, format)
eph_dtinicio = int(time.mktime(time.strptime(string_date, '%Y-%m-%d %H:%M:%S')) - time.timezone)

t = datainicio
s = datetime.datetime.now()
ss = (s-t)


#string_date = input("Insira a Data Final:")
string_date = "2018-08-29 23:59:59"
format = "%Y-%m-%d %H:%M:%S"
datafim = datetime.datetime.strptime(string_date, format)
eph_dtfim = int(time.mktime(time.strptime(string_date, '%Y-%m-%d %H:%M:%S')) - time.timezone)




#Chama Class e passa os parametros
acessoAPI = AcessoAPI(eph_dtinicio, eph_dtfim)
#Verifica se a API está disponivel
acessoAPI.conecta()
#Recupera os dados da API
dadosJson = acessoAPI.recuperaregistros()

#Chama Class e passa os parametros
gravabanco = GravaBanco(dadosJson)
#Chama o metodo de leitura do .json
queryString = gravabanco.leitor()
#Aqui os dados são gravados diretamente no banco
gravabanco.insertdados(queryString)

print("Rotina Finalizada")
print(datetime.datetime.now())

