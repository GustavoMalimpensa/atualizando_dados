import json
import os


# Caminho completo para o arquivo principal (tratativa.py)
caminho_principal = os.path.abspath(__file__)

# Caminho completo para o arquivo resultados.json
caminho_resultados_json = os.path.join(os.path.dirname(caminho_principal), '..', 'resultados', 'resultados.json')


# Carregar o arquivo JSON de resultados
with open(caminho_resultados_json, 'r', encoding='utf-8') as arquivo_json:
    resultados = json.load(arquivo_json)

# Inicializar contadores
total_sites_encontrados = 0
total_sites_nao_encontrados = 0

# Iterar pelos resultados e contar os sites encontrados e não encontrados
for resultado in resultados:
    if resultado["email"] != "Email não encontrado":
        total_sites_encontrados += 1
    else:
        total_sites_nao_encontrados += 1

# Imprimir os resultados
print("Total de sites encontrados:", total_sites_encontrados)
print("Total de sites não encontrados:", total_sites_nao_encontrados)