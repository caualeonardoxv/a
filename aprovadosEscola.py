
# Abrir o arquivo "Alunos.txt" para leitura (tem que ter um arquivo "pré-pronto" com esse nome e com os nomes dos alunos e as notas dentro)
alunos_e_notas = open("Alunos.txt", "r")

# Criar os arquivos "Aprovados.txt" e "Reprovados.txt" (precisa do "w" para abrir para escrita(ele cria automaticamente o arquivo))
arquivo_aprovados = open("Aprovados.txt", "w")
arquivo_reprovados = open("Reprovados.txt", "w")

for linha in alunos_e_notas:
# Separar o nome e a nota do aluno(a segunda parte tá em float pq a nota pode ser quebrada)
    nome = linha.split(":")[0].strip()
    nota = float(linha.split(":")[1].strip())
# Verificar se o aluno foi aprovado ou reprovado
    if nota >= 7:
        # Escrever o nome do aluno no arquivo de aprovados caso ele passou
        arquivo_aprovados.write(nome + "\n")
    else:
# Escrever o nome do aluno no arquivo de reprovados caso não passar
        arquivo_reprovados.write(nome + "\n")

# Fechar todos os arquivos
alunos_e_notas.close()
arquivo_aprovados.close()
arquivo_reprovados.close()

## não tenho certeza se tá funcionando 100%, mas pela logica era pra estar :D (o meu pc ta meio zuado no aplicativo de programar, ai nn deu pra testar no pc)