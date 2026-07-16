import tkinter as tk
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import settings
import graph
from enum import Enum

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
        self.add_to_graph_list("Temp") #TODO: load in all existing project graphs
        self.graphsvar.trace_add('write', self.build_graph_list)

        self.build_add_graph_button()
        self.build_graph_list()
        self.build_copy_graph_button()
        self.build_delete_graph_button()

    def add_to_graph_list(self, new_graph_name):
        settings.current_project.graphs.append(graph.Graph(new_graph_name))
        self.update_graphsvar()

    def remove_from_graph_list(self, index):
        del settings.current_project.graphs[index]
        self.update_graphsvar()
        
    def update_graphsvar(self):
        self.graphsvar.set([g.name for g in settings.current_project.graphs])

    def build_add_graph_button(self):
        button_add_graph = tk.Button(self, text="New Graph", justify="center", command=self.add_graph, padx=10)
        button_add_graph.grid(row=0, column=0, pady=5)
    
    def build_graph_list(self, *args):
        settings.listbox = tk.Listbox(self, listvariable=self.graphsvar, height=20)
        settings.listbox.grid(row=1,column=0, pady=5)

    def build_copy_graph_button(self):
        button_add_graph = tk.Button(self, text="Copy Selected", justify="center", command=self.copy_graph, padx=10)
        button_add_graph.grid(row=2, column=0, pady=5)
    
    def build_delete_graph_button(self):
        button_add_graph = tk.Button(self, text="Delete Selected", justify="center", command=self.delete_graph, padx=10)
        button_add_graph.grid(row=3, column=0, pady=5)

    def add_graph(self):
        allow = False
        while True:
            graph_name = simpledialog.askstring("Prompt", "Enter graph name")
            if graph_name == None:
                return
            graph_name = graph_name.replace(" ", "")
            allow = self.validate_graph_name(graph_name)
            if (allow == self.GraphValidation.SUCCESS):
                break
            elif (allow == self.GraphValidation.BLANK):
                messagebox.showwarning("Warning", "Graph name cannot be blank")
            elif (allow == self.GraphValidation.ALREADY_EXISTS):
                messagebox.showwarning("Warning", "Graph name already exists")
        self.add_to_graph_list(graph_name)
        
    def copy_graph(self):
        selected_indices = settings.listbox.curselection()
        if (len(selected_indices) == 0): return
        for index in selected_indices:
            selected_graph_name = settings.current_project.graphs[index].name
            count = 1
            while True:
                new_graph_name = f"{selected_graph_name} ({count})"
                count += 1
                allow = self.validate_graph_name(new_graph_name)
                if (allow == self.GraphValidation.SUCCESS):
                    break
            self.add_to_graph_list(new_graph_name)

    def delete_graph(self):
        selected_indices = settings.listbox.curselection()
        if (len(selected_indices) == 0): return
        for index in selected_indices:
            selected_graph_name = settings.current_project.graphs[index].name
            confirm = messagebox.askokcancel("Confirm Delete", f"Are you sure you want to delete {selected_graph_name}? You cannot undo this action.")
            if confirm:
                self.remove_from_graph_list(index)

    def validate_graph_name(self, graph_name):
        if len(graph_name) <= 0:
            return self.GraphValidation.BLANK
        if graph_name in [x.name for x in settings.current_project.graphs]:
            return self.GraphValidation.ALREADY_EXISTS
        return self.GraphValidation.SUCCESS
    
    class GraphValidation(Enum):
        SUCCESS = 1
        BLANK = 0
        ALREADY_EXISTS = -1