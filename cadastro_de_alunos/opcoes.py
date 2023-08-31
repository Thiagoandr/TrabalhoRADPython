import time

nome_arquivo = "cadastro_de_alunos/alunos.txt"

def mostrar_opcoes():
    print("ESCOLHA UMA DAS OPÇÕES\n")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar aluno")
    print("4 - Sair")


def cadastrar_aluno():
    nome = input("Informe o nome do aluno: ")
    curso = input("Informe o curso do aluno: ")
    email = input("Informe o E-Mail do aluno: ")

    aluno = f"Nome: {nome} | E-Mail: {email} | Curso: {curso}\n"

    arquivo = open(nome_arquivo, "a")
    arquivo.write(aluno)
    arquivo.close()

def mostrar_alunos():
    arquivo = open(nome_arquivo, "r")
    alunos = arquivo.readlines()
    
    for aluno in alunos:
        print(aluno)

    time.sleep(3)


def buscar_aluno():
    busca = input("Informe o aluno a ser buscado: ")

    arquivo = open(nome_arquivo, "r")
    alunos = arquivo.readlines()

    encontrou = False

    for aluno in alunos:
        if busca in aluno:
            print("Aluno encontrado\n")
            print(aluno)
            encontrou = True
        

    if encontrou == False:
        print("Aluno não encontrado")


    time.sleep(3)