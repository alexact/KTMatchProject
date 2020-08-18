from dash.dependencies import Input, Output, State

from Layouts.app import app
from Controllers.statistics_controller import StatisticsController as StController



@app.callback(Output('output-data-uploads', 'children'),
              [Input('upload-datas', 'contents')],
              [State('upload-datas', 'filename'),
               State('upload-datas', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    """
    Actualización para la pestaña de estadistica básica y para el algoritmo SVM
    :param list_of_contents: data en base64
    :param list_of_names: nombre del archivo
    :param list_of_dates: fecha
    :return: retorna los valores de los parametro anteriores en un contenedor
    """
    if list_of_contents is not None:
        children = [
            StController().parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children



