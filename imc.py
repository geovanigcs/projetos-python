altura = float(input('Qual é a sua altura em centímetros? '))
peso = float(input('Qual o seu peso em quilogramas? '))
imc = peso / (altura**2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('e está classificado como magreza'.format(imc))
elif 18.5<= imc <24.9:
    print('e está classificado como normal'.format(imc))
elif 25<= imc <29.9:
    print('e está classificado como Sobrepeso'.format(imc))
elif 30<= imc <34.9:
    print('e está classificado como Obesidade grau I'.format(imc))
elif 35<= imc <39.9:
    print('e está classificado como Obesidade grau II'.format(imc))
elif imc >=40:
    print('e está classificado como Obesidade grau III'.format(imc))
