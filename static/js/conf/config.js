/*
Autor:Diego Silva
Data:19/08/2020
Descrição: Script para retornar configurações de sistema
*/



//retorna rotas de notas
function servidor(dadosbackend){
	return "http://"+dadosbackend['host-server']+":"+dadosbackend['port']
}

//json de dados do servidor
function configuracao(){
	return {
	"host-server":"192.168.15.15",
	"port":5000
	}
}