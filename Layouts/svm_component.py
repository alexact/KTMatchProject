import dash_core_components as dcc
import dash_html_components as html
import Layouts.components_view_svm as drc

layout_SVM = html.Div(id='body', className='container scalable', children=[
            html.Div(className='row', children=[
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
                            drc.NamedDropdown(
                                name='Kernel',
                                id='dropdown-svm-parameter-kernel',
                                options=[
                                    {'label': 'Radial basis function (RBF)',
                                     'value': 'rbf'},
                                    {'label': 'Linear', 'value': 'linear'},
                                    {'label': 'Polynomial', 'value': 'poly'},
                                    {'label': 'Sigmoid', 'value': 'sigmoid'}
                                ],
                                value='rbf',
                                clearable=False,
                                searchable=False
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
            ]),
        ])
