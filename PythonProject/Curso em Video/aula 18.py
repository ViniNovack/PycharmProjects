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
menoryy = []
pen = L[0][1]
for p in L:
    if p[1] >= pen:
        if pen == p[1]:
            menoryy.append(p[0])
        else:
            menor = p [0]
            pen = p[1]

maioryy = []
peM = L[0][1]
for o in L:
    if o[1] <= peM:
        if peM == o[1]:
            maioryy.append(o[0])
        else:
            peM = o[1]
            maior = o[0]

print(f'Foram cadastradas {x} pessoas! \n')
print(f'O MAIOR peso foi de {peM} kg. Peso de {maior, maioryy} \n')
print(f'O MENOR peso foi de {pen} kg. Peso de {menor, menoryy} \n')
print('FIM')
