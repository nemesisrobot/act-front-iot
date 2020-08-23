function redirecionar(id){
	const nomedispositivo = document.getElementById("mytable").rows[id].cells[1].innerHTML
	window.location.href = `${servidorfront(configuracao())}/atualizadispositivo/${nomedispositivo}`;
}

function removerDispositvo(id){
	if(confirm("Deseja deletar o Dispositivo")){
		const nomedispositivo = document.getElementById("mytable").rows[id].cells[1].innerHTML
		console.log(nomedispositivo)
		deletaDispositvo(nomedispositivo).then( dados =>{
			alert(dados.Mensagem)
			console.log(dados.Mensagem);
		})
		
	}


}
//limpa tela
function limpatela(){
	if(document.querySelectorAll('.grid-item').length > 0){
		document.querySelectorAll('.grid-item').forEach(function(itens){
			itens.remove()
		})
	}
	//document.location.reload()
}

function conteudogrid(dispositivo,cliente,endereco,descricao,chave,id){

	const criandolinha = document.createElement('tr');
	criandolinha.classList.add(`grid-item`);
	 
	//alvo remoção
	const alvo=id;
	console.log(typeof(alvo))
	//motando conteudo
	const conteudo = `<td>${id}</td>
				   <td data-table-${alvo}>${dispositivo}</td>
				  <td>${cliente}</td>
				  <td>${endereco}</td>
				  <td>${descricao}</td>
				  <td>${chave}</td>
				  <button class="button excluir" onclick="removerDispositvo(${alvo})">Excluir</button>
				  <button class="button salvar" onclick="redirecionar(${alvo})"> Editar</button>
				 

				  `
	criandolinha.innerHTML = conteudo

	return criandolinha
}

const geragrid = (evento) =>{
	//previnindo ação do evento de enviar
	evento.preventDefault();
	limpatela();
	let id = 1;
	//criando elemento no html
	const listadispositivos = document.querySelector('[data-conteudo-tabela]');
	
	//pegando conteudo do campo input
	const inputcampo = document.querySelector('[data-form-device]')

	//coletando dados do servidor backend
	dadosdispositivos = getDadosDispositivos(servidor(configuracao())+"/dispositivobuscatodos")
	dadosdispositivos.then( exibedados =>{
		exibedados.forEach( indice =>{

			if((inputcampo.value=="")||(inputcampo.value==null)){
				listadispositivos.appendChild(conteudogrid(
					indice.device,indice.client,
				indice.address,indice.description,indice.key,id));
			}else{
				if(indice.device==inputcampo.value){
					listadispositivos.appendChild(conteudogrid(
					indice.device,indice.client,
				indice.address,indice.description,indice.key,id));
				}
			}
			id +=1;
		})
	})
	//console.log(servidor(configuracao())+"/dispositivobuscatodos");
	

}



//escutando evento do botão
const botaoconsulta = document.querySelector('[data-form-button]');

//adicionando escuta no evento de clicar no botão
botaoconsulta.addEventListener('click', geragrid)