# EXEMPLO 1
# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except (ValueError, TypeError):
#     print('Tivemos um problema com os tipos de dados que você digitou.')
# except (ZeroDivisionError):
#     print('Não é possível dividir um número por zero!')
# except KeyboardInterrupt:
#     print('O usuário preferiu não informar os dados!')
# except Exception as erro:
#     print(f'O erro encontrado foi {erro.__cause__}')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre! Muito obrigado!')

# EXERCICIO 113
# f = 0
# while True:
#     i = str(input('Digite um Inteiro: '))
#     try:
#         i = int(i)
#         while True:
#             try:
#                 f = str(input('Digite um Real: '))
#                 try:
#                     f = float(f)
#                     break
#                 except:
#                     print('ERRO: por favor, digite um número real válido.')
#                     continue
#             except KeyboardInterrupt:
#                 print('O usuario preferiu não digitar o numero Real')
#                 break
#         break
#     except:
#         print('ERRO: por favor, digite um número inteiro válido.')
#         continue
# print(f'O valor inteiro digitado foi {i} e o real foi {f}')

# EXERCICIO 114
# import urllib
# import urllib.request

# try:
#     site = urllib.request.urlopen('http://www.pudim.com.br')
# except urllib.error.URLError:
#     print('O site Pudim não está acessível no momento.')
# else:
#     print('Consegui acessar o site Pudim com sucesso!')
