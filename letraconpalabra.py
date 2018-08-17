
cadena=raw_input("escriba palabra")
letra=raw_input("escriba letra")
print(sum(letra in palabra for palabra in cadena.split()))
