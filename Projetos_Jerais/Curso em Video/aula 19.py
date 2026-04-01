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
# from datetime import date, datetime
# D = {}
# c = 1
# while True:
#     print('=-'*30)
#     f = str(input('Digite o nome do funcionário (ou "SAIR" para fanalizar o programa): \n'))
#     if (f.lower()).strip() == 'sair':
#         break
#     else:
#         D[f'funcionario {c}'] = f
#         ano = int(input('Digite o seu ano de nacimento: \n'))
#         D['ano de nacimento'] = ano
#         carteira = int(input('Digite o número da sua carteira de trabalho (ou 0 caso não tenha): \n'))
#         if carteira == 0:
#             print('=-'*30)
#             print(f'O funcionário {D[f'funcionario {c}']}\nTem {date.today().year - D['ano de nacimento']} anos\nNão TEM carteira de trabalho')
#             c +=1
#             continue
#         else:
#             D['carteira de trabalho'] = carteira
#             ano_contratação = int(input('Digite o ano de contratação: \n'))
#             D['ano de contratação'] = ano_contratação
#             salario = float(input('Digite seu salário: \n'))
#             D['salario'] = salario
#             print('=-'*30)
#             print(f'O funcionário {D[f'funcionario {c}']}\nTem {date.today().year - D['ano de nacimento']} anos\nSua CTPS tem valor {D['carteira de trabalho']}\nFoi contratado em {D['ano de contratação']}\nSalário é igual a {D['salario']}\nVai se aposentar com {D['ano de contratação'] + 45 - D['ano de nacimento']} anos')
#     D.clear()
# print('=-'*30)
# print('FIM')
# print('=-'*30)

#EXERCICIO 93
# G = []
# D = {}
# while True:
#     print('=-'*30)
#     q = int(input('Digite quantos atlétas voce quer analizar: \n'))
#     for c in range(1, (q + 1)):
#         print('=-'*30)
#         D['nome'] = str(input(f'Digite o nome do atleta {c}º: \n'))
#         partidas = int(input(f'Digite quantas partidas o atleta {D['nome']} jogou: \n'))
       
#         for p in range(1, (partidas + 1)):
#             D[f'PARTIDA {p}'] = int(input(f'Quantos gols o atleta {D['nome']} fez na partida {p}: \n'))
#             G.append(D[f'PARTIDA {p}'])
#         print('=-'*30)
#         print(f'O atleta {D['nome']} jogou {partidas} partidas')
        
#         for k, v in D.items():
#             if k == 'nome':
#                 continue
#             else:
#                 print(f' => Na {k} ele fez {v} gols\n')
#         print(f'Foi um total de {sum(G)} gols em {partidas} partidas')
#         D.clear()
#         G.clear()
#         print('=-'*30)
#     y = str(input('Quer analizar mas jogadores? (Y/N)\n'))
#     if (y.lower()).strip() == 'n':
#         break
#     else:
#         continue
# print('=-'*30)
# print('FIM')
# print('=-'*30)

#EXERCICIO 94
