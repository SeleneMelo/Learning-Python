nome = str(input('digite o nome do funcionário:'))
horas = int(input('digite o número de horas trabalhadas:'))
preco_hora =  int(input('digite o valor recebido por hora de trabalho:'))
salario = horas*preco_hora
print('o salário do funcionário {} é {}'.format(nome, salario))