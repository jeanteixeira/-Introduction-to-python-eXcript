from Tkinter import *
c = Canvas()
c.pack()

def novalinha(e):
	x,y = c.canvasx(e.x), c.canvasy(e.y)
	c.create_line(x,y,x,y,tags="corrente")

def estendelinha(e):
	x,y = c.canvasx(e.x), c.canvasy(e.y)
	coords = c.coords("corrente") + [x,y]
	c.coords("corrente",*coords)

def fechalinha(e): c.itemconfig("corrente",tags=())

c.bind("<Button-1>", novalinha)
c.bind("<B1-Motion>", estendelinha)
c.bind("<ButtonRelease-1>", fechalinha)
c.pack()
mainloop()
