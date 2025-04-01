# usei a função TITLE para deixar a primeira caractere de cada frase em maiúsculo
nom = str(input('Digite seu nome: ')).title().strip() 

# verifiquei se há silva no nome usando a função IN
print(f'Há Silva no nome? {'Silva' in nom}')