import json
import requests


# Headers is a dictionary
print(response.headers)

api_url_base = "https://api.directtalk.com.br/1.4/info/contacts"

headers = {
    'Content-Type': 'application/json',
    'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
    'cache-control': "no-cache"
    }

querystring = {"startDate":"1529280000","endDate":"1529366399","pageNumber":"1"}




print(response.text)




def acesso_api():
    
    response = requests.request("GET", api_url_base, headers=headers, params=querystring)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None



 if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso[1].items():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')        
