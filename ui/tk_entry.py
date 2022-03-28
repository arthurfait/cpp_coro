#!/usr/bin/env python3

import tkinter as tk


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.lblHello = tk.Label(
            text="Name:",
            fg="orange red",
            bg="white smoke",
            height=2,
            width=20
            )
        self.lblHello.pack()
        self.edfName = tk.Entry(
            fg="cyan",
            bg="black",
            width=50
        )
        self.edfName.pack()
        self.btnPush = tk.Button(
            text="Push me!",
            width=20,
            height=2,
            fg="blue",
            bg="red"
        )
        self.btnPush.pack()


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()