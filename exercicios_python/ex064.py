soma = 0
contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        contador += 1
        soma += num
    if num == 999:
        break
print(
    f'Foram digitados {contador} números, e a soma entre eles deu: {soma}!'
)