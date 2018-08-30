__author__='AlVictor'

import json
import os
import time 
import datetime
import pyodbc as Banco

class GravaBanco:

    def __init__(self, dadosJson):
            self.dadosJson = dadosJson

    def insertdados(self, queryString):
            conexao = Banco.connect("Driver={SQL Server};Server=wadb02.webaula.dc;Database=waControlesAutomatizadosCGE;uid=alexandre;pwd=Balao#13") 
            #"Integrated Security=SSPI") --- usar windowsautentication
            totalitens = float(len(queryString))
            if totalitens >0:
               for i in range(0,int(totalitens)):
                cursor = conexao.cursor()
                sql_command = queryString[i]
                #print("Total Itens:",totalitens,"Itens Inseridos:",i,"Perc:",totalitens/(i+1))
                cursor.execute(sql_command)
            else:
                return None
            # nunca esqueça disso, se quiser que as alterações sejam salvas:
            conexao.commit()
            return print('Insert realizado com sucesso')

    def leitor(self):
         resultado = []
         for lista in range(len(self.dadosJson)):
           protocolo                  =  self.dadosJson[lista]['protocolNumber']
           agente                     =  self.dadosJson[lista]['agentName']
           canal                      =  self.dadosJson[lista]['channel']
           departmento                =  self.dadosJson[lista]['departmentName']
           data_entrada               =  (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.dadosJson[lista]['onSystemDate'])))
           data_inicio                =  (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.dadosJson[lista]['contactStartedDate'])))
           data_fim                   =  (time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.dadosJson[lista]['contactFinishedDate'])))
           tempo_fila                 =  str(self.dadosJson[lista]['customerInQueueTime'])
           tempo_atendimento          =  str(self.dadosJson[lista]['agentServingTime'])
           tempo_total_atendimento    =  str(self.dadosJson[lista]['contactTotalTime'])
           estado_contato             =  self.dadosJson[lista]['contactState']
           estado_contato_detalhe     =  self.dadosJson[lista]['contactStateDetail']
           classifications            =  self.dadosJson[lista]['classifications']
           if len(self.dadosJson[lista]['classifications']) == 1 :
               classifications = self.dadosJson[lista]['classifications']
               classificacao,detalhe   = str(classifications).replace('[\'','').replace('\']','').split(' | ')
           else:
               classificacao           = None
               detalhe                 = None
           localizacao_email           =  self.dadosJson[lista]['mailQueue']
           entrada_email               =  self.dadosJson[lista]['mailStartQueue']
           origem_atendimento          =  self.dadosJson[lista]['origin']
           if canal ==  "DTChat" or  canal ==  "DTBot":
                generico_1             =  self.dadosJson[lista]['identifications'][0]['key']
                generico_2             =  self.dadosJson[lista]['identifications'][0]['value']
           elif canal ==  "DTMail" or canal == "DTPhone":
                generico_1             =  self.dadosJson[lista]['identifications'][2]['key']
                generico_2             =  self.dadosJson[lista]['identifications'][2]['value']
           else:
                 generico_1            = None
                 generico_2            = None
           if len(self.dadosJson[lista]['formAnswers']) >= 2 :
                pergunta_1             = self.dadosJson[lista]['formAnswers'][0]['question']
                resposta_1             = self.dadosJson[lista]['formAnswers'][0]['answer']
                pergunta_2             = self.dadosJson[lista]['formAnswers'][1]['question']
                resposta_2             = self.dadosJson[lista]['formAnswers'][1]['answer']
           elif len(self.dadosJson[lista]['formAnswers']) == 1 :
                pergunta_1             = self.dadosJson[lista]['formAnswers'][0]['question']
                resposta_1             = self.dadosJson[lista]['formAnswers'][0]['answer']
                pergunta_2             = None
                resposta_2             = None
           else:
                pergunta_1             = None
                resposta_1             = None
                pergunta_2             = None
                resposta_2             = None
           if len(self.dadosJson[lista]['ratings']) == 1 :
                pesquisa               = self.dadosJson[lista]['ratings'][0]['question']
                res_ppesquisa          = self.dadosJson[lista]['ratings'][0]['answer']
           else:
               pesquisa                = None
               resp_pesquisa           = None
 
           
           #Prepara sintaxe de insert     
           colunas =('INSERT INTO tb_basegeral_DT (protocolo ,agente ,canal ,departmento ,data_entrada ,data_inicio ,data_fim ,'+
                     'tempo_fila ,tempo_atendimento ,tempo_total_atendimento ,estado_contato ,estado_contato_detalhe ,'+
                     'classificacao ,detalhe ,localizacao_email ,entrada_email ,origem_atendimento ,generico_1 ,generico_2 ,'+
                     'pergunta_1 ,resposta_1 ,pergunta_2 ,resposta_2 ,pesquisa ,resp_pesquisa) VALUES ') 
           listvalores = (protocolo ,agente ,canal ,departmento ,data_entrada ,data_inicio ,data_fim,
                      tempo_fila ,tempo_atendimento ,tempo_total_atendimento,estado_contato ,estado_contato_detalhe ,
                      classificacao ,detalhe ,localizacao_email ,entrada_email ,origem_atendimento ,generico_1 ,generico_2 ,
                      pergunta_1 ,resposta_1 ,pergunta_2 ,resposta_2 ,pesquisa ,resp_pesquisa)

           #Formata as strings para insert no banco
           valores = "("
           for i in range(0,len(listvalores)):

               if listvalores[i] is None or listvalores[i] == '':
                   valores += 'NULL'
                   valores += ","
               elif i>6 and i<10:
                   valores += str(listvalores[i]).replace('\'','')
                   valores +=","
               else:
                   valores +='\''+str(listvalores[i]).replace('\'','')+'\','
           valores = valores[:-1]
           colunas += valores+");"
           resultado.append(colunas)
         print("Dados .json formatados e prontos para inser no banco.")
         return resultado