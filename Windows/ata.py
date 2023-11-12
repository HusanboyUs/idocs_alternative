import tkinter as tk
from tkinter import ttk

class CustomTreeView(ttk.Treeview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.heading("#1", text="Name")
        self.heading("#2", text="Value")

    def add_data(self):
        self.insert("", "end", values=("Root", ""))
        self.insert("Root", "end", values=("Node 1", "Value 1"))
        self.insert("Root", "end", values=("Node 2", "Value 2"))
        self.insert("Node 2", "end", values=("Subnode 2.1", "Value 2.1"))

class CustomTreeViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom TreeView")

        self.tree = CustomTreeView(root, columns=("Name", "Value"))
        self.tree.pack()

        self.tree.add_data()

def main():
    root = tk.Tk()
    app = CustomTreeViewApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
