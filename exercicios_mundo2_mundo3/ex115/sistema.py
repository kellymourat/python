from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
   criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'sair do sistema'])
    if resposta == 1:
         lerArquivo(arq)                                            # opção de listar o conteudo de um arquivo
    elif resposta ==2:                                             # opção para cadastrar pessoas
        cabeçalho('NOVO CADASTRO!')
        nome=str(input('Nome: '))
        idade= leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho(f'Saindo do sistema... Até logo!')
        break
    else:
        print('\033[0:31mErro! Digite uma opção válida! \033[m')
    sleep(0.5)