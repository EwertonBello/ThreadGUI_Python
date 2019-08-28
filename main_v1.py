import minha_thread as mt
from tkinter import messagebox

t1 = mt.minhaThread(1)

msg = 'no'
while msg == 'no':
	msg = messagebox.askquestion ('Thread Teste','Você deseja parar o loop?',icon = 'warning')
	
if msg == 'yes':
	print("Parando...")
	t1.setTeste(False)