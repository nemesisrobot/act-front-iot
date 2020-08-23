#Autor:Diego Silva
#Data:19/08/2020
#Descrição:Script para leitura de arquivos e parser de dados de arquivos
import json as j

class TrabalhaArquivos:

	def __init__(self, caminho):
		self._caminho = caminho

	def abrearquivo(self, arquivo):
		return open('{}{}'.format(self._caminho,arquivo),'r') 

	def escrevearquivo(self, arquivo, dados):
		arquivo.write('{}'.format(dados))

	def lerarquivo(self, arquivo):
		return arquivo.read();

	def fechaarquivo(self, arquivo):
		arquivo.close()

#classe para ler arquivo de configuração
class ArquivoConfiguracao(TrabalhaArquivos):

	def __init__(self, caminho):
		super(ArquivoConfiguracao, self).__init__(caminho)

	def parserStringParaDicionario(self, dados):
		return j.loads(dados)

	def getServidor(self, dados):
		return dados['host-server']

	def getPorta(self, dados):
		return dados['port']

	def getFront(self, dados):
		return dados['host-front']

	def getPortFront(self, dados):
		return dados['port-front']

#classe para retorar acesso as configurações
class AcessoConfiguracao:

	def __init__(self, caminho):
		self._caminho = caminho


	def getObjetoLeitura(self):
		return ArquivoConfiguracao(self._caminho)

	def getConfiguracao(self, arquivo, dados):
		#abrindo arquivo e retonando parser
		return arquivo.parserStringParaDicionario(arquivo.lerarquivo(arquivo.abrearquivo(dados)))

