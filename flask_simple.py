import flask
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, State, Output


server = flask.Flask(__name__)

@server.route('/')
def index():
    return 'Hello Flask app'


app = dash.Dash(
    server=server,
    requests_pathname_prefix='/dash/',
    routes_pathname_prefix='/dash/',
)

app.layout = html.Div([
    html.Div(id='target'),
    dcc.Input(id='my-input', type='text', value=''),
    html.Button(id='submit', n_clicks=0, children='Save')
])

@app.callback(Output('target', 'children'), [Input('submit', 'n_clicks')],
              [State('my-input', 'value')])
def callback(n_clicks, state):
    return "callback received value: {}".format(state)


if __name__ == '__main__':
    app.run_server(debug=True)
