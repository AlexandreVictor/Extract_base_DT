Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
import json
import requests
SyntaxError: multiple statements found while compiling a single statement
>>> import json
>>> import requests
>>> api_url_base = "https://api.directtalk.com.br/1.4/info/contacts"
>>> headers = {
    'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
    'cache-control': "no-cache"
    }
>>> querystring = {"startDate":"1529280000","endDate":"1529366399","pageNumber":"1","pageSize":"10"}
>>> response = requests.request("GET", url, headers=headers, params=querystring)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    response = requests.request("GET", url, headers=headers, params=querystring)
NameError: name 'url' is not defined
>>> response = requests.request("GET", api_url_base, headers=headers, params=querystring)
>>> print(response.text)
[{"protocolNumber":"66477971-32","agentName":"Edvan Silva","agentLogin":"waEdvans","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1528977656,"contactStartedDate":1528982909,"contactFinishedDate":1529309872,"customerInQueueTime":5253,"agentServingTime":326963,"contactTotalTime":332216,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Navegação nos cursos | Dificuldade na navegação pelo conteúdo"],"mailQueue":"Anbima","mailStartQueue":"Anbima","origin":"helpdesk.anbima@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"thiago.m.montagner@jpmorgan.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Thiago"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66483943-82","agentName":"Edvan Silva","agentLogin":"waEdvans","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529015334,"contactStartedDate":1529057591,"contactFinishedDate":1529309930,"customerInQueueTime":42257,"agentServingTime":252339,"contactTotalTime":294596,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Navegação nos cursos | Dificuldade na navegação pelo conteúdo"],"mailQueue":"Cursos Livres - Estácio","mailStartQueue":"Cursos Livres - Estácio","origin":"helpdesk.cursoslivres@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"netobertuleza@hotmail.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Manoel"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66496109-72","agentName":"Ana Luisa","agentLogin":"waanaluisa","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529149656,"contactStartedDate":1529309301,"contactFinishedDate":1529310017,"customerInQueueTime":159645,"agentServingTime":716,"contactTotalTime":160361,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Dados de acesso | Redefinição de senha"],"mailQueue":"Avon","mailStartQueue":"Avon","origin":"atendimento.helpdesk@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"poliany24@yahoo.com.br"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Poliany"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66488917-42","agentName":"Edvan Silva","agentLogin":"waEdvans","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529066517,"contactStartedDate":1529067333,"contactFinishedDate":1529310314,"customerInQueueTime":816,"agentServingTime":242981,"contactTotalTime":243797,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Certificado | Certificado não disponível"],"mailQueue":"Cursos Livres - Estácio","mailStartQueue":"Cursos Livres - Estácio","origin":"helpdesk.cursoslivres@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"ivanirpipi@terra.com.br"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Raquel"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66496897-22","agentName":"Ana Luisa","agentLogin":"waanaluisa","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529157939,"contactStartedDate":1529309313,"contactFinishedDate":1529310419,"customerInQueueTime":151374,"agentServingTime":1106,"contactTotalTime":152480,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Cursos Presenciais | Informações sobre cursos presenciais"],"mailQueue":"Avon","mailStartQueue":"Avon","origin":"atendimento.helpdesk@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"waleriasmoreno@gmail.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Waleria"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66492744-42","agentName":"Edvan Silva","agentLogin":"waEdvans","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529083723,"contactStartedDate":1529309057,"contactFinishedDate":1529310603,"customerInQueueTime":225334,"agentServingTime":1546,"contactTotalTime":226880,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Certificado | Informações sobre o Certificado"],"mailQueue":"Fila Padrão","mailStartQueue":"Fila Padrão","origin":"helpdesk.anbima@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"paulavais09@gmail.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Paula"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66497312-32","agentName":"Ana Luisa","agentLogin":"waanaluisa","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529163156,"contactStartedDate":1529309340,"contactFinishedDate":1529310794,"customerInQueueTime":146184,"agentServingTime":1454,"contactTotalTime":147638,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Dados de acesso | Redefinição de senha"],"mailQueue":"Avon","mailStartQueue":"Avon","origin":"atendimento.helpdesk@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"kitana.rodrigues@yahoo.com.br"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Quitéria"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66493176-22","agentName":"Edvan Silva","agentLogin":"waEdvans","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529086239,"contactStartedDate":1529309096,"contactFinishedDate":1529310791,"customerInQueueTime":222857,"agentServingTime":1695,"contactTotalTime":224552,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Informações sobre os cursos | Dúvidas não relativas ao Portal"],"mailQueue":"Avon","mailStartQueue":"Avon","origin":"atendimento.helpdesk@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"vanessaregio@hotmail.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Vanessa"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66498561-02","agentName":"Ana Luisa","agentLogin":"waanaluisa","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529184817,"contactStartedDate":1529309343,"contactFinishedDate":1529310926,"customerInQueueTime":124526,"agentServingTime":1583,"contactTotalTime":126109,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Dados de acesso | Redefinição de senha"],"mailQueue":"Avon","mailStartQueue":"Avon","origin":"atendimento.helpdesk@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"revendedoras464@gmail.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Leidiane"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]},{"protocolNumber":"66493883-22","agentName":"Edvan Silva","agentLogin":"waEdvans","groupName":"","channel":"DTMail","departmentName":"E-mail","onSystemDate":1529094575,"contactStartedDate":1529309097,"contactFinishedDate":1529311443,"customerInQueueTime":214522,"agentServingTime":2346,"contactTotalTime":216868,"contactState":"RESPONDIDO","contactStateDetail":"Respondido pelo operador","classifications":["Dados de acesso | Redefinição de senha"],"mailQueue":"Avon","mailStartQueue":"Avon","origin":"atendimento.helpdesk@webaula.com.br","identifications":[{"key":"Consumidor_Chat","value":""},{"key":"CPF","value":""},{"key":"email","value":"joycepaulino2012@hotmail.com"},{"key":"nome","value":""}],"formAnswers":[{"question":"Nome do Aluno","answer":"Joyce"},{"question":"Tipo de atendimento","answer":"Suporte ao aluno"}],"ratings":[]}]
>>> def acesso_api():
	response.request.get(api_url_base, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

	
>>> acesso = acesso_api()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    acesso = acesso_api()
  File "<pyshell#15>", line 2, in acesso_api
    response.request.get(api_url_base, headers=headers)
AttributeError: 'PreparedRequest' object has no attribute 'get'
>>> def acesso_api():
	response.requests.get(api_url_base, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

	
>>> acesso = acesso_api()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    acesso = acesso_api()
  File "<pyshell#20>", line 2, in acesso_api
    response.requests.get(api_url_base, headers=headers)
AttributeError: 'Response' object has no attribute 'requests'
>>>  def acesso_api():
	response = requests.get(api_url_base, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None
	
SyntaxError: unexpected indent
>>> def acesso_api():
	response.requests.get(api_url_base, headers=headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

	
>>> acesso = acesso_api()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    acesso = acesso_api()
  File "<pyshell#24>", line 2, in acesso_api
    response.requests.get(api_url_base, headers=headers)
AttributeError: 'Response' object has no attribute 'requests'
>>> def acesso_api():
    
    response = requests.request("GET", api_url_base, headers=headers, params=querystring)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

>>> acesso = acesso_api()
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso.items();
	
SyntaxError: invalid syntax
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso.items():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')

		
Aqui estão as suas informações: 
Traceback (most recent call last):
  File "<pyshell#36>", line 3, in <module>
    for k, v in acesso.items():
AttributeError: 'list' object has no attribute 'items'
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso.itens():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')

		
Aqui estão as suas informações: 
Traceback (most recent call last):
  File "<pyshell#38>", line 3, in <module>
    for k, v in acesso.itens():
AttributeError: 'list' object has no attribute 'itens'
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso[].items():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')
		
SyntaxError: invalid syntax
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso['0'].items():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')

		
Aqui estão as suas informações: 
Traceback (most recent call last):
  File "<pyshell#41>", line 3, in <module>
    for k, v in acesso['0'].items():
TypeError: list indices must be integers or slices, not str
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso[0].items():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')

		
Aqui estão as suas informações: 
protocolNumber:66477971-32
agentName:Edvan Silva
agentLogin:waEdvans
groupName:
channel:DTMail
departmentName:E-mail
onSystemDate:1528977656
contactStartedDate:1528982909
contactFinishedDate:1529309872
customerInQueueTime:5253
agentServingTime:326963
contactTotalTime:332216
contactState:RESPONDIDO
contactStateDetail:Respondido pelo operador
classifications:['Navegação nos cursos | Dificuldade na navegação pelo conteúdo']
mailQueue:Anbima
mailStartQueue:Anbima
origin:helpdesk.anbima@webaula.com.br
identifications:[{'key': 'Consumidor_Chat', 'value': ''}, {'key': 'CPF', 'value': ''}, {'key': 'email', 'value': 'thiago.m.montagner@jpmorgan.com'}, {'key': 'nome', 'value': ''}]
formAnswers:[{'question': 'Nome do Aluno', 'answer': 'Thiago'}, {'question': 'Tipo de atendimento', 'answer': 'Suporte ao aluno'}]
ratings:[]
[!] Solicitação Invalida
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso[1].items():
		print('{0}:{1}'.format(k,v))
	else:
		print('[!] Solicitação Invalida')

		
Aqui estão as suas informações: 
protocolNumber:66483943-82
agentName:Edvan Silva
agentLogin:waEdvans
groupName:
channel:DTMail
departmentName:E-mail
onSystemDate:1529015334
contactStartedDate:1529057591
contactFinishedDate:1529309930
customerInQueueTime:42257
agentServingTime:252339
contactTotalTime:294596
contactState:RESPONDIDO
contactStateDetail:Respondido pelo operador
classifications:['Navegação nos cursos | Dificuldade na navegação pelo conteúdo']
mailQueue:Cursos Livres - Estácio
mailStartQueue:Cursos Livres - Estácio
origin:helpdesk.cursoslivres@webaula.com.br
identifications:[{'key': 'Consumidor_Chat', 'value': ''}, {'key': 'CPF', 'value': ''}, {'key': 'email', 'value': 'netobertuleza@hotmail.com'}, {'key': 'nome', 'value': ''}]
formAnswers:[{'question': 'Nome do Aluno', 'answer': 'Manoel'}, {'question': 'Tipo de atendimento', 'answer': 'Suporte ao aluno'}]
ratings:[]
[!] Solicitação Invalida
>>> >>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso[1].items():
		print('{0}:{1}'.format(k,v))
else:
	print('[!] Solicitação Invalida')
	
SyntaxError: invalid syntax
>>> if acesso is not None:
	print ("Aqui estão as suas informações: ")
	for k, v in acesso[1].items():
		print('{0}:{1}'.format(k,v))
else:
	print('[!] Solicitação Invalida')

	
Aqui estão as suas informações: 
protocolNumber:66483943-82
agentName:Edvan Silva
agentLogin:waEdvans
groupName:
channel:DTMail
departmentName:E-mail
onSystemDate:1529015334
contactStartedDate:1529057591
contactFinishedDate:1529309930
customerInQueueTime:42257
agentServingTime:252339
contactTotalTime:294596
contactState:RESPONDIDO
contactStateDetail:Respondido pelo operador
classifications:['Navegação nos cursos | Dificuldade na navegação pelo conteúdo']
mailQueue:Cursos Livres - Estácio
mailStartQueue:Cursos Livres - Estácio
origin:helpdesk.cursoslivres@webaula.com.br
identifications:[{'key': 'Consumidor_Chat', 'value': ''}, {'key': 'CPF', 'value': ''}, {'key': 'email', 'value': 'netobertuleza@hotmail.com'}, {'key': 'nome', 'value': ''}]
formAnswers:[{'question': 'Nome do Aluno', 'answer': 'Manoel'}, {'question': 'Tipo de atendimento', 'answer': 'Suporte ao aluno'}]
ratings:[]
>>> def escrevercsv(lista):
	with open('arquivoteste.csv')
	
SyntaxError: invalid syntax
>>> def escrevercsv(lista):
	with open('arquivoteste.csv','w',encoding='utf-8') as f:
		for protocolNumber in lista:
			f.write(protocolNumber +'\n')

			
>>> listateste = ['jose','maria','marcelo','jonas']
>>> escrevercsv(listateste)
>>> def escrevercsv(lista):
	with open('C:\Users\alexandre.silva\Desktop\Robôs\API - DT\arquivoteste.csv','w',encoding='utf-8') as f:
		for protocolNumber in lista:
			f.write(protocolNumber +'\n')
			
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> def escrevercsv(lista):
	with open('@C:\Users\alexandre.silva\Desktop\Robôs\API - DT\arquivoteste.csv','w',encoding='utf-8') as f:
		for protocolNumber in lista:
			f.write(protocolNumber +'\n')
			
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 3-4: truncated \UXXXXXXXX escape
>>> def escrevercsv(lista):
	with open('C:\\Users\\alexandre.silva\\Desktop\\Robôs\\API - DT\\arquivoteste.csv','w',encoding='utf-8') as f:
		for protocolNumber in lista:
			f.write(protocolNumber +'\n')

			
>>> escrevercsv(listateste)
>>> import csv
>>> def escrevercsv(lista):
	Arquivo = csv.writer(open("C:\\Users\\alexandre.silva\\Desktop\\Robôs\\API - DT\\arquivoteste.csv","wb"))
	Arquivo.writerow("Nome","Rua","Casa","Cep")

	
>>> escrevercsv(listateste)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    escrevercsv(listateste)
  File "<pyshell#66>", line 3, in escrevercsv
    Arquivo.writerow("Nome","Rua","Casa","Cep")
TypeError: writerow() takes exactly one argument (4 given)
>>> escrevercsv(listateste,listateste,listateste,listateste)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    escrevercsv(listateste,listateste,listateste,listateste)
TypeError: escrevercsv() takes 1 positional argument but 4 were given
>>> escrevercsv("teste","teste1","teste2","teste4")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    escrevercsv("teste","teste1","teste2","teste4")
TypeError: escrevercsv() takes 1 positional argument but 4 were given
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 5, in <module>
    class Acesso_API:
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in Acesso_API
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 5, in <module>
    class Acesso_API:
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in Acesso_API
    response = requests.request("GET", url_base, headers=headers)
NameError: name 'url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 5, in <module>
    class Acesso_API:
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in Acesso_API
    response = requests.request("GET", url_base, headers=headers)
NameError: name 'url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 5, in <module>
    class Acesso_API:
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in Acesso_API
    response = requests.request("GET", url_base, headers=headers)
NameError: name 'url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 5, in <module>
    class Acesso_API:
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in Acesso_API
    response = requests.request("GET", url_base, headers=headers)
NameError: name 'url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 5, in <module>
    class Acesso_API:
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 13, in Acesso_API
    response = requests.request("GET", url_base, headers=headers)
NameError: name 'url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 15, in <module>
    response = requests.request("GET", api_url_base, headers=headers, params=querystring)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 15, in <module>
    response = requests.request("GET", api_url_base, headers=headers, params=querystring)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 15, in <module>
    response = requests.request("GET", api_url_base, headers=headers, params=querystring)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 13, in <module>
    response = requests.request("GET", api_url_base, headers=headers, params=querystring)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 13, in <module>
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>>  api_url_base = 'https://api.directtalk.com.br/1.4/info/contacts'
 
SyntaxError: unexpected indent
>>> api_url_base = 'https://api.directtalk.com.br/1.4/info/contacts'
>>> headers = {
                            'Content-Type': 'application/json',
                            'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                            'cache-control': "no-cache"
                }
>>> response = requests.request("GET", api_url_base, headers=headers)
>>> if response.status_code == 200:
        print("Dados ok")
    else :
        print("No Ok")
        
SyntaxError: unindent does not match any outer indentation level
>>> if response.status_code == 200:
        print("Dados ok")
    else:
        print("No Ok")
        
SyntaxError: unindent does not match any outer indentation level
>>> if response.status_code == 200:
        print("Dados ok")
else:
        print("No Ok")

        
No Ok
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 13, in <module>
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 13, in <module>
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in <module>
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>> api_url_base
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    api_url_base
NameError: name 'api_url_base' is not defined
>>> api_url_base = 'https://api.directtalk.com.br/1.4/info/contacts'
>>> headers = {
                            'Content-Type': 'application/json',
                            'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                            'cache-control': "no-cache"
                }
>>> response = requests.request("GET", api_url_base, headers=headers)
>>> if response.status_code == 200:
        print("Dados ok")
else:
        print("No Ok")

No Ok
>>> if response.status_code == 200:
        print("Dados ok")
else:
        print(response.status_code)

500
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 14, in <module>
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 13, in <module>
    response = requests.request("GET", api_url_base, headers=headers)
NameError: name 'api_url_base' is not defined
>>> 
=== RESTART: C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py ===
Traceback (most recent call last):
  File "C:/Users/alexandre.silva/Desktop/Robôs/API - DT/acesso_API.py", line 17, in <module>
    if response.status_code == 200:
NameError: name 'response' is not defined
>>>   def dadosAcesso():
api_url_base = "https://api.directtalk.com.br/1.4/info/contacts"
headers = {
                            'Content-Type': 'application/json',
                            'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                            'cache-control': "no-cache"
                }
	querystring = {"startDate":"1529280000","endDate":"1529366399","pageNumber":"1"}
    response = requests.request("GET", api_url_base, headers=headers)
if response.status_code == 200:
        print("Dados ok")
else:
        print(response.status_code)
        
SyntaxError: unexpected indent
>>> def dadosAcesso():
api_url_base = "https://api.directtalk.com.br/1.4/info/contacts"
headers = {
                            'Content-Type': 'application/json',
                            'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                            'cache-control': "no-cache"
                }
	querystring = {"startDate":"1529280000","endDate":"1529366399","pageNumber":"1"}
    response = requests.request("GET", api_url_base, headers=headers)
if response.status_code == 200:
        print("Dados ok")
else:
        print(response.status_code)
        
SyntaxError: expected an indented block
>>> import requests

class AcessoAPI:
    
    def dadosAcesso():
headers = {
                            'Content-Type': 'application/json',
                            'authorization': "Basic d2FBcGk6Y2MxYzg3NjQtNTc3NS00OGRhLWE4N2UtNGY1M2QwZDIyMDQ2",
                            'cache-control': "no-cache"
                }
	querystring = {"startDate":"1529280000","endDate":"1529366399","pageNumber":"1"}
    response = requests.request("GET", "https://api.directtalk.com.br/1.4/info/contacts", headers=headers)
if response.status_code == 200:
        print("Dados ok")
else:
        print(response.status_code)
        
SyntaxError: multiple statements found while compiling a single statement
>>> 
