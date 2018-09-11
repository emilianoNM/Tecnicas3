
class Patron():
    
    def __init__(self):
        self.patron = []
        
    def lectorPatron(self):
        archivo = open("patron.txt","r")
        for x in archivo.readlines():
            print (x)
        archivo.close()