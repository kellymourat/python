a= input ('Digite algo...' )
print ('Tipo primitivo desse valor: ',type(a))
print ('Valor digitado tem espaço ? ',a.isspace())
print ('Valor digitado é um número ? ',a.isnumeric())
print ('Valor digitado é alphabetic ? ',a.isalpha())
print ('Valor digitado é alphanumeric ? ',a.isalnum())
print ('Valor digitado tem letra minúscula ?',a.islower())
print ('Valor digitado tem letra maiúscula ?',a.isupper())



 # Tipos Primitivos em Detalhe:
 # String: Representa texto, como "Olá, mundo!".
 # Number: Representa números, como 10, 3.14 ou -5.
 # Boolean: Representa valores lógicos, como true ou false.
 # Null: Representa uma ausência de valor.
 # Undefined: Representa um valor que não foi definido.
 # Symbol: Representa um valor único e imutável.
 # BigInt: Representa inteiros de precisão arbitrária.

 # isspace for um espaço em branco, a função retorna um valor diferente de zero      (verdadeiro), caso contrário retorna zero (falso).

 #  isnumeric() é um método de string que verifica se todos os caracteres em uma string são numéricos. Retorna True se todos os caracteres forem numéricos e False caso contrário.

 # isalpha(): Verifica se todos os caracteres da string são letras.

 # isalnum() é um método de string que verifica se todos os caracteres numa string são alfanuméricos (letras ou números)

 # islower() é um método de string que verifica se todos os caracteres de uma string são letras minúsculas. Ele retorna True se todos os caracteres alfabéticos forem minúsculos, e False caso contrário.

 # isupper() é um método de string que retorna True se todos os caracteres em uma string são letras maiúsculas, e False caso contrário.