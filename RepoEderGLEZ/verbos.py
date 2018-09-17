
# coding: utf-8

# In[ ]:


pronombre = ['yo','tu','el','nosotros','ustedes','ellos']

terminaciones = {'yo':'o',
                 'tu':'as',
                 'el':'a',
                 'nosotros':'amos',
                 'ustedes':'en',
                 'ellos':'an'}

palabra = raw_input('Verbo regular 1ra. conjugacion: ')

for i in pronombre:
    print i, palabra[0:len(palabra)-2] + terminaciones[i]

