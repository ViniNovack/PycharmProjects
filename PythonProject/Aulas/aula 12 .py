#EXEMPLO 1
# name = str(input('Whats your name? \n'))
# if name == 'Gustavo':
#     print('Que nome bonito!')
# elif name == 'Pedro' or name == 'pedro:':
#     print('Seu nome é bem popular')
# else:
#     print('Seu noma é bem normal')

#EXERCICIO 36
# casa = int(input('Qual é o valor da casa? \n'))
# salario = int(input('Qual é seu salario? \n'))
# tempo = int(input('Em quanto tempo voce quer pagar a casa? \n'))
# prestaçao = casa / (tempo * 12)
# if prestaçao < (salario * 0.3):
#     print('Parabens!, seu emprestimo foi aprovado')
# else:
#     print('Voce não pode pagar a casa nesse tempo!')

#EXERCICIO 38
# a = int(input('Escreva um numero: \n'))
# b = int(input('Escreva outro numero: \n'))
# c = int(input('Escreva outro numero: \n'))
#
# menor = a
# if b < a and b < c:
#     menor = b
# if c < a and c < b:
#     menor = c
#
# maior = a
# if b > a and b > c:
#     maior = b
# if c > a and c > b:
#     maior = c
#
# print(f'O numero {menor} é o menor')
# print(f'O numero {maior} é o maior')

#EXERCICIO 40
# s = 0
# x = 0
# while True:
#     nota = ((input('Digite quais foram as notas do aluno e quando terminar escreva "pronto": \n')).strip()).lower()
#     if nota != 'pronto':
#         s = s + int(nota)
#         x +=1
#     if str(nota) == 'pronto':
#         break
# m = s / x
# if m < 7:
#     print(f'O aluno ficom com a média {m}, então esta de recuperação')
# elif m == 7:
#     print(f'O aluno ficou com a média {m}, foi quase em')
# else:
#     print(f'O aluno ficou com a média {m}, foi aprovado PARABENS!')