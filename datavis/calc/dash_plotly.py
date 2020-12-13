import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objs as go
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

from . import utils
from .visualiser import Visualiser

app = DjangoDash('Graph', external_stylesheets=[
    dbc.themes.BOOTSTRAP], add_bootstrap_links=True, hot_reload=True)

vardict = utils.load_pkl('vardict')
if vardict != None:
    varList = vardict.get_var_list()
else:
    varList = []

vis_obj = Visualiser(vardict)

plot_list = ['line', 'bar', 'histogram', 'pie']

axis_variable = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("X Variable"),
                    dcc.Dropdown(
                        id='x-axis',
                        options=[],
                        # value="x-axis"
                    ),
                ]
            ),
            md=10
        ),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Y Variable"),
                    dcc.Dropdown(
                        id='y-axis',
                        options=[],
                        # value="x-axis"
                    ),
                ]
            ),
            md=10
        )
    ]
)

axis_label = dbc.Row(
    [
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("X-Label"),
                    dbc.Input(id="x-label", type="text")
                ]
            ),
            md=6
        ),
        dbc.Col(
            dbc.FormGroup(
                [
                    dbc.Label("Y-Label"),
                    dbc.Input(id="y-label", type="text")
                ]
            ),
            md=6
        )
    ]
)

input_varname = dbc.Col(
    dbc.FormGroup(
        [
            dbc.Label("Variable"),
            dcc.Dropdown(
                id='varname_visualiser',
                options=[],
                # value="x-axis"
            ),
        ]
    ), md=6
)

input_title = dbc.Row(dbc.Col(
    dbc.FormGroup(
        [
            dbc.Label("Title"),
            dbc.Input(id="title-visualiser", type="text", value="Graph")
        ]
    )
))

plot_types = dbc.Row([
    input_varname,
    dbc.Col(
        dbc.FormGroup(
            [
                dbc.Label("Plot-type"),
                dcc.Dropdown(
                    id='plot-type',
                    options=[
                        {"label": plot, "value": plot} for plot in plot_list
                    ],
                    # value="x-axis"
                ),
            ]
        ),
        md=6
    )]
)

controls = dbc.Card(
    [
        plot_types,
        axis_variable,
        input_title,
        axis_label,
    ],
    body=True
)

app.layout = dbc.Row(
    [
        dbc.Col(dcc.Graph(id="vis-graph"), md=8),
        dbc.Col(controls, md=4),
    ]
)


@app.callback(
    [Output("x-axis", "options"),
     Output("y-axis", "options")],
    [Input("varname_visualiser", "value")]
)
def update_cols(varname):
    vardict = utils.load_pkl('vardict')
    vis_obj = Visualiser(vardict)
    col_list = vis_obj.get_columns(varname)
    # print(col_list)
    options = [{"label": col, "value": col} for col in col_list]

    return options, options


@app.callback(
    Output("varname_visualiser", "options"),
    [Input("plot-type", "value")]
)
def update_vars(plot_type):
    vardict = utils.load_pkl('vardict')
    if vardict != None:
        varList = vardict.get_var_list()
    else:
        varList = []

    options = [{"label": var, "value": var} for var in varList]
    return options


@app.callback(
    Output("vis-graph", "figure"),
    [
        Input("x-axis", "value"),
        Input("y-axis", "value"),
        Input("x-label", "value"),
        Input("y-label", "value"),
        Input("plot-type", "value"),
        Input("title-visualiser", "value"),
        Input('varname_visualiser', "value")
    ]
)
def make_graph(x, y, xlabel, ylabel, plot_type, gtitle, varname):

    x_values = []
    y_values = []
    data_dict = []

    vardict = utils.load_pkl('vardict')
    vis_obj = Visualiser(vardict)

    if (plot_type == 'line' or plot_type == 'bar') and varname != None and x != None and y != None and plot_type != None:
        x_values = vis_obj.get_values(varname, x, 500)
        y_values = vis_obj.get_values(varname, y, 500)

        data_dict = [
            {'x': x_values, 'y': y_values, 'type': plot_type, 'name': 'sample'}
        ]

    elif (plot_type == 'histogram') and varname != None and x != None and plot_type != None:
        x_values = vis_obj.get_values(varname, x, 500)
        df = vis_obj.get_dataframe(varname)
        data_dict = [
            {'df': df, 'x': x_values, 'type': plot_type}
        ]

    elif (plot_type == 'pie') and varname != None and x != None and y != None and plot_type != None:
        df = vis_obj.get_dataframe(varname)
        data_dict = [
            {'df': df, 'values': x, 'names': y, 'type': plot_type}
        ]

    figure = {
        'data': data_dict,
        'layout': {
            'title': gtitle,
            'xaxis': dict(
                title=xlabel
            ),
            'yaxis': dict(
                title=ylabel
            )
        }
    }

    return figure
