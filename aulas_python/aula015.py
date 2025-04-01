# while (parte 2)

s = 0
c = 0
while True: # executa para sempre
    num = int(input('Digite um número: '))
    
    if num != 999:
        s += num
        c += 1
    else:
        break
    
print(s, c)