# Lara Dayane da Silva Nascimento, 2°B   -   14/09/23.

def aprovou_(nota): 
    if nota >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"


with open("Alunos.txt", "w") as alunos_arquivo:
    alunos_arquivo.write("marcão, 8.5\n")
    alunos_arquivo.write("pedro, 7.4\n")
    alunos_arquivo.write("gabriel jesus, 9.9\n")
    alunos_arquivo.write("neymar, 10.0\n")
    alunos_arquivo.write("anthony, 9.1\n")
    alunos_arquivo.write("lucaralho, 9.8\n")
    alunos_arquivo.write("arrascaceta, 8.9\n")
    alunos_arquivo.write("luan santana, 4.8\n")
    alunos_arquivo.write("diniz, 3.8\n")
    alunos_arquivo.write("ribamar, 5.0\n")
    alunos_arquivo.write("josue, 6.0\n")
    alunos_arquivo.write("franchesco virgulini, 6.4\n")
    

with open("Alunos.txt", "rt") as arquivo:
  with open("Aprovado.txt", "w") as arquivo_aprovado, open("Reprovado.txt", "w") as arquivo_reprovado:
       #cria os arquivos de aprovado e reprovado
      for linha in arquivo:
              nota = linha.strip().split(",")
              nota =float(nota)
              resultado = aprovou_(nota)
              if resultado == "Aprovado":
                  arquivo_aprovado.write(f"{nome} : {nota}\n")
              else:
                  arquivo_reprovado.write(f"{nome} : {nota}\n")

arquivo_reprovado.close()
arquivo_aprovado.close()

print("Arquivos 'Aprovado.txt' e 'Reprovado.txt' criados")