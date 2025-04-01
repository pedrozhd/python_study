pr = float(input('Digite o preço do produto: R$'))
des = pr * (5/100)

print(f'O seu produto com 5% de desconto ficará em: R${pr - des:.2f}, você economizou R${des:.2f}')