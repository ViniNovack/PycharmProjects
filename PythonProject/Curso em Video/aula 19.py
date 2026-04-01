#EXEMPLO 1
# dados = {}
# dados = {'nome': 'Pedro', 'idade': 25}
# dados ['sexo'] = 'M'
# print(dados['sexo'])

#EXEMPLO 2
# filme = {'titulo': 'star wars', 'ano': 1977, 'diretor': 'George Lucas'}
# print(filme.values())
# print(filme.keys())
# print(filme.items())
# for k, v in filme.items():
#     print(f'O {k} é {v}')

#EXEMPLO 3
# filme1 = {'titulo': 'star wars', 'ano': '1977', 'diretor': 'George Lucas'}
# filme2 = {'titulo': 'avengers', 'ano': '2012', 'diretor': 'Joss Whedon'}
# filme3 = {'titulo': 'matrix', 'ano': '1999', 'diretor': 'Wachowski'}
# locadora = [filme1, filme2, filme3]
# print(locadora[0]['titulo'])

#EXEMPLO 4
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])
# print(brasil[1]['uf'])

#EXEMPLO 5
# estado = {}
# brasil = []
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: \n'))
#     estado['sigla'] = str(input('Sigla do Estado: \n'))
#     brasil.append(estado.copy())
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()

#___________________________________________________________________________________________________________________________________________________________
#EXERCICIO 90
# D = {}
# while True:
#     D.clear()
#     n = str(input('Digite o nome do aluno (ou "SAIR" para finalizar o programa): \n'))
#     if (n.lower()).strip() == 'sair':
#         break
#     else:
#         D['nome'] = n
#         m = float(input('Digite a média do aluno: \n'))
#         D['media'] = m
#         if m < 7:
#             D['situação'] = 'VOCE ESTA DE RECUPERAÇÃO'
#         elif m == 7:
#             D['situação'] = 'FOI QUASE EM, MAS VOCE ESTA APROVADO'
#         else:
#             D['situação'] = 'PARABENS, voce foi APROVADO'
#         print('=-'*30)
#         print(f'O aluno {D['nome']}\nMédia é igual a {D['media']}\nSituação do aluno é: {D['situação']}')
# print('=-'*30)
# print('FIM')

#EXERCICIO 91
# import random
# U = []
# L = []
# D = {}
# CR = 1
# CJ = 1
# p = 1
# while True:
#     print('=-'*30)
#     print(F'RODADA {CR}')
#     print('=-'*30)
#     while CJ <= 4:
#         D[f'jogador {CJ}'] = str(input(f'Digite "Y" para girar o dado: \n'))
#         if (D[f'jogador {CJ}'].lower()).strip() == 'y':
#             D[f'jogador {CJ}'] = random.randrange(1, 7)
#             print(f'O jogador {CJ} tirou {D[f'jogador {CJ}']}')
#             CJ +=1
#         else:
#             print('=-'*30)
#             print('TENTE DE NOVO')
#             print('=-'*30)
#             continue
#     for k, v in D.items():
#         U.append(v)
#         U.append(k)
#         L.append(U[:])
#         U.clear()
#     L.sort(reverse=True)
#     print('=-'*30)
#     for i in L:
#         print(f'{p}º Lugar: {i[1]} fez {i[0]} pontos')
#         p +=1 
#     print('=-'*30)
#     r = str(input('Quer jogar mais uma rodade? (Y/N) \n'))
#     print('=-'*30)
#     if (r.lower()).strip() == 'y':
#         CR +=1
#         CJ = 1
#         p = 1
#         D.clear()
#         L.clear()
#         continue
#     else:
#         break
# print('FIM')

#EXERCICIO 92
