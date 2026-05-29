#Os números primos possuem várias aplicações dentro da Ciência de Dados em 
#criptografia e segurança, por exemplo. Um número primo é aquele que é divisível 
#apenas por um e por ele mesmo. Assim, faça um programa que peça um número 
#inteiro e determine se ele é ou não um número primo.

while True:
    try:
        num = int(input('Digite um número inteiro para verificar se ele é primo ou não: '))
        break
    except ValueError:
        print('Digite apenas números inteiros.')

cont = 0
for i in range(num % i == 0):
    print(f'Seu número {num} é primo')
    cont =+ 1
