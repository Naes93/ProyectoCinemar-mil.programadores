from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.pelidb as pelidb
from agregarpelis import Agregarpelis


class Peliculas(Toplevel):
    def __init__(self, master = None, pelis_id = None):
        super().__init__(master)        
        self.master = master
        self.pelis_id = pelis_id   
        self.title("Listado de Peliculas")        
        width=800
        height=500
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
        GLabel_464["text"] = "Peliculas:"
        GLabel_464.place(x=10,y=10,width=70,height=25)


       
        ### TABLA ###############
        tabla = ttk.Treeview(self, columns=('col1', 'col2', 'col3', 'col4'), name="tabla")

        tabla.place(
            x=30,
            y=70,
         width=670.0,
         height=379.0
        )

        ##### COLUMNAS ##########
        tabla.column('#0', width=30)
        tabla.column('col1', width=75)
        tabla.column('col2', width=50)
        tabla.column('col3', width=50)
        tabla.column('col4', width=100)
       
        tabla.heading('#0', text='IdPelis')
        tabla.heading('col1', text='Nombre_pelicula')
        tabla.heading('col2', text='Categorias')
        tabla.heading('col3', text='Sala')
        tabla.heading('col4', text='Hs_funcion')

        #registros = pelidb.listar()
        #for fila in registros:
            #tabla.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3],  fila[4])) 
       

        #registros = pelidb.agregar()
        #for fila in registros:
            #tabla.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3],  fila[4])) 
            
        tabla.bind("<<TreeviewSelect>>", self.obtener_fila)


###################################
        self.refrescar()

        ft = tkFont.Font(family='Times',size=10)
        btn_agregar = Button(self)
        btn_agregar["bg"] = "#f0f0f0"        
        btn_agregar["font"] = ft
        btn_agregar["fg"] = "#000000"
        btn_agregar["justify"] = "center"
        btn_agregar["text"] = "Agregar"
        btn_agregar.place(x=530,y=10,width=70,height=25)
        btn_agregar["command"] = self.agregar

        btn_editar = Button(self)
        btn_editar["bg"] = "#f0f0f0"        
        btn_editar["font"] = ft
        btn_editar["fg"] = "#000000"
        btn_editar["justify"] = "center"
        btn_editar["text"] = "Editar"
        btn_editar.place(x=610,y=10,width=70,height=25)
        btn_editar["command"] = self.editar
      
        btn_eliminar = Button(self)
        btn_eliminar["bg"] = "#f0f0f0"        
        btn_eliminar["font"] = ft
        btn_eliminar["fg"] = "#000000"
        btn_eliminar["justify"] = "center"
        btn_eliminar["text"] = "Eliminar"
        btn_eliminar.place(x=690,y=10,width=70,height=25)
        btn_eliminar["command"] = self.eliminar
        

    def obtener_fila(self, event):
        print("estoy en obtener fila")
        tabla = self.nametowidget("tabla")
        current_item = tabla.focus()
        print(current_item, "estoy en current")
        if current_item:
            data = tabla.item(current_item)
            print(data, "estoy en data")
            self.pelis_id = int(data["text"])
        else:
            self.pelis_id = -1

    def agregar(self):
        Agregarpelis(self, True)

    def editar(self): 
        Agregarpelis(self,  True, self.pelis_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
        if answer:
            pelidb.eliminar(self.pelis_id)
            self.refrescar()

    # https://www.youtube.com/watch?v=n0usdtoU5cE
    def refrescar(self):        
        tabla = self.nametowidget("tabla")
        for record in tabla.get_children():
            tabla.delete(record)
        registro = pelidb.listar()
        for fila in registro:
            tabla.insert("", END, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4])) 
