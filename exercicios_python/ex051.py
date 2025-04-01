# p.a e a sua razão

# meu código com falhas
primeiro_termo = int(input(
    'Digite o primeiro termo: '
))

razao_progressao = int(input(
    'Digite a razão da progressão: '
))

termo_dez = []
for c in range(primeiro_termo, 99999, razao_progressao): # se começar com 99999 fudeu
    termo_dez.append(c)
   
print(f'Aqui está os 10 primeiros termos da sua P.A: {termo_dez[0:10]}')

# versão otimizada

termos = [primeiro_termo + (c * razao_progressao) for c in range (10)]
print(f'Aqui está os 10 primeiro termos: {termos}')

