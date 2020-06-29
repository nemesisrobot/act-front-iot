#Autor:Diego Silva
#Data:27/01/2020
#Descrição:Script para criação de rotas de cadastro
#biblioteca flask e flask_restful para tabalhar com micro serviços
from sys import path
path.append('/scripts')
from flask import Flask , render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/notas')
def cadastraNotas():
    return render_template('cadastronotas.html') 

@app.route('/cortereliga', methods=['POST'])
def envioCorteReliga():
    

    if(request.form['acao']=='turnoon'):
        return {'device':request.form['macid'],'corte':1,'data':'20/04/2020 10:10:10'} 
    else:
        return {'device':request.form['macid'],'corte':0,'data':'20/04/2020 10:10:10'} 

   

@app.route('/statusdispositivos')
def pesquisaStatus():
    return render_template('status.html') 

app.run(port=5005, debug=True)
