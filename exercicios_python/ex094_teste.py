from rich.console import Console
from rich.table import Table
from rich.style import Style

# Cria uma instância do console
console = Console()

lista_cadastro = list()
nome_mulheres = list()
acima_da_media = list()
soma_idades = 0

while True:
    cadastro = dict()
    
    # Nome
    cadastro['nome'] = console.input('[bold green]Digite seu nome: [/bold green]').capitalize()
    
    # Sexo
    while True:
        sexo = console.input('[bold blue]Digite seu sexo [M/F]: [/bold blue]').upper()
        if sexo in ['M', 'F']:
            cadastro['sexo'] = sexo
            break
        else:
            console.print('[bold red]Entrada inválida. Digite apenas "M" ou "F".[/bold red]')
    
    # Idade
    while True:
        try:
            idade = int(console.input('[bold yellow]Digite a sua idade: [/bold yellow]'))
            if idade >= 0:
                cadastro['idade'] = idade
                soma_idades += idade
                break
            else:
                console.print('[bold red]A idade deve ser um número positivo.[/bold red]')
        except ValueError:
            console.print('[bold red]Apenas números são válidos.[/bold red]')
    
    # Verifica se é mulher e adiciona ao nome_mulheres
    if cadastro['sexo'] == 'F':
        nome_mulheres.append(cadastro['nome'])
    
    lista_cadastro.append(cadastro)
    
    # Pergunta se quer continuar
    while True:
        pergunta = console.input('[bold cyan]Quer continuar [S/N]? [/bold cyan]').upper()
        if pergunta in ['S', 'N']:
            break
        else:
            console.print('[bold red]Entrada inválida. Digite apenas "S" ou "N".[/bold red]')
    
    if pergunta == 'N':
        break

# Calcula a média das idades
media = soma_idades / len(lista_cadastro)

# Verifica as pessoas com idade acima da média
for pessoa in lista_cadastro:
    if pessoa['idade'] > media:
        acima_da_media.append(pessoa)

# Exibe os resultados em uma tabela
table = Table(title="Resultados", show_header=True, header_style="bold magenta")
table.add_column("Descrição", style="cyan")
table.add_column("Valor", style="green")

table.add_row("Número total de pessoas cadastradas", str(len(lista_cadastro)))
table.add_row("Média de idade das pessoas cadastradas", f"{media:.2f}")
table.add_row("Mulheres registradas", ', '.join(nome_mulheres))
table.add_row("Pessoas com idade acima da média", '\n'.join([f"{pessoa['nome']} ({pessoa['idade']} anos)" for pessoa in acima_da_media]))

console.print(table)