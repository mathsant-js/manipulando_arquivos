### Arquivos .txt ###

# with -> gerenciador de contexto. Automatiza configuração e limpeza de recursos
# open -> abre arquivos do computador
# ("dados.txt", "w")
#   dados.txt -> nome do arquivo com extensão (.txt)
#   w -> modo de operação do arquivo. No caso iremos escrever algo. w = write
# as f -> apelidamos o open("dados.txt", "w") com o nome f
# f.write("Olá mundo") -> Olá Mundo é escrito no arquivo

with open("dados.txt", "w") as f:
    f.write("Olá mundo!")

# r -> modo de leitura. r = read
# conteudo = f.read() -> função de leitura para guardar o conteúdo do arquivo na variável conteudo
    
with open("dados.txt", "r") as f:
    conteudo = f.read()

print(conteudo)

with open("dados.txt", "a") as f:
    f.write("a")