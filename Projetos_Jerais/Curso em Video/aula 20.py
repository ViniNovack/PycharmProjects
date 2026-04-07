#EXEMPLO 1
# def linha(x):
#     print('=-'*x)

# linha(30)
# print('Olá, mundo!!!')
# linha(20)

#EXEMPLO 2
# def globo(x, y):
#     print('=-'*x)
#     print(y)
#     print('=-'*x)
 

# v = str(input('Escreva uma frse: \n'))
# globo(30, v)

#EXEMPLO 3
# def soma(a, b):
#     s = a + b
#     print(s)


# soma(4, 5) #OU soma(a = 4, b = 5) OU Também posso trocar a ordem: soma(b = 4, a= 5)
# soma(8, 9)
# soma(2, 1)

#EXEMPLO 4
# def contador(*num):
#     l = len(num)
#     print(num, f'Tem {l} elementos')


# contador(2, 1, 7)
# contador(9, 5, 1)

#EXEMPLO 5

# def dobra(lst):
#     for n in lst:
#         x = lst.index(n)
#         lst[x] = n * 2

# L = [1, 2, 3, 4, 5]
# dobra(L)
# print(L)
                      # OU
# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} termos {s}')

#EXEMPLO 6
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos +=1


# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

#EXERCICIO 96
# def area(l, c):
#     a = l * c
#     print(f'A área de um terreno {l} X {c} é de {a}mª')

# while True:
#     A = str(input('Quer continuar (Y/N)? \n'))
#     if (A.lower()).strip() == 'n':
#         break
#     else:
#         l = int(input('Digite a largura do terreno: \n'))
#         c = int(input('Digite o comprimento do terreno: \n'))
#         area(l, c)
# print('FIM')

#EXERCICIO 97
# def centralizar(x):
#     c = len(x)
#     print('='*(c + 4))
#     print(x.center(c + 4))
#     print('='*(c + 4))

# while True:
#     x = str(input('Digite uma frase (ou "SAIR" para finalizar): \n'))
#     if (x.lower()).strip() == 'sair':
#         break
#     else:
#         centralizar(x)
# print('FIM')

# EXERCICIO 98
# import time
# print('=-'*30)
# print('Contagem de 1 até 10 de 1 em 1: ')
# for c in range(1, 11):
#     print(f'{c}')
#     time.sleep(0.5)
# print('FIM')

# print('=-'*30)
# print('Contagem de 10 até 0 de 2 em 2: ')
# for c in range(10, -1, -2):
#     print(f'{c}')
#     time.sleep(0.5)
# print('FIM')
# print('=-'*30)

# print('Agora é sua vez:')
# time.sleep(0.5)
# ini = int(input('Início: \n'))
# fim = int(input('Fim: \n'))
# pas = int(input('Passo: \n'))
# if pas == 0:
#     pas = 1
# pas = abs(pas)
# print('=-'*30)

# if ini < fim:
#     for c in range(ini, (fim + 1), pas):
#         print(f'{c}')
#         time.sleep(0.5)
#     print('FIM')
# if ini > fim:
#     for c in range(ini, (fim - 1), -pas):
#         print(f'{c}')
#         time.sleep(0.5)
#     print('FIM')
# print('=-'*30)

#EXERCICIO 99
# def maior(*num):
#     n = len(num)
#     M = num[0]
#     for c in num:
#         if c > M:
#             M = c
#         else:
#             continue
#     print(f'Os valores digitados foram {num}, possuem {n} elementos e o maior número é {M} \n')

# L = []
# while True:
#     x = str(input('Digite valores (ou "SAIR" para finalizar): \n'))
#     if (x.lower()).strip() == 'sair':
#         break
#     else:
#         L.append(int(x))
# maior(*L)

#EXERCICIO 100
