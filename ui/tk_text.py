#!/usr/bin/env python3

import tkinter as tk


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.txtHello = tk.Text()
        self.txtHello.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()