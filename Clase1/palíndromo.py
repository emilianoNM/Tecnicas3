
frase = input('Ingrese una frase o palabra:') 
 
temp = frase.replace(' ','') 
 
if temp == temp[::-1]: 
    print('Palindromo') 
else: 
    print('No es palindromo') 
