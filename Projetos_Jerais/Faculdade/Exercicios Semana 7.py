# EXERCICIO 1
# import time
# x = 0
# for c in range(0, 101):
#     if c % 3 == 0 and c % 5 != 0:
#         print(c)
#         time.sleep(0.5)
#         x +=1
#     else:
#         continue
# print(f'{x} números comprirão as exigencias')

# EXERCICIO 2
# L = []
# r = 0
# while True:
#     n = int(input('Digite um número inteiro: \n'))
#     if n > 0:
#         for c in range(1, (n + 1)):
#             L.append(c)
#             r +=c
#         break
#     else:
#         continue

# n = len(L) - 1
# for c in L:
#     if c == L[n]:
#         print(f' {c} =', end='')
#     else:
#         print(f' {c} +', end='')
# print(f' {r}', end='')

# EXERCICIO 3
# i = int(input('Escreva o primeiro número: \n'))
# f = int(input('Escreva o ultimo número: \n'))
# for c in range(i, (f + 1)):
#     print('=-'*30)
#     for s in range(0, 11):
#         print(f'{s} X {c} = {s * c} \n')

#EXERCICIO 4
# l = int(input('Digite o número de linhas: \n'))
# print('=-'*30)
# for n in range(1, (l + 1)):
#     for i in range(1, (n + 1)):
#         print(f'{i} ', end='')
#     print()
