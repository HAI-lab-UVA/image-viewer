import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import settings
import graph

class GraphListFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.borderwidth=2
        self.relief="ridge"
        self.width=200
        self.height=150
        self.padx=3
        self.pady=3

        self.graphsvar = tk.StringVar()
        self.update_graphsvar()
        self.graphsvar.trace_add('write', self.build_graph_list)

        self.build_add_graph_button()
        self.build_graph_list()

    def update_graphsvar(self):
        self.graphsvar.set([g.name for g in settings.current_project.graphs])

    def build_add_graph_button(self):
        button_add_graph = tk.Button(self, text="New Graph", justify="center", command=self.add_graph, padx=10)
        button_add_graph.grid(row=0, column=0, pady=10)

    def build_graph_list(self, *args):
        print("RUNNIGN!")
        l = tk.Listbox(self, listvariable=self.graphsvar, height=20)
        l.grid(row=1,column=0)

    def add_graph(self):
        allow = False
        while not allow:
            graph_name = simpledialog.askstring("Prompt", "Enter graph name")
            if graph_name == None:
                return
            allow = self.validate_graph_name(graph_name)
        settings.current_project.graphs.append(graph.Graph(graph_name))
        self.update_graphsvar()

    def validate_graph_name(self, graph_name):
        if len(graph_name.replace(" ", "")) <= 0:
            messagebox.showwarning("Warning", "Graph name cannot be blank")
            return False
        if graph_name in [x.name for x in settings.current_project.graphs]:
            messagebox.showwarning("Warning", "Graph name already exists")
            return False
        return True