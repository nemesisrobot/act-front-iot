#Autor:Diego Silva
#Data:30/06/2020
#Descrição: Script para envio de dados ao backend


#importando bibliotecas para envio de dados e trabalha com formato json
import requests as rq
import json
from datetime import date , datetime

#cabeçalho para informar tipo de documento
HEADERS = {'content-type':'application/json'}

class EnviarMensagem:

	#metodo para fazer posto e retorna objetos 
	def envio(self, url_callback, dados_para_envio):
		return rq.post(url=url_callback, data=json.dumps(dados_para_envio), headers=HEADERS)

	#método para montar horario de envio
	def dataEnvio(self):
		dataatual = str(datetime.now())[0:19]
		data = datetime.strptime(dataatual, '%Y-%m-%d %H:%M:%S').date()
		hora = datetime.strptime(dataatual, '%Y-%m-%d %H:%M:%S').time()
		return '{} {}'.format(str(data.strftime('%Y-%m-%d')),str(hora.strftime('%H:%M:%S')))


