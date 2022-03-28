#!/usr/bin/env python3


from cgitb import text
from threading import main_thread
import tkinter as tk

def main():
    window = tk.Tk()
    greet = tk.Label(text="text is hello", height=20)
    label = tk.Label(text="Tkinter!", background="#34A2FE")
    greet.pack()
    label.pack()
    window.mainloop()


if __name__ == "__main__":
    main()