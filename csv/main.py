import csv

### Arquivo .csv ###

# escritor = csv.writer(f) -> Declarando uma varíavel como escritora.
# escritor.writerow(["nome", "idade"]) -> Escrevendo o header do csv
# escritor.writerow(["Ana", "32"]) -> Escrevendo uma linha

with open("dados.csv", "w") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Ana", 32])
    
# leitor = csv.reader(f) -> Declarando uma varíavel como leitora
# for... -> iterando o que está escrito no arquivo

with open("dados.csv", "r") as f:
    leitor = csv.reader(f)
    
    for linha in leitor:
        print(linha)