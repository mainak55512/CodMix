import tkinter as tk


class CodMix(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        root.title("Untitled - CodMix")
        self.root = root
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.menubar = MenuBar(self)

        self.vsb.pack(side="right", fill="y")
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()


    def set_win_name(self):
        pass

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save(self):
        pass

    def save_as(self):
        pass


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, root)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or
                args[0:3] == ("mark", "set", "insert") or
                args[0:2] == ("xview", "moveto") or
                args[0:2] == ("xview", "scroll") or
                args[0:2] == ("yview", "moveto") or
                args[0:2] == ("yview", "scroll")
            ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result
    # self.menubar = MenuBar(self)


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)


class MenuBar:
    def __init__(self, parent):
        menubar = tk.Menu(parent.root)
        parent.root.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, tearoff=0)
        file_dropdown.add_command(label="New", command=parent.new_file)
        file_dropdown.add_command(label="Open", command=parent.open_file)
        file_dropdown.add_command(label="Save", command=parent.save)
        file_dropdown.add_command(label="Save As...", command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Exit", command=parent.root.destroy)
        menubar.add_cascade(label="File", menu=file_dropdown)
        edit_dropdown = tk.Menu(menubar, tearoff=0)
        edit_dropdown.add_command(label="Undo")
        edit_dropdown.add_command(label="Redo")
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label="Cut")
        edit_dropdown.add_command(label="Copy")
        edit_dropdown.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=edit_dropdown)


if __name__ == "__main__":
    # main window
    root = tk.Tk()
    CodMix(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
