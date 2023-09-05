from random import randint
import time
print('JO KEN PÔ!!'.upper())
print('''Suas opções!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
lista=('PEDRA','PAPEL','TESOURA')
pc=randint(0,2)
e=int(input('Escolha uma das formas: '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔÔÔÔ')
time.sleep(2)
print('=-='*15)
print(f'O escolhido do Saitama foi {lista[pc]}!')
print(f"A sua escolha foi {lista[e]}!")
print('=-='*15)
if pc==0:
    if e==0:
        print('EMPATE!')
    elif e==1:
        print('Você ganhou!')
    elif e==2:
        print('Você perdeu!')
    else:
        print('Opção invalida!')
elif pc==1:
    if e==0:
        print('Você perdeu!')
    elif e==1:
        print(('EMPATE!'))
    elif e==2:
        print('Você ganhou!')
    else:
        print('Opção invalida!')
elif pc==2:
    if e==0:
        print('Você ganhou!')
    elif e==1:
        print('Você perdeu!')
    elif e==2:
        print('EMPATE!')
    else:
        print('o1pção invalida!')
