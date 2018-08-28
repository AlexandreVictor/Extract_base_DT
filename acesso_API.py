__author__='AlVictor'

import requests
import simplejson as json
from grava_arquivos  import GravaArquivos

class AcessoAPI:


        url = "https://api.directtalk.com.br/1.4/info/contacts"
        cabecalho = {
                    'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                    'cache-control': "no-cache"
                    }
        pagenumber = 1
        querystring = ""
        dados_py = []
    
        def __init__(self, eph_dt_inicio,eph_dtfim, nomearquivo):
            self.eph_dt_inicio = eph_dt_inicio
            self.eph_dtfim = eph_dtfim
            self.nomearquivo = nomearquivo
                                        
        def conecta(self):
            response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho)
            if response.status_code == 500:
             return print('Acessos validados com sucesso!')
            else:
             return print(response.text)
        def recuperaregistros(self):
            self.__class__.querystring = ("startDate="+str(self.eph_dt_inicio)+"&endDate="+str(self.eph_dtfim)+"&pagenumber="+str(self.__class__.pagenumber)+"&dateInfo=onSystem")
            Response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho, params= self.__class__.querystring)
            totalpags = int(Response.headers['X-Pagination-TotalPages'])
            print("Total de Paginas:",totalpags)
            if totalpags > 0:
                totallinhas = int(Response.headers['x-pagination-totalresults'])
                print("Total Linhas",totallinhas)
                while totalpags >= self.__class__.pagenumber  :
                         self.__class__.querystring = ("startDate="+str(self.eph_dt_inicio)+"&endDate="+str(self.eph_dtfim)+"&pagenumber="+str(self.__class__.pagenumber)+"&dateInfo=contactFinished")
                         ## contactFinished = data que o atendimento foi finalizado | onSystem =  data de entrada do atendimento no sistema
                         Response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho, params= self.__class__.querystring)
                         print("Pagina Atual: ",self.__class__.pagenumber,"/",totalpags)
                         self.__class__.dados_py += json.loads(Response.text)
                         self.__class__.pagenumber += 1
            else:
                return print("Não existem dados")
            gravar = GravaArquivos(self.nomearquivo,self.__class__.dados_py)
            gravar.save_json()

            return None
