
# coding: utf-8

# In[1]:


#Programa de cajero ATM (DEPOSITOS, RETIROS Y CONSULTA)
#Programa por CBLUELENNON (RVT)


# In[2]:


print("Bienvenido al cajero azul")
saldo=1500
print("Elija la opcion que desee")
print(" 1.-Consulta de saldo\n 2.-Retiro de efectivo\n 3.-Deposito de efectivo\n 4.-Salir")


# In[3]:


x=int(input("Elija la opcion que desea"))
while(x>=1 and x<=4):
    if(x==1):
        print("Su saldo es:",saldo,"MXN")
        x=int(input("Elija la opcion que desea"))
    if(x==2):
        y=int(input("ingrese la cantidad que desea retirar"))
        if(y<=saldo):
            print("Usted ha retirado",y,"MXN")
            saldo=saldo-y
            x=int(input("Elija la opcion que desea"))
        elif(y>saldo):
            print("Usted no cuenta con esa cantidad actualmente")
    if(x==3):
        z=int(input("Ingrese la cantidad que desea depositar"))
        print("Usted ha depositado",z,"MXN")
        saldo=saldo+z
        x=int(input("Elija la opcion que desea"))
    if(x==4):
        break
        

