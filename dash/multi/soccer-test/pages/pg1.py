import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

NUMBER_OF_PLAYERS = 20

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Home',  # name of page, commonly used as name of link
                   title='Index',  # title that appears on browser's tab
                   description='Histograms are the new bar charts.'
)

# read in premier league data
df = pd.read_csv('assets/pl-18-19.csv')
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(options=["Age", "Appearances", "Goals", "Assists", "Clean Sheets"],
                                     id='stat-choice')
                    ], xs=10, sm=10, md=8, lg=4, xl=4, xxl=4
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                        className="List",
                        # set default as the full name 
                        children=[
                            html.Ul(id='my-list', children=[html.Li(children=i) for i in df.full_name])
                        ],
                    ), html.Hr(),

                    ], width=12
                )
            ]
        )
    ]
)

@callback(
    Output('my-list', 'children'),
    Input('stat-choice', 'value')
)
def update_graph(value):
    value = name_converter(value)
    if value is None:
        data = [html.Li(i) for i in df.full_name]
    else:
        # check for clean sheets 
        if value == "clean_sheets_overall":
            df_sorted = df.query("position == 'Goalkeeper'").sort_values(by=f"{value}", ascending=False)
        else:
            df_sorted = df.sort_values(by=f"{value}", ascending=False)
        data = []
        for i in range(len(df_sorted[value])):
            data.append(html.Li(f"{df_sorted.full_name.iloc[i]}: {df_sorted[value].iloc[i]}"))
    return data[:NUMBER_OF_PLAYERS]

def name_converter(value: str) -> str:
    '''
    Helper function to match the name with the necessary data
    '''
    if not value:
        return value
    value = value.lower()
    if value == "age":
        return value 
    elif value == "goals":
        return "goals_overall"
    elif value == "assists":
        return "assists_overall"
    elif value == "appearances":
        return "appearances_overall"
    elif value == "clean sheets":
        return "clean_sheets_overall"
    else:
        return None