peso = float(input('Digite seu peso: '))
alt = float(input('Digite a sua altura: '))

imc = peso / alt ** 2 

if imc < 18.5:
    print('Você está abaixo do peso.')

elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal.')

elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso.')

elif imc > 30 and imc <= 40:
    print('Você está obeso.')

elif imc > 40:
    print('Você é um obeso mórbido.')