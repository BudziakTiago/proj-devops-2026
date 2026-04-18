import json

def menu():
    print('\n------Menu------')
    print('1. Estudantes')
    print('2. Disciplinas')
    print('3. Professores')
    print('4. Turmas')
    print('5. Matrículas')
    print('6. Sair')
    print('----------------\n')

def menu_op():
    print('1. Incluir')
    print('2. Listar')
    print('3. Atualizar')
    print('4. Excluir')
    print('5. Voltar ao Menu Principal')
    print('-------------------------------------\n')

menu_opcoes = ['', 
'-- Menu de Operações - Estudantes ---', 
'-- Menu de Operações - Disciplinas --', 
'-- Menu de Operações - Professores --', 
'---- Menu de Operações - Turmas -----', 
'-- Menu de Operações - Matrículas ---']

alunos = []

def incluir():
    dados = recuperar_arquivo()

    id = int(input("Digite o ID do aluno: "))
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")

    aluno = {'id':id, 'nome':nome, 'cpf':cpf}
    
    if dados:
        dados.append(aluno)

        with open("aluno.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False)
    else:
        alunos.append(aluno)

        with open("aluno.json", "w", encoding="utf-8") as arquivo:
            json.dump(alunos, arquivo, ensure_ascii=False)

def listar():
    dados = recuperar_arquivo()

    if dados:
        for i in range(len(dados)):
            print(f"- {dados[i]}")
    else:
        print("Nenhum aluno cadastrado")        

def editar():
    editado = False
    dados = recuperar_arquivo()
                
    if dados:
        codigo = int(input("Digite o ID do aluno a ser editado: "))

        for i in range(len(dados)):
            if dados[i]['id'] == codigo: 

                dados[i]['id'] = int(input("Digite o novo ID do aluno: "))
                dados[i]['nome'] = input("Digite o novo nome do aluno: ")
                dados[i]['cpf'] = input("Digite o novo CPF do aluno: ")

                with open("aluno.json", "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, ensure_ascii=False)

                print("Aluno editado com sucesso!")
                editado = True

        if editado != True: 
            print("Nenhum aluno cadastrado com este ID")
    else:
        print("\nNenhum aluno cadastrado")

def excluir():
    excluido = False
    dados = recuperar_arquivo()

    if dados:
        codigo = int(input("Digite o ID do aluno a ser excluído: "))

        for i in range(len(dados)): 
            if dados[i]['id'] == codigo:
                print(f"Aluno {dados[i]} excluído com sucesso!")
                dados.pop(i)

                with open("aluno.json", "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, ensure_ascii=False)

                break

        if excluido != True:
            print("\nNenhum aluno cadastrado com o ID indicado")
    else:
        print("\nNenhum aluno cadastrado")

def recuperar_arquivo():
    try:
        with open("aluno.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    except:
        dados = []
        return dados  

while True: 
    menu() # Mostra o menu

    try: 
        opcao = int(input("Digite a opção desejada: "))
    except:
        print("\nOpção Inválida")
        continue

    if opcao < 1 or opcao > 6:
        print("\nOpção Inválida")

    elif opcao == 6:
        print("Saindo...\n")
        break

    elif opcao == 2 or opcao == 3 or opcao == 4 or opcao == 5:
        print(menu_opcoes[opcao])
        print("--------- EM DESENVOLVIMENTO --------")
        print("-------------------------------------")

    elif opcao == 1:
        while True:
            print(f"\n{menu_opcoes[opcao]}")
            menu_op() # Mostra o menu de operações

            try: 
                opcao_op = int(input("Digite a opção desejada: "))
            except:
                print("\nOpção Inválida")
                continue

            if opcao_op < 1 or opcao_op > 5:
                print("\nOpção Inválida")

            elif opcao_op == 1: # Inclusão     
                print("\n--- Opcão - Inclusão ----")    
                incluir()
                input("Aperte ENTER para continuar")

            elif opcao_op == 2: # Listagem
                print("\n--- Opcão - Listagem ----")  
                listar()
                input("Aperte ENTER para continuar")

            elif opcao_op == 3: # Edição
                print("\n-- Opcão - Atualização -")  
                editar()
                input("Aperte ENTER para continuar")                                

            elif opcao_op == 4: # Exclusão
                print("\n--- Opcão - Exclusão ---")  
                excluir()
                input("Aperte ENTER para continuar")

            elif opcao_op == 5:
                break