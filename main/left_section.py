import dash
import dash_bootstrap_components as dbc
import settings
import enum


class LeftSection(dbc.Col):
    def __init__(self, width: int):
        super().__init__()
        self.id = "left-section"
        self.width = width
        self.children = [
            dash.html.Div(
                [
                    self.add_graph_input(),
                    self.add_graph_error_message(),
                    self.graph_list(),
                ],
                style={
                    "display": "flex",
                    "flexDirection": "column",
                    "gap": "5px",
                    "justifyContent": "center",
                    "alignItems": "flex-start",
                    "margin": "10px",
                    "width": "100%",
                },
            )
        ]

    def add_graph_input(self):
        return dash.html.Div(
            [
                dash.dcc.Input(
                    id="add-graph-input",
                    type="text",
                    placeholder="Enter add graph name...",
                    style={"width": "100%", "height": "30px"},
                ),
                dash.html.Button(
                    "+",
                    id="add-graph-btn",
                    n_clicks=0,
                    style={
                        "width": "10%",
                        "height": "30px",
                        "border-radius": "3px",
                        "alignItems": "center",
                    },
                ),
            ],
            style={
                "display": "flex",
                "flexDirection": "row",
                "justifyContent": "space-between",
                "alignItems": "center",
                "gap": "10px",
                "width": "100%",
            },
        )

    def add_graph_error_message(self):
        return dash.html.Div(id="error-message", style={"color": "red"})

    def graph_list(self):
        # Initial dummy data
        initial_graphs = ["APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY"]

        return dash.html.Div(
            [
                dash.dcc.Store(id="graph-store", data=initial_graphs),
                dash.dcc.Dropdown(
                    options=[{"label": g.title(), "value": g} for g in initial_graphs],
                    value=None,
                    id="graph-dropdown",
                    clearable=False,
                ),
            ],
            style={"width": "100%", "height": "30px"},
        )


def validate_graph_name(graph_name, current_graphs):
    if not graph_name or len(graph_name.strip()) == 0:
        return GraphValidation.BLANK

    clean_name = graph_name.replace(" ", "").upper()
    if clean_name in current_graphs:
        return GraphValidation.ALREADY_EXISTS

    return GraphValidation.SUCCESS


class GraphValidation(enum.Enum):
    SUCCESS = 1
    BLANK = 0
    ALREADY_EXISTS = -1


@dash.callback(
    dash.Output("graph-dropdown", "options"),
    dash.Output("error-message", "children"),
    dash.Output("graph-store", "data"),
    dash.Input("add-graph-btn", "n_clicks"),
    dash.State("add-graph-input", "value"),
    dash.State("graph-store", "data"),
    prevent_initial_call=True,
)
def add_graph(n_clicks, new_graph_name, current_graphs):
    match validate_graph_name(new_graph_name, current_graphs):
        case GraphValidation.BLANK:
            error_msg = "Graph name cannot be blank."
            return dash.no_update, error_msg, dash.no_update
        case GraphValidation.ALREADY_EXISTS:
            error_msg = f"Graph '{new_graph_name}' already exists."
            return dash.no_update, error_msg, dash.no_update
        case GraphValidation.SUCCESS:
            clean_name = new_graph_name.replace(" ", "").upper()
            current_graphs.append(clean_name)
            new_options = [{"label": g.title(), "value": g} for g in current_graphs]
            return new_options, "", current_graphs
