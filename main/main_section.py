import dash_bootstrap_components as dbc
import left_section
import center_section 
import right_section

class MainSection(dbc.Row):
    def __init__(self):
        super().__init__()
        self.id = "main-section"
        self.children = [
            left_section.LeftSection(3),
            center_section.CenterSection(6),
            right_section.RightSection(3),
        ]
    