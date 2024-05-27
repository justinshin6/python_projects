from dash import Dash, html, dcc, callback, Output, Input, State
import plotly.express as px
import pandas as pd

app = Dash()

app.layout = html.Div([
    html.Button(id='up-button', n_clicks=0, children="Up", style={'fontSize': 24, 'margin-left': 10}),
    html.Button(id='down-button', n_clicks=0, children="Down", style={'fontSize': 24, 'margin-left': 10}),
    html.Button(id='reset-button', n_clicks=0, children="Reset", style={'fontSize': 24, 'margin-left': 10}),
    html.H1(id='output')
])

@callback(
    [Output('output', 'children'), Output('up-button', 'n_clicks'), Output('down-button', 'n_clicks'), Output('reset-button', 'n_clicks')],
    [Input('up-button', 'n_clicks'), Input('down-button', 'n_clicks'), Input('reset-button', 'n_clicks')],
    [State('output', 'children')]
)
def return_output(up_clicks, down_clicks, reset, output):
    '''
    - The input parameters correspond to the order of the Input and the State variables in the callback function above.
    - The output depends on the order of the Output variables in the callback function above. 
    '''
    if reset:
        output = 0
        return output, 0, 0, 0
    
    # output state variable is the number of up minus the number of down 
    output = up_clicks - down_clicks
    return output, up_clicks, down_clicks, reset

if __name__ == '__main__':
    app.run(debug=True)

