import json
import os


# Caminho completo para o arquivo principal (tratativa.py)
caminho_principal = os.path.abspath(__file__)

# Caminho completo para o arquivo telefones.json
caminho_telefones_json = os.path.join(os.path.dirname(caminho_principal), '..', 'telefones', 'telefone.json')

# Carregar o arquivo JSON de telefones
with open(caminho_telefones_json, 'r', encoding='utf-8') as arquivo_json:
    telefones = json.load(arquivo_json)

# Inicializar contadores
total_telefones_encontrados = 0
total_telefones_nao_encontrados = 0

# Iterar pelos telefones e contar os telefones encontrados e não encontrados
for telefone in telefones:
    if telefone["telefone"] != "telefone não encontrado":
        total_telefones_encontrados += 1
    else:
        total_telefones_nao_encontrados += 1

# Imprimir os telefones
print("Total de telefones encontrados:", total_telefones_encontrados)
print("Total de telefones não encontrados:", total_telefones_nao_encontrados)