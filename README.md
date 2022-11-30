# Organizador
Projeto final de avaliacao do *Curso de Introdução a Programação com Python para Controle Externo*, ministrado pelo Prof. Nelson S. dos Santos em novembro de 2022, através da plataforma de aprendizagem remota da Universidade Federal do Rio Grande do Sul.

Este programa, elaborado pelo aluno **Fernando Mees Abreu**, atende às especificações propostas para o projeto, nos termos do arquivo *ProjetoFinal.pdf*, incluído neste repositório.

Resumidamente, as especificações determinam que:
- O programa deve ler o conteúdo de um diretório contendo uma lista predefinida de arquivos (*DespesasCorrentes.xlsx, DespesasCorrentes.docx, DespesasCapital.xlsx, DespesasCapital.docx, relatorio.docx*).
  - Não foi especificado qual o diretório, nem se o programa deve permitir a seleção de um diretório pelo usuário. Para evitar incursões indevidas em sistemas de arquivos alheios, fixou-se, no programa, o diretório "arquivos", no mesmo caminho do programa, conforme organizado neste repositório.
- O programa deve identificar a extensão de cada um dos arquivos.
- O programa deve mover os arquivos com extensão *docx* para o diretório *documentos*, e os com extensão *xlsx*, para o diretório *planilhas*.
  - Os diretórios indicados foram considerados caminhos relativos à localização dos arquivos do programa. Portanto, os arquivos serão movidos de `./arquivos` para `./documentos` e `./planilhas`.
- O programa deve ser procedural e modularizado: suas funções devem ser separadas em arquivos, conforme um critério de classificação que seja claro para o avaliador.
- O programa deve utilizar os módulos [os — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html) e [shutil — High-level file operations](https://docs.python.org/3/library/shutil.html).

Não foi feita qualquer especificação adicional quanto à interface ou diálogos do programa, interação com o usuário, ou tratamento de exceções. O programa irá, contudo, verificar se o diretório *arquivos* contém algum arquivo classificável, e, em caso negativo, encerrará "graciosamente".

Não foram feitas especificações quanto à compatibilidade com sistemas operacionais ou sistemas de arquivos específicos, nem com versões específicas do interpretador Python e seus componentes. O programa foi elaborado usando *Python 3.9.13 (Anaconda)*, em ambiente Linux. Em princípio, as funções usadas na criação dos caminhos (para diretórios e arquivos) usados pelo programa devem torná-lo compatível também com Windows e MacOS.

Como a tarefa é bastante simples, foram incluídos alguns diálogos com o usuário - até para viabilizar melhor a modularização.

Para fins de modularização, optou-se pela classificação básica de módulos proposta em aula, de acordo com os seguintes critérios:
- Entrada: funções que, preponderantemente, "tragam informações" para o programa.
  - Busca de arquivos: traz uma lista de arquivos para o programa classificar.
  - Exibição da tela de abertura: recebe a confirmação do usuário de que deseja executar o programa (tecla "S").
  - Exibição da barra de progresso: recebe o sinal de interrupção do programa, caso o usuário decida pela interrupção.
    - Estas duas últimas funções produzem saída de informação para a interface. Optou-se, contudo, por atribuir mais importância às entradas de dados que determinam o curso de execução do programa.
- Processamento: funções que manipulem informações da entrada, podendo encaminhá-las para saída, ou não.
  - Classificação de arquivos: identifica as extensões dos nomes dos arquivos de uma lista, e move cada arquivo para o diretório correto.
    - É claro que esta função também gera uma "saída" de informação. A maior parte do trabalho dela, contudo, se enquadra na classificação de "processamento".
- Saída: funções que "produzam informações".
  - Criação de diretórios.
  - Exibição de diálogos e itens da interface.

Para executar o programa, baixe o conteúdo deste repositório para um diretório em seu computador, e execute `python organizador.py`, ou o comando equivalente para o seu ambiente.
