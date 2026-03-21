#EXEMPLO 1
# num = [2, 5, 9, 1]
# num[2] = 3
# num +=[7]
# num.sort(reverse = True)
# print(num)

#EXEMPLO 2
# valores = []
# valores += [5]
# valores += [9]
# valores.append(4)
# for c, v in enumerate(valores):
#     print(f'Na posição {c + 1} encontrei o valor {v}!')
# print('Cheguei ao final !')

#EXERCICIO 78
# x = 0
# lista = str(input('Digite numeros separados por virgula(,): \n'))
# L = lista.split(',')
# M = int(L[0])
# m = int(L[0])
# while x <= len(L) - 1:
#     z = int(L[x])
#     if z > M:
#         M = z
#         x +=1
#     else:
#         x +=1
# x = 0
# while x <= len(L) - 1:
#     t = int(L[x])
#     if t < m:
#         m = t
#         x +=1
#     else:
#         x +=1
# M = str(M)
# print('As posições', end=' ')
# for r, v in enumerate(L):
#     if v == M:
#         print(f'{r + 1}',end='-')
# print(f'O MAIOR valor é {M}')
# m = str(m)
# print('As posições', end=' ')
# for k, ç in enumerate(L):
#     if ç == m:
#         print(f'{k + 1}', end='-')
# print(f'O MENOR valor é {m}')

#EXERCICIO 79
# L = []
# while True:
#     y = (str(input('Quer digitar numeros? [S/N] \n')).upper()).strip()
#     if y == 'N':
#         break
#     else:
#         n = int(input('Digite um numero: \n'))
#         if n not in L:
#             L.append(n)
#         else:
#             print('Esse valor já existe na lista!')
# L.sort()
# print(f'A sua lista é {L}')

#EXERCICO 80
# L = []
# y = 0
# while True:
#     y = 0
#     n = int(input('Digite um numero: \n'))
#     if n == 0:
#         break
#     elif len(L) == 0 or n > L[-1]:
#         L.append(n)
#         print(L)
#         continue
#     else:
#         while y <= len(L):
#             if n <= L[y]:
#                 L.insert(y, n)
#                 print(L)
#                 break
#             else:
#                 y +=1
#         if n not in L:
#             L.insert(0,n)
#             print(L)
# print(f'FIM, a lista final é {L}')

#EXERCICIO 81
