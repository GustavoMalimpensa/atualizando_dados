import os
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote_plus

# Caminho completo para o arquivo principal (tratativa.py)
caminho_principal = os.path.abspath(__file__)

# Caminho completo para o arquivo telefone.json
caminho_telefone_json = os.path.join(os.path.dirname(caminho_principal), '..', 'telefone', 'telefone.json')

# Caminho completo para o arquivo empresas.json
caminho_empresas_json = os.path.join(os.path.dirname(caminho_principal), '..', 'empresas.json')

# Carregar os dados do arquivo JSON (empresas.json)
with open(caminho_empresas_json, 'r', encoding='utf-8') as arquivo_json:
    dados_empresas = json.load(arquivo_json)

# Função para encontrar o telefone de uma empresa
def encontrar_telefone_empresa(razao_social):
    query = quote_plus(razao_social) + "+telefone"

    link = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    requisicao = requests.get(link, headers=headers)  # requisição GET para obter o conteúdo da página

    if requisicao.status_code == 200:
        telefone = BeautifulSoup(requisicao.text, "html.parser")  # criar um objeto BeautifulSoup para fazer o parsing do conteúdo HTML

        telefone_empresa = telefone.find("span", class_="mw31Ze")  # encontrar o elemento <cite> na página

        if telefone_empresa:
            return telefone_empresa.get_text()
        else:
            return "telefone não encontrado"

    return "Erro na requisição"

# Lista para armazenar os telefone das empresas
telefone_empresas = []

# Iterar pelas empresas e encontrar o telefone de cada uma
for empresa in dados_empresas:
    razao_social = empresa["razao_social"]
    telefone = encontrar_telefone_empresa(razao_social)
    resultado_empresa = {
        "razao_social": razao_social,
        "telefone": telefone
    }
    telefone_empresas.append(resultado_empresa)

# Criar a pasta de telefone, se não existir
pasta_telefone = os.path.join(os.path.dirname(caminho_principal), '..', 'telefone')
os.makedirs(pasta_telefone, exist_ok=True)

# Salvar os telefone em um arquivo JSON (telefone.json)
with open(caminho_telefone_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(telefone_empresas, arquivo_json, indent=4)

print(f"Arquivo '{caminho_telefone_json}' criado com sucesso.")
