# EXEMPLO 1
# def função():
#     global n1
#     n1 = 4
#     print(f'N1 dentro vale {n1}')


# n1 = 2
# função()
# print(f'N1 fora vale {n1}')

# EXEMPLO 2
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s

# r1 = somar(3, 2, 5)
# r2 = somar(1, 7)
# r3 = somar(4)
# print(f'Meus cálculos deram {r1}, {r2} e {r3}!')

# EXEMPLO 3
# def fatorial(num = 1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f


# x = int(input('Digite um número para calcular seu fatorial: \n'))
# print(f'{fatorial(x)}')

# EXEMPLO 4
# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# num = int(input('Digite um número: \n'))
# if par(num):
#     print('É PAR!')
# else:
#     print('É IMPAR!')

# EXERCICIO 101
# def voto(ano):
#     import datetime
#     atual = datetime.date.today().year
#     idade = atual - ano
#     if idade < 16:
#         return f'Com {idade} anos: NÃO VOTA.'
#     elif 16 <= idade < 18 or idade > 65:
#         return f'Com {idade} anos: VOTO OPCIONAL.'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


# while True:
#     nasc = int(input('Em que ano você nasceu? (ou digite 0 para SAIR)\n'))
#     if nasc == 0:
#         break
#     else:
#         print(voto(nasc))

# print('=-'*30)
# print('FIM')

# EXERCICIO 102
# def fatorial(n, show=False):
#     k = 1
#     for c in range(n, 0, -1):
#         if show == True:
#             k *=c
#             if c > 1:
#                 print(f'{c}', end=' ''X ')
#             elif c == 1:
#                 print(f'{c}', end=' ''= ')
#         else:
#             k *=c
#     print(k, end='')

# fatorial(10, True)

# EXERCICIO 103
# def ficha(nome='<desconhacido>', gols=0):
#     print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

# n = str(input('Nome do Jogador: \n'))
# g = str(input('Número de Gols: \n'))

# if g.isnumeric():
#     g = int(g)
# else:
#     g = 0

# if n.strip() == '':
#     ficha(gols=g)
# else:
#     ficha(n, g)

# EXERCICIO 104
# def leiaInt():
#     while True:
#         m = str(input('Digite um número: '))
#         if m.isnumeric():
#             m = int(m)
#             return m
#             break
#         else:
#             print('ERRO! Digite um número inteiro válido.')
#             continue

# n = leiaInt()
# print(f'Você digitou o número {n}!!!')

# EXERCICIO 105
# def notas(*n, sit=False):
#     D = {}
#     mm = 0
#     me = n[0]
#     med = 0
#     cont = 0
#     s = 0

#     for c in n:
#         if c > mm:
#             mm = c
#         elif c < me:
#             me = c
#     for c in n:
#         s +=c
#         cont +=1
#     med = s / cont

#     D['TOTAL'] = cont
#     D['MAIOR'] = mm
#     D['MENOR'] = me
#     D['MÉDIA'] = med

#     if sit == True:
#         if med < 7:
#             D['Situação'] = 'Ruim'
#         elif 7 <= med < 8:
#             D['Situação'] = 'Médio'
#         elif med >= 8:
#             D['Situação'] = 'Boa'
    
#     return D

# n = notas(7, 8, 8, 9, 6, 5, 8, 7, 7, 10, sit=True)
# print(n)

# EXERCICIO 106
# from time import sleep

# FUNDO_BRANCO = "\033[47m"
# FUNDO_AZUL = "\033[44m"
# FUNDO_VERDE = "\033[42m"
# TEXTO_PRETO = "\033[30m"
# LIMPA_LINHA = "\033[K"
# RESET = "\033[0m"
# SEM_CORES = '\033[m',

# print(f'{FUNDO_VERDE}{TEXTO_PRETO}~{LIMPA_LINHA}{RESET}'*50)
# print(f'{FUNDO_VERDE}{TEXTO_PRETO}           SISTEMA DE AJUDA PyHELP{LIMPA_LINHA}{RESET}')
# print(f'{FUNDO_VERDE}{TEXTO_PRETO}~{LIMPA_LINHA}{RESET}'*50)
# sleep(0.5)

# while True:
#     f = str(input('Função ou Biblioteca > '))
#     if (f.lower()).strip() == 'sair':
#         break
#     else:
#         print(f'{FUNDO_AZUL}{TEXTO_PRETO}~{LIMPA_LINHA}{RESET}'*50)
#         print(f'{FUNDO_AZUL}{TEXTO_PRETO}           Acessando o Manual do comando{LIMPA_LINHA}{RESET}')
#         print(f'{FUNDO_AZUL}{TEXTO_PRETO}~{LIMPA_LINHA}{RESET}'*50)
#         sleep(0.5)
#         print(f'{FUNDO_BRANCO}{TEXTO_PRETO}{LIMPA_LINHA}')
#         help(f)
#         print(f'{RESET}')
#         continue

# print('=-'*30)
# print('FIM')
