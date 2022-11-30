"""
Programa: Organizador
Modulo: Processamento
Requisito: funcoes de processamento - manipulam os dados recebidos
Autor: Fernando Mees
Data: 28/11/2022
Versao: 2.0
"""

import os
import shutil

# Move arquivos para diretorios, classificando por extensao
def classificar_arquivos(dir_arquivos: str, lista_arquivos: list,
                         ext_tipos: list, dir_tipos: list):
    dir_atual = os.getcwd()
    for arquivo in lista_arquivos:
        arquivo_nome, arquivo_ext = os.path.splitext(arquivo)
        arquivo_caminho = os.path.join(dir_arquivos, arquivo)
        if arquivo_ext == '.' + ext_tipos[0]:
            shutil.move(arquivo_caminho, dir_tipos[0])
        elif arquivo_ext == '.' + ext_tipos[1]:
            shutil.move(arquivo_caminho, dir_tipos[1])
        else:
            break
