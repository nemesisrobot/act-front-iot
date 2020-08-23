/*
Autor:Diego Silva
Data:19/08/2020
Descrição: Script para retornar configurações de sistema
*/



//retorna link composto por ip e porta 
function servidor(dadosbackend){
	return "http://"+dadosbackend['host-server']+":"+dadosbackend['port']
}

//retorna link de front
function servidorfront(dadosfront){
	return "http://"+dadosfront['host-front']+":"+dadosfront['front-port']
}
function configuracao(){
	return {
	"host-server":"192.168.15.15",
	"port":5000,
	"host-front":"192.168.15.15",
	"front-port":5005
	}
}