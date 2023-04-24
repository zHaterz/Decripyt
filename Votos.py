from datetime import date

Nasc = int(input('Digite seu ano de nascimento: '))

ano_Atual = date.today().year

Idd = ano_Atual - Nasc

if Idd <= 16: 
    print(f'Você ainda não pode votar!, sua idade é {Idd}')
elif Idd > 59:
    print(f'Você não precisa mais votar!, sua idade é {Idd}')
else: 
    print(f'Você precisa votar, sua idade é {Idd}')

