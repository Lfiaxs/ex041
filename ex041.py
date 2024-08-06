from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento atleta? '))
idade = atual - nasc
print('Analisando seu ano de nascimento, sua categoria é...')
if idade <= 9:
    print('MIRIM, você tem {} anos de idade.'.format(idade))
elif idade <= 14 and idade > 9:
    print('INFANTIl, você tem {} anos de idade.'.format(idade))
elif idade <= 19 and idade > 14:
    print('JUNIOR, você tem, {} anos de idade.'.format(idade))
elif idade <=25 and idade > 19:
    print('SÊNIOR, você tem {} anos de idade.'.format(idade))
else:
    print('MASTER, você tem, {} anos de idade.'.format(idade))


