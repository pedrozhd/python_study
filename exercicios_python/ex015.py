km = float(input("Quantos KM'S rodados? "))
dia = int(input('Rodou por quantos dias? '))
calc1 = 0.15 * km
calc2 = 60 * dia

print(f'Você vai pagar: R${calc1 + calc2:.2f}')