#Autor:Diego Silva
#Data:01/07/2020
#Descrição:Script para fazer parser de mensagens vindas do servidor backend

import ast
#crianda classe para parsers
class ParserMensagem:

	#parser de byte para string
	def buteParastring(self, mensagem):
		mensagem = mensagem.decode()
		mensagem = mensagem.replace('\n','')
		return mensagem

	#parser de string para dicionario
	def stringParadicionario(self, mensagem):
		dicionario = ast.literal_eval(mensagem)
		return dicionario
