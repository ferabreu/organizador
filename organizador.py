"""
Programa: Organizador
Requisito: Programa que organiza uma lista de arquivos nas pastas
'planilhas' e 'documentos', de acordo com a extensao do arquivo.
Autor: Fernando Mees
Data: 28/11/2022
Versao: 0.1
"""

import entrada
import processamento
import saida

def main():
    # Exibe a tela de abertura
    entrada.tela_intro()
    
    # Diretorio em que estao os arquivos a classificar
    dir_arquivos = 'arquivos'
    # Extensoes a classificar
    ext_tipos = ['docx', 'xlsx']
    # Diretorios de destino
    dir_tipos = ['documentos', 'planilhas']
    
    # Busca os arquivos a classificar
    lista_arquivos = entrada.buscar_arquivos(dir_arquivos)
    
    # Exibe uma barra animada de progresso
    entrada.barra_progresso()
        
    # Cria os diretorios de destino
    saida.criar_diretorios(dir_tipos)
    
    # Move os arquivos para os diretorios, classificando por extensao
    processamento.classificar_arquivos(dir_arquivos, lista_arquivos,
                                       ext_tipos, dir_tipos)
    
    # Exibe as mensagens de encerramento
    saida.tela_conclusao()

if __name__ == "__main__":
    main()

