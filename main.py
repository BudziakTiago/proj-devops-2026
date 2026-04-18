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

menu_op_opcoes = ['', 
'--- Opcão - Inclusão ----', 
'--- Opcão - Listagem ----', 
'-- Opcão - Atualização -', 
'--- Opcão - Exclusão ---']

alunos = []

def incluir(id, name, cpf):
    aluno = {'id':id, 'name':name, 'cpf':cpf}
    alunos.append(aluno)

def listar():
    if alunos:
        for i in range(len(alunos)):
            print(f"- {alunos[i]}")
    else:
        print("Nenhum aluno cadastrado")

def editar(i, id, name, cpf):
    alunos[i]['id'] = id
    alunos[i]['name'] = name
    alunos[i]['cpf'] = cpf
    print("Aluno editado com sucesso!")

def excluir(i):
    print(f"Aluno {alunos[i]} excluído com sucesso!")
    alunos.pop(i)

while True: 
    menu() # Mostra o menu

    try: 
        opcao = int(input("Digite a opção desejada: "))

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

                    if opcao_op < 1 or opcao_op > 5:
                        print("\nOpção Inválida")

                    elif opcao_op == 5:
                        break

                    elif opcao_op == 1: # Inclusão
                        print(f"\n{menu_op_opcoes[opcao_op]}")
                        
                        id = int(input("Digite o ID do aluno: "))
                        name = input("Digite o nome do aluno: ")
                        cpf = input("Digite o CPF do aluno: ")

                        incluir(id, name, cpf)

                        input("Aperte ENTER para continuar")

                    elif opcao_op == 2: # Listagem
                        print(f"\n{menu_op_opcoes[opcao_op]}")

                        listar()

                        input("Aperte ENTER para continuar")

                    elif opcao_op == 3: # Edição
                        editado = False

                        print(f"\n{menu_op_opcoes[opcao_op]}")

                        codigo = int(input("Digite o ID do aluno a ser editado: "))

                        for i in range(len(alunos)):
                            if alunos[i]['id'] == codigo: 

                                new_id = int(input("Digite o novo ID do aluno: "))
                                new_name = input("Digite o novo nome do aluno: ")
                                new_cpf = input("Digite o novo CPF do aluno: ")

                                editar(i, new_id, new_name, new_cpf)
                                
                                editado = True

                        if editado != True: 
                            print("Nenhum aluno cadastrado com este ID")

                        input("Aperte ENTER para continuar")

                    elif opcao_op == 4: # Exclusão
                        excluido = False

                        if alunos:
                            print(f"\n{menu_op_opcoes[opcao_op]}")

                            codigo = int(input("Digite o ID do aluno a ser excluído: "))
                            
                            for i in range(len(alunos)):
                                if alunos[i]['id'] == codigo: 
                                    excluir(i)
                                    excluido = True

                            if excluido != True: 
                                print("Nenhum aluno cadastrado com este ID")
                                    
                            input("Aperte ENTER para continuar")
                        else:
                            print("\nNenhum aluno cadastrado")

                except:
                    print("\nOpção Inválida")

    except:
        print("\nOpção Inválida")