# Função para escolher o serviço

"""
    escolha de serviço:
     primeiro é perguntado o estilo de serviço que o usuário deseja.
     cada 'if' usado tem o nome do serviço e o preço pré-definido que será salvo na variável 'preco'.
     'preco' é retornado da função
     para escolhas inválidas como nomes diferentes e valores númericos, é avisado do erro
     e pedido para inserir o serviço novamente
"""


def escolha_servico():
    preco = 0
    while True:
        servico = input('Escolha o serviço desejado: ')
        if servico == 'dig':
            preco = 1.10
            print('Você escolheu o serviço de digitalização, custa R${}'.format(preco))
            return preco
        if servico == 'ico':
            preco = 1.00
            print('Você escolheu o serviço de impressão colorida, custa R${}'.format(preco))
            return preco
        if servico == 'ibo':
            preco = 0.40
            print('Você escolheu o serviço de impressão preto e branco, custa R${}'.format(preco))
            return preco
        if servico == 'fot':
            preco = 0.20
            print('Você escolheu o serviço de fotocópia, custa R${}'.format(preco))
            return preco
        else:
            print('Escolha inválida\n Entre com o serviço desejado novamente')


"""
    Número de páginas e desconto
     dentro de um loop while, é perguntado o total de páginas desejado pelo cliente.
     as opções de if contem as especificações para cada desconto.
     o desconto é feito ao numero de páginas e retornado da função.
     caso o número de páginas for maior que o valor máximo de 20.000, a pergunta é reiniciada.
     se a resposta não foi do mesmo tipo primitivo, dará um erro e a pergunta é reiniciada
"""


def num_pagina():
    while True:
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas < 20:
                return paginas
            if 20 <= paginas < 200:
                return paginas * 0.15  # 0, 15 * 100 = 15%
            if 200 <= paginas < 2000:
                return paginas * 0.20  # 0, 20 * 10 = 20%
            if 2000 <= paginas < 20000:
                return paginas * 0.25  # 0,25 * 100 = 25%
            else:
                print('Não aceitamos esse número de páginas!')
                continue
        except ValueError:
            print('Inválido')
            continue


"""
    Serviço extra:
     aqui é feito um segundo menu, informando o produto extra e o valor.
     caso o cliente escolha uma opção extra, o produto é somado ao valor inicial 0 e retornada da função.
     caso o cliente digite um numero invalido, uma mensagem de erro é mostrada junto novamente com o menu de opções.
     se o cliente não quiser extras o valor adicionado é igual a 0 e retornado.

"""


def servico_extra():
    valor = 0
    print('Deseja adicionar mais algum serviço?')
    print('1 - Encadernação simples - R$15,00')
    print('2 - Encadernação de capa dura - R$40,00')
    print('0 - Não desejo mais nada')
    adicional = int(input())

    while True:
        if adicional == 1:
            valor = 15.0
            return valor
        if adicional == 2:
            valor = 40.0
            return valor
        if adicional == 0:
            valor = 0.0
            return valor
        else:
            print('Opção inválida')
            print('Deseja adicionar mais algum serviço?')
            print('1 - Encadernação simples - R$15,00')
            print('2 - Encadernação de capa dura - R$40,00')
            print('0 - Não desejo mais nada')
            adicional = int(input())


"""
    Código Main:
     aqui temos o menu e chamada de funções.
     cada opção tem um codigo String expecifico do serviço
     assim que as funções são finalizadas é feito o total da conta do cliente e mostrado o valor, e cada serviço pedido pelo cliente.
"""
print('Bem-vindo a copiadora do Lucas Francisco Falcão\n')
print('Entre com o serivço desejado: ')
print('DIG - Digitalização')
print('ICO - Impressão colorida')
print('IBO - Impressão preto e branco')
print('FOT - Fotocópia')

servico = escolha_servico()
numPagina = num_pagina()
extra = servico_extra()

total = servico * numPagina + extra
print('Total R${}: (serviço: {} * número de páginas: {} + extra: {})'.format(total, servico, numPagina, extra))