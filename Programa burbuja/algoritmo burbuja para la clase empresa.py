# algoritmo burbuja para la clase empresa

def Ordenburbuja(trabador):
    
#Se intruduce ciclos for para el ordenamiento
    for j in range(len(trabador)-1,0,-1):
        
        for i in range(j):
            
            if ord(trabador[i][0])>ord(trabador[i+1][0]) or ord(trabador[i][0])==ord(trabador[i+1][0]):
                if ord(trabador[i][0])==ord(trabador[i+1][0]):
                    for a in range(len(trabador)):
                        
                        if ord(trabador[i][a])==ord(trabador[i+1][a]):
                            
                            var = trabador[i]
                            trabador[i] = trabador[i+1]
                            trabador[i+1] = var
                            
                            break
                    continue
                
                var = trabador[i]
                trabador[i] = trabador[i+1]
                trabador[i+1] = var

trabador = [" Calor F"," Marta Olivare", " Carla Alvares", "Juan Sarate", "Luis Miguel", "Amanda Fer", "Paloma fea"]

Ordenburbuja(trabador)
#Lo imprime
print(trabador)
