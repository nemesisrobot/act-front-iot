#Autor:Diego Silva
#Data:27/01/2020
#Descrição:Script para criação de rotas de cadastro
#biblioteca flask e flask_restful para tabalhar com micro serviços
from sys import path
import ast
path.append('/scripts')
from flask import Flask , render_template, request, redirect, url_for
from scripts.enviorequisicoes import EnviarMensagem

app = Flask(__name__)

#endereço do servidor backend
HOSTBACK = 'http://192.168.15.15:5000'

#endereço do computador a ser acesso para web application
HOST = '192.168.15.15'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/notas')
def cadastraNotas():
    return render_template('cadastronotas.html', localhost = HOST) 

#end-point para envio de notas de corte e religa
@app.route('/cortereliga', methods=['POST'])
def envioCorteReliga():
    reposta = 500
    disparo_mensagem = EnviarMensagem() 
    if(request.form['acao']=='turnoon'):
        resposta = disparo_mensagem.envio('{}/{}'.format(HOSTBACK,'notaservico'), {'device':request.form['macid'],'corte':1,'data':'{}'.format(disparo_mensagem.dataEnvio())})
    else:
        resposta = disparo_mensagem.envio('{}/{}'.format(HOSTBACK,'notaservico'), {'device':request.form['macid'],'corte':0,'data':'{}'.format(disparo_mensagem.dataEnvio())})

    mensagem =  (resposta.content).decode()
    mensagem = mensagem.replace('\n','')

    return redirect('/cortereliga/{}/{}'.format(str(resposta.status_code),mensagem))

@app.route('/cortereliga/<string:codigo>/<string:mensagem>')
def repsotaservidor(codigo,mensagem):
    dadosjson = ast.literal_eval(mensagem)

    if int(codigo) == 201:
        codigorequisicao = 'Nota cadastrada com sucesso'
    return render_template('resultado.html', nota =dadosjson['Codigo'] , resposta = codigorequisicao) 


#end-point para status do dispostivo
@app.route('/statusdispositivos')
def pesquisaStatus():
    return render_template('status.html') 


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005)