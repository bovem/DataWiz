import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objs as go
from dash.dependencies import Input, Output

from django_plotly_dash import DjangoDash

app = DjangoDash('Graph')
col_list = ['Col-1', 'Col-2', 'Col-3']
controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("X Variable"),
                dcc.Dropdown(
                    id='x-axis',
                    options=[
                        {"label": col, "value": col} for col in col_list
                    ],
                    # value="x-axis"
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Y Variable"),
                dcc.Dropdown(
                    id='y-axis',
                    options=[
                        {"label": col, "value": col} for col in col_list
                    ],
                    # value="x-axis"
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("X-Label"),
                dbc.Input(id="x-label", type="text")
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Y-Label"),
                dbc.Input(id="y-label", type="text")
            ]
        )
    ],
    body = True
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id="vis-graph"), md=8),
                dbc.Col(controls, md=4),
            ],
            align="center"
        ),
    ],
    fluid=True
)

@app.callback(
    Output("vis-graph", "figure"),
    [
        Input("x-axis", "value"),
        Input("y-axis", "value"),
        Input("x-label", "value"),
        Input("y-label", "value")
    ],
)

def make_graph(x, y, xlabel, ylabel):

    figure = {
        'data': [
            {'x': [1, 2, 3], 'y':[1,2,3],'type':'line', 'name':'sample'}
        ],
        'layout': {
            'title': 'Graph',
            'xaxis': dict(
                title= xlabel
            ),
            'yaxis': dict(
                title=ylabel
            )
        }
    }

    return figure