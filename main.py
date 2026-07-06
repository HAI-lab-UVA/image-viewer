import tkinter as tk
import project
import graph

root = tk.Tk()
root.option_add('*tearOff', False)
root.title("Title")
root.geometry('{}x{}'.format(1000, 600))

# create all of the main containers
frame_left = tk.Frame(root, borderwidth=2, relief="ridge", width=200, height=150, padx=3, pady=3) # height flexes to root size
frame_center = tk.Frame(root, borderwidth=2, relief="ridge", width=50, height=150, padx=3, pady=3) # width & height flexes to root size
frame_right = tk.Frame(root, borderwidth=2, relief="ridge", width=200, height=150, padx=3, pady=3) # height flexes to root size

# layout all of the main containers
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

frame_left.grid(column=0, row=0, sticky="ns")
frame_center.grid(column=1, row=0, sticky="nsew")
frame_right.grid(column=2, row=0, sticky="ns")

# Root menu
menubar = tk.Menu()
root.config(menu=menubar)

project_menu = tk.Menu(menubar)
menubar.add_cascade(menu=project_menu, label="Project")

def example():
    pass

def quit_app():
    root.destroy()

project_menu.add_command(label="New Project", command=example)
project_menu.add_command(label="Load Project", command=example)
project_menu.add_command(label="Save Project", command=example)
project_menu.add_command(label="Save as New Project", command=example)
project_menu.add_command(label="Quit", command=quit_app)

# Left frame widgets
button_add_graph = tk.Button(frame_left, text="New Graph", justify="center", command=example, padx=10)
button_add_graph.grid(row=0, column=0, pady=10)

graphs = ["apple", "orange", "banana","apple", "orange", "banana","apple", "orange", "banana"]
graphsvar = tk.StringVar(value=graphs)
l = tk.Listbox(frame_left, listvariable=graphsvar, height=20)
l.grid(row=1,column=0)

root.mainloop()