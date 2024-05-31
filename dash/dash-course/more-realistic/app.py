import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# import data 
education = pd.read_csv('../Data/states_all.csv', usecols=["STATE", "YEAR", "TOTAL_EXPENDITURE"])
df = education.query("STATE == 'CALIFORNIA' & YEAR > 1992")
app = dash.Dash(__name__)

# app frontend 
app.layout = html.Div([
    html.Div(children="Select a state to analyze!"),
    dcc.Dropdown(id="state-dropdown", options=["Oregon", "California", "Washington"]),
    dcc.Graph(id="state-graph")
])

# app backend
@callback(
    Output("state-graph", "figure"),
    Input("state-dropdown", "value")
)
def update_output_div(state):
    if not state:
        raise dash.exceptions.PreventUpdate
    df = education.query(f"STATE == '{state.upper()}' & YEAR > 1992")
    fig = px.line(
        df, 
        x="YEAR",
        y="TOTAL_EXPENDITURE",
        title=f"Expenditure in {state.title()}"
    )
    return fig 

if __name__ == "__main__":
    app.run(debug=True)