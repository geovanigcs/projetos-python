print('*=*'*40)
print('{:^120}'.format('Banco Safra').upper())
print('*=*'*40)
valor=int(input('Qual valor você deseja realizar o saque? '.upper()))
total=valor
ced=50.00
totalcd=0
while True:
    if total>=ced:
        total-=ced
        totalcd+=1
    else:
        if totalcd>00:
            print(f'Serão {totalcd} cédulas de {ced}')
        if ced==50.00:
            ced=20.00
        elif ced==20:
            ced=10.00
        elif ced==10.00:
            ced=1
        totalcd=00
        if total ==00:
            break

print('-'*40)
print('{:^38}'.format('Volte sempre!!'.upper()))
print('-'*40)
