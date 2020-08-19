//fazendo get para pegar lista de dados
const consultaNotas = (urlcallback)=>{
	
	return fetch(urlcallback)
	.then( resposta => {
		return resposta.json();
	})
	.then( json => {
		return json;
	})
}