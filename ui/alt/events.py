from tkinter import *
from tkinter import ttk

root = Tk()
l = ttk.Label(root, text="Started")
l.grid()
l.bind('<Enter>', lambda e: l.configure(text="Moved inside"))
l.bind('<Leave>', lambda e: l.configure(text="Moved outside"))
l.bind('<ButtonPress-1>', lambda e: l.configure(text="Clicked left button"))
l.bind('<3>', lambda e: l.configure(text="Clicked right button"))
l.bind('<Double-1>', lambda e: l.configure(text="Clicked left twice button"))
l.bind('<B3-Motion>', lambda e: l.configure(text="Right Motion x = {} y = {}".format(e.x, e.y)))
l.bind('<B1-Motion>', lambda e: l.configure(text="Left Motion x = {} y = {}".format(e.x, e.y)))

root.mainloop()

