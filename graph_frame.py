import tkinter as tk

class GraphFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.borderwidth=2
        self.relief="ridge"
        self.width=50
        self.height=150
        self.padx=3
        self.pady=3