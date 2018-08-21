__author__='AlVictor'

import requests
import simplejson as json
class AcessoAPI:


        url = "https://api.directtalk.com.br/1.4/info/contacts"
        cabecalho = {
                    'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                    'cache-control': "no-cache"
                    }

        def __init__(self, querystring):
            self.querystring = querystring
                                        
        def conecta(self):
            response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho)
            if response.status_code == 500:
             return print("Acessos validados com sucesso!")
            else:
             return print(response.text)
        def recuperaregistros(self):
            response  = requests.request("GET", self.__class__.url, headers=self.__class__.cabecalho, params=self.querystring)
            dados_json = json.loads(response.content)
            #Captura o total de pags
            #return response.headers['X-Pagination-TotalPages']
            return dados_json
teste