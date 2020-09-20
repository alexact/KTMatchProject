from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
import numpy as np

from Layouts.app import app
from Controllers.statistics_controller import StatisticsController as StController, initialization
import plotly.graph_objects as go
import plotly.express as px


@app.callback([Output('var_XSev', 'options'),
               Output('var_XSev', 'value'),
               Output('var_YSev', 'options'),
               Output('var_YSev', 'value')],
              [Input('output-data-uploads', 'children')])
def update_dropdown(children):
    optionsX = initialization.titles_dropdown
    optionsY = optionsX
    valueX = optionsX[0]['value']
    valueY = optionsY[-1]['value']
    return optionsX, valueX, optionsY, valueY


@app.callback([Output('frec_table', 'data'),
               Output('frec_table', 'columns')],
              [Input('output-data-uploads', 'children')])
def update_table(children):
    """
    Actualiza la tabla de frecuentia de la severidad
    :param children:
    :return:
    """
    if initialization.df_data is not None:
        # table = dbc.Table.from_dataframe(initialization.df_frecuency.to_dict('records'), striped=True,
        # bordered=True, hover=True, id='frec_table')
        return initialization.df_frecuency.to_dict('records'), initialization.titles_frec


@app.callback(Output("correlation-Graph", "figure"),
              [Input("output-data-uploads", "children"),
               Input("var_XSev", "value"),
               Input("var_YSev", "value")])
def update_fig_corr(data_df, input_value, var_YSev):
    """
    Actualiza la gráfica de dispersión de la severidad
    :param data_df: data de severidad
    :param input_value: valor seleccionado desde la interfaz para el eje x
    :param var_YSev:valor seleccionado desde la interfaz para el eje y
    :return:
    """
    initialization( )
    if initialization.df_data is not None:
        title = [i for i in list(initialization.df_data)]
        print(title)
        colX = title.index(input_value)
        colY = title.index(var_YSev)
        data_df = initialization.df_data
        if data_df is not None:
            data = [dict(
                x=data_df[title[colX]],
                y=data_df[title[colY]],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                })]
            layout = dict(
                title="Gráfica de correlación severidad (Impacto x Frecuencia)",
                xaxis={'type': 'log', 'title': title[colX]},
                yaxis={'title': title[colY]},
                legend={'x': 'a', 'y': 0},
                hovermode='closest'
            )

            print('You have selected for X corr"{}"'.format(input_value))
            r = {"data": data,
                 "layout": layout}
            return r
        layout = dict(
            title="Gráfica de correlación",
            xaxis={'type': 'log', 'title': title[colX]},
            yaxis={'title': title[colY]},
            legend={'x': 'a', 'y': 0},
            hovermode='closest'
        )
        data = [dict(
            x=0,
            y=0,
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            })]
        r = {"data": data,
             "layout": layout}
        return r


@app.callback([Output('histogram_impact', 'figure'),
               Output('histogram_frecuency', 'figure')
               ],
              [Input("output-data-uploads", "children"),
               Input("var_XSev", "value"),
               Input("var_YSev", "value")
               ])
def update_histograms(upload, var_XSev, var_YSev):
    title = [i for i in list(initialization.df_data)]
    colX = title.index(var_XSev)
    colY = title.index(var_YSev)
    if initialization.df_data is not None:
        x_impac = initialization.df_impact[title[colX]]
        y_impac = initialization.df_impact[title[colY]]
        x_frec = initialization.df_data_frecuency[title[colX]]
        y_frec = initialization.df_data_frecuency[title[colY]]

        fig_impact = px.bar(initialization.df_impact,
                            x=title[colX],
                            y=title[colY],
                            title="Grafica de barras - Impacto del problema ")
        fig_frec = px.bar(initialization.df_data_frecuency,
                          x=title[colX],
                          y=title[colY],
                          title="Grafica de barras - Frecuecia con la que ocurre el problema")
    return fig_impact, fig_frec
    """@app.callback([Output('histogram_impact', 'figure'),
               Output('histogram_frecuency', 'figure')
               ],
              [Input("output-data-uploads", "children"),
               Input("var_XSev", "value"),
               Input("var_YSev", "value")
               ])
def update_histograms(upload, var_XSev, var_YSev):
    title = [i for i in list(initialization.df_data)]
    colX = title.index(var_XSev)
    colY = title.index(var_YSev)
    if initialization.df_data is not None:
            x_impac=initialization.df_impact[title[colX]]
            y_impac=initialization.df_impact[title[colY]]
            x_frec=initialization.df_data_frecuency[title[colX]]
            y_frec=initialization.df_data_frecuency[title[colY]]


    fig_impact = px.histogram(initialization.df_impact, x=x_impac,y=y_impac)
    fig_frec = px.histogram(initialization.df_data_frecuency, x=x_frec, y= y_frec)
    #x = np.random.randn(4)
    #y = np.random.randn(8)
    # print("X",x)
    # print("Y", y)
    #fig_hist_impac = go.Figure(data=[go.Histogram(x=y, histnorm='probability')])
    #fig_hist_frec =  go.Figure(data=[go.Histogram(x=x, histnorm='probability')])
    #print(fig_hist_impac,fig_hist_frec)
    return fig_impact,fig_frec"""


@app.callback(Output('heatmap_data', 'figure'),
              [Input("output-data-uploads", "children")])
def update_fig_corr(upload):
    if not initialization.df_data.empty:
        df = StController( ).get_correlation( )
        figure = go.Figure(data=go.Heatmap(
            z=df.values,
            x=df.columns,
            y=df.columns,
            hoverongaps=False))
        return figure

    ejemplo = go.Figure(data=go.Heatmap(
        z=[[0, 0.5, 0.8, 0.2, 1], [0.2, 1, 0.7, 0.2, 0], [0, 0.6, 0.8, -0.2, -1]],
        x=['D', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        y=['Morning', 'Afternoon', 'Evening'],
        hoverongaps=False))
    return ejemplo
