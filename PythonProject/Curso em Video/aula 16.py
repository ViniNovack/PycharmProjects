#EXEMPLO 1
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#
# # for cont in range(0, len(lanche)):
# #     print(lanche[cont])
#
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos + 1}')
#
# print('Comi muito')

#EXEMPLO 2
# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#
# print(sorted(lanche))
# print(lanche)

#EXEMPLO 3
# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c.count(5))

#EXEMPLO 4
# L = ['Gustavo', 39, 9.9]
# del L[0]
# print(L)

#EXERCICIO 72
# L = ['Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nova', 'Dez', 'Onse', 'Dose', 'Trese', 'Catorse', 'Quinse', 'Deseseis', 'Dezesete', 'Desoito', 'Desenove', 'Vinte']
# while True:
#     n = int(input('Digite um número de 0 a 20 (Ou um número negativo para SAIR): \n'))
#     if n < 0:
#         break
#     if n > 20:
#         print('Tente novamente!')
#         continue
#     else:
#         print(f'O número que voce digitou é {L[n]}')
# print('FIM')

#EXERCICIO 73
# T = []
# while True:
#     c = str(input('Ainda tem mais times(Y/N)? \n'))
#     if (c.strip()).upper() == 'N':
#         break
#     else:
#         times: str = input('Digite os times em ordem de casificação: \n')
#         T.append(times)
# a = int(input('Voce quer ver até qual colocado? \n'))
# u = int(input('Voce quer ver até quantos ultimos colocados? \n'))
# o = str(input('Voce quer ver os times que estão partisipando do campeonato em ordem alfabetica(Y/N)? \n'))
# p = str(input('Qual time voce quer ver a clasificação? \n'))
#
# if (o.strip()).upper() == 'Y':
#     print(f'Os times competindo são {sorted(T)}')
#
# print(f'Os primeiros colocados são {T[0:a]}')
# print(f'Os ultimos colocados são {T[-u:]}')
# print(f'A posição do time {p} é {T.index(p) + 1}')


v = str(input('Digite times, mas por favor de espaços entre eles: \n'))
v.list()
print(v[1])