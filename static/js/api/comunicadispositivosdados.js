const postDadosDispositivos = (dispositovo, cliente,endereco,descricao, urlcallback) =>{
	const jsoncorpo = JSON.stringify({
		 device:dispositovo,
    	 client:cliente,
    	 address:endereco,
    	 description:descricao
	})

	const header = {'Content-type':'application/json'}
	return fetch(urlcallback,{
		method:'POST',
		headers:header,
		body:jsoncorpo
	}).then( resposta => {
		return resposta.json()
	})
}

const postAtualizaDispositivos = (dispositovo, cliente,endereco,descricao, chave, urlcallback) =>{
	const jsoncorpo = JSON.stringify({
		 device:dispositovo,
    	 client:cliente,
    	 address:endereco,
    	 description:descricao,
    	 key:chave
	})

	const header = {'Content-type':'application/json'}
	return fetch(urlcallback,{
		method:'POST',
		headers:header,
		body:jsoncorpo
	}).then( resposta => {
		return resposta.json()
	})
}

const getDadosDispositivos = (urlcallback) =>{
	return fetch(urlcallback)
	.then( resposta => {
		return resposta.json();
	})
	.then( json => {
		return json;
	})
}

//deletando dispositivo
const deletaDispositvo = (urlcallback) =>{
	const ulr = `${servidor(configuracao())}/dispositivoconsultaexclui/EXCLUIR/${urlcallback}`
	return fetch(ulr)
	.then( resposta => {
		return resposta.json();
	})

}