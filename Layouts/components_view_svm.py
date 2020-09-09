from textwrap import dedent

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Model.data_service import Statistics



# Display utility functions
def _merge(a, b):
    return dict(a, **b)


def _omit(omitted_keys, d):
    return {k: v for k, v in d.items() if k not in omitted_keys}


# Custom Display Components
def Card(children, **kwargs):
    return html.Section(
        children,
        style=_merge({
            'padding': 20,
            'margin': 5,
            'borderRadius': 5,
            'border': 'thin lightgrey solid',

            # Remove possibility to select the text for better UX
            'user-select': 'none',
            '-moz-user-select': 'none',
            '-webkit-user-select': 'none',
            '-ms-user-select': 'none'
        }, kwargs.get('style', {})),
        **_omit(['style'], kwargs)
    )
def Card_markdown(children, **kwargs):
    return html.Section(
        children,
        style=_merge({
            'padding': 20,
            'margin': 5,
            'borderRadius': 5,
            'border': 'thin lightgrey solid',
            'background - color':  '# 003399',

            # Remove possibility to select the text for better UX
            'user-select': 'none',
            '-moz-user-select': 'none',
            '-webkit-user-select': 'none',
            '-ms-user-select': 'none'
        }, kwargs.get('style', {})),
        **_omit(['style'], kwargs)
    )


def FormattedSlider(**kwargs):
    return html.Div(
        style=kwargs.get('style', {}),
        children=dcc.Slider(**_omit(['style'], kwargs))
    )


def NamedSlider(name, **kwargs):
    return html.Div(
        style={'padding': '20px 10px 25px 4px'},
        children=[
            html.P(f'{name}:'),
            html.Div(
                style={'margin-left': '6px'},
                children=dcc.Slider(**kwargs)
            )
        ]
    )


def NamedDropdown(name, **kwargs):
    return html.Div(
        style={'margin': '10px 0px'},
        children=[
            html.P(
                children=f'{name}:',
                style={'margin-left': '3px'}
            ),

            dcc.Dropdown(**kwargs)
        ]
    )


def NamedRadioItems(name, **kwargs):
    return html.Div(
        style={'padding': '20px 10px 25px 4px'},
        children=[
            html.P(children=f'{name}:'),
            dcc.RadioItems(**kwargs)
        ]
    )


# Non-generic
def DemoDescription(filename, strip=False):
    with open(filename, 'r') as file:
        text = file.read()

    if strip:
        text = text.split('<Start Description>')[-1]
        text = text.split('<End Description>')[0]

    return html.Div(
            className='row',
            style={
                'padding': '15px 30px 27px',
                'margin': '45px auto 45px',
                'width': '80%',
                'max-width': '1024px',
                'borderRadius': 5,
                'border': 'thin lightgrey solid',
                'font-family': 'Roboto, sans-serif'
            },
            children=dcc.Markdown(dedent(text))
    )

def card_dropdown():
    titles = Statistics( ).generate_titles( )
    return Card([
        html.Div(
            [
                dbc.Button(
                    "Tips",
                    id="collapse-button_variables",
                    className="mb-3",
                    color="primary",
                ),
                dbc.Collapse(
                    dbc.Card(dbc.CardBody("Las variables X son las que definen la clasificación"
                                          " y la variable Y es el resultado de la clasificación. "
                                          "El algoritmo SVM de acuerdo al comportamiento de los datos de entrada "
                                          "intentará predecir para siguientes registros si con los datos de las "
                                          "variables x el resultado de la variable Y es de 0 a 5")),
                    id="collapse_tips_variables",
                ),
            ]
        ),
                        NamedDropdown(
                            name='Selecciona la variable X ',
                            id='dropdown-svm-parameter-X',
                            options=titles,
                            value=titles[0]['value'],
                            clearable=False,
                            searchable=False
                        ),
                        NamedDropdown(
                            name='Seleccione la variable Y a predecir',
                            id='dropdown-svm-parameter-Y',
                            options=titles,
                            value=titles[1]['value'],
                            clearable=False,
                            searchable=False
                        ),
                    ])