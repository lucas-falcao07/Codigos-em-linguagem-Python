print('Bem - vindo a loja do Lucas Francisco Falcão, RU: 4540726')
valor_prod = float(input('Entre com o valor do produto: '))
qtd_prod = int(input('Entre com a quantidade do produto: '))
total = valor_prod * qtd_prod
#Aplicação de descontos conforme o valor total
if (2500 <= total < 6000):
    desconto = total * 4 / 100  #4/100 =0,04 * 100 = 4%
    print('Valor total sem desconto {}'.format(total))
    print('Valor total com desconto {} (desconto 4%)'.format(total - desconto))
elif (6000 <= total < 10000):
    desconto = total * 7 / 100  #7/100 =0,07 * 100 = 7%
    print('Valor total sem desconto {}'.format(total))
    print('Valor total com desconto {} (desconto 7%)'.format(total - desconto))
elif (total >= 10000):
    desconto = total * 11 / 100  #11/100 =0,11 * 100 = 11%
    print('Valor total sem desconto {}'.format(total))
    print('Valor total com desconto {} (desconto 11%)'.format(total - desconto))
else:
    desconto = total - 0  #Valor total abaixo de 2500 = sem desconto
    print('Valor total sem desconto {}'.format(total))
    print('Valor total com desconto {}'.format(desconto))
