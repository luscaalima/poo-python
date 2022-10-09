import requests 

cep = input()
# url = 'https://API.lucaslima150.repl.co/pegarvendas'
url2=f'https://viacep.com.br/ws/{cep}/json/'
# requisicao = requests.get(url)
requisicao2 = requests.get(url2)
print(requisicao2.json())
# print(requisicao.json())
dicionario =requisicao2.json()
print(dicionario)
# print(dicionario['total_vendas'])