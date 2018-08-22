__author__='AlVictor'

import datetime
from acesso_API import AcessoAPI

epoch = datetime.datetime(1970,1,1)

#string_date = input("Insira a Data Inicial: ")
string_date = "2018-08-19 00:00:00"
format = "%Y-%m-%d %H:%M:%S"
DataInicio = datetime.datetime.strptime(string_date, format)
Eph_DtDtInicio = int((DataInicio - epoch).total_seconds())

#string_date = input("Insira a Data Final:")
string_date = "2018-08-19 23:59:59"
format = "%Y-%m-%d %H:%M:%S"
DataFim = datetime.datetime.strptime(string_date, format)
Eph_DtFim = int((DataFim - epoch).total_seconds())

nomearquivo = ("Extract_Atendimento_"+str(DataInicio)+"_"+str(DataFim)).replace(' ','_').replace(':','')
querystring = ("{startDate:"+str(Eph_DtDtInicio)+",endDate:"+str(Eph_DtFim)+",pageNumber:")#+str(1)+"}")

acessoAPI = AcessoAPI(querystring,nomearquivo)

acessoAPI.conecta()

acessoAPI.recuperaregistros()

print("Rotina Finalizada")
