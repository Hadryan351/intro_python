import os
from rich.console import Console

console = Console()

os.system('cls' if os.name == 'nt' else 'clear')

menu = '''[bold green][1][/bold green]: -> Criar Arquivo
[bold green][2][/bold green]: -> Ler Arquivo
[bold green][3][/bold green]: -> Editar Arquivo
[bold green][4][/bold green]: -> Deletar Arquivo
[bold green][5][/bold green]: -> Limpar Tela
[bold green][6][/bold green]: -> Lista diretório
[bold green][7][/bold green]: -> Mudar diretório
[bold green][8][/bold green]: -> Localização atual
[bold green][0][/bold green]: -> Encerrar Script'''

opcoes_menu = ('1','2','3','4','5','6','7','8','0')
OP = ''

while OP != '0':
    try:
        console.print(menu)
        OP = console.input('Informe a opção desejada: ')

        if OP in opcoes_menu:
            if OP == '1':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} CRIANDO ARQUIVO {'#' * 10}')
                fname = console.input('Informe o nome do arquivo: ')
                fname = f'{fname}.txt'

                with open(fname, 'x', encoding='utf8') as f:
                    console.print(f'Arquivo {fname.upper()} Criado com sucesso')
            
            elif OP == '2':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} LENDO ARQUIVO {'#' * 10}')
                fname = console.input('Informe o nome do Arquivo: ')
                fname = f'{fname}.txt'

                with open(fname, 'r', encoding='utf8') as f:
                    console.print(f'Arquivo {fname.upper()} Criado com sucesso')
                
            elif OP == '3':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} EDITANDO ARQUIVO {'#' * 10}')
                fname = console.input('Informe o nome do Arquivo: ')
                fname = f'{fname}.txt'

                text = console.input ('Digite o  texto:\n')

                with open(fname, 'a', encoding='utf8') as f:
                    f.write(text)
    
            elif OP == '4':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} EXCLUINDO ARQUIVO {'#' * 10}')
                fname = console.input('Informe o nome do Arquivo: ')
                fname = f'{fname}.txt'

                if os.path.exists(fname):
                    os.remove(fname)
                    console.print('Arquivo excluido com sucesso!')
                else:
                    console.log('Arquivo não encontrado!')
            
            elif OP == '5':
                os.system('cls' if os.name == 'nt' else 'clear')
            elif (OP == '6'):
                os.system('cls' if os.name == 'nt' else 'clear')
                list_dir = os.listdir()

                for i in list_dir:
                    console.print(1)
            elif OP == '7':
                os.system('cls' if os.name == 'nt' else 'clear')
                console.print(f'{'#' * 10} NAVEGANDO ENTRE PASTAS {'#' * 10}')
                destination = os.chdir(console.input('Mudar para Pasta:'))
                console.print('PASTA ATUAL: ', os.getcwd())

            elif OP == '8':
                os.system('cls' if os.name == 'nt' else 'clear')
                current = os.getcwd()
                console.print(f'[blue] DIRETORIO CORRENTE[/blue] [underline] {current}[/underline]')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
        console.print('[bold red]Opção invalida, tente novamente![/bold red]')    
    except FileExistsError:
        console.print('[boldyellow]O arquivo já existe!![/boldyellow]')
    except FileNotFoundError:
        console.print('[boldyellow]Arquivo não encontrado!![/boldyellow]')     
os.system('cls' if os.name == 'nt' else 'clear')