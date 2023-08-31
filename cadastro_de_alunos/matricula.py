from opcoes import mostrar_opcoes, cadastrar_aluno, mostrar_alunos, buscar_aluno
import os

while True:
    mostrar_opcoes()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        os.system("cls")
        cadastrar_aluno()
    elif opcao == 2:
        os.system("cls")
        mostrar_alunos()
    elif opcao == 3:
        os.system("cls")
        buscar_aluno()
    elif opcao == 4:
        os.system("cls")
        print("Encerrando programa")
        break
    else:
        os.system("cls")
        print("Digite uma opção válida")