# EXERCICIO 1
# import time
# for c in range(0, 11):
#     print(c)
#     time.sleep(0.5)
# print()
# for i in range(10, -1, -1):
#     print(i)
#     time.sleep(0.5)

# EXERCICIO 2
# import time
# for c in range(0, 11):
#     if c % 2 == 0:
#         print(f'O número {c} é PAR')
#         time.sleep(0.5)
#     elif c == 0:
#         print(f'O número {c} é NEUTRO')
#     else:
#         print(f'O número {c} é ÍMPAR')
#         time.sleep(0.5)

#EXERCICIO 3
# import time
# while True:
#     p = str(input('Digite uma palavra que comece com uma vogal (ou digite "SAIR"): \n'))
#     if p.lower() == 'sair':
#         break
#     else:
#         for c in p:
#             if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
#                 print(f'A palavra: {p} É VALIDA')
#                 for i in p:
#                     print(i)
#                     time.sleep(0.5)
#                 break
#             else:
#                 print(f'A palavra: {p} É INVALIDA')
#                 break
