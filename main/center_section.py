import dash
import dash_bootstrap_components as dbc

class CenterSection(dbc.Col):
    def __init__(self, width : int):
        super().__init__()
        self.id = "center-section"
        self.width = width
        self.children = [

        ]
    