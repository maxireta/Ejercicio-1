from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Aplicacion():
    __ventana=None
    __cantidad:None
    __precioBase: None
    __precioActual: None
    __vestimenta: None
    __alimentos: None
    __educacuon: None
 
    def __init__(self):        
        self.__ventana= Tk()
        self.__ventana.geometry('400x250')
        self.__ventana.configure(bg='lightgrey')
        self.__ventana.title('Calculadora IPC')
   
        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__cantidad = StringVar()
        self.__precioBase = StringVar()
        self.__precioActual = StringVar()
        self.__vestimenta = StringVar()
        self.__alimentos = StringVar()
        self.__educacuon = StringVar()
        ttk.Label(mainframe, text="Item  ").grid(column=1, row=0, sticky=W)
        ttk.Label(mainframe, text="  Cantidad ").grid(column=2, row=1, sticky=W)
        cantidadEntry = ttk.Entry(mainframe, width=7, textvariable=self.__cantidad)
        cantidadEntry.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(mainframe, text=" Precio Año Base ").grid(column=3, row=1, sticky=W)
        precioBaseEntry = ttk.Entry(mainframe, width=7, textvariable=self.__precioBase)
        precioBaseEntry.grid(column=3, row=2, sticky=(W, E))

        precioBaseEntry = ttk.Entry(mainframe, width=7, textvariable=self.__precioBase)
        precioBaseEntry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(mainframe, text=" Precio Año Actual ").grid(column=4, row=1, sticky=W)
        precioActualEntry = ttk.Entry(mainframe, width=7, textvariable=self.__precioActual)
        precioActualEntry.grid(column=4, row=2, sticky=(W, E))
        precioActualEntry = ttk.Entry(mainframe, width=7) #, textvariable=self.__precioActual) acá pongo en donde voy a almacenar ese dato
        precioActualEntry.grid(column=4, row=3, sticky=(W, E))
        precioActualEntry = ttk.Entry(mainframe, width=7)#, textvariable=self.__precioActual) acá pongo en donde voy a almacenar ese dato
        precioActualEntry.grid(column=4, row=4, sticky=(W, E))

        ttk.Label(mainframe, text="Vestimenta ").grid(column=1, row=2, sticky=W)
        vestimentaEntry = ttk.Entry(mainframe, width=7, textvariable=self.__vestimenta)
        vestimentaEntry.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(mainframe, text="Alimentos ").grid(column=1, row=3, sticky=W)
        alimentosEntry = ttk.Entry(mainframe, width=7, textvariable=self.__alimentos)
        alimentosEntry.grid(column=3, row=2, sticky=(W, E))

        ttk.Label(mainframe, text="Educación ").grid(column=1, row=4, sticky=W)
        educacionEntry = ttk.Entry(mainframe, width=7, textvariable=self.__educacuon)
        educacionEntry.grid(column=3, row=3, sticky=(W, E))
        educacionEntry = ttk.Entry(mainframe, width=7 )#, textvariable=self.__educacuon) acá pongo en donde voy a almacenar ese dato
        educacionEntry.grid(column=3, row=4, sticky=(W, E))


        ttk.Button(mainframe, text="Calcular IPC", command=self.calcular).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=4, row=6, sticky=W)

        ttk.Label(mainframe, text="IPC %   ").grid(column=1, row=7, sticky=W)
        
        for child in mainframe.winfo_children():
             child.grid_configure(padx=5, pady=5)

        self.__ventana.mainloop()

    def calcular(self):
        try:            
            precioActual = float(self.__precioActual.get())
            precioBase = float(self.__precioBase.get())
            cant= int(self.__cantidad.get())
            ipc = ((precioActual * cant) / (precioBase* cant)) * 100
            print(f"IPC: {ipc}")
        
        except ValueError:
            messagebox.showerror(title='Error', message='Ingrese un valor numérico')

def testAPP():
    mi_app = Aplicacion()


if __name__ == '__main__':
    testAPP()
  