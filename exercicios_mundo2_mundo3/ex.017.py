def funcao():
    # Código pode gerar uma exceção personalizada
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")

# try...except é um bloco de código que permite tratar exceções (erros que ocorrem durante a execução do código). A instrução try tenta executar um bloco de código, e a instrução except é executada se ocorrer uma exceção dentro do bloco try. 

#1. try:
#Este bloco contém o código que pode potencialmente gerar uma exceção. Se a execução #for bem-sucedida, o bloco except é ignorado. 

#2. except:
#Este bloco é executado se uma exceção ocorrer dentro do bloco try. Permite-lhe #definir como quer lidar com a exceção (por exemplo, imprimir uma mensagem de erro, #tentar corrigir o erro ou simplesmente ignorá-lo).

#3. Exceções:
#São erros que ocorrem durante a execução do código, mesmo que este seja #sintaticamente correto. Podem ser causadas por fatores externos (como entrada do #usuário) ou internos (como um cálculo inesperado). 
