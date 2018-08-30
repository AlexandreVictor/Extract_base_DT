__author__='AlVictor'

import json
import os
import time 
import datetime
class LeitorArquivos:
    def __init__(self, nomearquivo, nomediretorio):
            self.nomearquivo = nomearquivo
            self.nomediretorio = nomediretorio

    def leitor(self):
        #Verifica se o arquivo existe
        t = 0
        resultado = []
        for arquivos in os.listdir(self.nomediretorio):
             if (arquivos.endswith('.json')):
              dadosJson = json.loads(open(arquivos).read())
              for lista in range(0, len(dadosJson)):
                #print(lista)
                protocolo                  =  dadosJson[lista]['protocolNumber']
                agente                     =  dadosJson[lista]['agentName']
                canal                      =  dadosJson[lista]['channel']
                departmento                =  dadosJson[lista]['departmentName']
                data_entrada               =  (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dadosJson[lista]['onSystemDate'])))
                data_inicio                =  (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dadosJson[lista]['contactStartedDate'])))
                data_fim                   =  (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(dadosJson[lista]['contactFinishedDate'])))
                tempo_fila                 =  float(dadosJson[lista]['customerInQueueTime'])
                tempo_atendimento          =  float(dadosJson[lista]['agentServingTime'])
                tempo_total_atendimento    =  float(dadosJson[lista]['contactTotalTime'])
                estado_contato             =  dadosJson[lista]['contactState']
                estado_contato_detalhe     =  dadosJson[lista]['contactStateDetail']
                classifications            = dadosJson[lista]['classifications']
                if len(dadosJson[lista]['classifications']) == 1 :
                    classifications = dadosJson[lista]['classifications']
                    classificacao,detalhe   = str(classifications).replace('[\'','').replace('\']','').split(' | ')
                else:
                    classificacao           = ''
                    detalhe                 = ''
                localizacao_email           =  dadosJson[lista]['mailQueue']
                entrada_email               =  dadosJson[lista]['mailStartQueue']
                origem_atendimento          =  dadosJson[lista]['origin']
                if canal ==  "DTChat" or  canal ==  "DTBot":
                     generico_1             =  dadosJson[lista]['identifications'][0]['key'] 
                     generico_2             =  dadosJson[lista]['identifications'][0]['value'] 
                elif canal ==  "DTMail" or canal == "DTPhone":
                     generico_1             =  dadosJson[lista]['identifications'][2]['key'] 
                     generico_2             =  dadosJson[lista]['identifications'][2]['value']
                else:
                      generico_1            = ''
                      generico_2            = ''
                if len(dadosJson[lista]['formAnswers']) >= 2 :
                     pergunta1              = dadosJson[lista]['formAnswers'][0]['question']
                     resposta1              = dadosJson[lista]['formAnswers'][0]['answer']
                     pergunta2              = dadosJson[lista]['formAnswers'][1]['question']
                     resposta2              = dadosJson[lista]['formAnswers'][1]['answer']
                elif len(dadosJson[lista]['formAnswers']) == 1 :
                     pergunta1              = dadosJson[lista]['formAnswers'][0]['question']
                     resposta1              = dadosJson[lista]['formAnswers'][0]['answer']
                     pergunta2              = ''
                     resposta2              = ''
                else:
                     pergunta1              = ''
                     resposta1              = ''
                     pergunta2              = ''
                     resposta2              = ''
                if len(dadosJson[lista]['ratings']) == 1 :
                     pesquisa               = dadosJson[lista]['ratings'][0]['question']
                     resppesquisa           = dadosJson[lista]['ratings'][0]['answer']
                else:
                    pesquisa                = ''
                    resppesquisa            = ''
                t += 1
              print(t)