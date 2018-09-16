num = int(input("introduce numero:"))

if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"no es numero primo")
           print(i,"veces",num//i,"es",num)
           break
   else:
       print(num,"es numero primo")
       
else:
   print(num,"no es numero primo")
