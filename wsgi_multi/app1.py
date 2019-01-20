import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Output


app = dash.Dash(requests_pathname_prefix='/app1/')

app.layout = html.Div([
    html.Div(id='target'),
    dcc.Input(id='my-input', type='text', value=''),
    html.Button(id='submit', n_clicks=0, children='Save')
])

@app.callback(Output('target', 'children'), [Input('submit', 'n_clicks')],
              [State('my-input', 'value')])
def callback(n_clicks, state):
    return "App1: callback received value: {}".format(state)
