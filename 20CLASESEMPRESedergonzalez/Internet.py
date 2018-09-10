
# coding: utf-8

# In[ ]:


class Contacto(object):
    def __init__(self, PaginaOficial, Facebook, Twitter, LinkedIn, Youtube, Instagram , WhatsApp, Telefono):
        self.PaginaOficial=PaginaOficial
        self.Facebook=Facebook
        self.Twitter=Twitter
        self.LinkedIn=LinkedIn
        self.Youtube=Youtube
        self.Instagram=Instagram
        self.WhatsApp=WhatsApp
        self.Telefono=Telefono

class PaginaOficial(object):
    def __init__(self, url, Creacion, experacion, Imagenes, Creador, Actilizacion):
        self.url=url
        self.Creacion=Creacion
        self.experacion=experacion
        self.Imagenes=Imagenes
        self.Creador=Creador
        self.Actilizacion=Actilizacion

