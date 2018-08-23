__author__='AlVictor'

import datetime
import time
from acesso_API import AcessoAPI


string_date = input("Insira a Data Inicial: ")
#string_date = "2018-08-21 00:00:00"
format = "%Y-%m-%d %H:%M:%S"
datainicio = datetime.datetime.strptime(string_date, format)
eph_dtinicio = int(time.mktime(time.strptime(string_date, '%Y-%m-%d %H:%M:%S')) - time.timezone)


string_date = input("Insira a Data Final:")
#string_date = "2018-08-21 23:59:59"
format = "%Y-%m-%d %H:%M:%S"
datafim = datetime.datetime.strptime(string_date, format)
eph_dtfim = int(time.mktime(time.strptime(string_date, '%Y-%m-%d %H:%M:%S')) - time.timezone)


nomearquivo = ("Extract_Atendimento_"+str(datainicio)+"_"+str(datafim)).replace(' ','_').replace(':','')


acessoAPI = AcessoAPI(eph_dtinicio, eph_dtfim, nomearquivo)

acessoAPI.conecta()

acessoAPI.recuperaregistros()

print("Rotina Finalizada")
