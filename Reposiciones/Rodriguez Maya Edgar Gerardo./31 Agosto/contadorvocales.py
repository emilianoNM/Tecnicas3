###programa para contar vocales

def contar_vocales(cad):
    voc = 0
    for c in cad:
        if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
            voc=voc+1
    return voc


cad = raw_input('')
print contar_vocales(cad)