# desafio consiste em desifrar uma mensagem cripitografada.

# Usando ord(), Basicamente a gente ira pegar as letras é converte para o numero correspondete em ASCII, exemplo: a = 97, se somar 97 + 2 = 99, 99 é correspondete a c em ASCII.

# função ord() é chr() são opostas uma trasforma a = 97, enquanto a outra converte 99 = c.



# criamos uma função que converte é soma os numeros em ASCII é retorna um o valor, Exemplo n = 110 é 2 - return = p

# operador mod, para efutar os calculos em ordem, precisara ficar atento as ordem de precedencias 

def lasso_letter(letter, shift_amount):
    # passo 0
    letter_code = ord(letter.lower())
    
    # passo cod
    
    a_ascii = ord('a')
    
    # passo alf
    alphabet_size = 26
    
    #passo calculo
    true_letter_code = a_ascii + (((letter_code - a_ascii)+ shift_amount) % alphabet_size)
    
    #convertendo de ASCII, Numero em caractert
    decoded_letter = chr(true_letter_code)
    
    # retorno final
    return decoded_letter
    

def lasso_word(word , shift_amount):
    
    # valor final e atribuido nessa variavel.
    decoded_word = ""
    
    # usando for, um lasso de controle, consigo repetir as letras, decripitando elas, formando as frases!
    for letter in word:
        
        decoded_letter = lasso_letter(letter, shift_amount)
        
        decoded_word = decoded_word + decoded_letter
        
    # para retorna o valor, lembrese de manter a return fora da contatenação do for!   
    return decoded_word
        
    
    
    
    
# \n é usado apenas para quebra de linha!
print(f'{lasso_word("Ncevy", 13)},{lasso_word("gpvsui", 25)},{lasso_word("ugflgkg", -18)}{lasso_word("wjmmf", -1)}')


# print(lasso_letter("p", -2))

    
    