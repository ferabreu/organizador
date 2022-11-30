"""
Programa: Organizador
Modulo: Saida
Requisito: funcoes de saida - mensagens para o usuario.
Autor: Fernando Mees
Data: 28/11/2022
Versao: 2.0
"""

import os

# Cria um ou mais diretorios
def criar_diretorios(diretorios: list):
    dir_atual = os.getcwd()
    for diretorio in diretorios:
        dir_criar = os.path.join(dir_atual, diretorio)
        os.makedirs(dir_criar, exist_ok=True)

# Mensagens de encerramento.
def tela_conclusao():
    print('\n\nOs arquivos foram movidos para as diretorios definidos nas especificacoes.\n')

def tela_encerramento():
    print('\nPrograma encerrado.\n')

def tela_lista_vazia():
    print('\nNão há arquivos para mover.')

# A funcao "progress" foi copiada da URL abaixo.
# https://realpython.com/python-print/#living-it-up-with-cool-animations
# Ela nao e essencial para o programa, e nao contraria
# as especificacoes do projeto. Apenas gera uma barra animada de progresso.
def progress(percent=0, width=63):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)
