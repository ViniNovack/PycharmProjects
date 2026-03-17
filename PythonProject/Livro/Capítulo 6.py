#EXERCICIO 6.1
# notas = [0, 0, 0, 0, 0, 0, 0]
# x = 0
# y = 0
# soma = 0
# while x <= 6:
#     notas[x] = int(input('Qual foi a nota do aluno: \n'))
#     x += 1
# while y <= 6:
#     soma = soma + notas[y]
#     y += 1
# m = soma / 7
# print(f'A media desse aluno é {m}')

#EXEMPLO 6.7
# numeros = [0, 0, 0, 0, 0]
# x = 0
# while x < 5:
#     numeros[x] = int(input('Digite um numero: \n'))
#     x +=1
# while True:
#     escolhido = int(input('Que posição voce quer imprimir (Digite 0 para sair): \n'))
#     if escolhido == 0:
#         break
#     else:
#         print(f'Voce escolheu o número {(numeros[escolhido - 1])}')

#EXEMPLO 6.15
# L = []
# while True:
#     n = int(input('Digite um número ou digite 0 para SAIR: \n'))
#     if n == 0:
#         break
#     else:
#         L.append(n)
# x = 0
# while x < len(L):
#     print(L[x], end=' ')
#     x +=1

#EXERCICIO 6.2
# L = []
# W = []
# Z = []
# while True:
#     x = int(input('Digite os numeros da primeira lista (Digite 0 para SAIR): \n'))
#     if x == 0:
#         break
#     else:
#         L.append(x)
# while True:
#     y = int(input('Digite os numeros da sugunda lista (Digite 0 para SAIR): \n'))
#     if y == 0:
#         break
#     else:
#         W.append(y)
# Z.extend(L)
# g = 0
# while g < len(W):
#     if W[g] not in L:
#         Z.append(W[g])
#         g +=1
#     else:
#         g +=1
# print(f'A listas é {Z}')

#Listagem 6.23 - Pesquisa sequencial
# L = []
# while True:
#     y = str(input('Quer continuar(Y/N)? \n'))
#     if (y.lower()).strip() == 'n':
#         break
#     else:
#         l = int(input('Digite um numero para montar sua lista: \n'))
#         L.append(l)
# while True:
#     pp = 0
#     p = 0
#     v = 0
#     vv = 0
#     x = 0
#     y = 0
#     n = str(input('Quer achar um numero(Y/N)? \n'))
#     if (n.lower()).strip() == 'n':
#         break
#     else:
#         p = int(input('Qual número voce quer vereficar? \n'))
#         v = int(input('Qual o segundo número que voce quer verificar? \n'))
#         if p in L:
#             while x < len(L):
#                 if L[x] == p:
#                     pp = L[x]
#                     break
#                 else:
#                     x +=1
#             print(f'O valor {p} esta na posição {pp}')
#         if p not in L:
#             print(f'O valor {p} não esta na lista')
#         if v in L:
#             while y < len(L):
#                 if L[y] == v:
#                     vv = L[y]
#                     break
#                 else:
#                     y +=1
#             print(f'O valor {v} esta na lista na posição {vv}')
#         if v not in L:
#             print(f'O valor {v} não esta na lista')
# print('FIM')

#Listagem 6.24
# L = [8, 9, 15]
# for e in L:
#     print(e)

#Listagem 6.27
# for v in range(5, 8):
#     print(v)

# for t in range(3, 33, 3):
#     print(t, end=" - ")
# print()

#Listagem 6.31
# L = [5, 9, 13]
# x = 0
# for e in L:
#     print(f'{x + 1} - {e}')
#     x +=1

# z = 0
# L = [5, 9, 13]
# for x, e in enumerate(L):
#     print(f'{x + 1} - {e}')

#LISTAGEM 6.33
# L = [1, 7, 2, 4]
# maximo = L[0]
# for e in L:
#     if e > maximo:
#         maximo = e
# print(maximo)
# for c in L:
#     if c < m:
#         m = c
# print(f'o menor valor é {m}')

#EXERCICIO 6.7
# L = []
# while True:
#     v = int(input('Adicione um valor a lista (Ou digite 000 para SAIR): \n'))
#     if v == 000:
#         break
#     else:
#         L.append(v)
# while True:
#     d = str(input('Deseja descobrir o maior e menor valor da sua lista (Y/N)? \n'))
#     if (d.strip()).upper() == 'N':
#         break
#     else:
#         M = L[0]
#         for c in L:
#             if c > M:
#                 M = c
#         m = L[0]
#         for g in L:
#             if g < L[0]:
#                 m = g
#     print(f'O maior número é {M} e o menor é {m}')
# print('FIM')