from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.peliculas as movies
from frmpelicula import Pelicula

class Peliculas(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.select_id = -1
        self.master = master        
        self.title("Peliculas")        
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

        tv = ttk.Treeview(self, columns=("nombre", "genero", "idioma", "clasificacion"), name="tvPeliculas")
        tv.column("#0", width=5)
        tv.column("nombre", width=140, anchor=CENTER)
        tv.column("genero", width=90, anchor=CENTER)
        tv.column("idioma", width=70, anchor=CENTER)
        tv.column("clasificacion", width=50, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("genero", text="Genero", anchor=CENTER)
        tv.heading("idioma", text="Idioma", anchor=CENTER)
        tv.heading("clasificacion", text="Clasificacion", anchor=CENTER)
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
        tvPeliculas = self.nametowidget("tvPeliculas")
        current_item = tvPeliculas.focus()
        if current_item:
            data = tvPeliculas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1

    def agregar(self):
        Pelicula(self, True)
        print('agregar')

    def editar(self): 
        Pelicula(self, True, self.select_id)
        print('Editar')

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar esta sala?")   
        if answer:
            movies.eliminar(self.select_id)
            self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):        
        tvPeliculas = self.nametowidget("tvPeliculas")
        for record in tvPeliculas.get_children():
            tvPeliculas.delete(record)
        peliculas = movies.listar()
        for movie in peliculas:
            tvPeliculas.insert("", END, text=movie[0], values=(movie[1], movie[2], movie[3], movie[4]))        
        tvPeliculas.place(x=10,y=40,width=650,height=300)