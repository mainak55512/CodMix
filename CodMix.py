import tkinter as tk
from tkinter import filedialog as fd


class CodMix(tk.Frame):
    # Main window
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self)
        root.title("Untitled - CodMix")
        self.root = root
        self.filename = None
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
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

    def set_win_name(self, name=None):
        if name:
            self.root.title(name + " - CodMix")
        else:
            self.root.title("Untitled - CodMix")

    def new_file(self):
        self.text.delete(1.0, tk.END)
        self.filename = None
        self.set_win_name()

    def open_file(self):
        self.filename = fd.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("All Files", "*.txt"),
                       ("Python file", "*.py"),
                       ("C file", "*.c"),
                       ("C++ file", "*.cpp"),
                       ("Java file", "*.java"),
                       ("Mark down files", "*.md"),
                       ("HTML files", "*.html"),
                       ("CSS files", "*.css"),
                       ("JavaScript files", "*.js")
                       ]
        )
        if self.filename:
            self.text.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.text.insert(1.0, f.read())
            self.set_win_name(self.filename)

    def save(self):
        if self.filename:
            try:
                text_content = self.text.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(text_content)
            except Exception as e:
                print("!!!Something went wrong!!!")
        else:
            self.save_as()

    def save_as(self):
        try:
            new_file = fd.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"),
                           ("All Files", "*.txt"),
                           ("Python file", "*.py"),
                           ("C file", "*.c"),
                           ("C++ file", "*.cpp"),
                           ("Java file", "*.java"),
                           ("Mark down files", "*.md"),
                           ("HTML files", "*.html"),
                           ("CSS files", "*.css"),
                           ("JavaScript files", "*.js")
                           ]
            )
            text_content = self.text.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(text_content)
            self.filename = new_file
            self.set_win_name(self.filename)
        except Exception as e:
            print("!!!Something went wrong!!!")

    def cut(self):
        self.text.event_generate(("<<Cut>>"))

    def copy(self):
        self.text.event_generate(("<<Copy>>"))

    def paste(self):
        self.text.event_generate(("<<Paste>>"))


class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, root, undo=True)

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
        edit_dropdown.add_command(label="Undo", command=parent.text.edit_undo)
        edit_dropdown.add_command(label="Redo", command=parent.text.edit_redo)
        edit_dropdown.add_separator()
        edit_dropdown.add_command(label="Cut", command=parent.cut)
        edit_dropdown.add_command(label="Copy", command=parent.copy)
        edit_dropdown.add_command(label="Paste", command=parent.paste)
        menubar.add_cascade(label="Edit", menu=edit_dropdown)


if __name__ == "__main__":
    # main window
    root = tk.Tk()
    CodMix(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
