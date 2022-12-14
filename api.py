# instala a biblioteca requests no meu programa
import requests
# importa biblioteca que imprime bonito Pretty Print
import pprint
# dando um apelido pro comando
bunitinho =  pprint.pprint
# dominio e path base da api
domain = 'https://dadosabertos.camara.leg.br/api/v2/'

def busca_deputado(): 
    # recurso a ser utilizado
    path = 'deputados'
    # endereco a ser pesquisado
    url = domain + path
    # parametros
    params = {'nome': '', 'ordem': 'asc', 'ordenarPor': 'id'}
    params['nome'] = input('qual o nome do deputado:')
    # faz um get no site dados abertos da camara e obtem a listagem dos deputados
    r = requests.get(url, params)
    # imprime o status code
    #print(r.status_code)
    # imprime o conteudo json formatado pra ficar bonito com a pprint
    #bunitinho(r.json())
    data = r.json()
    # imprime somente o nome e o id do deputado
    for deputado in data['dados']:
        print('nome:',deputado['nome'],' id:',deputado['id'])

busca_deputado()