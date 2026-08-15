import csv

alunos_dados = [
    ["Ana Silva", 8.5],
    ["Bruno Souza", 6.0],
    ["Carla Dias", 9.2],
    ["Daniel Lima", 5.5],
    ["Eduarda Rocha", 7.0]
]

with open("alunos.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])
    
    escritor.writerows(alunos_dados)

print("Arquivo 'alunos.csv' criado com sucesso!\n")

print("--- Alunos com bom desempenho (Nota >= 7.0) ---")

with open("alunos.csv", mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)
    
    for linha in leitor:
        nome = linha[0]
        nota = float(linha[1])
        
        if nota >= 7.0:
            print(f"- {nome}: {nota}")