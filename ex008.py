nome = str(input('digite o nome do funcionário:'))
salario_fixo = int(input('digite o salário fixo do(a) funcionário(a) {}:'.format(nome)))
vendas = float(input('digite o valor das vendas mensais:'))
salario = salario_fixo+0.15*vendas
print('o valor do salário total do(a) funcionário(a) {} é {}'.format(nome, salario))

