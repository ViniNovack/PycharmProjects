#EXEMPLO 1
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#
# # for cont in range(0, len(lanche)):
# #     print(lanche[cont])
#
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos + 1}')
#
# print('Comi muito')

#EXEMPLO 2
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#
# print(sorted(lanche))
# print(lanche)

#EXEMPLO 3
# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c.count(5))

#EXEMPLO 4
# L = ['Gustavo', 39, 9.9]
# del L[0]
# print(L)

#EXERCICIO 72
# L = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nova', 'Dez', 'Onse', 'Dose', 'Trese', 'Catorse', 'Quinse', 'Deseseis', 'Dezesete', 'Desoito', 'Desenove', 'Vinte']
# while True:
#     n = int(input('Digite um número de 0 a 20 (Ou um número negativo para SAIR): \n'))
#     if n < 0:
#         break
#     if n > 20:
#         print('Tente novamente!')
#         continue
#     else:
#         print(f'O número que voce digitou é {L[n]}')
# print('FIM')

#EXERCICIO 73
# while True:
#     times = str(input('Escreva o nome dos times desejados em ordem separados com virgula(,): \n'))
#     c = str(input('Ainda tem mais times(Y/N)? \n'))
#     if (c.strip()).upper() == 'N':
#         break
#     else:
#         print('Quando for adicionar o nome time por favor reescreva todos os outros: \n')
#         continue
# T = times.split(',')
# a = int(input('Voce quer ver até qual colocado? \n'))
# u = int(input('Voce quer ver até quantos ultimos colocados? \n'))
# o = str(input('Voce quer ver os times que estão partisipando do campeonato em ordem alfabetica(Y/N)? \n'))
# p = str(input('Qual time voce quer ver a clasificação? \n'))
#
# if (o.strip()).upper() == 'Y':
#     print(f'Os times competindo são {sorted(T)}')
#
# P = T[0:a]
# for x, e in enumerate(P):
#     print(f'Os primeiros colocados são {x + 1} - {e}')
#
# print(f'Os ultimos colocados são {T[-u:]}')
#
# print(f'A posição do time {p} é {T.index(p) + 1}')

#EXERCICIO 74
# import random
# L = []
# x = 0
# z = 0
# while x <= 5:
#     a = random.randrange(1, 101)
#     L.append(a)
#     x +=1
# print(L)
# M = L[0]
# m = L[0]
# y = 0
# while y <= (len(L) - 1):
#     if M < L[y]:
#         M = L[y]
#         y +=1
#     else:
#         y +=1
# while z <= (len(L) - 1):
#     if L[z] < m:
#         m = L[z]
#         z +=1
#     else:
#         z+=1
# print(f'O maior número é {M} e o menor é {m}')

#EXERCICIO 75
# x = 0
# P = []
# lista = str(input('Escreva uma sequencia numerica separando a por virgula(,): \n'))
# L = lista.split(',')
# if '9' in L:
#     print(f'O 9 apareceu {L.count('9')} vezes')
# else:
#     print('O 9 nao foi digitado')
# if '3' in L:
#     print(f'O primeiro 3 esta em {L.index('3') + 1}')
# else:
#     print('O 3 nao foi digitado')
# while x <= (len(L) - 1):
#     n = int(L[x]) % 2
#     if n == 0:
#         P.append(L[x])
#         x +=1
#     else:
#         x +=1
# print(f'Os valores pares digitados foram: {P}')

#EXERCICIO 76
# listagem = ('Lápis', 1.75,
#             'Borracha', 2,
#             'Caderno', 15.90,
#             'Estojo', 25)
# print('-' * 40)
# print(f'{"Listagem de Produtos":^40}')
# print('_' * 40)
# for pos in range(0, len(listagem)):
#     if pos % 2 == 0:
#         print(f'{listagem[pos]:.<30}', end='')
#     else:
#         print(f'R${listagem[pos]:7.2f}')
# print('-' * 40)

#EXERCICIO 77
# x = 0
# Z = 0
# y = 0
# V = []
# lista = str(input('Digite palavras separando as por virgulas(,): \n'))
# L = lista.split(',')
# while x <= (len(L) - 1):
#     Z = list(L[x])
#     del V[:]
#     y = 0
#     while y <= (len(Z) - 1):
#         if Z[y] == 'a' or Z[y] == 'e' or Z[y] == 'i' or Z[y] == 'o' or Z[y] == 'u':
#             V.append(Z[y])
#             y +=1
#         else:
#             y +=1
#     print(f'A palavra: {L[x]}, tem as vogais: {V}')
#     x +=1
# print('FIM')