def ordburbuja(empleados):
    for j in range(len(empleados)-1,0,-1):
        for i in range(j):
            if ord(empleados[i][0])>ord(empleados[i+1][0]) or ord(empleados[i][0])==ord(empleados[i+1][0]):
                if ord(empleados[i][0])==ord(empleados[i+1][0]):
                    for a in range(len(empleados)):
                        if ord(empleados[i][a])==ord(empleados[i+1][a]):
                            var = empleados[i]
                            empleados[i] = empleados[i+1]
                            empleados[i+1] = var
                            break
                    continue
                var = empleados[i]
                empleados[i] = empleados[i+1]
                empleados[i+1] = var

empleados = [" Jose A"," Arreonda M", " Arreola Alarcon", "Ramiro Valer", "Diego Mirante", "Wanda Xia", "Jamie Side"]
ordburbuja(empleados)
print(empleados)
