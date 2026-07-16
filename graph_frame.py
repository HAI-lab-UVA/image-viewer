import tkinter as tk
import settings
import plotly.express as px
from tkinterweb import HtmlFrame

class GraphFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.borderwidth=2
        self.relief="ridge"
        self.width=200
        self.height=150
        self.padx=3
        self.pady=3
        settings.listbox.bind("<<ListboxSelect>>", self.update_frame)

    def update_frame(self, *args):
        selected_graph = settings.current_project.graphs[settings.listbox.curselection()[0]]
        self.build_graph_name_label(selected_graph)
        self.build_graph()

    def build_graph_name_label(self, graph):
        graph_name_label = tk.Label(self, text=f"Graph: {graph.name}", justify="left", padx=10)
        graph_name_label.grid(row=0, column=0, pady=5)
    
    def build_graph(self):
        # 1. Create your Plotly figure
        df = px.data.iris()
        fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

        # 2. Convert the figure directly to an HTML string
        # include_plotlyjs="cdn" keeps the string size smaller
        html_string = fig.to_html(include_plotlyjs="cdn", full_html=True)


        # 4. Use HtmlFrame to display the interactive graph
        frame = HtmlFrame(self, height=50, width=150)
        frame.load_html(html_string)
        frame.grid(row=1, column=0, pady=5)

        