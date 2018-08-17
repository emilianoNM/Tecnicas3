
# coding: utf-8

# In[ ]:


Actividad 1

Dron
float Peso
string Color
int Piezas
int tamaño
void Vuelo()
void Fotografia()
float getPeso()
void setPeso()
string getColor()
void setColor()
string getPiezas()
void setPiezas()

Actividad 2
Clase Dron

namespace VANT
{
    class Dron
    {
        private int piezas;
        private string color;
        private int tamaño;
        private float peso;

        public Boolean sinbateria = false;
        public int Piezas {get => piezas; set => piezas = value;}
        public string Color {get => color; set => color = value;}
        public int Peso {get => peso; set => peso = value;}
        public int Tamaño {get => tamaño; set => tamaño = value;}

        enum TiposDeDrones {Carrera, Fotografia, Riego}
        public Dron(string color, int peso)
        {
           peso = pesoDelDron;
           tamaño = tamañoDelDron;
        }

        public Dron()
        {
        }
        public Boolean vuelo(int mint)
        {
            int tiempodevuelo = 10;
            if (mint > tiempodevuelo)
                return true;
            else
                return false;
        }

        public bool grabar(bool bateriacargada)
        {
            if (bateriacargada)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        void foto()
        {
        }
        void video()
        {
        }

        public bool tipos(int tipoDeDrones)
        {
            switch (tipoDeDrones)
            {
                case (int)TiposDeDrones.Carrera:
                    return false;
                    break;
                case (int)TiposDeDrones.Fotografia:
                    return true;
                    break;
                case (int)TiposDeDrones.Riego:
                    return true;
                    break;
                default:
                    return false;
                    break;
            }                                  
        }
    }
}

