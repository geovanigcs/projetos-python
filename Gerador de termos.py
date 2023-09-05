print('Gerador de PA')
term=int(input('Digite o primeiro termo: '))
raz=int(input('Digite a razão: '))
print('=-='*20)
termo=term
pa=1
total=0
mais=10
while mais !=0:
    total=total+mais
    while pa<=total:
        print(f'{termo}',end=' ')
        termo+=raz
        pa+=1
    print('PAUSA'.upper())
    mais=int(input(f'Quantos termos você quer mostar a mais? '))
print(f'A contagem de termos total foi de {pa} termos!')
