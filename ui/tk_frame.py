#!/usr/bin/env python3


import tkinter as tk


class Application:
    def center(self):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        self.window.update_idletasks()
        width = self.window.winfo_width()
        frm_width = self.window.winfo_rootx() - self.window.winfo_x()
        win_width = width + 2 * frm_width
        height = self.window.winfo_height()
        titlebar_height = self.window.winfo_rooty() - self.window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.window.winfo_screenwidth() // 2 - win_width // 2
        y = self.window.winfo_screenheight() // 2 - win_height // 2
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.deiconify()

    def __init__(self):
        self.window = tk.Tk()
        self.frame1 = tk.Frame(master=self.window, relief=tk.GROOVE, borderwidth=2)
        self.frame2 = tk.Frame()

        label = tk.Label(master=self.frame1, text="Hello")
        label.pack()

        label2 = tk.Label(master=self.frame2, text="Hello 2")
        label2.pack()

        self.frame1.pack(fill=tk.Y, side=tk.LEFT)
        self.frame2.pack(fill=tk.Y, side=tk.LEFT)

        self.button = tk.Button(text="Me")
        # self.button.pack(fill=tk.BOTH, expand=True)
        self.button.place(x=22, y=55)

        self.center()


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = Application()
    app.run()