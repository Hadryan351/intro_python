import os
from rich.console import Console
from rich.table import Table

console = Console()

def limpar_tela():
    """Limpa a tela do terminal."""
    console.print(f'[bold red]LIMPANDO A TELA...[/bold red]')
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpar_tela()
    """Mostra o menu de opções."""
    MENU = f'''
    [bold green][1][/bold green]: -> Tabuada de 1
    [bold green][2][/bold green]: -> Tabuada de 2
    [bold green][3][/bold green]: -> Tabuada de 3
    [bold green][4][/bold green]: -> Tabuada de 4
    [bold green][5][/bold green]: -> Tabuada de 5
    [bold green][6][/bold green]: -> Tabuada de 6
    [bold green][7][/bold green]: -> Tabuada de 7
    [bold green][8][/bold green]: -> Tabuada de 8
    [bold green][9][/bold green]: -> Tabuada de 9
    [bold green][0][/bold green]: -> Sair
'''
    console.print(MENU)
    return ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

def calcular_tabuada(numero):
    limpar_tela()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(f'Tabuada do {numero}', justify="center")
    for i in range(0, 11):
        if operacao == '+':
            resultado = i + numero
        elif operacao == '-':
            i = i + numero
            resultado = i - numero
        elif operacao == '*':
            resultado = i * numero
        elif operacao == '/':
            i = i * numero
            resultado = i / numero
                
        table.add_row(f'{i} {operacao} {numero} = {int(resultado)}', style="bold green")
    console.print(table)

console.print(f'[bold green]Bem-vindo ao programa de Tabuada![/bold green]')
options_menu = mostrar_menu()
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
                numero = int(OP)
                operacao = console.input(f'Informe a operação desejada (+, -, *, /): ')
                if operacao not in operadores:
                    console.print(f'[bold red]Operação inválida! Use +, -, * ou /.[/bold red]')
                    continue
                calcular_tabuada(numero)

        else:
            console.print(f'[bold red]Opção inválida! Tente novamente.[/bold red]')
        
    except ValueError:
        console.print(f'[bold red]Por favor, insira um número válido.[/bold red]')