from tkinter import *
from views.coches_view import CochesView
from controllers.coches_controller import CochesController

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.coches_view = CochesView(ventana)


if __name__=="__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()
