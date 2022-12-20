from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.funciones as sesiones
from frmfuncion import Funcion

class Funciones(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.select_id = -1
        self.master = master        
        self.title("Funciones")        
        width=820
        height=350
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Funciones:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("pelicula", "idioma", "sala", "fecha", "hora", "tipo", "clasificacion", "precio"), name="tvFunciones")
        tv.column("#0", width=5)
        tv.column("pelicula", width=100, anchor=CENTER)
        tv.column("idioma", width=30, anchor=CENTER)
        tv.column("sala", width=20, anchor=CENTER)
        tv.column("fecha", width=30, anchor=CENTER)
        tv.column("hora", width=10, anchor=CENTER)
        tv.column("tipo", width=10, anchor=CENTER)
        tv.column("clasificacion", width=10, anchor=CENTER)
        tv.column("precio", width=10, anchor=CENTER)


        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("pelicula", text="Pelicula", anchor=CENTER)
        tv.heading("idioma", text="Idioma", anchor=CENTER)
        tv.heading("sala", text="Sala", anchor=CENTER)
        tv.heading("fecha", text="Fecha", anchor=CENTER)
        tv.heading("hora", text="Hora", anchor=CENTER)
        tv.heading("tipo", text="Tipo", anchor=CENTER)
        tv.heading("clasificacion", text="Clasificación", anchor=CENTER)
        tv.heading("precio", text="Precio", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)          
        
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=430,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=510,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
        
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=590,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar

    def obtener_fila(self, event):
        tvFunciones = self.nametowidget("tvFunciones")
        current_item = tvFunciones.focus()
        if current_item:
            data = tvFunciones.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Funcion(self, True)
        print('agregar')

    def editar(self): 
        Funcion(self, True, self.select_id)
        print('Editar')

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Eliminar esta sala?")   
        if answer:
            sesiones.eliminar(self.select_id)
            self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):        
        tvFunciones = self.nametowidget("tvFunciones")
        for record in tvFunciones.get_children():
            tvFunciones.delete(record)
        funciones = sesiones.listar()
        for funci in funciones:
            tvFunciones.insert("", END, text=funci[0], values=(funci[1], funci[2], funci[3], funci[4], funci[5], funci[6], funci[7], funci[8]))        
        tvFunciones.place(x=10,y=40,width=800,height=300)

#realizado por Humberto Caregua 
