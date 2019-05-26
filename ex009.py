p1 = int(input('digide o código do produto 1:'))
quan1 = int(input('digite a quantidade do produto 1 desejada:'))
p2 = int(input('digide o código do produto 2:'))
quan2 = int(input('digite a quantidade do produto 2 desejada:'))
p1 = 10*quan1  #observe que aqui eu mudei a atribuição de p1, ele passou a ser 10*quan1. por isso nao somou o valor inicial de p1, que seria o codigo 105
p2 = 20*quan2
valor = p1+p2
print('o valor a pagar é {}'.format(valor))