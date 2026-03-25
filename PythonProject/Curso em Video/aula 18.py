# EXEMPLO 1
# teste = []
# teste.append('Gustavo')
# teste.append(40)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# EXEMPLO 2
# galera = [['João', 19], ['Ana', 33], ['Joaguim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'O/A {p[0]} tem {p[1]} anos de idade! \n')

#EXEMPLO 3
# galera = []
# dado = []
# totmal = 0
# totmen = 0
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
#
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade! \n')
#         totmal +=1
#     else:
#         print(f'{p[0]} é menor de idade! \n')
#         totmen +=1
# print(f'Temos {totmal} maior e {totmen} menor de idade! \n')

#EXERCICIO 84
# x = 0
# L = []
# U = []
# while True:
#     n = str(input('Digite seu nome(Ou SAIR para finalizar): \n'))
#     if n.lower() == 'sair':
#         break
#     else:
#         x +=1
#         i = float(input('Digite seu peso: \n'))
#         U.append(n)
#         U.append(i)
#         L.append(U[:])
#         U.clear()
#
# peso_menor = L[0][1]
# peso_maior = L[0][1]
#
# for p in L:
#     if p[1] < peso_menor:
#         peso_menor = p[1]
#     if p[1] > peso_maior:
#         peso_maior = p[1]
#
# lista_pessoa_menor = []
# lista_pessoa_maior = []
#
# for p in L:
#     if p[1] == peso_menor:
#         lista_pessoa_menor.append(p[0])
#     if p[1] == peso_maior:
#         lista_pessoa_maior.append(p[0])
#
# print(f'Foram cadastradas {x} pessoas! \n')
# print(f'O MAIOR peso foi de {peso_maior}kg. Da pessoa {lista_pessoa_maior}! \n')
# print(f'O MENOR peso foi de {peso_menor}kg. Da pessoa {lista_pessoa_menor}! \n')
# print('FIM')

#EXERCICIO 85
# L = [[], []]
# while True:
#     n = int(input('Digite um valor(ou 0 para SAIR): \n'))
#     if n == 0:
#         break
#     else:
#         if n % 2 == 0:
#             L[0].append(n)
#         else:
#             L[1].append(n)
#
# L[0].sort()
# L[1].sort()
#
# print(f'Os números PARES são {L[0]}')
# print(f'Os números INPARES são {L[1]} \n')

#EXERCICIO 86
M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite o valor de [{l}, {c}] \n'))
        M[l][c] = n
print('=-'*30)
print(f'{M[0]}\n{M[1]}\n{M[2]}')
print('=-'*30)
