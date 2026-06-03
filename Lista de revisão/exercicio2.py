#2. Escreva um laço que calcule
#a. A soma de todos os números pares entre 2 e 100 (inclusive).
#b. A soma de todos os quadrados entre 1 e 100 (inclusive).
#c. A soma de todos os números ímpares entre a e b.
#d. A soma de todos os dígitos ímpares de n. (Por exemplo, se n for 32677, a soma deve ser 3 + 7 + 7 = 17).

from a import print_separator
print_separator()

print('Exercício n°2 - Lista de revisão')

print('a) A soma de todos os números pares entre 2 e 100 (inclusive).')

soma = 0
for i in range(2,101,2):
    soma += i

print(soma)

# ou
# soma = 0

# for i in range(2, 101):
#     if i % 2 == 0:
#         soma += i

# print(soma)


print_separator()
print('b) A soma de todos os quadrados entre 1 e 100 (inclusive).')

soma = 0
for i in range(1,101):
    soma += i ** 2

print(soma)

print_separator()
print('c) A soma de todos os números ímpares entre a e b.')
soma = 0

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
