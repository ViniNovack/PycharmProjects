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
L = []
W = []
Z = []
while True:
    x = int(input('Digite os numeros da primeira lista (Digite 0 para SAIR): \n'))
    if x == 0:
        break
    else:
        L.append(x)
while True:
    y = int(input('Digite os numeros da sugunda lista (Digite 0 para SAIR): \n'))
    if y == 0:
        break
    else:
        W.append(y)
Z.extend(L)
g = 0
while g < len(W):
    if W[g] not in L:
        Z.append(W[g])
        g +=1
    else:
        g +=1
print(f'A listas é {Z}')