import time
from sklearn import datasets
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from Model.data_model import DataModel
from Layouts.figures_svm_component import serve_prediction_plot, serve_roc_curve, \
    serve_pie_confusion_matrix
from Controllers.statistics_controller import StatisticsController as StController, initialization

from Layouts.app import app


@app.callback(Output('slider-svm-parameter-gamma-coef', 'marks'),
              [Input('slider-svm-parameter-gamma-power', 'value')])
def update_slider_svm_parameter_gamma_coef(power):
    scale = 10 ** power
    return {i: str(round(i * scale, 8)) for i in range(1, 10, 2)}


@app.callback(Output('slider-svm-parameter-C-coef', 'marks'),
              [Input('slider-svm-parameter-C-power', 'value')])
def update_slider_svm_parameter_C_coef(power):
    scale = 10 ** power
    return {i: str(round(i * scale, 8)) for i in range(1, 10, 2)}


@app.callback(Output('slider-threshold', 'value'),
              [Input('button-zero-threshold', 'n_clicks')],
              [State('graph-sklearn-svm', 'figure')])
def reset_threshold_center(n_clicks, figure):
    if n_clicks:
        Z = np.array(figure['data'][0]['z'])
        value = - Z.min( ) / (Z.max( ) - Z.min( ))
    else:
        value = 0.4959986285375595
    return value


# Disable Sliders if kernel not in the given list
@app.callback(Output('slider-svm-parameter-degree', 'disabled'),
              [Input('dropdown-svm-parameter-kernel', 'value')])
def disable_slider_param_degree(kernel):
    return kernel != 'poly'


@app.callback(Output('slider-svm-parameter-gamma-coef', 'disabled'),
              [Input('dropdown-svm-parameter-kernel', 'value')])
def disable_slider_param_gamma_coef(kernel):
    return kernel not in ['rbf', 'poly', 'sigmoid']


@app.callback(Output('slider-svm-parameter-gamma-power', 'disabled'),
              [Input('dropdown-svm-parameter-kernel', 'value')])
def disable_slider_param_gamma_power(kernel):
    return kernel not in ['rbf', 'poly', 'sigmoid']


@app.callback(Output('div-graphs', 'children'),
              [Input('dropdown-svm-parameter-kernel', 'value'),
               Input('slider-svm-parameter-degree', 'value'),
               Input('slider-svm-parameter-C-coef', 'value'),
               Input('slider-svm-parameter-C-power', 'value'),
               Input('slider-svm-parameter-gamma-coef', 'value'),
               Input('slider-svm-parameter-gamma-power', 'value'),
               Input('radio-svm-parameter-shrinking', 'value'),
               Input('slider-threshold', 'value'),
               Input('dropdown-svm-parameter-X', 'value'),
               Input('dropdown-svm-parameter-Y', 'value'),
               Input('output-data-uploads', 'children')
               ],
              [State('upload-datas', 'filename')])
