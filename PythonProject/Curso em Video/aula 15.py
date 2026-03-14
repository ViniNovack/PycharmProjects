#EXEMPLO 1:
# cont = 1
# while True:
#     print(cont, '...', end='')
#     cont +=1
#     break
# print('Acabou')

#EXEMPLO 2:
# n = 0
# while n != 999:
#     n = int(input('Digite um número: \n'))

#EXEMPLO 3:
# n = s = 0
# while True:
#     n = int(input('Digite um número: \n'))
#     if n == 0:
#         break
#     s += n
# print(f'A soma vale {s}')

#EXERCICIO 67
# x = 0
# y = 0
# z = 0
# while True:
#     x = 0
#     y = 0
#     n = int(input('Digite o numero que voce quer a tabuada (Ou difite um número negativo para SAIR): \n'))
#     if n < 0:
#         break
#     else:
#         z = int(input('Digite até onde voce quer a tabuada: \n'))
#         while x <= z:
#             y = n * x
#             print(f'{n} X {x} = {y}')
#             x +=1
# print('FIM')

#EXERCICIO 69
# M = 0
# H = 0
# W = 0
# while True:
#     Y = str(input('Voce quer continuar (Y/N)? \n'))
#     if (Y.strip()).lower() == 'n':
#         break
#     else:
#         s = str(input('Qual é o sexo dessa pessoa (M/H)? \n'))
#         i = int(input('Qual é a idade dessa pessoa? \n'))
#         if i > 18:
#             M +=1
#         if (s.strip()).upper() == 'H':
#             H +=1
#         if (s.strip()).upper() == 'M' and i < 20:
#             W +=1
# print(f'{M} são maiores de 18 anos / {H} homens foram cadastrados / {W} mulheres tem menos de 20 anos')

#EXERCICIO 70
# x = 0
# b = str(' ')
# t = 0
# M = 0
# m = 0
# while True:
#     Y = str(input('Voce quer continuar (Y/N)? \n'))
#     if (Y.strip()).upper() == 'N':
#         break
#     else:
#         n = str(input('Qual é o nome do produto? \n'))
#         p = int(input('Qual é o preço desse produto? \n'))
#         t = t + p
#         if p >= 1000:
#             M +=1
#         if x == 0:
#             m = p
#         if p < m:
#             m = p
#             b = n
#         x +=1
# print(f'O total da compra é {t}\n{M} produtos tem um valor acima de 1000 reais\nE o produto mais barato é o {b}')

#EXERCICIO 71
