from opcoes import mostrar_opcoes, cadastrar_aluno, mostrar_alunos, buscar_aluno
import os
import time

while True:
    try:
        os.system("cls")
        mostrar_opcoes()
        opcao = int(input("Escolha uma opção: "))
        os.system("cls")

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            mostrar_alunos()
        elif opcao == 3:
            buscar_aluno()
        elif opcao == 4:
            print("Encerrando programa")
            break
        else:
            print("Digite uma opção válida")
    except ValueError:
        os.system("cls")
        print("Digite corretamente o que foi pedido")
        time.sleep(3)

