# Para começar, você deverá fazer cinco perguntas com somente duas opções de resposta!

#Teste de Personalidade Basico, Agradavel ainda pode ser mais otimizado é melhorado! 

def escr(n):
    txt = input(n)
    txt.lower()
    return txt 
def cole(n):
    print(n)
    


cole('-' * 30)
cole('Teste de Personalidade!')
cole('-' * 30)

# Primeira Opção!
cole('[a] - Ler um livro')
cole('[b] - Ir à uma festa') 
P = escr('O que você prefere fazer à noite ? ')
cole('-' * 30)

#Segunda Opção

cole('[a] - Ser um curador no Instituto Smithsonianw')
cole('[b] - Administrar uma empresa') #luxo

S = escr('Qual é o seu emprego dos sonhos? ')

#Terceira Opção 
cole('[a] - Money')
cole('[b] - Amor')

T = escr('O que é mais importante? ')

cole('-' * 30)

#Quarta Opção 
cole('[a] - Década de 1910')
cole('[b] - Década de 2010')

Q = escr('Qual é a sua década favorita? ')

cole('-' * 30)

#Quinta Opção 
cole('[a] - Automóvel')
cole('[b] - De avião')

Qi  = escr('Qual é o seu modo favorito de viajar? ')

ls_one = P,S,T,Q,Qi
ls_two = P,S,T,Q,Qi

if ls_one == ('a', 'a', 'b', 'a', 'a'):
    
    cole(f'\nVocê e muito luxuoso é ambicioso!')
    
elif ls_two == ('b', 'b', 'a', 'b', 'b'):
    cole(f'Você preza muito pelo conhecimento!')
    
else:
    cole(f'Você é muito legal! ')


