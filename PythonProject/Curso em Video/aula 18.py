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
    x +=1
    if n.lower() == 'sair':
        break
    else:
        i = float(input('Digite seu peso: \n'))
        U.append(n)
        U.append(i)
        L.append(U[:])
        U.clear()

menor = []
pen = L[0][1]
for p in L:
    if p[1] >= pen:
        if p[1] == pen:
            menor.append(p[0])
        else:
            pen = p[1]
            menor.append(p[0])

maior = []
peM = L[0][1]
for p in L:
    if p[1] <= peM:
        if p[1] == peM:
            maior.append(p[0])
        else:
            peM = p[1]
            maior.append(p[0])

print(f'Foram cadastradas {x} pessoas! \n')
print(f'O MAIOR peso foi de {pen} kg. Peso de {maior} \n')
print(f'O MENOR peso foi de {peM} kg. Peso de {menor} \n')
print('FIM')
