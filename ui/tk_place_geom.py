#!/usr/bin/env python3

import tkinter as tk


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.lblHello = tk.Label(text="Hello tk!")
        self.lblHello.place(x=2, y=4)

        self.lbl2 = tk.Label(text="1 tk!")
        self.lbl2.place(x=2, y=5)
        self.center()

    def run(self):
        self.window.mainloop()

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
        # self.window.deiconify()


if __name__ == "__main__":
    app = Application()
    app.run()