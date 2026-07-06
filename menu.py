import tkinter as tk

class Menu(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.create_project_menu()
    
    def create_project_menu(self):
        project_menu = tk.Menu(self)
        self.add_cascade(menu=project_menu, label="Project")

        project_menu.add_command(label="New Project", command=self.example)
        project_menu.add_command(label="Load Project", command=self.example)
        project_menu.add_command(label="Save Project", command=self.example)
        project_menu.add_command(label="Save as New Project", command=self.example)
        project_menu.add_command(label="Quit", command=self.quit_app)

    def example():
        pass

    def quit_app(self):
        self.parent.destroy()