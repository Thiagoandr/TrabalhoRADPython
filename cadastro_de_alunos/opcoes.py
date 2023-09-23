import time
from colorama import Fore, Back, Style, init
from banco import *

init(autoreset=True)

nome_arquivo = "cadastro_de_alunos/alunos.txt"

def mostrar_opcoes():
    print(Fore.YELLOW + "ESCOLHA UMA DAS OPÇÕES\n" + Style.RESET_ALL)
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sair \n")


def cadastrar():
    print(Fore.YELLOW + "Informe os dados para cadastrar o aluno\n" + Style.RESET_ALL)
    nome = input("Informe o nome do aluno: ")
    curso = input("Informe o curso do aluno: ")
    email = input("Informe o E-Mail do aluno: ")

    for caractere in nome:
        if caractere.isdigit():
            print(Fore.RED + "O Campo NOME não pode possuir números.\n" + Style.RESET_ALL)
            print(Fore.BLUE + "O Cadastro não foi efetuado." + Style.RESET_ALL)
            time.sleep(3)
            return
        
    for caractere in curso:
        if caractere.isdigit():
            print(Fore.RED + "O Campo CURSO não pode possuir números.\n" + Style.RESET_ALL)
            print(Fore.BLUE + "O Cadastro não foi efetuado." + Style.RESET_ALL)
            time.sleep(3)
            return
        
    cadastrar_aluno(nome, email, curso)
    


def mostrar_alunos():
    listar_alunos()
    time.sleep(20)


def buscar_aluno():
    busca = input(Fore.YELLOW + "Informe o aluno a ser buscado: " + Style.RESET_ALL)

    arquivo = open(nome_arquivo, "r")
    alunos = arquivo.readlines()

    encontrou = False

    for aluno in alunos:
        if busca in aluno:
            print(Fore.BLUE + "Aluno encontrado\n" + Style.RESET_ALL)
            print(aluno)
            encontrou = True
        

    if encontrou == False:
        print(Fore.BLUE + "Aluno não encontrado" + Style.RESET_ALL)


    time.sleep(3)