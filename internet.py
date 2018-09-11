Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
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