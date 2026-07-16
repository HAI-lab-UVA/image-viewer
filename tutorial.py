# Import packages
import dash
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = dash.Dash()

# App layout
app.layout = [
    dash.html.Div(children='My First App with Data, Graph, and Controls'),
    dash.html.Hr(),
    dash.dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dag.AgGrid(
        rowData=df.to_dict('records'),
        columnDefs=[{"field": i} for i in df.columns]
    ),
    dash.dcc.Graph(figure={}, id='controls-and-graph')
]

# Add controls to build the interaction
@dash.callback(
    dash.Output(component_id='controls-and-graph', component_property='figure'),
    dash.Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)