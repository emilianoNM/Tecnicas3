#karen
a=int(input("escribe n1:"))
b=int(input("\nescribe n2:"))
c=int(input("\nescribe n3:"))
print("sum:%i",a+b+c)
print("\npromedio:%i",(a+b+c)/3)
print("\nproducto:%i",a*b*c)
if a>b and a>c:
    print("a es el numero mayor",a)
    if b>c:
        print("\nc es el numero menor",c)
    else:
        print("\nb es el numero menor",b)
else:
    if b>a and b>c:
        print("\nb es el numero mayor",b)
        if c>a:
            print("\na es el numero menor",a)
        else:
            print("\nc es el numero menor",c)
    else:
        print("\nc es el numero mayor",c)
        if b>a:
            print("\na es el numero menor",a)
        else:
            print("\nb es el numero menor",b)
        

        
        
