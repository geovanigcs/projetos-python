n=int(input('Digite um número de 0 a 9999: '))
u= n // 1%10
d= n // 10%10
c= n // 100%10
m= n // 1000%10
print(f'o numero  digitado foi {n}! \n\n'
      f'A unidade é {u}!\n'
      f'A dezena  é {d}!\n'
      f'A centena é {c}!\n'
      f'O milhar é {m}!')
