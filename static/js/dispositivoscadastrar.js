/*
Autor:Diego Silva
Data:21/08/2020
Descrição:Script para interação com tela de cadastro de dispositivos
*/

//constantes
const CAMPOSNAOPREENCHIDOS = "Por favor, Preencha todos os campos para o cadastro do dispositivo";

//método para validar preenchimento de campos
function validaCampos(dispositovo, cliente,endereco,descricao){
	if((dispositovo=="")||(endereco=="")
		||(cliente=="")||(descricao=="")){
		return false;
	}
	else if((dispositovo==null)||(endereco==null)
		||(cliente==null)||(descricao==null)){
		return false;
	}else{
		return true;
	}
}

function mensagemusuarios(informacao){

	if(informacao=="Dispositivo Ja cadastrado"){
		return `Erro no cadastro: ${informacao.replace('Ja','Já')}`
	}else{
		return `Dispositivo cadastrado com sucesso ${informacao}`
	}

}
//método para cadastrar clientes
const cadastraNovoDispositivo = () =>{

	//pegando informações dos campos de input
	const dispositovo = document.querySelector('[data-form-device]')
	const cliente = document.querySelector('[data-form-client]')
	const endereco = document.querySelector('[data-form-address]')
	const descricao = document.querySelector('[data-form-description]')

	//validando que todos os campos foram preenchidos
	if(!validaCampos(dispositovo.value,
		cliente.value,
		endereco.value,
		descricao.value)){
		alert(CAMPOSNAOPREENCHIDOS)
	}else{
		const url = servidor(configuracao())+"/dispositivocadastraatualiza/CADASTRA";
		const resposta = postDadosDispositivos(dispositovo.value,
		cliente.value,
		endereco.value,
		descricao.value,
		url)

		resposta.then( dados =>{
			alert(mensagemusuarios(dados.Mensagem))
			console.log(dados.Mensagem);
		})
		console.log("funcionou");

		dispositovo.value =""
		cliente.value =""
		endereco.value  =""
		descricao.value  =""
	}
}

const botaosalva = document.querySelector('[data-form-button]')
botaosalva.addEventListener('click', cadastraNovoDispositivo);