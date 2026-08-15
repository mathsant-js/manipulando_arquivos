### Arquivos .json ###

import json

dados = {"nome": "Matheus", "idade": 18, "endereco": "Rua Teste, 0"}

# json.dump -> Adiciona informações com um dicionário no arquivo dados.json

with open("dados.json", "w") as f:
    json.dump(dados, f)

# dados_lidos = json.load() -> Carrega as informações do arquivo dados.json

with open("dados.json", "r") as f:
    dados_lidos = json.load(f)
    print(dados_lidos)