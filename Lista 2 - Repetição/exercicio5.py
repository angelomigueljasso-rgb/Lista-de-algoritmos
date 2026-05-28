# Escreva um programa que calcule o fatorial de um número inteiro fornecido 
# pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a 
# multiplicação desse número por todos os seus antecessores até o número 1. 
# Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

num = int(input('Digite um número inteiro: '))
fatorial = 1
if num < 0:
    print('O fatorial não existe para números negativos.')
elif num == 0:
    print('O fatorial de 0 é 1.')
else:
    for i in range(1, num + 1):
        fatorial *= i
    print(f'O fatorial de {num} é {fatorial:,}')