n=str(input('Digite seu nome completo: '))
ns=n.strip('')
print(f'o seu nome e {n}!')
print(f'o seu nome com todas as letras Maiusculas e {n.upper()}!')
print(f'o seu nome com todas as letras minisculas e {n.lower()}!')
print(f"o Seu nome tem {len(n)-n.count(' ')} letras.")
SS=n.split()
print(f'o primeiro nome e {SS[0]} e  tem {len(SS[0])} letras!')
