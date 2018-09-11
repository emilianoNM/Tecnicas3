Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> # Hello World program in Python
    
print "Hello World!\n"

	print("Pacheco Rios Jesús")
def imprimirRombo(n):
    n = n//2
    for i in range(n,0,-1):
        for j in range(n,(n-(i+1)),-1):
            print '',
        for k in range(i+1,n+1):
            print '*',
        print
    for i in range(0,n):
        for j in range(n,(n-(i+1)),1):
            print '',
        for k in range(i+1,n+1):
            print '*',
        print 
 
imprimirRombo(10)  
