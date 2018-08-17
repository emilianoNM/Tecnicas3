word = input("Comprobar la palabra si es palindroma: ")
print(word[::-1].lower().replace(' ','')==word[::1].lower().replace(' ',''))
