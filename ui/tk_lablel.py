#!/usr/bin/env python3

import tkinter as tk


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.lblHello = tk.Label(
            text="Hello tk!",
            fg="orange red",
            bg="white smoke",
            height=2,
            width=20
            )
        self.lblHello.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()