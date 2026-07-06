import tkinter as tk

class ChatFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.borderwidth=2
        self.relief="ridge"
        self.width=200
        self.height=150
        self.padx=3
        self.pady=3