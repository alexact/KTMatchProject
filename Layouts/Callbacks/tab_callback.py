from dash.dependencies import Input, Output, State

import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from Layouts.app import app
from Layouts.tab_component import content_tab_layout
from Layouts.upload_component import upload_component
from Layouts.sts_graphs_component import scatter_graph, dropdown_scatter_graph, frec_table, heatmap_correlation, \
    frec_table_boostrapt, histogram_graph_impact, histogram_graph_frecuency

from Layouts.description_component import Description
from Layouts.svm_component import layout_SVM

content_tab_layout

desc = Description( )


@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return [
           desc.description_about_app()
        ]
    elif tab == 'tab-2':
        return desc.description_instruction()
    elif tab == 'tab-3':
        card_graph = dbc.Card([dbc.CardHeader(html.H4("Correlación de variables para la severidad")),
                               dbc.CardBody(
                                   [upload_component( ), dropdown_scatter_graph( ), scatter_graph( )]
                               )],
                              color="info", outline=True, style={"padding": "20px", 'marginTop': '30px'}
                              )
        section_graph = dbc.Row([dbc.Col(desc.description_scatter_plot( ), width=4),
                                 dbc.Col(card_graph, width=8)
                                 ]
                                )
        section_frec_table = dbc.Row(dbc.Col([desc.description_frec_table( ),
                                              frec_table( )]))

        section_heatmap = dbc.Row([dbc.Col([desc.heatmap_plot( ),
                                            heatmap_correlation( )
                                            ])
                                   ])
        section_histogram = dbc.Card(
            dbc.CardBody(dbc.Row([dbc.Col(histogram_graph_frecuency( )),
                                  dbc.Col(histogram_graph_impact( ))]
                                 ))
            , color="info", outline=True, style={"padding": "20px", 'marginTop': '30px'}
        )
        return [
            section_graph,
            section_histogram,
            section_frec_table,
            section_heatmap

        ]

    elif tab == 'tab-4':
        return [upload_component( ), layout_SVM]

