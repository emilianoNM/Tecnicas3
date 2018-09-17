
# coding: utf-8

# In[ ]:


def main():
    a_curso = input ("Ingresa el anio en curso: ")
    for i  in range (3):
        nombre = raw_input ("Nombre de la persona: ")
        nacimiento = input ("Anio de nacimiento: ")
        print  nombre, "cumple", (a_curso - nacimiento), "anios en el", a_curso

