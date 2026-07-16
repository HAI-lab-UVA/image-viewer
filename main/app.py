import dash
import dash_bootstrap_components as dbc
import menu
import main_section

class App(dash.Dash):
    def __init__(self):
        super().__init__(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.layout = dbc.Container([
            menu.Menu(),
            main_section.MainSection(),
        ])
    