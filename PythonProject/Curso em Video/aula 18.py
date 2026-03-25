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
x = 0
L = []
U = []
while True:
    n = str(input('Digite seu nome(Ou SAIR para finalizar): \n'))
    if n.lower() == 'sair':
        break
    else:
        x +=1
        i = float(input('Digite seu peso: \n'))
        U.append(n)
        U.append(i)
        L.append(U[:])
        U.clear()

lista_pessoa_menor = []
peso_menor = L[0][1]
for pm in L:
    if pm[1] <= peso_menor:
        if pm[1] == peso_menor:
            lista_pessoa_menor.append(pm[0])
        peso_menor = pm[1]
        pessoa_menor = pm[0]
    else:
        continue
lista_pessoa_menor.append(pessoa_menor)

lista_pessoa_maior = []
peso_maior = L[0][1]
for pM in L:
    if pM[1] >= peso_maior:
        if pM[1] == peso_maior:
            lista_pessoa_maior.append(pM[0])
        peso_maior = pM[1]
        pessoa_maior = pM[0]    
    else:
        continue
lista_pessoa_maior.append(pessoa_maior)

print(f'Foram cadastradas {x} pessoas! \n')
print(f'O MAIOR peso foi de {peso_maior}kg. Da pessoa {lista_pessoa_maior}! \n')
print(f'O MENOR peso foi de {peso_menor}kg. Da pessoa {lista_pessoa_menor}! \n')
print('FIM')
