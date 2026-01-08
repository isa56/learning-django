import os

APP_NAME = """
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
"""

restaurants = [{'name': 'pizza place', 'category': 'italiana', 'active': True},
               {'name': 'sushi world', 'category': 'japonesa', 'active': False}]


def create_restaurant():
    '''
    Função para cadastrar um novo restaurante.

    Inputs:
    - Nome do restaurante
    - Categoria do restaurante
    '''

    restaurant_name = input('Digite o nome do restaurante: ')
    restaurant_category = input('Digite a categoria do restaurante: ')
    restaurants.append({'name': restaurant_name, 'category': restaurant_category, 'active': False})
    print(f'Restaurante "{restaurant_name}" cadastrado com sucesso!\n')

def list_restaurants():
    '''
    Função para listar todos os restaurantes cadastrados.
    '''
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurant in restaurants:
        print(f'- {restaurant["name"].ljust(20)} | {restaurant["category"].ljust(20)}: {"Ativo" if restaurant["active"] else "Inativo"}')
    print('')

def toggle_restaurant_activation():
    '''
    Função para ativar ou desativar um restaurante.

    Inputs:
    - Nome do restaurante
    '''

    list_restaurants()
    restaurant_name = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    for restaurant in restaurants:
        if restaurant['name'].lower() == restaurant_name.lower():
            restaurant['active'] = not restaurant['active']
            status = "ativado" if restaurant['active'] else "desativado"
            print(f'Restaurante "{restaurant_name}" {status} com sucesso!\n')
            break
    else:
        print(f'Restaurante "{restaurant_name}" não encontrado.\n')

def exit_app():
    '''
    Função para sair do aplicativo.
    '''

    clean_show_text('Saindo do aplicativo. Até logo!')
    exit()

def clean_show_text(text, showLine=True):
    '''
    Função para limpar a tela e mostrar um texto formatado.

    :param text: Texto a ser exibido
    :param showLine: Indica se deve mostrar linhas acima e abaixo do texto
    '''

    os.system('cls')
    line = '*' * (len(text) + 4) if showLine else ''
    print(f'{line}\n{text}\n{line}\n')

def return_to_menu():
    '''
    Função para retornar ao menu principal.

    Inputs:
    - Pressione Enter para voltar ao menu principal
    '''

    input('\nPressione Enter para voltar ao menu principal...')
    os.system('cls')
    initialize_app()

def handle_options(option):
    '''
    Função para lidar com as opções do menu.
        
    :param option: Opção selecionada pelo usuário
    '''

    match option:
        case 1:
            clean_show_text('Cadastro de novo restaurante')
            create_restaurant()
            return_to_menu()
        case 2:
            clean_show_text('Lista de restaurantes cadastrados')
            list_restaurants()
            return_to_menu()
        case 3:
            clean_show_text('Alterar estado do restaurante\n')
            toggle_restaurant_activation()
            return_to_menu()
        case 4:
            exit_app()
        case _:
            print('Opção inválida. Tente novamente.\n')
            initialize_app()


def initialize_app():
    '''
    Função para inicializar o aplicativo e mostrar o menu principal.

    Inputs:
    - Opção do menu principal
    '''

    options = ['Cadastrar Restaurante', 'Listar Restaurantes', 'Alterar Estado do Restaurante', 'Sair']

    for option in options:
        print(f'{options.index(option) + 1}. {option}')
    try:
        user_choice = int(input('Selecione uma opção: '))
        handle_options(user_choice)
    except ValueError:
        print('\nEntrada inválida. Por favor, insira um número.\n')
        initialize_app()


def main():
    clean_show_text(APP_NAME, False)
    initialize_app()

if __name__ == '__main__':
    main()
