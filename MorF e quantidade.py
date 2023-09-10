tot18=toth=totm20=0
while True:
    idade=int(input('Qual é a sua idade? '))
    sexo=' '
    while sexo not in 'M,F':
        sexo=str(input('Qual é o seu sexo? [ M ]/[ F ] ')).upper().strip()[0]
    if idade>=18:
        tot18+=1
    if sexo=='M':
        toth+=1
    if sexo=='F' and idade<20:
        toth+=1
    resposta=' '
    while resposta not in 'SN':
        resposta=str(input('Quer continuar [ S ]/[ N ]')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'O total de pessoas maiores de 18 anos é de {tot18}!')
print(f'O total de homens cadastrados é de {toth}!')
print(f'O total de mulheres cadastradas abaixo de 20 anos é de {totm20}!')
