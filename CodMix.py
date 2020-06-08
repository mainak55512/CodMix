"""
Program Name: CodMix.py,  Description: Code Editor
    Copyright (C) 2020  Mainak Bhattacharjee

    Albus.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Albus.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    e-mail: mbhattacharjee432@gmail.com
"""

import tkinter as Tk 
from tkinter import ttk
from ttkthemes import themed_tk as tk


class MenuBar:
    def __init__(self,parent):
        menubar = Tk.Menu(parent.root)
        parent.root.config(menu=menubar)


class CodMix:
    def __init__(self,root):
        root.title("Untitled - CodMix")
        root.geometry("800x600")
        self.root=root
        self.textarea = Tk.Text(root)
        self.scroll = Tk.Scrollbar(root, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=Tk.LEFT,fill=Tk.BOTH,expand=True)
        self.scroll.pack(side=Tk.RIGHT, fill=Tk.Y)
        self.menubar=MenuBar(self)


if __name__ == "__main__":
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("breeze")
    cm = CodMix(root)
    root.mainloop()
