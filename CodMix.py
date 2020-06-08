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

import tkinter as tk


class CodMix:
    def __init__(self,root):
        root.title("Untitled - CodMix")
        root.geometry("800x600")
        self.textarea = tk.Text(root)
        self.scroll = tk.Scrollbar(root, command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)


if __name__ == "__main__":
    root = tk.Tk()
    cm = CodMix(root)
    root.mainloop()
