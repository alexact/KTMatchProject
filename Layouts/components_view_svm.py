from textwrap import dedent

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Model.data_service import DataService
from Controllers.statistics_controller import StatisticsController as StController, initialization

initialization( )
sts_controller = StController( )
# Display utility functions
def _merge(a, b):
    return dict(a, **b)


def _omit(omitted_keys, d):
    return {k: v for k, v in d.items( ) if k not in omitted_keys}


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
            'background - color': '# 003399',

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
        text = file.read( )

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
    return Card([
        html.Div(
            [
                dbc.Button(
                    "Tips 1",
                    id="collapse-button_variables",
                    className="mb-3",
                    color="primary",
                ),
                dbc.Collapse(
                    dbc.Card(dbc.CardBody("Las variables <<X>> son las que definen la clasificación"
                                          "La variable <<Y>> es el resultado de la clasificación:"
                                          " Si tiene o no tiene gestión del conocimiento formal. "
                                          "El algoritmo SVM de acuerdo al comportamiento de los datos de entrada "
                                          "intentará predecir para el último registros si con los datos de las "
                                          "variables <<X>> el resultado de la variable Y es de Si o No")),
                    id="collapse_tips_variables",
                ),
            ]
        ),
        NamedDropdown(
            name='Selecciona una variable dependiente(X)',
            id='dropdown-svm-parameter-X',
            options=sts_controller.titles_dropdown_svm,
            value=sts_controller.titles_dropdown_svm[0]['value'],
            clearable=False,
            searchable=False
        ),
        NamedDropdown(
            name='Selecciona una variable dependiente(X)',
            id='dropdown-svm-parameter-Y',
            options=StController().titles_dropdown_svm,
            value=StController().titles_dropdown_svm[1]['value'],
            clearable=False,
            searchable=False
        ),
    ])
