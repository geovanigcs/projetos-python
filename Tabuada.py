while True:
    numero = int(input('Digite um número para ver a Tabuada dele: '))
    print('-' * 30)
    if numero < 0:
        break
    for c in range(1, 11):
         print(f' {numero}  X {c}  = {numero*c}!')
    print('-' * 30)
print('Tabuada encerrada, te vejo em breve!')
