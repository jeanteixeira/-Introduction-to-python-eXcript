from Tkinter import *

top = Frame()
top.pack()
rotulo = Label(top,text="Rotulo Exemplo",foreground="blue")
rotulo.pack()
rotulo.configure(relief="ridge", font="Arial 24 bold",border=5, background="yellow")

mainloop()
