#Questão 01

num = int(input("Digite um número para saber seu fatorial: "))

c = num
f = 1
while c > 0:
    print(f"{c}", end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f"{f}.")
