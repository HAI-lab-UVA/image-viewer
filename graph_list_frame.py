import tkinter as tk

class GraphListFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.borderwidth=2
        self.relief="ridge"
        self.width=200
        self.height=150
        self.padx=3
        self.pady=3

        self.build_add_graph_button()
        self.build_graph_list()

    def build_add_graph_button(self):
        button_add_graph = tk.Button(self, text="New Graph", justify="center", command=self.example, padx=10)
        button_add_graph.grid(row=0, column=0, pady=10)

    def build_graph_list(self):
        graphs = ["apple", "orange", "banana","apple", "orange", "banana","apple", "orange", "banana"]
        graphsvar = tk.StringVar(value=graphs)
        l = tk.Listbox(self, listvariable=graphsvar, height=20)
        l.grid(row=1,column=0)

    def example():
        pass