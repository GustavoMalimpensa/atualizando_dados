import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import quote_plus

# Carregar os dados do arquivo JSON
with open('empresas.json', 'r', encoding='xutf-8') as arquivo_json:
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

# Iterar pelas empresas e encontrar o site de cada uma
for i, empresa in enumerate(dados_empresas, start=1):
    razao_social = empresa["razao_social"]
    site = encontrar_site_empresa(razao_social)
    print(f"Empresa {i}: {razao_social} - Site: {site}")
