sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'FEMININO MASCULINO':
    sexo=str(input('Informação inválida! digite o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} válidado com sucesso.'.format(sexo))




   
    #[0] dentro de um contexto de indexação, como em uma lista ou string, significa que você está acessando o primeiro elemento da sequência. A indexação em Python começa em 0, e não em 1, como em outras linguagens. 

   