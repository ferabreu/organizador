"""
Programa: Organizador
Modulo: Entrada
Requisito: funcoes de entrada - fornecem dados ao programa.
Autor: Fernando Mees
Data: 28/11/2022
Versao: 2.0
"""

import os
from time import sleep
import saida

# Retorna a lista de arquivos contidos em um diretorio
def buscar_arquivos(diretorio):
    dir_atual = os.getcwd()
    dir_buscar = os.path.join(dir_atual, diretorio)
    return os.listdir(dir_buscar)

# Tela de abertura.
def tela_intro():
    print('\nCurso de extensao 3782, Turma I:')
    print('"Introdução à Programação em Python para o Controle Externo"')

    print('\nProjeto final de avaliacao do curso de extensao 3782:')
    print('"Programa Organizador"')

    print("""\nEste programa atende estritamente aos requisitos definidos
nas especificacoes propostas para o projeto.""")

    print("""\nPara evitar interferencias indevidas no sistema de arquivos do usuario,
este programa não permite escolher diretorios de entrada e saida.
Os arquivos a serem movidos devem estar no diretorio ./arquivos,
e serao movidos para os diretorios ./planilhas e ./documentos.""")
    
    continuar = input('\nDigite "S" para continuar: ')
    if continuar.lower() != 's':
        saida.tela_encerramento()
        quit()

# Chama a funcao que gera a barra de progresso, definindo o tempo da animacao.
# Oferece a possibilidade de interromper o programa antes das alteracoes
# no sistema de arquivos.
def barra_progresso():
    print('\nPara cancelar, pressione Ctrl+C, Ctrl+Break, Alt+F4...')
    for i in range(101):
        saida.progress(i)
        sleep(0.02)
