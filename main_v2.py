import tkinter as tk
import minha_thread as mt

t1 = mt.minhaThread(1)

root = tk.Tk()

canvas = tk.Canvas(root, width = 200, height = 200)
canvas.pack()

def pararLoop():
    print("Parando...")
    t1.setTeste(False)
        
btnParar = tk.Button (root, text='Parar loop',command=pararLoop)
canvas.create_window(100, 100, window=btnParar)
  
root.mainloop()