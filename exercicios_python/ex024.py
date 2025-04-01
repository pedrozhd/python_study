# usei a função LOWER para deixar todas as carateres em minúsculas e 
# STRIP para que eu possa divdir a string e pegar a primeira posição [0]
cid = str(input('Digite o nome da sua cidade: ')).lower().strip()

# usei o comando split para dividir a string, verifiquei se há 'santo' na primeira posição [0] com a string já dividida!
print(f'Ela começa com Santo? {'santo' in cid.split()[0]}')