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

#