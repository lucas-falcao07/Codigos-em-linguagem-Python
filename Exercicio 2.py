print('Bem-vindo a loja de gelados do Lucas Francisco Falcão')
print('--------------------Cardápio---------------------')
print('------|Tamanho | Cupuaçu (CP) | Açaí (AC) |------')
print('------|   P    |   R$ 9,00   |  R$ 11,00  |------')
print('------|   M    |   R$ 14,00  |  R$ 16,00  |------')
print('------|   G    |   R$ 18,00  |  R$ 20,00  |------')
print('-------------------------------------------------')
#Pergunta o sabor e o tamanho
while True:
    sabor = input('Entre com o sabor desejado(CP/AC): ')
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido. Tente novamente')
        continue
    break

while True:
    tamanho = input('Entre com o tamanho desejado(P/M/G): ')
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Tamanho inválido. Tente novamente')
        continue
    break
preco = 0
soma = 0
#Determina o valor com base no sabor e tamanho
if sabor == 'CP':
    if tamanho == 'P':
        preco += 9
        soma += 9
    elif tamanho == 'M':
        preco += 14
        soma += 14
    else:
        preco += 18
        soma += 18
    print('Você pediu um CUPUAÇU no tamanho {}. Custa R${} '.format(tamanho, preco))
else:
    if tamanho == 'P':
        preco += 11
        soma += 11
    elif tamanho == 'M':
        preco += 16
        soma += 16
    else:
        preco += 20
        soma += 20
    print('Você pediu um AÇAÍ no tamanho {}. Custa R${} '.format(tamanho, preco))
#Pergunta se quer pedir mais
pergunta = input('Deseja pedir mais alguma coisa?(S/digite outra tecla): ')
#Se a resposta for 'S', tudo se repete
if pergunta == 'S':
    while True:

        while True:
            sabor = input('Entre com o sabor desejado(CP/AC): ')
            if sabor != 'CP' and sabor != 'AC':
                print('Sabor inválido. Tente novamente')
                continue
            break

        while True:
            tamanho = input('Entre com o tamanho desejado(P/M/G): ')
            if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
                print('Tamanho inválido. Tente novamente')
                continue
            break
        preco = 0

        if sabor == 'CP':
            if tamanho == 'P':
                preco += 9
                soma += 9
            elif tamanho == 'M':
                preco += 14
                soma += 14
            else:
                preco += 18
                soma += 18
            print('Você pediu um CUPUAÇU no tamanho {}. Custa R${} '.format(tamanho, preco))
        else:
            if tamanho == 'P':
                preco += 11
                soma += 11
            elif tamanho == 'M':
                preco += 16
                soma += 16
            else:
                preco += 20
                soma += 20
            print('Você pediu um AÇAÍ no tamanho {}. Custa R${} '.format(tamanho, preco))
        pergunta = input('Deseja pedir mais alguma coisa?(S/digite outra tecla): ')
        if pergunta != 'S':
            break
#Se tudo der certo, o programa irá exibir o valor total do pedido
print('Valor total a ser pago: {}'.format(soma))
