from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.pelidb as pelidb
import bll.roles as rol

import tkinter as tk

class Agregarpelis(tk.Toplevel):
    def __init__(self, master=None, isAdmin = False, peli_id = None):        
        super().__init__(master)
        self.master = master
        self.peli_id = peli_id       
        self.title("Agregar Pelicula")        
        width=443
        height=423
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLabel_243 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#333333"
        GLabel_243["anchor"] = "e"
        GLabel_243["text"] = "Nombre:"
        GLabel_243.place(x=10,y=10,width=124,height=30)

        GLineEdit_871 = Entry(self, name="txtNombre")
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "left"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=140,y=10,width=284,height=30)

        GLabel_599 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#333333"
        GLabel_599["anchor"] = "e"
        GLabel_599["text"] = "Categoria:"
        GLabel_599.place(x=10,y=50,width=122,height=30)

        GLineEdit_911 = Entry(self, name="txtCategoria")
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = ""
        GLineEdit_911.place(x=140,y=50,width=285,height=30)        

        GLabel_600 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["anchor"] = "e"
        GLabel_600["text"] = "Sala:"
        GLabel_600.place(x=10,y=90,width=123,height=30)

        GLineEdit_208 = Entry(self, name="txtSala")
        GLineEdit_208["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_208["font"] = ft
        GLineEdit_208["fg"] = "#333333"
        GLineEdit_208["justify"] = "left"
        GLineEdit_208["text"] = ""
        GLineEdit_208.place(x=140,y=90,width=94,height=30)

        GLabel_737 = Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["anchor"] = "e"
        GLabel_737["text"] = "Hs_funcion:"
        GLabel_737.place(x=10,y=130,width=121,height=30)

        GLineEdit_234 = Entry(self, name="txtHs_funcion")
        GLineEdit_234["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_234["font"] = ft
        GLineEdit_234["fg"] = "#333333"
        GLineEdit_234["justify"] = "left"
        GLineEdit_234["text"] = ""
        GLineEdit_234.place(x=140,y=130,width=133,height=30)

 
        GButton_825 = Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=270,y=370,width=70,height=25)
        GButton_825["command"] = self.aceptar
        
        GButton_341 = Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=350,y=370,width=70,height=25)
        GButton_341["command"] = self.GButton_341_command

        if peli_id is not None:
            peilicula = pelidb.obtener_id(peli_id)
            print(peilicula, "estoy aca")
            if peilicula is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_871.insert(0, peilicula[1])
                GLineEdit_911.insert(0, peilicula[2])
                #fecha_nac = date(int(peilicula[3][:4]), int(peilicula[3][5:7]), int(peilicula[3][8:]))
                GLineEdit_208.insert(0, peilicula[3])
                GLineEdit_234.insert(0, peilicula[4])
                #GLineEdit_384.insert(0, peilicula[5])
                #GLineEdit_481.insert(0, peilicula[6])
                #GLineEdit_481["state"] = "disabled"           
                #cb_roles.set(peilicula[8])
########################
    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def aceptar(self):
        #try:            
            nombre = self.get_value("txtNombre")
            categorias = self.get_value("txtCategoria")            
            sala = self.get_value("txtSala")            
            hs_funcion = self.get_value("txtHs_funcion")
            #email = self.get_value("txtEmail")            
            #usuario = self.get_value("txtUsuario")

            #contrasenia = self.get_value("txtContrasenia")            
            #confirmacion = self.get_value("txtConfirmacion")
            #rol_id = self.get_index("cbRoles")

            # TODO validar los datos antes de ingresar
            #if nombre == "":
            #    tkMsgBox.showerror(self.master.title(), "Nombre es un valor requerido.")
            #    return
            
            #if categorias == "":
            #    tkMsgBox.showerror(self.master.title(), "Categorias es un valor requerido.")
           #     return
            
            # agregar los demas
            # .....
            
            #if contrasenia != confirmacion:
            #    tkMsgBox.showerror(self.master.title(), "La contraseña con su confirmacion no tienen el mismo valor.")
            #    return  
#####################
            if self.peli_id is None:
                print("Alta de pelicula")
                if not pelidb.existe(nombre):
                    pelidb.agregar(nombre, categorias, sala, hs_funcion)
                    tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                    try:
                        self.master.refrescar()
                    except Exception as ex:
                        print(ex)
                    self.destroy()                
                else:
                    tkMsgBox.showwarning(self.master.title(), "Pelicula existente en nuestros registros")
            else:
                print("Actualizacion de pelicula")
                pelidb.actualizar(nombre, categorias, sala, hs_funcion, self.peli_id)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Pelicula modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        #except Exception as ex:
         #   tkMsgBox.showerror(self.master.title(), str(ex))