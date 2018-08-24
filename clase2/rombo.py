Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def imprimirRombo(n):
    n = n//2
    for i in range(n,0,-1):
        for j in range(n,(n-(i+1)),-1):
            print '',
        for k in range(i+1,n+1):
            print '*',
        print
    for i in range(0,n):
        for j in range(n,(n-(i+1)),-1):
            print '',
        for k in range(i+1,n+1):
            print '*',
        print 
 
imprimirRombo(10)
