# instala a biblioteca requests no meu programa
import requests
# importa biblioteca que imprime bonito Pretty Print
import pprint

# faz um get no site dados abertos da camara e obtem a listagem dos deputados
r = requests.get('https://dadosabertos.camara.leg.br/api/v2/deputados')
# imprime o status code
print(r.status_code)
# imprime o conteudo json formatado pra ficar bonito com a pprint
pprint.pprint(r.json())