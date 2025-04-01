x = str(input('Digite algo: '))

print('=========================')

print(f'O valor escolhido é letra? {x.isalpha()}')
print(f'O valor escolhido é número? {x.isnumeric()}')
print(f'O valor escolhido está em maiúsculo? {x.isupper()}')
print(f'O valor está capitalizado? {x.istitle()}') # nem maiúsculas e nem minúsculas