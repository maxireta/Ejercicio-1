from claseIndicador import indicador
from tkinter import *
from tkinter import ttk

class ventana:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('500x300')
        self.__ventana.title('Calculadora IPC')
        ttk.Label(self.__ventana, text="Item").place(x=20, y=20)
        ttk.Label(self.__ventana, text="Cantidad").place(x=120, y=20)
        ttk.Label(self.__ventana, text="Precio año base").place(x=220, y=20)
        ttk.Label(self.__ventana, text="Precio año actual").place(x=350, y=20)
        ttk.Label(self.__ventana, text="Vestimenta").place(x=20, y=55)
        ttk.Label(self.__ventana, text="Alimentos").place(x=20, y=90)
        ttk.Label(self.__ventana, text="Educación").place(x=20, y=125)
        self.__cantidad = StringVar()
        self.__base = StringVar()
        self.__actual = StringVar()
        self.__ipc = StringVar()
        self.__cantidadv = ttk.Entry(self.__ventana, width= 12, textvariable= self.__cantidad).place(x=110, y=55)
        self.__cantidada = ttk.Entry(self.__ventana, width= 12, textvariable= self.__cantidad).place(x=110, y=90)
        self.__cantidade = ttk.Entry(self.__ventana, width= 12, textvariable= self.__cantidad).place(x=110, y=125)
        self.__basev = ttk.Entry(self.__ventana, width=12, textvariable= self.__base).place(x=225, y=55)
        self.__basea = ttk.Entry(self.__ventana, width=12, textvariable= self.__base).place(x=225, y=90)
        self.__basee = ttk.Entry(self.__ventana, width=12, textvariable= self.__base).place(x=225, y=125)
        self.__actualv = ttk.Entry(self.__ventana, width=12, textvariable= self.__actual).place(x=357, y=55)
        self.__actuala = ttk.Entry(self.__ventana, width=12, textvariable= self.__actual).place(x=357, y=90)
        self.__actuale = ttk.Entry(self.__ventana, width=12, textvariable= self.__actual).place(x=357, y=125)
        ttk.Button(self.__ventana, text="Salir", command= self.__ventana.destroy).place(x=270, y=200)
        ttk.Button(self.__ventana, text="Calcular IPC", command= self.calcular).place(x=110, y=200)
        ttk.Label(self.__ventana, text="IPC %").place(x=30, y=250)
        ttk.Label(self.__ventana, text= "%").place(x=100, y=250)
        ttk.Label(self.__ventana, textvariable= self.__ipc).place(x=70, y=250)
        self.__ventana.mainloop()
    def calcular(self):
        cantidad = int(self.__cantidad.get())
        base = float(self.__base.get())
        actual = float(self.__actual.get())
        fua = indicador(cantidad, base, actual)
        a = fua.calcular()
        self.__ipc.set(a)