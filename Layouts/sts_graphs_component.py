import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import plotly.graph_objects as go
import numpy as np

from Controllers.statistics_controller import StatisticsController as StController, initialization


def table_header_style():
    return {
        "backgroundColor": "rgb(2,21,70)",
        "color": "white",
        "textAlign": "center",
    }


def frec_table():
    return html.Div([
        dash_table.DataTable(
            id='frec_table',
            style_as_list_view=True,
            style_header=table_header_style( ),
            style_data_conditional=[
                {
                    "if": {"column_id": "param"},
                    "textAlign": "right",
                    "paddingRight": 10,
                },
                {
                    "if": {"row_index": "odd"},
                    "backgroundColor": "white",
                },
            ],
        ),

        html.Hr( )
    ])


def frec_table_boostrapt():
    return dbc.Card( )


def scatter_graph():
    pass
    return html.Div([
        dcc.Graph(
            id="correlation-Graph",
            config={'displaylogo': False}
        )
    ], className="six_columns")


def dropdown_scatter_graph():
    card = dbc.Card(children=html.Div([
        dbc.Row([
            dbc.Col(html.Div(html.H4('Eje X')), width=5),
            dbc.Col(html.Div(html.H4('Eje Y')), width=5)
        ],
            justify="between"),
        dbc.Row(
            [
                dbc.Col(html.Div([dcc.Dropdown(id='var_XSev', options=StController.titles_dropdown,
                                               value=StController( ).titles_dropdown[2]['value'], clearable=False)],
                                 className="titlesXSev_Dropdown")
                        , width=5),

                dbc.Col(html.Div([dcc.Dropdown(id='var_YSev', options=StController.titles_dropdown,
                                               value=StController( ).titles_dropdown[3]['value'], clearable=False)],
                                 className="titlesYSev_Dropdown"), width=5),
            ], justify="between")
    ]), color="info", outline=True,
        style={'padding': '15px'})
    return card


def histogram_graph_impact():
    y = np.random.randn(3)
    fig2 = go.Figure(data=[go.Histogram(x=y, histnorm='probability')])
    return dcc.Graph(figure=fig2, id='histogram_impact')


def histogram_graph_frecuency():
    x = np.random.randn(5)
    fig2 = go.Figure(data=[go.Histogram(x=x, histnorm='probability')])
    return dcc.Graph(figure=fig2, id='histogram_frecuency')


def heatmap_correlation():
    fig = go.Figure( )
    return dcc.Graph(figure=fig, id='heatmap_data')
