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

# EXEMPLO 3
galera = []
dado = []
totmal = 0
tormen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p in galera:
        print(f'{p[0]} é maior de idade! \n')
        totmal +=1
    else:
        print(f'{p[0]} é menor de idade! \n')
        totmen +=1
print(f'Temos {totmal} maior e {totmen} menor de idade! \n')
