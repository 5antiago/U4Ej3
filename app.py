import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from datetime import datetime
from dolar import Dolar


class App(tk.Tk):
    __cotizaciones = Dolar
    def __init__(self):
        self.__cotizaciones = Dolar()
        self.__cotizaciones.actualizar()
        super().__init__()
        self.title("Tipos de cambio")
        self.geometry("500x600")
        self.config(padx=10, pady=10)
        self.__oficial= tk.StringVar()
        self.__oficialc= tk.StringVar()
        self.__blue= tk.StringVar()
        self.__bluec= tk.StringVar()
        self.__liqui= tk.StringVar()
        self.__liquic= tk.StringVar() 
        self.__mep= tk.StringVar()
        self.__mepc= tk.StringVar()
        self.__dolar= tk.StringVar()
        self.__dolarc = tk.StringVar()
        self.__ultact= tk.StringVar()
        self.__fuentelb = Font(family="Times New Roman", size=18)
        self.__fuenteprecios= Font(family="Times New Roman", size=20)

        #Creando Elementos
        self.__frameoficial = ttk.Frame(self, padding="3 3 5 5")
        self.__frameoficial["relief"] = "sunken"
        self.__framedolar = ttk.Frame(self, padding= "3 3 5 5")
        self.__framedolar["relief"] = "sunken"
        self.__frameblue = ttk.Frame(self, padding= "3 3 5 5")
        self.__frameblue["relief"] = "sunken"
        self.__framemep= ttk.Frame(self, padding="3 3 5 5")
        self.__framemep["relief"] = "sunken"
        self.__frameliqui = ttk.Frame(self, padding="3 3 5 5")
        self.__frameliqui["relief"] = "sunken"
        self.__frameactu = ttk.Frame(self, padding="3 3 5 5")
        self.__frameactu["relief"] = "sunken"
        self.__lbof=ttk.Label(self.__frameoficial, text="Dólar Oficial", font=self.__fuentelb)
        self.__lbpof=ttk.Label(self.__frameoficial, textvariable= self.__oficial, font=self.__fuenteprecios)
        self.__lbblue= ttk.Label(self.__frameblue, text="Dólar Blue", font=self.__fuentelb)
        self.__lbpblue=ttk.Label(self.__frameblue, textvariable=self.__blue, font=self.__fuenteprecios)
        self.__lbdolar= ttk.Label(self.__framedolar, text="Dólar", font=self.__fuentelb)
        self.__lbpdolar=ttk.Label(self.__framedolar, textvariable=self.__dolar, font=self.__fuenteprecios)
        self.__lbmep= ttk.Label(self.__framemep, text ="Dólar Bolsa", font=self.__fuentelb)
        self.__lbpmep=ttk.Label(self.__framemep, textvariable=self.__mep, font=self.__fuenteprecios)
        self.__lbliqui=ttk.Label(self.__frameliqui, text="Dolar Liqui", font=self.__fuentelb)
        self.__pliqui=ttk.Label(self.__frameliqui, textvariable=self.__liqui, font=self.__fuenteprecios)
        self.__lbinfo=ttk.Label(self.__frameactu, text="Ultima actualización", font=Font(family="Times New Roman", size=12))
        self.__lbactualizacion= ttk.Label(self.__frameactu, textvariable=self.__ultact, font=Font(family="Times New Roman", size=10))
        self.__btnact= ttk.Button(self.__frameactu, text="Actualizar", command=self.actualiza)
        
        #ubicando elementos
            
        #Dolar Oficial
        self.__frameoficial.place(anchor=tk.NW,  relwidth=0.49, relheight=0.3, relx=0)
        self.__lbof.place( anchor=tk.CENTER, relwidth = 0.57, relheight= 0.2, relx=0.5, rely=0.2)
        self.__lbpof.pack(fill="x")
        self.__lbpof.place(anchor=tk.CENTER, relheight= 0.5, relx=0.5, rely=0.6)

        #Dolar 
        self.__framedolar.place(anchor= tk.NE, relwidth=0.49, relheight=0.3, relx= 1)
        self.__lbdolar.place(anchor = tk.CENTER, relwidth= 0.28, relheight= 0.2, relx=0.5, rely = 0.2)
        self.__lbpdolar.pack(fill="x")
        self.__lbpdolar.place(anchor=tk.CENTER, relheight=0.5, relx=0.5, rely=0.6)

        #Dolar Blue
        self.__frameblue.place(anchor= tk.W, relwidth=0.49, relheight=0.3, relx=0, rely=0.47)
        self.__lbblue.place(anchor= tk.CENTER, relwidth = 0.5, relheight = 0.2, relx=0.5, rely=0.2)
        self.__lbpblue.pack(fill="x")
        self.__lbpblue.place(anchor=tk.CENTER, relheight= 0.5, relx=0.5, rely=0.6 )

        #Dolar Bolsa
        self.__framemep.place(anchor= tk.E, relwidth=0.49, relheight=0.3, relx=1, rely=0.47)
        self.__lbmep.place(anchor = tk.CENTER, relwidth = 0.52, relheight=0.2, relx=0.5, rely=0.2)
        self.__lbpmep.pack(fill="x")
        self.__lbpmep.place(anchor=tk.CENTER, relheight=0.5, relx=0.5, rely=0.6)
        #Dolar Contado con liqui
        self.__frameliqui.place(anchor= tk.CENTER, relwidth=0.49, relheight=0.3, relx=0.245, rely=0.795)
        self.__lbliqui.place(anchor=tk.CENTER, relwidth=0.51, relheight=0.2, relx=0.5, rely= 0.2)
        self.__pliqui.pack(fill="x")
        self.__pliqui.place(anchor=tk.CENTER, relheight=0.5, relx=0.5, rely=0.6)

        #Frame informativo
        self.__frameactu.place(anchor= tk.CENTER, relwidth=0.49, relheight=0.3, relx=0.755, rely = 0.795)
        self.__lbinfo.place(anchor= tk.CENTER, relwidth=0.55, relheight= 0.2, relx=0.5, rely=0.2)
        self.__lbactualizacion.place(anchor=tk.CENTER, relwidth= 0.46, relheight = 0.2, relx= 0.5, rely=0.4)
        self.__btnact.place(anchor=tk.CENTER, relwidth= 0.3, relheight= 0.2, relx=0.5, rely=0.7)

    def actualiza(self):
        for aux in self.__cotizaciones.obtener():
            if aux["nombre"] == "Dolar Oficial":
                self.__oficial.set("Venta:" +aux["venta"] + "\nCompra: " + aux["compra"])
            elif aux["nombre"] == "Dolar Blue":
                self.__blue.set("Venta: "+aux["venta"]+ "\nCompra: " + aux["compra"])
            elif aux["nombre"] == "Dolar Contado con Liqui":
                self.__liqui.set("Venta: "+aux["venta"]+ "\nCompra: " + aux["compra"])
            elif aux["nombre"] == "Dolar Bolsa":
                self.__mep.set("Venta: "+aux["venta"]+ "\nCompra: " + aux["compra"])
            elif aux["nombre"] == "Dolar":
                self.__dolar.set("Venta: "+aux["venta"]+ "\nCompra: " + aux["compra"])
        self.__ultact.set(datetime.now().strftime('%d - %m - %Y, %H:%M'))