def update_svm_graph(kernel,
                     degree,
                     C_coef,
                     C_power,
                     gamma_coef,
                     gamma_power,
                     shrinking,
                     threshold,
                     titleX,
                     titleY, update, filename
                     ):
    t_start = time.time( )
    h = .3  # step size in the mesh
    shrinking = bool(shrinking)
    # Data Pre-processing
    initialization( )
    # data = DataModel( )  # Se inicializa el objeto data
    # df_X = data.get_df_X( )  # se llama al al dataFrame que se encuentra en el update

    # LA DATA NO ESTÁ LLEGANDO PORQUE NO LAHE LLAMADO DESDE EL CONTROLLER FALTA HACER UN METODO O VARIABLE GLOBAL QUE LO HAGA

    df_X = StController.get_allData()
    print("Datafame", df_X.head(3))
    print(titleY in df_X.columns)
    print("Titulo a quitar del dataframe", titleY)
    if titleY in df_X.columns:
        print("si entro al def_X en svm callback")
        y = initialization.df_data[titleY]
        X = df_X.drop([titleY], axis=1)
    else:
        print("No entro al def_X en svm callback")
        dataset = datasets.make_moons(
            n_samples=200,
            noise=0.6,
            random_state=0
        )
        X, y = dataset
    # print(" xxxxx ",X, " yyyy ", y)
    X = StandardScaler( ).fit_transform(X)  # Requere que tenga una matriz con nejemplos y n columnas

    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=.4, random_state=42)

    x_min = X[:, 0].min( ) - .5
    x_max = X[:, 0].max( ) + .5
    y_min = X[:, 1].min( ) - .5
    y_max = X[:, 1].max( ) + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    C = C_coef * 10 ** C_power
    gamma = gamma_coef * 10 ** gamma_power

    # Train SVM
    clf = SVC(
        C=C,
        kernel=kernel,
        degree=degree,
        gamma=gamma,
        shrinking=shrinking
    )
    clf.fit(X_train, y_train)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    # print(np.c_[xx.ravel(), yy.ravel()])
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel( ), yy.ravel( )])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel( ), yy.ravel( )])[:, 1]

    prediction_figure = serve_prediction_plot(
        model=clf,
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        Z=Z,
        xx=xx,
        yy=yy,
        mesh_step=h,
        threshold=threshold
    )

    roc_figure = serve_roc_curve(
        model=clf,
        X_test=X_test,
        y_test=y_test
    )

    confusion_figure = serve_pie_confusion_matrix(
        model=clf,
        X_test=X_test,
        y_test=y_test,
        Z=Z,
        threshold=threshold
    )

    print(
        f"Total Time Taken: {time.time( ) - t_start:.3f} sec")

    return [
        html.Div(
            className='three columns',
            style={
                'min-width': '24.5%',
                'height': 'calc(100vh - 90px)',
                'margin-top': '5px',

                # Remove possibility to select the text for better UX
                'user-select': 'none',
                '-moz-user-select': 'none',
                '-webkit-user-select': 'none',
                '-ms-user-select': 'none'
            },
            children=[
                dcc.Graph(
                    id='graph-line-roc-curve',
                    style={'height': '40%'},
                    figure=roc_figure
                ),
                html.Div(
                    [
                        dbc.Button(
                            "Tips",
                            id="collapse-button_confusion-matrix",
                            className="mb-3",
                            color="primary",
                        ),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("Busca que los porcentajes de Verdadero Positivo y "
                                                  "Verdaderos Negativo sean los más altos")),
                            id="collapse_tips_confusion-matrix",
                        ),
                    ]
                ),
                dcc.Graph(
                    id='graph-pie-confusion-matrix',
                    figure=confusion_figure,
                    style={'height': '60%'}
                )
            ]),

        html.Div(
            className='six columns',
            style={'margin-top': '5px'},
            children=[
                dcc.Graph(
                    id='graph-sklearn-svm',
                    figure=prediction_figure,
                    style={'height': 'calc(100vh - 90px)'}
                )
            ])
    ]


# Callbacks collapse

@app.callback(
    Output("collapse_tips_svm", "is_open"),
    [Input("collapse-button_kernel", "n_clicks")],
    [State("collapse_tips_svm", "is_open")]
)
def toggle_collapse_kernel(n, is_open):
    print("isopen", is_open)
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse_tips_confusion-matrix", "is_open"),
    [Input("collapse-button_confusion-matrix", "n_clicks")],
    [State("collapse_tips_confusion-matrix", "is_open")]
)
def toggle_collapse_confusion_matrix(n, is_open):
    print("isopen2", is_open)
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("collapse_tips_variables", "is_open"),
    [Input("collapse-button_variables", "n_clicks")],
    [State("collapse_tips_variables", "is_open")]
)
def toggle_collapse_kernel(n, is_open):
    print("isopen", is_open)
    if n:
        return not is_open
    return is_open
