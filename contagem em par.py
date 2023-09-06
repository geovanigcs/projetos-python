from time import sleep
x=str(input('Digite OK para receber a sequência de números pares: ').upper())
if x=='OK':
    print('Iniciando.'.upper())
    sleep(1)
    print('Processando requisição...')
    sleep(2)
    for c in range(0,50,2):
        print(c)
print('Sequência finalizada!!')
