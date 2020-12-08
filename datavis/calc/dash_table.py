import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objs as go
from dash.dependencies import Input, Output

from django_plotly_dash import DjangoDash
import pandas as pd
from .utils import *

app = DjangoDash('Table', external_stylesheets=[
                 dbc.themes.BOOTSTRAP], add_bootstrap_links=True)

files = getMediaFiles()

opt = [{'label': f, 'value': f} for f in files]
# print(opt, type(opt))
headerList = ['Col-1', 'Col-2', 'Col-3']
df = pd.DataFrame([
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montréal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
])
top = html.Div(
    children=[
        html.H3(
            children=['Data']
        ),
        dcc.Dropdown(
            id='varname-show',
            options=opt,
            style={
                'position': 'relative',
                'float': 'right'
            }
        )
    ]
)


table = html.Table(
    [
        html.Thead([
            html.Tr([html.Th(col) for col in df.columns])
        ]),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(len(df))
        ])
    ],
    id='table',
    className="table table-striped"
)
# add id of table by appending it with name of dataframe;


app.layout = dbc.Row(
    [
        dbc.Col(top, md=12),
        dbc.Col(table, md=12)
    ],
    className="m-3"
)


@app.callback(
    Output("table", "children"),
    [Input("varname-show", "value")]
)
def update_table(input_varname):
    df = pd.read_csv('./media/'+input_varname)

    upd_table = [html.Thead([
        html.Tr([html.Th(col) for col in df.columns])
    ]),
        html.Tbody(
        [html.Tr([
            html.Td(df.iloc[i][col]) for col in df.columns
        ]) for i in range(len(df))]
    )]
    
    return upd_table
