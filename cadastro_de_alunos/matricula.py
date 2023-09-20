from opcoes import mostrar_opcoes, cadastrar_aluno, mostrar_alunos, buscar_aluno
import os
import time

from colorama import Fore, Back, Style, init

init(autoreset=True)

while True:
    try:
        os.system("cls")
        mostrar_opcoes()
        opcao = int(input(Fore.YELLOW + "Escolha uma opção: " + Style.RESET_ALL))
        os.system("cls")

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            mostrar_alunos()
        elif opcao == 3:
            buscar_aluno()
        elif opcao == 4:
            print(Fore.BLUE + "Encerrando programa" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Digite uma opção válida" + Style.RESET_ALL)
            time.sleep(2)
    except ValueError:
        os.system("cls")
        print(Fore.RED + "Digite corretamente o que foi pedido" + Style.RESET_ALL)
        time.sleep(3)

