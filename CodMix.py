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
