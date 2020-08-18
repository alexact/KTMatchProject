from typing import List

import dash
import dash_bootstrap_components as dbc

external_css: List[str] = [
    # Normalize the CSS
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    # Fonts
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto",
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
]

app = dash.Dash(__name__, external_stylesheets=[ external_css, dbc.themes.BOOTSTRAP],
                assets_folder='../Assets/',suppress_callback_exceptions=True)
server = app.server
app.config.suppress_callback_exceptions = True
