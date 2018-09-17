###programa para dar el triangulo de pascal

def pascalTriangle(n): 
    # Caso base 
    if n == 0: 
        return [] 
     
    if n == 1: 
        return [[1]] 
     
    # Caso recursivo 
    last_list = pascalTriangle(n-1) 
     
    this_list = [1] 
    for i in range(1, n-1): 
        this_list.append(last_list[n-2][i-1] + last_list[n-2][i]) 
    this_list.append(1) 
     
    last_list.append(this_list) 
     
    return last_list 
     
def lastLine(n): 
    triangle = pascalTriangle(n) 
    return triangle[n-1] 