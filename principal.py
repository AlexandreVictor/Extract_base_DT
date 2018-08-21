__author__='AlVictor'

import datetime
from acesso_API import AcessoAPI

epoch = datetime.datetime(1970,1,1)

#string_date = input("Insira a Data Inicial: ")
string_date = "2018-08-01 00:00:00"
format = "%Y-%m-%d %H:%M:%S"
DataInicio = datetime.datetime.strptime(string_date, format)
#print("Data Inicio",DataInicio)
Eph_DtDtInicio = (DataInicio - epoch).total_seconds()

#string_date = input("Insira a Data Final:")
string_date = "2018-08-20 23:59:59"
format = "%Y-%m-%d %H:%M:%S"
DataFim = datetime.datetime.strptime(string_date, format)
Eph_DtFim = (DataFim - epoch).total_seconds()
#print("Data Fim",DataFim)



querystring = ("{startDate:"+str(Eph_DtDtInicio)+",endDate:"+str(Eph_DtFim)+",pageNumber:"+str(1)+"}")
print(querystring)
acessoAPI = AcessoAPI(querystring)
acessoAPI.conecta()
obj = acessoAPI.recuperaregistros()
print (obj)



#querystring = {"startDate":"1529280000","endDate":"1529366399","pageNumber":"1"}

#from acesso_API import AcessoAPI
#C = AcessoAPI(1,5,10,1)
#C.conecta()
