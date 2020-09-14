import matplotlib.pyplot as plt 
import numpy as np
import urllib.request
import json
import tkinter 
import PIL 

url = "https://api.sunat.cloud/cambio/2020"
uh = urllib.request.urlopen(url)
data = uh.read().decode()
js = json.loads(data)

Fecha = list()
Pcompra = list()
Pventa = list()


for entry in reversed(js):
    Fecha.append(entry)
    Pcompra.append(float(js[entry]["compra"]))
    Pventa.append(js[entry]["venta"])
    
dias = -(15)
semanas = np.array(Fecha[dias:])
csemanas = np.array(Pcompra[dias:])

root = tkinter.Tk()
root.title('Tipo de Cambio')
root.geometry('200x50')

def graph():
    plt.plot(semanas, csemanas)
    plt.xticks(semanas, rotation = 'vertical')
    plt.margins(0.1)
    plt.show()

my_button = tkinter.Button(root, text = "Grafico Tipo de cambio", command = graph)
my_button.pack()

root.mainloop()





