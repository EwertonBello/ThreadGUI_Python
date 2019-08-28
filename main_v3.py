from tkinter import *
import minha_thread as mt

t1 = mt.minhaThread(1)

class App:
    def __init__(self, master=None):
        self.fonte = ("Comic Sans MS", "10", "bold")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()       
     
  
        self.titulo = Label(self.primeiroContainer, text="Parar Loop")
        self.titulo["font"] = ("Arial", "14", "bold")
        self.titulo.pack()     

        self.parar = Button(self.segundoContainer)
        self.parar["text"] = "Parar"
        self.parar["font"] = ("Arial", "11")
        self.parar["width"] = 12
        self.parar["command"] = self.pararLoop
        self.parar.pack()
  

    def pararLoop(self):
        print("Parando...")
        t1.setTeste(False)
  
root = Tk()
App(root)
root.mainloop()
