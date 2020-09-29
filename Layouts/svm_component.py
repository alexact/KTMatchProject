import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import Layouts.components_view_svm as drc

layout_SVM = html.Div(id='body', className='container scalable', children=[
                html.Div(
                    id='div-graphs',
                    children=dcc.Graph(
                        id='graph-sklearn-svm',
                        style={'display': 'none'}
                    )
                ),

                html.Div(
                    className='three columns',
                    style={
                        'min-width': '24.5%',
                        'max-height': 'calc(100vh - 85px)',
                        'overflow-y': 'auto',
                        'overflow-x': 'hidden',
                    },
                    children=[
                        drc.card_dropdown(),

                        drc.Card([
                            drc.NamedSlider(
                                name='Threshold',
                                id='slider-threshold',
                                min=0,
                                max=1,
                                value=0.5,
                                step=0.01
                            ),

                            html.Button(
                                'Reset Threshold',
                                id='button-zero-threshold'
                            ),
                        ]),

                        drc.Card([
                            html.Div(
                                [
                                    dbc.Button(
                                        "Tips 2",
                                        id="collapse-button_kernel",
                                        className="mb-3",
                                        color="primary",
                                    ),
                                    dbc.Collapse(
                                        dbc.Card(dbc.CardBody("Cambia los kernel y selecciona el que clasifique en la "
                                                              "gráfica del mapa de calor menos combinación entre los "
                                                              "puntos de diferentes formas y colores. Apóyate en la "
                                                              "matriz de confusión Tip 3 y en la precisión (Accuracy) "
                                                              "deberá acercarse a 1 tanto para datos de prueba como para entrenamiento")),
                                        id="collapse_tips_svm",
                                    ),
                                ]
                            ),
                            drc.NamedDropdown(
                                name='Kernel',
                                id='dropdown-svm-parameter-kernel',
                                options=[
                                    {'label': 'Función básica Radial (RBF)',
                                     'value': 'rbf'},
                                    {'label': 'Lineal', 'value': 'linear'},
                                    {'label': 'Polinomial', 'value': 'poly'},
                                    {'label': 'Sigmoid', 'value': 'sigmoid'}
                                ],
                                value='rbf',
                                clearable=False,
                                searchable=False
                            ),
                            html.Div(
                                [
                                    dbc.Button(
                                        "Tips 4",
                                        id="collapse_button_params",
                                        className="mb-3",
                                        color="primary",
                                    ),
                                    dbc.Collapse(
                                        dbc.Card(dbc.CardBody("Parametriza cada uno de los siguientes atributos"
                                                              " y verifica si la precisión se acerca a 1")),
                                        id="collapse_tips_params",
                                    ),
                                ]
                            ),
                            drc.NamedSlider(
                                name='Cost (C)',
                                id='slider-svm-parameter-C-power',
                                min=-2,
                                max=4,
                                value=0,
                                marks={i: '{}'.format(10 ** i) for i in
                                       range(-2, 5)}
                            ),

                            drc.FormattedSlider(
                                style={'padding': '5px 10px 25px'},
                                id='slider-svm-parameter-C-coef',
                                min=1,
                                max=9,
                                value=1
                            ),

                            drc.NamedSlider(
                                name='Degree',
                                id='slider-svm-parameter-degree',
                                min=2,
                                max=10,
                                value=3,
                                step=1,

                            ),

                            drc.NamedSlider(
                                name='Gamma',
                                id='slider-svm-parameter-gamma-power',
                                min=-5,
                                max=0,
                                value=-1,
                                marks={i: '{}'.format(10 ** i) for i in
                                       range(-5, 1)}
                            ),

                            drc.FormattedSlider(
                                style={'padding': '5px 10px 25px'},
                                id='slider-svm-parameter-gamma-coef',
                                min=1,
                                max=9,
                                value=5
                            ),

                            drc.NamedRadioItems(
                                name='Shrinking',
                                id='radio-svm-parameter-shrinking',
                                labelStyle={
                                    'margin-right': '7px',
                                    'display': 'inline-block'
                                },
                                options=[
                                    {'label': ' Enabled', 'value': 'True'},
                                    {'label': ' Disabled', 'value': 'False'},
                                ],
                                value='True',
                            ),
                        ]),

                    ]
                ),

        ])
