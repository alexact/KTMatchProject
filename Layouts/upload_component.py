import datetime
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc


def upload_component():
    """
    :return: Retorna la barra de carga de archivos para el componente tab_component
    """
    pass
    return html.Div([
        dcc.Upload(
            id='upload-datas',
            children=html.Div([
                'Arrastra o ',
                html.A('selecciona el archivo')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=True
        ),
        html.Div(id='output-data-uploads')
    ],
        className='text-contain')


def succesfull_upload(filename, date):
    return html.Div([
        dbc.Alert("Carga exitosa",  color="success"),
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),
        html.Hr( ),  # horizontal line
    ])


def not_succesfull_upload():
    return html.Div([
        dbc.Alert('Hubo un error al procesar el archivo.',color="danger"),
        dbc.Alert('Recuerde delimitar por ";". No usar texto con tíldes.\nEn los resultados de las variables '
                  'usar solo números, excepto por la última columna que es la variables Y (texto)', color="danger")
    ])
