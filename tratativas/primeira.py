import os
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote_plus

# Caminho completo para o arquivo principal (tratativa.py)
caminho_principal = os.path.abspath(__file__)

# Caminho completo para o arquivo resultados.json
caminho_resultados_json = os.path.join(os.path.dirname(caminho_principal), '..', 'resultados', 'resultados.json')

# Caminho completo para o arquivo empresas.json
caminho_empresas_json = os.path.join(os.path.dirname(caminho_principal), '..', 'empresas.json')

# Carregar os dados do arquivo JSON (empresas.json)
with open(caminho_empresas_json, 'r', encoding='utf-8') as arquivo_json:
    dados_empresas = json.load(arquivo_json)

# Função para encontrar o site de uma empresa
def encontrar_site_empresa(razao_social):
    query = quote_plus(razao_social) + "+rio+claro+sp"

    link = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    requisicao = requests.get(link, headers=headers)  # requisição GET para obter o conteúdo da página

    if requisicao.status_code == 200:
        site = BeautifulSoup(requisicao.text, "html.parser")  # criar um objeto BeautifulSoup para fazer o parsing do conteúdo HTML

        site_empresa = site.find("cite", class_="apx8Vc tjvcx GvPZzd cHaqb")  # encontrar o elemento <cite> na página

        if site_empresa:
            return site_empresa.get_text()
        else:
            return "Site não encontrado"

    return "Erro na requisição"

# Lista para armazenar os resultados das empresas
resultados_empresas = []

# Iterar pelas empresas e encontrar o site de cada uma
for empresa in dados_empresas:
    razao_social = empresa["razao_social"]
    site = encontrar_site_empresa(razao_social)
    resultado_empresa = {
        "razao_social": razao_social,
        "site": site
    }
    resultados_empresas.append(resultado_empresa)

# Criar a pasta de resultados, se não existir
pasta_resultados = os.path.join(os.path.dirname(caminho_principal), '..', 'resultados')
os.makedirs(pasta_resultados, exist_ok=True)

# Salvar os resultados em um arquivo JSON (resultados.json)
with open(caminho_resultados_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(resultados_empresas, arquivo_json, indent=4)

print(f"Arquivo '{caminho_resultados_json}' criado com sucesso.")
