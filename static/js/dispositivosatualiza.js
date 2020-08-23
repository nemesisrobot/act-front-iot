function ulratualizadispositivo(){
	return servidor(configuracao())
	+"/dispositivocadastraatualiza/ATUALIZA"
}

function mensagemusuarios(informacao){
	return informacao; 
}

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

const atualizadados = (evento) =>{
	evento.preventDefault()
	const dispositivo = document.querySelector('[data-form-device]').value
	const cliente = document.querySelector('[data-form-client]').value
	const endereco = document.querySelector('[data-form-address]').value
	const descricao = document.querySelector('[data-form-description]').value
	const chave = document.querySelector('[data-form-key]').value

	if(!validaCampos(dispositivo,cliente,endereco,descricao)){
		alert("Por favor, verifique se todos os campos estão preenchidos")
	}else{
		const resposta = postAtualizaDispositivos(dispositivo,cliente,endereco,descricao,
			chave,ulratualizadispositivo())
		resposta.then( dados =>{
			alert(mensagemusuarios(dados.Mensagem))
			console.log(dados.Mensagem);
		})
	}

}

//criando escuta de evento
const botaoatualiza = document.querySelector('[data-form-button]');
botaoatualiza.addEventListener('click', atualizadados)