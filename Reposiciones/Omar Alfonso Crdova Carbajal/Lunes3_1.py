nombres = [["aaaaa", 111111, 11], ["sssssss", 2222222, 22], ["ddddddd", 3333333, 33], ["qqqqqqqqq", 55555555, 55],
          ["gggggg", 323232, 32], ["wwwwww", 444444, 44], ["rrrrrrrrrr", 888888888, 88], ["uuuuuu", 77777, 77],
          ["yyyyyyyyyy", 9999999, 99], ["fffffff", 10000000, 100000]]

def busquedaAlumno(A, n, cuenta):
   E = -1
   for i in range(n):
       if A[i][1] == cuenta:
           E = i
           break
   if E != -1:
       print("Nombre:", A[E][0], "Edad;:", A[E][2])

   else:
       print("No se ecnuetra")
   return E

n = len(nombres)
r=0
while(r!=1):
   print("Ingrese su numero de cuenta")
   cuenta = int(input())
   busquedaAlumno(nombres, n, cuenta)
   print("si desea terminar presione 1, si no culaquier otra tecla")
   r=int(input())
