import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
    {'nome': 'Pizza Suprema', 'categoria': 'Pizzaria', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]


def voltar_ao_menu(): 
    input('Digite qualquer tecla para voltar ao menu principal: ')
    main()


def subtitulo(texto):
    os.system('cls')

    print(f'\033[33m{texto}\033[m\n')
    


def exibir_nome_programa():
    print('\033[mSabor Express\n\033[m')


def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu()


def cadastrar_restaurante():
    subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Categoria: ')
    dados_do_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)

    print(f'{nome_restaurante} foi cadastrado!\n')

    voltar_ao_menu()


def listar_restaurantes():
    subtitulo('Listando restaurantes')
    
    print(f'{"Nome do restaurante".ljust(25)}  {"Categoria".ljust(25)}  Status\n')
    for r in restaurantes:
        if r['ativo']:
            mensagem_ativo = 'Ativo'
        else:
            mensagem_ativo = 'Não ativo'
        
        nome_restaurante = r['nome']
        categoria = r['categoria']
        print(f'{nome_restaurante.ljust(25)}  {categoria.ljust(25)}  {mensagem_ativo.ljust(25)}\n')
    
    print()

    voltar_ao_menu()



def alterar_estado_restaurante():
    subtitulo('Ativação do restaurante')
    nome_restaurante = input('Nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            if restaurante['ativo']:
                mensagem = f'{nome_restaurante} foi ativado com sucesso!\n'
            else:
                mensagem = f'{nome_restaurante} foi desativado com sucesso!\n'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('Restaurante não foi encontrado\n')
    
    voltar_ao_menu()


def finalizar_app():
    os.system('cls')
    print('Finalizando o app')


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
