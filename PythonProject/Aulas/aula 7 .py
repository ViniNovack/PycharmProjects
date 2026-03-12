v = float(input('Qual o valor: \n'))
s = float(input('Qual seu sálario: \n'))
a = int(input('Em quantos anos voce quer pagar: \n'))

m = a * 12
p = v / m
x = s * 0.3




if p > x:
    print('Voce não pode pagar a casa por querer pagar e {}'.format(a))
else:
    print('Parabens')