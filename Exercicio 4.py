lista_livro = []
id_global = 0  # contador


def cadastrar_livro(id):
    global id_global
    nome = input('Qual o nome do livro? ')
    autor = input('Qual o nome do autor? ')
    editora = input('Qual é a editora do livro? ')

    livro = {
        'id': id_global,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    lista_livro.append(livro)
    print('Livro cadastrado com sucesso')

    # Incrementa o id_global APÓS adicionar o livro na lista
    id_global += 1


def consultar_livro():
    opcao = int(input('escolha a opção desejada: \n1. Consultar todos \n2. Consultar por Id '
                      '\n3. Consultar por autor \n4. Retornar ao menu \n>> '))
    if opcao == 1:
        for livro in lista_livro:
            print(livro)
    elif opcao == 2:
        id_consulta = int(input('Qual é o id do livro que você deseja consultar? '))
        for livro in lista_livro:
            if livro['id'] == id_consulta:
                print(livro)
                break
    elif opcao == 3:
        autor = input('Qual o autor você deseja consultar? ')
        for livro in lista_livro:
            if livro['autor'] == autor:
                print(livro)
    elif opcao == 4:
        return
    else:
        print('Opção inválida')


def remover_livro():
    id_remover = int(input('Qual o id do livro que você deseja remover? '))
    for i, livro in enumerate(lista_livro):
        if livro['id'] == id_remover:
            lista_livro.pop(i)
            print('Livro removido com sucesso')
            break


def main():
    print('Bem-vindo ao Controle de Livros de Lucas Francisco Falcão')

    while True:
        opcao = int(input('escolha a opção desejada: \n1. Cadastrar livro \n2. Consultar livro '
                          '\n3. Remover livro \n4. Encerrar programa \n>> '))
        if opcao == 1:
            cadastrar_livro(id_global)
        elif opcao == 2:
            consultar_livro()
        elif opcao == 3:
            remover_livro()
        elif opcao == 4:
            print("Encerrando o programa...")
            break
        else:
            print('Opção inválida')


main()
