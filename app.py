import tkinter as tk
import chat_frame
import graph_list_frame
import graph_frame
import menu

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.option_add('*tearOff', False)
        self.title("Title")
        self.geometry('{}x{}'.format(1000, 600))
        self.config(menu=menu.Menu(self))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.chat_frame = chat_frame.ChatFrame(self)
        self.graph_list_frame = graph_list_frame.GraphListFrame(self)
        self.graph_frame = graph_frame.GraphFrame(self)

        self.chat_frame.grid(column=0, row=0, sticky="ns")
        self.graph_list_frame.grid(column=1, row=0, sticky="nsew")
        self.graph_frame.grid(column=2, row=0, sticky="ns")