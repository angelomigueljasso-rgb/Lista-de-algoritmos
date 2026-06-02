# 1. Escreva um laço while para imprimir cada uma das seguintes situações:
# a. Todos os quadrados menores que n. Por exemplo, se n for 100, imprimir 0 1 4 9 16 25 36 49 64 81.
# b. Todos os números positivos que são divisíveis por 10 e menores que n. Por exemplo, se n for 100,
# imprimir 10 20 30 40 50 60 70 80 90.
# c. Todas as potências de dois menores que n. Por exemplo, se n for 100, imprimir 1 2 4 8 16 32 64.
def print_separator():
    print('_' * 30)


print('Exercício n°1 - Lista de revisão')

print('a) Todos os quadrados menores que n.')

n = int(input("Informe o valor de n: "))

i = 0
while i**2 < n:
    print(i ** 2)
    i += 1

print_separator()
print('b) Todos os números positivos que são divisíveis por 10 e menores que n.')

n = int(input("Informe o valor de n: "))

i = 1
while i*10 < n:
    print(i * 10)
    i += 1

print_separator()
print('c) Todas as potências de dois menores que n.')

n = int(input("Informe o valor de n: "))

i = 1
while 2**i < n:
    print(2**i)
    i += 1

print_separator()
