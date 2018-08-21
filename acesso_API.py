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
        pageNumber = 1
        dados_py = []
    
        def __init__(self, querystring,nomearquivo):
            self.querystring = querystring
            self.nomearquivo = nomearquivo
                                        
        def conecta(self):
            response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho)
            if response.status_code == 500:
             return print('Acessos validados com sucesso!')
            else:
             return print(response.text)
        def recuperaregistros(self):
            response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho, params=self.querystring+str(self.__class__.pageNumber)+"}")
            totalpags = int(response.headers['X-Pagination-TotalPages'])
            
            print("Total de Paginas:",totalpags)
            if totalpags > 0:
                while totalpags >= self.__class__.pageNumber  :
                         response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho, params=self.querystring+str(self.__class__.pageNumber)+"}")            
                         TotalLinhas = int(response.headers['x-pagination-totalresults'])
                         print("Total Linhas",TotalLinhas)
                         print("Pagina Atual: ",self.__class__.pageNumber,"/",totalpags)
                         print(self.querystring+str(self.__class__.pageNumber)+"}")
                         self.__class__.dados_py += json.loads(response.text)
                         self.__class__.pageNumber += 1
            else:
                return print("Não existem dados")
            gravar = GravaArquivos(self.nomearquivo,self.__class__.dados_py)
            gravar.save_json()
            return None
