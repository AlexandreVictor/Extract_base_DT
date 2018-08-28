__author__='AlVictor'

import datetime
import time
import os
from acesso_API import AcessoAPI
from leitor_arquivos import LeitorArquivos

#onde estão todos os arquivos do programa 
nomediretorio = os.path.dirname(os.path.realpath(__file__))

#string_date = input("Insira a Data Inicial: ")
string_date = "2018-08-01 00:00:00"
format = "%Y-%m-%d %H:%M:%S"
datainicio = datetime.datetime.strptime(string_date, format)
eph_dtinicio = int(time.mktime(time.strptime(string_date, '%Y-%m-%d %H:%M:%S')) - time.timezone)


#string_date = input("Insira a Data Final:")
string_date = "2018-08-01 23:59:59"
format = "%Y-%m-%d %H:%M:%S"
datafim = datetime.datetime.strptime(string_date, format)
eph_dtfim = int(time.mktime(time.strptime(string_date, '%Y-%m-%d %H:%M:%S')) - time.timezone)


nomearquivo = ("Extract_Atendimento_"+str(datainicio)+"_"+str(datafim)).replace(' ','_').replace(':','')

print(nomearquivo)
print(nomediretorio)
#acessoAPI = AcessoAPI(eph_dtinicio, eph_dtfim, nomearquivo)

#acessoAPI.conecta()

#acessoAPI.recuperaregistros()


leitorarquivos = LeitorArquivos(nomearquivo,nomediretorio)
leitorarquivos.leitor()



print("Rotina Finalizada")
