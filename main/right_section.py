import dash
import dash_bootstrap_components as dbc

class RightSection(dbc.Col):
    def __init__(self, width : int):
        super().__init__()
        self.id = "right_section"
        self.width = width
        self.children = [

        ]
    