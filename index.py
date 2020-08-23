import dash_core_components as dcc
from Layouts.app import app
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from Layouts.tab_component import content_tab_layout
from Layouts.navbar_component import navbar
import Layouts.Callbacks.tab_callback, Layouts.Callbacks.upload_callback, Layouts.Callbacks.statistics_callback
import Layouts.Callbacks.svm_callback, Layouts.Callbacks.description_callback

app.layout = html.Div([
    html.Div([navbar]),
    html.Br( ),

        html.Div([dbc.Container(dcc.Location(id='url', refresh=False) )
              ], id='page-content',style={'width':'100%', 'padding':'40px'})])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/ktmath/svmAlgorithm':
        return ""
    elif pathname == '/ktmath/statistics':
        return content_tab_layout
    else:
        return content_tab_layout

server=app.server
if __name__ == '__main__':
    app.run_server(debug=True)
