import requests

def pegar_cotacoes(codigo_moeda):
    try:
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")
        requisicao_dic = requisicao.json()
        cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']
        return cotacao
    except:
        print("Código de Moeda Inválido")
        return None

'''
# linha 1: 'import requests' 
Prioritariamente vamos ver muito disso, para fazer interação com API

# linha 3: 'def pegar_cotacoes(codigo_moeda):'
Definimos uma função chamada 'pegar_cotacoes' que quando usada vamos colocar o código da moeda, 
como (USD, EUR, BTC ...)

# linha 5: 'requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{codigo_moeda}-BRL")' 
com o "requests.get" vamos pegar uma informação do link que está digitado. As chaves com "{codigo_moeda}"
vai ser digitado pelo usuário.

# linha 6: 'requisicao_dic = requisicao.json()'
Criamos a variável 'requisicao_dic' que vai ser igual a 'requisicao.json()' que faz a troca de informações 
com o site que está na LINHA 5 em um formato de dicionário que é o formato json.

# linha 7: 'cotacao = requisicao_dic[f'{codigo_moeda}BRL']['bid']' 
A "cotacao" é igual a "requisicao_dic" que é o dicionário com o formato json. 
O "[f'{codigo_moeda}BRL']" vai pegar o código digitado pelo usuário e vai entrar no dicionário dele, 
e puxar o "['bid']" que é a 'key' do dicionário que está o 'value' da "cotacao" que estamos buscando.

# linha 8: 'return cotacao'
Vai retornar a cotação da moeda que pedimos
'''

    