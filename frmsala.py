from tkinter import *

import tkinter.font as tkFont

import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.salas as rooms
from frmsala import Sala

class Salas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.select_id = -1
        self.master = master        
        self.title("Salas")        
        width=670
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
        GLabel_464["text"] = "Usuarios:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("nombre", "tipo", "capacidad"), name="tvSalas")
        tv.column("#0", width=50)
        tv.column("nombre", width=100, anchor=CENTER)
        tv.column("tipo", width=100, anchor=CENTER)
        tv.column("capacidad", width=90, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("tipo", text="tipo", anchor=CENTER)
        tv.heading("capacidad", text="capacidad", anchor=CENTER)
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
        tvSalas = self.nametowidget("tvSalas")
        current_item = tvSalas.focus()
        if current_item:
            data = tvSalas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Sala(self, True)
        print('agregar')

    def editar(self): 
        Sala(self, True, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar esta sala?")   
        if answer:
            rooms.eliminar(self.select_id)
            self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):        
        tvSalas = self.nametowidget("tvSalas")
        for record in tvSalas.get_children():
            tvSalas.delete(record)
        salas = rooms.listar()
        for room in salas:
            tvSalas.insert("", END, text=room[0], values=(room[1], room[2], room[3]))        
        tvSalas.place(x=10,y=40,width=650,height=300)