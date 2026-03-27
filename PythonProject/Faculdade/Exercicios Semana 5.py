#EXERCICIO 1
# while True:
#     n = int(input('Digite um valor: \n'))
#     if 0 <= n <= 10:
#         print(f'O valor {n} é VALIDO \n')
#         break
#     else:
#         print(f'O valor {n} é INVALIDO')
# print('=-' *30)
# print('FIM')

#EXERCICIO 2
# L = []
# while True:
#     n = str(input('Digite números (digte "sair" parafinalizar o codigi): \n'))
#     if n.lower() == 'sair':
#         break
#     else:
#         L.append(int(n))

# s = str(input('Escolha um sinal entre "+" ou "-" \n'))

# y = L[0]
# x = 0

# if s == '+':
#     for c in L:
#         x = x + c
# elif s == '-':
#     for m in L[1:]:
#         y = y - m

# if s == '+':
#     print(f'O resultado da "+" é {x} \n')
# elif s == '-':
#     print(f'O resultado da "-" é {y} \n')

#EXERCICIO 3
# x = 0
# y = 0
# while True:
#     n = int(input('Digite números(digite "algum número negativo para SAIR"): \n'))
#     if n < 0:
#         break
#     else:
#         x +=1
#         y = y + n
# print(f'A MÉDIA dos valores digitados é {y/x} \n')

#EXERCICIO 4
# x = 1
# p = 0
# i = 0
# P = []
# I = []
# while x <= 10:
#     n = int(input('Digite um número: \n'))
#     if n % 2 == 0:
#         P.append(n)
#         p +=1
#     else:
#         I.append(n)
#         i +=1
#     x +=1
# print(f'O número de números PARES lidos foi de {p} e eles são: {P} \n')
# print(f'O número de números INPARES lidos foi de {i} e eles são: {I} \n')

#EXERCICIO 5
while True:
    s = str(input(' 1: soma\n 2: subtração\n 3: multiplicação\n 4: divisão\n 0: sair\n Escolha uma opção: \n'))
    n1 = int(input('Digite um número: \n'))
    n2 = int(input('Digite o outro número: \n'))
   
    if s == 1:
        print(f'O resultado da some é {n1 + n2} \n')
    elif s == 2:
        print(f'O resultado da subtração é {n1 - n2} \n')
    elif s == 3:
        print(f'O resultado da multiplicação é {n1 * n2} \n')
    elif s == 4:
        if n2 == 0:
            print('Não é possivel dividir por 0 \n')
        else:
            print(f'O resultado da divisão é {n1 / n2} \n')
    elif s == 0:
        print('O programa finalizou \n')
        break
    else:
        print('Opção invalida, tente novamente \n')
