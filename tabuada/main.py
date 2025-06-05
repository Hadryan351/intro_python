import os
from rich.console import Console
from rich.table import Table

console = Console()

def clear_screen():
    """Clear the console screen."""
    console.print(f'[bold red]LIMPANDO A TELA...[/bold red]')
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    MENU_TABUADA = f'''
    [bold green][1][/bold green]: -> Tabuada de 1
    [bold green][2][/bold green]: -> Tabuada de 2
    [bold green][3][/bold green]: -> Tabuada de 3
    [bold green][4][/bold green]: -> Tabuada de 4
    [bold green][5][/bold green]: -> Tabuada de 5
    [bold green][6][/bold green]: -> Tabuada de 6
    [bold green][7][/bold green]: -> Tabuada de 7
    [bold green][8][/bold green]: -> Tabuada de 8
    [bold green][9][/bold green]: -> Tabuada de 9
    [bold green][0][/bold green]: -> Sair do programa
'''

    console.print(MENU_TABUADA)
    return ('1', '2' , '3', '4', '5', '6', '7', '8', '9', '0')

def geneterate_tabuada(num):
    clear_screen()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(f"Multiplicando {num}", style="center")
    for i in range(1, 11):
        if operacao == '+':
            result = i + num
        elif operacao == '-':
            while i > num: 
                  i += 1
            result = i - num
        elif operacao == '*':
              result = i * num
        elif operacao == '/':
            i = i * num
            result = i / num
                
        table.add_row(f'{i} {operacao} {num} = {int(result)}', style="bold green")
    console.print(table)

console.print(f'[bold green]Bem-vindo ao programa de Tabuada![/bold green]')
options_menu = display_menu()
operadores = ['+', '-', '*', '/']
operacao = ''
OP = ''
while OP != '0':
    try:
        OP = console.input(f'Informe a opção desejada: ') 
        if OP in options_menu:
            if OP == '0':
                console.print(f'[bold red]Saindo do programa...[/bold red]')
                break
            else:
                num = int(OP)
                operacao = console.input(f'Informe a operação desejada (+, -, *, /): ')
                if operacao not in operadores:
                    console.print(f'[bold red]Operação inválida! Use +, -, * ou /.[/bold red]')
                    continue
                geneterate_tabuada(num)

        else:
            console.print(f'[bold red]Opção inválida! Tente novamente.[/bold red]')
        
    except ValueError:
        console.print(f'[bold red]Por favor, insira um número válido.[/bold red]')


   