from time import sleep
x=input('Digite ok pra continuar.').upper()
if x=='OK':
    for c in range(10,0,-1):
     print(c)
     sleep(1)
else:
    print('Error tente novamente!'.upper())
print('end!')
print('I Happy new world'.upper())
