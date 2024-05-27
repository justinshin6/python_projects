from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd

app = Dash()

app.layout = html.Div([
    dcc.Input(id='number-in', value=1, style={'fontSize': 24}),
    html.Button(id='submit-button',
                n_clicks=0,
                children='Submit Here',
                style={'fontSize': 24}),
    html.H1(id='number-out')
])

@callback(Output('number-out', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('number-in', 'value')])
def output(n_clicks, number):
    return f"{number} was type in, and button was clicked {n_clicks} times"

if __name__ == '__main__':
    app.run(debug=True)