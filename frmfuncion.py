import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.peliculas as movies
import bll.funciones as sesiones
from datetime import date

class Funcion(tk.Toplevel):
    def __init__(self, master=None, isAdmin = False, id_funcion = None):
        super().__init__(master)
        self.master = master 
        self.id_funcion = id_funcion 
        #setting title
        self.title("Función")
        #setting window size
        width=280
        height=258
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_131=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_131["font"] = ft
        GLabel_131["fg"] = "#333333"
        GLabel_131["justify"] = "right"
        GLabel_131["text"] = "Película:"
        GLabel_131.place(x=10,y=20,width=70,height=25)

        peli = dict(sesiones.listar_peliculas())

        cb_Peliculas = ttk.Combobox(self, state="readonly", values=list(peli.values()), name="cbPelicula")
        cb_Peliculas.set(peli[1])
        cb_Peliculas.place(x=90,y=20,width=140,height=30)

        GLabel_358=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_358["font"] = ft
        GLabel_358["fg"] = "#333333"
        GLabel_358["justify"] = "right"
        GLabel_358["text"] = "Sala:"
        GLabel_358.place(x=10,y=60,width=70,height=25)

        sala = dict(sesiones.listar_salas())

        cb_Salas = ttk.Combobox(self, state="readonly", values=list(sala.values()), name="cbSala")
        cb_Salas.set(sala[1])
        cb_Salas.place(x=90,y=55,width=140,height=30)

        GLabel_861=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_861["font"] = ft
        GLabel_861["fg"] = "#333333"
        GLabel_861["justify"] = "right"
        GLabel_861["text"] = "Fecha:"
        GLabel_861.place(x=10,y=95,width=70,height=25)

        GLabel_357=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_357["font"] = ft
        GLabel_357["fg"] = "#333333"
        GLabel_357["justify"] = "right"
        GLabel_357["text"] = "Hora:"
        GLabel_357.place(x=10,y=140,width=70,height=25)

        GLineEdit_125=tk.Entry(self, name="txtFecha")
        GLineEdit_125["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_125["font"] = ft
        GLineEdit_125["fg"] = "#333333"
        GLineEdit_125["justify"] = "left"
        GLineEdit_125["text"] = ""
        GLineEdit_125.place(x=90,y=90,width=140,height=30)

        GLineEdit_765=tk.Entry(self, name="txtHora")
        GLineEdit_765["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_765["font"] = ft
        GLineEdit_765["fg"] = "#333333"
        GLineEdit_765["justify"] = "left"
        GLineEdit_765["text"] = ""
        GLineEdit_765.place(x=90,y=130,width=140,height=30)

        GLabel_300=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_300["font"] = ft
        GLabel_300["fg"] = "#333333"
        GLabel_300["justify"] = "right"
        GLabel_300["text"] = "Precio:"
        GLabel_300.place(x=10,y=185,width=70,height=25)

        GLineEdit_700=tk.Entry(self, name="txtPrecio")
        GLineEdit_700["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_700["font"] = ft
        GLineEdit_700["fg"] = "#333333"
        GLineEdit_700["justify"] = "left"
        GLineEdit_700["text"] = ""
        GLineEdit_700.place(x=90,y=170,width=140,height=30)

        GButton_812=tk.Button(self)
        GButton_812["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_812["font"] = ft
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Cancelar"
        GButton_812.place(x=190,y=210,width=70,height=25)
        GButton_812["command"] = self.cancelar

        GButton_420=tk.Button(self)
        GButton_420["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_420["font"] = ft
        GButton_420["fg"] = "#000000"
        GButton_420["justify"] = "center"
        GButton_420["text"] = "Aceptar"
        GButton_420.place(x=100,y=210,width=70,height=25)
        GButton_420["command"] = self.aceptar


        if id_funcion is not None:
            funcion = sesiones.obtener_id(id_funcion)
            if funcion is None:
                tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de la función, reintente nuevamente")
                self.destroy()
            else:
                # TODO bloquear el campo usuario
                cb_Peliculas.set(funcion[1])
                cb_Salas.set(funcion[3])
                GLineEdit_125.insert(0, funcion[4]) # TODO corregir formato de fecha
                #fecha = date(int(funcion[4][:4]), int(funcion[4][5:7]), int(funcion[4][8:]))
                #GLineEdit_125.insert(0, fecha.strftime(r"%d/%m/%Y"))
                GLineEdit_765.insert(0, funcion[5])
                GLineEdit_700.insert(0, funcion[8])

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def cancelar(self):
        self.destroy()

    def aceptar(self):
        try:            
            id_pelicula = self.get_index("cbPelicula")
            sala = self.get_index("cbSala")            
            fecha = self.get_value("txtFecha")            
            hora = self.get_value("txtHora")
            precio = self.get_value("txtPrecio")

            if fecha == "":
                tkMsgBox.showerror(self.master.title(), "La fecha es un valor requerido.")
                return

            if fecha == "":
                tkMsgBox.showerror(self.master.title(), "La hora es un valor requerido.")
                return

            if fecha == "":
                tkMsgBox.showerror(self.master.title(), "El precio es un valor requerido.")
                return

            if not sesiones.existe(id_pelicula, sala, fecha, hora): #no ternima de funcionar bien
                sesiones.agregar(fecha, hora, sala, id_pelicula, precio)
                tkMsgBox.showinfo(self.master.title(), "Función agregada!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()                
            else:
                print("Actualizacion de función")
                sesiones.actualizar(self.id_funcion, fecha, hora, sala, id_pelicula, precio)  # TODO ver que no esta cargando bien
                tkMsgBox.showinfo(self.master.title(), "funcion modificada!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))




