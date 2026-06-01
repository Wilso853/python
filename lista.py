alunos = [{"nome": "wilson", "idade": 17, "sobrenome": "Figueiredo"},
          {"nome": "maria", "idade": 16, "sobrenome": "Joao Filipe"},
          {"nome": "edil", "idade": 18, "sobrenome": "Borges Figueiredo"},
          {"nome": "Rita", "idade": 14, "sobrenome": "Caetano Figueiredo"}]
alunos.append({"nome": "ivane", "idade": 15, "sobrenome": "Caetano Figueirdo"})
alunos.remove({"nome": "maria", "idade": 16, "sobrenome": "Joao Filipe"})
for aluno in alunos:
    print("nome", aluno["nome"])
    print("sobrenome", aluno["sobrenome"])
    print("idade", aluno["idade"])
    print("="*10)