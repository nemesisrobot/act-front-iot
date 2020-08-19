
//limpa tela
function limpatela(){
	if(document.querySelectorAll('.grid-item').length > 0){
		document.querySelectorAll('.grid-item').forEach(function(itens){
			itens.remove()
		})
	}
}


//método para tratar dados coletados do back-end
const exibeNotas = (device, tipo, data) => {
	const nota = document.createElement('div');
	nota.classList.add('grid-item')
	
	//sé a nota for 1 é relgia 0 é corte
	if(tipo == 1){
		tipo="Religa";
	}else{
		tipo="Corte";
	}

	//escreve conteudo na pagina html
	const conteudo = 
		`Dispositivo: ${device}
		 <br>Nota: ${tipo}
		 <br>Data: ${data}`
	nota.innerHTML = conteudo;
	return nota; 
}


//método para percorrer reposta e addciona ele
const populagrid = (evento) => {
	
	
	evento.preventDefault();
	//impando grid
	limpatela();

	//pegando elemento onde vais ser populado as notas de serviço
	const grid = document.querySelector('[data-list]');

	//coletando dados
	console.log(servidor(configuracao()))
	//"http://192.168.15.15:5000/notaservico"
	dados = consultaNotas(servidor(configuracao())+"/notaservico")

	//pegando dado do campo input
	const campo = document.querySelector('[data-form-numero]').value;
	//populando grid
	console.log(dados)
	dados.then( exibe => {
		exibe.forEach( indice => {
		if(campo !=null && campo!=""){
			if( indice.device == campo){
			  grid.appendChild(exibeNotas(indice.device, indice.corte, indice.data))
			}
		  }
		 else{
		 	  grid.appendChild(exibeNotas(indice.device, indice.corte, indice.data))
		 }
			
		})
	})

}
//escutando grid

const listanotas = document.querySelector('[data-form-button]');
listanotas.addEventListener('click', populagrid);