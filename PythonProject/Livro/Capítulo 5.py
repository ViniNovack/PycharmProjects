#EXEMPLO 1
# fim = int(input('Digite o último número a imprimir: \n'))
# x =0
# while x <= fim:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1

#EXEMPLO 2
# fim = int(input('Digite o Último número a imprimir: \n'))
# x = 0
# while x <= fim:
#     print(x)
#     x = x + 2

#EXERCICIO 5.4
# fim = int(input('Digite o fim: \n'))
# x = 1
# while x <= fim:
#     print(x)
#     x = x + 2

#EXERCICIO 5.5
# fim = int(input('Digite o fim: \n'))
# x = 1
# while x <= fim:
#     if x % 3 == 0:
#         print(x)
#     x = x + 1

#EXERCICIO 5.6
# n = int(input('Tabuada do: \n'))
# x = 1
# while x <= 10:
#     print(2 * x)
#     x = x + 1

#EXERCICIO 5.10
# pontos = 0
# questão = 1
# while questão <= 3:
#     resposta = str(input('Qual é a sua resposta: \n'))
#     if questão == 1 and (resposta.lower()).strip() == 'b':
#         pontos = pontos + 1
#     if questão == 2 and (resposta.lower()).strip() == 'c':
#         pontos = pontos + 1
#     if questão == 3 and (resposta.lower()).strip() == 'd':
#         pontos = pontos + 1
#     questão +=1
# print(f'Você tiro {pontos}')

#EXERCICIO 5.11
# deposito = int(input('Qual foi o deposito inicial: \n'))
# taxa = float(input('Qual a taxa de juros: \n'))
# x = 1
# while x <= 5:
#     extra = int(input('Voce quer depositar mais dinheiro: \n'))
#     deposito = (deposito + extra) * taxa
#     x = x + 1
#     x +=1
# print(f'Voce esta com {deposito}')

#EXEMPLO 5.13
# s = 0
# while True:
#     v = int(input('Digite um número a somer ou 0 para sair: \n'))
#     if v== 0:
#         break
#     s = s + v
# print(s)

#EXERCICÍO 5.14
# s = 0
# q = 0
# while True:
#     numero = int(input('Digite um número ou escreva 0 para encerrar: \n'))
#     if numero == 0:
#         break
#     s = s + numero
#     q = q + 1
#     m = s / q
# print(m)

#EXERCICÍO 5.15
# v = 0
# while True:
#     p = str(input('Digite o código: \n'))
#     if p == '0':
#         break
#     if p == '1' or p == '2' or p == '3' or p == '5' or p == '9':
#         q = int(input('Digite a quantidade: \n'))
#         if p == '1':
#           v = v + (0.5 * q)
#         if p == '2':
#           v = v + (1 * q)
#         if p == '3':
#           v = v + (4 * q)
#         if p == '5':
#           v = v + (7 * q)
#         if p == '9':
#           v = v + (8 * q)
#     else:
#         print('Código invalido')
# print(f'O valor a pagar é {v}')

#EXERCÍCIO 5.23
# x = 1
# y = 0
# while True:
#     x = 1
#     sinal = str(input('Digite um sinal ou escreva sair: \n'))
#     if sinal == '+' or sinal == '-' or sinal == '*' or sinal == '/':
#         numero = int(input('Digite um numero: \n'))
#         if sinal == '+':
#             while x <= 10:
#                 y = x + numero
#                 print(f'{x} + {numero} = {y}')
#                 x = x + 1
#         if sinal == '-':
#             while x <= 10:
#                 y = numero - x
#                 print(f'{numero} - {x} = {y}')
#                 x = x + 1
#         if sinal == '*':
#             while x <= 10:
#                 y = x * numero
#                 print(f'{x} * {numero} = {y}')
#                 x = x + 1
#         if sinal == '/':
#             while x <= 10:
#                 y = numero / x
#                 print(f'{numero} / {x} = {y}')
#                 x = x + 1
#     else:
#         break
# print('Voce saiu')

