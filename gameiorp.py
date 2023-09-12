from random import randint
v=0
while True:
    jogador=int(input('Digite um numero: '))
    computador=randint(0,10)
    total=jogador+computador
    tipo=' '
    while tipo not in'PI':
        tipo=str(input('PAR OU IMPAR? [ P ]/[ I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, total de {total} ',end='')
    print(f'DEU PAR!'if total % 2==0 else 'DEU IMPAR!')
    if tipo=='P':
        if total % 2 == 0:
           print('Você ganhou!!'.upper())
           v+=1
        else:
            print('Você perdeu!!'.upper())
            break
    elif tipo=='I':
        if total % 2 == 1:
            print('Você ganhou!!')
            v+=1
        else:
            print('Você perdeu!!'.upper())
            break
    print('Vamos jogar novamente? '.capitalize())
print(f'Gamer houver você ganhou {v} partida.')
