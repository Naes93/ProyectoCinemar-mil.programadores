import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.peliculas as movies
import bll.roles as rol

class Pelicula(tk.Toplevel):
    def __init__(self, master=None, isAdmin = False, id_pelicula = None):
        super().__init__(master)
        self.master = master 
        self.id_pelicula = id_pelicula 
        #setting title
        self.title("Película")
        #setting window size
        width=450
        height=260
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_22=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_22["font"] = ft
        GLabel_22["fg"] = "#333333"
        GLabel_22["justify"] = "right"
        GLabel_22["text"] = "Nombre de la Película:"
        GLabel_22.place(x=10,y=40,width=130,height=25)

        GLineEdit_204=tk.Entry(self, name="txtNombre")
        GLineEdit_204["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_204["font"] = ft
        GLineEdit_204["fg"] = "#333333"
        GLineEdit_204["justify"] = "left"
        GLineEdit_204["text"] = ""
        GLineEdit_204.place(x=150,y=40,width=290,height=30)

        GLabel_20=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_20["font"] = ft
        GLabel_20["fg"] = "#333333"
        GLabel_20["justify"] = "right"
        GLabel_20["text"] = "Genero:"
        GLabel_20.place(x=70,y=80,width=70,height=25)

        GLineEdit_610=tk.Entry(self, name="txtGenero")
        GLineEdit_610["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_610["font"] = ft
        GLineEdit_610["fg"] = "#333333"
        GLineEdit_610["justify"] = "left"
        GLineEdit_610["text"] = ""
        GLineEdit_610.place(x=150,y=80,width=290,height=30)

        GLabel_555=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_555["font"] = ft
        GLabel_555["fg"] = "#333333"
        GLabel_555["justify"] = "right"
        GLabel_555["text"] = "Idioma:"
        GLabel_555.place(x=70,y=120,width=70,height=25)

        GLineEdit_371=tk.Entry(self, name="txtIdioma")
        GLineEdit_371["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_371["font"] = ft
        GLineEdit_371["fg"] = "#333333"
        GLineEdit_371["justify"] = "left"
        GLineEdit_371["text"] = ""
        GLineEdit_371.place(x=150,y=120,width=290,height=30)

        GLabel_770=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_770["font"] = ft
        GLabel_770["fg"] = "#333333"
        GLabel_770["justify"] = "right"
        GLabel_770["text"] = "Clasificación:"
        GLabel_770.place(x=70,y=160,width=70,height=25)

        cb_clasificacion = ttk.Combobox(self, state="readonly", values=["ATP", "+13", "+16", "+18"], name="cbclasificacion")
        cb_clasificacion.place(x=150,y=160,width=70,height=30)

        GButton_258=tk.Button(self)
        GButton_258["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_258["font"] = ft
        GButton_258["fg"] = "#000000"
        GButton_258["justify"] = "center"
        GButton_258["text"] = "Aceptar"
        GButton_258.place(x=260,y=210,width=70,height=25)
        GButton_258["command"] = self.aceptar

        GButton_529=tk.Button(self)
        GButton_529["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_529["font"] = ft
        GButton_529["fg"] = "#000000"
        GButton_529["justify"] = "center"
        GButton_529["text"] = "Cancelar"
        GButton_529.place(x=350,y=210,width=70,height=25)
        GButton_529["command"] = self.cancelar

        if id_pelicula is not None:
            pelicula = movies.obtener_id(id_pelicula)
            if pelicula is None:
                tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos de la sala, reintente nuevamente")
                self.destroy()
            else:
                GLineEdit_204.insert(0, pelicula[0])
                GLineEdit_610.insert(0, pelicula[1])
                GLineEdit_371.insert(0, pelicula[2])
                cb_clasificacion.set(pelicula[3])

    def get_value(self, name):
        return self.nametowidget(name).get()
    
    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def aceptar(self):
        try:            
            nombrepelicula = self.get_value("txtNombre")            
            genero = self.get_value("txtGenero")  
            idioma = self.get_value("txtIdioma")
            clasificacion = self.get_value("cbclasificacion")
            #print (clasificacion)

            # TODO validar los datos antes de ingresar
            if not movies.existe(nombrepelicula):
                movies.agregar(nombrepelicula, genero, idioma, clasificacion)
                tkMsgBox.showinfo(self.master.title(), "Pelicula agregada!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()                
            else:
                print("Actualizacion de pelicula")
                movies.actualizar(self.id_pelicula, nombrepelicula, genero, idioma, clasificacion) 
                #print (tiposala)
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))


    def cancelar(self):
        self.destroy()
        #print("command")

