
# coding: utf-8

# In[ ]:


def fibonacci(n):
    valoractual = 1
    valoranterior = 1
    for i in range(n - 1):
        k = valoranterior
        valoranterior = valoractual + valoranterior
        valoractual = k
    return valoractual
    
def fibonacci_r(n):
 if n == 1 or n == 2:
  return 1
 return fibonacci_r(n - 1) + fibonacci_r(n - 2)

