#Autor:Diego Silva
#Data:27/07/2020
#Descrição:Script para criação de rotas de cadastro

from sys import path
import ast
path.append('/scripts')
from flask import Flask , render_template, request, redirect, url_for
from scripts.enviorequisicoes import EnviarMensagem
from scripts.parsermensagensservidor import ParserMensagem
from scripts.leituraarquivos import AcessoConfiguracao

#instanciando classe para parser de mensagens do servidor
parser = ParserMensagem()

app = Flask(__name__)

#lendo arquivo de configuração
arquivoconf = AcessoConfiguracao('static/js/conf/')
configuracao = arquivoconf.getConfiguracao(arquivoconf.getObjetoLeitura(),'config.json')

#endereço do servidor backend
HOSTBACK = 'http://{}:{}'.format(configuracao['host-server'],configuracao['port'])

HOSTFRONT = 'http://{}:{}'.format(configuracao['host-front'],configuracao['port-front'])


#lista de status


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/notas')
def cadastraNotas():
    return render_template('cadastronotas.html', localhost = HOSTFRONT) 

#end-point para envio de notas de corte e religa
@app.route('/cortereliga', methods=['POST'])
def envioCorteReliga():
    #reposta = 500
    disparo_mensagem = EnviarMensagem() 
    dados=disparo_mensagem.coletardadosservidor('{}/dispositivoconsultaexclui/CONSULTA/{}'.format(HOSTBACK,request.form['macid']))
    dados = parser.stringParadicionario(parser.byteParastring(dados.content))
    print(dados)
    #print(type(dados['device']))

    if (request.form['macid']).lstrip()=='':
        return render_template('resultadofalha.html', resposta = "Nota não criada.\n Evite colocar espaços ou caracteres especiais!!!")

    if(dados == "Dispositivo Nao Localizado"):
         return render_template('resultadofalha.html', resposta = "Nota não criada.\n Cadastre o dispositivo!!!")
         
    if(request.form['acao']=='turnoon'):
        resposta = disparo_mensagem.envio('{}/{}'.format(HOSTBACK,'notaservico'), {'device':request.form['macid'],'corte':1,'data':'{}'.format(disparo_mensagem.dataEnvio())})
    else:
        resposta = disparo_mensagem.envio('{}/{}'.format(HOSTBACK,'notaservico'), {'device':request.form['macid'],'corte':0,'data':'{}'.format(disparo_mensagem.dataEnvio())})


    return redirect('/cortereliga/{}/{}'.format(str(resposta.status_code),parser.byteParastring(resposta.content)))

@app.route('/cortereliga/<string:codigo>/<string:mensagem>')
def repostaservidor(codigo,mensagem):
    dadosjson = parser.stringParadicionario(mensagem)

    if int(codigo) == 201:
        codigorequisicao = 'Nota cadastrada com sucesso'
        return render_template('resultadosucesso.html', nota =dadosjson['Codigo'] , resposta = codigorequisicao) 

    if int(codigo) == 400:
        dadosjson = ast.literal_eval(dadosjson)
        return render_template('resultadofalha.html', resposta = dadosjson['mensagem'])

#end-point para status do dispostivo
@app.route('/consultastatusdispositivos')
def pesquisaStatus():
    return render_template('consultastatus.html', localhost = HOSTFRONT) 

#end-point para consultar status do disposito no servidor
@app.route('/pegandostatus', methods=['POST'])
def pegandostatusservidor():

    #checando se mensagem está em branco
    if (request.form['dispositivo']).lstrip()=='':
         return render_template('resultadofalha.html', resposta = "Evite colocar espaços ou caracteres especiais!!!")

    dispostivo_status = EnviarMensagem() 
    dadosjson = dispostivo_status.coletardadosservidor('{}{}{}'.format(HOSTBACK,'/dispositivostatus/',request.form['dispositivo']))
    dadosjson = parser.byteParastring(dadosjson.content)

    if int(parser.stringParadicionario(dadosjson)['corte']) == 3:
         return render_template('resultadofalha.html', resposta = "Dispostivo não localizado!!!")

    if int(parser.stringParadicionario(dadosjson)['corte']) == 0:
        return render_template('statusdispositivo.html', dispostivo=parser.stringParadicionario(dadosjson)['device'],
            estado='Desligado',
            datacomunicacao=parser.stringParadicionario(dadosjson)['data'])
    else:
        return render_template('statusdispositivo.html', dispostivo=parser.stringParadicionario(dadosjson)['device'],
            estado='Ligado',
            datacomunicacao=parser.stringParadicionario(dadosjson)['data'])
   
#end-point para consulta de notas
@app.route('/consultanotas')
def consultadenotas():
    return render_template('consultanotas.html')

#end-point para tela de consulta dispositivos
@app.route('/dispositivos')
def dispositivos():
    return render_template('dispositivos.html', localhost=HOSTFRONT)

#end-point para tela de cadasta dispisitvos
@app.route('/cadastrodispositivos')
def cadastrodispositivo():
    return render_template('cadastrodispositivo.html')

@app.route('/atualizadispositivo/<string:device>')
def atualizadispositivo(device):
    consulta = EnviarMensagem() 
    dados=consulta.coletardadosservidor('{}/dispositivoconsultaexclui/CONSULTA/{}'.format(HOSTBACK,device))
    dados = parser.stringParadicionario(parser.byteParastring(dados.content))
    return render_template('atualizadispositivo.html',
        dispositvo=dados['device'],
        cliente=dados['client'],
        endereco=dados['address'],
        descricao=dados['description'],
        chave=dados['key'])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005, debug=True)
