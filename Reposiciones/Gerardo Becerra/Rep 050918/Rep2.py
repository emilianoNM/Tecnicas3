
# coding: utf-8

# In[ ]:


def numero_primo(num):
    if num==1 or num==0: 
        return False
    elif num == 2:
         return True
    elif num > 2:
        for divisor in range (2, num):
            if num % divisor==0:
                return False
            elif num % divisor != 0 and divisor==num-1:
                return True

print numero_primo (265)

