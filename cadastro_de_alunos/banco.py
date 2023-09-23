import sqlite3
import time
from colorama import Fore, Back, Style, init

init(autoreset=True)

conexao = sqlite3.connect("database.db")

cursor = conexao.cursor()

def iniciar_banco():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_curso TEXT NOT NULL
        );
        '''
    )

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aluno (
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            curso_id INTEGER,
            email TEXT UNIQUE NOT NULL,
            FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
        );
    '''
    )

    conexao.commit()

def cadastrar_curso(nome_curso):
    cursor.execute(f'INSERT INTO cursos(nome_curso) VALUES ("{nome_curso}")')
    conexao.commit()

def cadastrar_aluno(nome, email, curso):
    if verificar_curso(curso):
        cursor.execute(f'INSERT INTO aluno(nome, curso_id, email) VALUES ("{nome}", "{verificar_curso(curso)}", "{email}")')
        conexao.commit()
        print(Fore.GREEN + "Aluno Cadastrado com Sucesso" + Style.RESET_ALL)
        time.sleep(3)
        return
        
    print(Fore.RED + "Não foi possível efetuar o cadastro pois o CURSO informado não existe" + Style.RESET_ALL)
    time.sleep(3)

def listar_alunos():
    cursor.execute("SELECT * FROM aluno")
    alunos = cursor.fetchall()

    for aluno in alunos:
        print(aluno)

def verificar_curso(curso_pretendido):
    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()

    for curso in cursos:
        if curso[1] == curso_pretendido:
            return curso[0]
    
    return False


def fechar_banco():
    conexao.close()
